# Nextjs Delivery

Use this reference when the target stack for design-driven delivery is Next.js.

## Workflow

1. Inspect the current Next.js app shape first.
   - Confirm App Router versus older routing if the repo is mixed or transitional.
   - Inspect route groups, layouts, providers, state boundaries, and shared UI primitives.

2. Keep Next.js decisions local to the repo.
   - Prefer existing route segment patterns, layouts, data loading, and client/server boundaries.
   - Reuse existing shells and page-level structure before inventing new route patterns.

3. Apply Next.js defaults only for greenfield work.
   - Default stack profile:
     - Next.js latest with App Router
     - TypeScript
     - Tailwind CSS
     - React Query
     - Sonner
     - React Hook Form + Yup
     - Axios
     - date-fns
     - next-intl
     - Zustand
     - ESLint + Prettier + prettier-plugin-tailwindcss

4. Map source screens into Next.js structures.
   - Use routes for real navigation destinations.
   - Use local or shared state interactions for dialogs, drawers, tabs, review states, and transient overlays unless the user explicitly wants separate URLs.
   - Keep viewport-level overlays at the viewport layer.

## Decision Defaults

- App Router first for greenfield Next.js delivery
- state-only screens collapse into parent-route interactions
- shared shells and layouts own shell-wide panels and overlays
- repo conventions override the greenfield defaults when a real app already exists
