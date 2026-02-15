# 3.3 Fine-Tuning Models on BABILong [p. 7]

## Fine-tuning experiments overview [p. 7]

We performed fine-tuning experiments with GPT-3.5-Turbo, Mistral-7B-Instruct-v0.2, RMT and ARMT with GPT-2 (137M) backbone, and Mamba (130M) models. Fine-tuning results are in Figure 3b and Appendix I, Figure 9. [p. 7]

## RMT training details [p. 7]

RMT with a GPT-2 (Radford et al., 2019) backbone model is trained on each task individually with a segment size of 512 and memory size of 16. ARMT with GPT-2 used 10 memory tokens (Rodkin et al., 2024). Train and evaluation splits of each task contain 10000 and 1000 samples, respectively, with a number of facts in each sample ranging from 2 to 320 depending on the task. A curriculum strategy is employed, initiating training sequences that fit in a single segment and then gradually introducing longer sequences once the training converges. During each curriculum stage n, sequence lengths are randomly sampled from 1 to n segments. We provide details of training and evaluation procedures in Appendix C. [p. 7]

## Performance of RMT and ARMT [p. 7]

RMT and ARMT models trained on 32 segments totalling in 16K tokens demonstrates strong performance on this length. Notably, recurrent memory models outperform GPT-4 significantly, underscoring the efficiency of memory mechanism in processing long context. Even more importantly, the power of recurrent models extends beyond the training limit. RMT shows consistent performance on longer sequences, up to 128k tokens, with only a marginal quality degradation. Surprisingly, with context sizes scaling to 1 million, 10 million tokens, and even 11.1 million tokens, which is over 600 times of the training length. While ARMT successfully scales even further, reaching up to 50 million tokens (Rodkin et al., 2024). Recurrent memory models persistently outperform the larger counterparts utilizing RAG. [p. 7]

## Fine-tuned transformer models [p. 7]

Finetuned recurrent models, Mamba, RMT and ARMT perform equally well on QA1, however due to the technical limitations of the Mamba implementation the inference beyond 128k was extremely slow, which makes it nearly impossible to process longer sequences. Recurrent Memory models greatly outperform retrieval-augmented generation and are able to process sequences up to 10M and 50M tokens much faster than Mamba. However, Mamba has an edge in complex tasks such as remembering a large number of facts in QA3 (Table 4). [p. 7]

## GPT-3.5 and Mistral-7B fine-tuning [p. 7]

We evaluated GPT-3.5 and Mistral-7B models fine-tuned with 1000 samples from QA1 for 3 epochs. The evaluation results are shown in Appendix I, Figure 9. Fine-tuning dramatically improves performance for longer contexts making scores uniform across all input sizes. Still, these results are behind of fine-tuned Mamba, RMT and ARMT. [p. 7]
