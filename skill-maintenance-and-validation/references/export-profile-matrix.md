# Export profiles

- Codex-native: complete package directories, metadata, references, scripts and assets.
- Universal folder: complete local packages and required cross-package/root support files, preserving relative layout. Tools and runtimes are still external.
- Flattened Markdown: linked text dependencies resolved into deduplicated anchors; executable listings do not install scripts. Binary assets and host/runtime requirements are disclosed.

Choose by consumer needs, not file count. The exporter requires an explicit new destination outside the source tree, excludes vendor packages by default, and never destructively replaces an existing destination.
