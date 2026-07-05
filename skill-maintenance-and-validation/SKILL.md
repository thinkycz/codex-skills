---
name: skill-maintenance-and-validation
description: Use when creating, updating, or reviewing skills that need to stay linted, internally consistent, reference-safe, and realistically testable.
version: 2.0.0
category: skill-ops
sources:
  - local skill packages and their support files
  - /Users/longdo/.agents/skills/SKILL_STANDARD.md
use_when:
  - The task is to create, update, or review skills without letting triggers, references, or handoffs drift.
  - A validator-backed maintenance pass is needed on the skill library itself.
avoid_when:
  - The primary work is creating a brand-new domain workflow from scratch and skill-creator should lead.
  - The task is ordinary feature implementation unrelated to skills.
artifacts:
  - SKILL.md
  - agents/openai.yaml
  - agents/
  - references/
quality_gates:
  - Frontmatter matches the shared schema and still reflects the workflow body.
  - Referenced files, prompts, and handoffs are consistent and discoverable.
  - Validation status is reported honestly when tooling is blocked or warnings remain.
---

# Skill Maintenance And Validation

Use this skill to keep existing skills healthy after edits or to harden a newly created skill before relying on it.

This skill is for maintenance, consistency, and validation work on skills themselves. It is not the primary skill for creating a brand-new domain workflow from scratch; use `skill-creator` for that.

This skill owns package correctness, not portfolio strategy and not distribution shape. Use `skill-stocktake` for keep/merge/retire judgments across the library. Use `cross-tool-packaging` for exports, manifests, catalogs, and compatibility work.

## Boundary

- Own package-level correctness for skills and their support files.
- Do not replace `skill-stocktake` when the question is portfolio overlap, sprawl, or retire-versus-keep decisions.
- Do not replace `cross-tool-packaging` when the question is export shape, flattening, cataloging, or compatibility.
- Use this skill when the maintainer needs one skill or a targeted set of skills kept internally consistent and honestly validated.

## When to Use

Use this skill when the user:

- wants to update an existing skill and avoid drift
- wants to validate that a skill still matches its metadata and references
- wants to add or refine skills without breaking routing or handoff behavior
- wants a repeatable quality pass on a custom skill set
- hits a validator or environment problem and needs a reliable fallback validation workflow

## Core Workflow

1. Inspect the skill package first.
   - Read `SKILL.md`, `agents/openai.yaml`, and any referenced files that matter for the change.
   - Confirm the skill directory shape is intentional and minimal.
   - Check whether the skill overlaps with or should hand off to another existing skill.
   - Use `/Users/longdo/.agents/skills/SKILL_STANDARD.md` as the source of truth for metadata and optional layout.
   - Keep editable user skills in `/Users/longdo/.agents/skills`; treat `/Users/longdo/.codex/skills/.system` as vendor-managed.

2. Check trigger quality.
   - Ensure frontmatter `name` and `description` clearly say when the skill should be used.
   - Ensure the description is specific enough to trigger for the intended tasks without swallowing unrelated work.
   - Check that the body instructions are consistent with the trigger promise.
   - Treat narrow triggers and minimal overlap as first-class quality requirements, not cleanup polish.

3. Check internal consistency.
   - `agents/openai.yaml` should match the actual skill purpose.
   - `default_prompt` should mention the skill as `$skill-name`.
   - Referenced files in `references/`, `scripts/`, or `assets/` should exist and still fit the workflow.
   - Handoffs to other skills should be intentional, not accidental duplication.
   - Debugging and delivery skills should consistently explain when to widen from a local symptom to a shared pattern or reusable root cause.
   - Prefer one primary owner skill plus explicit handoffs over blended ownership that hides the real boundary.

4. Distinguish package maintenance from portfolio review.
   - If the task is really about overlap, aging, context bloat, or whether several skills should merge, split, refresh, or retire, route to `skill-stocktake`.
   - If the task is about export formats, catalogs, flattened bundles, or compatibility assumptions, route to `cross-tool-packaging`.
   - Keep validator-backed package correctness checks separate from library-level portfolio judgments.

