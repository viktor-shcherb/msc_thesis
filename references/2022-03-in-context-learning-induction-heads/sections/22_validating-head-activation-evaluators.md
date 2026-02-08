# Validating Head Activation Evaluators [p. 56]

[p. 56] The authors show that their head activation evaluators (used to measure the properties in their definition of induction heads) correlate well with mathematically-based measures in small attention-only models. [p. 56]

## Copying [p. 56]

The copying evaluator correlates well with the OV matrix of each head. Specifically, the authors plot against the sum of the eigenvalues, divided by the absolute value of the eigenvalues, which is a measure of what fraction of the eigenvalues are positive vs. negative. [p. 56]

**Figure (Copying validation — Small attn models)** (p. 57): Scatter plot titled "Small attn models". X-axis: "OV eigs sum/abs" (range -1.00 to 1.00). Y-axis: "Copying head evaluator" (range -1.00 to 1.00). Points are colored by model and layer (1l-attn layer 0 through 6l-attn layer 5). The plot shows a strong positive correlation: heads with a high OV eigenvalue sum/abs ratio also have a high copying evaluator score. Heads in the upper-right cluster (OV eigs sum/abs near 1.0, copying evaluator near 0.75-1.0) correspond to strong copying heads. Heads with negative OV eigs sum/abs values tend to have negative copying evaluator scores. The correlation validates the heuristic copying evaluator against the mathematical OV eigenvalue measure. [p. 57]

## Prefix matching [p. 57]

The prefix matching evaluator correlates well with the trace of QK eigenvalues for the previous-token QK-circuit term. [p. 57]

**Figure (Prefix matching validation — Small attn models)** (p. 57): Scatter plot titled "Small attn models". X-axis: "QK eigs trace" (range approximately -500 to 1250). Y-axis: "Prefix matching head evaluator" (range 0.0 to 1.0). Points are colored by model and layer (2l-attn layer 1 through 6l-attn layer 5). The plot shows a positive correlation: heads with higher QK eigenvalue traces tend to have higher prefix matching evaluator scores. Heads with QK eigs trace above ~500 generally have prefix matching evaluator scores above 0.4, with the highest-scoring heads (prefix matching > 0.8) having QK eigs traces above ~750. Heads with negative QK eigs traces cluster near zero on the prefix matching evaluator. The correlation validates the heuristic prefix matching evaluator against the mathematical QK eigenvalue trace measure. [p. 57]
