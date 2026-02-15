# Appendix B: Causal Tracing [p. 14-23]

## B.1 Experimental Settings

[p. 14-15] Setup details:

- 1000 factual prompts known by GPT-2 XL.
- Corruption: Gaussian embedding noise with variance scaled to 3x token-embedding std.
- Ten corruption draws per prompt.
- Clean object probability averages: 27.0%.
- Corrupted object probability averages: 8.47%.

## B.2 Separating MLP and Attention Effects

[p. 15] Single activation restoration for individual MLP/attention vectors had weak effect; authors restore runs of 10 module outputs around a center layer for module-specific causal maps.

[p. 15] Reported max average restored scores:

- MLP runs: 23.6% max (location-wise peak around layer 17 at last subject token, ~15.0% bucketed score).
- Attention runs: 19.4% max (location-wise peak around layer 32 at last prompt token, ~16.5% bucketed score).

**Figure 7** (p. 15): line-plot version with 95% confidence intervals corresponding to main-paper heatmaps.

## B.3 Cross-Model Traces

[p. 16-17] Causal traces on GPT-NeoX (20B), GPT-J (6B), GPT-2 Medium, GPT-2 Large show similar early-site MLP / late-site attention pattern across scales and architecture variants.

**Figure 8** (p. 16): GPT-NeoX and GPT-J trace maps.

**Figure 9** (p. 17): cross-scale comparison including GPT-2 medium/large and NeoX-20B.

## B.4 Additional Cases and Robustness

[p. 17-23] Additional analyses:

- per-example trace visualizations,
- exceptions where decisive token is not subject-final,
- robustness under expanded corruption scheme (corrupting additional token),
- robustness to alternative noise distributions,
- comparison against Integrated Gradients (IG).

Figures:

- **Figure 10** (p. 18): diverse factual-trace examples.
- **Figure 11** (p. 19): cases where non-final subject token is decisive.
- **Figure 12** (p. 20): extra-token corruption traces.
- **Figure 13** (p. 21): noise-distribution comparisons.
- **Figure 14** (p. 22): detailed per-example path effects.
- **Figure 15** (p. 22): line plots under extra-token corruption.
- **Figure 16** (p. 23): IG saliency maps do not show the same clear global mechanism as causal tracing.
