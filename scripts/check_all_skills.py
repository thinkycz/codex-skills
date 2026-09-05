#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

from generate_skill_catalog import compute_source_fingerprint


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
CATALOG_PATH = ROOT / "skills.catalog.json"
STOCKTAKE_PATH = ROOT / "stocktake.report.md"
USAGE_REVIEW_PATH = ROOT / "usage-review.report.md"


def run_step(label: str, command: list[str]) -> None:
    print(f"\n== {label} ==")
    result = subprocess.run(command, cwd=ROOT)
    if result.returncode != 0:
        raise SystemExit(result.returncode)


def validate_generated_reports() -> None:
    catalog = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
    skill_count = int(catalog["skill_count"])
    stocktake = STOCKTAKE_PATH.read_text(encoding="utf-8")
    usage = USAGE_REVIEW_PATH.read_text(encoding="utf-8")
    match = re.search(r"Local skills reviewed: `(\d+)`", stocktake)
    if not match:
        raise SystemExit("stocktake.report.md is missing the local skill count")
    reviewed = int(match.group(1))
    if reviewed != skill_count:
        raise SystemExit(
            f"stocktake local skill count ({reviewed}) does not match catalog skill_count ({skill_count})"
        )
    if "Fixture Coverage By Cluster" not in usage:
        raise SystemExit("usage-review.report.md is missing fixture coverage")
    if "Observed Conversation Evidence" not in usage:
        raise SystemExit("usage-review.report.md is missing observed conversation evidence")
    if "Recorded Behavioral Evaluations" not in usage:
        raise SystemExit("usage-review.report.md is missing behavioral evaluation status")
    fingerprint = str(catalog.get("source_fingerprint", ""))
    if not fingerprint:
        raise SystemExit("skills.catalog.json is missing source_fingerprint")
    if fingerprint not in stocktake or fingerprint not in usage:
        raise SystemExit("generated reports do not contain the catalog source fingerprint")
    print(f"Generated reports are internally consistent for {skill_count} skill(s).")


def validate_generated_freshness() -> None:
    catalog = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
    recorded = str(catalog.get("source_fingerprint", ""))
    current = compute_source_fingerprint()
    if recorded != current:
        raise SystemExit(
            "Generated skill artifacts are stale. Run python3 ~/.agents/skills/scripts/check_all_skills.py."
        )
    print(f"Generated artifacts match source fingerprint {current}.")


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate and regenerate the editable skill library.")
    parser.add_argument(
        "--check-generated",
        action="store_true",
        help="Check current generated artifacts without rewriting them.",
    )
    args = parser.parse_args()
    py = sys.executable
    run_step("validate skills", [py, str(SCRIPTS / "validate_skills.py")])
    run_step("static routing boundaries (no model execution)", [py, str(SCRIPTS / "check_skill_routing.py")])
    run_step("behavior scenario and recorded-evidence validation", [py, str(SCRIPTS / "check_skill_behavior.py")])
    run_step("behavior evidence checker regression tests", [py, str(SCRIPTS / "test_skill_behavior.py")])
    run_step("mirror parity", [py, str(SCRIPTS / "check_mirror_parity.py")])
    if args.check_generated:
        print("\n== validate generated reports ==")
        validate_generated_reports()
        print("\n== validate generated freshness ==")
        validate_generated_freshness()
        print("\nAll skill checks passed without rewriting generated artifacts.")
        return 0
    run_step("generate catalog", [py, str(SCRIPTS / "generate_skill_catalog.py")])
    run_step("generate stocktake", [py, str(SCRIPTS / "generate_stocktake_report.py")])
    run_step("generate usage review", [py, str(SCRIPTS / "generate_usage_review.py")])
    run_step("validate skills after generation", [py, str(SCRIPTS / "validate_skills.py")])
    print("\n== validate generated reports ==")
    validate_generated_reports()
    print("\n== validate generated freshness ==")
    validate_generated_freshness()
    print("\nAll skill checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
