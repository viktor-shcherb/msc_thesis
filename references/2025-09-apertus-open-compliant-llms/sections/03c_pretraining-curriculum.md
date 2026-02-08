# 3.3 Pretraining Curriculum [p. 21–25]

[p. 21] This section details the pretraining data stages used for pretraining Apertus. Similar to previous research (Martins et al., 2025; Allal et al., 2025), the training is separated into several stages, focusing on different model capabilities, beginning with broad natural language modelling and basic mathematical and coding capabilities, and progressively incorporating more diverse and higher-quality data with a higher proportion of mathematical and code data as training progresses. Cooldown experiments are performed using intermediate model checkpoints to determine the mixture schedule.

[p. 22] The model is trained on 15T tokens (~0.3T masked due to Goldfish Loss) divided into five stages:

1. **Stage 1 (0T -- 5T Tokens):** Focuses on building a robust foundation in natural language modelling and incorporating core mathematical and code concepts. Uses the larger Score-2 subset of FineWeb-Edu dataset, FineWeb-2-HQ data with quality filtering retaining 33% highest-quality data and FineWeb-2 for other languages, CommonCrawl subset of FineMath, and StarCoder data.

2. **Stage 2 (5T -- 9T Tokens):** Focuses on expanding the diversity and quality of English data. Uses the smaller and higher-quality Score-3 subset of FineWeb-Edu and introduces English FineWeb-HQ data with quality filtering retaining 33% highest-quality data. Note that FineWeb-Edu and FineWeb-HQ are not mutually exclusive, but use different filtering criteria. Maintains multilingual, mathematical and code data mixture from Stage 1, consisting of FineWeb-2-HQ data with quality filtering retaining 33% highest-quality data and FineWeb-2 data for other languages, CommonCrawl subset of FineMath, and StarCoder data.

3. **Stage 3 (9T -- 12T Tokens):** Starts to increase math ratio, in addition to the data mixture of Stage 2 adds InfiMM-WebMath subsets of FineMath and LLM360-MegaMath web.

4. **Stage 4 (12T -- 13.5T Tokens):** Further focuses on improving data quality and increasing the amount of mathematical and code content. To improve the quality of natural language data, uses the DCLM-Edu dataset, FineWeb-2-HQ data with quality filtering retaining 10% highest-quality data, and FineWeb-2 data for other languages. For mathematical data replaces LLM360-MegaMath web with LLM360-MegaMath web-pro. The StarCoder data remains unchanged.

5. **Stage 5 (13.5T -- 15T Tokens):** The last pretraining stage, the learning rate cooldown. Further refines data quality by incorporating CommonPile/Stack v2 Edu and StarCoder datasets scored at 2, along with data scored higher than 3 sampled twice. Additionally, adds Clean-Wikipedia, data parallel data (Europarl and Paradocs) and English as well as multilingual instruction and task data, the Data Provenance Initiative subset of Flan and the Euroblocks.

[p. 22] During Stages 1-3, the small, specially-crafted canary datasets are also included to detect and measure verbatim memorization by the model in evaluations, as detailed in Section 3.2.4. In Stages 1-2, Gutenberg-V1 and Poison data are used. In Stage 3, Gutenberg-V2 data is used. Stage 2 was only used in the 70B run. For the 8B model, Stage 1 lasted until 7T tokens where it switched directly to Stage 3.

[p. 22] The pretraining framework (built on top of Megatron-LM; Shoeybi et al., 2019) did not natively support training with multiple data mixtures, as it keeps track of the total number of consumed samples independent of the data mixture specified. To enable this functionality, the dataloader state is reset by subtracting the total number of samples consumed thus far [p. 23] to the dataloader sampler. In addition, the dataset seed was modified when transitioning to stages 3, 4, and 5 to introduce additional data reshuffling and reduce redundancy, ensuring better coverage of the training corpus across later mixtures.

## Cooldown Experiments [p. 23]

[p. 23] The project began with the Stage 1 data mixture. Once training and infrastructure had stabilized, the data mixture was updated to incorporate the most recent and best available data quality filters. To guide mixture selection for subsequent pretraining stages, prior work (Grattafiori et al., 2024; Blakeney et al., 2024) was followed and cooldown experiments on 1.5B ablation model checkpoints were run, evaluating candidate datasets. For Stage 5 (the cooldown of the final model), larger 8B cooldown ablations were conducted.

*Intermediate Stages Cooldowns.* To refine mixtures for Stages 2-4, cooldowns with a 70/30 setup are used: 70% of the Stage 1 data plus 30% of the dataset being tested, sometimes replacing the FineWeb-Edu Score-2 *base* English dataset. These ratios were only for evaluation and do not necessarily match the proportions in the final training mixtures (see Table 6). Cooldowns used a learning rate schedule that decayed to zero over 100B tokens with a 1-sqrt schedule. After measuring dataset impact in this setup, cooldown experiments were also run using the proposed final mixtures to validate their performance. These experiments were carried out on a 1.5B model (see Section 2.4), with each cooldown spanning 100B tokens: [p. 23]

