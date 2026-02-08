# 1 Introduction [p. 1–2]

[p. 1] LLMs (Brown et al., 2020; OpenAI, 2023a; Touvron et al., 2023) have exhibited exceptional performance across a range of NLP tasks (Qiu et al., 2020; Han et al., 2021). LLMs are showing a promising direction toward generalist task assistance, being capable of aiding users in practical tasks through conversational interactions. These tasks include web navigation (Nakano et al., 2021), analysis of code repositories (Chen et al., 2021), and extraction of useful information from documents (Kociskỳ et al., 2018), indicating a step towards artificial general intelligence. For these LLM-based scenarios, the ability to process long contexts is increasingly critical, in addition to understanding fine-grained semantics and possessing extensive knowledge (Dong et al., 2023; Huang et al., 2023). Textual documents, historical dialogues, complex instructions, and cumbersome workflows must be input to LLMs as long contexts for effective processing.

Despite this growing importance, LLMs consistently face challenges in processing long contexts, primarily due to the substantial computational resources required for long sequence training (Dao et al., 2022; Dao, 2023) as well as the apparent inability to generalize to sequences longer than those encountered during training (Chen et al., 2023a; Peng et al., 2023b). LLMs are typically trained on sequences containing no more than 8K tokens (Touvron et al., 2023; Penedo et al., 2023; Biderman et al., 2023), and thus cannot well handle contexts exceeding 8K tokens. These limitations have largely restricted most LLMs from being applied to more complex tasks.

[p. 2] Recent advancements in training infrastructure (Shoeybi et al., 2019; Narayanan et al., 2021; Dao et al., 2022; Dao, 2023), and efforts to improve length generalization (Anil et al., 2022; Chen et al., 2023b; Peng et al., 2023b) have led to rapid developments in long-context LLMs. Based on these improved training infrastructures and length generalization methods, several LLMs have purportedly managed to process data exceeding 100K tokens (Peng et al., 2023b; OpenAI, 2023b; 01.AI, 2023b,a), with Claude 2 (Anthropic, 2023) and Kimi-Chat (AI, 2023) even claiming to be able to process up to 200K tokens. However, the rapid emergence of long-context LLMs has outpaced the development of adequate evaluation benchmarks. Present long-context benchmarks predominantly feature contexts averaging around 10K tokens (Bai et al., 2023; Tay et al., 2020), invariably falling below 100K tokens.

> "This lag in the advancement of long-context evaluation methodologies impedes both the comparative analysis of diverse long-context LLMs and the pinpointing of potential enhancements in long-context processing." [p. 2]

The authors present InfiniteBench, the first comprehensive benchmark featuring an average data length surpassing 100K tokens. InfiniteBench includes tasks in different domains (novels, code, math, etc.) and languages (English and Chinese). To fully evaluate the performance of long-context LLMs, InfiniteBench integrates synthetic tasks that can be auto-generated for even longer contexts (e.g., finding the top-k number in an array) in addition to a set of realistic tasks.

To construct tasks annotated by humans, the authors develop 5 annotation pipelines for detailed example annotation. These pipelines undergo iterative refinement until the examples meet quality standards. Auto-generated tasks, conversely, can be easily scaled to various lengths.

The authors assess the performance of several SOTA long-context LLMs on InfiniteBench. The results show that current SOTA LLMs are not fully equipped to handle all tasks within InfiniteBench, highlighting the ongoing challenge of enabling LLMs to process long contexts effectively. They also conduct analyses on LLM behavior on such long contexts, including task length ablation, the absence of the "lost in the middle" phenomenon (Liu et al., 2023), and context recalling prompting techniques.

## Contributions

- Construction and release of InfiniteBench, the first multi-domain bilingual benchmark for evaluating the ability to understand and reason over contexts surpassing 100K tokens. [p. 2]
- Evaluation of SOTA long-context LLMs on InfiniteBench, which reveals severe performance degradation when scaling context lengths. The experimental results and analysis also indicate promising directions to improve long-context LLMs. [p. 2]

## Figure 1

**Figure 1** (p. 1): "The performance of GPT-4, Kimi-Chat, YaRN-Mistral, and Claude 2 on InfiniteBench. A higher value represents better performance."

Radar chart showing performance of four models (GPT-4, YaRN-Mistral, Kimi-Chat, Claude 2) across all 12 InfiniteBench tasks: En.Sum, Retrieve.KV, Retrieve.Number, Retrieve.PassKey, Math.Find, Math.Calc, Code.Run, Code.Debug, Zh.QA, En.Dia, En.MC, En.QA. GPT-4 generally covers the most area, particularly strong in retrieval and code tasks. Kimi-Chat shows strength in En.MC and En.Sum. Claude 2 is notable for En.Dia performance. YaRN-Mistral generally shows the smallest coverage area.
