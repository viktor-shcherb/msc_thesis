# 5 Analysis [p. 7–9]

[p. 7] The authors perform a detailed analysis of the results, identifying and emphasizing several notable and interesting phenomena.

## 5.1 Length Ablation

[p. 7] In line with the benchmark's goal to assess proficiency in managing lengthy contexts, the authors verify the baselines' capability with shortened context versions. A subset of the auto-generated tasks is modified accordingly, and the performance outcomes are illustrated in Figure 4. It is observed that model performance generally declines with longer input lengths compared to shorter ones. This suggests that while these baselines are technically equipped to handle extended inputs, their effectiveness diminishes significantly under such conditions.

### Figure 4

**Figure 4** (p. 8): "Baseline performance as a function of input length."

Four subplots showing performance vs. input length for four tasks:

- **Retrieve.KV** (x-axis: Length in # KV pairs, range 0–3000; y-axis: Scores, range 0–100): GPT-4 starts near 100 and gradually declines to ~50 at 3000 pairs. Kimi-Chat starts near 80 and drops to ~50. YaRN-Mistral stays near 0 throughout.
- **Math.Find** (x-axis: Length in # numbers, range 0–30000; y-axis: Scores, range 0–60): GPT-4 starts around 60 and declines to ~20–30 at longer lengths. Kimi-Chat and YaRN-Mistral both start around 30–40 and decline, converging near 20.
- **Code.Run** (x-axis: Length in # functions, range 0–5000; y-axis: Scores, range 0–75): GPT-4 starts at ~75 and drops steeply to near 0 around 2000–3000 functions. Kimi-Chat and YaRN-Mistral remain near 0 throughout.
- **En.Dia** (x-axis: Length in # characters, range 0–200000; y-axis: Scores, range 0–60): GPT-4 starts near 40 and shows modest decline. Kimi-Chat starts near 60 and declines. YaRN-Mistral fluctuates around 10–20.

## 5.2 Lost in the Middle

[p. 7–8] Prior research indicates a performance decline in some LLMs when answers are positioned around the center of the context (Liu et al., 2023). However, the authors' findings do not strongly corroborate this. As depicted in Figure 5, the authors analyze model performance based on answer location in three location-dependent tasks. They observe *no consistent trend between performance and answer position across different models*. For instance, GPT-4 shows a preference for early answers in Retrieval.KV but favors later ones in En.Dia. In contrast, Claude 2's performance remains relatively unaffected by answer position on all three tasks, whereas YaRN-Mistral and Kimi-Chat excel with end-positioned answers (except that YaRN-Mistral gets zero performance on all positions on Retrieval.KV).

[p. 8–9] One plausible reason why the authors have different observations from Liu et al. (2023) is that they experiment with different models using at most 16K length contexts, which is about 8 times shorter than the authors' setting. The models in their study are also different from the authors'. Finally, the tasks are different: their experiments involve document question answering (and their result with Retrieval.KV arguably does not show a very pronounced performance drop as well). The authors hypothesize that the phenomenon of "Lost in the middle" is only exhibited on specific tasks and models. A more thorough investigation of these differences is beyond the scope of this paper.

### Figure 5

**Figure 5** (p. 8): "Performance as a function of the answer position (in the number of characters). The steep drop in performance for Kimi-Chat in the middle on Retrieval.KV is caused by the answer being removed by truncation."

Three subplots showing Score (y-axis, 0–1.0) vs. Answer Position (x-axis, in number of characters) for four models (GPT-4, Kimi-Chat, Claude 2, YaRN-Mistral):

- **Retrieval.Number** (x-axis range: 0–440000): GPT-4 and Claude 2 remain consistently near 1.0 across all positions. Kimi-Chat stays near 0.8–1.0. YaRN-Mistral shows a dip to ~0.2–0.4 around position 200000, recovering to ~0.8 at the end.
- **Retrieval.KV** (x-axis range: 0–190000): GPT-4 starts near 1.0 and gradually declines to ~0.6. Claude 2 stays relatively stable near 0.6–0.8. Kimi-Chat shows a steep drop to 0.0 in the middle, then recovers. YaRN-Mistral remains at 0.0 throughout.
- **En.Dia** (x-axis range: 0–410000): GPT-4 shows variable performance, generally low (0.0–0.2) at the start, improving to ~0.2 at the end. Claude 2 stays near 0.4–0.6 across all positions. Kimi-Chat fluctuates around 0.0–0.2. YaRN-Mistral stays near 0.0–0.2.

## 5.3 Context Recalling

[p. 9] The authors identify an intriguing prompting technique for tasks involving extended context, termed *context recalling*. This technique posits that, although the information is present in the context and accessible via direct attention, it may be more effective to first prompt the model to *recall the relevant information in its generation before engaging in further reasoning*.

In their experiments using Code.Debug, when they merely instructed GPT-4 to process information step-by-step, the accuracy was **15.74%**. However, by explicitly directing GPT-4 to repeat the relevant code before analysis, its accuracy on Code.Debug markedly improved to **39.59%**. This approach of context recalling warrants additional investigation.

### Figure 6

**Figure 6** (p. 9): "Compared to the first prompt, the second prompt improves GPT-4's results on Code.Debug dramatically."

Two prompt box examples shown side by side:

- **First prompt (step-by-step only):** "One function in this repo is deliberately made to include an obvious error. Find it. \<code\> Think step by step and at last give me your answer for the function with the deliberate error. \<list of options\>"
- **Second prompt (context recalling):** "One function in this repo is deliberately made to include an obvious error. Find it. \<code\> Locate the functions in the options, repeat their content, inspect through code, and at last give me your answer for the function with the deliberate error. \<list of options\>"

The key difference is the second prompt explicitly asks the model to "repeat their content" before answering, which improved GPT-4 accuracy from 15.74% to 39.59% on Code.Debug.
