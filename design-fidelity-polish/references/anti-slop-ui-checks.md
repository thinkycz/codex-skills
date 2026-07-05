# Anti-Slop UI Checks

Use this when the implementation feels generic, lazy, or visually under-resolved even if it is technically functional.

## Common Frontend Slop Patterns

- generic centered hero with weak hierarchy
- repeated 3-card rows with no information rhythm
- placeholder copy, fake stats, or unfinished labels
- `h-screen` sections that break mobile viewport behavior
- brittle flex percentage layouts where grid would be clearer
- default-looking typography with no intentional hierarchy
- purple or blue neon "AI app" styling used without product fit
- motion everywhere but no meaningful interaction feedback

## Better Defaults

- use grid when layout needs deliberate spatial structure
- design around content rhythm, not just symmetrical boxes
- make hierarchy through spacing, scale, weight, and contrast
- tune layout for mobile viewport realities rather than desktop screenshots only
- treat loading, empty, error, hover, press, disabled, and destructive states as part of the product

## Rules

- Do not chase "premium" through glow, blur, and gradients alone.
- Do not accept a layout just because it is tidy if it still feels generic.
- Prefer intentional asymmetry or rhythm only when it improves the product, not as decoration.
