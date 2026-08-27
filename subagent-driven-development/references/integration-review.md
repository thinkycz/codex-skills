# Integration Review

Lead agent review should check:

- the worker stayed within scope
- the actual diff matches repo conventions and the canonical example files named in the brief
- generator or scaffold names, namespaces, output locations, and generated-file handling follow local policy
- upstream and downstream dependency contracts still agree
- the slice still fits the shared design
- nearby behavior did not regress
- targeted checks support the slice claim
- the integrated result satisfies the repository's exact full-project gate

Do not accept worker completion as final completion.

For broad or high-risk multi-slice work, follow lead integration with a fresh read-only adversarial review. Do not prime the reviewer with the expected answer. Resolve or explicitly defer material findings before release readiness.
