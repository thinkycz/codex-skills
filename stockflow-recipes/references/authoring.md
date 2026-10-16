# Recipe authoring and verification

## Current-format discovery

The reviewed library used one Markdown document per recipe under `resources/recipes/<category>/`, a category manifest, a first fenced JSON metadata block, and locale dictionaries. Re-read the current guide and parser before editing; do not copy dated totals or assume a new category/component is already allowed.

- Preserve stable category/file slugs and variant keys. Give new recipes the appropriate category position, aliases and tags; the same display name can exist in separate hot/cold categories.
- Keep canonical structural headings and source ingredient/component terms in English when that is still the parser contract. Match variant headings to metadata; keep selectors explicit and authored combinations intact.
- Keep one action per numbered preparation step in the same order. Only create timers for source-confirmed exact durations. A visual endpoint or duration range is not a fixed timer.
- Use the existing locale-key scheme. In the reviewed format, number placeholders occur exactly once and in source order in EN/CS/SK templates; localized instructions must not change units or add quantities. Local ingredient terms must remain searchable.

## Formula review

- Reconcile every method ingredient and quantity with the ingredient table. Preserve mass versus volume, scoops versus pieces, brewed tea versus dry leaves, and total-volume instructions versus an amount to add. Do not silently convert grams to millilitres.
- Put all ice in the `Ice` component, including chilling cubes and batch dilution, with a corresponding method step. Where the source specifies a full serving cup, retain it. Do not remove explicitly authored chilling cubes merely because a variant is named no-ice.
- Keep hot milk steaming, powder preparation and cloud/topping preparation explicit and in a workable order. Hot drinks must not accidentally inherit a cold drink's ice step.
- Preserve batch formulas and user-confirmed ratios. Do not derive ice quantity by subtracting starting water from finished batch volume; other ingredients contribute volume. Keep cooking, draining/rinsing and sauce preparation distinct.
- Keep recipe quantities separate from optional topping/sweetness guidance. Use the current catalog's applicability rules rather than applying a gram-based hot-drink adjustment from a millilitre-based cold-drink rule.

## Employee acceptance

Run the current catalog validator and required repository gate. Derive intentional count changes from the actual files; never replace precise validation with permissive checks just to accept new content.

In a browser, check the changed recipes on desktop and phone in EN/CS/SK: category placement, autocomplete including hot/cold disambiguation, complete ingredients and method, quantity formatting, and starting/completing guided preparation. Check variant changes reset temporary progress/timers as documented. Expand to related variants when a shared translation, parser or component changes. Record skipped database or environment checks explicitly.
