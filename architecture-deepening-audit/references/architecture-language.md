# Architecture Language

Use precise terms so the audit stays actionable.

- Module: any unit that hides implementation behind an interface. It may be a file, package, class, function set, service, route layer, state machine, or adapter.
- Interface: the surface other code must understand to use the module. It includes signatures, data shapes, invariants, expected side effects, errors, and sequencing rules.
- Implementation: the hidden work behind the interface.
- Depth: how much implementation complexity is hidden behind a simple, stable interface. Depth is a property of the interface, not a reward for complicated internals.
- Shallow module: a module whose interface is nearly as complex as the implementation it hides.
- Seam: a place where independent implementations can meet through a stable contract.
- Adapter: implementation that translates a dependency, protocol, or external shape into the local domain model.
- Leverage: how much caller complexity disappears when the module is used.
- Locality: how much related knowledge lives together instead of being spread across callers.

Useful tests:

- Deletion test: if deleting the module forces callers to recreate detailed choreography, the module may be deep. If callers barely change, it may be shallow.
- Interface test: if tests must know many internal steps, the interface may be exposing implementation.
- Adapter test: one adapter usually means a hypothetical seam; two or more real adapters make the seam more credible.

Avoid fuzzy replacements such as "component", "unit", "service", "API", or "boundary" when a more precise term is available.
