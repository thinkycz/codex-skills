# Linux feasibility and recoverable installation

Inventory model/board ID, CPU architecture, RAM/storage, GPU and graphics API support, network hardware and boot firmware. Separate CPU bitness from EFI/bootloader bitness on older Macs. Verify the intended distribution's current requirements against this exact hardware before preparing an installation.

The reviewed older Mac's graphics were a blocker for the requested Hyprland-based environment, even though an alternate lightweight desktop was plausible. Establish GPU compatibility before spending time installing a preferred shell. Present a supported alternative and let the user choose when it changes the intended experience; do not silently substitute distributions or desktops.

For Chromebooks, check the exact board's firmware support, write protection, storage and ChromeOS restoration requirements. Developer Mode, disk replacement and firmware flashing have different data/recovery consequences. Prepare required backups, firmware copies and recovery media before the authorized destructive step. Do not promise that ChromeOS can be restored merely because a recovery image exists; verify the boot-firmware restoration route too.

Verify boot/network/storage first, then the selected desktop/session, graphics, input and required device behavior. “The installer has internet” does not establish a working installed system. Report untested suspend, Wi-Fi, audio or other requested peripherals as unverified rather than inferring them from successful boot.
