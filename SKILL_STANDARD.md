# Skill Packaging Standard

This library adopts MiniMax-inspired packaging discipline without importing MiniMax's opinionated product or vendor defaults wholesale.

## Core Principles

- Keep the existing repo-first, lifecycle-aware operating model.
- Add richer metadata so skills are easier to trigger, review, and validate.
- Use optional support folders only when they materially improve the skill.
- Prefer narrow ownership plus explicit handoffs over broad mega-skills.
- Avoid vendor lock-in, stack dogma, and taste-level UI rules as global defaults.

## Required Frontmatter

Every `SKILL.md` in this library should define:

- `name`
- `description`
- `version`
- `category`
- `sources`
- `use_when`
- `avoid_when`
- `artifacts`
- `quality_gates`

Expected shape:

```yaml
---
name: example-skill
description: Explain when the skill should trigger and what it helps accomplish.
version: 1.0.0
category: execution
sources:
  - internal skill library
use_when:
  - The user asks for a phased implementation plan with docs.
avoid_when:
  - The task is a trivial one-file edit that does not need delivery tracking.
artifacts:
  - SKILL.md
  - agents/openai.yaml
  - references/
quality_gates:
  - Trigger language is narrow enough to avoid swallowing unrelated work.
  - Referenced files exist and match the workflow body.
---
```

## Optional Layout

Only add these when the skill benefits from them:

- `references/` for reusable deep guidance
- `scripts/` for validation, scaffolding, or domain helpers
- `templates/` for reusable output skeletons
- `assets/` for icons or bundled visual artifacts

Every listed artifact should either exist or be intentionally omitted from `artifacts`.

## Authoring Rules

- Keep `SKILL.md` procedural and concise.
- Put reusable detail into `references/` instead of bloating the main file.
- Make trigger boundaries explicit in both `description` and `use_when`.
- Use `avoid_when` to protect against overlap and accidental over-triggering.
- Keep quality gates concrete enough to review manually or with tooling.
- When a skill operates inside a codebase, defer to repo grounding, docs, and verification instead of replacing those workflows.

## Versioning Rules

- Start a new skill at `1.0.0`.
- Bump the patch version for wording fixes, reference repairs, or packaging-only changes that do not materially change behavior.
- Bump the minor version when the trigger boundary, workflow, quality gates, or major handoffs change in a way maintainers should notice.
- Bump the major version only when the skill’s core contract or expected outputs are intentionally incompatible with previous behavior.
- If behavior changes, update the version in the same edit instead of leaving the skill on a stale number.

## Validation

Run:

```bash
python3 /Users/longdo/.agents/skills/scripts/validate_skills.py
```

That command validates the editable local skill library by default. Add `--include-system` only when you intentionally want to audit vendor-managed `.system` skills too.

Use the scaffold helper for new skills:

```bash
python3 /Users/longdo/.agents/skills/scripts/init_skill.py --help
```

Generate the machine-readable catalog and manifest with:

```bash
python3 /Users/longdo/.agents/skills/scripts/generate_skill_catalog.py
```

Pressure-test overlap-prone routing examples with:

```bash
python3 /Users/longdo/.agents/skills/scripts/check_skill_routing.py
```

Generate a current stocktake report with:

```bash
python3 /Users/longdo/.agents/skills/scripts/generate_stocktake_report.py
```

Generate the current usage-review prompt and cadence report with:

```bash
python3 /Users/longdo/.agents/skills/scripts/generate_usage_review.py
```

Check that no editable skills remain in the legacy root with:

```bash
python3 /Users/longdo/.agents/skills/scripts/check_mirror_parity.py
```

Run the full sequential skill-library check with:

```bash
python3 /Users/longdo/.agents/skills/scripts/check_all_skills.py
```

## Feedback Loop

- After real projects, capture routing near-misses and useful prompt shapes in `scripts/fixtures/skill-routing-fixtures.json`.
- Use `templates/usage-review-template.md` to record prompt candidates, unclear boundaries, and example-output gaps.
- Prefer operational feedback from real sessions over speculative rewrites of already-stable skills.
