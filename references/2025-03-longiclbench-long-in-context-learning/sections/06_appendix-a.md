# Appendix [p. 16]

## A.1 Additional Datasets [p. 16]

A few additional datasets are listed as follows:

### GoEmotions

**GoEmotions** (Demszky et al., 2020) is the largest manually annotated dataset of 58k English comments from Reddit, which is labeled into 27 emotion categories or Neutral. There are 27 types of emotion types and drop the rare ones with few examples. Each selected example contains 28 tokens on average [p. 16].

### Few-NERD

**Few-NERD** (Ding et al., 2021) is a large-scale human-annotated name entity recognition dataset with a hierarchy of 8 coarse-grained and 66 fine-grained entity types. Each of the instances is a paragraph with approximately 61 tokens on average and contains one or multiple entity names as the ground truth answer. There are 66 types of entities in the collection [p. 16].

---
[p. 17 continued]

**Table 7: GoEmotion Result** [p. 17]

| Model | Param | Support | 1R | 2R | 3R | 4R | 5R |
|-------|-------|---------|-----|-----|-----|-----|-----|
| **Context Tokens** | | | **0.8K** | **1.6K** | **2.4K** | **3.2K** | **4K** |
| Gemma-7B-base | 7B | 8K | 0 | 0 | 0 | 0 | 0 |
| LLaMA-2-7B-32K | 7B | 32K | 0 | 0 | 0 | 0.2 | 0.2 |
| ChatGLM3-6B-32K | 6B | 32K | 22.0 | 17.0 | 15.0 | 12.6 | 10.6 |
| Qwen-1.5-7B-base | 7B | 32K | 14.8 | 18.2 | 18.6 | 19.0 | 14.2 |
| Mistral-7B-v0.2-base | 7B | 32K | 2.6 | 11.4 | 7.4 | 11.6 | 12.4 |
| LLaMA-2-7B-LongLora | 7B | 100K | 0 | 0 | 0 | 0 | 0 |
| Yi-6B-200K | 6B | 200K | 0 | 0 | 0.8 | 4.0 | 4.0 |
| InternLM2-7B-base | 7B | 200K | 0 | 0 | 0 | 0 | 0 |
| Long-LLaMA-code-7B | 7B | 256K | 0 | 0 | 0 | 0.2 | 0.4 |
| RWKV-5-World | 7B | 4K | 8.8 | 7.4 | 4.6 | 5.2 | 4.0 |
| Mamba-2.8B | 2.8B | 2K | 0 | 0 | 0 | 0 | 0 |
| GPT4-turbo | N/A | 128K | 36.5 | 34.4 | 35.0 | 33.3 | 32.0 |
| GPT4o | N/A | 128K | 23.0 | 23.8 | 21.2 | 21.2 | 22.2 |
| Claude3-Opus | N/A | 200K | 25.8 | 7.4 | 17.0 | 12.6 | 19.6 |
| Gemini-1.5-Pro | N/A | 10M | 19.0 | 10.4 | 9.2 | 10.6 | 9.4 |
| **SoTA (BERT)** | **N/A** | **-** | | | **58.9** | | |

**Table 8: Few-NERD Result** [p. 17]

