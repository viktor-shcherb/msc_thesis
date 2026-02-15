# Appendix F. Comparing PRM and ORM [p. 24–25]

[p. 24–25] The authors trained a PRM and ORM model using the PaLM 2-S* base LM. They see in Figure 14, that the PRM outperforms the ORM, and the gap between the gap between the PRM and ORM grows with the number of samples used. They use the last step prediction from the PRM to score the answers as described in Appendix E.

**Figure 14** (p. 25): "We compare PRM and ORM models finetuned from PaLM 2-S* in a best-of-N evaluation. We use the PaLM 2-S* base LM to sample outputs, using a few-shot prompt. We see that the PRM greatly outperforms the ORM at a larg number of samples."

Description: Line plot comparing PRM and ORM models
- X-axis: Number of Samples (log scale from 2^0 to 2^11)
- Y-axis: MATH Test Accuracy (%) ranging from ~10% to ~40%
- Three lines plotted: PRM best-of-N weighted (blue), Base LM Majority (orange), ORM best-of-N weighted (green)
- Notable patterns: PRM (blue) achieves highest performance, reaching ~40% at 2^11 samples; ORM (green) reaches ~35% at 2^11 samples; Base LM Majority (orange) reaches ~30% at 2^11 samples; gap between PRM and ORM increases from ~0% at 2^0 to ~5% at 2^11; all methods show smooth logarithmic scaling.
- Supports claim: PRM outperforms ORM in best-of-N evaluation, with the performance gap growing as the number of samples increases.
