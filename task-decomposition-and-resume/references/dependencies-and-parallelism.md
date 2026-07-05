# Dependencies And Parallelism

Use this reference when deciding execution order.

## Dependency Questions

- what must exist before this slice can start
- what does this slice unblock
- what blocker or external access still prevents progress
- what verification must happen before the next slice is safe

## Parallelism Rule

- default to one active slice
- allow parallel slices only when they do not depend on each other and do not fight over the same write surface
- if parallel work is used, record the split clearly in the plan or tracker
