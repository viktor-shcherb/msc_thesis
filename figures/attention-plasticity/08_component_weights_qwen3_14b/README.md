# Positional Information by Embedding Dimension: Qwen3-14B

## File
`figure.png`

## What This Figure Shows

A bar chart showing the share of positional information carried by each embedding dimension (component index 0–127) in Qwen3-14B. Positional information is measured as the contribution of each dimension to the position-dependent component of Q/K vectors.

Two clusters of position-encoding dimensions are visible: indices ~38–55 and ~100–115, separated by dead zones (indices 0–33 and 73–100) carrying zero positional information. This bimodal structure directly reflects RoPE's architecture: position information is applied as 2D rotations to specific dimension pairs, leaving other dimensions as pure content channels.

## How It Was Produced

1. **Data source**: Post-RoPE Q/K vectors from `viktoroo/sniffed-qk` on LongBench-Pro 128K+ samples.
2. **Computation**: Decomposition of Q/K variance into positional and content components per embedding dimension.
3. **Tool**: `attention-plasticity` CLI, `component_weights.png` output.

## Key Takeaway

The dead-zone dimensions (0–33, 73–100) are pure content dimensions — they carry zero positional information and contribute only semantic signal to attention scores. This connects to the rotation analysis: the complement of the {a, b} plane contains both RoPE rotation planes (in the active clusters) and these content-only dimensions (in the dead zones). The relative width of the active clusters varies by family: Ministral3 has sharper, narrower peaks (more concentrated positional encoding) while Qwen3 has broader peaks (more distributed). This may relate to the plasticity differences — broader positional encoding could mean position information leaks into more dimensions, reducing the effective content-only subspace.
