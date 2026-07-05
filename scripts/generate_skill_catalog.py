#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FIXTURES_PATH = ROOT / "scripts" / "fixtures" / "skill-routing-fixtures.json"


def iter_skill_dirs(include_system: bool) -> list[Path]:
    skill_dirs: list[Path] = []
    for child in sorted(ROOT.iterdir()):
        if child.name == "scripts":
            continue
        if child.name.startswith(".") and child.name != ".system":
            continue
        if child.name == ".system":
            if not include_system:
                continue
            for nested in sorted(child.iterdir()):
                if (nested / "SKILL.md").is_file():
                    skill_dirs.append(nested)
            continue
        if (child / "SKILL.md").is_file():
            skill_dirs.append(child)
    return skill_dirs


def parse_frontmatter(skill_path: Path) -> dict[str, object]:
    lines = skill_path.read_text(encoding="utf-8").splitlines()
    if len(lines) < 3 or lines[0].strip() != "---":
        raise ValueError(f"{skill_path} is missing frontmatter")

    try:
        end_index = lines[1:].index("---") + 1
    except ValueError as exc:
        raise ValueError(f"{skill_path} is missing closing frontmatter") from exc

    data: dict[str, object] = {}
    current_list_key: str | None = None
    for raw_line in lines[1:end_index]:
        line = raw_line.rstrip()
        if not line:
            continue
        stripped = line.lstrip()
        if stripped.startswith("- "):
            if not current_list_key:
                raise ValueError(f"{skill_path} contains a list item without a key: {line}")
            data.setdefault(current_list_key, []).append(stripped[2:].strip())
            continue
        if ":" not in line:
            raise ValueError(f"{skill_path} has an invalid frontmatter line: {line}")
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


def skill_body(skill_path: Path) -> str:
    text = skill_path.read_text(encoding="utf-8")
    parts = text.split("---", 2)
    return parts[2].lstrip() if len(parts) >= 3 else text


def load_overlap_clusters() -> dict[str, list[str]]:
    payload = json.loads(FIXTURES_PATH.read_text(encoding="utf-8"))
    mapping: dict[str, list[str]] = {}
    for cluster in payload["clusters"]:
        for skill in cluster["skills"]:
            mapping.setdefault(skill["id"], []).append(cluster["name"])
    return mapping


def load_expected_handoffs() -> dict[str, list[str]]:
    payload = json.loads(FIXTURES_PATH.read_text(encoding="utf-8"))
    handoffs: dict[str, list[str]] = {}
    for cluster in payload["clusters"]:
        for skill in cluster["skills"]:
            handoffs[skill["id"]] = sorted(set(skill["required_mentions"]))
    return handoffs


def extract_handoff_mentions(text: str, skill_ids: set[str], current_skill: str) -> list[str]:
    mentions: list[str] = []
    for skill_id in sorted(skill_ids):
        if skill_id == current_skill:
            continue
        if re.search(rf"\b{re.escape(skill_id)}\b", text):
            mentions.append(skill_id)
    return mentions


def derive_warnings(entry: dict[str, object]) -> list[str]:
    warnings: list[str] = []
    line_count = int(entry.get("skill_md_lines", 0))
    references_count = int(entry.get("references_count", 0))
    handoff_mentions = list(entry.get("handoff_mentions", []))
    body = str(entry.get("body", ""))
    overlap_clusters = list(entry.get("overlap_clusters", []))
    has_boundary_section = bool(re.search(r"^## Boundar(?:y|ies)\b", body, re.MULTILINE))

    if line_count >= 180 and references_count < 2:
        warnings.append("large_owner_with_thin_references")
    if line_count >= 120 and not has_boundary_section and entry.get("category") in {"execution", "orchestration", "product-design", "design-quality", "quality"}:
        warnings.append("missing_explicit_boundary_section")
    if overlap_clusters and not has_boundary_section:
        warnings.append("overlap_prone_without_boundary_section")
    if len(handoff_mentions) >= 8 and references_count < 2:
        warnings.append("many_neighbor_mentions_without_reference_support")
    if len(handoff_mentions) >= 10 and line_count >= 140:
        warnings.append("high_neighbor_density")
    return warnings


