# Long In-context Evaluation [p. 5-6]

## 3.1 Long In-context Benchmark [p. 5]

To support the evaluation of long in-context learning on extreme-label classification tasks in different domains and varied difficulty levels, we collect six datasets containing context length from short to long. In order to balance the sequence token length within each dataset and the goal of evaluation for long in-context learning, we keep a subset of the classes among all of classes to make evaluations around 1 round, 2 rounds, 3 rounds, 4 rounds, and 5 rounds correspondingly, where each round represent a complete set of examples containing all unique chosen labels [p. 5].

We sample the number of instances from each of the classes evenly to reduce the bias resulting from the label distribution. The statistics of the datasets are described in detail in Table 1.

**Table 1** (p. 5): "Statistics of the collected sub-dataset in LongICLBench. We evaluate from 1-shot/label to 5-shot/label, which results in the shown #total token range."

| Dataset | Task Type | # Classes | # Tokens/Shot | # Total Tokens |
|---------|-----------|-----------|---------------|----------------|
| GoEmotion | Emotion Classification | 28 | 28 | [1K, 4K] |
| BANKING77 | Intent Classification | 77 | 28 | [2K, 11K] |
| TacRED | Relation Extraction | 41 | 80 | [4K, 18K] |
| Few-NERD | Entity Recognition | 66 | 61 | [5K, 23K] |
| DialogRE | Relation Extraction | 36 | 226 | [8K, 32K] |
| Discovery | Discourse Marker Classification | 174 | 61 | [10K, 50K] |

### GoEmotions

GoEmotions (Demszky et al., 2020) is the largest manually annotated dataset of 58k English comments from Reddit, which is labeled into 27 emotion categories or Neutral. Each selected example contains 28 tokens on average [p. 5].

### BANKING77

BANKING77 (Casanueva et al., 2020) is a banking-domain intent detection dataset comprising 13,083 annotated examples over 77 intents. We keep all of the types of intents, and each of the instances contains around 28 tokens.

### TacRED

TacRED (Zhang et al., 2017) is a large-scale relation extraction dataset with 106,264 examples built over news and web text. Only one relation is labeled for each of the sentences in the dataset. It covers 41 relation types in total, with an average length of 80 tokens for each example.

### Few-NERD

Few-NERD (Ding et al., 2021) is a human-annotated name entity recognition dataset with a hierarchy of 8 coarse-grained and 66 fine-grained entity types. Each of the instances is a paragraph with about 61 tokens on average and contains one or multiple entity names as the ground truth answer [p. 5].

### DialogRE

DialogRE (Yu et al., 2020) is a human-annotated dialogue-based relation extraction dataset from an American television comedy, Friends. It identifies the existing between an argument pair in a dialogue. Each example contains an average of 226 tokens.

### Discovery

Discovery (Sileo et al., 2019) automatically discovers sentence pairs with relevant discourse markers and forms a dataset containing 174 discourse markers with at least 10K examples each. Each example contains around 61 tokens. This dataset is the most difficult task with fine-grained labels.

## 3.2 Model and Experimental Setup [p. 5-6]

In the exploration of in-context learning for extreme-label classification, we conduct a comprehensive evaluation of popular open-source long-context language models of size around 7B parameters. We also include SoTA models like Gemini-1.5-Pro, Claude3-Opus, and GPT-4-turbo [p. 5-6].

Table 2 provides an overview of the models investigated, highlighting the innovations in their architecture specifically for dealing with long context. We can observe that there are multiple strategies adopted to extend the context window. Some of the models support the training context window size while some models support length extrapolation. RWKV (Peng et al., 2023a) and Mamba (Gu & Dao, 2023) are the two new RNN-like architectures to decrease attention complexity, which would allow the model to easily extrapolate to much longer inputs with linear time/memory complexity [p. 6].

**Table 2** (p. 6): "The overview of the evaluated models. We utilize base models before instruction-tuning except API-based models. LF means fine-tuning the model on longer-context corpus after pre-training."

