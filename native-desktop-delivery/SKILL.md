---
name: native-desktop-delivery
description: Deliver native desktop behavior, offline/device-local state and verifiable packaged installers.
version: 1.1.0
category: execution
sources:
  - Supplied task evidence and applicable project conventions
use_when:
  - Deliver native desktop behavior, offline/device-local state and verifiable packaged installers.
avoid_when:
  - The requested outcome belongs to another owner or exceeds the authorized scope.
artifacts:
  - SKILL.md
  - agents/openai.yaml
  - agents/
  - references/
quality_gates:
  - Evidence supports the stated outcome and limitations.
  - Selected mode, references and actions remain within authorization.
---

# Native Desktop Delivery

Identify the actual desktop stack, target platforms and native requirements before reusing browser assumptions. Separate device-local settings from account-global state. Validate offline recovery, durable writes, sync conflict/idempotency and platform printing/window/menu behavior where relevant. Keep writable state outside signed application bundles. Build with isolated synthetic configuration only within authorized scope and applicable rules; never overwrite real credentials. Distinguish source tests, built installer, signing/notarization, installed launch and exact native runtime verification. Do not claim packaged or cross-platform success from browser tests. Read platform and installed-verification guidance for packaging; select offline/sync guidance only for those flows.

## Working evidence

Reuse existing repository identity, relevant changes, acceptance criteria, canonical examples, required checks and blockers. Refresh only invalidated facts. Stay within the requested scope and applicable permissions; report observed evidence and remaining gaps separately.

## Selected detail

Read only what the current task needs; supporting references do not mandate extra workflow stages.

- [Installed Verification](references/installed-verification.md): for installed verification.
- [Nativephp Electron](references/nativephp-electron.md): for nativephp electron.
- [Offline Data And Sync](references/offline-data-and-sync.md): for offline data and sync.
