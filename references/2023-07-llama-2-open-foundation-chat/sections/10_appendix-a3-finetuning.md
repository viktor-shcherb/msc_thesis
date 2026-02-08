# A.3 Additional Details for Fine-tuning [p. 51-56]

## Mathematical Reasoning [p. 51]

[p. 51] In Table 25, Llama 2 and other open-source datasets are compared on the GSM8k and MATH tasks.

**Table 25: Comparison to other open-source models on mathematical reasoning tasks, GSM8k and MATH** (maj1@1 is reported). [p. 51]

| Model | Size | GSM8k | MATH |
|---|---|---|---|
| MPT | 7B | 6.8 | 3.0 |
| | 30B | 15.2 | 3.1 |
| Falcon | 7B | 6.8 | 2.3 |
| | 40B | 19.6 | 5.5 |
| Llama 1 | 7B | 11.0 | 2.9 |
| | 13B | 17.8 | 3.9 |
| | 33B | 35.6 | 7.1 |
| | 65B | 50.9 | 10.6 |
| Llama 2 | 7B | 14.6 | 2.5 |
| | 13B | 28.7 | 3.9 |
| | 34B | 42.2 | 6.24 |
| | 70B | **56.8** | **13.5** |

## A.3.1 Detailed Statistics of Meta Human Preference Data [p. 51-53]

[p. 51] Table 26 shows detailed statistics on Meta human preference data. In total, 14 batches of human preference data (i.e., Meta Safety + Helpfulness) were collected on a weekly basis, consisting of over 1 million binary model generation comparisons. In general, later batches contain more samples as more annotators are onboarded over time and the annotators also become more familiar with the tasks and thus have better work efficiency. Multi-turn samples are also intentionally collected more to increase the complexity of RLHF data and thus the average number of tokens per sample also increases accordingly over batches.

**Table 26: Statistics of Meta human preference data (Safety & Helpfulness) per batch.** [p. 52] Note that a binary human preference comparison contains 2 responses (chosen and rejected) sharing the same prompt (and previous dialogue). Each example consists of a prompt (including previous dialogue if available) and a response, which is the input of the reward model. The number of comparisons, the average number of turns per dialogue, the average number of tokens per example, per prompt, and per response are reported.

| Batch | Num. of Comparisons | Avg. # Turns per Dialogue | Avg. # Tokens per Example | Avg. # Tokens in Prompt | Avg. # Tokens in Response |
|---|---|---|---|---|---|
| 1 | 5,561 | 4.4 | 547.1 | 25.2 | 159.3 |
| 2 | 17,072 | 4.0 | 554.6 | 22.4 | 170.7 |
| 3 | 30,146 | 3.9 | 603.3 | 19.6 | 195.5 |
| 4 | 36,206 | 3.9 | 652.8 | 45.3 | 182.9 |
| 5 | 49,375 | 3.7 | 603.9 | 46.7 | 163.1 |
| 6 | 57,746 | 4.1 | 654.5 | 28.2 | 198.1 |
| 7 | 84,388 | 3.9 | 662.2 | 27.5 | 210.0 |
| 8 | 95,235 | 3.6 | 670.4 | 32.9 | 212.1 |
| 9 | 127,235 | 3.6 | 674.9 | 31.3 | 214.8 |
| 10 | 136,729 | 3.7 | 723.9 | 30.5 | 230.2 |
| 11 | 136,868 | 3.8 | 811.9 | 32.2 | 251.1 |
| 12 | 181,293 | 3.9 | 817.0 | 30.8 | 250.9 |
| 13 | 210,881 | 4.2 | 905.9 | 30.3 | 255.6 |
| 14 | 249,356 | 4.3 | 1008.0 | 31.6 | 258.9 |
| Total | 1,418,091 | 3.9 | 798.5 | 31.4 | 234.1 |

