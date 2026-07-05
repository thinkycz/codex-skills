---
name: design-fidelity-polish
description: Use when a design-driven app already has screen coverage and now needs a dedicated visual parity pass for exact assets, typography, spacing, overlays, states, and browser QA. Trigger when the source may come from Figma, Google Stitch, or another confirmed design handoff.
version: 1.4.0
category: design-quality
sources:
  - confirmed design handoff from Figma, Google Stitch, or similar sources
  - browser QA and accessibility checks used by this workspace
use_when:
  - Screens already exist but need exactness work across assets, type, spacing, overlays, or states.
  - The user wants a dedicated final fidelity and browser QA pass.
avoid_when:
  - The work is first-pass route creation or broad app planning.
  - A design source has not been normalized yet.
artifacts:
  - SKILL.md
  - agents/openai.yaml
  - agents/
  - references/
quality_gates:
  - The implementation is re-grounded in the design source before broad edits.
  - Exact assets and shell ownership issues are fixed before ad hoc CSS tweaking.
  - Browser QA, accessibility, and interaction-state checks run before claiming parity.
---

# Design Fidelity Polish

Use this as the canonical fidelity workflow after the main routes or parent-state interactions already exist.

This skill is design-platform-agnostic. Apply a source adapter such as `figma` or `google-stitch` first when you need fresh screenshots, source notes, or source-specific asset guidance.

This skill assumes a target design already exists and the main job is parity. Use `frontend-redesign-audit` when the current product feels weak but no confirmed target design is driving the changes yet. Hand off to `design-system-export` only after the visual direction is stable enough to codify beyond one screen or pass.

## Boundary

- Own screen-level and interaction-level parity once a target design is already established.
- Do not replace `design-to-traversable-app` for first-pass implementation or route/state buildout.
- Do not replace `frontend-redesign-audit` when the current UI needs diagnosis before a target direction exists.
- Hand off to `design-system-export` only after parity work reveals stable reusable rules worth codifying.

## When To Use

Use this skill when the user:

- says the screens are implemented but the visuals still do not match the design source
- wants 1:1 parity for icons, fonts, logos, images, spacing, overlays, or active states
- needs route/state coverage refined into true design fidelity
- wants a final browser QA pass driven by the design source
- needs a canonical UI quality pass for accessibility, interaction polish, or motion sanity checks after the screens already exist

Do not use this skill for first-pass route creation or broad app planning. Use `design-to-traversable-app` for that.

## Core Workflow

1. Confirm the current implementation shape first.
   - Apply `repo-convention-discovery` before changing visual primitives or shell behavior.
   - Identify which screens are already routes versus parent-state interactions.
   - Identify whether current mismatches are asset problems, layout problems, state or interaction problems, or shell ownership problems.

2. Re-ground in the source design.
   - Use the relevant source adapter first for screenshots, structure, asset guidance, and source caveats.
   - Prefer the user-confirmed source canvas, screen, or project scope rather than an arbitrary child view.

3. Build a fidelity checklist before broad edits.
   - Track every relevant screen or interaction in a fidelity matrix.
   - Separate exactness work into:
     - icons
     - fonts
     - images and logos
     - spacing and sizing
     - active and inactive states
     - overlays and slideovers
     - browser QA notes
   - Include operational QA checks for:
     - accessibility
     - interaction states
     - typography and layout readability
     - motion and transition behavior
     - product-inappropriate anti-patterns
   - Explicitly check for generic AI-generated UI patterns such as centered-hero defaults, repeated card rows, placeholder copy, and decorative motion with no product value.

4. Fix exact assets before tweaking CSS by hand.
   - If icon fidelity matters, export or generate the correct assets from the source system and replace placeholder icon libraries.
   - If the user provides proprietary fonts, ingest them into the project instead of continuing with fallbacks.
   - Localize unstable remote assets into stable project paths.
   - Track exact active and inactive asset variants separately when the design uses different states.
   - Do not use emoji as structural icons when the product needs real iconography.
   - When the user provides a final logo, banner, menu image, favicon, or brand asset, use that asset directly or localize it rather than recreating an approximate decorative substitute.

