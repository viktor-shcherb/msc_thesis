# 3.6 Contextual Hallucination Evaluation [p. 8]

The authors evaluate contextual hallucination of the 3B-size language models (described in Appendix B) on text summarization and question answering [p. 8]. Notice that they focus on the cases where the input context contains correct facts, but the model fails to produce accurate outputs [p. 8].

They follow the evaluation protocol of Chuang et al. (2024) [p. 8]. They feed the model output along with ground-truth responses to GPT-4o (OpenAI, 2024) [p. 8]. Then they ask GPT-4o to make binary judgements on whether the model outputs are accurate and free of hallucinations [p. 8]. Previous studies (Chuang et al., 2024; Ravi et al., 2024) have shown that the above hallucination evaluation protocol has relatively high agreement between GPT-4o judgments and human annotations, the automatic metric is reliable and mirrors the human evaluation [p. 8]. For each dataset, the accuracy is averaged over 100 samples [p. 8].

## Summarization [p. 8]

Table 4a presents hallucination evaluation on summarization datasets XSum (Narayan et al., 2018), CNN/DM (See et al., 2017), and MultiNews (Fabbri et al., 2019) [p. 8]. The task is to generate summaries for input documents [p. 8].

| Model | XSum | CNN/DM | MultiNews |
|-------|------|--------|-----------|
| Transformer | 0.44 | 0.32 | 0.42 |
| DIFF | 0.53 | 0.41 | 0.61 |

Table 4a: Accuracy (i.e., free of hallucinations) on text summarization datasets [p. 8].

## Question Answering [p. 9]

As shown in Table 4b, the authors compare the hallucination rate of DIFF Transformer and Transformer on both single- and multi-document question answering [p. 9]. The Qasper (Dasigi et al., 2021) dataset is single-document question answering [p. 9]. In contrast, HotpotQA (Yang et al., 2018) and 2WikiMultihopQA (Ho et al., 2020) are multi-document [p. 9]. The goal is to answer questions about the given context [p. 9]. All evaluation examples are from LongBench (Bai et al., 2023) [p. 9].

| Model | Qasper | HotpotQA | 2WikiMQA |
|-------|--------|----------|----------|
| Transformer | 0.28 | 0.36 | 0.29 |
| DIFF | 0.39 | 0.46 | 0.36 |

Table 4b: Accuracy (i.e., free of hallucinations) on question answering datasets [p. 9].

Table 4: Evaluation of contextual hallucination on text summarization and question answering [p. 8]. Higher accuracy indicates less hallucination [p. 8]. They follow Chuang et al. (2024) to employ GPT-4o to make binary judgments, which has relatively high agreement with human annotation [p. 8].

Compared with Transformer, their method mitigates contextual hallucination on summarization and question answering [p. 9]. The performance improvement possibly stems from DIFF Transformer's better focus on essential information needed for the task, instead of irrelevant context [p. 9]. This aligns with previous observation (Huang et al., 2024) that one primary reason for contextual hallucination in Transformer is the misallocation of attention scores [p. 9].
