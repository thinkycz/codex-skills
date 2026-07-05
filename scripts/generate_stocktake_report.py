#!/usr/bin/env python3

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = ROOT / "skills.catalog.json"
REPORT_PATH = ROOT / "stocktake.report.md"


def load_catalog() -> dict[str, object]:
    if not CATALOG_PATH.exists():
        raise SystemExit(
            "skills.catalog.json is missing. Run generate_skill_catalog.py before generating the stocktake report."
        )
    return json.loads(CATALOG_PATH.read_text(encoding="utf-8"))


def top_bloated(skills: list[dict[str, object]], limit: int = 5) -> list[dict[str, object]]:
    return sorted(skills, key=lambda skill: int(skill.get("skill_md_lines", 0)), reverse=True)[:limit]


def overlap_summary(skills: list[dict[str, object]]) -> list[str]:
    lines: list[str] = []
    for skill in sorted(
        skills,
        key=lambda item: (len(item.get("overlap_clusters", [])), item["id"]),
        reverse=True,
    ):
        clusters = skill.get("overlap_clusters", [])
        if not clusters:
            continue
        lines.append(f"- `{skill['id']}`: {', '.join(clusters)}")
    return lines


def handoff_gaps(skills: list[dict[str, object]]) -> list[str]:
    lines: list[str] = []
    for skill in skills:
        expected = set(skill.get("expected_handoffs", []))
        actual = set(skill.get("handoff_mentions", []))
        missing = sorted(expected - actual)
        if missing:
            lines.append(f"- `{skill['id']}` is missing expected handoff mention(s): {', '.join(missing)}")
    return lines


def reference_light(skills: list[dict[str, object]]) -> list[str]:
    lines: list[str] = []
    for skill in skills:
        line_count = int(skill.get("skill_md_lines", 0))
        references_count = int(skill.get("references_count", 0))
        if line_count >= 90 and references_count == 0:
            lines.append(f"- `{skill['id']}` has {line_count} lines in `SKILL.md` and no markdown references.")
    return lines


def warning_summary(skills: list[dict[str, object]]) -> list[str]:
    lines: list[str] = []
    for skill in skills:
        warnings = skill.get("warnings", [])
        if warnings:
            lines.append(f"- `{skill['id']}`: {', '.join(warnings)}")
    return lines


def main() -> int:
    catalog = load_catalog()
    skills = [skill for skill in catalog["skills"] if skill["source_type"] == "local"]
    generated_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat()

    bloated = top_bloated(skills)
    overlap = overlap_summary(skills)
    gaps = handoff_gaps(skills)
    leaning = reference_light(skills)
    warnings = warning_summary(skills)

    report = "\n".join(
        [
            "# Skill Stocktake Report",
            "",
            f"- Generated at: `{generated_at}`",
            f"- Catalog source: `{CATALOG_PATH}`",
            f"- Local skills reviewed: `{len(skills)}`",
            "",
            "## Current Shape",
            "",
            f"- Skills in overlap clusters: `{sum(1 for skill in skills if skill.get('overlap_clusters'))}`",
            f"- Skills with companion files: `{sum(1 for skill in skills if skill.get('has_companion_files'))}`",
            f"- Skills with references: `{sum(1 for skill in skills if int(skill.get('references_count', 0)) > 0)}`",
            "",
            "## Largest Skills",
            "",
            *[
                f"- `{skill['id']}`: {skill.get('skill_md_lines', 0)} lines, {skill.get('references_count', 0)} reference file(s)"
                for skill in bloated
            ],
            "",
            "## Overlap Clusters",
            "",
            *(overlap or ["- None detected from the current routing fixtures."]),
            "",
            "## Handoff Gaps",
            "",
            *(gaps or ["- No expected handoff gaps detected by the current routing fixtures."]),
            "",
            "## Context Budget Watchlist",
            "",
            *(leaning or ["- No obvious long-form owner files without references were detected."]),
            "",
            "## Derived Warnings",
            "",
            *(warnings or ["- No derived warning rules are currently firing."]),
            "",
            "## Recommendations",
            "",
            "- Keep using routing fixtures based on real prompts after major skill edits.",
            "- Prefer pushing repeated procedural detail into `references/` when a core owner keeps growing.",
            "- Review the largest skills first during future stocktakes because that is where overlap and context creep usually show up earliest.",
            "",
        ]
    )
    REPORT_PATH.write_text(report + "\n", encoding="utf-8")
    print(REPORT_PATH)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
