# Appendix C: Details About RECL [p. 13–14]

## Formal definition of RECL

Let M = {m_1, m_2, ..., m_N} be a model group consisting of N models. Let l_i(c, t) denote the loss of model m_i on the t-th token in the corpus with a context length c. Concretely, the loss can be written as: [p. 13]

$$l_i(c, t) = -\log P_{m_i}(x_t | x_{t-1}, \ldots, x_{t-c})$$

where P_{m_i} is the probability distribution given by model m_i, and x_t is the t-th token in the corpus. [p. 13]

Given a short context length c and a long context length c' such that c' >= c, define a baseline for each position t: [p. 13]

$$b(c, t) = \min_{i=1}^{N} l_i(c, t)$$

The *relative loss* of m_i w.r.t. the model group M is written as: [p. 13]

$$f_i(c, c') = \frac{1}{|\mathcal{T}|} \sum_{t \in \mathcal{T}} \min\bigl(b(c, t),\; l_i(c', t)\bigr)$$

The above equation uses the minimum loss of all models on the short length c as a baseline, and only losses smaller than the baseline will be effectively counted towards the relative loss. This enables fair comparison between multiple models because all models with a long context length c' need to improve over the same baseline. [p. 13–14]

Sometimes only positions where the baseline performs poorly (meaning short-term dependency with context length c is not sufficient) are of interest, so given a ratio parameter r, the set T is defined as: [p. 14]

$$\mathcal{T} = \text{top-}r \text{ positions } t \text{ with largest } b(c, t)$$

The *relative gain* is subsequently defined as the relative perplexity reduction: [p. 14]

$$g_i(c, c') = \frac{\exp f_i(c, c) - \exp f_i(c, c')}{\exp f_i(c, c)}$$

## Algorithm to find RECL

Given a step size Delta, the following algorithm is used to find the RECL by thresholding the relative gain: [p. 14]

1. Set initial short context length c, and long context length c' = c + Delta
2. Compute g_i(c, c'). If g_i(c, c') < 0.01, return RECL = c. If g_i(c, c') >= 0.01, set c = c', c' = c + Delta and go to step 1.

## Figures

**Figure 3** (p. 13): "Visualizing unnormalized relative perplexity gains with r = 0.1."
- (a) Transformer-XL vs RNNs: x-axis is "Context length change" (100 to 1000), y-axis is "Perplexity difference (with baseline)". Shows Transformer-XL, QRNN, and LSTM. Transformer-XL has consistently larger gains that decrease more gradually with increasing context, while QRNN and LSTM gains drop off more quickly.
- (b) Transformer-XL vs Baseline: x-axis same, y-axis same (scale up to ~2500). Compares Transformer-XL, Transformer-XL with Shaw et al. encoding, and Transformer-XL w/o recurrence. The full Transformer-XL has substantially larger gains than the ablated variants.

In Figure 3, the unnormalized relative perplexity gains (exp f_i(c, c) - exp f_i(c, c')) with various pairs of (c, c') when r = 0.1 are visualized. It is clear that Transformer-XL has a longer RECL compared to RNNs and other baselines because the relative gains are substantially larger. [p. 14]

**Figure 4** (p. 13): "Perplexity vs context length."
- (a) Transformer-XL vs RNNs: x-axis is "Context length" (100 to 1000), y-axis is "Perplexity" (approximately 20 to 45). Shows Transformer-XL, QRNN, and LSTM. All three models see decreasing perplexity with longer context, but Transformer-XL is consistently lowest (around 23-25), QRNN is in the middle (~30-33), and LSTM is highest (~35-42).
- (b) Transformer-XL vs Baseline: x-axis same, y-axis "Perplexity" (approximately 26.0 to 30.5). Compares Transformer-XL, Transformer-XL with Shaw et al. encoding, and Transformer-XL w/o recurrence. The full model has the lowest perplexity and continues to improve with longer context, while the other variants plateau earlier.

For reference, the perplexities with varying context lengths are plotted in Figure 4. The y-axis denotes the "normal" perplexity (not calibrated by baselines). [p. 14]
