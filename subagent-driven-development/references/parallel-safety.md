# Parallel Safety

Parallel workers are safe only when:

- write scopes are disjoint
- dependency order is already known
- one worker does not block the other
- integration ownership remains central

Avoid parallelism when:

- both tasks touch the same shared layer
- one task defines the contract the other consumes
- the lead agent is still discovering the shape of the problem
