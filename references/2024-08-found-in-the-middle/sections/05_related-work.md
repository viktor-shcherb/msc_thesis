# 5 Related work [p. 8-9]

## Retrieval augmented generation

[p. 8-9] While LLMs exhibit strong capabilities (Gemini Team, 2023; OpenAI, 2022; Touvron et al., 2023), their knowledge is inherently limited in its pretraining data, and they are observed to struggle in handling knowledge intensive tasks (Petroni et al., 2020). To tackle this, retrieval augmented generation (RAG) is an effective framework that retrieves relevant information from external knowledge sources to aid and ground language models' generation (Lewis et al., 2020; Khandelwal et al., 2020; Borgeaud et al., 2021; Izacard and Grave, 2021; Izacard et al., 2022a; Izacard et al., 2022b).

Although RAG has powered many recent language model applications from question-answering (Izacard and Grave, 2021) to automatic task completion (Shen et al., 2023), recent work shows that LLMs tend to *lost-in-the-middle*, significantly hindering the full potential of RAG (Liu et al., 2023). In this work, the authors take a step further to understand the lost-in-the-middle problem from the viewpoint of attention bias. Moreover, they propose a remedy through attention calibration, which improves upon existing RAG frameworks.

## Long-context utilization in language models

[p. 9] There is a rich literature on enabling LLMs to handle longer input contexts, including designing efficient training and finetuning schemes (Dao et al., 2022; Li et al., 2023b,a; Shi et al., 2023b) and inference-time methods that extend an LLM's context length (Press et al., 2021; Ratner et al., 2023; Xiao et al., 2023; Bertsch et al., 2023). Nonetheless, even models specifically trained for long-context suffer lost-in-the-middle problem (Liu et al., 2023; Li et al., 2023a).

To improve LLMs' performance on handling long contexts, recent methods design better prompting techniques and pipelines that mechanically work around the lost-in-the-middle problem (Chen et al., 2023; Jiang et al., 2023; Peysakhovich and Lerer, 2023; Junqing et al., 2023). For instance, to avoid having the models process long input contexts, (Chen et al., 2023; Junqing et al., 2023) proposes to split long inputs into shorter contexts for models to better understand. To avoid relevant context being missed by the model, (Jiang et al., 2023; Peysakhovich and Lerer, 2023) proposes to rank the relevance of different parts of the input and re-order the most important parts to either the beginning or end of the entire input, where the models tend to focus more.

While these existing solutions lead to improved model performances by manipulating the input contexts, they do not fundamentally improve LLMs' underlying long-context utilization capability. In contrast, the authors set out to directly improve LLMs' long-context utilization capability to mitigate lost-in-the-middle problem.

## Self-attention and attention bias

[p. 9] The attention mechanism is initially introduced in RNN-based encoder-decoder architectures (Bahdanau et al., 2015; Luong et al., 2015). Building upon the self-attention mechanism, transformers (Vaswani et al., 2017) have achieved state-of-the-art performance in various domains (Devlin et al., 2018; Dosovitskiy et al., 2020). Self-attention has also been widely used as a proxy to understand and explain model behaviors (Clark et al., 2019; Hao et al., 2021; Vashishth et al., 2019).

However, the relationship between the lost-in-the-middle problem and LLM's self-attention has been under-explored. As an initial trial, "attention sorting" (Peysakhovich and Lerer, 2023) sorts documents multiple times by the attention they receive to counter lost-in-the-middle. Recently, He et al. (2023) construct a dataset for training LLMs to focus on the most relevant documents among long contexts. Unlike that method, which necessitates significant investment in data collection and LLM tuning, the authors' method offers an efficient solution by mitigating lost-in-the-middle problem with off-the-shelf LLMs.
