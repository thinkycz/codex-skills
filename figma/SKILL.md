---
name: figma
description: Acquire Figma design context, screenshots and assets for an identified file or node.
version: 1.2.0
category: design-source
sources:
  - Supplied task evidence and applicable project conventions
use_when:
  - Acquire Figma design context, screenshots and assets for an identified file or node.
avoid_when:
  - The requested outcome belongs to another owner or exceeds the authorized scope.
artifacts:
  - SKILL.md
  - agents/openai.yaml
  - agents/
  - references/
  - assets/
quality_gates:
  - Evidence supports the stated outcome and limitations.
  - Selected mode, references and actions remain within authorization.
---

# Figma

Resolve the supplied file/node and discover available Figma tools. Read design context and a screenshot; inspect children selectively when output is too large. Preserve node IDs, exact assets, layout constraints and observed states in the handoff. Source acquisition does not require a repository. Read configuration guidance only for setup failures and tool guidance for acquisition details. A repository becomes relevant when translating designs into implementation conventions, not before fetching a screen. Report missing access instead of inventing design details. Do not edit the Figma source unless requested.

## Working evidence

Reuse existing repository identity, relevant changes, acceptance criteria, canonical examples, required checks and blockers. Refresh only invalidated facts. Stay within the requested scope and applicable permissions; report observed evidence and remaining gaps separately.

## Selected detail

Read only what the current task needs; supporting references do not mandate extra workflow stages.

- [Figma Mcp Config](references/figma-mcp-config.md): for figma mcp config.
- [Figma Tools And Prompts](references/figma-tools-and-prompts.md): for figma tools and prompts.
