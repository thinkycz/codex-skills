---
name: teacha-delivery-menus
description: "Update or check Teacha menus and two-drink bundles in Wolt, Bolt Food or Foodora, including branch-specific descriptions, prices and options. GoKasa cashier work is separate."
version: 1.0.0
category: operations
sources:
  - Reviewed user-confirmed workflows and source artifacts
use_when:
  - "The user requests Teacha delivery-platform menu descriptions, categories, bundles or a read-only menu check."
avoid_when:
  - "The task only changes GoKasa cashier products, source recipes or delivery-partnership correspondence."
artifacts:
  - SKILL.md
  - agents/openai.yaml
  - agents/
  - references/
quality_gates:
  - "Each requested platform and branch is verified independently."
  - "Bundle totals and options match the approved components and discount."
  - "Saved, submitted, published and customer-visible states are reported separately."
---
# Teacha delivery menus

Use the current merchant interface or available connector for the named platforms. Read [the menu procedure](references/menus.md) before menu writes or bundle verification.

- Confirm platform, branch, exact items, sizes/volumes, category, component choices and pricing from the current request and catalog. Carry forward explicit session decisions without inventing new prices or promotion terms.
- Keep each platform/branch independent. A successful edit on one platform proves nothing about another catalog or its publication state.
- Preserve existing descriptions outside the requested change, availability, applicable modifiers and surcharge rules. Verify duplicate items/categories before creating new ones.
- Apply only the approved discount to the comparable current component total. Do not make an entry size appear discounted by silently changing the included sizes or charging mandatory extras later.
- Verify the persisted menu and available customer preview after saving. If moderation or publication is pending, report that state rather than claim the menu is live.
