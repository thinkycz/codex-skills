# Trello MCP Workflow

Use this reference when ticket evidence comes from Trello and MCP tools are available.

## Evidence Order

1. Resolve shortlinks first when needed.
   - Trello URLs often contain a shortlink such as `/c/abc12345/...`.
   - If `get_card` rejects the shortlink because it needs a 24-character card ID, call `trello_search` with the shortlink or title and use the returned card `id`.
2. Read the card detail with `get_card` and keep the card ID, title, URL, list, labels, and description visible in working notes.
3. Read comments with `trello_get_card_actions(filter: "commentCard")`.
4. Read attachments with `trello_get_card_attachments`.
5. Read checklists with `trello_get_card_checklists` when checklist state could affect acceptance.
6. Only after evidence gathering, inspect the repo and classify the card as implementation-needed, verification-only, blocked, or needs clarification.

## Prioritization

- Latest QA, customer, or reviewer comments override older descriptions when they conflict.
- Card titles are often shorthand; do not infer full acceptance from title alone.
- Attachments may contain the actual visual acceptance criteria even when the card description is empty.
- If another agent may have implemented the work, verify against current repo state before writing a fix plan.

## Common Pitfalls

- Public Trello URLs may not be readable through unauthenticated web or REST calls; prefer MCP credentials.
- Some Trello tools require the internal 24-character ID rather than the URL shortlink.
- Do not skip cards with empty descriptions; comments can contain the only actionable details.
- Preserve card IDs and titles in outputs so summaries can be pasted back to the board.
