# UI Variant Prototype

Use this branch when seeing or clicking alternatives is the fastest way to decide.

Preferred shape:

- Reuse an existing route and switch variants with `?variant=`.
- If the app already has feature flags or storybook-like preview routes, use that convention.
- Create a standalone route only when no existing surface can host the variants safely.
- Keep variants out of production navigation and mark them as temporary in code.

Variant design:

- Default to three structurally different approaches.
- Vary interaction model, hierarchy, navigation, density, or layout rather than only colors.
- Use real product content where available.
- Keep assets and typography consistent with the existing app unless the question is explicitly visual direction.

Verification:

- Start the app and give the user the URL.
- Check at least one desktop and one mobile viewport when the choice depends on responsive layout.
- Capture what each variant teaches and which one should be absorbed or discarded.
