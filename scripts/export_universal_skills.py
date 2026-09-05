#!/usr/bin/env python3
"""Non-destructive complete-package or flattened-text export."""
import argparse
import hashlib
import json
import re
import shutil
from pathlib import Path
from library_paths import source_files, local_links, resolve_link

SOURCE_ROOT = Path(__file__).resolve().parents[1]

def skill_dirs(root, include_system=False):
    result = sorted(p for p in root.iterdir() if not p.name.startswith('.') and (p / 'SKILL.md').is_file())
    if include_system and (root / '.system').is_dir():
        result += sorted(p for p in (root / '.system').iterdir() if (p / 'SKILL.md').is_file())
    return result

def validate_destination(source, destination):
    source, destination = source.resolve(), destination.expanduser().resolve()
    if source == destination or source in destination.parents or destination in source.parents:
        raise ValueError('Export destination must not overlap the source tree (including symlinks).')
    if destination.exists():
        raise ValueError('Export destination already exists; choose a new directory.')
    return destination

def flatten_skill_content(package, root):
    pending = [package / 'SKILL.md', *source_files(package)]
    contract_path = root / 'routing-contracts.json'
    contracts = json.loads(contract_path.read_text())['skills'] if contract_path.exists() else {}
    content, binary, runtime = {}, set(), set()
    while pending:
        path = pending.pop(0).resolve()
        if path in content or path in binary:
            continue
        if root not in path.parents:
            raise ValueError(f'External file dependency is not exportable: {path}')
        if not path.is_file():
            continue
        try:
            text = path.read_text(encoding='utf-8')
        except UnicodeDecodeError:
            binary.add(path)
            continue
        content[path] = text
        if path.name == 'SKILL.md':
            for dependency in contracts.get(path.parent.name, {}).get('dependencies', []):
                dependency_root = root / dependency
                if not (dependency_root / 'SKILL.md').is_file():
                    raise ValueError(f'Missing named export dependency: {dependency}')
                pending.extend(source_files(dependency_root))
        if path.suffix in {'.py', '.sh', '.js', '.ts'}:
            runtime.add(path)
        owner = next((p for p in path.parents if (p / 'SKILL.md').is_file()), package)
        for link in local_links(text):
            if link.startswith(('/', '~', '$')):
                raise ValueError(f'Nonportable local dependency: {path}: {link}')
            target = resolve_link(path, link, owner)
            if not target.exists():
                raise ValueError(f'Broken export dependency: {path}: {link}')
            if target.is_dir():
                raise ValueError(f'Directory link unsupported in flattened format; link specific files: {path}: {link}')
            pending.append(target)
    def anchor(path):
        return 'file-' + hashlib.sha256(str(path.relative_to(root)).encode()).hexdigest()[:16]
    parts = ['# ' + package.name, '', 'Flattened text reference. Scripts are listings, not executable installations.',
             'Binary assets and tool/runtime dependencies require the complete folder export.', '']
    for path, text in content.items():
        owner = next((p for p in path.parents if (p / 'SKILL.md').is_file()), package)
        def rewrite(match):
            target = resolve_link(path, match[2].strip('<>').split('#', 1)[0], owner)
            return f'[{match[1]}](#{anchor(target)})' if target in content else match[0]
        if path.suffix == '.md':
            text = re.sub(r'\[([^\]]*)\]\(([^)]+)\)', rewrite, text)
            for name in contracts:
                target = (root / name / 'SKILL.md').resolve()
                if target in content:
                    for token in (name, '$' + name):
                        text = text.replace(chr(96) + token + chr(96), '[' + token + '](#' + anchor(target) + ')')
            for link in local_links(text):
                target = resolve_link(path, link, owner)
                if target in content:
                    text = text.replace(chr(96) + link + chr(96), '[' + link + '](#' + anchor(target) + ')')
        else:
            fence = chr(96) * max(3, max((len(x) + 1 for x in re.findall(chr(96) + '+', text)), default=3))
            text = fence + '\n' + text + '\n' + fence
        parts += [f'<a id="{anchor(path)}"></a>', f'## {path.relative_to(root)}', '', text, '']
    parts += ['## Non-inline dependencies', '', 'Host tools, connectors, credentials and interpreter versions are not bundled.']
    parts += [f'- Binary: {p.relative_to(root)}' for p in sorted(binary)]
    parts += [f'- Runtime script (listing only): {p.relative_to(root)}' for p in sorted(runtime)]
    return '\n'.join(parts) + '\n'

def export_skills(destination, include_system=False, flatten=False, source_root=SOURCE_ROOT):
    root = source_root.resolve()
    destination = validate_destination(root, destination)
    packages = skill_dirs(root, include_system)
    if len({p.name for p in packages}) != len(packages):
        raise ValueError('Duplicate package names across local/system packages.')
    files = [p for p in source_files(root) if '.system' not in p.relative_to(root).parts or include_system]
    for path in root.rglob('*'):
        if path.is_symlink() and path.is_dir() and ('.system' not in path.relative_to(root).parts or include_system):
            raise ValueError(f'Directory symlink unsupported; materialize a safe copy first: {path}')
    for path in files:
        if root not in path.resolve().parents:
            raise ValueError(f'Source symlink escapes checkout: {path}')
    flattened = {p.name: flatten_skill_content(p, root) for p in packages} if flatten else {}
    destination.mkdir(parents=True, exist_ok=False)
    if flatten:
        exported = []
        for name, text in flattened.items():
            target = destination / (name + '.md')
            target.write_text(text)
            exported.append(target)
    else:
        for path in files:
            if len(path.relative_to(root).parts) == 1 and path.name in {'skills.catalog.json', 'skills.manifest.json', 'stocktake.report.md', 'usage-review.report.md'}:
                continue
            target = destination / path.relative_to(root)
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(path, target)
        exported = [destination / p.relative_to(root) for p in packages]
    (destination / 'export.manifest.json').write_text(json.dumps({
        'source_root': str(root), 'flatten': flatten, 'include_system': include_system,
        'export_count': len(exported), 'exports': [str(p.relative_to(destination)) for p in exported],
        'limitations': ['Text flattening does not install runtimes, tools, credentials or binary assets.'] if flatten else [],
    }, indent=2) + '\n')
    return exported

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('destination', type=Path)
    parser.add_argument('--source', type=Path, default=SOURCE_ROOT)
    parser.add_argument('--include-system', action='store_true')
    parser.add_argument('--flatten', action='store_true')
    args = parser.parse_args()
    try:
        exported = export_skills(args.destination, args.include_system, args.flatten, args.source)
    except (ValueError, OSError) as exc:
        parser.exit(1, f'Export refused: {exc}\n')
    print(f'Exported {len(exported)} packages; flattened exports disclose non-inline dependencies.')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
