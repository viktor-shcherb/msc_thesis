# Introduction [p. 2-3]

## Long Context Era

Large language models have already entered the long context era. A myriad of LLMs has been released to support long context windows from 32K to 2M tokens [p. 2]. These methods (Hao et al., 2022; Chen et al., 2023a; Peng et al., 2023b; Ratner et al., 2023; Xiao et al., 2024; Jin et al., 2024) can unlock lots of complex real-world applications, such as long-document question-answering, multi-document summarization, long-horizon agent tasks, and repo-level code understanding.

## Research Approaches for Long Context

One line of research is based on ALiBi (Press et al., 2022) and RoPE (Su et al., 2024) embeddings, which allows us to train Transformers with short sequences and subsequently apply them to longer sequences during inference. Recently, different approaches (Xiong et al., 2023; Fu et al., 2024; Lin et al., 2024) help the model to extrapolate to 128K window size with continued pre-training. Later on, LongRoPE (Ding et al., 2024) was proposed to further extend the context window to 2M tokens [p. 2].

Another line of research also utilizes methodologies like context window sliding and segmentation to overcome the issue of the limited context window in original Transformers (Hao et al., 2022; Ratner et al., 2023). Furthermore, architectural innovations, transitioning from traditional Transformer-based designs to recurrent models or state space models, have shown promise in facilitating long-range computations naturally (Orvieto et al., 2023; Gu & Dao, 2023; Peng et al., 2023a). These techniques have been incorporated into several current open-source LLMs to enhance long sequence understanding capability (Chen et al., 2023b; Tworkowski et al., 2023).

## Current Evaluation Methods

These long-context models are primarily evaluated on three types of evaluations [p. 2]:
1. language model perplexity over long documents, which is used by most papers.
2. passkey retrieval (Mohtashami & Jaggi, 2023; Chen et al., 2023a; Li et al., 2023a) or needle-in-a-haystack (Team et al., 2023; Fu et al., 2024), which requires reciting a randomly inserted information in a long sequence. Several LLMs achieve 99%+ on this synthetic task.
3. long document question-answer or summarization over Qasper (Dasigi et al., 2021).

Evaluations (1) and (2) only provide a minimum bar for LLMs to pass, but their results cannot reflect LLMs' true ability to deal with realistic long-sequence tasks. Evaluation (3) provides a more realistic metric [p. 2].

## Comparison with Existing Tasks

**Figure 2** (p. 2): "Comparison extreme-label ICL with existing evaluation tasks. Passkey Retrieval is a synthetic task. Long-document Question-answering does not require reading the entire document to find the answer. In extreme-label ICL, the model needs to scan through the entire demonstration to understand the whole label space to make the correct prediction."

Description: Three-panel comparison showing task examples
- Panel (a) shows Passkey Retrieval with irrelevant filler text and a hidden pass key
- Panel (b) shows Long-document Question-answer with a passage about Mark Hunter and a question
- Panel (c) shows Extreme-label In-context Learning with in-context prompts, dialogues, and entity relationship prediction tasks with detailed label pairs

Notable patterns: Demonstrates the increasing complexity from synthetic retrieval to question answering to extreme-label classification
- Supports claim: Existing evaluations are insufficient to measure LLMs' ability to comprehend and reason over the entire input sequence

However, these tasks are more focused on retrieving correct information from the long input. In question answering, LLMs can take a shortcut to read a short snippet to predict the answer without reading the entire document as demonstrated in Figure 2 case (b). Similarly, summarization also suffers from the strong position bias, where LLMs can utilize the few leading sentences (Nallapat et al., 2017) to achieve high performance. Therefore, these metrics are insufficient to measure LLMs' ability to comprehend and reason over the entire input sequence [p. 3].

## Proposed Approach: In-context Learning on Extreme-label Classification

In this paper, we propose to adopt in-context learning (ICL) on extreme-label classification tasks (Anil et al., 2022; Milos et al., 2023) to evaluate long-context LLMs. Unlike the prior tasks, in-context learning requires LLMs to recognize the task by scanning over the entire input to understand the label space. This task necessitates LLMs ability to comprehend the entire input to make predictions [p. 3].

Due to the massive label space, the task demonstration could easily become a long sequence. For example, Discovery (Sileo et al., 2019) encompasses 174 classes with each example taking an average of 61 tokens. Therefore, the minimum total demonstration length (1 shot per class) already exceeds 10K tokens. Normally, LLMs demand more than 1 shot per class to understand the nuances of different fine-grained labels. Having multiple shots can significantly extend the total demonstration length to above 32K. Therefore, this task becomes a natural testbed for long-context understanding.

