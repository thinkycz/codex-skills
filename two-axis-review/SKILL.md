---
name: two-axis-review
description: Use when reviewing a branch, PR, work-in-progress diff, or changes since a fixed point against both repo standards and the originating spec or issue.
version: 1.0.0
category: quality
sources:
  - git diff, repo standards docs, PRDs, issues, specs, plans, ADRs, and user-provided review sources
  - review workflow adapted from /Users/longdo/Downloads/skills-main
use_when:
  - The user asks for a review since a branch, commit, tag, merge base, or PR.
  - The review should separate documented-standard violations from spec, issue, PRD, or plan mismatches.
avoid_when:
  - The user wants final go/no-go readiness rather than review findings; use release-readiness.
  - The user wants implementation fixes rather than a review.
  - There is no diff, fixed point, or changed work to compare.
artifacts:
  - SKILL.md
  - agents/openai.yaml
  - agents/
  - references/
quality_gates:
  - Findings are separated into Standards and Spec axes.
  - Each actionable finding includes severity, file, line, and evidence where available.
  - The review distinguishes repo convention violations from wrong or incomplete implementation against the source request.
---

# Two-Axis Review

Review changed code on two independent axes: standards and spec.

Use this skill when the user wants a branch, PR, or diff reviewed against both documented repo conventions and the originating issue, PRD, plan, or user-provided source. Keep the axes separate so a clean implementation style does not hide a wrong feature, and a correct feature does not hide a repo-standard violation.

## Boundary

- Own review findings for changed work since a fixed point.
- Do not replace ordinary code review instructions; keep findings-first severity ordering, file and line references, open questions, and brief summaries.
- Do not replace `release-readiness`, which decides final handoff or release after verification evidence exists.
- Do not replace `verification-before-completion`, which proves a specific completion claim with fresh evidence.
- Do not implement fixes unless the user explicitly asks after the review.

## Workflow

### 1. Pin The Review Scope

- Identify the fixed point: user-provided base, PR target, merge base with `main`, last tag, or explicit commit.
- Inspect `git status` before reviewing so user work and dirty changes are not mistaken for committed diff.
- Review the relevant diff, changed files, commits, and tests.
- If no fixed point is available, state the assumption used.

### 2. Gather Standards Evidence

Look for documented repo expectations such as:

- `AGENTS.md`, `CONTRIBUTING`, `README`, `guidelines.md`, `CONTEXT.md`
- ADRs and architecture notes
- lint, formatting, type, test, build, and package configs
- local component, API, state, routing, or error-handling conventions discovered from nearby code

Use `repo-convention-discovery` if standards are hard to locate or spread across the repo.

### 3. Gather Spec Evidence

Look for the feature source:

- user-provided issue, PRD, ticket, plan, or checklist
- branch or PR description
- docs under `/docs`
- design handoff, API contract, or acceptance criteria
- explicit conversation request in the current turn

If no spec exists, run the Standards axis and mark Spec findings as unavailable rather than inventing requirements.

### 4. Review In Two Passes

- Standards axis:
  Find violations of documented repo conventions, architecture rules, style rules, test expectations, and established local patterns.
- Spec axis:
  Find mismatches, omissions, overreach, behavior drift, and acceptance criteria gaps against the issue, PRD, plan, or user request.

Use [references/review-axes.md](references/review-axes.md) to keep the axes distinct.

When the review is large and subagents are available, `subagent-driven-development` may delegate bounded read-only passes, but the lead remains responsible for final severity and de-duplication.

### 5. Report Findings

Lead with findings, ordered by severity within each axis:

- `[Standards][P0-P3] file:line - problem`
- `[Spec][P0-P3] file:line - problem`

Then include:

- open questions or assumptions
- test gaps and residual risk
- brief change summary only after findings

If there are no findings on an axis, say so clearly.

## Rules

- Do not blend spec mismatches into standards wording.
- Do not treat undocumented personal taste as a standards violation.
- Do not hide missing requirements under generic "needs tests" language.
- Do not call the work release-ready from this review alone.
- Do not modify files during the review unless the user explicitly changes the task from review to implementation.

## References

Read these only as needed:

- [references/review-axes.md](references/review-axes.md)
  Use for examples of Standards vs Spec findings and report shape.
