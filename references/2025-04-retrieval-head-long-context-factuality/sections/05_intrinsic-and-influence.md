# 3.3 Intrinsic [p. 6] (continued)

---
[p. 6 continued]

being continuously pre-trained, chat fine-tuned, or sparsely upcycled, there is a notable consistency in their retrieval scores heatmaps. Figure 6 offers a more direct and strict examination, where the authors compute the statistical correlations between different models. The data reveal a high degree of correlation in the retrieval score distributions between base models and their respective variants, with a Pearson correlation coefficient exceeding 0.8. Models of different families exhibit a correlation coefficient of less than 0.1, indicative of their distinct pretraining recipes.

**Figure 6** (p. 6): "The retrieval heads of models of the same family are strongly correlated, i.e., the chat model and base model typically uses the same set of retrieval heads. The retrieval heads of models of different families are clearly different."

Description: Correlation heatmap matrix showing pairwise correlations between models.
- Key elements: 6×6 matrix with models on both axes (Llama-2-7B, Qwen1.5-14B, Mistral-7B-v0.2, Llama-2-7B-80K, Qwen1.5-14B-Chat, Mistral-8x7B-v0.1); color scale from 0 (light) to 1.0 (dark red)
- Notable patterns: Strong positive correlations (dark red cells, ~0.84-0.91) within model families (e.g., Llama-2-7B and Llama-2-7B-80K: 0.84; Qwen1.5-14B and Qwen1.5-14B-Chat: 0.87; Mistral-7B-v0.2 and Mistral-8x7B-v0.1: 0.91); near-zero correlations across different families (e.g., 0.00087, -0.022, -0.021)
- Supports claim: Models from the same family share similar retrieval head patterns, while different families have distinct patterns

**Figure 7** (p. 6): "Masking out top K retrieval heads vs K random heads. For all models are consider, the removal of retrieval heads clearly reduces the Needle-in-a-Haystack performance, versus the removal of non-retrieval heads have much weaker influence."

Description: Line graph showing accuracy vs number of masked heads.
- Key elements: X-axis shows "Masking K Heads" (0-100), Y-axis shows "Average Score" (20-100); multiple lines for different models and masking strategies
- Lines shown: Dashed lines (masking random heads) remain high (~80-100%) across all K values; solid lines (masking retrieval heads) drop sharply: Llama-2-7B-80K, Mistral-8x7B-v0.1, Yi-6B-200K all decline steeply; special note for "Retrieval Head" and "Random Head"
- Notable patterns: Masking retrieval heads causes dramatic performance drops (to ~20-30% at K=50-100), while masking random heads maintains high performance (80%+)
- Supports claim: Retrieval heads are causally important for Needle-in-a-Haystack performance

# 4 Influence on Downstream Tasks [p. 6]

This section examines how retrieval heads influence downstream tasks. Across the experiments the authors use Mistral-7B-Instruct-v0.2 [18] as it is a popular and strong open language model with 32K context length. The authors first show that retrieval heads explains the factuality of Needle-in-a-Haystack test. When the model can retrieve the needle and produce the required answer, retrieval heads are activated. When the model cannot retrieve and hallucinate instead, retrieval heads are either partially activated or not activated. Then the authors show that retrieval heads significantly influence questions answering that requires extracting the information from the input, but does not strongly influence tasks where the model directly produce answers based on its intrinsic knowledge. The authors further explore how retrieval heads influence more sophisticated reasoning behaviors like chain-of-thought [23].

## 4.1 Retrieval Heads Explains Factuality in Needle-in-a-Haystack [p. 6]

The authors start with a closer look at Needle-in-a-Haystack and construct an additional set of needle tests that are different from the three sets used for retrieval head detection. The authors gradually mask out the number of retrieval/ random heads and observe the model's behavior changes. As is shown in Fig. 7, masking out retrieval heads severely damages the model's Needle-in-a-Haystack performance, while masking out random heads shows much smaller performance impact. Notably, when increasing the number of masked heads K to 50 (about 5% of the full number of heads), all models' needle test performance drop to below 50, showing that the top retrieval heads are responsible for most of the needle retrieval behavior.

