# AirPort Time Capsule notes

The reviewed recovery used AirPort Utility to identify a Time Capsule, then TimeCapsuleSMB's managed Samba deployment. After the device reboot, the tool's Checkup was clean and Finder mounted the intended Data share. These describe a past successful route, not the current device's state or a required check count.

- Confirm the exact device and its current configuration before acting. A reachable old SMB service can still fail Finder negotiation or mounting on a modern Mac. Check current macOS and vendor/project compatibility rather than assuming AFP or legacy SMB is acceptable.
- When using TimeCapsuleSMB, inspect its current official documentation and installed app. Establish whether the requested install is an initial deployment or recovery of an existing managed runtime; do not deploy another copy blindly.
- Use the app's authorized local password entry, follow its deployment/reboot state, then run current diagnostics and verify the actual Finder share. A tool log by itself does not establish usable file access.
- If the user only requests file access, preserve bridge/Wi-Fi/router configuration. Switching use and storage access are separate decisions.

For backups, verify the Time Machine contract independently using backup mode. A modern Samba file share does not by itself prove that the device is a valid Time Machine destination.