| Model | Param | Support | 1R | 2R | 3R | 4R | 5R |
|-------|-------|---------|-----|-----|-----|-----|-----|
| **Context Tokens** | | | **5K** | **9K** | **14K** | **19K** | **24K** |
| Gemma-7B-base | 7B | 8k | 44.0 | 44.2 | 0 | 0 | 0 |
| LLaMA-2-7B-32K | 7B | 32k | 36.9 | 40.8 | 41.1 | 41.6 | 41.3 |
| ChatGLM3-6B-32K | 6B | 32k | 24.1 | 9.3 | 23.6 | 10.4 | 1.1 |
| Qwen-1.5-7B-base | 7B | 32k | 40.0 | 46.4 | 47.6 | 47.3 | 47.8 |
| Mistral-7B-v0.2-base | 7B | 32K | 42.2 | 47.4 | 48.9 | 50.0 | 50.0 |
| LLaMA-2-7B-LongLora | 7B | 100K | 0 | 0 | 0 | 0 | 0 |
| Yi-6B-200K | 6B | 200k | 34.3 | 40.2 | 44.8 | 42.3 | 43.2 |
| InternLM2-7B-base | 7B | 200k | 43.6 | 46.2 | 46.5 | 47.8 | 48.3 |
| Long-LLaMA-code-7B | 7B | 256K | 22.3 | 25.5 | 26.5 | 29.4 | 27.0 |
| RWKV-5-World | 7B | 1k | 13.9 | 0 | 0 | 0.7 | 9.9 |
| Mamba-2.8B | 2.8B | 2k | 0 | 0 | 0 | 0 | 0 |
| GPT4-turbo | N/A | 128k | 53.4 | 55.3 | 56.2 | 55.6 | 56.8 |
| GPT4o | N/A | 128k | 46.7 | 41.4 | 42.8 | 39.0 | 44.4 |
| Claude3-Opus | N/A | 200k | 53.5 | 51.3 | 51.2 | 52.4 | 52.5 |
| Gemini-1.5-Pro | N/A | 10M | 55.4 | 47.8 | 49.5 | 41.4 | 42.4 |
| **SoTA (PL-Marker)** | **N/A** | **-** | | | **70.9** | | |

## A.2 Prompting Template [p. 17]

The prompting template for each of the datasets is presented at Table 9 [p. 17].

---
[p. 18 continued]

**Table 9: The data prompt format of each dataset** [p. 18]

Each dataset has a unique prompt format to effectively utilize the context and format of its respective data to get the best output response.

