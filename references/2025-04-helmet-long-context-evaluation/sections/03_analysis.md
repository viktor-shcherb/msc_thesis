# Analysis [p. 7-9]

The authors evaluate 59 LCLMs with HELMET [p. 7]. To their best knowledge, this is the most thorough and controlled comparison of long-context models on diverse applications [p. 7]. These models cover closed-source models, such as GPT-4, Claude, and Gemini, as well as open-source model families, such as Llama (Dubey et al., 2024), Mistral (Jiang et al., 2023), Phi (Abdin et al., 2024), and Qwen (Qwen et al., 2025) [p. 7]. They also consider models with different architectures—full dense transformers (Vaswani et al., 2017), sliding-window attention (Beltagy et al., 2020), and hybrid models with SSM modules (Dao & Gu, 2024) [p. 7]. They also consider models with extra-long context extrapolation training such as YaRN (Peng et al., 2024) and LongRoPE (Ding et al., 2024) [p. 7]. They list all the models evaluated in Table 15 [p. 7]. They evaluate each model at input lengths: L ∈ {8K, 16K, 32K, 64K, 128K}, where L is the number of Llama 2 tokens (Touvron et al., 2023), using greedy decoding for all models to ensure consistency [p. 7]. They randomly sample 100 to 600 examples from each dataset; more details are in §D [p. 7].

## 3.1 Simple Synthetic Tasks Are Poor Predictors of Real-World Performance [p. 7]

Many model developers rely on simple synthetic tasks, such as NIAH, for evaluating long-context language models, but it is unclear if these tasks correlate with real-world performance [p. 7]. To this end, the authors calculate Spearman's rank correlation ρ between synthetic and real-world tasks for 35 instruction-tuned models [p. 7]. First, Figure 3 shows that none of the synthetic tasks achieves an average correlation higher than 0.8 [p. 7]. They make the following observations [p. 7]:

**Figure 3** (p. 7): Spearman's rank correlation at 128K input length, calculated across 35 instruction-tuned models.

Description: Heatmap showing correlation values between different task types on the left axis (NIAH, RULER MK, RULER MV, RULER All, Recall, RAG) and task categories on the right (ICL, Cite, Re-rank, LongQA, Summ, Avg).

Key patterns:
- NIAH shows correlations: 0.44 (ICL), 0.71 (Cite), 0.75 (Re-rank), 0.76 (LongQA), 0.72 (Summ), 0.68 (Avg)
- RULER MK: 0.48 (ICL), 0.73 (Cite), 0.84 (Re-rank), 0.79 (LongQA), 0.87 (Summ), 0.74 (Avg)
- RULER MV: 0.61 (ICL), 0.71 (Cite), 0.77 (Re-rank), 0.83 (LongQA), 0.79 (Summ), 0.74 (Avg)
- RULER All: 0.51 (ICL), 0.77 (Cite), 0.85 (Re-rank), 0.79 (LongQA), 0.83 (Summ), 0.75 (Avg)
- Recall: 0.61 (ICL), 0.74 (Cite), 0.85 (Re-rank), 0.82 (LongQA), 0.85 (Summ), 0.77 (Avg)
- RAG: 0.5 (ICL), 0.72 (Cite), 0.85 (Re-rank), 0.92 (LongQA), 0.89 (Summ), 0.78 (Avg)

Supports claim: None of the synthetic tasks achieves an average correlation higher than 0.8; demonstrates varying correlation strengths across different task types.

**Not all synthetic tasks are created equal.** The original NIAH, which places a needle in the middle of unrelated essays and asks the model to retrieve it, exhibits weak correlation with real-world tasks: all correlations are less than 0.8 [p. 7]. Similarly, the popular RULER average score—which includes not only NIAH variants but also question generation, multi-hop tracing, and QA—does not yield strong correlations (all < 0.85) [p. 7].

They take a closer look at different RULER tasks and find that harder recall-type tasks are more reflective of real-world categories—for example, RULER MK, which places distracting needles around the target needle [p. 7]. Despite the overall correlation, these tasks can still serve as a useful sanity check during model development [p. 7]. They compile several such RULER tasks, along with JSON KV, to form the HELMET synthetic recall set (more discussions in §E.1) [p. 7].

**Tasks with noisier, more distracting contexts better differentiate models.** To understand why synthetic tasks exhibit weak correlation with real-world tasks, they plot the performance of different models on NIAH, RULER MK (one of their recall tasks), and HotpotQA (one of their RAG tasks) in Figure 4 [p. 7-8]. They use x-BENCH QA as a representative real-world task [p. 8]. Most models achieve either perfect or near-zero performance on the original NIAH, leaving few data points in the middle and resulting in poor separability between models [p. 8]. But RULER MK, which introduces more distracting contexts, better distributes model performance between 0% and 100%, leading to clearer differentiation [p. 8].

