# Validation Checklist

Use this checklist after changing a skill.

## Core Files

- `SKILL.md` exists
- YAML frontmatter is present
- required frontmatter keys exist:
  `name`, `description`, `version`, `category`, `sources`, `use_when`, `avoid_when`, `artifacts`, `quality_gates`
- `name` is hyphen-case and matches the skill directory
- `description` clearly explains when the skill should be used
- `version` is valid semver
- `agents/openai.yaml` exists when UI metadata matters

## Metadata And Trigger Quality

- `use_when` and `avoid_when` create a clear ownership boundary
- `artifacts` match the files and optional folders that really exist
- `quality_gates` are concrete enough to validate
- `agents/openai.yaml` display name matches the skill purpose
- `short_description` is consistent with the frontmatter description
- `default_prompt` explicitly mentions `$skill-name`
- the trigger description is narrow enough to avoid accidental over-invocation
- the skill description does not swallow neighboring workflows that should be handoffs

## Internal Consistency

- references linked from `SKILL.md` exist
- referenced scripts or assets exist if mentioned
- handoffs to other skills are intentional
- the workflow in the body still matches the references
- there are no stale claims about files or steps that no longer exist
- pseudo-tool transcripts or fake Thought/Action/Observation examples are not presented as patterns to imitate

## Maintenance Quality

- `SKILL.md` stays concise
- references hold detailed reusable material instead of bloating the core file
- there are no unnecessary README or process-history files
- the skill does not duplicate another skill without a clear boundary
- the core file is lean enough that detailed material clearly lives in references
- scenario validation was considered when the skill enforces process or quality gates
- repeated low-signal material across neighboring skills is identified and reduced where practical
- portfolio-level overlap concerns are routed to `skill-stocktake` instead of being hidden inside package-fix work

## Validation Result

Close with one of:

- validator passed
- fallback validation passed
- validation blocked with known issues
