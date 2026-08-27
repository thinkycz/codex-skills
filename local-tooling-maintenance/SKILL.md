---
name: local-tooling-maintenance
description: Safely install, update, disable, uninstall, or clean up local AI tools, editor integrations, routers, plugins, CLIs, layered configuration, credentials, and leftovers. Use when lifecycle mutation requires exact ownership mapping, shared-data protection, recoverable removal, and verification across every registration layer.
version: 1.0.0
category: operations
sources:
  - installed applications, CLIs, package receipts, processes, shell hooks, editor registrations, configuration layers, and credential metadata
  - recurring local Codex router, MCP, editor-plugin, CLI, and application cleanup patterns from recent work
use_when:
  - The user asks to install, disable, uninstall, purge, or repair local development or AI tooling.
  - A tool appears removed or inactive but layered registrations, processes, caches, credentials, or shared data may remain.
avoid_when:
  - The task is only read-only inventory or evidence gathering; use search-first.
  - The request concerns ordinary project dependencies or application code rather than host-level tooling lifecycle.
artifacts:
  - SKILL.md
  - agents/openai.yaml
  - agents/
  - references/
quality_gates:
  - Installed or active state is distinguished from stale metadata and leftovers.
  - Shared ownership is proven before any application, configuration, credential, cache, or data path is mutated.
  - Removal is recoverable where practical and exact removed targets are reported.
  - Verification covers every relevant registration layer and confirms named preserved integrations still work.
  - Secret values are never exposed in logs, notes, or final reporting.
---

# Local Tooling Maintenance

Treat local developer and AI tooling as a layered lifecycle, not as one app bundle or one config file.

This skill owns host-level installation, update, disabling, uninstall, and cleanup work for apps, CLIs, editor integrations, MCP registrations, routers, plugins, shell hooks, launch items, credentials, caches, and related data.

## Boundary

- Own lifecycle mutation after the target, ownership, and preservation requirements are understood.
- Use `search-first` for a read-only inventory when the user has not yet authorized install, uninstall, cleanup, or configuration changes.
- Hand off from `search-first` to this skill as soon as discovery becomes host-level mutation.
- Do not use this skill for ordinary repository dependencies, application migrations, or `.env` normalization.
- Apply `env-file-mutation-guard` whenever a requested tooling change could touch `.env*` content.

## Workflow

### 1. Resolve The Exact Target

- Identify the product, vendor, bundle identifier, command names, package manager entries, editor integrations, router or plugin names, and known configuration homes.
- Distinguish the currently installed or active tool from stale catalog entries, cached metadata, old receipts, and unrelated products with similar names.
- Inspect all relevant installation channels before concluding what exists.
- Record what the user wants removed, what must remain, and whether account data or credentials are in scope.

Use [references/inventory-and-ownership.md](references/inventory-and-ownership.md) for the inventory surface.

### 2. Build An Ownership And Dependency Map

- Trace each candidate path or registration to an exact owner before mutation.
- Resolve layered configuration in precedence order: active host overlay, environment-selected homes such as `CODEX_HOME`, user config, project config, system config, plugin-provided registrations, and generated caches.
- Identify shared directories, shared editor homes, common credential stores, reusable runtimes, and integrations consumed by more than one tool.
- Treat broad Application Support, Caches, preferences, extension, plugin, and configuration directories as shared until evidence proves otherwise.
- Identify running processes, launch services, background helpers, and shell hooks that could recreate removed state.

If ownership is ambiguous or a shared path contains preserved data, stop mutation at that boundary and report the exact uncertainty.

### 3. Plan A Recoverable Mutation

- List exact targets and the verification check for each target before changing state.
- Prefer vendor uninstallers or package-manager removal for registered packages.
- Prefer moving user-level files into one timestamped Trash bundle that preserves relative paths when practical.
- Separate disposable caches from durable projects, account data, prompts, settings, models, credentials, and shared assets.
- Preserve unrelated host, router, editor, plugin, and shared-tool components.
- Never broaden a target through an unresolved variable, wildcard, home directory, or guessed vendor folder.

Ask for additional authority before destructive credential removal, broad shared-data deletion, or any materially different target not already covered by the user request.

### 4. Apply The Smallest Complete Change

- Stop or disable only target-owned processes and launch items.
- Remove or update exact app bundles, packages, commands, plugins, registrations, hooks, and config entries in dependency-aware order.
- Do not edit `.env*` files unless the user explicitly requested it and `env-file-mutation-guard` permits the exact change.
- Never print secret contents while examining Keychain or credential metadata.
- Keep a concise record of changed targets, preserved shared targets, and recoverability.

### 5. Verify Every Relevant Layer

After mutation, verify applicable checks for:

- application bundle and bundle identifier
- command resolution and package-manager receipt
- running process, launch item, and background helper
- shell startup hook and environment-selected config home
- editor extension, MCP/server registration, plugin, router, and host overlay
- user, project, system, and plugin-provided config sources
- exact credential entry presence or absence without reading secret values
- target-owned Application Support, cache, preference, log, and state paths

Then verify that every named preserved integration still starts, resolves, or remains registered as intended. Use [references/verification.md](references/verification.md) for the closeout matrix.

Apply `verification-before-completion` to compare the layered evidence to the exact install, removal, cleanup, or configuration claim before reporting success.

## Status And Reporting

Report separately:

- removed or changed and verified
- moved to Trash and recoverable, including the bundle location
- preserved because it is shared or outside scope
- stale metadata that is inactive but intentionally left
- blocked or uncertain ownership boundaries
- manual restart, sign-in, or editor reload still required

Do not say a tool is “fully removed” unless all applicable layers were checked.

## Rules

- Do not infer ownership from a folder name alone.
- Do not delete a broad Application Support, Caches, editor, config, or credential directory because one target used part of it.
- Do not equate “command not found” with complete uninstall.
- Do not equate an absent app bundle with removal of plugins, processes, shell hooks, credentials, or layered configuration.
- Do not remove shared runtimes or data until every owner is mapped.
- Do not expose secrets while verifying credentials.

## References

- [references/inventory-and-ownership.md](references/inventory-and-ownership.md)
  Use to inventory installation channels, layered configuration, shared ownership, and preservation constraints.
- [references/verification.md](references/verification.md)
  Use to prove the requested lifecycle change across all applicable host layers.
