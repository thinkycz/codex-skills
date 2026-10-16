---
name: teacha-inventory-review
description: "Review Teacha or StockFlow historical inventory counts, stock movements and recipe context without changing stock. Recipe authoring and live POS menus are separate tasks."
version: 1.0.0
category: operations
sources:
  - Reviewed user-confirmed workflows and source artifacts
use_when:
  - "The user asks to compare inventory counts, expected stock, movement history or recipe-related discrepancies."
avoid_when:
  - "The requested outcome is entering counts, closing a stocktake, changing recipes or editing POS products."
artifacts:
  - SKILL.md
  - agents/openai.yaml
  - agents/
  - references/
quality_gates:
  - "Comparisons use the same branch, item, unit and observation period."
  - "Missing evidence stays unknown; discrepancies are not relabeled as proven consumption."
---
# Teacha inventory review

Review the requested stock evidence without changing counts or movements. Read [the comparison procedure](references/compare.md) when comparing stocktakes or explaining discrepancies.

- Confirm branch, count/session identity, dates and units. Keep historical snapshots separate from current stock and open drafts.
- Compare physical count against the relevant expected quantity and intervening movements. A difference between two counts alone is not proof of usage, waste or theft.
- Use current approved recipe content only to explain possible ingredient relationships or conversions. Recipe yields do not prove actual sales or staff preparation.
- Return a concise item/unit/expected/counted/difference/evidence table. Separate observations, plausible explanations and missing records; do not invent quantities to close a gap.
- A review does not authorize starting or closing a stocktake, changing classifications, entering adjustments or editing recipes. Hand off a separately requested mutation to the appropriate current workflow.
