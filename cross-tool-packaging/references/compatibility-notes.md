# Compatibility Notes

Document what the target bundle keeps and what it loses.

## Questions To Answer

- Is the export Codex-native or universal?
- Are references preserved, omitted, or inlined?
- Is agent metadata preserved?
- Are scripts preserved, omitted, or embedded as text?
- How are binary assets handled?
- Are `.system` skills included?

## Rules

- Prefer explicit compatibility notes over implicit assumptions.
- If a format degrades fidelity, say so plainly.
- Make regeneration commands easy to rerun.