## LongICLBench Development

To systematically assess how these extended input capabilities affect model performance in the realm of fine-grained classification with in-context learning, we have compiled a benchmark, i.e. LongICLBench, consisting of six carefully-selected tasks with different difficulty levels in terms of context length and label space [p. 3].

We evaluate the performance of a wide range of long-context LLMs and **find that the performance of the open-source models uniformly dips as the task becomes more complex (e.g. requiring longer demonstration) as shown in Figure 3**. **Among the open-source models, the non-Transformer-based models, like RWKV and Mamba (Peng et al., 2023a; Gu & Dao, 2023), perform far behind the Transformer-based models**. Simultaneously, within a task, most of the models can benefit from the extensive demonstration if the length is within a certain range. As the input grows longer, it either hurts or makes the performance fluctuate as shown in Figure 1.

**Figure 1** (p. 1): "LLM performance on long in-context benchmark across different lengths. We curate datasets with different difficulty levels. As we increase the difficulty of the dataset, LLMs struggle to understand the task definition and suffer from significant performance degradation."

Description: Three-panel line graph showing accuracy vs. context token length
- Left panel: BANKING77 (Easy), showing performance from 2K to 14K tokens
- Middle panel: DialogRE, showing performance from 8K to 32K tokens
- Right panel: Discovery (Hard), showing performance from 10K to 50K tokens
- Legend shows 15 models including LLaMA-2-7B-LongLora, Long-LLaMA-code-7B, ChatGLM3-6B-32K, Yi-6B-200K, ChatGLM3-6B, Qwen-1.5-7B-base, Mistral-7B-v0.2-base, Gemini-7B-base, RWKV-5-World, InternLM2-7B-base, GPT-4-turbo, GPT4o, Claude3-Opus, Gemini-1.5-Pro, Random

Notable patterns: Performance generally decreases as context length increases; easy tasks maintain higher accuracy; hard tasks show dramatic performance drops; most models perform near random baseline on Discovery task
- Supports claim: LLMs struggle to understand task definition and suffer significant performance degradation as difficulty increases

**Figure 3** (p. 3): "Results for representative models across different evaluation datasets. The performance greatly decreases as the task becomes more challenging."

Description: Two-panel line graph comparing Open-source Models (left) and API-based Models (right)
- X-axis: Context Token Length (10000 to 40000)
- Y-axis: Accuracy (%)
- Open-source models: BANKING77-9K, TacRED-19K, DialogRE-32K, Discovery-41K showing models LLaMA-2-7B-32K, Long-LLaMA-code-7B, Mistral-7B-v0.2-base, Qwen-1.5-7B-base, RWKV-5-World, Mamba-2.8B
- API-based models: BANKING77-9K, DialogRE-32K, TacRED-19K, Discovery-41K showing GPT-4-turbo, GPT4o, Claude3-Opus, Gemini-1.5-Pro

Notable patterns: Both open-source and API-based models show declining performance as task difficulty increases; API-based models generally maintain higher accuracy; Discovery-41K shows near-zero performance for all models
- Supports claim: Performance greatly decreases as task becomes more challenging

## Discovery Task Performance

On the most difficult extreme-label classification task Discovery (Sileo et al., 2019), all LLMs achieve close-to-zero performance except Gemini-1.5-Pro with 14% accuracy. In contrast, a fine-tuned BERT model (Kenton & Toutanova, 2019) can achieve 87% [p. 3]. This highlights the challenges that the long in-context learning pose for the existing LLMs.

Moreover, we make further analysis on the distribution of label position to investigate the factors that affect the long in-context learning capability of these models. It is shown that the position distribution of instances in the prompt can dramatically influence the performance of some of the evaluated models.

## Contributions

In a nutshell, our contributions to this work can be summarized as follows [p. 3]:

1. We have identified in-context learning on extreme-label classification tasks as an ideal testbed for the evaluation of the long-context capability of the current LLMs. We developed LongICLBench, which serves as a complement to earlier benchmarks that concentrated on tasks like long document summarization, question answering (QA), or retrieval, focusing instead on long in-context learning.
2. We evaluate a line of recent long-context LLMs on LongICLBench and reveal their performances with gradually changed difficulty levels. Simultaneously, we find the sensitivity of some of the long-context LLMs regarding instance position in the prompt. We hope the evaluation results can provide more insights for the improvement of the design of long-context large language models.
