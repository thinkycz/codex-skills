---
name: legacy-device-recovery
description: Recover an older Apple TV or repurpose an older Mac/Chromebook with Linux, using exact hardware and firmware evidence plus a recoverable installation path.
version: 1.0.0
category: device-support
sources:
  - Reviewed user-confirmed workflows and current source artifacts
use_when:
  - The user requests an Apple TV jailbreak/Kodi recovery or Linux repurposing on an older Mac or Chromebook.
avoid_when:
  - The task is Finder/Time Machine storage recovery, electrical rewiring, or only a device-specification lookup.
artifacts:
  - SKILL.md
  - agents/openai.yaml
  - references/
quality_gates:
  - Exact device, firmware, boot and graphics constraints are checked before choosing a procedure.
  - Authorized device changes have a concrete backup/recovery path.
  - Boot, application launch and requested functionality are verified separately.
---

# Legacy device recovery

Identify exact hardware, current software/firmware, the host computer, connections and the user's desired end state. Inspect what already works before reinstalling. Use current authoritative compatibility and recovery instructions; a similar model or an old chat is not enough to select firmware or an image.

## Modes

- **apple-tv** — Jailbreak/install recovery and Kodi add-on diagnosis. Read [Apple TV recovery](references/apple-tv.md).
- **linux** — Older Mac or Chromebook repurposing. Read [Linux feasibility and recovery](references/linux.md).

Before a disk or firmware write, establish the concrete data backup, correct target and restoration path. Keep reversible diagnosis within the authorized task; identify and obtain authorization for destructive steps not already covered. Prefer one observable step at a time when the user operates a remote device. Preserve earlier answers and avoid asking again for known model or connection details.

Network storage troubleshooting belongs to `mac-network-storage-recovery`; simple model/spec comparisons belong to `evidence-discovery`. Do not extend these modes to mains wiring or unrelated electronics repair.
