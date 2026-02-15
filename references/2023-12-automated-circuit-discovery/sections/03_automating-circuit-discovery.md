# 3 Automating circuit discovery (Step 3) [p. 5-6]

[p. 5] The section formalizes ACDC, then compares it against modified SP and HISP baselines.

## ACDC objective and setup

Given:
- Full computational graph `G`
- Candidate subgraph `H ⊆ G`
- Clean inputs `x_i`
- Corrupted inputs `x'_i`

`H(x_i, x'_i)` denotes a forward pass where edges not in `H` are replaced with corrupted activations.

Primary score:

```text
DKL(G || H) = average_i DKL( G(x_i) || H(x_i, x'_i) )
```

## Algorithm 1 (edge pruning)

[p. 6] ACDC iterates graph nodes from output-to-input order. For each parent edge `w -> v`, it tests removing that edge and keeps the removal when performance drop is below threshold `τ`.

```text
If DKL(G||Hnew) - DKL(G||H) < τ, then remove edge permanently.
```

This returns a sparse subgraph balancing task fidelity and edge count.

## SP and HISP adaptations

[p. 6] To make comparisons fair, the authors adapt prior methods:
- **SP (Cao et al., 2021):** remove linear probe objective, optimize the same metric as ACDC, and interpolate with corrupted activations.
- **HISP (Michel et al., 2019):** extend gradient-based head importance to broader components (Q/K/V and MLP outputs) and support corrupted-activation interpolation.

**Figure 2** (p. 5) visualizes ACDC in three stages:
1. Specify graph/task/threshold.
2. Prune weak incoming connections.
3. Recurse until a compact circuit is obtained.