5. Validate progressively.
   - Run `python3 /Users/longdo/.agents/skills/scripts/validate_skills.py` after meaningful skill changes when the local environment supports it.
   - Use `--include-system` only when intentionally auditing vendor-managed `.system` skills too.
   - Run the bundled validator if the local environment supports it.
   - If the validator is blocked by missing dependencies or environment gaps, perform a manual fallback pass:
     - check frontmatter shape
     - check hyphen-case name
     - check description clarity
     - check referenced files exist
     - check `openai.yaml` consistency
     - check for stale or contradictory instructions
     - check that app-wide fix guidance appears where it should, without implying that every bug must become a broad refactor
   - Validate the workflow under realistic pressure when possible:
     - test whether the skill would trigger for the right prompt shape
     - test whether it routes to the correct owner or handoff
     - test whether a process-enforcing skill still works without rationalizing around its rules
   - Reject pseudo-tool or pseudo-transcript examples that encourage the model to imitate output formats instead of using real tools.

6. Keep the skill lean.
   - Prefer a concise `SKILL.md` plus targeted references over one bloated instruction file.
   - Move detailed material into `references/` only when it is truly reusable and only loadable on demand.
   - Avoid adding extra docs such as README or changelog files.
   - Treat context footprint as a maintenance concern:
     - remove low-signal prose
     - keep reusable detail in references
   - avoid repeating the same checklist across multiple skills
   - Flag bloated `SKILL.md` files and recommend moving repeated or reusable depth into `references/`.
   - Look for low-signal repetition across neighboring skills, not just within one file.
   - When mining prior conversations, extract reusable conventions only; do not preserve secrets, client-specific facts, private URLs, or one-off project memory inside skills.

7. Close with honest validation status.
   - Say whether validation was tool-based or fallback/manual.
   - Call out remaining risks such as missing local dependencies, stale references, or overlap with another skill.
   - Do not claim a skill is fully validated if the validator could not run and fallback checks found unresolved issues.

## Required Outputs

For non-trivial skill maintenance work, produce or update:

- the skill files themselves
- any necessary references under `references/`
- `agents/openai.yaml` when the UI-facing metadata is stale
- a concise closeout note that distinguishes:
  - validator passed
  - fallback/manual validation only
  - known remaining maintenance gaps

## Decision Defaults

Use these defaults unless the user overrides them:

- update existing skills instead of creating duplicates when the scope clearly belongs in one place
- prefer one primary owner skill plus explicit handoffs over overlapping mega-skills
- keep `SKILL.md` procedural and concise
- keep detailed examples or checklists in references
- run validator-based checks when possible
- preserve one canonical editable copy under `/Users/longdo/.agents/skills`
- if validator dependencies are missing, do a documented fallback validation instead of pretending validation succeeded
- keep shared-root-cause guidance centralized in the primary owner skill and mirrored lightly in related skills rather than copy-pasting the full workflow
- prefer realistic scenario validation over metadata-only review when a skill governs behavior, discipline, or quality gates

## References

Read these only as needed:

- `references/context-economy.md`
  Use when trimming skill scope, deciding what belongs in references, or checking context-budget discipline.
- `references/validation-checklist.md`
  Use for the standard maintenance and validation checklist.
- `references/fallback-validation.md`
  Use when the bundled validator cannot run cleanly.
- `references/scope-and-overlap.md`
  Use when deciding whether to update, split, or hand off between skills.
- `references/pressure-testing.md`
  Use when validating skills through realistic prompts, workflow pressure, or discipline-enforcement scenarios.
- `/Users/longdo/.agents/skills/SKILL_STANDARD.md`
  Use for the shared metadata schema, optional layout rules, and authoring defaults for this library.
- `skill-stocktake`
  Use when the problem is portfolio health, overlap, skill sprawl, or keep versus retire decisions rather than package correctness alone.