def build_entry(
    skill_dir: Path,
    skill_ids: set[str],
    overlap_clusters: dict[str, list[str]],
    expected_handoffs: dict[str, list[str]],
) -> dict[str, object]:
    frontmatter = parse_frontmatter(skill_dir / "SKILL.md")
    body = skill_body(skill_dir / "SKILL.md")
    support_dirs = sorted(
        path.name
        for path in skill_dir.iterdir()
        if path.is_dir() and path.name not in {".git"}
    )
    source_type = "system" if ".system" in skill_dir.parts else "local"
    references_dir = skill_dir / "references"
    references_count = len(list(references_dir.glob("*.md"))) if references_dir.is_dir() else 0
    handoff_mentions = extract_handoff_mentions(body, skill_ids, skill_dir.name)
    entry = {
        "id": skill_dir.name,
        "name": frontmatter.get("name", skill_dir.name),
        "description": frontmatter.get("description", ""),
        "version": frontmatter.get("version", ""),
        "category": frontmatter.get("category", ""),
        "source_type": source_type,
        "path": str(skill_dir),
        "artifacts": frontmatter.get("artifacts", []),
        "support_dirs": support_dirs,
        "skill_md_lines": len((skill_dir / "SKILL.md").read_text(encoding="utf-8").splitlines()),
        "references_count": references_count,
        "has_companion_files": any(
            path.is_file() and path.name != "SKILL.md" for path in skill_dir.rglob("*")
        ),
        "requires_companion_files": any(name in support_dirs for name in {"references", "templates", "assets", "scripts"}),
        "handoff_mentions": handoff_mentions,
        "expected_handoffs": [
            handoff for handoff in expected_handoffs.get(skill_dir.name, []) if handoff in skill_ids
        ],
        "overlap_clusters": overlap_clusters.get(skill_dir.name, []),
        "body": body,
        "exportable_profiles": [
            "universal-folder",
            "flattened-markdown",
            "codex-local",
        ],
    }
    entry["warnings"] = derive_warnings(entry)
    entry.pop("body", None)
    return entry


def write_json(path: Path, payload: dict[str, object]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=False) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate machine-readable skill catalog artifacts.")
    parser.add_argument(
        "--include-system",
        action="store_true",
        help="Include vendor-managed skills under .system.",
    )
    args = parser.parse_args()

    generated_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    skill_dirs = iter_skill_dirs(include_system=args.include_system)
    skill_ids = {skill_dir.name for skill_dir in skill_dirs}
    overlap_clusters = load_overlap_clusters()
    expected_handoffs = load_expected_handoffs()
    skills = [
        build_entry(
            skill_dir,
            skill_ids=skill_ids,
            overlap_clusters=overlap_clusters,
            expected_handoffs=expected_handoffs,
        )
        for skill_dir in skill_dirs
    ]

    catalog_payload = {
        "generated_at": generated_at,
        "root": str(ROOT),
        "include_system": args.include_system,
        "skill_count": len(skills),
        "skills": skills,
    }
    manifest_payload = {
        "pack_name": "codex-skills",
        "pack_version": "1.0.0",
        "generated_at": generated_at,
        "root": str(ROOT),
        "default_validation_command": "python3 /Users/longdo/.agents/skills/scripts/validate_skills.py",
        "default_catalog_command": "python3 /Users/longdo/.agents/skills/scripts/generate_skill_catalog.py",
        "default_routing_check_command": "python3 /Users/longdo/.agents/skills/scripts/check_skill_routing.py",
        "default_export_command": "python3 /Users/longdo/.agents/skills/scripts/export_universal_skills.py /Users/longdo/skills/exports --flatten",
        "profiles": [
            "universal-folder",
            "flattened-markdown",
            "codex-local",
        ],
        "included_skill_ids": [skill["id"] for skill in skills],
        "excluded_by_default": [".system"] if not args.include_system else [],
        "compatibility_notes": [
            "System skills are vendor-managed and excluded from generated artifacts unless explicitly requested.",
            "Flattened exports inline text companions and inventory non-text assets.",
        ],
    }

    write_json(ROOT / "skills.catalog.json", catalog_payload)
    write_json(ROOT / "skills.manifest.json", manifest_payload)

    print(f"Wrote catalog for {len(skills)} skills")
    print(ROOT / "skills.catalog.json")
    print(ROOT / "skills.manifest.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