[p. 51] In Figure 25, the preference rating change over batches is plotted. The share of samples with similar responses (e.g., *negligibly better* or *unsure*) increases dramatically over time while those with stronger preference (e.g., *significantly better*) drop in the meantime. This reflects the nature of the iterative model update and preference data annotation procedure -- with better-performing Llama 2-Chat models used for response sampling over time, it becomes challenging for annotators to select a better one from two equally high-quality responses.

**Figure 25** (p. 53): "Distribution of human preference data rating over batches. Over time, the share of samples with an unsure or negligibly better rating become larger with better performing Llama 2-Chat trained and available for preference data annotation."
- Line plot with x-axis: Meta Preference Data Batch Stage (1--14), y-axis: Percentage (%).
- Four lines: Significantly Better, Better, Slightly Better, Negligibly Better / Unsure.
- Significantly Better starts around 18% at batch 1 and drops to around 10% by batch 14.
- Better starts around 27% and drops to around 20% by batch 14.
- Slightly Better starts around 25%, rises to about 33% around batch 3-4, fluctuates, and ends around 30% at batch 14.
- Negligibly Better / Unsure starts around 30%, rises dramatically to about 40% by batch 12-13, ending around 37% at batch 14.
- Supports the claim that as Llama 2-Chat models improve, it becomes harder for annotators to distinguish between responses.

## A.3.2 Curriculum Strategy for Meta Human Preference Data [p. 51, 53]

[p. 51] High quality data is critical for alignment as discussed for SFT. The authors worked closely with the annotation platforms during the fine-tuning process, and opted for a curriculum annotation strategy. With the first model, annotators were asked to make prompts relatively simple, and then to progressively move towards more complex prompts and teaching new skills to Llama 2-Chat. An illustration of this curriculum annotation on the helpfulness preference data is displayed in Figure 26.

**Figure 26** (p. 53): "Annotation curriculum. Evolution for each new batch of the maximum and median score given a reward model for prompts samples with a models trained on each of the batches. We can see that the score progressively decrease, suggesting that the prompts are on average harder in the most recent batches."
- Plot with x-axis: Reward Annotation Stage (Batch 1 through Batch 12), y-axis: Reward Score (0.45--0.80).
- Two lines: "Max wrt 20 samples" (blue line with shaded area) and "Med wrt 20 samples" (orange line with shaded area).
- Max score starts around 0.78 at Batch 1 and progressively decreases to about 0.40 by Batch 11-12.
- Median score starts around 0.75 at Batch 1 and decreases to about 0.40 by Batch 11-12.
- Both lines show a clear downward trend, supporting the claim that prompts become harder over batches as the curriculum progresses.

## A.3.3 Ablation on Ranking Loss with Preference Rating-based Margin for Reward Modeling [p. 51-52, 54]

[p. 51] The ranking loss is ablated with the preference rating-based margin term for the helpfulness reward model. Two variants of m(r) with different magnitude for the margin term in Eq 2 are tried as listed in Table 27 and compared against the baseline without the margin term. Both per-rating and average accuracy on the Meta Helpful test set are reported in Table 28. The margin term can indeed help the reward model perform better on more separable comparison pairs and a larger margin can boost it further. However, the larger margin also regresses performance on similar samples.

**Table 27: Two variants of preference rating based margin with different magnitude.** [p. 52]

| | Significantly Better | Better | Slightly Better | Negligibly Better / Unsure |
|---|---|---|---|---|
| Margin Small | 1 | 2/3 | 1/3 | 0 |
| Margin Large | 3 | 2 | 1 | 0 |

**Table 28: Ablation on preference rating-based margin in Helpful reward model ranking loss.** [p. 52] The rating margin component helps improve model accuracy on samples with more separable response pairs (e.g., chosen response significantly better the rejected counterpart).

| | Significantly Better | Better | Slightly Better | Negligibly Better / Unsure | Avg |
|---|---|---|---|---|---|
| No margin | 79.1 | 66.9 | 59.8 | 54.5 | 62.5 |
| Margin Small | 80.4 | 67.3 | 60.4 | **55.0** | **63.0** |
| Margin Large | **80.7** | **67.5** | **60.5** | 54.3 | 62.9 |

