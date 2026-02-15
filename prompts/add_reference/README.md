# add_reference — Orchestrator Instructions

YOU are the orchestrator. You directly spawn one subagent per pipeline step and use its return summary to decide the next step. You never delegate multiple steps to a single subagent. Your job is **mechanical**: spawn, wait, route. Do NOT verify, check, or validate — the verify_reading subagent does that.

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

Process a queue of papers using N concurrent **slots** (N specified by user).

**CRITICAL: A "slot" is NOT a subagent.** A slot is a label you use to track
which paper is at which pipeline stage. YOU (the orchestrator) directly spawn
every subagent for every slot. You never delegate an entire pipeline to a
single subagent.

### What you do

You maintain a simple state table:

```
Slot 1: paper A → currently at step 2A.1 (window 3 of 7) → task_id: abc123
Slot 2: paper B → currently at step 1 (init running) → task_id: def456
```

You spawn subagents yourself — one Task call per step. You use **background
tasks** so you never block waiting for one slot while another could make
progress.

### Anti-pattern (DO NOT DO THIS)

```
❌ WRONG: Spawn a subagent and tell it "run Steps 1-3 for paper A"
❌ WRONG: Spawn a "slot manager" agent
❌ WRONG: Delegate the pipeline to any single subagent
❌ WRONG: Spawn 2 blocking tasks and wait for both before continuing
```

### Correct pattern: background tasks + polling

**Step 1 — Spawn with `run_in_background: true`:**

All cross-slot subagents MUST use `run_in_background: true`. This returns
immediately with a `task_id` so you can continue working on other slots.

```
✅ Spawn "init for paper A" (Task, model: opus, run_in_background: true) → task_id_1
✅ Spawn "init for paper B" (Task, model: opus, run_in_background: true) → task_id_2
```

**Step 2 — Poll with `TaskOutput(block: false)`:**

Check each task's status without blocking:

```
✅ TaskOutput(task_id_1, block: false) → completed? Read summary, spawn next step for slot 1
✅ TaskOutput(task_id_2, block: false) → still running? Skip, check again later
```

**Step 3 — React immediately:**

As soon as ANY slot's task completes, spawn the next step for that slot
right away. Do NOT wait for other slots.

```
✅ Slot 1 init done → immediately spawn "read window 1-6 for A" in background
✅ Slot 2 init still running → leave it, check again next loop
```

### Setup

1. Build the queue (ordered list of papers to process).
2. Pop the first N papers from the queue.
3. Assign one paper per slot.
4. Spawn Step 1 (init) for all N slots with `run_in_background: true`.

### Running the slots

After setup, loop until all slots are done:

1. **Poll each active slot's task** using `TaskOutput(task_id, block: false)`.
   If no slot has completed, use `TaskOutput(task_id, block: true, timeout: 30000)`
   on any one task to wait briefly.
2. **For each completed task:** read its summary, determine the next step
   for that slot using the Single Reference Procedure (Steps 1→2A/2B→3).
3. **Spawn the next step** for that slot with `run_in_background: true`.
   Update your state table with the new task_id.
4. **When a slot finishes Step 3:** update the checklist, pop the next
   paper from the queue, spawn Step 1 for the new paper in background.
   If queue is empty, the slot is done.

**Exception:** Within a single slot, read_paper windows are sequential.
After window N completes, spawn window N+1 immediately (still in
background so other slots aren't blocked).

**Constraint:** Only one write_analysis (2A.3 or 2B.3) may run at a time
across all slots. If another slot is running write_analysis, wait for it
before spawning yours.

### Parallelism rules

- **init** for different papers → CAN run in parallel
- **read_paper windows** for the SAME paper → MUST be sequential
- **read_paper windows** for DIFFERENT papers → CAN run in parallel
- **verify_reading** for different papers → CAN run in parallel
- **write_analysis** → only ONE at a time across all slots

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
