# Installed Artifact Verification

Record source revision, build identity, platform, architecture, installation location, and the exact artifact launched. Check that an old background process or development server is not providing the observed behavior.

## Runtime Checks

- Test installation and first launch with a disposable profile, then relaunch with existing data. Verify migrations, local workers/scheduling, and startup/recovery where they participate in the requested feature.
- Locate the runtime database, attachments, logs, cache, and settings. They must use supported writable user-data locations, not mutate the application bundle. Check signature integrity after launch where applicable; pre-launch signature success does not prove the bundle stays intact.
- Test required offline workflows with network access unavailable, including local assets, pending work, printer settings, backup, and recovery. Reconnect and inspect durable outcomes rather than only a success toast.
- Exercise menus, shortcuts, resize/scroll behavior, modal focus, print/export cancellation, and the affected business flow in the installed app. Run hardware-specific checks only within authorization and label unavailable hardware evidence separately.
- Test supported upgrade and restore paths with disposable data when persistence changes. A fresh empty installation does not prove existing-profile compatibility.

## Platform Evidence

| Platform / architecture | Artifact identity | Built | Installed | Runtime-tested | Signed: type/identity | Notarized | Remaining evidence |
| --- | --- | --- | --- | --- | --- | --- | --- |

Use observed results or `not checked`, `blocked`, and `not applicable`. Cross-compiling a Windows installer on macOS establishes only build evidence. Archive/checksum validation establishes artifact integrity, not successful installation or Windows runtime behavior. Linux/Windows do not inherit macOS runtime evidence; macOS notarization must be verified independently of signing.

If only unsigned development artifacts can be produced, deliver them with that status and continue locally testable work. Missing release credentials block production signing, not every implementation step. Publication and production rollout remain separate actions governed by the user's authorization.