The authors observe three types of error: (1) Incomplete retrieval, where models only captured partial information of the target and omitted key details; (2) Hallucination, where models generated hallucinated sentences; and (3) Wrong extraction, where models incorrectly retrieved irrelevant content from the haystack. Without any masking, instances of wrong extraction occurred when retrieval heads were active but focused on incorrect sections. During hallucinated generation, retrieval heads predominantly attended to the initial token of the input, which is often known as "attention sink" [24], presumably dummy tokens that provide less meaningful signal.

---
[p. 7 continued]

As the authors increase the number of masked heads, initially, a small subset of the most robust retrieval heads are masked, and incomplete retrieval began to appear. In the absence of the strongest retrieval heads, the remaining weaker heads only managed to retrieve a fraction of the target information. Metaphorically, each retrieval head holds a small piece of the "needle," yet these pieces cannot form a complete one, resulting in incomplete retrieval. This phenomenon typically begins when the mask out heads of retrieval score larger than 0.4. As the authors further increase the number of mask, hallucinations becoming more prevalent, signaling a complete failure of the retrieval capability.

**Figure 8** (p. 7): "Masking out retrieval heads severely damages ExtractQA performance."

Description: Bar chart showing F1 scores at different masking levels.
- Key elements: X-axis shows "Mask Num." (50 and 100), Y-axis shows "F1" (30-60); three bar types per group: "No Masking" (red, 56.7), "Retrieval Head" (green, 47.5 at 50 / 32.3 at 100), "Random Head" (green, 55.7 at 50 / 55.4 at 100)
- Notable patterns: At 50 masked heads, retrieval head masking drops to 47.5 F1 vs 56.7 baseline (random head masking stays at 55.7); at 100 masked heads, retrieval head masking drops to 32.3 F1 while random head masking maintains 55.4 F1
- Supports claim: Masking retrieval heads severely damages extractive QA performance

**Figure 9** (p. 7): "When the model fails to retrieve the full needle, there are two typical errors: (1) incomplete retrieval, where the retrieval heads miss part of the information 'eat a sandwich'; (2) hallucination, where the retrieval heads attend to the initial tokens."

Description: Two side-by-side diagrams showing attention patterns.
- Left diagram (Case 1: Incomplete Retrieval): Shows attention pattern for "Go to Dolores park on a sunny day" with attention of top retrieval heads [16-19], [11-15], [17-22], [19-15]. Below: "Go to Dolores park on a sunny day and eat a sandwich" → "Needle Sentence"
- Right diagram (Case 2: Hallucination): Shows "Golden Gate Bridge" with attention of top retrieval heads [16-19], [11-15], [17-22], [19-15]. Below: "[Begin of Input] Once upon a time..." → "Haystack"
- Notable patterns: In incomplete retrieval, heads attend to partial information; in hallucination, heads attend to initial tokens
- Supports claim: Different error modes have distinct attention patterns

## 4.2 Influence on Extractive QA [p. 7]

Now the authors study how retrieval heads influence more realistic tasks beyond Needle-in-a-Haystack. The authors use extractive QA as a test bed, as common usecase of long-context model where the user typically upload a pdf (research papers, finantial reports, legal documents, _etc) and ask questions about specific information within the document. When the knowledge being asked does not exist in the model's internal knowledge, the authors synthesize an extractive QA dataset by selecting a set of up-to-date news articles, extract a paragraph, and asking GPT-4 to produce a question-answer pair based on the extracted paragraph, similar to the evaluation conducted in Anthropic [1]. As illustrated in Figure 8, randomly masking out non-retrieval heads demonstrated no significant impact on performance. Masking out retrieval heads led to a substantial decrease in F1 scores, with reductions of 9.2% and 23.1%. These observations demonstrate that real-world document QA tasks heavily rely on the functionality of retrieval heads.

## 4.3 Chain-of-Thought Reasoning also Requires Retrieval Heads [p. 7]

