# Appendix C: Evaluation on Mathematical Reasoning [p. 16]

They continue training the 3B-size language models that support 64K input length (Section 3.3) with math data to evaluate their o1-style (Jaech et al., 2024) reasoning capability [p. 16]. The training consists of two stages: fine-tuning with synthetic math data, and distilling from DeepSeek-R1 (Guo et al., 2025) to promote o1-style reasoning [p. 16]. They evaluate the models across 8 math benchmarks: GSM-8K (Cobbe et al., 2021), MATH (Hendrycks et al., 2021), SVAMP (Patel et al., 2021), ASDiv (Miao et al., 2020), MAWPS (Koncel-Kedziorski et al., 2016), CARP (Zhang et al., 2023), TABMWP (Lu et al., 2023), and CollegeMath (Tang et al., 2024) [p. 16].

## Math Capability Evaluation

In the first stage, they train both DIFF Transformer and Transformer for additional 20B tokens on synthetic math data (Li et al., 2024) [p. 16]. The learning rate is 8e-5 [p. 16]. The batch size is 4M tokens [p. 16]. Hyperparameters are kept the same as in Section 3.3 [p. 16]. They evaluate the models every 2B tokens from 6B tokens to 20B tokens and report the average over 8 math datasets [p. 16]. The output length is restricted to 1K tokens [p. 16]. As shown in Figure 9, DIFF Transformer outperforms Transformer in solving mathematical problems [p. 16]. DIFF Transformer starts to substantially outperform Transformer after 15B tokens, reaching an accuracy gap of 11.3% by the end of 20B tokens [p. 16]. The results demonstrate that DIFF Transformer can learn to solve reasoning tasks more effectively than Transformer [p. 16].

**Figure 9** (p. 16): "DIFF surpasses Transformer in averaged accuracy over 8 math datasets."

Description: Line chart showing accuracy (%) on y-axis and number of tokens in billions on x-axis (from 10 to 20 tokens)
- Key elements: Two lines - orange line for "Diff (Ours)" and black line for "Transformer"
- Notable patterns: Both lines start around 30% accuracy at 10B tokens. DIFF Transformer (orange) shows steadier improvement and pulls ahead significantly after 15B tokens, reaching approximately 30% accuracy at 20B tokens. Transformer (black) shows more modest improvement, reaching approximately 20% accuracy at 20B tokens. The gap between the two widens substantially in the later training phase.
- Supports claim: DIFF Transformer can learn to solve reasoning tasks more effectively than Transformer, with an 11.3% accuracy advantage by 20B tokens [p. 16]

---
[p. 17 continued]

## o1-style Reasoning Evaluation

In the second stage, they further distill the models from OpenThoughts-114K-Math (Open-R1, 2025) [p. 17]. The dataset is filtered from OpenThoughts-114K (OpenThoughts, 2025) dataset [p. 17]. It consists of 89K math samples with the average length of 6K tokens [p. 17]. They apply supervised fine-tuning on the dataset to equip the models with o1-style reasoning capability [p. 17]. The learning rate is set to 1e-5 [p. 17]. The batch size is 1M tokens [p. 17]. Other hyperparameters are the same as in the first stage [p. 17]. They train both models for 2B tokens and select the best checkpoint for each [p. 17]. The output length is restricted to 16K tokens [p. 17]. As shown in Figure 10, DIFF Transformer outperforms Transformer on all benchmarks with an average accuracy gain of 7.5% [p. 17]. DIFF Transformer generates reasoning process with an average length of 6144 tokens, compared to 6913 for Transformer [p. 17]. The experimental results demonstrate the superior reasoning capability of DIFF Transformer over Transformer [p. 17]. It suggests that differential attention mechanism contributes to the improved performance in mathematical reasoning [p. 17].

**Figure 10** (p. 17): "Accuracy on 8 math benchmarks with o1-style reasoning."

Description: Bar chart comparing DIFF (Ours) in blue striped bars vs Transformer in solid light blue bars
- Key elements: 8 math benchmarks on x-axis (GSM-8K, MATH, SVAMP, ASDiv, MAWPS, CARP, TABMWP, CollegeMath) plus Average; accuracy (%) on y-axis ranging from 0 to 80%
- Notable patterns: DIFF Transformer (blue striped) consistently outperforms Transformer (light blue) across all benchmarks. Performance values for DIFF/Transformer: GSM-8K: 42.6/41.2, MATH: 25.0/19.9, SVAMP: 63.7/55.0, ASDiv: 83.8/79.8, MAWPS: 86.2/75.1, CARP: 42.5/32.3, TABMWP: 32.4/27.5, CollegeMath: 30.0/16.4, Average: 50.8/43.3
- Supports claim: DIFF Transformer achieves 7.5% average accuracy gain over Transformer on o1-style reasoning tasks [p. 17]
