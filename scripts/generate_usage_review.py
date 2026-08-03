#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = ROOT / "skills.catalog.json"
FIXTURES_PATH = ROOT / "scripts" / "fixtures" / "skill-routing-fixtures.json"
REPORT_PATH = ROOT / "usage-review.report.md"
TEMPLATE_PATH = ROOT / "templates" / "usage-review-template.md"
DEFAULT_EVIDENCE_PATH = ROOT / "scripts" / "fixtures" / "skill-usage-evidence.json"


def load_json(path: Path) -> dict[str, object]:
    if not path.exists():
        raise SystemExit(f"Missing required artifact: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def top_owner_skills(skills: list[dict[str, object]], limit: int = 5) -> list[dict[str, object]]:
    owner_categories = {"execution", "orchestration", "product-design", "design-quality", "quality", "skill-ops"}
    relevant = [skill for skill in skills if skill["category"] in owner_categories]
    return sorted(relevant, key=lambda item: int(item.get("skill_md_lines", 0)), reverse=True)[:limit]


def cluster_summaries(fixtures: dict[str, object]) -> list[str]:
    lines: list[str] = []
    for cluster in fixtures["clusters"]:
        fixture_count = sum(len(skill["fixtures"]) for skill in cluster["skills"])
        lines.append(f"- `{cluster['name']}`: {fixture_count} fixture(s)")
    return lines


def sample_prompts(fixtures: dict[str, object], limit: int = 6) -> list[str]:
    samples: list[str] = []
    for cluster in fixtures["clusters"]:
        for skill in cluster["skills"]:
            for fixture in skill["fixtures"]:
                samples.append(f"- `{skill['id']}`: {fixture['prompt']}")
                if len(samples) >= limit:
                    return samples
    return samples


def observed_evidence_lines(evidence: dict[str, object] | None) -> list[str]:
    if not evidence:
        return ["- No observed conversation evidence was provided."]

    metric_labels = {
        "threads_reviewed": "Recent conversations reviewed",
        "codex_threads": "Codex threads in the review window",
        "detailed_codex_threads": "Prior Codex threads inspected in detail",
        "turns_reviewed": "Detailed turns reviewed",
        "completed_turns": "Completed detailed turns",
        "context_compactions": "Context compactions",
        "multi_skill_turns": "Turns mentioning four or more workflow skills",
        "browser_defects_caught": "Real defects first caught by browser or rendered-artifact checks",
        "full_gate_defects_caught": "Late defects first caught by the full repository gate",
        "environment_blocker_mentions": "Turns mentioning environment-only blockers",
    }
    lines = [f"- Evidence window: `{evidence.get('reviewed_at', 'unknown')}`"]
    for key, label in metric_labels.items():
        if key in evidence:
            lines.append(f"- {label}: `{evidence[key]}`")
    return lines


def observed_skill_lines(evidence: dict[str, object] | None) -> list[str]:
    if not evidence:
        return ["- No observed skill-mention counts were provided."]
    mentions = evidence.get("skill_turn_mentions", {})
    if not isinstance(mentions, dict) or not mentions:
        return ["- No observed skill-mention counts were provided."]
    return [
        f"- `{skill}`: {count} turn(s)"
        for skill, count in sorted(mentions.items(), key=lambda item: (-int(item[1]), item[0]))
    ]


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate a skill usage review from catalog, fixtures, and optional observed evidence.")
    parser.add_argument(
        "--evidence",
        type=Path,
        default=DEFAULT_EVIDENCE_PATH,
        help="JSON file containing aggregate, sanitized conversation evidence.",
    )
    args = parser.parse_args()
    catalog = load_json(CATALOG_PATH)
    fixtures = load_json(FIXTURES_PATH)
    evidence = load_json(args.evidence) if args.evidence.exists() else None
    generated_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    skills = [skill for skill in catalog["skills"] if skill["source_type"] == "local"]

    report = "\n".join(
        [
            "# Skill Usage Review",
            "",
            f"- Generated at: `{generated_at}`",
            f"- Catalog source: `{CATALOG_PATH}`",
            f"- Fixture source: `{FIXTURES_PATH}`",
            f"- Evidence source: `{args.evidence if evidence else 'not provided'}`",
            f"- Source fingerprint: `{catalog.get('source_fingerprint', 'missing')}`",
            f"- Review template: `{TEMPLATE_PATH}`",
            "",
            "## Observed Conversation Evidence",
            "",
            *observed_evidence_lines(evidence),
            "",
            "## Observed Skill Mentions",
            "",
            *observed_skill_lines(evidence),
            "",
            "## Current Priorities",
            "",
            *[
                f"- `{skill['id']}`: {skill.get('skill_md_lines', 0)} lines, {skill.get('references_count', 0)} reference file(s)"
                for skill in top_owner_skills(skills)
            ],
            "",
            "## Fixture Coverage By Cluster",
            "",
            *cluster_summaries(fixtures),
            "",
            "## Sample Realistic Prompts",
            "",
            *(sample_prompts(fixtures) or ["- No sample prompts found."]),
            "",
            "## Review Cadence",
            "",
            "- After a real project or substantial thread, open the usage-review template and capture any routing near-misses.",
            "- Store only aggregate, sanitized evidence; do not preserve client prompts, private paths, secrets, or project-specific memory.",
            "- Add only the prompts that taught a new routing distinction or exposed a missing handoff.",
            "- Regenerate the routing check, catalog, stocktake, and usage review after meaningful additions.",
            "",
            "## Commands",
            "",
            "- `python3 ~/.agents/skills/scripts/check_skill_routing.py`",
            "- `python3 ~/.agents/skills/scripts/generate_skill_catalog.py`",
            "- `python3 ~/.agents/skills/scripts/generate_stocktake_report.py`",
            "- `python3 ~/.agents/skills/scripts/generate_usage_review.py`",
            "",
        ]
    )
    REPORT_PATH.write_text(report + "\n", encoding="utf-8")
    print(REPORT_PATH)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
