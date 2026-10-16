---
name: mac-network-storage-recovery
description: Diagnose Mac Finder SMB access and Time Machine network destinations, including AirPort Time Capsule and Synology. Verify file access and backup completion as separate outcomes.
version: 1.0.1
category: device-support
sources:
  - Reviewed user-confirmed workflows and current source artifacts
use_when:
  - The user needs Mac access to a network drive or a working network Time Machine destination.
avoid_when:
  - The task is an application database backup or an unrelated firmware/OS installation.
  - The request is only a general product comparison without a storage-access task.
artifacts:
  - SKILL.md
  - agents/openai.yaml
  - agents/
  - references/
quality_gates:
  - Current device identity, macOS version and intended storage use are established.
  - Reachability, authentication, mounted file access and completed backup are distinguished.
  - Existing stored data and unrelated network configuration remain preserved.
---

# Mac network storage recovery

Start from the requested outcome: browsing files or completing Time Machine backups. Identify the device model, current firmware, Mac/macOS version, network path and observed failure. Recheck state after a reboot or account/network change; earlier IPs, credentials and successful checks are not current guarantees.

## Modes

- **access** — Diagnose and verify Finder SMB access. Read [Finder access](references/access.md), then the relevant [Time Capsule](references/time-capsule.md) or [Synology](references/synology.md) notes.
- **backup** — Verify the intended Time Machine target through an actual backup. Read [backup acceptance](references/backup.md) and the relevant device notes.

Inspect before changing configuration. Preserve disks, shares, backups, device credentials and unrelated router settings. An access request does not authorize formatting, resetting a device, broad permission changes, or enabling legacy protocols. Reuse authorized setup steps; explain any new destructive requirement and obtain scope for it before acting. Keep credentials in the device/app's authorized local entry flow, never in skill files or reports.
