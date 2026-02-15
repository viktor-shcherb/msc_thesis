# write_analysis — Usage for Main Agent

Create `analysis.md` from completed `sections/` (papers) or `sources/`
(non-standard references), then update reciprocal cross-references, claim
interactions, and open question resolutions in existing papers.

## Files

- `prompt.md` — instructions for the subagent (the subagent reads this itself)
- `README.md` — this file: usage instructions for the main agent

## Prerequisites

One of these must exist:
- `references/<slug>/sections/` — populated by `read_paper`
- `references/<slug>/sources/` — populated by `read_sources`

Also required:
- `references/<slug>/source.md` — bibliographic metadata
- `references/metadata.yaml` — ontology for controlled vocabularies

## Parameters

| Parameter | Required | Description |
|---|---|---|
| `SLUG` | yes | Reference directory name |

## Invocation

Spawn a subagent (**model: opus**) with this prompt:

```
Read prompts/add_reference/write_analysis/prompt.md and follow those
instructions with this parameter:

SLUG = <slug>
```
