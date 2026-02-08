# Conclusion [p. 10]

[p. 10] The robustness of different positional encodings, in decoder-only Transformers, at length generalization on various downstream mathematical and reasoning tasks was studied. The extensive empirical study shows the effectiveness of NoPE, and further demonstrates that widely used explicit PEs are not suited for length generalization. NoPE can implicitly learn both absolute and relative positions, but uses the latter in practice. The effectiveness of scratchpad is task-dependent, and is not a reliable solution for length generalization.

## Limitations

[p. 10] This work primarily focuses on positional encodings as a design choice in the Transformers decoder architecture. The authors could not study how large-scale pretraining affects different PEs because there are no publicly available large language models trained with various PEs under similar conditions. This is left for future work due to limited compute budget.
