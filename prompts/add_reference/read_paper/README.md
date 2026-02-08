# read_paper — Paper Reading Prompt

Read a paper PDF in 6-page overlapping windows and extract structured
section-by-section notes into `references/<SLUG>/sections/*.md`.

## Files

- `prompt.md` — instructions for the subagent (the subagent reads this itself)
- `README.md` — this file: usage instructions for the main agent

## How it works

The main agent spawns one subagent **per window**. Each subagent:
1. Reads `prompts/add_reference/read_paper/prompt.md` for its instructions
2. Reads existing `sections/*.md` files for context
3. Reads the assigned PDF pages
4. Creates or updates section files

The subagent is stateless — all accumulated knowledge lives on disk in the
section files. The main agent just passes parameters.

## Usage (main agent)

### 1. Get the page count and PDF path

```bash
pdfinfo references/<SLUG>/*.pdf | grep Pages
ls references/<SLUG>/*.pdf
```

### 2. Create the sections directory

```bash
mkdir -p references/<SLUG>/sections
```

### 3. Spawn subagents, one per window

Window sequence: 6-page windows, step 5, overlap 1.

```
Window 1:  pages 1–6
Window 2:  pages 6–11
Window 3:  pages 11–16
Window 4:  pages 16–21
...
Last window: clamp PAGE_END to TOTAL_PAGES
```

For each window, spawn a `general-purpose` subagent (**model: sonnet**) with this prompt:

```
Read prompts/add_reference/read_paper/prompt.md and follow those instructions with
these parameters:

SLUG = <slug>
PDF_PATH = <absolute path to pdf>
PAGE_START = <first page>
PAGE_END = <last page>
```

**Wait for each window to complete before spawning the next** for the same
paper. Windows for *different* papers can run in parallel.

## Window count estimates

| Paper length | Windows |
|---|---|
| 10 pages | 2 |
| 20 pages | 4 |
| 30 pages | 6 |
| 60 pages | 12 |
| 90 pages | 18 |
