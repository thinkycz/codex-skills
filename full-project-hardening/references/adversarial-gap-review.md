# Adversarial Gap Review

Use this after integrated implementation on broad or high-risk hardening work.

## Reviewer Brief

Ask a fresh reviewer to work read-only and inspect:

- the original user outcome and acceptance artifacts
- the product-flow and audit matrices
- the integrated diff and current worktree state
- targeted and full-gate results
- runtime, browser, device, deployment, and external-provider evidence
- blockers, deferrals, and closeout wording

Ask for findings only, ordered by severity, with exact evidence and the missing verification or fix. Do not tell the reviewer that the implementation is expected to pass.

## Questions The Review Must Challenge

- Which requested flow or role is missing from the inventory?
- Which layer was implemented but not integrated into its consumer?
- Which success claim is stronger than its evidence?
- Which async or external handoff stops at an intermediate signal?
- Which generated, deployed, or installed artifact may differ from the source under review?
- Which P0 or P1 issue would block handoff despite green local checks?

The lead agent resolves, converts to an authorized fix slice, or explicitly defers every material finding. The reviewer does not own the release verdict.
