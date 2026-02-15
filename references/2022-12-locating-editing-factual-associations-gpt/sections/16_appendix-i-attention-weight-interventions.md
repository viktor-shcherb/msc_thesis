# Appendix I: Are Attention Weight Interventions Effective? [p. 30-31]

[p. 30-31] Appendix tests an attention-focused editor ("AttnEdit") versus ROME.

Setup:

- AttnEdit applies constrained fine-tuning on attention `W_Q`, `W_K`, `W_V` weights at high-causal attention layer (layer 33).
- Constraint chosen by sweep to balance success and bleedover.

Reported pattern:

- Attention editing can increase direct prompt regurgitation.
- It fails more often on paraphrase/generalization prompts.
- ROME remains stronger on generalized factual rewriting.

**Figure 23** (p. 30): unconstrained optimization sweeps for attention editing.

**Figure 24** (p. 31): score distributions for AttnEdit experiment.

**Figure 25** (p. 31): generation comparison where AttnEdit regurgitates in original prompt but fails paraphrase/generalization relative to ROME.