| Dataset | Prompt |
|---------|--------|
| GoEmotion | Given a comment, please predict the emotion category of this comment. The prediction answer must come from the demonstration examples with the exact format. The examples are as follows:<br>{comment: '...comment...'<br>emotion category: '...emotion...'<br>} × repeat n times |
| BANKING77 | Given a customer service query, please predict the intent of the query. The predicted answer must come from the demonstration examples with the exact format. The examples are as follows:<br>{service query: '...service...'<br>intent category: '...intent...'<br>} × repeat n times |
| TacRED | Given a sentence and a pair of subject and object entities within the sentence, please predict the relation between the given entities. The examples are as follows:<br>{sentence: '...sentence...<br>the subject is '...subject...'<br>the object is '...object...'<br>the relation between the two entities is: '...relation...'<br>} × repeat n times |
| Few-NERD | Given the sentence, please find the name entities in the sentence and their corresponding entity types in the strict format of the given examples as following (Entity: EntityType):<br>{'...entity...': '...entity type...'<br>} × repeat n times |
| DialoRE | Given the dialogue, please find the name pair entities in the dialogue and their corresponding relation types in the strict format of given examples as following (note that the number of entities has to strictly have the same value as the number of respective relation):<br>{Dialogue:<br>"...dialogue..."<br>The list of entity pairs are '...(subject1, object1), (subject2, object2), etc...<br>The "...number of pairs..." respective relations between each entity pair are: "...relation, relation2, etc...<br>} × repeat n times |
| Discovery | Given two sentence1 and sentence2, please predict the conjunction word between the two sentences. The predicted answer must come from the demonstration examples with the exact format. The examples are as follows:<br>{'...sentence1...' ( ) '...sentence2...'<br>the conjunction word in ( ) is '...conjunction...'<br>} × repeat n times |

## A.3 Additional Distribution Analysis [p. 17]

To facilitate a clear comparison between random and grouped distributions, we organize instances of the same class to be adjacent within the demonstration prompts. The impact of this reorganization on model performance, both pre and post-grouping, is presented in Table 10 [p. 17].

---
[p. 19 continued]

**Table 10: Exploratory Result on TacRED 3 Round** [p. 19]

**Grouped** means forcing the same-typed demonstration examples near by each other instead of randomly distributing in the prompt.

| Model | Param | Support | Scatter | Grouped | Δ |
|-------|-------|---------|---------|---------|---|
| **Context Tokens** | | | | **10K** | |
| Gemma-7B-base | 7B | 8K | 0 | 0 | 0 |
| LLaMA-2-7B-32K | 7B | 32K | 0.4 | 3.0 | +2.6 |
| ChatGLM3-6B-32K | 6B | 32K | 38.9 | 35.6 | -3.3 |
| Qwen-1.5-7B-base | 7B | 32K | 45.2 | 33.0 | -12.2 |
| Mistral-7B-v0.2-base | 7B | 32K | 51.6 | 5.1 | -46.5 |
| LLaMA-2-7B-LongLora | 7B | 100K | 0 | 0 | 0 |
| Yi-6B-200K | 6B | 200K | 8.0 | 0 | -8 |
| InternLM2-7B-base | 7B | 200K | 15.5 | 4.8 | -9.7 |
| Long-LLaMA-code-7B | 7B | 256K | 4.1 | 0 | -4.1 |
| RWKV-5-World | 7B | 4K | 1.0 | 3.6 | +2.6 |
| Mamba-2.8B | 2.8B | 2K | 0 | 0 | 0 |
| GPT4-turbo | N/A | 128K | 79.5 | 59.2 | -20.3 |
| Gemini-1.5-Pro | N/A | 10M | 79.6 | 57.3 | -22.3 |

**Figure 5** (p. 19): "Visualization of accuracy for every class when instances from the same class are scattered V.S. grouped in the demonstration prompt."

Description: A 2×3 grid of scatter plots comparing class-wise accuracy under two distribution strategies
- **Top row (Scatter):** Three scatter plots showing Mistral-7B-v0.2-base, Qwen-1.5-7B-base, and LLaMA-2-7B-32K performance when instances are randomly scattered
- **Bottom row (Grouped):** The same three models with instances grouped by class
- **Axes:** Instance Position (x-axis, 0-125) vs. Class Accuracy % (y-axis, 0-100)
- **Notable patterns:**
  - In scattered distribution, points are relatively evenly distributed across instance positions with accuracy varying 0-100% across classes
  - In grouped distribution, points cluster at specific instance positions (where each class's examples are grouped), showing much lower and more concentrated accuracy patterns
  - All three models show substantial performance degradation when examples are grouped vs. scattered
- **Supports claim:** This visualization demonstrates that most models perform significantly worse when demonstration examples from the same class are positioned adjacently, compared to random scattering, as quantified in Table 10 [p. 19]

**Figure 6** (p. 20): "Visualization of accuracy for every class when instances from the same class are scattered V.S. grouped in the demonstration prompt."

Description: A 2x3 grid of scatter plots comparing class-wise accuracy under two distribution strategies for three additional models
- **Top row (Scatter):** Three scatter plots showing Long-LLaMA-code-7B, Yi-6B-200K, and Gemini-1.5-Pro performance when instances are randomly scattered
- **Bottom row (Grouped):** The same three models with instances grouped by class
- **Axes:** Instance Position (x-axis, 0-125) vs. Class Accuracy % (y-axis, 0-100)
- **Notable patterns:**
  - Long-LLaMA-code-7B: Very low accuracy in both scattered and grouped, with most points near 0%
  - Yi-6B-200K: Sparse high-accuracy points in scattered; grouped shows near-zero for most classes
  - Gemini-1.5-Pro Scatter: Many points distributed across 20-100% accuracy range, showing broad but uneven performance
  - Gemini-1.5-Pro Grouped: Points cluster at specific positions with generally lower accuracy, showing clear step-pattern corresponding to grouped class blocks
- **Supports claim:** Even Gemini-1.5-Pro, which shows the strongest performance among evaluated models, suffers substantial performance degradation when demonstration examples are grouped rather than scattered [p. 20]

## A.4 Data Accessibility [p. 18]

Our LongICLBench is set under MIT license, thus permission is granted, free of charge, to any person obtaining a copy of this dataset and associated documentation files. The datasets are curated under the rules guaranteed by the original dataset. There is no personally identifiable or offensive content in the dataset [p. 18].
