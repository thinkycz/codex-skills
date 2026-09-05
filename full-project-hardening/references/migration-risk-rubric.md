# Risk Rubric

Use this when auditing migration or upgrade risk.

## Shared-Layer Risk

- wrappers, adapters, or helpers used widely
- config assumptions reused across modules
- serialization or schema layers consumed by many features

## Rollout Risk

- work that cannot safely ship incrementally
- changes that require ordered deployment or coordinated release
- fallback or rollback complexity

## Verification Risk

- flows that need more than lint or build checks
- user-visible journeys likely to break silently
- integrations whose failure would not be obvious from static checks

## Rule

- If a shared layer changes, assume the audit must search for every major consumer before implementation.
