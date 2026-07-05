#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path


SOURCE_ROOT = Path("/Users/longdo/.agents/skills")
TEXT_SUFFIXES = {
    ".md": "markdown",
    ".yaml": "yaml",
    ".yml": "yaml",
    ".json": "json",
    ".py": "python",
    ".js": "javascript",
    ".ts": "typescript",
    ".sh": "bash",
    ".txt": "text",
    ".svg": "xml",
}


def parse_frontmatter(skill_path: Path) -> dict[str, object]:
    lines = skill_path.read_text(encoding="utf-8").splitlines()
    if len(lines) < 3 or lines[0].strip() != "---":
        return {}
    try:
        end_index = lines[1:].index("---") + 1
    except ValueError:
        return {}

    data: dict[str, object] = {}
    current_list_key: str | None = None
    for raw_line in lines[1:end_index]:
        line = raw_line.rstrip()
        if not line:
            continue
        stripped = line.lstrip()
        if stripped.startswith("- "):
            if current_list_key:
                data.setdefault(current_list_key, []).append(stripped[2:].strip())
            continue
        if ":" not in line:
            current_list_key = None
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if not value:
            data[key] = []
            current_list_key = key
            continue
        data[key] = value.strip("\"'")
        current_list_key = None
    return data


def iter_skill_dirs(include_system: bool) -> list[Path]:
    skill_dirs: list[Path] = []
    for child in sorted(SOURCE_ROOT.iterdir()):
        if child.name == ".system":
            if not include_system:
                continue
            for nested in sorted(child.iterdir()):
                if (nested / "SKILL.md").is_file():
                    skill_dirs.append(nested)
            continue
        if child.name.startswith(".") or child.name == "scripts":
            continue
        if (child / "SKILL.md").is_file():
            skill_dirs.append(child)
    return skill_dirs


def is_text_file(path: Path) -> bool:
    try:
        path.read_text(encoding="utf-8")
        return True
    except UnicodeDecodeError:
        return False


def fence_language(path: Path) -> str:
    return TEXT_SUFFIXES.get(path.suffix.lower(), "text")


def flatten_skill_content(skill_dir: Path, exported_at: str, include_system: bool) -> str:
    skill_text = (skill_dir / "SKILL.md").read_text(encoding="utf-8").rstrip() + "\n"
    frontmatter = parse_frontmatter(skill_dir / "SKILL.md")
    companion_files = sorted(
        p for p in skill_dir.rglob("*") if p.is_file() and p.name != "SKILL.md"
    )

    metadata_lines = [
        "---",
        "",
        "## Export Metadata",
        "",
        f"- Exported at: `{exported_at}`",
        f"- Source root: `{SOURCE_ROOT}`",
        f"- Source skill path: `{skill_dir}`",
        f"- Source type: `{'system' if '.system' in skill_dir.parts else 'local'}`",
        f"- Skill version: `{frontmatter.get('version', 'unknown')}`",
        f"- Flattened export: `true`",
        f"- Included system skills: `{'true' if include_system else 'false'}`",
        "",
    ]

    if not companion_files:
        return "\n".join([skill_text.rstrip(), *metadata_lines, ""])

    text_parts: list[str] = [
        skill_text.rstrip(),
        "",
        *metadata_lines,
        "## Inlined Companion Files",
        "",
        "This flattened export inlines companion files from the original skill package.",
        "",
    ]
    binary_files: list[Path] = []

    for path in companion_files:
        rel = path.relative_to(skill_dir)
        if is_text_file(path):
            content = path.read_text(encoding="utf-8").rstrip()
            text_parts.extend(
                [
                    f"### `{rel.as_posix()}`",
                    "",
                    f"```{fence_language(path)}",
                    content,
                    "```",
                    "",
                ]
            )
        else:
            binary_files.append(rel)

    if binary_files:
        text_parts.extend(["## Binary Assets", ""])
        for rel in binary_files:
            text_parts.append(f"- `{rel.as_posix()}`")
        text_parts.append("")

    return "\n".join(text_parts)


def write_export_manifest(
    destination: Path,
    exported_paths: list[Path],
    include_system: bool,
    flatten: bool,
    exported_at: str,
) -> None:
    entries: list[dict[str, object]] = []
    for path in exported_paths:
        if flatten:
            skill_name = path.stem
            source_path = next(
                skill_dir for skill_dir in iter_skill_dirs(include_system=include_system) if skill_dir.name == skill_name
            )
            frontmatter = parse_frontmatter(source_path / "SKILL.md")
            entries.append(
                {
                    "id": skill_name,
                    "output": str(path),
                    "source": str(source_path),
                    "version": frontmatter.get("version", "unknown"),
                }
            )
        else:
            source_path = next(
                skill_dir for skill_dir in iter_skill_dirs(include_system=include_system) if skill_dir.name == path.name
            )
            frontmatter = parse_frontmatter(source_path / "SKILL.md")
            entries.append(
                {
                    "id": path.name,
                    "output": str(path),
                    "source": str(source_path),
                    "version": frontmatter.get("version", "unknown"),
                }
            )

    manifest = {
        "generated_at": exported_at,
        "source_root": str(SOURCE_ROOT),
        "destination": str(destination),
        "flatten": flatten,
        "include_system": include_system,
        "export_count": len(entries),
        "exports": entries,
    }
    (destination / "export.manifest.json").write_text(
        json.dumps(manifest, indent=2) + "\n",
        encoding="utf-8",
    )


def export_skills(destination: Path, include_system: bool, flatten: bool) -> list[Path]:
    exported: list[Path] = []
    destination.mkdir(parents=True, exist_ok=True)
    exported_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    skill_dirs = iter_skill_dirs(include_system=include_system)

    for skill_dir in skill_dirs:
        if flatten:
            target_file = destination / f"{skill_dir.name}.md"
            if target_file.exists():
                target_file.unlink()
            target_file.write_text(
                flatten_skill_content(skill_dir, exported_at=exported_at, include_system=include_system),
                encoding="utf-8",
            )
            exported.append(target_file)
        else:
            target_dir = destination / skill_dir.name
            if target_dir.exists():
                shutil.rmtree(target_dir)
            target_dir.mkdir(parents=True)
            shutil.copy2(skill_dir / "SKILL.md", target_dir / "SKILL.md")
            exported.append(target_dir)

    write_export_manifest(destination, exported, include_system, flatten, exported_at)
    return exported


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Export Codex skills into universal folder or flattened markdown layouts."
    )
    parser.add_argument(
        "destination",
        nargs="?",
        default=".",
        help="Where to write the exported universal skill folders",
    )
    parser.add_argument(
        "--exclude-system",
        action="store_true",
        help="Skip vendor-managed skills under .system",
    )
    parser.add_argument(
        "--flatten",
        action="store_true",
        help="Export each skill as a single <skill-name>.md file in the destination.",
    )
    args = parser.parse_args()

    destination = Path(args.destination).expanduser().resolve()
    exported = export_skills(
        destination,
        include_system=not args.exclude_system,
        flatten=args.flatten,
    )

    layout = "flattened files" if args.flatten else "skill folders"
    print(f"Exported {len(exported)} skills to {destination} as {layout}")
    for path in exported:
        print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
