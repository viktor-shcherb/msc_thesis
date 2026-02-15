# Interventions on Activations for Tracing Information Flow [p. 2-4]

## 2.1 Causal Tracing of Factual Associations

[p. 2] Setup uses fact tuple `t = (s, r, o)` and prompt `p` eliciting object `o`.

[p. 2] Autoregressive LM notation:

`G: X -> Y`, `x = [x_1, ..., x_T]`, hidden states `h_i^(l)`, final prediction from `decode(h_T^(L))`.

[p. 2] Transformer update rule (Equation 1):

`h_i^(l) = h_i^(l-1) + a_i^(l) + m_i^(l)`

`a_i^(l) = attn^(l)(h_1^(l-1), ..., h_i^(l-1))`

`m_i^(l) = W_proj^(l) sigma(W_fc^(l) gamma(a_i^(l) + h_i^(l-1)))`

[p. 3] Three runs are defined:

1. **Clean run**: normal prompt execution.
2. **Corrupted run**: add Gaussian noise to subject-token embeddings.
3. **Corrupted-with-restoration run**: restore one hidden state from clean run while keeping other corruption.

[p. 3] Effects measured with object-token probability `P[o]`:

- Total effect: `TE = P[o] - P*[o]`.
- Indirect effect for mediator `h_i^(l)`: `IE = P* , clean h_i^(l)[o] - P*[o]`.
- Averages over prompts give ATE/AIE.

## 2.2 Causal Tracing Results

[p. 4] Over 1000 factual statements (GPT-2 XL), ATE is reported as **18.6%**.

[p. 4] Key localization result:

- Strong "early site" at last subject token in middle layers (peak AIE for individual states around layer 15: **8.7%**).
- MLP contribution at early site dominates attention contribution there.
- Late site near output token shows strong attention contribution.

[p. 4] Reported magnitudes:

- MLP at early site: AIE peak **6.6%**.
- Attention at last subject token: AIE **1.6%**.

[p. 4] Path-specific intervention (severing MLP influence) shows early-layer causal effects collapse without downstream MLP activity; analogous severing for attention does not show the same transition.

## 2.3 The Localized Factual Association Hypothesis

[p. 4] Hypothesis: factual association recall is localized in middle-layer MLP computations at subject-token processing; late attention copies/propagates the retrieved information to prediction position.

[p. 4] Localization dimensions:

- module type (MLP),
- layer band (middle layers),
- token position (subject-final token, with notable exceptions).

[p. 4] Authors conjecture some layer-order interchangeability in middle layers and suggest factual associations could be stored equivalently across one of those layers.

**Figure 2** (p. 3): AIE heatmaps by token position and layer.
- Shows early-site and late-site structure.
- MLP heatmap peaks at early site; attention heatmap peaks near output token.

**Figure 3** (p. 4): Causal effects under modified graph with MLP severing.
- Demonstrates dependence of early-site causal effects on MLP pathway.
