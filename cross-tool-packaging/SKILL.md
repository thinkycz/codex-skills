---
name: cross-tool-packaging
description: Use when the skill library or agent assets need packaging, export, catalog, or compatibility work across Codex and universal formats.
version: 1.3.0
category: skill-ops
sources:
  - skill packaging, export profiles, catalogs, and compatibility workflows
use_when:
  - The task is to package, export, catalog, validate, or distribute the skill library across multiple target formats.
  - The work is about bundle shape and compatibility rather than skill content itself.
avoid_when:
  - The task is just to edit one skill's content without touching packaging or distribution.
artifacts:
  - SKILL.md
  - agents/openai.yaml
  - agents/
  - references/
quality_gates:
  - Packaging output stays reproducible, profile-aware, and explicit about target format assumptions.
---

# Cross Tool Packaging

Own the packaging, export, and compatibility workflow for the skill library across Codex-native and universal formats.

This skill is for bundle shape, export profiles, compatibility assumptions, catalog generation, and reproducible packaging behavior. It is not the skill for editing content inside one skill unless that content change is part of a packaging or distribution task.

It is narrower than `skill-stocktake` and `skill-maintenance-and-validation`: this skill owns bundle outputs, manifest/catalog generation, flattened export behavior, and compatibility notes, not overlap decisions or one-package content repair.

## Boundary

- Own export shape, manifest and catalog generation, and compatibility notes across formats.
- Do not replace `skill-maintenance-and-validation` for one-package correctness work.
- Do not replace `skill-stocktake` for keep, merge, retire, or portfolio-health decisions.
- Use this skill when the main question is how the bundle should be produced or described, not what an individual skill should say.

## When To Use

Use this skill when:

- the library needs exporting, flattening, cataloging, or profile-aware packaging
- the library needs a flattened export or a machine-readable catalog, not just a copied folder
- compatibility between Codex-native and universal formats matters
- the question is about how the bundle should be produced or distributed, not just what one skill says

Do not use this skill when:

- the task is ordinary skill-content editing with no packaging implications
- the problem is one broken skill package that should be handled by `skill-maintenance-and-validation`
- the broader issue is portfolio overlap or retirement rather than packaging shape

## Core Workflow

1. Inspect the current packaging surface.
   - Read the current scripts, manifests, exports, and catalog artifacts first.
   - Confirm which formats already exist and which one is the source of truth.

2. Define the target format clearly.
   - Distinguish:
     - Codex-native package
     - universal folder export
     - flattened self-contained markdown export
     - any future manifest or catalog output

3. Preserve reproducibility.
   - Prefer scriptable generation over manual copying.
   - Keep output shape deterministic and easy to regenerate.

4. Make compatibility assumptions explicit.
   - State what companion files are preserved, inlined, omitted, or merely inventoried.
   - Call out `.system` handling and any profile-specific behavior.

5. Verify the packaged result.
   - Check file counts, expected outputs, and representative artifacts.
   - Keep the packaging story honest when outputs differ by profile or environment.

## Output

Produce a concise packaging summary with:

- source of truth
- target format or profile
- scripts or commands used
- resulting artifacts
- compatibility notes or known limits

## Rules

- Prefer one reproducible script over repeated manual export steps.
- Do not blur content maintenance with packaging maintenance.
- Make target-format assumptions explicit.
- Keep the packaging workflow simple enough that another maintainer can rerun it quickly.

## References

Read these only as needed:

- [references/profile-matrix.md](references/profile-matrix.md)
  Use for deciding which bundle format fits the request.
- [references/compatibility-notes.md](references/compatibility-notes.md)
  Use when documenting what is preserved, inlined, excluded, or degraded across exports.
