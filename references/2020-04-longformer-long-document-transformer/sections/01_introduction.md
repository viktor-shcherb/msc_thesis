# Introduction [p. 1-2]

## Problem statement

[p. 1] Transformers (Vaswani et al., 2017) have achieved state-of-the-art results in a wide range of NLP tasks including generative language modeling (Dai et al., 2019; Radford et al., 2019) and discriminative language understanding (Devlin et al., 2019). This success is partly due to the self-attention component which enables the network to capture contextual information from the entire sequence. However, the memory and computational requirements of self-attention grow quadratically with sequence length, making it infeasible (or very expensive) to process long sequences.

## Proposed solution

[p. 1-2] To address this limitation, the authors present Longformer, a modified Transformer architecture with a self-attention operation that scales linearly with the sequence length, making it versatile for processing long documents (Fig 1). This is an advantage for NLP tasks such as long document classification, question answering (QA), and coreference resolution, where existing approaches partition or shorten the long context into smaller sequences that fall within the typical 512 token limit of BERT-style pretrained models. Such partitioning could potentially result in loss of important cross-partition information. Longformer is able to build contextual representations of the entire context using multiple layers of attention, reducing the need for task-specific architectures.

## Gap addressed

[p. 2] Recent work has addressed computational inefficiency of Transformers on long sequences (see Tab. 1). However, they primarily focus on autoregressive language modeling (LM), while the application of long document transformers to document-level NLP tasks in the transfer learning setting (Dai and Le, 2015; Peters et al., 2018; Howard and Ruder, 2018; Devlin et al., 2019) has remained largely unexplored. The authors address this gap and show that Longformer's attention mechanism can act as a drop-in replacement for the self-attention mechanism in pretrained Transformers, and leads to gains across a suite of document NLP tasks.

## Attention mechanism overview

[p. 2] Longformer's attention mechanism is a combination of a windowed local-context self-attention and an end task motivated global attention that encodes inductive bias about the task. Through ablations and controlled trials the authors show both attention types are essential: the local attention is primarily used to build contextual representations, while the global attention allows Longformer to build full sequence representations for prediction.

## Contributions

[p. 2] Three main contributions:

1. **Autoregressive character-level language modeling** using a combination of windowed and a new dilated attention pattern, allowing the model to process sequences of up to 32K characters on modern GPUs. Achieves state-of-the-art results on `text8` and `enwik8` benchmark datasets.

2. **Pretraining and finetuning for downstream tasks.** Pretrain Longformer with the masked language modeling (MLM) objective, continuing from the RoBERTa (Liu et al., 2019) released checkpoint. After pretraining, apply it to downstream language tasks through finetuning. Longformer consistently outperforms RoBERTa on a wide range of document-level NLP tasks including text classification, QA, and coreference resolution, achieving state-of-the-art results on two of these datasets.

3. **Longformer-Encoder-Decoder (LED):** A variant following an encoder-decoder architecture similar to the original Transformer model (Vaswani et al., 2017), intended for sequence-to-sequence (seq2seq) learning (Sutskever et al., 2014). LED uses Longformer's efficient attention pattern on the encoder network, allowing it to address long document seq2seq tasks such as summarization. Effectiveness demonstrated on the arXiv summarization dataset (Cohan et al., 2018).
