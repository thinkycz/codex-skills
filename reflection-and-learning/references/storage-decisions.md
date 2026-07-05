# Storage Decisions

Use this reference to choose where a lesson should live.

## Keep It Task-Local When

- it only matters for the current feature, bug, or verification pass
- it explains a narrow blocker or temporary workaround
- it is unlikely to help future unrelated work

## Put It In Project-Level Artifacts When

- it reflects a stable repo convention
- it would help future debugging, implementation, or verification work
- it describes a recurring integration, testing, or release pattern

## Escalate Carefully

- do not promote a weak lesson into broad project memory
- do not duplicate the same lesson across multiple artifacts
- prefer the narrowest durable home that will still make the next run better