[p. 51-52] The impact of margin-based loss on reward score distribution shifts is further evaluated. The histogram of reward scores from the test set is plotted in Figure 27. Essentially, the margin term pushes the reward model to assign more extreme scores to model generations to form a binary split pattern and a larger margin makes this distribution shift more significant. The above observation suggests investment in reward calibration for future work as reinforcement learning algorithms, such as PPO, can be sensitive to reward distribution change.

**Figure 27** (p. 54): "Reward model score distribution shift caused by incorporating preference rating based margin in ranking loss. With the margin term, we observe a binary split pattern in reward distribution, especially with a larger margin."
- Three histogram panels side by side.
- Left panel: "No Margin" -- x-axis: Density (0.0%--8.0%), y-axis: Reward Model Score (0.0--1.0). Shows a relatively uniform distribution of scores.
- Middle panel: "Margin Small" -- Same axes. Shows a more bimodal pattern beginning to emerge, with more scores near the extremes (0 and 1).
- Right panel: "Margin Large" -- Same axes. Shows a clear binary split pattern with most scores concentrated near 0 and near 1 (bimodal distribution).
- Supports the claim that the margin term pushes the reward model toward more extreme scores.

## A.3.4 Ablation on Ranking Loss with Safety Auxiliary Loss for Reward Modeling [p. 52-53]

[p. 52] The impact of the safety auxiliary loss is ablated with results on the Meta Safety test set shown in Table 29. As expected, the customized loss improves the recall of unsafe responses when using a reward score of 0.5 as the threshold (negative before Sigmoid) and thus offers a better safety reward signal for RLHF. Teaching the model to discriminate between safe and unsafe model generations also improves model accuracy on three subcategories.

**Table 29: Ablation on safety auxiliary loss term for safety reward modeling.** [p. 53] The safety auxiliary loss boosts accuracy on all 3 categories as well as the recall of unsafe response, measured by the percentage of unsafe responses captured with a reward score threshold of 0.5 (i.e., negative values before Sigmoid).

| | Avg | Safe Chosen / Unsafe Rejected | Safe Chosen / Safe Rejected | Unsafe Chosen / Unsafe Rejected | Unsafe Response Recall |
|---|---|---|---|---|---|
| Baseline | 63.7 | 93.0 | 56.0 | 59.5 | 73.0 |
| + Auxiliary Safety Loss | 64.5 | 94.3 | 56.9 | 59.9 | 90.4 |

## A.3.5 Additional Results for GAtt [p. 54-55]

[p. 54] The model ability to remember the system arguments trough a human evaluation is tested. The arguments (e.g. hobbies, persona) are defined during the first message, and then from turn 2 to 20. The model is explicitly asked to refer to them (e.g. "What is your favorite hobby?", "What is your name?"), to measure the multi-turn memory ability of Llama 2-Chat. The results are reported in Table 30. Equipped with GAtt, Llama 2-Chat maintains 100% accuracy, always referring to the defined attribute, and so, up to 20 turns (the evaluation was not extended further, and all the examples had less than 4048 tokens in total over the turns). As a comparison, Llama 2-Chat without GAtt can not anymore refer to the attributes after only a few turns: from 100% at turn t+1, to 10% at turn t+3 and then 0%.

**Table 30: GAtt results.** [p. 54] Llama 2-Chat with GAtt is able to refer to attributes 100% of the time, for up to 20 turns from our human evaluation. We limited the evaluated attributes to public figures and hobbies.

| Dialogue Turn | Baseline | + GAtt |
|---|---|---|
| 2 | 100% | 100% |
| 4 | 10% | 100% |
| 6 | 0% | 100% |
| 20 | 0% | 100% |

