# Deployment Smoke Evidence

Use when a change affects dependencies, framework versions, build output, deployment scripts, caches, migrations, or startup, or when a local fix seems absent in the deployed product.

## Before Push Or Deployment Handoff

1. Read the actual CI/deployment entrypoint and its called scripts. Identify required runtime and package-manager versions, dependency flags, production build, cache generation, migration ordering, and worker restarts.
2. Confirm the repository's required lockfiles are tracked and available in a clean checkout. Do not assume a developer's installed dependencies reproduce the deployment.
3. Replay applicable install/build/cache/startup commands in an isolated checkout or disposable environment using the intended runtime versions. Include production-mode environment semantics without copying production secrets. For Laravel, inspect the project's actual configuration, route, and view cache commands rather than assuming a generic command list.
4. Separate safe build checks from destructive seeds, real migrations, service restarts, and external calls. Never run the deployment script against a live target merely to test its build section. When isolation is unavailable, report the untested stage and the static evidence.
5. Record command, runtime, source identity, exit status, and the first failing stage. Fix a demonstrated deployment-command incompatibility within scope; do not mask it with a locally installed dependency or unsupported flag.

## After An Authorized Deployment

Observe successful deployment completion, the intended artifact/commit, required migration state, and running process/worker identity. Then replay the affected user path. If deployment failed, investigate that failure before rewriting an otherwise locally verified feature.

| Claim | Minimum evidence |
| --- | --- |
| Source verified | Relevant regression and repository checks on the reported source. |
| Production command path verified | Isolated replay of applicable install/build/cache/startup stages. |
| Deployed | Successful rollout and intended artifact observed on the target. |
| Live behavior verified | Affected user path observed against that target, including dependent workers/providers where relevant. |

These are separate claims. A local smoke pass does not authorize deployment; a pushed commit does not establish deployment; a failed rollout does not establish that the new code ran.
