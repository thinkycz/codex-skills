# Verify

Match each acceptance claim to evidence from the affected code and exact runtime. Before tests/browser work confirm architecture gates, asset build, server identity, isolated test database and runtime dependencies. Reuse successful checks with unchanged inputs; rerun affected checks after code, configuration, dependency, data, environment or scope changes. Complete repository-required gates. Never substitute a screenshot, mock, compilation or unit test for an untested integration claim. Separate tested source, built artifact, installed runtime and production status.

When the repository names an exact gate such as `make check`, report that command's result separately from targeted tests, build checks and skips. Reuse passing checks only while the relevant inputs remain unchanged. A known audit failure still makes the exact gate fail, even when feature tests pass.

For a requested commit/push closeout, read [Git release evidence](git-release-evidence.md). This reference supplies evidence requirements within existing authorization; verification alone does not authorize a release.

## Selected detail

Read only the reference matching the current question; these are not a mandatory sequence.

- [Closeout Language](closeout-language.md): for closeout language.
- [Deployment Smoke](deployment-smoke.md): for deployment smoke.
- [Exact Path And Parity](exact-path-and-parity.md): for exact path and parity.
- [Verification Layers](verification-layers.md): for verification layers.
