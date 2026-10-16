# Requested commit and push evidence

Apply this only when commit/push is requested or already authorized. Reuse that authorization for the same scope rather than asking again for each routine step. Preserve explicit repository requirements for dependency updates or other scope expansion.

Confirm repository identity, branch, remote and current changes before staging. Distinguish requested changes from unrelated work; “everything” applies to the established repository scope and is not authority to include credentials or unrelated repositories. Keep unrelated changes intact and avoid broad staging when the request is narrower.

Run the repository-required gate and applicable checks, or reuse valid results for unchanged inputs. State targeted success, full-gate failure, environment skips and accepted deferrals separately. Do not substitute unit/build success for an exact required gate. If a requirement prevents release, report its concrete source and the remaining action without inventing a different workflow.

Inspect the final staged diff, commit the intended scope and push to the verified intended remote when authorized. If the commit already exists, inspect its scope and remote state before creating another. A missing remote prevents a push claim; ask for its destination only after confirming none is configured. Do not fabricate a remote from project names or initialize a new repository merely to satisfy a push request.

Verify the resulting local commit and remote ref when claiming push completion. Report the actual branch/commit and any remaining local changes. Keep code push, deployment and live/provider acceptance as distinct outcomes.
