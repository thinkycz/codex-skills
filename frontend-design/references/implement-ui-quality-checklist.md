# UI Quality Checklist

Use this reference after screen coverage exists and before claiming high fidelity.

## Accessibility QA

- text contrast meets the intended accessibility bar, especially body text, muted text, badges, and overlays
- interactive elements have visible focus treatment
- reduced motion is respected where motion exists
- forms use visible labels and clear error states
- critical meaning is not conveyed by color alone
- keyboard and screen-reader basics work for the touched surfaces

## Interaction QA

- important actions do not rely on hover alone
- web interactions use obvious pointer affordance where appropriate
- press, hover, active, disabled, loading, and destructive states are visually clear
- long-running actions give feedback instead of appearing inert
- destructive actions are semantically and visually distinct from neutral or primary actions

## Typography And Layout QA

- body text stays readable at the chosen size
- line height supports reading instead of crowding text
- line length is controlled on wider layouts
- heading hierarchy is visually clear
- spacing follows a deliberate scale instead of arbitrary one-off values
- semantic tokens and reusable primitives are preferred over ad hoc styling when they preserve fidelity

## Motion QA

- default UI transitions usually stay in the 150-300ms range unless there is a reason to differ
- motion communicates hierarchy, cause, or state change instead of adding decoration only
- animations avoid layout-shift-heavy properties when transform or opacity can do the job
- reduced motion disables or softens non-essential animation
- the interface still feels responsive when animations are interrupted

## Anti-Pattern Checklist

- no emoji used as structural icons
- no accidental gray-on-gray or otherwise low-contrast core text
- no decorative-only animation that distracts from tasks
- no product-inappropriate "AI purple/pink" or novelty-heavy styling defaults where trust and clarity matter
- no mixed visual languages unless the design source clearly calls for it

## Closeout Rule

If this checklist still has failing items, the result may be `close`, `blocked`, or `unresolved`, but it should not be called 1:1 or final.
