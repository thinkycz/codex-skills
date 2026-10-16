---
name: teacha-business-communications
description: "Draft Teacha partner correspondence or answer Google Maps customer reviews in their original language, preserving approved commercial facts and distinguishing drafts from publication."
version: 1.0.0
category: operations
sources:
  - Reviewed user-confirmed workflows and source artifacts
use_when:
  - "The user asks for Teacha partnership or expansion correspondence, or replies to business reviews."
avoid_when:
  - "The task changes delivery menus, performs unrelated translation or handles general personal email."
artifacts:
  - SKILL.md
  - agents/openai.yaml
  - agents/
  - references/
quality_gates:
  - "Branch, amounts, recipient language and commercial commitments match current evidence."
  - "Only authorized messages are sent or published and their stored status is verified."
---
# Teacha business communications

Choose the requested mode and read only its reference. Use the user's latest corrections and actual recipient/source text; do not treat observed history as permission to contact anyone.

## Modes

- **correspondence** — Draft or send authorized partner/expansion replies. [Correspondence procedure](references/correspondence.md).
- **reviews** — Prepare or publish requested Google Maps review replies. [Review procedure](references/reviews.md).

Confirm the intended business/branch and existing thread or review before writing. Drafting does not authorize sending. A current request to send or reply supplies authorization for that target and content scope; do not ask again for the same authorized action. Verify the stored draft, sent message or submitted reply, and distinguish pending moderation from public visibility.
