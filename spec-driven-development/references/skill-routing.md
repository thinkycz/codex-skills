# Skill Routing

Apply `custom-skill-routing` first for the shared routing model across your local custom skills.

This reference only covers the routing choices that are specific to spec-driven delivery from client artifacts.

## Default Routing

### Design-driven frontend implementation

Use:

- `figma`
- `google-stitch`
- `design-to-prd`
- `design-to-traversable-app`

Choose this when:

- the user provides Figma URLs, Stitch screens, or other confirmed design-source inputs
- frontend screens or components must match design closely
- visual fidelity is part of acceptance
- the target framework materially affects delivery shape

Routing note:

- use the source adapter first (`figma` or `google-stitch`)
- use `design-to-prd` first when the visual source needs to become a normalized written product document
- then use `design-to-traversable-app` for the shared multi-screen buildout
- then read the matching framework reference inside `design-to-traversable-app` for Next.js, Vue.js, Laravel + Inertia, or AdonisJS + Inertia
- use `design-fidelity-polish` when the remaining work is mostly parity cleanup on an existing implementation

### Frontend implementation backed by a real API

Use:

- `integrating-backend-api-into-frontend`

Choose this when:

- frontend forms, pages, or tables depend on live backend support
- delivery needs blocker tracking against partial backend support
- browser QA and runtime behavior matter

### Ambiguous or conflicting product definition

Use:

- `product-brainstorming`

Choose this when:

- the source artifacts are too ambiguous to implement safely
- the written spec and design leave important behavior undefined
- a design direction must be clarified before planning or coding

### During implementation

Always apply:

- `test-driven-development`
- `verification-before-completion`

## Routing Notes

- One task may use more than one helper skill.
- Route by dominant risk: fidelity, integration, ambiguity, execution scale, or source-of-truth conflict.
- If no helper skill cleanly fits, keep the main workflow simple and explain the choice.
