# 1 Introduction [p. 1-2]

[p. 1] Understanding long documents requires modeling various discourse-level phenomena, including anaphora (Hobbs, 1979; Grosz et al., 1995), argument structure (Grimshaw, 1990), narrative scripts and trajectories (Schank and Abelson, 1977; Labov and Waletzky, 1997), and causal links between concepts (Mooney and DeJong, 1985). Most language models (LMs) are trained to predict the next word given only a small window of local context, preventing them from using long-range discourse structure.

Many research efforts have attempted to address this: Rosenfeld (1996) incorporated statistics from distant tokens to improve n-gram models, while Ji et al. (2015) added document-level context to neural LMs.

The Transformer LM (Vaswani et al., 2017), which forms the backbone of state-of-the-art NLP systems (Devlin et al., 2019; Brown et al., 2020), has been the focus of numerous efforts to process longer input sequences. Transformer LMs are constrained by the inefficiency of self-attention, whose complexity scales quadratically with the input sequence length. More efficient methods based on sparse attention (Correia et al., 2019) and cached memory (Rae et al., 2020) have been proposed to increase the maximum sequence length, progressing from GPT-2's 1024 tokens (Radford et al., 2019) to 4096 tokens (Zaheer et al., 2020) and finally 8192 tokens (Roy et al., 2021, *Routing Transformer*). When evaluated on the PG-19 benchmark dataset (Rae et al., 2020), these "long-range" Transformer LMs reach lower perplexities than baseline models on held-out data.

The paper asks: How do "long-range" Transformer LMs make use of the long-range context? The authors conduct a series of fine-grained analysis experiments inspired by the context analysis of LSTM LMs conducted by Khandelwal et al. (2018). They focus on analyzing the behavior of the state-of-the-art Routing Transformer and a simpler baseline model in the presence of various perturbations (e.g., word shuffling, random document replacement), and look closely at how different types of tokens are affected.

## Key findings (stated as contributions) [p. 1-2]

- Providing long-range context (i.e., further than 2K tokens away) to these models has *negligible* impact on the perplexity of tokens near the end of a sequence in aggregate. However, a fine-grained analysis reveals that it does help a small set of tokens (tokens within subword clusters and those that can only be copied from the distant context), as well as particular types of books (fictional and continuous). [p. 1-2]

- Despite the aforementioned improvements on a fraction of tokens, significantly perturbing the long-term context with word shuffling and random replacement has no notable impact on perplexity overall, suggesting that the evaluated models encode long-range context superficially at best. [p. 2]

- Long-range context is not used for sequence-level prediction tasks that move outside the teacher-forced setting of the previous experiments. [p. 2]

The authors conclude that while modern LMs can process much longer input sizes than those of the past, they do not exploit the information available in the long-range context. They recommend that future research on long-range LMs includes analysis experiments to shed light on how and when they are using the distant context. [p. 2]
