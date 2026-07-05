# Routing Fixture Maintenance

Add new routing fixtures after real work, not just hypothetical examples.

## What To Capture

- the user-facing prompt or a sanitized version of it
- the expected owner skill
- the overlap cluster it belongs to
- why the prompt was easy or hard to route

## Good Fixture Candidates

- prompts that almost routed to the wrong owner
- prompts that needed a boundary clarification before the right skill became obvious
- prompts that exposed a missing handoff
- prompts that looked similar but should resolve to different owners

## Avoid

- synthetic prompts that do not resemble real requests
- overly stack-specific prompts unless that stack difference actually matters to routing
- duplicates that do not teach a new routing distinction

## Workflow

1. Add the prompt to the right cluster in `skill-routing-fixtures.json`.
2. Keep the prompt short, realistic, and close to the user's phrasing.
3. Record the expected owner, not a whole skill chain.
4. Run `python3 /Users/longdo/.agents/skills/scripts/check_skill_routing.py`.
5. Regenerate the catalog and stocktake after meaningful fixture growth.
