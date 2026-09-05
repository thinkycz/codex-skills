# Deepening Rubric

Classify dependencies before proposing seams.

## Dependency Categories

- In-process dependency:
  Direct local code used in the same process. Prefer ordinary module boundaries and behavior tests.
- Local-substitutable dependency:
  A local implementation can be swapped for another local implementation. A seam may help if there are real alternatives or test pain.
- Remote-owned port or adapter:
  A remote service, protocol, queue, payment provider, browser API, or system boundary owns behavior outside the repo. Local code should translate it into domain language.
- True external mock:
  A dependency cannot be run or controlled locally. Tests may need fakes, contract tests, or captured examples, but the fake should sit behind the local adapter interface.

## Deepening Signals

- Callers repeat the same ordering, normalization, validation, retry, or mapping steps.
- Tests mock long chains of collaborators instead of checking one useful behavior surface.
- Domain terms appear in many unrelated modules with small variations.
- External payload shapes leak through UI, business logic, or test code.
- Changing one rule requires coordinated edits in several places.

## Cautions

- Do not create a seam only because one might be useful later.
- Do not keep old shallow tests and add deep tests on top; replace tests when a better interface makes the old surface obsolete.
- Do not hide important domain choices behind vague helper names.
- Do not mistake dependency inversion for architectural depth; the interface still needs to simplify caller knowledge.
