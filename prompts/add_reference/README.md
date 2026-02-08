# add_reference — Orchestrator Instructions

You orchestrate subagents to add references. Your job is **mechanical**: spawn agents in sequence, use their return summaries to route to the next step. Do NOT verify, check, or validate — the verify_reading subagent does that.

## Pipeline

```
Standard:     init → read_paper (windows) → verify_reading → [re-run if needed] → write_analysis → done
Non-standard: init → read_sources → verify_reading → write_analysis → done
```

## How subagents communicate with you

Each subagent returns a text summary when it completes. Use that summary to
route to the next step. Do NOT read files to check progress or results.

| Stage | Subagent reports back |
|-------|---------------------|
| init_reference | SLUG, PDF path (or "non-standard"), success/failure |
| read_paper | Window done |
| read_sources | Done |
| verify_reading | "Actions Required: None" or "Re-run windows: [X-Y]" or "Re-fetch sources: [...]" |
| write_analysis | Done |

---

## Single Reference Procedure

Execute these steps **mechanically** in order. Wait for each to complete before proceeding.

### Step 1: init_reference

Spawn subagent (model: opus):
```
Read prompts/add_reference/init_reference/prompt.md and follow those instructions.

Paper identifier: <title, arxiv ID, or URL>
```

**Wait.** The subagent reports back with SLUG, PDF path, and success/failure.
- Reports PDF path → Go to Step 2A (standard path)
- Reports non-standard (no PDF) → Go to Step 2B (non-standard path)
- Reports failure → STOP, report to user

### Step 2A: Standard path (has PDF)

#### 2A.1: read_paper windows

See `read_paper/README.md` for full details. Summary:

**Get info:**
```bash
TOTAL_PAGES=$(pdfinfo references/<SLUG>/*.pdf | grep 'Pages:' | awk '{print $2}')
PDF_PATH=$(ls references/<SLUG>/*.pdf)
```

**Calculate windows:** 6-page windows, step 5 (1-page overlap). Clamp last window to TOTAL_PAGES.

```
Window 1:  pages 1–6
Window 2:  pages 6–11
Window 3:  pages 11–16
Window 4:  pages 16–21
...
Last window: clamp PAGE_END to TOTAL_PAGES
```

Example: a 37-page paper → windows [1-6], [6-11], [11-16], [16-21], [21-26], [26-31], [31-37]

**For each window, sequentially:**

Spawn subagent (model: sonnet):
```
Read prompts/add_reference/read_paper/prompt.md and follow those instructions with
these parameters:

SLUG = <slug>
PDF_PATH = <absolute path>
PAGE_START = <number>
PAGE_END = <number>
```

**Wait for window to complete. Then spawn next window.** Windows for the same
paper MUST be sequential (each window reads prior sections for context).
Windows for different papers (in slot mode) can run in parallel.

#### 2A.2: verify_reading

Spawn subagent (model: opus):
```
Read prompts/add_reference/verify_reading/prompt.md and follow those instructions
with these parameters:

SLUG = <slug>
PDF_PATH = <absolute path>
```

**Wait.** The subagent reports back with its "Actions Required" verdict.

- Reports "None" → Go to 2A.3
- Reports "Re-run windows: [X-Y], [Z-W]" → re-run those windows (same as 2A.1 but only the listed ranges), then back to 2A.2

#### 2A.3: write_analysis

Spawn subagent (model: opus):
```
Read prompts/add_reference/write_analysis/prompt.md and follow those instructions
with these parameters:

SLUG = <slug>
MODE = standard
```

**Wait.** Then go to Step 3.

### Step 2B: Non-standard path (no PDF)

#### 2B.1: read_sources

Spawn subagent (model: sonnet):
```
Read prompts/add_reference/read_sources/prompt.md and follow those instructions
with these parameters:

SLUG = <slug>
```

**Wait.**

#### 2B.2: verify_reading

Spawn subagent (model: opus):
```
Read prompts/add_reference/verify_reading/prompt.md and follow those instructions
with these parameters:

SLUG = <slug>
MODE = non-standard
```

**Wait.** The subagent reports back with its "Actions Required" verdict.

- Reports "None" → Go to 2B.3
- Reports "Re-fetch sources: [source1, source2]" → re-run read_sources, then back to 2B.2

#### 2B.3: write_analysis

Spawn subagent (model: opus):
```
Read prompts/add_reference/write_analysis/prompt.md and follow those instructions
with these parameters:

SLUG = <slug>
MODE = non-standard
```

**Wait.** Then go to Step 3.

### Step 3: Done

Report to user: `✅ Reference <SLUG> added successfully`

---

## Slot Mode: N Concurrent Papers

Process a queue of papers using N independent **slots** (N specified by user).
Each slot runs the full single-reference pipeline (Steps 1-3) for one paper
at a time. When a slot finishes a paper, it immediately picks the next paper
from the queue.

### How it works (example with 3 slots)

```
Queue: [A, B, C, D, E, F, G, ...]

Slot 1: A ────────→ D ──────→ G → ...
Slot 2:  B ──────────→ E ────→ ...
Slot 3:   C ─────→ F ──────→ ...
                 ↑
         Slots do NOT wait for each other
```

### Setup

1. Build the queue (ordered list of SLUGs to process).
2. Pop the first N papers from the queue.
3. Assign one paper per slot.
4. Start all slots.

### Per-slot procedure

Each slot runs the Single Reference Procedure (Steps 1-3) independently,
with one modification:

**write_analysis (2A.3 or 2B.3) requires a lock.** Before spawning
write_analysis, check if another slot is currently running write_analysis.
If so, wait for it to finish. Only one write_analysis may run at a time —
cross-reference updates conflict.

### Slot completion

When a slot finishes Step 3 for its current paper:

1. Update the checklist: mark paper as `[x] [x] [x] | ✓`
2. Pop the next paper from the queue
3. If queue is empty → slot is done
4. If queue has a paper → start it immediately

### Queue exhaustion

When all slots are done (queue empty, no in-progress papers), report to user.

---

## Model Assignments

| Stage | Model | Why |
|-------|-------|-----|
| init_reference | opus | Metadata extraction |
| read_paper | sonnet | High-volume windowed reads |
| read_sources | sonnet | Web fetching |
| verify_reading | opus | Catches subtle errors, judgment calls |
| write_analysis | opus | Synthesis, cross-referencing |
