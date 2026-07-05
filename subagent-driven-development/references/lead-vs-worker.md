# Lead Vs Worker

Use this split when applying `subagent-driven-development`.

Lead agent ownership:
- repo grounding and convention discovery
- source-of-truth interpretation
- task decomposition and dependency order
- deciding what to delegate and what to keep local
- cross-slice integration decisions
- final verification and completion claims
- approval boundaries for delegation, scope shifts, and completion claims

Worker ownership:
- well-scoped implementation slices
- repetitive or mechanical edits
- isolated test-writing tasks
- bounded refactors
- narrow follow-up fixes that do not require broad architectural judgment

Workers should not silently redefine scope, architecture, or ownership.