| Model | Size | Initialization | Strategy | Train | Support |
|-------|------|----------------|----------|-------|---------|
| Gemini-7B-base | 7B | Gemma | RoPE + LF | 8K | 8K |
| LLaMA-2-7B-32K | 7B | LLaMA-2 | Position Interpolation | 32K | 32K |
| ChatGLM3-6B-32K | 6B | ChatGLM | Position Encoding Scheme | 32K | 32K |
| Qwen-1.5-7B-base | 7B | Qwen | NTK-Aware Interpolation | 32K | 32K |
| Mistral-7B-v0.2-base | 7B | Mistral | LF | 32K | 32K |
| LLaMA-2-7B-LongLora | 7B | LLaMA-2 | Shifted Short Attention | 100K | 100K |
| Yi-6B-200K | 6B | Yi | Position Interpolation +LF | 200K | 200K |
| InternLM2-7B-base | 7B | InternLM | Dynamic NTK | 32K | 200K |
| Long-LLaMA-code-7B | 7B | LLaMA-2 | Focused Transformer | 8K | 256K |
| RWKV-5-World | 3B | RWKV | Attention-free Model | 4K | ∞ |
| Mamba-2.8B | 2.8B | Mamba | State Space Model | 2K | ∞ |
| GPT4-turbo | - | GPT-4 | - | - | 128K |
| GPT4o | - | GPT-4 | - | - | 128K |
| Claude3-Opus | - | Claude3 | - | - | 200K |
| Gemini-1.5-Pro | - | Gemini | - | - | 10M |

We construct a prompt following the template as shown in A.2 for each of the datasets. To fairly evaluate the open-source and API-based models with a series of input lengths, we sample the same example set for all the models with labels distributed the same to ensure an unbiased distribution for the in-context demonstration [p. 6].

For instance, an input of one round will include one set of examples traversing all the types, and 5 rounds will contain instances from each of the labels 5 times. For testing, we sample 500 examples from the test set of each dataset, simultaneously ensuring an even distribution in terms of the type of labels. All the open-source models are loaded from the weights in HuggingFace¹ and inferred on eight NVIDIA RTX A6000 GPUs, while the API-based models are based on the official documentations².

¹https://huggingface.co/
²https://platform.openai.com/docs/guides/text-generation/chat-completions-api, https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/overview

## 3.3 Experiment Result [p. 6]

The main evaluation results are demonstrated in Table 3, Table 4, Table 5, Table 6 and subsection A.1. For the error recognition and relationship extraction dataset, we use the F1 score as the evaluation metric, and Accuracy is utilized for the other datasets [p. 6].

From the presented results, generally, we can find that models of Transformer-based architecture perform consistently better than the RNN-based ones in all the evaluated datasets. However, both of them are still falling behind the powerful API-based models.

For a relatively simple task like BANKING77, whose context length from 1 round to 5 rounds is 2K to 14 K, most of the models can benefit from the extensive context with more demonstrations. As shown in Figure 1 and Table 3, from 2K to 4K, there is either a huge increase nearly doubling the accuracy, or a complete failure for most of the open-source models. After 3 rounds, limited performance gain can be achieved by adding more examples.

When it comes to more complicated tasks like TacRED and DialogueRE in Table 4 and Table 5, which are more urgently requiring the capability of long-context comprehension, the overall performance of all the few-shot models drops compared to 1-shot. As shown in the middle plot of Figure 1, only GPT4-turbo and GPT4o can consistently benefit from more demonstrations, all of the other models reach their peak at the middle with context length around 18K to 25K.

For the most challenging Discovery dataset, which has an extremely large label space including 174 classes, one round of traversing for all the label possibilities has already made up a context length of 10K. In this [p. 6]

---
[p. 6-7 continued]

extreme case, all of the models except Gemini-1.5-Pro, fail to tell the difference among the fine-grained types including GPT4-turbo, leading to a score of 0. The results across different datasets reveal the models' capability to understand different types of tasks. Our initial hypothesis suggests that the strongest LLMs like GPT-4-turbo are capped at a certain complexity level between DialogRE and Discovery [p. 7].

Another interesting observation we have is that some LLMs' performance on the extreme-label ICL seems highly predictable. According to the left sub-graph of Figure 1, the performance of Qwen and Mistral is almost linear w.r.t the demonstration length. This reveals that there might be an underlying mathematical relation between performance and the task complexity for ICL [p. 7].

**Table 3** (p. 7): "BANKING77 result with respect to increasing context length. 1R represents one round of traversing all the instances with a unique label."

