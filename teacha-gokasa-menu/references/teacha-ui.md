# Teacha GoKasa UI notes

These observations were verified on 2026-10-16. Recheck the active UI before using identifiers or locators.

## Accounts and catalogs

- Both branches used `https://teachamatchasro.gokasa.cz/`.
- The account labeled `Teacha Matcha s.r.o.` had the Point of Sale address `Na Pankráci 1727/86`, Praha 4: Pankrác.
- The other account was labeled `Teacha Matcha s.r.o. #2`. The user switched accounts by signing out and signing in, on the same domain. Its placeholder address did not reliably identify the physical location; do not invent a branch name from it.
- `Point of Sale` showed another site's header, but that was not a working account switch. Clicking the profile opened the sign-out confirmation.
- Catalog numbering differed. Pankrác's Taro Milk Tea (Hot) was EAN 44; branch #2's was EAN 41. The completed Bueno Hojicha additions used 47/48 at Pankrác and 44/45 at #2. These are occupied historical examples, not codes reserved for future drinks.
- The final user correction set both Bueno Hojicha versions to 160 Kč. Do not treat that as a price rule for future drinks.

## Forms and navigation

- Settings → `PLU Articles` → `Create New PLU`: EAN, NAME, PRICE, GROUP; amount 1 and PCS were used for drinks. Existing hot drink and Specials groups were 9 and 6 respectively on both branches. Confirm group labels and current values rather than relying on numbers.
- Wait for `Saved` after saving. New-product forms then offered `Add to tab` plus a tab selector. Select the desired tab before adding.
- Alternative: Settings → `Quick Sale Buttons` → desired tab → `Add button`; enter the saved EAN and save. The form can initially say `PLU not found`; verify the resolved name and saved state rather than creating another product because of that initial label.
- `Tables → Item modifications` contained sugar and ice settings; `Tables → Item surcharges` contained topping links. Group and EAN assignments were separate fields, with semicolon-delimited lists.
- The branches had different topping catalogs. Copy from equivalent drinks on the current branch; do not synchronize their entire topping catalogs as an incidental menu edit.

## Browser interaction pitfalls

- Follow the current browser tool documentation. Do not reuse old accessibility indices after UI changes or access hidden application state, browser credentials, private endpoints or network mutation APIs.
- DOM snapshots sometimes included an off-screen Settings panel. A locator could match its text even while the cashier screen was foreground. When a click has no effect, verify visibility/state with a targeted observation or screenshot before retrying. Do not keep clicking stale text.
- Duplicate labels could match both catalog rows and cashier buttons. Scope actions to the currently intended panel. In this observed UI, `#tabs` held cashier buttons, `#cp-body` held Settings content and `#curtain` held the modal. Re-observe these selectors before reuse.
- The Settings close control was `#cp-header .close`; modal close was a button inside `#curtain`. A generic × could also match the calculator multiplication key.
- The existing-item EAN field was disabled. A search by an exact code opened its product; confirm the name before editing. Search fields enforced formatting, so an invalid query could leave the form unchanged with a browser validation message. Inspect the message rather than assuming a save/search succeeded.
- For cashier verification, clicking a product added a draft item. Clicking that item's total (`.si-total` in the observed UI) expanded the row; `Sale item modifications` opened its sugar, ice and topping options. The item's remove button (`.si-remove`) removed that verification row without completing a sale.

Re-derive locators from current rendered UI. The selectors above explain the observed navigation; they are not a substitute for checking current page state.