The authors test Mistrial-7B-Instruct-v0.2's performance on MMLU [11], MuSiQue and GSM8K [4], with and without chain-of-thought reasoning. As is shown in Fig. 10, if the authors use answer-only prompting (without CoT), masking out either retrieval heads or random heads do not really influence the performance, presumably because the model's generation is based on its internal knowledge primarily stored in the FFN layers [8]. For CoT styled reasoning, masking out retrieval heads significantly influence the model's performance. Upon inspecting typically error cases (Fig. 11), the authors find out the model becomes "blind" to important input information and hallucinate instead. The authors find the relationship between CoT and retrieval heads particularly intriguing as it may offers deeper insights into model's complex reasoning performance. The authors leave more in-depth studies to future research.

**Figure 10** (p. 8): "Retrieval heads significantly influence tasks that require chain-of-thought reasoning. This is because typically in a reasoning chain, the next step reasoning requires the model to refer to previous information. See Fig. 11 for examples."

Description: Six subplots (3×2 grid) showing accuracy for three benchmarks with/without CoT.
- Top row (with CoT):
  - GSM8K (w/ CoT): No Masking ~45.1, Masking Retrieval ~34.4, Masking Random ~22.1-21.3, 50 heads shows ~2.0 at 100
  - MMLU (w/ CoT): No Masking ~43.6, Masking Retrieval ~37.6, values at 50: ~26.1, ~29.3, ~24.8
  - MuSiQue (w/ CoT): No Masking shows values ~14.2, with Masking Retrieval ~9.3-11.4-11.3-9.9
- Bottom row (w/o CoT):
  - GSM8K (w/o CoT): Values remain low: ~1.8, ~2.8, ~2.5, ~2.3, ~2.3 at different mask levels
  - MMLU (w/o CoT): Values ~55.6-57.2-57.6, ~54.2-54.0 showing minimal degradation
  - MuSiQue (w/o CoT): Legend shows "No Masking", "Masking Retrieval", "Masking Random"; values ~14.0-16.0-17.6, ~12.5, ~14.6
- X-axis: "Mask Num." (50 and 100 for most plots)
- Y-axis: "Acc" (accuracy percentage)
- Notable patterns: CoT tasks show dramatic drops when masking retrieval heads; non-CoT tasks show minimal impact
- Supports claim: Retrieval heads are critical for chain-of-thought reasoning

**Figure 11** (p. 8): "When we mask out retrieval heads, the model becomes 'blind' to important information in the question description resulting in incorrect reasoning chains."

Description: Two example questions with masking demonstrations.
- Question 1 (left box): "Misha bought 3 pairs of shorts, 3 pairs of pants, and 3 pairs of shoes. One pair of shorts costs $16.50. One pair of pants costs $22.50 and one pair of shoes costs $42. How much did Misha spend on all the clothing items?"
- Masking Top 100 Retrieval Heads demonstration:
  1. "Let's calculate the total cost of each type of clothing for Misha:"
  2. "For shorts, there are 3 pairs, so the total cost is 3 * $16.5 = $59.10."
  3. "For pants, the cost is the same, so 3 pairs cost 3 * $22 = $66." [error]
  4. "For shoes, there are 3 pairs, so the total cost is 3 * $42 = $126."
  5. "So, the answer is $125." [error]
  - Shows: "Misunderstood Information" highlighted on "$22.50" being misread as "$22"
- Question 2 (right box): "James decides to run 3 sprints 3 times a week. He runs 60 meters each sprint. How many total meters does he run a week?"
- Masking Top 100 Retrieval Heads:
  1. "James runs 3 times a week for each sprint session."
  2. "During each session, he covers a distance of 60 meters (3 times the length of a standard football field goal post)."
  3. "Therefore, the total distance James covers in a week is:"
  4. "6 (sessions in a week) x1 (number of sprints in session)"
  5. "x 60(meters in a sprint)= 360 meters."
  6. "So, James runs a total of 360 meters every week."
  - Shows: "Misunderstood Information" highlighted on "3 sprints 3 times a week" and "60 meters"
- Notable patterns: Model loses track of numerical values when retrieval heads masked, leading to calculation errors and incomplete reasoning
- Supports claim: Retrieval heads enable the model to refer back to question details during multi-step reasoning
