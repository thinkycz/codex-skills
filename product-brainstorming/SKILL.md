---
name: product-brainstorming
description: Turn feature ideas, product changes, UX flows, and redesign requests into a clear design direction before implementation. Use when the agent needs to shape ambiguous or user-facing work by exploring current context, clarifying intent, comparing meaningful approaches, and writing a full design doc that can hand off to planning.
version: 1.3.0
category: product-design
sources:
  - current product and codebase context
  - design-direction heuristics for this workspace
use_when:
  - Product intent or UX direction is still ambiguous and needs structured shaping.
  - The user wants solution tradeoffs compared before implementation planning.
avoid_when:
  - The design is already fixed enough to write a PRD or implement directly.
  - The task is a narrow coding change with no product-direction ambiguity.
artifacts:
  - SKILL.md
  - agents/openai.yaml
  - agents/
  - references/
quality_gates:
  - Current product context is grounded before proposing a new direction.
  - Tradeoffs and recommendations are explicit rather than implicit guesses.
  - The output is concrete enough to hand off into planning.
---

# Product Brainstorming

Shape feature and redesign ideas into implementation-ready product designs without dragging the user through unnecessary ceremony.

Start by grounding in the current product and codebase, then guide the conversation toward a concrete recommendation. Keep the process collaborative, but compress it when the intent is already clear.

## Core Stance

- Default to using this skill for new features, product behavior changes, UX flows, and redesign work.
- Do not treat every tiny code edit or isolated refactor as a brainstorming exercise.
- Prefer design-first when the work is ambiguous, user-facing, cross-cutting, or likely to create rework if assumptions are wrong.
- Skip straight to implementation only when the request is already narrow, low-risk, and clearly specified.
- Use [references/brainstorming-defaults.md](references/brainstorming-defaults.md) for the shorthand defaults when the task shape is obvious.

## Boundary

- Own ambiguous product direction, UX shaping, and redesign thinking before planning.
- Do not replace `design-to-prd` when the main missing artifact is a PRD derived from an already-set design source.
- Do not replace `spec-driven-development` when the source is already stable enough for planning and execution.
- Hand off to `frontend-redesign-audit` when the current product needs diagnosis before design direction can be trusted.

## Workflow

### 1. Ground In Reality

- Explore the repo, existing UX, docs, and nearby implementation patterns before asking questions.
- Summarize the current state in plain language so the user can confirm or correct it quickly.
- If the request is obviously too large for a single coherent design, propose a smaller first slice before refining details.

### 2. Clarify Only What Matters

- Ask the highest-leverage questions first.
- Prefer one question at a time when the answer will materially change the design.
- Use multiple choice when it helps the user respond quickly, but do not force it.
- Focus on purpose, audience, constraints, success criteria, and what must not change.
- When UI direction matters, clarify product type, audience expectations, trust level, and brand tone early enough to choose an intentional visual direction.
- If a reasonable assumption is low risk, make it and say so instead of turning it into process.

Use [references/high-leverage-questions.md](references/high-leverage-questions.md) when you need concrete prompt shapes for clarification.

### 3. Compare Approaches Only When Tradeoffs Are Real

- Propose 2-3 approaches when there are meaningful product, UX, or engineering tradeoffs.
- Lead with the recommended option and explain why it fits the current product and constraints.
- If one option is clearly dominant, present it directly instead of inventing fake alternatives.
- Name the anti-patterns to avoid for the chosen direction when the product category makes them risky, such as novelty-heavy UI in trust-sensitive products or generic AI gradients in products that need clarity and credibility.
- When the work is frontend-heavy, call out common AI-generated UI traps early: generic centered heroes, repetitive card grids, decorative gradients, weak state design, and layout choices that look polished in isolation but do not fit the product.

Use [references/tradeoff-patterns.md](references/tradeoff-patterns.md) when the solution space has real alternatives.

### 4. Converge Quickly

- Move from exploration to recommendation as soon as the shape of the solution is clear.
- Keep momentum by synthesizing what has been learned instead of repeating open questions.
- Aim for guided, efficient collaboration: thoughtful enough to improve the idea, light enough to stay useful in day-to-day work.

### 5. Present The Design

Present a concise but complete design that covers the parts an implementer would need to trust:

- Product goal and user outcome
- Core UX flow and behavioral rules
- Visual direction that fits the product, audience, and trust level
- Key anti-patterns and visual traps to avoid
- Key states, edge cases, and failure handling
- Data flow, dependencies, and integration points
- Testing and validation expectations

Scale the depth to the work. A focused feature may only need a compact design. A larger redesign may need fuller sections and explicit tradeoffs.

When UI direction is a meaningful part of the request, include a brief design-system recommendation:

- visual style or stylistic keywords
- color and token direction
- typography hierarchy direction
- motion stance
- icon or illustration stance
- accessibility-sensitive constraints that should shape the design from the start
- layout rhythm or anti-slop guidance when the product needs to avoid generic AI-generated structure

### 6. Write The Design Doc

- Once the direction is validated, write a full design doc.
- Do not draft the design doc in the very first reply unless the user explicitly asked for an immediate written spec.
- Use the early turns to ground context, resolve the most important ambiguities, and confirm the proposed direction is close enough.
- Default location: `docs/specs/YYYY-MM-DD-<topic>-design.md`
- User preferences for document location override the default.
- The doc should be polished enough to hand to planning or implementation without re-explaining the conversation.

Use [references/design-doc-template.md](references/design-doc-template.md) for the suggested structure instead of repeating it inline.

### 7. Hand Off When Needed

- If the result should become a formal product document derived from design or validated feature direction, hand off to `design-to-prd`.
- If the task still needs implementation planning and traceable execution prep, hand off to `spec-driven-development`.
- If the current UI needs diagnosis before redesign direction can be trusted, hand off to `frontend-redesign-audit`.
- If the design direction is stable enough to codify into reusable system rules, hand off to `design-system-export`.
- Treat `spec-driven-development` as the usual next step for multi-step implementation work in this workspace.
- Do not force a rigid chain when the user only wanted the design.

## Visual Exploration

Offer visual exploration only when the question is genuinely easier to understand by seeing it.

- Use visuals for wireframes, layout comparisons, flows, diagrams, and look-and-feel choices.
- Stay in the terminal for scope, requirements, prioritization, and most conceptual tradeoffs.
- If visuals would help, offer the companion once and keep it optional.
- Read [references/visual-companion.md](references/visual-companion.md) before using it.

Use this offer text by itself when you want consent:

> Some of what we're working on might be easier to explain if I can show it to you in a web browser. I can put together mockups, diagrams, comparisons, and other visuals as we go. This feature is still new and can be token-intensive. Want to try it? (Requires opening a local URL)

Do not combine that offer with another question.

## Quality Bar

- Optimize for better decisions, not more ritual.
- Follow the product and codebase that already exist; do not brainstorm in a vacuum.
- Include targeted improvements to rough edges only when they support the requested work.
- Check accessibility-sensitive choices before they harden into the design direction: contrast, focus visibility, motion sensitivity, input clarity, and icon semantics.
- Avoid speculative extras and YAGNI violations.
- Do not require per-section approvals, mandatory commits, or mandatory review loops unless the work is large or risky enough to justify them.
- Treat complete state design and finished output as part of quality, not optional cleanup for later.

## References

Read these only as needed:

- [references/brainstorming-defaults.md](references/brainstorming-defaults.md)
  Use for shorthand defaults about when to brainstorm versus move straight to planning.
- [references/high-leverage-questions.md](references/high-leverage-questions.md)
  Use when choosing the smallest set of clarifying questions that will materially change the design.
- [references/tradeoff-patterns.md](references/tradeoff-patterns.md)
  Use when comparing multiple meaningful approaches.
- [references/design-direction-heuristics.md](references/design-direction-heuristics.md)
  Use when choosing product-appropriate visual directions, anti-patterns, color/token rules, or typography defaults.
- [references/design-doc-template.md](references/design-doc-template.md)
  Use for the handoff-ready design doc shape.
- [references/visual-companion.md](references/visual-companion.md)
  Use when a visual companion would help the user reason about layouts, flows, or look and feel.

## Output Expectations

At the end of a successful run, the user should have:

- A clear recommended direction
- A shared understanding of scope and tradeoffs
- A full design doc capturing the final decision
- A clean next step, usually `design-to-prd`, `spec-driven-development`, or implementation
