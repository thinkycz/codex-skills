# Source Normalization

Use the design source to infer product intent carefully.

## Extract From The Source

- top-level screens or states
- primary user actions
- transitions between states
- visible form fields and controls
- confirmation, error, empty, and success states
- gating conditions suggested by the UI

## Separate Three Kinds Of Statements

- `Specified`: clearly present in the design or written source
- `Inferred`: strongly suggested by the design, but not fully explicit
- `Unknown`: important behavior that the source does not define safely

## Conflict Rule

If the visual source and written source disagree in a way that changes behavior or acceptance criteria, ask which source has priority before finalizing the PRD.

## Writing Rule

Do not overfit the PRD to pixel-level styling details unless they express real product behavior.