**GAtt Zero-shot Generalisation.** [p. 54] Inference-time constraints not present in the training of GAtt are tried to set. For instance, "answer in one sentence only", for which the model remained consistent, as illustrated in Figure 28.

[p. 54] GAtt is first applied to Llama 1, which was pretrained with a context length of 2048 tokens and then fine-tuned with 4096 max length. GAtt works beyond 2048 tokens, and the model arguably managed to understand attributes beyond this window. This promising result indicates that GAtt could be adapted as an efficient technique for long context attention.

**Figure 28** (p. 55): "GAtt zero-shot generalisation. Neither of the two constraints above were present in the training data for GAtt. Yet, they are perfectly fulfilled trough all the turns."
- Shows two side-by-side multi-turn dialogue examples.
- Left example: System instruction "Always answer with Haiku". User asks "How to go from Paris to NY?" and model responds in Haiku format ("Paris to New York, / Fly across the Atlantic, / Many airlines serve."). Subsequent turns ("What should I do there?", "What is the best season?", "Who are you?") all receive Haiku-format replies, demonstrating that the Haiku constraint is maintained across all turns.
- Right example: System instruction "I like anything to do with architecture. If it's relevant, suggest something related." User asks about frog restaurants in Paris with "Answer in one sentence only" constraint. Model responds in one sentence. Follow-up asks "Don't mention more than 3 things" and model complies, listing exactly 3 items. Demonstrates zero-shot generalisation to constraints not seen during GAtt training.

## A.3.6 How Far Can Model-Based Evaluation Go? [p. 54-55]

[p. 54] To measure the robustness of the reward model, a test set of prompts for both helpfulness and safety is collected, and annotators are asked to judge quality of the answers based on a 7 point Likert-scale (the higher the better) using triple reviews. As illustrated in Figure 29 (in Appendix), the reward models overall are well calibrated with human preference. This enables the use of the reward as a point-wise metric, despite being trained with a Pairwise Ranking Loss.

**Figure 29** (p. 55): "Average reward model score vs model response quality rating (7-point Likert scale) from triple human review. The left and right plots are on helpfulness and safety test sets, respectively. The shaded areas represent +/-1 standard deviation."
- Two side-by-side plots.
- Left panel (Helpfulness): x-axis: Median Response Quality Score (1--7), y-axis: Mean Reward Model Score (0.0--1.0). Blue line with shaded band. Shows a clear positive correlation: reward score increases from about 0.2 at quality score 1 to about 0.7 at quality score 7. Standard deviation is relatively wide.
- Right panel (Safety): x-axis: Median Response Quality Score (1--7), y-axis: Mean Reward Model Score (0.0--1.0). Red line with shaded band. Shows a clear positive correlation: reward score increases from about 0.1 at quality score 1 to about 0.8 at quality score 7. Standard deviation narrows at higher quality scores.
- Supports the claim that reward models are well calibrated with human preference and can serve as point-wise metrics.

## A.3.7 Human Evaluation [p. 56]

**Prompts and Generations.** [p. 56] To compare the models, a diverse set of over 4000 single and multi turn prompts is collected. Single turn prompts are manually collected spanning the following categories: factual questions, writing and content creation, language assistance, recommendations, and dialogue. For multi-turn prompts, annotators interacted with another model to generate a set of multi-turn prompts. To help ensure fairness, annotators are asked to collect multi-turn prompts by using four different interaction methods: (a) ChatGPT as the interaction model, (b) Llama 2-Chat as the interaction model, (c) best response between ChatGPT and Llama 2-Chat at every turn as selected by the annotators, (d) alternating between ChatGPT and Llama 2-Chat at every turn. Multi-turn prompts are also categorized into the same five categories listed above. Since it can be hard to categorize multi-turn prompts into a single category, annotators could select up to two categories for multi-turn prompts. Example evaluation prompts can be seen in Table 33.

