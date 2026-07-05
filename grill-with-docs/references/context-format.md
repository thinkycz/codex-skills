# Context Format

Use `CONTEXT.md` to capture domain language only. It is a glossary, not a spec, task plan, implementation note, or decision log.

## Single Context

Most repos use one root `CONTEXT.md`:

```md
# {Context Name}

{One or two sentences describing what this domain context is and why it exists.}

## Language

**Order**:
One or two sentences defining what the term is.
_Avoid_: Purchase, transaction

**Invoice**:
A request for payment sent to a customer after delivery.
_Avoid_: Bill, payment request
```

## Multiple Contexts

If `CONTEXT-MAP.md` exists, use it to find the right context-local glossary.

```md
# Context Map

## Contexts

- [Ordering](./src/ordering/CONTEXT.md) - receives and tracks customer orders
- [Billing](./src/billing/CONTEXT.md) - generates invoices and processes payments

## Relationships

- **Ordering -> Billing**: Ordering emits order events; Billing consumes them to create invoices.
```

## Rules

- Pick one canonical term when multiple words compete.
- List aliases to avoid when they would cause drift.
- Keep definitions tight: one or two sentences.
- Define what the concept is, not how it is implemented.
- Include only project-domain concepts, not generic programming concepts.
- Flag ambiguity explicitly when a word is used for multiple concepts.
- Group terms under subheadings only when natural clusters emerge.
- Include a short example dialogue only when it clarifies relationships that prose definitions do not.
