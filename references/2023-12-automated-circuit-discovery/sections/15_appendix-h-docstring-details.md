# Appendix H: Docstring task details and qualitative evidence [p. 27-29]

[p. 27-29] The appendix compares ACDC with the manual circuit from Heimersheim and Janiak (2023).

Key observations:
- ACDC recovers most key manual heads and additionally surfaces one useful head not emphasized in the original manual reconstruction.
- Exact recovered graph depends strongly on threshold and metric objective.

**Table 4** reports comparative metrics (KL divergence, mean logit difference, edge count) across:
- Full model,
- Multiple ACDC runs (KL and logit-difference objectives),
- Manual circuit variants.

[p. 29] Limitation explicitly noted: experiments here used head/QKV granularity without splitting nodes by token position, whereas prior manual analysis used more position-specific structure.
