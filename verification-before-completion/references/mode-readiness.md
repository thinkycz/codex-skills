# Readiness

Assess evidence without changing code or deploying. Report ready, ready with explicit limitations, or blocked against the requested handoff/release target. Check requirement coverage, remaining blockers, docs freshness and environment identity. Missing live or packaged verification remains a limitation even when every automated test passes. Do not treat required blocked integrations as post-MVP work without accepted deferral.

## Selected detail

When deployment failed, recommend an isolated replay of the actual install/build/cache/startup commands with the intended runtime and synthetic configuration. Inspect the failed stage before changing otherwise verified source. Require successful rollout identity and the original live path before claiming live resolution; assessment alone does not authorize deployment. Read [deployment smoke](deployment-smoke.md) for this case.

Read only the reference matching the current question; these are not a mandatory sequence.

- [Example Output](readiness-example-output.md): for example output.
