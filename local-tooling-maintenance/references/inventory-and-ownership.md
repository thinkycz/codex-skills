# Inventory And Ownership

Inventory only the layers relevant to the named target, but do not assume the first match is complete.

## Installation And Runtime Layers

- application bundles and bundle identifiers
- package-manager formulas, casks, packages, global modules, and receipts
- command paths, shims, aliases, functions, and symlinks
- running processes, login items, launch agents or daemons, and background helpers
- editor extensions, IDE plugins, MCP servers, routers, and host overlays
- shell startup files and environment-selected configuration homes

## Data And Configuration Layers

- user, project, system, and plugin-provided configuration
- Application Support, Caches, preferences, logs, saved state, and update metadata
- models, repositories, prompts, session data, generated caches, and shared assets
- Keychain or credential-store entry metadata without secret values

## Ownership Questions

For every mutation candidate, answer:

- What exact product or registration owns it?
- Is it active, stale, generated, or durable user data?
- Does another preserved tool consume it?
- Can a process, plugin, shell hook, or higher-precedence config recreate it?
- Is the removal reversible, and what is the restore path?

No exact owner means no destructive mutation at that boundary.
