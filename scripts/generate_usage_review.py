#!/usr/bin/env python3

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = ROOT / "skills.catalog.json"
FIXTURES_PATH = ROOT / "scripts" / "fixtures" / "skill-routing-fixtures.json"
REPORT_PATH = ROOT / "usage-review.report.md"
TEMPLATE_PATH = ROOT / "templates" / "usage-review-template.md"


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


def main() -> int:
    catalog = load_json(CATALOG_PATH)
    fixtures = load_json(FIXTURES_PATH)
    generated_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    skills = [skill for skill in catalog["skills"] if skill["source_type"] == "local"]

    report = "\n".join(
        [
            "# Skill Usage Review",
            "",
            f"- Generated at: `{generated_at}`",
            f"- Catalog source: `{CATALOG_PATH}`",
            f"- Fixture source: `{FIXTURES_PATH}`",
            f"- Review template: `{TEMPLATE_PATH}`",
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
            "- Add only the prompts that taught a new routing distinction or exposed a missing handoff.",
            "- Regenerate the routing check, catalog, stocktake, and usage review after meaningful additions.",
            "",
            "## Commands",
            "",
            "- `python3 /Users/longdo/.agents/skills/scripts/check_skill_routing.py`",
            "- `python3 /Users/longdo/.agents/skills/scripts/generate_skill_catalog.py`",
            "- `python3 /Users/longdo/.agents/skills/scripts/generate_stocktake_report.py`",
            "- `python3 /Users/longdo/.agents/skills/scripts/generate_usage_review.py`",
            "",
        ]
    )
    REPORT_PATH.write_text(report + "\n", encoding="utf-8")
    print(REPORT_PATH)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
