#!/usr/bin/env python3

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FIXTURES_PATH = ROOT / "scripts" / "fixtures" / "skill-routing-fixtures.json"


def load_checks() -> list[dict[str, object]]:
    payload = json.loads(FIXTURES_PATH.read_text(encoding="utf-8"))
    checks: list[dict[str, object]] = []
    for cluster in payload["clusters"]:
        for skill in cluster["skills"]:
            checks.append(
                {
                    "cluster": cluster["name"],
                    "skill": skill["id"],
                    "required_mentions": skill["required_mentions"],
                    "fixtures": skill["fixtures"],
                }
            )
    return checks


def main() -> int:
    failures = 0
    print("Skill routing boundary check")
    print()
    for check in load_checks():
        skill_path = ROOT / check["skill"] / "SKILL.md"
        text = skill_path.read_text(encoding="utf-8")
        missing = [needle for needle in check["required_mentions"] if needle not in text]
        print(f"[{check['cluster']}] {check['skill']}")
        for fixture in check["fixtures"]:
            print(f"  fixture: {fixture['prompt']}")
            print(f"  expected owner: {fixture['expected_owner']}")
        if missing:
            failures += 1
            print(f"  ERROR: missing boundary mention(s): {', '.join(missing)}")
        else:
            print("  OK: boundary mentions present")
        print()

    if failures:
        print(f"Routing checks failed for {failures} skill(s).")
        return 1
    print("All routing boundary checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