| Model | Param | Support | 1R | 2R | 3R | 4R | 5R |
|-------|-------|---------|----|----|----|----|-----|
| **Context Tokens** | | | **2K** | **4K** | **7K** | **9K** | **14K** |
| Gemma-7B-base | 7B | 8K | 0 | 0 | 0 | 0 | 0 |
| LLaMA-2-7B-32K | 7B | 32K | 30.2 | 70.4 | 72.0 | 75.6 | 77.2 |
| ChatGLM3-6B-32K | 6B | 32K | 16.0 | 23.2 | 22.4 | 22.8 | 8.8 |
| Qwen-1.5-7B-base | 7B | 32K | 21.6 | 52.8 | 61.4 | 66.0 | 67.8 |
| Mistral-7B-v0.2-base | 7B | 32K | 29.8 | 43.6 | 66.4 | 67.8 | 64.0 |
| LLaMA-2-7B-LongLora | 7B | 100K | 0 | 0 | 0 | 0 | 0 |
| Yi-6B-200K | 6B | 200K | 25.8 | 0 | 0 | 0 | 1.2 |
| InternLM2-7B-base | 7B | 200K | 5.6 | 0 | 0 | 0 | 0 |
| Long-LLaMA-code-7B | 7B | 256K | 3.0 | 19.4 | 28.0 | 31.6 | 32.6 |
| RWKV-5-World | 7B | 4K | 8.6 | 21.2 | 0.4 | 0 | 0 |
| Mamba-2.8B | 2.8B | 2K | 0 | 0 | 0 | 0 | 0 |
| GPT4-turbo | N/A | 128K | 73.5 | 80.5 | 82.0 | 83.5 | 84.4 |
| GPT4o | N/A | 128K | 80.8 | 79.8 | 81.2 | 71.2 | 71.4 |
| Claude3-Opus | N/A | 200K | 60.0 | 62.6 | 62.2 | 43.8 | 26.0 |
| Gemini-1.5-Pro | N/A | 10M | 28.8 | 79.4 | 82.2 | 81.8 | 70.4 |
| SoTA (RoBERTA + ICDA) | N/A | - | | | **94.4** | | |

**Table 4** (p. 7): "TacRED result with respect to increasing context length."

| Model | Param | Support | 1R | 2R | 3R | 4R | 5R |
|-------|-------|---------|----|----|----|----|-----|
| **Context Tokens** | | | **4K** | **7K** | **10K** | **14K** | **18K** |
| Gemma-7B-base | 7B | 8K | 0.4 | 0.4 | 0 | 0 | 0 |
| LLaMA-2-7B-32K | 7B | 32K | 0 | 0.4 | 0.4 | 0.8 | 0.4 |
| ChatGLM3-6B-32K | 6B | 32K | 29.7 | 36.1 | 38.9 | 40.1 | 25.2 |
| Qwen-1.5-7B-base | 7B | 32K | 38.7 | 47.3 | 45.2 | 43.6 | 40.6 |
| Mistral-7B-v0.2-base | 7B | 32K | 53.3 | 53.1 | 51.6 | 48.0 | 42.3 |
| LLaMA-2-7B-LongLora | 7B | 100K | 0 | 0 | 0 | 0 | 0 |
| Yi-6B-200K | 6B | 200K | 5.6 | 1.9 | 8.0 | 9.5 | 2.0 |
| InternLM2-7B-base | 7B | 200K | 29.6 | 27.2 | 15.5 | 10.7 | 8.0 |
| Long-LLaMA-code-7B | 7B | 256K | 3.8 | 7.1 | 4.1 | 6.6 | 4.9 |
| RWKV-5-World | 7B | 1K | 2.3 | 2.6 | 1.0 | 0 | 1.2 |
| Mamba-2.8B | 2.8B | 2K | 0 | 0 | 0 | 0 | 0 |
| GPT4-turbo | N/A | 128K | 74.4 | 76.5 | 79.5 | 80.4 | 84.2 |
| GPT4o | N/A | 128K | 71.1 | 75.5 | 73.6 | 73.2 | 72.3 |
| Claude3-Opus | N/A | 200K | 68.7 | 74.1 | 35.4 | 43.4 | 44.3 |
| Gemini-1.5-Pro | N/A | 10M | 72.6 | 81.4 | 79.6 | 81.4 | 82.3 |
| SoTA (DeepStruct) | N/A | - | | | 76.8 | | |
# Long In-context Evaluation (continued) [p. 8]

