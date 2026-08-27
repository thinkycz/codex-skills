# Stage Detection

Use these evidence cues when deciding the current lifecycle stage.

- `brainstorming`
  Product direction or UX behavior is still ambiguous and no stable product artifact exists yet.
- `source or design intake`
  A design source exists, but it has not been normalized into usable implementation context.
- `spec or PRD`
  Source material exists, but the written product artifact is missing, weak, or not implementation-ready.
- `delivery planning`
  Intent is clear, but phased implementation docs or a traceable roadmap are still missing.
- `execution`
  `/docs/plans` or `/docs/progress` already exist and the next problem is continuation, resumption, or bounded implementation.
- `hardening`
  An existing product is substantially implemented, but the user wants comprehensive cross-stack assessment, prioritized fixes, full-flow testing, and production-readiness improvement rather than proof of one narrow claim.
- `fidelity and verification`
  Implementation exists and the remaining work is parity, QA, or proof-oriented.
- `release readiness`
  Implementation is substantially complete and the main question is go, no-go, or handoff readiness.
- `reflection and learning`
  Execution and verification are done enough that the next high-value step is preserving lessons or guardrails.

If multiple stages are present, choose the earliest incomplete stage that unblocks the rest of the lifecycle. Do not route a broad audit-to-fix request directly to fidelity, verification, or release readiness when hardening work is still expected.
