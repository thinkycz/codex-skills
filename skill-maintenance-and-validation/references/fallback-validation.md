# Fallback Validation

Use this when the normal validator cannot run because of local environment problems.

## Typical Blockers

- missing Python dependencies such as `PyYAML`
- missing interpreter or shell tools
- validator script exists but the environment is incomplete

## Fallback Workflow

1. Read `SKILL.md`.
   - confirm frontmatter exists
   - confirm `name` and `description` exist
   - confirm the name is lowercase hyphen-case

2. Read `agents/openai.yaml` if present.
   - confirm the display name and description still match the skill
   - confirm `default_prompt` mentions the skill as `$skill-name`

3. Check linked resources.
   - confirm files named in `references/`, `scripts/`, or `assets/` actually exist
   - confirm the references still support the workflow described in `SKILL.md`

4. Check for stale guidance.
   - remove references to files that were renamed or deleted
   - remove claims that the skill validates itself automatically if that is no longer true
   - ensure handoff recommendations still point to real skills

5. Report the limitation honestly.
   - say the validator did not run
   - say what fallback checks were performed
   - say whether any remaining uncertainty is due to the missing dependency

## Rule

Fallback validation is acceptable when the environment is blocked, but it is not the same as a clean validator pass. Say that explicitly.
