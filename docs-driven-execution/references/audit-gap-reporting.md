# Gap Reporting

Record missing history explicitly instead of smoothing it over.

## When To Record A Gap

- some steps happened but were not captured in durable artifacts
- a delegated slice returned incomplete context
- command output or verification evidence is missing for part of the story
- the team can infer what happened, but cannot prove it from current records

## Good Gap Record Shape

- what is missing
- why it is missing
- what can still be trusted
- what risk the gap creates
- what would close the gap later

## Rules

- A gap is not a failure by itself.
- Do not inflate minor missing detail into a major incident.
- Do not hide a material missing step just because the likely story seems obvious.
