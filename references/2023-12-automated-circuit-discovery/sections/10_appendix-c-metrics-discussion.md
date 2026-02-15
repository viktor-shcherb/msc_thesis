# Appendix C: Discussion of metrics optimized [p. 17-18]

[p. 17] The appendix formalizes alternatives to the KL-based pruning rule and explains why KL divergence was chosen as the default across tasks.

Generalized edge-removal condition:

```text
F(H) - F(Hnew) < τ
```

where `F` is any metric to minimize over subgraphs.

[p. 17-18] Two alternatives considered:
1. Match full-model metric value (`|F(H)-F(G)|` objective).
2. Keep only edges causing small local metric change (`|F(Hnew)-F(H)|`).

Reported issue: these alternatives were unstable or underperformed in key settings.

[p. 18] The appendix notes practical problems with logit-difference objectives (including over-optimization and sign issues), and reports stronger overall robustness from KL objectives in their experiments.
