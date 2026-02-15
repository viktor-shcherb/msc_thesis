# 3.2 Retrieval-Augmented Generation Does Not Perform Well on BABILong [p. 6-7]

## RAG as a solution for long contexts [p. 6]

Retrieval-Augmented Generation (RAG) is a popular solution for language models to handle large amounts of text. In RAG relevant parts of text are retrieved from a large dataset in the first stage. Then, the language model uses input augmented with retrieved texts to generate the final response. In the case of BABILong, we expect RAG to extract all the facts relevant to a question from a long input text and then place them in the context of the language model. [p. 6]

## Experimental setup [p. 6]

We experiment with two options: (1) retrieval by chunks of size 512 tokens, denoted RAG-C and (2) retrieval by sentences, called RAG-S. We perform full grid of evaluation in RAG samples with GPT4 and Llama-3 please refer to Appendix G. The findings from the QA1 task, depicted in Figure 3a, indicate that retrieval performance using sentence chunks is superior to that of 512-token segments, with a notable increase in accuracy observed already after 16k token context length. However, this superiority is task-specific and may not translate effectively to real-world applications due to the potential for information loss in smaller chunks. [p. 6]

**Figure 3** (p. 6): "Fine-tuning but not RAG solves BABILong. a) RAG on QA1 task. Retrieval by chunks with size 512 tokens (RAG-C) fails to improve GPT-4 performance on long-context tasks. RAG-S, which retrieves by sentences achieves better results, but further increasing the number of retrieved sentences from top-5 to top-20 does not help. b) Task specific fine-tuning. Pretrained Mamba achieve the best overall results, greatly outperforming RAG models. However, processing sequences longer than 128k is extremely slow due to technical limitations. On the other hand, RMT shines on extremely long sequences, managing to keep high accuracy up to 10M tokens."

Description: Two-panel heatmap figure showing performance across different models and context lengths:
- Panel (a): Shows RAG results on QA1 task with different chunk sizes and top-k retrievals across context lengths (0K to 10M). Color coding from red (poor, <40%) to green (good, 90-100%). Shows that RAG-C (512 tokens) performs poorly across most lengths, while RAG-S (sentence-level) performs better but still has limitations.
- Panel (b): Shows task-specific results for QA1-QA5 across different models and tasks. RMT and ARMT show strong performance (80-100%, green) across most tasks. Mamba shows good results on shorter contexts but has limitations on extremely long sequences. Models are evaluated at different context lengths from 0K to 10M tokens.

Key patterns:
- RAG methods struggle with increasing context length
- Fine-tuned models (RMT, ARMT, Mamba) significantly outperform RAG
- RMT maintains high accuracy even at 10M tokens
- Task complexity (QA1 to QA5) affects all models

Supports claim: RAG achieves only modest 60% accuracy on single-fact question answering [p. 6], while fine-tuned recurrent memory transformers can process up to 50 million tokens [p. 6].

---
[p. 6-7 continued]

## Performance analysis of RAG pipeline [p. 6-7]

The RAG pipeline with GPT-4-turbo shows scalable but weak performance on BABILong for sentence embeddings and poor scalability with chunking (see Fig. 3b). The weak performance of RAG might be attributable to the temporal dependencies inherent in the task, where the relevant fact is positioned at the end of the text. In QA2 and QA3, retrieval fails dramatically with accuracy plummeting below random guessing. This lack of success is attributable to the specific demands of these tasks, which require the retrieved facts (or three) to be in close proximity to generate accurate responses. For example, in instances where the key facts are "Mary got the milk there." and "Mary travelled to the hallway.", with the query being "Where is the milk?", the retrieval system may successfully identify the first fact but fail to retrieve the second due to insufficient similarity between the question and the latter fact. The default retrieval algorithm's lack of temporal consideration and limitations in the similarity function underscore the necessity for additional methods in tasks with multi-hop reasoning and temporal dynamics. [p. 6-7]
