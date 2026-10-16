---
name: env-file-mutation-guard
description: Protect .env files and environment templates from unrequested edits; use whenever work could modify, redact, clean, regenerate, or normalize .env* content.
version: 1.0.1
category: safety
sources:
  - explicit user preference from a production debugging incident
use_when:
  - A task may add, edit, delete, redact, clean, regenerate, or normalize a .env* file or environment template.
  - Credentials or suspected secrets are discovered in .env, .env.example, or another environment file during unrelated work.
avoid_when:
  - The task only reads environment configuration and cannot mutate any environment file.
artifacts:
  - SKILL.md
  - agents/openai.yaml
  - agents/
quality_gates:
  - No .env* file content changes without an explicit user instruction authorizing that exact mutation scope.
  - Security findings are reported without echoing secret values or silently redacting files.
  - Broader implementation approval is never treated as permission to clean environment files.
---

# Env File Mutation Guard

Protect environment files as an explicit user-controlled boundary.

## Non-Negotiable Rule

Never create, edit, delete, redact, sanitize, regenerate, reformat, or otherwise change any `.env*` file or environment-template file unless the user directly and explicitly requests that environment-file mutation.

The authorization must come from the user's own instruction and identify the intended environment-file change. Do not infer it from:

- approval of a broader implementation or security task
- an assistant-proposed plan that happens to include environment cleanup
- requests such as "fix it," "implement the plan," "clean the repo," or "remove secrets"
- repository conventions, security best practices, test failures, or release verification work

When explicit authorization is absent, leave every environment file byte-for-byte unchanged.

## Covered Files

Apply this guard to `.env`, `.env.example`, `.env.test`, `.env.production`, local variants, encrypted variants, and any file whose primary purpose is serving as an environment-variable template.

Reading these files for an in-scope task is allowed. Never echo or reproduce credential values in tool output, patches, documentation, or responses.

## When Sensitive Values Are Found

- Do not redact, blank, rotate, move, or rewrite them.
- Report the affected file and variable names without revealing their values.
- Recommend rotation or secret-store migration when warranted.
- Ask for a direct instruction before changing the environment file itself.
- Continue the rest of the authorized task when the environment-file change is not required.

## When The User Explicitly Authorizes A Change

- Limit the mutation to the named files, variables, and purpose.
- Preserve all unrelated environment values and existing user edits.
- Avoid commands, formatters, generators, or bulk rewrites that touch additional environment files.
- Verify the final diff contains only the authorized environment-file changes.

## Completion Check

Before finishing any task that touched configuration or credentials, inspect the changed-file list. If an environment file changed without direct authorization, restore only the agent-created environment-file change while preserving user-owned work, then report the correction.
