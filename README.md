# Codex Skills

Personal Codex skill library shared between Macs through Git.

## Installation contract for an AI agent

Install this repository as the user's canonical editable skill directory:

```text
~/.agents/skills
```

Codex discovers user-level skills from this location. Keep
`~/.codex/skills/.system` separate: it is managed by Codex and must not be
copied, replaced, committed, or deleted.

### 1. Check the destination first

Before changing anything, inspect both locations:

```bash
ls -la "$HOME/.agents/skills" 2>/dev/null || true
find "$HOME/.codex/skills" -maxdepth 2 -name SKILL.md -print 2>/dev/null || true
```

Do not overwrite a non-empty `~/.agents/skills` directory. If it contains an
existing checkout of this repository, update it instead of cloning again. If it
contains unrelated files, preserve it as a dated backup and tell the user before
reconciling those files with this library.

### 2. Fresh installation

Requirements: Git, Python 3, Codex, and SSH access to the private GitHub
repository.

```bash
mkdir -p "$HOME/.agents"
git clone git@github.com:thinkycz/codex-skills.git "$HOME/.agents/skills"
```

Confirm that the checkout is on `main` and uses the expected remote:

```bash
git -C "$HOME/.agents/skills" branch --show-current
git -C "$HOME/.agents/skills" remote get-url origin
```

Expected values:

```text
main
git@github.com:thinkycz/codex-skills.git
```

### 3. Existing installation

When the expected repository is already installed and the working tree is
clean:

```bash
git -C "$HOME/.agents/skills" pull --ff-only
```

If the working tree is not clean, do not discard or overwrite changes. Report
them and either commit them or ask the user how they should be preserved.

### 4. Validate the installation

Run the complete local validation suite:

```bash
python3 "$HOME/.agents/skills/scripts/check_all_skills.py"
```

Installation is complete only when this command ends with:

```text
All skill checks passed.
```

The canonical-root check intentionally fails if editable skill packages remain
directly under `~/.codex/skills`. Move personal packages into this repository,
but leave `~/.codex/skills/.system` untouched.

Codex normally detects skill changes automatically. Restart Codex if the new
skills do not appear.

## Keeping both Macs synchronized

Before editing skills:

```bash
git -C "$HOME/.agents/skills" pull --ff-only
```

After editing, validate before committing:

```bash
python3 "$HOME/.agents/skills/scripts/check_all_skills.py"
git -C "$HOME/.agents/skills" add -A
git -C "$HOME/.agents/skills" commit -m "Describe the skill update"
git -C "$HOME/.agents/skills" push
```

Do not use two-way filesystem synchronization on this directory. Git is the
source of truth and provides conflict detection and history.

## Repository layout

- `<skill-name>/SKILL.md`: individual skill packages
- `scripts/`: validation, routing, catalog, and export tools
- `templates/`: reusable workflow templates
- `SKILL_STANDARD.md`: conventions for maintaining this library

Generated catalogs and reports are intentionally ignored by Git. Regenerate
them with `scripts/check_all_skills.py` when needed.
