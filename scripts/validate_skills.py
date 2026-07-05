#!/usr/bin/env python3

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_KEYS = [
    "name",
    "description",
    "version",
    "category",
    "sources",
    "use_when",
    "avoid_when",
    "artifacts",
    "quality_gates",
]
SEMVER_RE = re.compile(r"^\d+\.\d+\.\d+$")
REL_PATH_RE = re.compile(r"(?:\(|`)(references|scripts|assets|agents)/([^)`\s]+)(?:\)|`)")


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
                if (nested / "SKILL.md").exists():
                    skill_dirs.append(nested)
            continue
        if (child / "SKILL.md").exists():
            skill_dirs.append(child)
    return skill_dirs


def parse_frontmatter(skill_path: Path) -> tuple[dict[str, object], list[str]]:
    lines = skill_path.read_text(encoding="utf-8").splitlines()
    errors: list[str] = []
    if len(lines) < 3 or lines[0].strip() != "---":
        return {}, ["missing opening frontmatter delimiter"]

    try:
        end_index = lines[1:].index("---") + 1
    except ValueError:
        return {}, ["missing closing frontmatter delimiter"]

    data: dict[str, object] = {}
    current_list_key: str | None = None

    for raw_line in lines[1:end_index]:
        line = raw_line.rstrip()
        if not line:
            continue
        stripped = line.lstrip()
        if stripped.startswith("- "):
            if not current_list_key:
                errors.append(f"list item without active key: {line}")
                continue
            data.setdefault(current_list_key, []).append(stripped[2:].strip())
            continue
        if ":" not in line:
            errors.append(f"invalid frontmatter line: {line}")
            current_list_key = None
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if not value:
            data[key] = []
            current_list_key = key
            continue
        data[key] = value.strip("\"'")
        current_list_key = None

    return data, errors


def extract_relative_paths(skill_path: Path) -> set[str]:
    text = skill_path.read_text(encoding="utf-8")
    matches = REL_PATH_RE.findall(text)
    return {f"{prefix}/{suffix}" for prefix, suffix in matches}


def find_default_prompt(agent_path: Path) -> str | None:
    text = agent_path.read_text(encoding="utf-8")
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("default_prompt:"):
            return stripped.split(":", 1)[1].strip().strip("\"'")
    return None


def validate_skill(skill_dir: Path) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    skill_path = skill_dir / "SKILL.md"
    frontmatter, fm_errors = parse_frontmatter(skill_path)
    errors.extend(fm_errors)

    if fm_errors:
        return errors, warnings

    for key in REQUIRED_KEYS:
        if key not in frontmatter:
            errors.append(f"missing required frontmatter key `{key}`")

    if errors:
        return errors, warnings

    name = str(frontmatter["name"])
    if name != skill_dir.name:
        errors.append(f"name `{name}` does not match directory `{skill_dir.name}`")

    version = str(frontmatter["version"])
    if not SEMVER_RE.match(version):
        errors.append(f"version `{version}` is not semver")

    for list_key in ["sources", "use_when", "avoid_when", "artifacts", "quality_gates"]:
        value = frontmatter.get(list_key)
        if not isinstance(value, list) or not value:
            errors.append(f"`{list_key}` must be a non-empty list")

    artifacts = frontmatter.get("artifacts", [])
    if isinstance(artifacts, list):
        for artifact in artifacts:
            artifact_path = skill_dir / artifact
            if artifact.endswith("/"):
                if not artifact_path.is_dir():
                    errors.append(f"artifact directory `{artifact}` is missing")
            else:
                if not artifact_path.is_file():
                    errors.append(f"artifact file `{artifact}` is missing")

        for implicit_dir in ["references", "scripts", "templates", "assets", "agents"]:
            present = (skill_dir / implicit_dir).exists()
            declared = f"{implicit_dir}/" in artifacts
            if present and not declared:
                warnings.append(f"`{implicit_dir}/` exists but is not listed in artifacts")
            if declared and not present:
                errors.append(f"`{implicit_dir}/` listed in artifacts but missing")

    agent_path = skill_dir / "agents" / "openai.yaml"
    if not agent_path.exists():
        errors.append("missing agents/openai.yaml")
    else:
        default_prompt = find_default_prompt(agent_path)
        if not default_prompt:
            warnings.append("agents/openai.yaml has no default_prompt")
        elif f"${name}" not in default_prompt:
            errors.append("default_prompt does not mention the skill token")

    for rel_path in sorted(extract_relative_paths(skill_path)):
        if not (skill_dir / rel_path).exists():
            errors.append(f"referenced path `{rel_path}` does not exist")

    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate the local Codex skill library.")
    parser.add_argument(
        "--include-system",
        action="store_true",
        help="Also audit vendor-managed skills under .system.",
    )
    parser.add_argument(
        "--strict-warnings",
        action="store_true",
        help="Exit non-zero when warnings are present.",
    )
    args = parser.parse_args()

    failures = 0
    warning_count = 0

    for skill_dir in iter_skill_dirs(include_system=args.include_system):
        errors, warnings = validate_skill(skill_dir)
        if errors or warnings:
            print(f"[{skill_dir.relative_to(ROOT)}]")
            for error in errors:
                print(f"  ERROR: {error}")
            for warning in warnings:
                print(f"  WARN: {warning}")
            print()
        failures += len(errors)
        warning_count += len(warnings)

    if failures == 0 and warning_count == 0:
        print("All skills passed validation.")
        return 0

    print(f"Validation finished with {failures} error(s) and {warning_count} warning(s).")
    if failures > 0:
        return 1
    return 1 if args.strict_warnings else 0


if __name__ == "__main__":
    raise SystemExit(main())
