# Appendix B: Experiment Contunued [p. 21-22]

## B.1 Evaluation [p. 21]

### Commonsense reasoning [p. 21]

Following Gu & Dao (2023), we evaluate our model on multiple commonsense reasoning benchmarks: PIQA (Bisk et al., 2020), HellaSwag (Hella.: Zellers et al., 2019), WinoGrande (Wino.: Sakaguchi et al., 2020), ARC-easy (ARC-e) and ARC-challenge (ARC-c) (Clark et al., 2018), SIQA (Sap et al., 2019), BoolQ (Clark et al., 2019), Wikitext (Wiki.: Merity et al., 2017), and LAMBADA (LMB.: Paperno et al., 2016) [p. 21].

### In-context retrieval [p. 21]

Our evaluation comprises both synthetic and real-world tasks [p. 21]. For synthetic tasks, we utilize the Needle-In-A-Haystack (NIAH-S) benchmark suite from RULER (Hsieh et al., 2024), which includes three increasingly complex tasks: S-NIAH-1 (passkey retrieval), S-NIAH-2 (numerical needle in haystack), and S-NIAH-3 (word-level retrieval and haystack) [p. 21]. For real-world tasks, following Arora et al. (2024b), we evaluate on diverse datasets: SWDE (Lockard et al., 2019) for structured HTML relation extraction, FDA (Arora et al., 2023b) for PDF key-value retrieval, and several question-answering benchmarks including SQuAD (Rajpurkar et al., 2018), TriviaQA (Joshi et al., 2017a), Drop (Dua et al., 2019), and NQ (Kwiatkowski et al., 2019) [p. 21]. Since our pretrained models lack instruction tuning, we employed the task formatting prompts provided by Arora et al. (2024b), which better align with our models' next-word-prediction training objective [p. 21].

### Long context understanding [p. 21]

We evaluate on 14 tasks from Longbench (Bai et al., 2023), encompassing: narrative comprehension (Narrative QA (Kočiský et al., 2018)), scientific understanding (QasperQA (Dasigi et al., 2021)), multi-document QA (MultiField QA, HotpotQA (Yang et al., 2018), 2WikiMulti QA (Ho et al., 2020), Musique (Trivedi et al., 2022)), document summarization (GovReport (Huang et al., 2021), QMSum (Zhong et al., 2021), MultiNews (Fabbri et al., 2019)), and various specialized tasks (TRec (Li & Roth, 2002), Trivia QA (Joshi et al., 2017b), SamSum (Gliwa et al., 2019), LCC (Guo et al., 2023), and RepoBench-P (Liu et al., 2023)) [p. 21].

## B.2 Ablation Study [p. 22]

**Table S.1:** Ablation study on the Gated DeltaNet block. Avg-PPL and Avg-Acc denote average perplexity and zero-shot commonsense reasoning accuracy (as in Table 3), respectively. All models have 400M parameters and are trained for 15B tokens on the same subset of FineWeb-Edu dataset (Penedo et al., 2024) [p. 22].

| Gated DeltaNet Ablations (400M) | Avg-PPL (↓) | Avg-Acc (↑) |
|----------------------------------|-------------|-------------|
| Gated DeltaNet w. Head Dim 128   | 27.35       | 47.26       |
| **Macro Design**                 |             |             |
| w. naive Delta Rule              | 30.87       | 45.12       |
| w/o. Short Conv                  | 28.95       | 46.16       |
| w/o. Output Gate                 | 29.12       | 45.46       |
| w/o. Output Norm                 | 27.55       | 47.07       |
| **Normalization & Feature Map**  |             |             |
| w. L₁-norm & ReLU                | 30.79       | 45.92       |
| w. L₁-norm & 1+ELU               | 30.34       | 46.05       |
| w. L₁-norm & SiLU                | 30.18       | 46.09       |
| w. L₂-norm & ReLU                | 27.67       | 46.94       |
| w. L₂-norm & 1+ELU               | 27.58       | 47.17       |
| **Model Dimensions**             |             |             |
| w. Head Dim 64                   | 28.31       | 46.35       |
| w. Head Dim 256                  | 27.13       | 47.38       |

**Table S.2:** Ablation studies of Gated DeltaNet models. All evaluations are performed by using lm-evaluation-harness (Gao et al., 2021). All models use the Llama tokenizer and are trained on the same subset of the FineWeb-Edu dataset (Penedo et al., 2024) [p. 22].

| Model | Wiki. ppl ↓ | LMB. ppl ↓ | LMB. acc ↑ | PIQA acc ↑ | HellaS. acc ↑ | Wino. acc ↑ | ARC-e acc ↑ | ARC-c acc ↑ | SIQA acc ↑ | BoolQ acc ↑ | Avg ↑ |
|-------|-------------|------------|-----------|-------------|---------------|-------------|-------------|-------------|------------|-------------|-------|
| **Hybrid Ablations (500M/15B)** | | | | | | | | | | | |
| Gated DeltaNet + SWA + Mamba2 | 24.02 | 28.20 | 34.77 | 67.08 | 40.84 | 50.74 | 60.35 | 28.83 | 38.94 | 61.49 | 47.88 |
| Gated DeltaNet + Mamba2 + SWA | 23.69 | 26.83 | 36.17 | 67.51 | 41.51 | 51.85 | 61.19 | 29.77 | 38.58 | 53.73 | 47.54 |
| Mamba2 + SWA + Gated DeltaNet | 24.14 | 25.21 | 36.79 | 64.96 | 41.18 | 52.01 | 60.90 | 30.03 | 38.07 | 59.44 | 47.92 |
| Mamba2 + Gated DeltaNet + SWA | **23.54** | **24.11** | 36.92 | 66.48 | 41.70 | 52.72 | 61.06 | 30.54 | 39.91 | 60.51 | **48.73** |

Table S.1 presents ablation studies on the Gated DeltaNet block's components [p. 22]. Our experiments demonstrate that both the short convolution and output gate are crucial for model performance, while output normalization yields marginal improvements [p. 22]. Consistent with Yang et al. (2024b), we found L2 normalization to be essential for training, though the choice of feature map was less influential [p. 22]. Nevertheless, SiLU consistently outperformed other activation functions, aligning with observations from Qin et al. (2023a) [p. 22]. Through empirical analysis, we determined that a head dimension of 128 provides an optimal trade-off between performance and computational efficiency [p. 22]. Additionally, Table S.2 demonstrates that among various hybrid architectures, the combination of Mamba2, Gated DeltaNet, and SWA in this specific order produces superior results [p. 22].
