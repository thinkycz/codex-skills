---
name: stockflow-recipes
description: Add, revise or audit StockFlow developer-managed Markdown recipes, including ingredient logic, localized content, lookup and guided preparation. Live GoKasa menu changes belong to teacha-gokasa-menu.
version: 1.0.0
category: operations
sources:
  - Reviewed user-confirmed workflows and current source artifacts
use_when:
  - The request changes or checks StockFlow recipe content, variants or preparation guidance.
avoid_when:
  - The task only changes live GoKasa products, prices or cashier options.
  - The request is an unrelated cooking question or a general application redesign.
artifacts:
  - SKILL.md
  - agents/openai.yaml
  - references/
quality_gates:
  - Authored amounts, variants, recipe URLs and all supported languages remain consistent.
  - Ice and other ingredients appear in both the ingredient list and applicable method steps.
  - The current catalog validator and requested employee browser flows pass.
---

# StockFlow recipes

Maintain the source-file recipe library employees browse and follow. Read the current project's `AGENTS.md` and `resources/recipes/README.md`, then a close existing recipe and its locale entries. Repository documentation defines the current format; this skill supplies review criteria rather than a replacement schema.

Read [the authoring checklist](references/authoring.md) for source structure, formula review and employee-flow verification.

- Start from the user's supplied formula and later corrections. A named analog such as “same as Bueno Matcha” contributes its established preparation details, including ice, where applicable. Resolve conflicts with the source or user before inventing an amount, ingredient, time or temperature. Ask one focused formula question with meaningful options when a material value remains unknown.
- Keep recipes developer-managed and browse-only. A content update does not authorize restoring an in-app editor, database catalog or employee test workflow. Preserve permanent category/file URLs and existing authored variants.
- Keep official menu names intact while localizing preparation content and controls in English, Czech and Slovak according to the project's current catalog contract. Verify content as well as interface chrome.
- Recipes omit prices. Use `teacha-gokasa-menu` only when live menu work is also requested; carry approved product facts across without assuming authority to edit the other system.
- Run the repository's applicable catalog checks and required gate, then inspect the requested employee paths. Report source changes, browser evidence and any environment-limited checks separately. Preserve unrelated local changes.
