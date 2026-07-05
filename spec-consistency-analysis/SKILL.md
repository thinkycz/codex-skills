---
name: spec-consistency-analysis
description: Use when spec, plan, and task artifacts exist and need a read-only consistency pass before implementation or handoff.
version: 1.1.0
category: quality
sources:
  - cross-artifact analysis of specs, plans, tasks, and checklists
use_when:
  - Multiple delivery artifacts exist and contradictions, omissions, or coverage gaps could cause rework.
  - The next step should be a read-only analysis rather than more planning or coding.
avoid_when:
  - Only one artifact exists and the work is still in early specification.
artifacts:
  - SKILL.md
  - agents/openai.yaml
  - agents/
  - references/
quality_gates:
  - Analysis stays read-only, cross-checks artifacts systematically, and distinguishes conflicts from missing detail.
---

# Spec Consistency Analysis

Analyze delivery artifacts for contradictions, omissions, and weak traceability before implementation or handoff.

This skill is a read-only quality pass across written artifacts such as specs, plans, tasks, and requirement checklists. It does not rewrite the docs and it does not implement the work. It is the “find the gaps before coding” step.

## When To Use

Use this skill when:

- the spec, plan, and task artifacts all exist or mostly exist
- the team wants a consistency review before implementation accelerates
- contradictions or missing coverage could create avoidable rework

Do not use this skill when:

- the work is still at first-spec stage
- the next step is still clarification rather than cross-artifact analysis
- the task is to edit the docs directly rather than analyze them first

## Core Workflow

1. Load the relevant artifacts.
   - Read the active spec, implementation plan, tasks, and any requirements-quality checklist if present.
   - Work from the current written artifacts, not chat memory.

2. Compare them systematically.
   - Check whether every important requirement is planned.
   - Check whether every planned slice is reflected in tasks.
   - Check whether tasks imply scope not justified by the spec.

3. Classify the findings.
   - Contradiction:
     two artifacts disagree
   - Omission:
     an important requirement has no downstream coverage
   - Drift:
     later artifacts quietly changed intent
   - Ambiguity:
     wording is too weak to validate reliably

4. Report impact and next action.
   - Tie each finding to planning, sequencing, testing, UX, or operational risk.
   - Recommend whether the next owner should clarify, re-plan, decompose tasks, or proceed.

## Output

Produce a concise analysis report with:

- artifacts reviewed
- major contradictions
- coverage gaps
- ambiguous or weak completion signals
- recommended next action before implementation

Use [references/example-output.md](references/example-output.md) for a concrete analysis report shape when needed.

## Rules

- Keep the pass read-only.
- Compare artifacts against each other, not against imagined ideal scope.
- Prefer a short set of high-impact findings over exhaustive noise.
- Distinguish true contradiction from simple missing detail.

## References

Read these only as needed:

- [references/analysis-rubric.md](references/analysis-rubric.md)
  Use for contradiction, omission, drift, and ambiguity checks.
- [references/requirements-checklists.md](references/requirements-checklists.md)
  Use for checklist-style spec quality review before or during analysis.
