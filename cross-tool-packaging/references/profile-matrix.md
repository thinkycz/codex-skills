# Profile Matrix

Use this when deciding how the skill library should be packaged.

## Codex-Native

- full skill directories
- companion files preserved
- best for local Codex consumption and maintenance

## Universal Folder Export

- one folder per skill
- `SKILL.md` only
- best for minimal interoperability when companion files are not needed

## Flattened Universal Export

- one markdown file per skill
- companion text files inlined
- binary assets inventoried rather than fully embedded
- best for portability and single-file sharing

## Rules

- Choose the lightest format that still preserves the behavior needed by the target consumer.
- Do not pretend two formats are equivalent if one loses important structure.