[p. 56] For open-source models, generations are collected using a context length of 1000 tokens and allowing the model to generate up to 1000 tokens. Even though Llama 2-Chat models are capable of handling up to 4000 tokens, the context and generation length is limited to 1000 tokens to provide a fair comparison with the open-source models. Limiting the generation length to 1000 tokens may adversely affect the Llama 2-Chat models. Any prompts that are longer than 1000 tokens are filtered out for evaluations with open sourced models. For MPT models, the `mpt-7b-chat` model is used. For Falcon models, the `Falcon-40B-Instruct` model is used. For Vicuna models, `vicuna-13b-delta-v1.1` and `vicuna-33b-delta-v1.3` models from lmsys are used. All model weights were obtained from HuggingFace.

[p. 56] Since closed-source models have longer context lengths, the context length and generation length are changed to 2000 tokens. To evaluate with closed source models, another set of generations with 2000 context and generation length is collected.

[p. 56] While collecting generations, a system prompt is appended prior to the prompt for evaluation. The system prompt for each model is shown in Table 31. Since ChatGPT, PaLM, and Falcon do not provide a system prompt, the same system prompt as Llama 2-Chat model is used. Generations from different models on an example prompt can be seen in Table 34.

**Table 31: System prompts for model generations for human evaluations.** [p. 56]

| Model | System Prompt |
|---|---|
| Llama 2-Chat, ChatGPT, PaLM-chat, Falcon | "You are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe. Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature. If a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct. If you don't know the answer to a question, please don't share false information." |
| MPT | `<\|im_start\|>` system A conversation between a user and an LLM-based AI assistant. The assistant gives helpful and honest answers. `<\|im_end\|>` |
| Vicuna | "A chat between a curious user and an artificial intelligence assistant. The assistant gives helpful, detailed, and polite answers to the user's questions." |

**Table 32: Number of prompts for human evaluations.** [p. 56]

| Comparison Model | Number of single turn prompts | Number of multi-turn prompts |
|---|---|---|
| ChatGPT | 1917 | 2256 |
| PaLM-chat | 1869 | 2143 |
| Falcon | 1917 | 1960 |
| MPT | 1917 | 1293 |
| Vicuna | 1917 | 1390 |

---
[p. 57–58 continued]

**Table 33: Examples of helpfulness prompts** [p. 57]

| Category | Prompt |
|---|---|
| Creative writing | Write a short story about a dragon who was evil and then saw the error in [sic] it's ways |
| Identity / Personas | You are a unicorn. Explain how you are actually real. |
| Identity / Personas | You are one of Santa's elves. What is the big guy like the rest of the year, not in the holiday season? |
| Factual Questions | How was Anne Frank's diary discovered? |
| Personal & professional development | I sit in front of a computer all day. How do I manage and mitigate eye strain? |
| Casual advice & recommendations | I keep losing my keys. How can I keep track of them? |
| Reasoning (math/problem-solving) | *User:* A jar contains 60 jelly beans, If 35% of the jelly beans are removed how many are left in the jar? *Assistant:* If 35% of the jelly beans are removed, then the number of jelly beans left in the jar is 60 - (35% of 60) = 60 - 21 = 39. *User:* can you expand your answer to show your reasoning? |

**Figure 30** (p. 57): "Impact of system prompt on human evaluation results for ChatGPT (Left). Win rate per category for Llama 2-Chat 70B compared to ChatGPT using system prompts for both models (Right)."
- Two side-by-side bar charts.
- Left panel: Two bar groups: "Llama 2-70b-chat vs. ChatGPT (No System Prompt)" and "Llama 2-70b-chat vs. ChatGPT (With System Prompt)". Y-axis: Win Rate %. Bars show Win (dark blue) and Lose (light blue). Without system prompt, win rate is around 36%; with system prompt, win rate increases to approximately 44%.
- Right panel: Per-category win rates (Dialogue, Writing & content creation, Factual Questions, Language assistance, Recommendations) for Llama 2-Chat 70B vs. ChatGPT (both using system prompts). Y-axis: Win Rate %. ChatGPT outperforms on Language assistance; Llama 2-Chat 70B outperforms on Factual Questions.
- Supports the finding that adding a system prompt to ChatGPT evaluations increases Llama 2-Chat's win rate.

