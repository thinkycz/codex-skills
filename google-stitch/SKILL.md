---
name: google-stitch
description: Acquire or explicitly generate/edit Stitch screens and hand them off with source provenance.
version: 1.2.0
category: design-source
sources:
  - Supplied task evidence and applicable project conventions
use_when:
  - Acquire or explicitly generate/edit Stitch screens and hand them off with source provenance.
avoid_when:
  - The requested outcome belongs to another owner or exceeds the authorized scope.
artifacts:
  - SKILL.md
  - agents/openai.yaml
  - agents/
  - references/
quality_gates:
  - Evidence supports the stated outcome and limitations.
  - Selected mode, references and actions remain within authorization.
---

# Google Stitch

Discover the specified project/screens and available Stitch capabilities. Fetch screen detail, preview and assets; preserve project/screen IDs and separate generated markup from confirmed product behavior. Acquisition works without a repository. Generate or edit remote designs only when requested; inspect results before handoff. Tool limitations or absent access must remain explicit. For implementation, map the confirmed source into repository conventions without treating prototype code as a production architecture mandate.

## Working evidence

Reuse existing repository identity, relevant changes, acceptance criteria, canonical examples, required checks and blockers. Refresh only invalidated facts. Stay within the requested scope and applicable permissions; report observed evidence and remaining gaps separately.

## Selected detail

Read only what the current task needs; supporting references do not mandate extra workflow stages.

- [Source Caveats](references/source-caveats.md): for source caveats.
- [Stitch Workflows](references/stitch-workflows.md): for stitch workflows.
