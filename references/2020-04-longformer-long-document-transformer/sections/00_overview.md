# Longformer: The Long-Document Transformer

**Authors:** Iz Beltagy\*, Matthew E. Peters\*, Arman Cohan\* (\* Equal contribution)
**Affiliation:** Allen Institute for Artificial Intelligence, Seattle, WA, USA
**Contact:** {beltagy, matthewp, armanc}@allenai.org
**Venue:** arXiv:2004.05150v2 [cs.CL]
**Date:** 2 Dec 2020
**Code:** https://github.com/allenai/longformer

## Abstract

> "Transformer-based models are unable to process long sequences due to their self-attention operation, which scales quadratically with the sequence length. To address this limitation, we introduce the Longformer with an attention mechanism that scales linearly with sequence length, making it easy to process documents of thousands of tokens or longer. Longformer's attention mechanism is a drop-in replacement for the standard self-attention and combines a local windowed attention with a task motivated global attention. Following prior work on long-sequence transformers, we evaluate Longformer on character-level language modeling and achieve state-of-the-art results on text8 and enwik8. In contrast to most prior work, we also pretrain Longformer and finetune it on a variety of downstream tasks. Our pretrained Longformer consistently outperforms RoBERTa on long document tasks and sets new state-of-the-art results on WikiHop and TriviaQA. We finally introduce the Longformer-Encoder-Decoder (LED), a Longformer variant for supporting long document generative sequence-to-sequence tasks, and demonstrate its effectiveness on the arXiv summarization dataset." [p. 1]

## Section headings

1. Introduction
2. Related Work
3. Longformer
   - 3.1 Attention Pattern
   - 3.2 Implementation
4. Autoregressive Language Modeling
   - 4.1 Attention Pattern
   - 4.2 Experiment Setup
   - 4.2.1 Results
   - 4.2.2 Ablation Study
5. Pretraining and Finetuning
6. Tasks
   - 6.1 Question Answering
   - 6.2 Coreference Resolution
   - 6.3 Document Classification
   - 6.4 Results
   - 6.5 Ablations on WikiHop
7. Longformer-Encoder-Decoder (LED)
8. Conclusion and Future Work
A. Implementation Details
B. Character LM Hyperparameters
C. Pretraining Data
D. Task Specific Model Details