**Figure 4** (p. 8): Distribution of instruction-tuned models' performance on x-BENCH QA with respect to NIAH, RULER MK, and HotpotQA.

Description: Three scatter plots showing the relationship between x-BENCH QA performance (y-axis, labeled "InfBench QA") and three different tasks (x-axis).

Key details:
- Left plot (NIAH): n=35, Spearman rho=0.63, p=5.1e-05. Points clustered at extremes (0 and 100 on x-axis), poor separation
- Middle plot (RULER MK): n=35, Spearman rho=0.81, p=3.2e-09. Better distribution across 0-100 range
- Right plot (HotpotQA): n=35, Spearman rho=0.88, p=2.9e-12. Points well distributed across 0-60 range

Supports claim: Original NIAH shows poor separability with most models at extremes; RULER MK provides better distribution; RAG tasks like HotpotQA show even better correlation and distribution.

**RAG is a better proxy for real-world tasks.** Finally, they find that RAG datasets, such as HotpotQA, consistently achieve higher correlation with other real-world tasks [p. 8]. Figure 4 also shows that HotpotQA exhibits an almost linear relationship with the QA dataset [p. 8]. Similar to synthetic tasks, RAG tasks are easy to control and assess models' recall abilities [p. 8]. However, since all passages are retrieved and relevant to the query, RAG contexts are more distracting and therefore harder to saturate [p. 8].

## 3.2 Diverse LCLM Applications Call for Diverse Evaluation [p. 8]

In long-context language modeling, realistic tasks are often only used in isolation (Karpinska et al., 2024; Li et al., 2024c; Dubey et al., 2024), which limits the understanding of LCLMs in a broader context [p. 8]. In this work, they cross-examine models' performance over a wide range of real tasks, and find that different categories do not consistently correlate with each other, as shown in Figure 5 [p. 8].

**Figure 5** (p. 8): Spearman rank correlation between different categories at L = 128K.

Description: Heatmap showing correlation matrix between different task categories (Recall, RAG, Cite, Re-rank, LongQA, Summ, ICL).

Key correlation values:
- Recall-RAG: 0.88
- Recall-Cite: 0.74
- Recall-Re-rank: 0.85
- Recall-LongQA: 0.82
- Recall-Summ: 0.85
- Recall-ICL: 0.61
- RAG-Cite: 0.72
- RAG-Re-rank: 0.85
- RAG-LongQA: 0.92
- RAG-Summ: 0.89
- RAG-ICL: 0.5
- Cite-Re-rank: 0.84
- Cite-LongQA: 0.72
- Cite-Summ: 0.82
- Cite-ICL: 0.34
- Re-rank-LongQA: 0.87
- Re-rank-Summ: 0.89
- Re-rank-ICL: 0.36
- LongQA-Summ: 0.85
- LongQA-ICL: 0.51
- Summ-ICL: 0.38

(Values shown with color gradient from light/low correlation to dark/high correlation)

Supports claim: Different categories show moderate correlation but do not consistently correlate strongly with each other; ICL shows notably low correlation with several categories (0.34-0.51 range), while generation with citations also shows lower correlation with other categories.

Recall and RAG show moderate correlation due to their shared retrieval component [p. 8]. However, the added complexity of generating citations in ALCE results in lower correlation with other categories [p. 8]. Naturally, RAG and passage re-ranking moderately correlate due to the shared retrieval component [p. 8]. As shown in Figure 5, generating correct answers and producing valid citations are not strongly correlated, suggesting that instruction following and recalling facts in long contexts are distinct capabilities [p. 8].

Furthermore, some categories—generation with citations and in-context learning—do not correlate well with other categories [p. 8]. Intuitively, summarization tests for the model's ability to aggregate information across the entire input, while ICL evaluates its ability to learn new tasks from many examples [p. 8]. Such capabilities are orthogonal to recall facts in long contexts [p. 8]. Therefore, model developers should evaluate across many distinct axes to form a more holistic understanding of a model's capabilities (see additional analysis in §E.2) [p. 8].

## 3.3 Model Performance Across Tasks and Lengths [p. 8-9]

They show the performance of instruction-tuned models on HELMET at five different lengths in Figure 6, and the full results are illustrated in Figure 10 [p. 8]. They analyze the model performance across two critical dimensions of long-context language modeling: task complexity and input length [p. 8].

