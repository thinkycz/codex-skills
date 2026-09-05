# NativePHP And Electron Adaptation

Inspect lockfiles, package code/types, generated shell configuration, and build scripts for the installed versions. Consult current official documentation when the local contract is insufficient. Do not copy APIs or navigation examples from a different framework major version.

## Native Interaction

- Check the application menu in the packaged app, including the macOS application name and conventional application/File/Edit/Window actions where applicable. Verify shortcut ownership; preserve text-editing shortcuts and avoid duplicate handlers in web and native layers.
- Inspect focused-window commands, reused window IDs, close/reopen behavior, external-link handling, and modal lifetime. Test Escape, cancellation, focus return, and opening the same dialog twice.
- Use the existing framework navigation primitives. When adapting density, inspect actual desktop window dimensions, long content, and window resizing. Test overlays outside nested clipping/stacking containers.
- Bundle assets required offline, including fonts, CSS, print styles, and icons. Test without network access rather than assuming that assets cached by a development browser are bundled.

## Printing

- Define document profiles from requirements: page size, orientation, margins, scaling, and printer selection. Do not assume receipts use the same profile as full-page documents.
- Store physical printer bindings per device. Refresh discovery and handle missing, renamed, or disconnected printers with explicit feedback and a supported selection/dialog fallback.
- Keep preview, direct printing, printing with a dialog, and PDF export distinct. Respect the requested defaults; avoid unsolicited physical print jobs during QA. A cancelled dialog proves dialog behavior, not successful paper output.
- Verify page geometry and pagination using actual generated output. Label hardware printing unverified until observed on the intended printer.

## Native Boundaries

- Keep privileged native capabilities behind narrow interfaces. Inspect local HTTP/IPC authentication and origin boundaries; a desktop shell does not make arbitrary local requests trusted.
- Keep secrets in the platform-supported secure store or an approved device-bound mechanism. Report locked/unavailable key stores accurately and test recovery without weakening protection.
- Inspect generated Electron wrappers before editing; preserve regeneration compatibility. Prefer the project's supported extension points to patches that disappear on the next build.
