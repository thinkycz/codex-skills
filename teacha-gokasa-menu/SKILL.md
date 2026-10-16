---
name: teacha-gokasa-menu
description: Add or update Teacha drinks in GoKasa for one or both branches, including prices, sale groups, cashier buttons, sugar, ice and topping options. Use for authorized live menu changes or read-only checks; StockFlow recipe editing is a separate task.
version: 1.0.0
category: operations
sources:
  - User-confirmed Teacha GoKasa workflow and live UI verification on 2026-10-16
use_when:
  - The user asks to add or update drinks in Teacha GoKasa or check their cashier options.
avoid_when:
  - The task only changes StockFlow recipes or source code.
artifacts:
  - SKILL.md
  - agents/
  - references/
quality_gates:
  - Verify each requested branch independently and keep its existing products intact.
  - Confirm saved names, prices, categories, cashier buttons and applicable modifier options.
  - Leave no verification items in the receipt and do not complete a sale.
---

# Teacha GoKasa menu

Complete the requested menu change in the live GoKasa UI and verify it on each requested branch's cashier screen. Use the browser tools available in the session; for the established Teacha workflow, use the logged-in Google Chrome session.

Read [references/teacha-ui.md](references/teacha-ui.md) when locating branch accounts or navigating the GoKasa forms. Its branch details and item codes are dated observations, not values to assume are still current.

## Establish the requested change

- Record drink names, hot/cold variants, target branches, categories, prices in Kč and modifier requirements. Reuse explicit decisions in the current conversation, including later corrections. Ask only for missing material details; do not infer new prices from an older drink.
- For the established Teacha convention, cold specials belong in `SPECIALS`; hot versions belong in `HOT DRINKS`. Keep hot names distinguishable, following the branch's existing `(Hot)` naming. User instructions override these defaults.
- Sugar and toppings follow corresponding drinks in that branch/category. Hot drinks have no ice selector; cold drinks retain the applicable regular/less/no-ice options. Do not assign every available topping indiscriminately or change surcharges without a request.
- If the user refers to StockFlow recipes, use the approved recipe or developer-managed Markdown as product information. A GoKasa request alone does not authorize editing recipes, changing their prices, committing code, or messaging staff.

## Work one branch at a time

1. Confirm the active account and branch in the UI. Both branches can use the same domain with different logins and independent catalogs. Switching may require signing out and signing in to the other account; it is not necessarily a different URL or an in-app branch selector. Use an existing authorized login or let the user sign in when credentials are unavailable. Never store credentials in this skill.
2. Inspect the current branch's catalog for duplicates and occupied EAN/PLU codes. Reuse a matching existing product when updating it; select a verified unused code for a new product. Never copy another branch's numeric codes blindly. Check the product name when opening any existing code before editing it.
3. In `PLU Articles`, create/update the name, confirmed price and sale group. Match the relevant existing drink's unit and applicable group/tax setup; do not change global taxes or account configuration. Wait for the saved state. If saving is uncertain, search for the product before retrying creation.
4. Add the product's EAN to its matching cashier tab. Saving the catalog product does not itself guarantee a cashier button. Use the saved product's `Add to tab` control or `Quick Sale Buttons`; inspect the current tab first to avoid duplicates. Preserve existing buttons and order.
5. Inspect `Tables → Item modifications` for sugar and ice and `Tables → Item surcharges` for toppings. Assignments can use sale groups and/or EAN lists. A new item in the correct group may already inherit everything required. Change only missing assignments within scope; avoid widening options for unrelated drinks. Match the branch's equivalent hot/cold drink when interpreting exclusions.
6. Verify the saved product and cashier button before switching accounts. Keep a small per-branch record of names, EANs, prices, categories and verification status to avoid mixing catalogs.

## Verify the cashier workflow

For each new/changed drink on each requested branch:

- Close Settings and open the actual cashier tab. Verify the label, price and category.
- With an empty receipt, add one verification item, open its item options, and inspect the actual sugar percentages and surcharge choices. Confirm ice options for cold drinks and their absence for hot drinks. Group assignments alone are not proof of the final options.
- Remove only the verification items you added. Preserve any pre-existing customer order; if one is present, do not clear it for testing. Do not use Pay, complete a transaction or print a receipt.
- Save a screenshot showing the result and relevant branch context using the active browser tooling. Include useful screenshot evidence in the final reply when supported. Report which branches and drinks are verified, and identify any remaining blocker precisely.

If a tool blocks a write due to a possible EAN collision, stop that write and inspect the current branch's persisted records. A code occupied on one branch can be unused or refer to another product on the other branch. Retry only after fresh UI evidence resolves the concern, following the tool's review instructions; otherwise finish unaffected work and report the blocked action. Never rename or replace an unrelated product to make a code fit.
