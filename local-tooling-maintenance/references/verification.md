# Local Tooling Verification

Use one row per applicable lifecycle layer.

| Layer | Expected state | Check | Observed state | Verdict |
| --- | --- | --- | --- | --- |
| App bundle and identifier |  |  |  |  |
| Command and package receipt |  |  |  |  |
| Process and launch service |  |  |  |  |
| Shell hook and environment home |  |  |  |  |
| Editor, MCP, plugin, or router registration |  |  |  |  |
| User, project, system, and host config |  |  |  |  |
| Credential entry metadata |  |  |  |  |
| Support, cache, preference, log, and state paths |  |  |  |  |
| Named preserved integrations |  |  |  |  |

## Closeout Rules

- Verify absence with more than one signal when a layer can be recreated or shadowed.
- Verify the actual active configuration source, not only the file the operator expected to be active.
- For services, compare the loaded unit, executable, working directory, user, and current process rather than only the source plist or unit file.
- For credentials, report entry presence, account/service identifiers when safe, and whether removal was verified; never reveal secret values.
- Record Trash or backup location and restore steps for recoverable removals.
- State which layers were not applicable or could not be observed.
