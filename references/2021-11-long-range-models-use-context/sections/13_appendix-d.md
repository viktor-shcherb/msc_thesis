# D Perturbation [p. 13-14]

[p. 13] Perplexity with perturbed distant prefix when evaluated with Local Transformer is shown in Figure 20. Perplexity hardly changes when perturbing up to around 6K tokens. Because LT does not properly use long-range context, only the results of Routing Transformer are presented in the main text. [p. 13]

**Figure 18** (p. 13): "The perplexity of all target tokens plateaus after 2K prefix tokens for both Routing Transformer and Local Transformer. The LT model is the one released in 2021 summer."
- Single panel: "All target tokens"
- X-axis: prefix length (2000-8000); Y-axis: perplexity (~35-38).
- Two lines: RT (blue) and LT (green).
- RT perplexity is lower (~35.2) and flat. LT perplexity is higher (~37) and flat. Both plateau after 2K prefix tokens.

**Figure 19** (p. 13): "Perplexity of all target tokens when evaluated with Local Transformer released in 2021 summer."
- Single panel: "Local Transformer"
- X-axis: perturbation length (0-8000); Y-axis: perplexity (~37-42).
- Three lines: LT-shuffle (green), LT-random (blue), LT-8K (red dashed).
- Inset zooms into perturbation length 0-5000 showing perplexity range ~37-37 (very flat).
- LT-shuffle and LT-random remain flat near ~37 until perturbation length ~5000-6000, then rise. LT-shuffle reaches ~42, LT-random reaches ~40 at perturbation length 8000. LT-8K baseline stays flat at ~37.
- Confirms LT is not sensitive at all to perturbation further than local 2K tokens.

**Figure 20** (p. 15): "Perplexity of all target tokens when evaluated with Local Transformer derived from the RT checkpoint."
- Single panel: "Local Transformer"
- X-axis: perturbation length (0-8000); Y-axis: perplexity (~40-48).
- Three lines: LT-shuffle (green), LT-random (blue), LT-8K (red dashed).
- Inset zooms into perturbation length 0-5000 showing perplexity range ~39.5-40.5.
- LT-shuffle and LT-random remain flat near ~40 until perturbation length ~5000-6000, then rise. LT-shuffle reaches ~48, LT-random reaches ~46 at perturbation length 8000. LT-8K baseline stays flat at ~40.
