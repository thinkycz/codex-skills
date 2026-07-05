#!/usr/bin/env python3

from __future__ import annotations

import argparse
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def render_list(items: list[str], fallback: str) -> list[str]:
    values = items or [fallback]
    return [f"  - {item}" for item in values]


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a new local skill scaffold.")
    parser.add_argument("name", help="Hyphen-case skill name")
    parser.add_argument("description", help="One-line trigger description")
    parser.add_argument("category", help="Skill category, for example execution or quality")
    parser.add_argument(
        "--version",
        default="1.0.0",
        help="Initial semver version for the skill frontmatter; use 1.0.0 for new skills unless you are importing an existing versioned workflow.",
    )
    parser.add_argument(
        "--with",
        dest="extras",
        action="append",
        choices=["references", "scripts", "templates", "assets"],
        default=[],
        help="Optional support directory to create",
    )
    parser.add_argument("--source", action="append", default=[], help="Add a source item")
    parser.add_argument("--use-when", action="append", default=[], help="Add a use_when item")
    parser.add_argument("--avoid-when", action="append", default=[], help="Add an avoid_when item")
    parser.add_argument(
        "--quality-gate",
        action="append",
        default=[],
        help="Add a quality gate item",
    )
    args = parser.parse_args()

    skill_dir = ROOT / args.name
    if skill_dir.exists():
        raise SystemExit(f"{skill_dir} already exists")

    (skill_dir / "agents").mkdir(parents=True)
    for extra in args.extras:
        (skill_dir / extra).mkdir()

    artifacts = ["  - SKILL.md", "  - agents/openai.yaml", "  - agents/"]
    for extra in args.extras:
        artifacts.append(f"  - {extra}/")

    skill_md = "\n".join(
        [
            "---",
            f"name: {args.name}",
            f"description: {args.description}",
            f"version: {args.version}",
            f"category: {args.category}",
            "sources:",
            *render_list(args.source, "internal skill library"),
            "use_when:",
            *render_list(args.use_when, "The task clearly matches this skill's owning workflow."),
            "avoid_when:",
            *render_list(args.avoid_when, "Another existing skill is the more specific owner."),
            "artifacts:",
            *artifacts,
            "quality_gates:",
            *render_list(
                args.quality_gate,
                "Trigger language, references, and handoffs stay aligned after edits.",
            ),
            "---",
            "",
            f"# {args.name.replace('-', ' ').title()}",
            "",
            "Describe the workflow here.",
            "",
        ]
    )
    (skill_dir / "SKILL.md").write_text(skill_md, encoding="utf-8")

    openai_yaml = "\n".join(
        [
            "interface:",
            f'  display_name: "{args.name.replace("-", " ").title()}"',
            f'  short_description: "{args.description}"',
            f'  default_prompt: "Use ${args.name} to handle this task."',
            "",
        ]
    )
    (skill_dir / "agents" / "openai.yaml").write_text(openai_yaml, encoding="utf-8")
    print(f"Created {skill_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