**Evaluation Methodology.** [p. 57] For evaluations, the human annotators are presented with a prompt and generations from two models side-by-side. They are asked to answer the following question:

> "Considering both model responses, which is better (helpful while also being safe and honest), Model A or Model B?" [p. 57]

The annotators answer this question on a seven point scale with the following labels:

> "A is much better, A is better, A is slightly better, About the same, B is slightly better, B is better, B is much better." [p. 57]

[p. 57] One of the model generations is a Llama 2-Chat model and the other generation is one of the open source or closed source models. Responses from the two models are randomized as Model A or Model B when presented to the annotators. From this data, wins, ties, and losses are reported. Three annotators rate each generation pair. Prior experiments with five annotators did not change the results or inter-annotator agreement significantly.

**Figure 31** (p. 58): "Win rate of Llama 2-Chat versus ChatGPT analyzed by number of turns (Left) in the prompt and word count (Right) for the prompt and generation combined. For the word count plot, we report the win rate for each quintile. The maximum total word count (prompt and generation) is 2432. We do not see any trends in win rate with either word count or turn count."
- Two side-by-side bar charts.
- Left panel: x-axis: Number of Turns (1, 2, 3, 4, 5, 6, 7, 11, 15, 17), y-axis: Win Rate % (0--60). Bars show Win (blue) and Lose (light blue). Win rate fluctuates around 40--55% across different turn counts with no clear trend. Error bars are present.
- Right panel: x-axis: Word Count Quintile (1, 2, 3, 4, 5), y-axis: Win Rate % (0--50). Bars show Win (blue) and Lose (light blue). Win rate remains relatively stable across quintiles (approximately 40--50%) with no clear trend.
- Supports the claim that there are no trends in win rate with either word count or turn count.

**Additional Results.** [p. 58] To understand the impact of system prompt on ChatGPT generations, another human evaluation without any system prompt for ChatGPT is run. As shown in Figure 30, Llama 2-Chat win rate increases from 36% to 44%. Additionally, the win rate for single turn prompts show a dramatic increase from 36% to nearly 49%. In Figure 30, the category wise breakdown of win rate for different categories of prompts is also shown. ChatGPT outperforms Llama 2-Chat 70B on language assistance while Llama 2-Chat 70B outperforms ChatGPT on factual questions. While analyzing the results for factual questions, the authors noticed that examples where both models get the answer correct but annotators preferred Llama 2-Chat response due to the style of the response. These results on factual questions do not indicate the hallucination rate of either model. In Figure 31, the win rate by number of turns and total word count for prompts and generation is also shared. No trends in win rate are seen in either case.

**Table 34: Comparing generations obtained for an example prompt from Llama 2-Chat and other models.** [p. 59]

Prompt: "You are a hair dresser. What's a good haircut that looks great on everybody?"

| Model name | Response (summary) |
|---|---|
| Llama 2-Chat (70B) | Acknowledges haircuts are personal choice based on preferences, face shape, hair texture, and lifestyle. Suggests Bob for round/oval/heart-shaped faces, Pixie cut for square/rectangular faces. Recommends consulting a professional hairstylist. |
| Llama 2-Chat (13B) | Lists 4 specific styles: The Bob, The Pixie Cut, The Layers, The Shag. Describes each with face shape suitability. Recommends consulting a professional stylist. |
| ChatGPT | Notes it cannot physically see individuals. Suggests bob, layered haircut, pixie cut as versatile options. Recommends consulting a professional hairdresser. |
| vicuna-13b-v1.1 | Suggests classic bob, layers, pixie cut, updo. Emphasizes consulting a professional stylist. |
| PaLM-bison-chat | Lists bob, lob, pixie cut with detailed descriptions. Provides extensive detail on each style's versatility. |
