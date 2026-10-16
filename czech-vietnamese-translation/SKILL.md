---
name: czech-vietnamese-translation
description: Translate supplied Czech and Vietnamese practical, technical or operational text in either direction while preserving facts, units, uncertainty and tone. Factual research is a separate task.
version: 1.0.0
category: communication
sources:
  - Reviewed user-confirmed workflows and current source artifacts
use_when:
  - The user explicitly requests Czech-to-Vietnamese or Vietnamese-to-Czech translation, including a follow-up referring to the preceding text.
avoid_when:
  - The user is asking an ordinary factual question in Czech or Vietnamese without requesting translation.
  - The requested task is a legal, technical or medical reassessment rather than translation of supplied material.
artifacts:
  - SKILL.md
  - agents/openai.yaml
quality_gates:
  - Numbers, units, names, conditions, negations and certainty match the source.
  - The target text is natural and adds no unsupported factual or operational instructions.
---

# Czech–Vietnamese translation

Resolve the source from the supplied passage or the clearly referenced preceding message. Use the requested target language; infer the opposite language for an explicit translation request between Czech and Vietnamese when clear. Ask only if the source or target is materially ambiguous. A message merely written in either language does not trigger translation.

Translate into natural, practical language while preserving the source's formality and intended audience. Preserve useful headings, lists and tables. Return the translated text directly unless the user also requests explanation or review.

- Preserve all quantities, decimal meaning, units, prices, dates, identifiers, product names and symbols. Keep ingredient names and component labels consistent. Preserve diacritics; do not turn brand/menu names into invented equivalents.
- Preserve uncertainty and conditions: “probably,” “may,” “must” and “definitely” are not interchangeable. Keep negatives, exceptions and distinctions such as insurance versus registration or verification versus assumption intact.
- For Czech institutional or operational terms, keep the original term/acronym on first mention with a short neutral gloss when needed for understanding. Do not invent a Vietnamese legal equivalent or add a legal conclusion.
- Translate technical instructions faithfully without adding wiring steps, doses, settings, requirements or promised outcomes. Flag an unclear source phrase briefly rather than silently correcting its factual meaning. If verification is also requested, separate researched corrections from the translation.
- For a source image, translate only text actually readable through an available image/document tool. Do not infer missing labels from what a pictured device usually contains.

Before delivery, compare source and target for every number/unit, negation, condition and certainty marker. Uncertainty in the source must remain uncertainty in the translation.
