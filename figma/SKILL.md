---
name: figma
description: "Use the Figma MCP server as a Figma-specific design-source adapter: setup, design context, screenshots, assets, and handoff into the shared design-delivery workflows. Trigger when a task involves Figma URLs, node IDs, Figma MCP setup, or Figma source acquisition for implementation or fidelity work."
version: 1.1.0
category: source-adapter
sources:
  - Figma MCP tools and node context
  - bundled Figma setup and prompt references
use_when:
  - The user provides Figma URLs, node IDs, or a Figma-led design handoff.
  - Implementation or fidelity work needs grounded screenshots, structure, or assets from Figma.
avoid_when:
  - The task is broader delivery ownership, routing, or release closeout.
  - The source is not Figma.
artifacts:
  - SKILL.md
  - LICENSE.txt
  - agents/openai.yaml
  - agents/
  - assets/
  - references/
quality_gates:
  - Repo context is checked before translating Figma output into implementation guidance.
  - Exact node context and screenshots are gathered before asset or code decisions.
  - The handoff stays source-oriented and does not treat MCP output as production code.
---

# Figma

Use this as the Figma-specific source adapter in this workspace.

It does not own the whole implementation lifecycle. It owns the Figma-specific source acquisition, context gathering, and handoff into shared design workflows such as `design-to-prd`, `design-to-traversable-app`, `design-fidelity-polish`, and `spec-driven-development`.

For setup and debugging details, see `references/figma-mcp-config.md`.

## When To Use

Use this skill when the user:

- provides Figma URLs, node ids, or files as the design source
- wants Figma design context gathered before implementation
- wants an existing app or feature implemented from Figma outputs
- needs Figma screenshots, metadata, or assets before broader design-driven delivery work

Do not use this skill as the sole owner for phased delivery, route/state implementation, or release closeout.

## Core Workflow

1. Ground in the repo first.
   - Apply `repo-convention-discovery` before making assumptions about routing, feature structure, shared primitives, styling, or state.
   - Explore any existing `/docs` artifacts that might already describe the feature or current implementation.

2. Identify the Figma source surface.
   - Determine whether the user has:
     - a Figma file or frame URL
     - exact node ids or only a broader canvas
     - a finalized design source or an exploratory reference
   - If the request is ambiguous, gather the minimum missing Figma identifiers before continuing.

3. Gather the right Figma context.
   - Run `get_design_context` first for the exact node or nodes in scope.
   - If the response is too large or truncated, run `get_metadata` to get the high-level node map and then re-fetch only the required nodes with `get_design_context`.
   - Run `get_screenshot` for a visual reference of the node variant being implemented.
   - Download assets only after the node context and screenshot are both grounded.
   - Treat the MCP output as source material for implementation, not as direct production code.

4. Normalize the handoff for downstream implementation skills.
   - Produce a concise working summary that captures:
     - file, frame, or node identifiers
     - screen inventory and role
     - important states, overlays, or interactions
     - asset and font caveats
     - any missing information still needed from written specs or backend contracts
   - When the work should become a written Product Requirements Document before implementation, hand off to `design-to-prd`.
   - When the work is larger than a single screen and headed toward implementation, hand off to `design-to-traversable-app` and read the matching framework reference there for Next.js, Vue.js, Laravel + Inertia, or AdonisJS + Inertia.
   - When the work is mostly parity cleanup on an existing app, hand off to `design-fidelity-polish`.
   - When the work is tied to a written client specification or mixed backend/admin scope, hand off to `spec-driven-development`.

5. Resolve source-of-truth issues honestly.
   - If written specification, backend reality, and Figma designs disagree in a way that changes scope, fields, flows, or acceptance criteria, stop and ask the user which source has priority.
   - Do not silently treat Figma as authoritative when the written client specification says otherwise.

## Figma-Specific Rules

- Treat Figma as a design source and planning aid, not as final production architecture.
- If proprietary fonts or unstable remote assets are missing, document that limitation so downstream implementation or polish work stays honest.
- The Figma MCP Server provides an assets endpoint which can serve image and SVG assets.
- IMPORTANT: If the Figma MCP Server returns a localhost source for an image or an SVG, use that image or SVG source directly.
- IMPORTANT: DO NOT import or add new icon packages when the needed assets are present in the Figma payload.
- IMPORTANT: do NOT use or create placeholders if a localhost source is provided.

## Handoff Contract

Before handing off to shared delivery skills, make sure the downstream skill has:

- the Figma file, frame, or node identifiers when available
- a usable screen inventory
- key interactions, overlays, and state notes
- asset, font, or source-quality caveats
- the target delivery adapter when the framework is known
- any required pairing with written specs, API contracts, or backend docs

## Link-Based Prompting
- The server is link-based: copy the Figma frame/layer link and give that URL to the MCP client when asking for implementation help.
- The client cannot browse the URL but extracts the node ID from the link; always ensure the link points to the exact node/variant you want.

## References
- `references/figma-mcp-config.md` — setup, verification, troubleshooting, and link-based usage reminders.
- `references/figma-tools-and-prompts.md` — tool catalog and prompt patterns for selecting frameworks/components and fetching metadata.
