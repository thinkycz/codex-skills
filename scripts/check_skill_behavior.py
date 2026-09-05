#!/usr/bin/env python3
"""Validate scenarios and recorded evaluations; never execute or grade a model."""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCENARIOS = ROOT / "scripts/fixtures/skill-behavior-scenarios.json"
RESULTS = ROOT / "scripts/fixtures/skill-behavior-results.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def nonempty(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def validate_scenarios(data: dict, root: Path = ROOT) -> list[dict]:
    require(isinstance(data, dict), "scenario document must be an object")
    require(data.get("schema_version") == 1, "unsupported scenario schema")
    scenarios = data.get("scenarios")
    require(isinstance(scenarios, list) and bool(scenarios), "scenarios must be a nonempty list")
    ids: set[str] = set()
    for s in scenarios:
        require(isinstance(s, dict), "scenario must be an object")
        sid = s.get("id")
        require(nonempty(sid) and sid not in ids, "missing or duplicate scenario id")
        ids.add(sid)
        require(nonempty(s.get("prompt")), f"{sid}: missing prompt")
        skills = s.get("skills")
        require(isinstance(skills, list) and bool(skills), f"{sid}: missing skill sources")
        for skill in skills:
            require(nonempty(skill) and Path(skill).name == skill and skill not in (".", ".."), f"{sid}: invalid skill name")
            require((root / skill / "SKILL.md").is_file(), f"{sid}: missing skill {skill}")
        require(s.get("expected_owner") in skills, f"{sid}: expected owner absent from sources")
        keys: set[str] = set()
        for group in ("required_actions", "prohibited_actions"):
            actions = s.get(group)
            require(isinstance(actions, dict) and bool(actions), f"{sid}: missing {group}")
            for key, instruction in actions.items():
                require(nonempty(key) and key not in keys and nonempty(instruction), f"{sid}: invalid or duplicate assertion")
                keys.add(key)
    return scenarios


def source_fingerprint(scenario: dict, root: Path = ROOT) -> str:
    """Bind each evaluation to its scenario and the complete declared skill packages."""
    digest = hashlib.sha256(json.dumps(scenario, sort_keys=True).encode())
    for skill in sorted(set(scenario["skills"])):
        for path in sorted((root / skill).rglob("*")):
            if not path.is_file() or "__pycache__" in path.parts:
                continue
            digest.update(str(path.relative_to(root)).encode())
            digest.update(b"\0")
            digest.update(path.read_bytes())
            digest.update(b"\0")
    return digest.hexdigest()


def assess(scenarios: list[dict], data: dict | None, root: Path = ROOT) -> dict[str, str]:
    by_id = {s["id"]: s for s in scenarios}
    states = {sid: "not_run" for sid in by_id}
    if data is None:
        return states
    require(isinstance(data, dict), "result document must be an object")
    require(data.get("schema_version") == 1, "unsupported result schema")
    records = data.get("evaluations")
    require(isinstance(records, list), "evaluations must be a list")
    seen: set[str] = set()
    for record in records:
        require(isinstance(record, dict), "evaluation must be an object")
        sid = record.get("scenario_id")
        require(sid in by_id and sid not in seen, "unknown or duplicate evaluation scenario")
        seen.add(sid)
        s = by_id[sid]
        for field in ("evaluator", "evaluated_at", "source_fingerprint", "response", "reviewer"):
            require(nonempty(record.get(field)), f"{sid}: missing {field}")
        timestamp = datetime.fromisoformat(record["evaluated_at"].replace("Z", "+00:00"))
        require(timestamp.tzinfo is not None, f"{sid}: evaluated_at needs timezone")
        require(record.get("method") in ("independent-dry-run", "observed-execution"), f"{sid}: invalid evaluation method")
        status = record.get("status")
        require(status in ("passed", "failed", "blocked"), f"{sid}: invalid recorded status")
        require(nonempty(record.get("observed_owner")), f"{sid}: missing observed owner")
        if status == "blocked":
            require(nonempty(record.get("blocker")), f"{sid}: blocked evaluation needs reason")
        else:
            checks = record.get("checks")
            require(isinstance(checks, dict), f"{sid}: missing assessment checks")
            expected = set(s["required_actions"]) | set(s["prohibited_actions"])
            require(set(checks) == expected, f"{sid}: missing or unknown assertion assessments")
            for key, check in checks.items():
                require(isinstance(check, dict) and type(check.get("passed")) is bool, f"{sid}/{key}: assessment needs boolean passed")
                require(nonempty(check.get("evidence")), f"{sid}/{key}: missing response evidence")
                require(check["evidence"] in record["response"], f"{sid}/{key}: evidence must quote the recorded response")
            derived = "passed" if record["observed_owner"] == s["expected_owner"] and all(c["passed"] for c in checks.values()) else "failed"
            require(status == derived, f"{sid}: status contradicts recorded assessments or owner")
        states[sid] = status if record["source_fingerprint"] == source_fingerprint(s, root) else "stale"
    return states


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--scenarios", type=Path, default=SCENARIOS)
    parser.add_argument("--results", type=Path, default=RESULTS)
    parser.add_argument("--require-evaluated", action="store_true", help="Fail unless every scenario has a current recorded passing evaluation.")
    args = parser.parse_args()
    try:
        scenarios = validate_scenarios(json.loads(args.scenarios.read_text()))
        data = json.loads(args.results.read_text()) if args.results.exists() else None
        states = assess(scenarios, data)
    except (ValueError, OSError, TypeError, KeyError) as exc:
        print(f"Behavior evidence validation failed: {exc}")
        return 1
    print(f"Behavioral scenario definitions valid: {len(scenarios)}")
    for sid, state in states.items():
        print(f"  {sid}: {state}")
    print("Recorded evaluations only. This checker does not run a model or independently judge its behavior.")
    if any(s == "failed" for s in states.values()):
        return 1
    if args.require_evaluated and any(s != "passed" for s in states.values()):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
