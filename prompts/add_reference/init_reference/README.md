# init_reference — Usage for Main Agent

Initialize a new reference directory with metadata files.

## Files

- `prompt.md` — instructions for the subagent (the subagent reads this itself)
- `README.md` — this file: usage instructions for the main agent

## Parameters

| Parameter | Required | Description |
|---|---|---|
| `INPUT` | yes | Paper title, URL, arXiv ID, or description of the contribution |

## Invocation

Spawn a `general-purpose` subagent (**model: sonnet**) with this prompt:

```
Read prompts/add_reference/init_reference/prompt.md and follow those
instructions with this input:

INPUT = <paper title, URL, arXiv ID, or description>
```

## Output

Three lines:

```
SLUG = <slug>
PDF_PATH = <absolute path to PDF, or null>
STANDARD = <true or false>
```
