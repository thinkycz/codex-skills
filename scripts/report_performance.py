#!/usr/bin/env python3
"""Measure actual declared instruction loads from paired independent dry-run records."""
import argparse
import hashlib
import json
import statistics
from pathlib import Path
from generate_skill_catalog import parse_frontmatter

def library_metrics(root):
    mains = sorted(root.glob('*/SKILL.md'))
    return {'skill_count': len(mains), 'main_words': sum(len(p.read_text().split()) for p in mains),
            'discovery_description_words': sum(len(str(parse_frontmatter(p)['description']).split()) for p in mains)}

def record_metrics(root, record):
    files = record.get('loaded_files')
    if not isinstance(files, list) or not files:
        raise ValueError('Missing confirmed load inventory; do not substitute mentions or zero.')
    if len(files) != len(set(files)):
        raise ValueError('Per-case load inventory must identify unique files; repeated tool reads are separate telemetry.')
    main, refs = 0, 0
    sources = {}
    resolved = set()
    for name in files:
        path = (root / name).resolve()
        if path in resolved:
            raise ValueError(f'Duplicate resolved instruction source: {name}')
        resolved.add(path)
        if root.resolve() not in path.parents or not path.is_file():
            raise ValueError(f'Invalid loaded source: {name}')
        data = path.read_bytes()
        sources[name] = hashlib.sha256(data).hexdigest()
        words = len(data.decode('utf-8').split())
        if path.name == 'SKILL.md':
            main += words
        else:
            refs += words
    return {'main_words': main, 'selected_reference_words': refs,
            'instruction_words': main + refs, 'skill_reads': sum(Path(p).name == 'SKILL.md' for p in files),
            'reference_reads': sum(Path(p).name != 'SKILL.md' for p in files), 'source_hashes': sources,
            'latency_ms': record.get('latency_ms'), 'tokens': record.get('tokens')}

def compare(baseline_root, revised_root, baseline_runs, revised_runs):
    variants = {}
    for name, root, runs in [('baseline', baseline_root, baseline_runs), ('revised', revised_root, revised_runs)]:
        records = {}
        for run in runs:
            payload = json.loads(run.read_text())
            for record in payload['records']:
                key = f"{payload['run']}/{record['case_id']}"
                if key in records:
                    raise ValueError(f'Duplicate case/run: {key}')
                records[key] = record_metrics(root, record)
        variants[name] = {**library_metrics(root), 'records': records}
    keys = set(variants['baseline']['records'])
    if keys != set(variants['revised']['records']) or not keys:
        raise ValueError('Matched case/run records required for both variants.')
    for name, values in variants.items():
        values['median_loaded_words'] = statistics.median(r['instruction_words'] for r in values['records'].values())
        values['median_skill_reads'] = statistics.median(r['skill_reads'] for r in values['records'].values())
        values['median_with_discovery_words'] = values['median_loaded_words'] + values['discovery_description_words']
    reduction = 1 - variants['revised']['median_loaded_words'] / variants['baseline']['median_loaded_words']
    return {'schema_version': 1, 'variants': variants, 'median_loaded_reduction': reduction,
            'matched_case_runs': len(keys), 'load_telemetry': 'Evaluator-recorded files actually consulted; not historical mentions.',
            'timing_and_tokens': 'Unknown unless recorded; word reduction does not prove task latency improvement.'}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--baseline', type=Path, required=True)
    parser.add_argument('--revised', type=Path, required=True)
    parser.add_argument('--baseline-runs', type=Path, nargs='+', required=True)
    parser.add_argument('--revised-runs', type=Path, nargs='+', required=True)
    parser.add_argument('--output', type=Path, help='Write the measured report to this explicit file.')
    args = parser.parse_args()
    report = compare(args.baseline, args.revised, args.baseline_runs, args.revised_runs)
    rendered = json.dumps(report, indent=2) + '\n'
    if args.output:
        args.output.write_text(rendered)
        print(f'Matched runs: {report["matched_case_runs"]}; median loaded reduction: {report["median_loaded_reduction"]:.1%}')
    else:
        print(rendered)

if __name__ == '__main__':
    main()