1. **Regular:** Stage 1 data mixture to isolate the impact of data change during LR cooldown.
2. **30% DCLM:** Downsampled Stage 1 mixture to 70% and include the DCLM dataset with 30% total weight.
3. **30% DCLM-edu:** Downsampled Stage 1 mixture to 70% and include the DCLM-edu dataset with 30% total weight.
4. **30% FW-HQ-10:** Downsampled Stage 1 mixture to 70% and include the FineWeb-HQ dataset (10% highest quality data) with 30% total weight.
5. **Base-FW-HQ-33:** Stage 1 data mixture where FineWeb-Edu Score-2 has been replaced with FineWeb-HQ (33% highest quality).
6. **Base-FW-HQ-33 + 30% DCLM-edu:** Stage 1 data mixture where FineWeb-Edu Score-2 has been replaced with FineWeb-HQ (33% highest quality), downsampled to 70% total weight, and the DCLM-edu dataset included with 30% total weight.
7. **Base-FW-HQ-33 + 30% FW-HQ-10:** Stage 1 data mixture where FineWeb-Edu Score-2 has been replaced with FineWeb-HQ (33% highest quality), downsampled to 70% total weight, and the FineWeb-HQ (10% highest quality), dataset included with 30% total weight.
8. **Base-FW-HQ-33 + 30% FW-edu (score-3):** Stage 1 data mixture where FineWeb-Edu Score-2 has been replaced with FineWeb-HQ (33% highest quality), downsampled to 70% total weight, and the FineWeb-edu dataset (small score-3 subset) included with 30% total weight.

[p. 23] These ablations were run without robots/compliance filtering (results in Table 7). Most mixtures were later revalidated at the 3B scale under full compliance filtering. Among the tested datasets, **DCLM-edu gave the largest performance gain**, while replacing FineWeb-Edu with FineWeb-HQ-33 consistently improved results. Because DCLM-edu is limited in size, a phased approach was adopted: in Stages 2 and 3, FW-HQ was used together with FineWeb-Edu Score-3 as the English component; later, once large-scale DCLM-edu availability was secured, the switch was fully made to DCLM-edu. In parallel, the weighting of code and math data was increased.

### Table 7: Cooldown Ablations on 1.5B Model [p. 25]

> "We report aggregated benchmarks (Full, English, Multilingual)"

| Configuration | Full Macro Acc. | English Macro Acc. | Multilingual Macro Acc. |
|---|---|---|---|
| Regular | 0.44738 | 0.45175 | 0.44301 |
| 30% DCLM | 0.45215 | 0.45968 | 0.44461 |
| 30% DCLM-edu | 0.45383 | 0.46158 | 0.44608 |
| 30% FW-HQ-10 | 0.45304 | 0.46041 | 0.44567 |
| Base-FW-HQ-33 | 0.44888 | 0.45529 | 0.44248 |
| Base-FW-HQ-33 + 30% DCLM-edu | 0.45380 | 0.45266 | 0.44322 |
| Base-FW-HQ-33 + 30% FW-HQ-10 | 0.45219 | 0.46030 | 0.44409 |
| Base-FW-HQ-33 + 30% FW-edu | 0.45041 | 0.45492 | 0.44590 |

### Table 6: Pretraining Data Mixture Composition and Token Counts [p. 24]

> "Note that not necessarily all tokens of each stage data were consumed, due to the stage duration. For precise dataset versions and links, see Section 3 and our data reproduction codebase github.com/swiss-ai/pretrain-data. Stage durations in tokens below refer to the 70B model pretraining. For the 8B version, Stage 1 lasted until 7T tokens, after switched directly to Stage 3 (while doubling the global batch size). More details in Appendix H.3."

**Stage 1 (0T - 5T tokens)**

| Dataset | Total Tokens (B) |
|---|---|
| FineWeb-Edu (Score-2) | 4815 |
| FineWeb-2-HQ (33% highest quality) and FineWeb-2 (random 33% sample of remaining languages) | 3557 |
| StarCoder | 235 |
| FineMath CommonCrawl subset | 32 |
| Gutenberg V1 and poison | 2 |

**Stage 2 (5T - 9T tokens)**

| Dataset | Total Tokens (B) |
|---|---|
| FineWeb-HQ (33% highest quality) | 4064 |
| FineWeb-2-HQ (33% highest quality) and FineWeb-2 (random 33% sample of remaining languages) | 3557 |
| FineWeb-Edu (Score-3) | 1179 |
| FineMath CommonCrawl subset | 32 |
| StarCoder | 235 |
| Gutenberg V1 and poison | 2 |

**Stage 3 (9T - 12T tokens)**

| Dataset | Total Tokens (B) |
|---|---|
| FineWeb-HQ (33% highest quality) | 4064 |
| FineWeb-2-HQ (33% highest quality) and FineWeb-2 (random 33% sample of remaining languages) | 3556 |
| FineWeb-Edu (Score-3) | 1179 |
| StarCoder | 235 |
| FineMath CommonCrawl subset | 32 |
| InfiMM-WebMath CommonCrawl subset | 19 |
| LLM360-MegaMath Web | 260 |
| Gutenberg V2 | 1 |

**Stage 4 (12T - 13.5T tokens)**

| Dataset | Total Tokens (B) |
|---|---|
| DCLM-Edu | 1619 |
| FineWeb-2-HQ (10% highest quality) and FineWeb-2 (random 10% sample of remaining languages) | 986 |
| StarCoder | 234 |
| FineMath CommonCrawl subset | 32 |
| InfiMM-WebMath CommonCrawl subset | 19 |
| LLM360-MegaMath Web-Pro | 15 |

**Stage 5 (13.5T - 15T tokens)**

| Dataset | Total Tokens (B) |
|---|---|
| DCLM-Edu | 1619 |
| FineWeb-2-HQ (10% highest quality) and FineWeb-2 (random 10% sample of remaining languages) | 986 |
| StarCoder (twice with threshold above 2 and 3) | 182 |
| CommonPile/Stack v2 Edu | 68 |
| FineMath CommonCrawl subset | 32 |
| InfiMM-WebMath CommonCrawl subset | 19 |
| LLM360-MegaMath Web-Pro | 15 |
| Clean Wikipedia | 33 |
| Translation parallel data | 21 |
| 3 replica of Task data | 3 x 1 |
