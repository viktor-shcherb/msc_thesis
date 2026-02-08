# 1 Introduction [p. 1-2]

Transformer-based Large Language Models [40] (LLMs) have become the near-ubiquitous choice for many NLP tasks where long-range abilities such as *in-context learning* (ICL) have been crucial. The maximal length of sequences (the *context window*) determined by training has been one of the major limits of a pretrained LLM. Being able to dynamically extend the context window via a small amount of fine-tuning (or without fine-tuning) has become increasingly desirable. Position encodings of transformers are the center of these discussions. [p. 1]

The original Transformer architecture used an absolute sinusoidal position encoding, later improved to a learnable absolute position encoding [15]. Relative positional encoding schemes [32] further increased performance. Currently, the most popular relative positional encodings are *T5 Relative Bias* [30], *RoPE* [34], *XPos* [35], and *ALiBi* [27]. [p. 1]

One reoccurring limitation with positional encodings is the inability to generalize past the context window seen during training. While some methods such as ALiBi are able to do limited generalization, none are able to generalize to sequences significantly longer than their pre-trained length [22]. [p. 1]

Some works have been done to overcome such limitation. [9] and concurrently [21] proposed to extend the context length by slightly modifying RoPE via Position Interpolation (PI) and fine-tuning on a small amount of data. As an alternative, [6] proposed the "NTK-aware" interpolation by taking the loss of high frequency into account. Since then, two improvements of the "NTK-aware" interpolation have been proposed: [p. 2]

- the "Dynamic NTK" interpolation method [14] for pre-trained models without fine-tuning.
- the "NTK-by-parts" interpolation method [7] which performs the best when fine-tuned on a small amount of longer-context data.

The "NTK-aware" interpolation and the "Dynamic NTK" interpolation have already seen their presence in open-source models such as Code Llama [31] (using "NTK-aware" interpolation) and Qwen 7B [2] (using "Dynamic NTK"). [p. 2]

In this paper, in addition to making a complete account of the previous unpublished works on the "NTK-aware", the "Dynamic NTK" and the "NTK-by-part" interpolations, the authors present YaRN (Yet another RoPE extensioN method), an improved method to efficiently extend the context window of models trained with Rotary Position Embeddings (RoPE) including the LLaMA [38], the GPT-NeoX [5], and the PaLM [10] families of models. [p. 2]

**Key claims (contributions):** [p. 2]
- YaRN reaches state-of-the-art performances in context window extensions after fine-tuning on less than ~0.1% of the original pre-training data.
- By combining with the inference-time technique called Dynamic Scaling, the Dynamic-YaRN allows for more than 2x context window extension without any fine-tuning.

**Figure 1** (p. 1): "Sliding window perplexity (S = 256) of ten 128k Proof-pile documents truncated to evaluation context window size"

The figure shows perplexity (y-axis, lower is better) vs. context window (x-axis, 0 to ~130,000). The following models are plotted:
- CodeLlama-13b-hf
- Yarn-Llama-2-13b-64k
- Yarn-Llama-2-13b-128k
- togethercomputer/LLaMA-2-7B-32K
- CodeLlama-7b-hf
- Yarn-Llama-2-7b-64k
- Yarn-Llama-2-7b-128k

Key trends: All models show increasing perplexity when pushed far beyond their trained context windows. The YaRN models (64k and 128k variants) maintain low perplexity across their full extended context windows. At short context windows (~0-20,000), all models show similar perplexity around 2.3-2.6. The Code Llama and togethercomputer models show sharp perplexity increases beyond ~60,000-80,000 tokens. YaRN-128k models maintain stable perplexity (around 2.3-2.5) up to ~120,000 tokens.
