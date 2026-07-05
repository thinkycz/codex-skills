#!/usr/bin/env python3

from __future__ import annotations

import argparse
from pathlib import Path


DEFAULT_AGENTS_ROOT = Path("/Users/longdo/.agents/skills")
DEFAULT_CODEX_ROOT = Path("/Users/longdo/.codex/skills")


def skill_packages(root: Path) -> set[str]:
    return {
        child.name
        for child in root.iterdir()
        if child.is_dir() and (child / "SKILL.md").is_file()
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Check that editable skills live only in the canonical user root."
    )
    parser.add_argument("--agents-root", default=str(DEFAULT_AGENTS_ROOT))
    parser.add_argument("--codex-root", default=str(DEFAULT_CODEX_ROOT))
    args = parser.parse_args()

    agents_packages = skill_packages(Path(args.agents_root))
    legacy_packages = skill_packages(Path(args.codex_root))

    if legacy_packages:
        print("Canonical-root check failed; editable skills remain in ~/.codex/skills:")
        for name in sorted(legacy_packages):
            print(f"- {name}")
        return 1

    print(
        f"Canonical-root check passed for {len(agents_packages)} skill package(s); "
        "no legacy duplicates found."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
