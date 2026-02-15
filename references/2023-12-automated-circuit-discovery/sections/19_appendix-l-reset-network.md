# Appendix L: Reset network experiments [p. 32-33]

[p. 32-33] The paper tests whether methods can spuriously recover "circuits" on models with permuted/reset parameters.

Procedure summary:
- Permute selected parameters to disrupt learned behavior while preserving broad activation statistics.
- Run circuit-discovery methods and compare performance trends.

Interpretation:
- If a method still finds strong task circuits on reset models, this is evidence of false-positive tendency.
- Reported trends suggest meaningful but imperfect separation between trained vs reset cases across methods.
