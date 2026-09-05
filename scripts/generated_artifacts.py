"""Compute and compare generated artifacts without writing any library files."""
import json
import re
from pathlib import Path
import generate_skill_catalog as catalog
from generate_stocktake_report import render_report as stocktake
from generate_usage_review import render_report as usage

ROOT = Path(__file__).resolve().parents[1]

def expected_artifacts():
    data, manifest = catalog.main([], emit=False)
    return {'skills.catalog.json': data, 'skills.manifest.json': manifest,
            'stocktake.report.md': stocktake(data), 'usage-review.report.md': usage(data, [])}

def semantic(value):
    if isinstance(value, dict):
        return {k: semantic(v) for k, v in value.items() if k != 'generated_at'}
    if isinstance(value, list):
        return [semantic(v) for v in value]
    if isinstance(value, str):
        return re.sub(r'^- Generated at:.*\n', '', value, flags=re.M)
    return value

def check_generated(root=ROOT, expected=None):
    errors = []
    for name, value in (expected_artifacts() if expected is None else expected).items():
        path = root / name
        if not path.is_file():
            errors.append(f'missing: {name}')
            continue
        try:
            actual = json.loads(path.read_text()) if name.endswith('.json') else path.read_text()
            if semantic(actual) != semantic(value):
                errors.append(f'stale or tampered: {name}')
        except (ValueError, OSError) as exc:
            errors.append(f'invalid: {name}: {exc}')
    return errors

def generate():
    for name, value in expected_artifacts().items():
        (ROOT / name).write_text(json.dumps(value, indent=2) + '\n' if isinstance(value, dict) else value)
