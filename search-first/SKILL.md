---
name: search-first
description: Use when the task needs fast, scoped evidence gathering before implementation, planning, or architectural claims.
version: 1.0.0
category: research
sources:
  - repo evidence and primary-source research practices
use_when:
  - Freshness, uncertainty, or multiple plausible explanations make early evidence gathering important.
  - The task would benefit from repo exploration first and selective web verification second.
avoid_when:
  - The answer is already stable, local, and directly discoverable without extra research.
artifacts:
  - SKILL.md
  - agents/openai.yaml
  - agents/
  - references/
quality_gates:
  - Search stays bounded, source-backed, and explicit about inference versus confirmed fact.
---

# Search First

Search before asserting when uncertainty, freshness, or architectural ambiguity could change the answer.

This skill is a lightweight research-first layer that complements repo exploration, debugging, and planning. It does not replace the owning workflow. It improves the quality of the next decision.

## When To Use

Use this skill when:

- the task has multiple plausible explanations and guessing would be risky
- architectural claims depend on real repo evidence, not assumptions
- external information may have changed and primary-source verification matters
- you need a bounded fact-finding pass before planning or coding

Do not use this skill when:

- the answer is already obvious from nearby code or docs
- the task is so small that extra research would be slower than the work itself
- the real need is a full owner skill such as `systematic-debugging` or `repo-convention-discovery`

## Core Workflow

1. Start local before going remote.
   - Inspect the repo, nearby files, docs, configs, tests, and existing artifacts first.
   - Prefer discoverable local truth over asking the user or reaching for the web.

2. Define the search question narrowly.
   - State what unknown must be resolved before the next step.
   - Keep the search bounded to the minimum evidence needed for that decision.

3. Use the strongest sources available.
   - Prefer primary sources such as official docs, source code, schemas, and repo-owned artifacts.
   - When browsing, compare multiple plausible sources if the answer could vary or be stale.

4. Mark fact versus inference explicitly.
   - Separate what the evidence directly confirms from what you infer from it.
   - Call out missing evidence instead of smoothing over uncertainty.

5. Hand off to the owner skill once the unknown is resolved.
   - Route back into the workflow that actually owns the next step.
   - Keep the research summary short and decision-oriented.

## Output

Produce a concise working summary of:

- the question being resolved
- the evidence gathered
- what is confirmed
- what is inferred
- what owner skill or next action should follow

## Rules

- Repo exploration comes before web research when local truth exists.
- Use primary sources when browsing is required.
- Keep the research pass short, relevant, and decision-driven.
- Do not turn this into generic endless searching.
- Do not claim certainty when the evidence only supports an inference.

## References

Read these only as needed:

- [references/source-quality.md](references/source-quality.md)
  Use when deciding which evidence should count as primary, secondary, or too weak.
- [references/freshness-and-inference.md](references/freshness-and-inference.md)
  Use when the task depends on up-to-date facts or when you need to mark inference clearly.
