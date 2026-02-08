# read_sources — Usage for Main Agent

Read non-standard source content (web pages, repos, threads) into
`references/<SLUG>/sources/` for references that have no PDF.

## Files

- `prompt.md` — instructions for the subagent (the subagent reads this itself)
- `README.md` — this file: usage instructions for the main agent

## Prerequisites

`init_reference` must have already created:
- `references/<slug>/source.md` — bibliographic metadata
- `references/<slug>/sources/manifest.md` — list of sources to fetch

## Parameters

| Parameter | Required | Description |
|---|---|---|
| `SLUG` | yes | Reference directory name |

## Invocation

Spawn a single `general-purpose` subagent with this prompt:

```
Read prompts/add_reference/read_sources/prompt.md and follow those
instructions with this parameter:

SLUG = <slug>
```
