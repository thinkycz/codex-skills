# Vuejs Delivery

Use this reference when the target stack for design-driven delivery is Vue.js.

## Workflow

1. Inspect the current Vue app shape first.
   - Confirm whether the repo uses Vue Router, Nuxt-style routing, Pinia, composables, or another established pattern.
   - Inspect page organization, layout wrappers, shared components, state boundaries, and form patterns.

2. Keep Vue decisions local to the repo.
   - Prefer existing router structure, composables, store patterns, and component layering.
   - Reuse shared layouts and shells before inventing new page hierarchy.

3. Apply Vue defaults only for greenfield work.
   - Default stack profile:
     - Vue 3
     - TypeScript when the repo supports it
     - Vue Router
     - Pinia
     - Tailwind CSS when design-system tokens are not already established
     - VeeValidate or the repo's existing form pattern
     - Axios or the repo's existing HTTP client
     - ESLint + Prettier

4. Map source screens into Vue structures.
   - Use router pages for true navigation destinations.
   - Use component state, composables, or store-backed interactions for transient states such as dialogs, drawers, tabs, and overlays unless the user explicitly wants separate URLs.
   - Keep viewport-level overlays at the viewport layer.

## Decision Defaults

- router pages for real destinations, state for transient design states
- existing composables and store patterns win over new abstractions
- repo conventions override the greenfield defaults when a real app already exists
