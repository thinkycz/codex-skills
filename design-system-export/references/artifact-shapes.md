# Artifact Shapes

Choose the lightest artifact that downstream work can actually reuse.

## Common Outputs

- token summary markdown
- component rule matrix
- motion and state rules
- design-system guidance doc
- generation-oriented design brief such as a portable `DESIGN.md`-style artifact

## Selection Guidance

- use markdown guidance when the audience is maintainers or implementers
- use generation-oriented exports when another tool or agent will consume the rules directly
- include unresolved inconsistencies instead of hiding them
