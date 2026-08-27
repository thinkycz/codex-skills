#!/usr/bin/env python3

from __future__ import annotations

import argparse
from pathlib import Path


DEFAULT_AGENTS_ROOT = Path.home() / ".agents" / "skills"
DEFAULT_CODEX_ROOT = Path.home() / ".codex" / "skills"

# These packages are runtime shims, not editable mirrors. Codex must discover them
# from its own skill root so custom-model router, thread, browser, computer-use,
# and media calls can be restored to the host-native tools.
RUNTIME_ONLY_CODEX_PACKAGES = frozenset(
    {
        "codex-app-threads",
        "codex-computer-use",
        "codex-in-app-browser",
        "codex-router",
        "codex-router-media",
    }
)


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
    codex_packages = skill_packages(Path(args.codex_root))
    runtime_only_packages = codex_packages & RUNTIME_ONLY_CODEX_PACKAGES
    legacy_packages = codex_packages - RUNTIME_ONLY_CODEX_PACKAGES

    if legacy_packages:
        print("Canonical-root check failed; editable skills remain in ~/.codex/skills:")
        for name in sorted(legacy_packages):
            print(f"- {name}")
        return 1

    runtime_note = (
        f"; allowed {len(runtime_only_packages)} runtime-only Codex bridge package(s)"
        if runtime_only_packages
        else ""
    )
    print(
        f"Canonical-root check passed for {len(agents_packages)} editable skill package(s); "
        f"no legacy duplicates found{runtime_note}."
    )
    for name in sorted(runtime_only_packages):
        print(f"- runtime bridge: {name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
