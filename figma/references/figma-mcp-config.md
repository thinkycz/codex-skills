# Figma access troubleshooting

Inspect the active host's supported Figma connection and available tools before changing configuration. Reuse a configured plugin or connector when available. Setup instructions and authentication options vary by host/version; inspect local configuration and current official documentation when the local contract is insufficient. Never print bearer tokens or copy real credentials into logs, skills or synthetic fixtures.

Check only whether the required credential is present and which process/configuration source supplies it. Change registration or persistent shell configuration only when setup changes are authorized, preserving other entries and applicable host safeguards. Confirm access with a read-only call against the requested source. Do not add obsolete feature flags or invented region headers from a static example.