**Open-source models lag behind closed-source models on complex tasks.** First, they consider the performance of frontier LCLMs at the longest input length of 128K tokens [p. 8]. They find that the closed-source models—notably GPT-4o-08 and Gemini-1.5-Pro—stand out as the strongest LCLMs [p. 8]. Other than ICL, the closed-source models outperform the open-source models on all tasks [p. 8]. The gap is relatively small on synthetic recall and LongQA, where the task is to retrieve information from the context [p. 8]. There is a stark contrast in the generation with citations and re-ranking performance, where the closed-source models are 30 to 40 absolute points better than the best open-source models [p. 8].

**Figure 6** (p. 9): Results of HELMET. All models are instruction-tuned and have a claimed context window of 128K tokens or more.

Description: Large heatmap table showing performance scores across multiple models, tasks, and input lengths.

Structure:
- Rows: Different models (GPT-4, GPT-4o-05, GPT-4o-08, Claude-3.5-Sonnet, Gemini-1.5-Flash, Gemini-1.5-Pro, Llama-3.1-8B, Llama-3.1-70B, Llama-3.1-70B, Mistral-Nemo, MegBeam-Mistral, Ministral-8B, Phi-3-mini-128k, Phi-3-small-128k, Phi-3-med-128k, Phi-3.5-mini, Qwen2.5-72B, Qwen2.5-7B-IM, Qwen2.5-14B-IM, Jamba-1.5-Mini, ProLong)
- Columns grouped by: Recall, RAG, Cite, Re-rank (at different input lengths: 8K, 16K, 32K, 64K, 128K)
- Second set of columns: LongQA, then additional metrics with "Avg" column
- Color-coded cells showing performance scores (darker = better performance)

Key observations from the table:
- GPT-4o-08 shows strong performance across most categories
- Closed-source models (GPT-4, Claude, Gemini) generally outperform open-source
- Performance varies significantly by task type and input length
- Some models show degradation at longer input lengths

Supports claim: Comprehensive results showing model performance across diverse tasks and lengths; demonstrates performance gaps between closed and open-source models.

**Performance degradation with longer inputs is category-dependent.** Most frontier models largely retain performance on recall and RAG at longer inputs; however, even the best models experience significant degradation as context length increases on tasks like re-ranking and generation with citations [p. 9]. As illustrated in Figure 7, performance degradation at longer lengths becomes more pronounced as task complexity grows from left to right [p. 9]. On generation with citations, open-source models completely collapse at 128K, while GPT-4o remains relatively stable [p. 9]. This underscores the importance of evaluating models over more complex long-context applications [p. 9].

**No clear winner across all categories.** As they observe from the previous sections, the different categories do not always correlate with each other [p. 9]. This is evident in the varying top-performing models across categories: for instance, GPT-4o is the best on recall and generation with citations, while Gemini performs better in passage re-ranking and long-document QA [p. 9]. Furthermore, many open-source models outperform closed-source models on ICL, potentially because heavy instruction tuning negatively impacts ICL [p. 9]. They provide qualitative examples in Table 19 [p. 9]. Thus, evaluating models across multiple axes is essential [p. 9]. In the appendix, they also present additional analysis, such as the performance of positional embeddings and extrapolation methods (§E.3), the lost-in-the-middle phenomenon (§E.4), and the performance of Claude (§E.6) [p. 9].

**Figure 7** (p. 10): Results of selected instruction-tuned models on various lengths and increasing complexity of tasks. Notably, Qwen2 relies on position extrapolation, while other open-models are trained at or greater than 128K context window.

Description: Heatmap table showing performance for selected models across different tasks and input lengths.

Structure:
- Rows: GPT-4o-08, Gemini-1.5-Pro, Llama-3.1-8B-Inst, Llama-3.1-70B-Inst, Jamba-1.5-Mini, Qwen2.5-7B-Inst, Qwen2.5-57B-Inst
- Columns grouped by task complexity (left to right): NIAH, RAG, Re-rank, Cite
- Each task shows results at multiple input lengths: 8K, 16K, 32K, 64K, 128K
- Color-coded cells (green = high performance, red = low performance)

Key values visible (selected examples):
- GPT-4o-08: NIAH (100.0 across all lengths), RAG (high 90s), Re-rank (85.8-89.2), Cite (45.4-48.8)
- Gemini-1.5-Pro: NIAH (98.5-100.0), RAG (73.8-77.4), Re-rank (77.6-81.7), Cite (47.3-48.2)
- Llama-3.1-8B-Inst: Shows degradation, especially on complex tasks at longer lengths
- Qwen2.5-57B-Inst: NIAH (100.0 at 8K-64K, 96.6 at 128K), significant drops on harder tasks at longer lengths

Supports claim: Performance degradation increases with task complexity; open-source models struggle more at longer contexts on complex tasks; position extrapolation (Qwen2) vs trained context window affects performance.
