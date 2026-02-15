# Appendix F: IOI task details and qualitative evidence [p. 23-26]

[p. 23-24] Setup:
- Model: GPT-2 Small.
- Dataset size: 50 IOI prompts from a single template.
- Corrupted set: ABC-style prompts from prior IOI work.

[p. 24-25] The appendix compares ACDC-recovered heads with the prior canonical IOI circuit.

Reported behavior:
- At moderate thresholds, ACDC recovers a compact subset of documented IOI heads.
- Lower thresholds recover additional known classes (including negative heads) but also many extra heads.

[p. 25] Authors highlight that negative components are hard to recover robustly under single-metric optimization.
