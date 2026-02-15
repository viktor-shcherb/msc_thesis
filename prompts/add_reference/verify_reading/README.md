# verify_reading — Usage for Main Agent

Verify completeness and accuracy of `sections/*.md` files against the
source PDF after all reading windows have completed.

## Files

- `prompt.md` — instructions for the subagent (the subagent reads this itself)
- `README.md` — this file: usage instructions for the main agent

## Prerequisites

- `references/<slug>/sections/` — populated by `read_paper` (all windows done)
- The source PDF must be accessible at the path used during reading

## Parameters

| Parameter | Required | Description |
|---|---|---|
| `SLUG` | yes | Reference directory name |
| `PDF_PATH` | yes | Absolute path to the paper PDF |

## Invocation

Spawn a subagent (**model: opus**) with this prompt:

```
Read prompts/add_reference/verify_reading/prompt.md and follow those
instructions with these parameters:

SLUG = <slug>
PDF_PATH = <absolute path to pdf>
```