5. Fix ownership and behavior mismatches.
   - Move state-only routes into parent interactions if the design implies a dialog, drawer, tab state, or slideover.
   - Make overlays viewport-level when the design visually covers the viewport.
   - Put shell-owned panels such as notification drawers in the shell rather than behind separate pages when the design implies that ownership.
   - Make sure important interactions do not depend on hover alone when the target experience includes touch devices.

6. Fix layout and type mismatches after assets are correct.
   - Align spacing, sizing, content widths, card heights, text scale, and state variants to the design screenshots.
   - Reuse repo primitives only if they preserve fidelity.
   - Prefer editing shared primitives and shells when that resolves a mismatch across multiple screens.
   - Check readable body sizes, line height, line length, heading hierarchy, and semantic color usage before treating the UI as done.
   - Prefer grid over brittle flex percentage hacks when the layout needs deliberate structure.
   - Avoid viewport-height shortcuts that degrade mobile behavior.

7. Run the canonical UI quality pass before claiming parity.
   - Validate contrast, focus treatment, reduced motion behavior, keyboard or screen-reader basics, form labeling, and color-not-alone signaling.
   - Validate hover, press, loading, disabled, and destructive states for clarity.
   - Validate motion timing and that transitions use meaning rather than decoration.
   - Validate that the product is not leaning on generic low-contrast, over-animated, or product-inappropriate visual defaults.
   - Validate that the implementation is fully resolved, not padded with placeholder comments, missing states, or obviously temporary UI substitutions unless those are explicitly documented as blockers.

8. Verify before claiming fidelity is done.
   - Run formatter if configured.
   - Run linter.
   - Run production build.
   - Update the fidelity matrix with what is exact, what is close, what is blocked, what is unresolved, and any remaining constraints.
   - Do not claim 1:1 parity while known mismatches, QA failures, or unresolved font or asset gaps remain.
   - For static sites and marketing pages, verify the actual browser-rendered responsive layout, language switching, metadata/favicons when touched, and outbound links that were changed.
   - Apply `release-readiness` when the polish work is part of a broader handoff or release decision.
   - Hand off to `design-system-export` when the visual direction is stable and should be codified into reusable tokens, component rules, or generation-friendly guidance.

## Required Outputs

Produce or update these when the work is non-trivial:

- `docs/verification/design-fidelity-matrix.md`
- any route/state matrix entries affected by consolidation
- localized icon, font, or image assets under stable project paths
- a clear closeout note that distinguishes:
  - exact parity achieved
  - close approximation
  - blocked areas
  - known remaining constraints

## Decision Defaults

Use these defaults unless the user overrides them:

- treat screen coverage and fidelity polish as separate completion stages
- replace generic icon libraries with source-correct assets when icon fidelity is requested
- ingest provided proprietary fonts instead of continuing with approximations
- localize brittle remote assets
- treat dialogs, drawers, and slideovers as parent-state interactions unless the user explicitly wants standalone URLs
- implement full-screen overlays at viewport level when the design behaves that way
- use `exact`, `close`, `blocked`, and `unresolved` language in fidelity reporting
- treat accessibility, interaction clarity, and motion sanity checks as part of fidelity, not optional extras
- keep docs honest about remaining mismatches

## References

Read these only as needed:

- `references/exact-assets.md`
  Use for icon, logo, image, and font handling rules.
- `references/overlays-and-shells.md`
  Use when fixing dialogs, slideovers, shell-owned panels, and viewport overlays.
- `references/browser-qa.md`
  Use for the fidelity checklist structure and closeout expectations.
- `references/ui-quality-checklist.md`
  Use for the canonical accessibility, interaction, typography, layout, motion, and anti-pattern QA pass.
- `references/anti-slop-ui-checks.md`
  Use when the UI is functional but still feels generic, repetitive, or AI-default.
- `references/output-completeness.md`
  Use when checking that the polish pass actually finished the UI instead of leaving placeholders or silent omissions.