**Table 5** (p. 8): "DialogRE result with respect to increasing context length."

| Model | Param | Support | 1R | 2R | 3R | 4R | 5R |
|-------|-------|---------|----|----|----|----|-----|
| **Context Tokens** | | | **8K** | **13K** | **19K** | **25K** | **32K** |
| Gemma-7B-base | 7B | 8K | 14.7 | 0 | 0 | 0 | 0 |
| LLaMA-2-7B-32K | 7B | 32K | 6.6 | 13.5 | 6.0 | 5.4 | 5.5 |
| ChatGLM3-6B-32K | 6B | 32K | 0.5 | 1.1 | 2.5 | 1.8 | 7.6 |
| Qwen-1.5-7B-base | 7B | 32K | 14.0 | 17.8 | 15.3 | 16.2 | 13.1 |
| Mistral-7B-v0.2-base | 7B | 32K | 24.0 | 23.0 | 23.2 | 22.0 | 21.1 |
| LLaMA-2-7B-LongLora | 7B | 100K | 0 | 0 | 0 | 0 | 0 |
| Yi-6B-200K | 6B | 200K | 0 | 0 | 0.4 | 0.4 | 0 |
| InternLM2-7B-base | 7B | 200K | 12.0 | 13.2 | 5.8 | 1.8 | 0.7 |
| Long-LLaMA-code-7B | 7B | 256K | 2.7 | 3.0 | 2.6 | 5.2 | 1.7 |
| RWKV-5-World | 7B | 4K | 0 | 0 | 0 | 0 | 0 |
| Mamba-2.8B | 2.8B | 2K | 0 | 0 | 0 | 0 | 0 |
| GPT4-turbo | N/A | 128K | 42.9 | 47.8 | 52.0 | 55.9 | 57.7 |
| GPT4o | N/A | 128K | 40.6 | 41.5 | 41.0 | 47.3 | 45.3 |
| Claude3-Opus | N/A | 200K | 16.8 | 30.3 | 15.3 | 0.8 | 0 |
| Gemini-1.5-Pro | N/A | 10M | 29.6 | 37.8 | 31.2 | 32.4 | 34.3 |
| SoTA (HiDialog) | N/A | - | | | 77.1 | | |

**Table 6** (p. 8): "Discovery result with respect to increasing context length."

| Model | Param | Support | 1R | 2R | 3R | 4R | 5R |
|-------|-------|---------|----|----|----|----|-----|
| **Context Tokens** | | | **10K** | **20K** | **30K** | **40K** | **50K** |
| Gemma-7B-base | 7B | 8K | 0 | 0 | 0 | 0 | 0 |
| LLaMA-2-7B-32K | 7B | 32K | 0 | 0 | 0 | 0 | X |
| ChatGLM3-6B-32K | 6B | 32K | 0 | 1.0 | 0 | X | X |
| Qwen-1.5-7B-base | 7B | 32K | 0 | 0 | 0 | 0 | 0 |
| Mistral-7B-v0.2-base | 7B | 32K | 0 | 0 | 0 | 0 | 0 |
| LLaMA-2-7B-LongLora | 7B | 100K | 0 | 0 | 0 | 0 | 0 |
| Yi-6B-200K | 6B | 200K | 0 | 0 | 0 | 0 | 0 |
| InternLM2-7B-base | 7B | 200K | 0 | 0 | 0 | 0 | 0 |
| Long-LLaMA-code-7B | 7B | 256K | 0 | 0 | 0 | 0 | 0 |
| RWKV-5-World | 7B | 4K | 0 | 0.2 | 0 | 0 | 0 |
| Mamba-2.8B | 2.8B | 2K | 0 | 0 | 0 | 0 | 0 |
| GPT4-turbo | N/A | 128K | 1.5 | 0.5 | 0.5 | 0.5 | 0.5 |
| GPT4o | N/A | 128K | 2.8 | 0.8 | 0.8 | 0.6 | 0.4 |
| Claude3-Opus | N/A | 200K | 1.2 | 0.6 | 0.6 | 0.6 | 0.2 |
| Gemini-1.5-Pro | N/A | 10M | 14.0 | 6.0 | 3.2 | 1.8 | 2.8 |
| SoTA (MTL) | N/A | - | | | 87.4 | | |
