---
name: native-desktop-delivery
description: Port or deliver a desktop application when native windows, menus, printing, device-local storage, offline recovery, or packaged installers require work beyond browser delivery. Use for desktop product implementation, not maintenance of installed developer tools.
version: 1.0.0
category: execution
sources:
  - current application code, platform contracts, build configuration, and installed-runtime evidence
use_when:
  - A web application is being adapted into an independent desktop product.
  - Desktop features, local data, offline behavior, or installers need implementation and verification.
avoid_when:
  - The task is installing or removing developer tools; use local-tooling-maintenance.
  - The task is ordinary browser-only delivery with no native behavior.
artifacts:
  - SKILL.md
  - agents/openai.yaml
  - agents/
  - references/
quality_gates:
  - Source preservation and target repositories are explicit before a port begins.
  - Native interactions and data boundaries are verified in the installed application where the claim requires it.
  - Each target platform has separate build, installation, runtime, signing, and notarization evidence.
  - Device-local state and portable data have explicit ownership and recovery rules.
---

# Native Desktop Delivery

Deliver the desktop behavior the user requested, including the installed runtime and its data boundaries.

## Boundary

Own desktop product implementation and packaging. Use `local-tooling-maintenance` for the lifecycle of installed development tools, not application feature delivery. Use `systematic-debugging` when a native failure needs root-cause investigation, `frontend-redesign-audit` for redesign diagnosis, and `release-readiness` for the final release verdict.

An approved specification remains the acceptance source. This skill supplies desktop-specific execution and verification, not permission to rewrite the web application, add synchronization, or publish installers.

## Workflow

1. **Map source and target.** Identify repositories, source revision, supported platforms/architectures, framework versions, and the desired desktop workflows. When an independent port is requested, preserve the source repository and its unrelated changes; record the baseline so preservation is verifiable.
2. **Map web behavior to native behavior.** Inventory navigation, application menus, shortcuts, window lifecycle, dialogs, file access, printing, external links, and bundled assets. Reuse business rules while replacing browser-only affordances where desktop behavior requires it. Do not turn every web page into a new native window.
3. **Define local data ownership.** Distinguish account-shared business data, session context, device settings, and credentials. Use [references/offline-data-and-sync.md](references/offline-data-and-sync.md) for persistence, backup portability, recovery, and synchronization only when sync is in scope.
4. **Implement bounded native slices.** Preserve normal keyboard behavior, focus, cancellation, and failure feedback. For NativePHP/Electron work, read [references/nativephp-electron.md](references/nativephp-electron.md) and inspect the actual installed package contracts before choosing APIs.
5. **Verify the installed artifact.** Use [references/installed-verification.md](references/installed-verification.md) for installation, writable paths, offline operation, printing, and platform-specific evidence. A browser server or development launcher does not prove packaged runtime behavior.
6. **Hand off with exact status.** Report delivered behavior and unresolved gaps per platform. Continue authorized work that can close gaps; identify external blockers without turning a successful cross-build into an unsupported runtime claim.

## Closeout

Use a row per target OS and architecture, with the artifact version/source identity and evidence for `built`, `installed`, `runtime-tested`, `signed`, and `notarized`. Use `not checked`, `blocked`, or `not applicable` where appropriate. Signing includes the identity/type; ad-hoc signing is not production signing. Notarization applies only to relevant platforms.

Keep platform limitations visible alongside download artifacts. Do not call an installer release-ready because its archive integrity check passes. Do not add a sync service, production signing, publication, or device migration beyond the user's scope.
