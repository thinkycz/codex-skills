---
name: google-stitch
description: Use Google Stitch as a design-source adapter for project and screen discovery, generation, editing, and handoff into shared design-delivery workflows. Trigger when the user provides Stitch projects or wants Stitch-generated screens used as the source for implementation or fidelity work.
version: 1.1.0
category: source-adapter
sources:
  - Google Stitch projects and screen artifacts
  - bundled Stitch workflow references
use_when:
  - Stitch screens or projects are the design source for implementation or fidelity work.
  - The user needs Stitch-specific source discovery, generation, or edit guidance.
avoid_when:
  - The task is lifecycle ownership or non-Stitch design acquisition.
  - A generic implementation skill is the real owner.
artifacts:
  - SKILL.md
  - agents/openai.yaml
  - agents/
  - references/
quality_gates:
  - Repo context is checked before translating Stitch artifacts into delivery work.
  - Screen inventory and source caveats are summarized before handoff.
  - Stitch-specific behavior stays separate from shared implementation workflows.
---

# Google Stitch

Use this skill as the Stitch-specific source adapter in this workspace.

It does not own the whole implementation lifecycle. It owns the Stitch-specific source acquisition, context gathering, and handoff into shared design workflows such as `design-to-prd`, `design-to-traversable-app`, `design-fidelity-polish`, and `spec-driven-development`.

## When To Use

Use this skill when the user:

- provides a Google Stitch project or screens as the design source
- wants Stitch screens generated or edited before implementation
- wants an existing app or feature implemented from Stitch outputs
- needs Stitch context gathered before broader design-driven delivery work

Do not use this skill as the sole owner for phased delivery, route/state implementation, or release closeout.

## Core Workflow

1. Ground in the repo first.
   - Apply `repo-convention-discovery` before making assumptions about routing, feature structure, shared primitives, styling, or state.
   - Explore any existing `/docs` artifacts that might already describe the feature or current implementation.

2. Identify the Stitch source surface.
   - Determine whether the user has:
     - an existing Stitch project
     - existing Stitch screens
     - only a text prompt and wants Stitch generation first
   - If the request is ambiguous, gather the minimum missing Stitch identifiers before continuing.

3. Gather the right Stitch context.
   - List or open the relevant Stitch project and screens.
   - Use Stitch generation or edit flows only when the user actually needs new or revised source screens.
   - Treat Stitch screens as source material for implementation, not as direct production code.

4. Normalize the handoff for downstream implementation skills.
   - Produce a concise working summary that captures:
     - project or screen identifiers
     - screen inventory and role
     - important states or interactions
     - visual or UX caveats
     - any missing information still needed from written specs or backend contracts
   - When the work should become a written Product Requirements Document before implementation, hand off to `design-to-prd`.
   - When the work is larger than a single screen and headed toward implementation, hand off to `design-to-traversable-app` and read the matching framework reference there for Next.js, Vue.js, Laravel + Inertia, or AdonisJS + Inertia.
   - When the work is mostly parity cleanup on an existing app, hand off to `design-fidelity-polish`.
   - When the work is tied to a written client specification or mixed backend/admin scope, hand off to `spec-driven-development`.

5. Resolve source-of-truth issues honestly.
   - If written specification, backend reality, and Stitch screens disagree in a way that changes scope, fields, flows, or acceptance criteria, stop and ask the user which source has priority.
   - Do not silently treat Stitch as authoritative when the written client specification says otherwise.

## Stitch-Specific Rules

- Treat Stitch as a design source and planning aid, not as final production architecture.
- If Stitch generation is needed, keep prompts tightly aligned with the provided product intent rather than letting the generated screens redefine the requirement.
- If Stitch output is too coarse for exact fidelity acceptance, document that and ask for the missing written or visual artifacts rather than pretending the source is complete.
- When the user already has finalized Stitch screens, prefer reading and normalizing those screens over regenerating them.

## Handoff Contract

Before handing off to shared delivery skills, make sure the downstream skill has:

- the Stitch project id or screen ids when available
- a usable screen inventory
- key interactions and state notes
- known limitations or ambiguities in the Stitch source
- the target delivery adapter when the framework is known
- any required pairing with written specs, API contracts, or backend docs

## References

Read these only as needed:

- `references/stitch-workflows.md`
  Use for the common Stitch acquisition and handoff patterns.
- `references/source-caveats.md`
  Use for source-quality limits, regeneration rules, and conflict handling guidance.
