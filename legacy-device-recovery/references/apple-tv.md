# Apple TV jailbreak and Kodi recovery

The reviewed successful case was an Apple TV A1469 on software 7.9 using Blackb0x, followed by recovery of Kodi 14.2. Treat those as dated examples; verify exact current model/software and official tool guidance before selecting a payload. Apple TV 3 is not modern tvOS.

## Detection and installation

- Establish USB detection, data-capable cable/adapter, power/HDMI state and DFU requirements from the current guide. If a host guide specifies Intel, distinguish that documented support scope from observed Apple-silicon behavior; neither assume success nor reject the attempt without device evidence.
- If the device is missing over USB, resolve detection before repeatedly running a jailbreak. Keep the host unlocked and handle its accessory prompt when applicable. Follow model-specific remote/button instructions rather than generalizing them.
- A reboot handoff or “Finished installation” is intermediate evidence. Rediscover the device, verify authorized SSH/package state where applicable, then confirm Kodi appears and launches. Diagnose missing packages before rerunning the entire jailbreak.

## Add-on diagnosis

An empty repository and an incompatible add-on are separate issues. Inspect repository settings, source address and refresh behavior; the reviewed empty-catalog repair used the official direct download server. Re-derive the correct current URL and legacy repository layout rather than embedding a guessed feed.

Verify categories and entries in the Kodi UI after a repair. Then check the requested add-on's Kodi/Python dependencies. The reviewed Kodi 14.2 environment could populate its catalog while remaining unable to run a modern Python-3 YouTube add-on. Do not report that add-on working from catalog visibility alone or propose installing an incompatible package. Explain supported alternatives within the user's requested goal.
