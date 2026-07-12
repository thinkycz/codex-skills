# Trello MCP Workflow

Use this reference when ticket evidence comes from Trello and MCP tools are available.

## Evidence Order

1. Resolve shortlinks first when needed.
   - Trello URLs often contain a shortlink such as `/c/abc12345/...`.
   - If `get_card` rejects the shortlink because it needs a 24-character card ID, call `trello_search` with the shortlink or title and use the returned card `id`.
   - For the current Trello MCP search schema, use positive limits such as `cardsLimit: 10`, `boardsLimit: 1`, and `membersLimit: 1`. Zero board or member limits are schema-invalid.
   - Resolve independent shortlinks in parallel and keep a thread-local map of shortlink, internal card ID, title, and URL.
2. Read the card detail with `get_card` and keep the card ID, title, URL, list, labels, and description visible in working notes.
3. Read comments with `trello_get_card_actions(filter: "commentCard")`.
4. Read attachments with `trello_get_card_attachments`.
5. Read checklists with `trello_get_card_checklists` when checklist state could affect acceptance.
6. Follow related cards only when the requested card explicitly depends on them or their evidence is required to interpret acceptance. Read the related card's current details, comments, attachments, and checklists using the same evidence order.
7. Only after evidence gathering, inspect the repo and classify the card as implementation-needed, verification-only, blocked, or needs clarification.

## Efficient Retrieval

- After resolving IDs, fetch independent card details concurrently.
- For each resolved card, comments, attachments, and checklists may also be fetched concurrently when no call depends on another call's output.
- Reuse the stored internal ID for implementation, follow-up verification, and closeout comments.
- If a Trello call fails because its arguments are rejected before execution, correct it once to the known-safe positive-limit shape. Do not repeat the invalid call across every card.
- Keep related-card traversal bounded; dependency evidence should improve the contract, not turn intake into an unbounded board crawl.

## Prioritization

- Latest QA, customer, or reviewer comments override older descriptions when they conflict.
- Card titles are often shorthand; do not infer full acceptance from title alone.
- Attachments may contain the actual visual acceptance criteria even when the card description is empty.
- A linked or dependency card may define the authoritative enum, terminology, or prerequisite implementation; do not invent that contract from the referring card alone.
- If another agent may have implemented the work, verify against current repo state before writing a fix plan.

## Common Pitfalls

- Public Trello URLs may not be readable through unauthenticated web or REST calls; prefer MCP credentials.
- Some Trello tools require the internal 24-character ID rather than the URL shortlink.
- `boardsLimit: 0` and `membersLimit: 0` are rejected by the current Trello search tool; use positive limits even when only cards are needed.
- Do not skip cards with empty descriptions; comments can contain the only actionable details.
- Preserve card IDs and titles in outputs so summaries can be pasted back to the board.
