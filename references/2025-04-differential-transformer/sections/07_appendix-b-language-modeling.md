# Appendix B: Language Modeling Evaluation [p. 16]

Following the same setting as in Section 3.1, they train 3B-size language models on 350B tokens and compare DIFF Transformer with Transformer (Vaswani et al., 2017) in various downstream tasks [p. 16]. They use the augmented Transformer architecture as in LLaMA (Touvron et al., 2023) [p. 16]. Specifically, the "Transformer" models include improvements in RMSNorm (Zhang & Sennrich, 2019), SwiGLU (Shazeer, 2020; Ramachandran et al., 2017), and removal of bias [p. 16].

Table 8 reports the zero-shot and 5-shot results on the LM Eval Harness benchmark (Gao et al., 2023) [p. 16]. The results show that DIFF Transformer outperforms Transformer across various tasks in both zero-shot and few-shot settings [p. 16].

| Model | ARC-C | ARC-E | BoolQ | HellaSwag | OBQA | PIQA | WinoGrande | Avg |
|---|---|---|---|---|---|---|---|---|
| *Training with 350B tokens (Zero-Shot)* | | | | | | | | |
| Transformer-3B | 32.2 | 66.8 | 62.9 | 63.4 | 26.2 | 74.5 | 61.6 | 55.4 |
| DIFF-3B | **33.0** | **68.3** | **60.1** | **66.2** | **27.6** | **75.5** | **62.7** | **56.2** |
| *Training with 350B tokens (5-Shot)* | | | | | | | | |
| Transformer-3B | 34.0 | 69.5 | 65.3 | 63.4 | 25.0 | 75.2 | 62.6 | 56.4 |
| DIFF-3B | **35.0** | **69.5** | **67.2** | **66.9** | **27.6** | **76.1** | **63.8** | **58.0** |

Table 8: Comparison of DIFF Transformer with well-trained Transformer language models on LM Eval Harness (Gao et al., 2023) [p. 16]. DIFF Transformer achieves better accuracy in the zero- and few-shot settings [p. 16].
