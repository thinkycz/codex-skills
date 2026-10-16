# Synology notes

Identify the exact model and currently installed DSM before proposing an update. A model's latest supported DSM can differ from the newest DSM release; the older DS211+ and newer DS124/DS223j questions illustrated why family-level answers are insufficient.

Use current Synology model compatibility, DSM release and Time Machine documentation. Check available SMB support, Time Machine share settings, account permissions, quota/capacity and the current Mac's requirements. Keep AFP support and ordinary SMB file access distinct from supported network backup behavior.

When external storage is involved, verify the specific model's ports and DSM/filesystem support, then inspect the attached device and share. Do not assume external USB storage automatically inherits the internal volume's backup features. Preserve existing filesystems and data; avoid formatting merely to make a suggested setup simpler.
