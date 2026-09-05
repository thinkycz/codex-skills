# Docs Layout

Use markdown files under `/docs` only after verifying the owning repository root.

## Repository-Root Preflight

1. Run `git rev-parse --show-toplevel` or the repository's equivalent from the candidate docs home.
2. Confirm `/docs` will be inside that root.
3. Confirm the target is not ignored and will appear as tracked or intended new content in version-control status.
4. Record the owning repository when the workspace contains more than one repo.

If a shared parent is not a repository, prefer a clearly owned tracked coordination repo. Otherwise keep repository-specific docs in each affected repo and link them with repo/commit mappings. If neither is safe to infer, do not create uncommittable “durable” docs; keep minimal chat state until the user selects a home. Only create untracked workspace docs when explicitly requested, and label them as untracked.

## Default Structure

- `/docs/specs/`
- `/docs/plans/`
- `/docs/progress/`
- `/docs/verification/`

Create missing folders as needed during real execution.

## Typical Files

### `/docs/specs/`

- source summary
- clarified decisions
- normalized requirements

### `/docs/plans/`

- phased implementation plan
- roadmap index when multiple plan files exist

### `/docs/progress/`

- phase tracker
- traceability matrix
- blocker index

### `/docs/verification/`

- verification report
- domain-specific compliance matrix if needed

## Naming Guidance

- prefix with `YYYY-MM-DD-`
- use one stable topic slug
- prefer one primary file per purpose
