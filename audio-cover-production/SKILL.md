---
name: audio-cover-production
description: Separate audio stems or create a melody-preserving cover with a new backing or synthesized singer, using source audio and reference recordings. Choose separation versus cover production from the requested deliverable.
version: 1.0.0
category: creative-production
sources:
  - Reviewed user-confirmed workflows and current source artifacts
use_when:
  - The user requests vocal/instrumental stems or a finished audio cover from supplied recordings.
avoid_when:
  - The request is only a factual question about an artist or a verbatim lyric lookup.
  - The task requires only ordinary text translation or unrelated video editing.
artifacts:
  - SKILL.md
  - agents/openai.yaml
  - references/
quality_gates:
  - The original recording remains unchanged and the requested vocal treatment is explicit.
  - Preview and full exports preserve requested melody, lyrics and timing with technical evidence.
  - Listening acceptance is distinguished from numerical diagnostics.
---

# Audio cover production

Choose the deliverable before choosing a tool. “Separate vocals” produces stems; “make the cover” requires a finished musical performance. Reuse the latest clarified intent instead of continuing a superseded approach.

## Modes

- **separate** — Extract aligned vocal and instrumental files without changing the source. Read [stem separation](references/separate.md).
- **cover** — Produce the requested cover with explicit decisions about original versus synthesized vocals and original versus new backing. Read [cover production](references/cover.md).

Inspect available tools, source files, architecture, storage and existing model caches before installing or downloading anything. Reuse a working local setup where suitable. Honor the user's tool choice when it can deliver the requested result; explain a needed alternative if an editor cannot generate the requested performance. Verify actual provider capabilities before relying on upload or subscription features, and honor provider restrictions.

Keep source recordings intact, work on copies and use explicit output filenames. An authorized cover task does not authorize unrelated purchases, publication, or assuming rights to a third party's voice or recording. Use only recordings and voice references within the user's authorized scope.
