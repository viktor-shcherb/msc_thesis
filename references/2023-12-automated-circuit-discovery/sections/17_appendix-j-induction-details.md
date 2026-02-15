# Appendix J: Induction task details and qualitative evidence [p. 31]

[p. 31] Setup summary:
- Model: 2-layer attention-only transformer (8 heads/layer) from TransformerLens.
- Data: 40 filtered OpenWebText sequences containing induction-style repeated patterns.
- Metric: KL divergence over selected induction-related prediction positions.

[p. 31] The appendix describes ordering details for parent-edge iteration that affected performance in this setting (head index order sensitivity).

[p. 31] Example recovered circuits include expected induction/previous-token style structures.
