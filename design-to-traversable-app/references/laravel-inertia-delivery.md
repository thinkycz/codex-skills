# Laravel Inertia Delivery

Use this reference when the target stack for design-driven delivery is Laravel with Inertia.

## Workflow

1. Inspect the current Laravel and Inertia app shape first.
   - Confirm route organization, controller boundaries, Inertia page structure, shared layouts, prop hydration patterns, validation flow, and frontend asset pipeline.
   - Inspect whether the app uses Vue, React, or another frontend layer under Inertia and follow the existing pattern.

2. Keep Laravel and Inertia decisions local to the repo.
   - Prefer existing route files, controller structure, request validation, shared props, and page composition.
   - Reuse app layouts, middleware-driven props, and shell components before inventing new boundaries.

3. Apply Laravel + Inertia defaults only for greenfield work.
   - Default profile:
     - Laravel latest stable
     - Inertia.js
     - the repo's existing frontend layer, or Vue if none exists
     - named routes for real destinations
     - server-provided page props for initial page state
     - shared layout components for shell-owned panels and global navigation

4. Map source screens into Laravel + Inertia structures.
   - Use Laravel routes and Inertia pages for real navigation destinations.
   - Use client-side page state for dialogs, drawers, tabs, overlays, and transient design states unless the user explicitly wants separate URLs.
   - Keep viewport-level overlays at the viewport layer even when route-backed pages own the surrounding shell.

5. Respect backend and frontend boundaries.
   - Keep server-side data shaping, authorization, and validation in Laravel layers.
   - Keep transient UI state and view-specific interaction logic in the Inertia frontend.

## Decision Defaults

- Laravel routes and Inertia pages for real destinations
- client-side state for transient screen states and overlays
- existing controller, request, and shared-prop patterns win over new abstractions
- repo conventions override the greenfield defaults when a real app already exists
