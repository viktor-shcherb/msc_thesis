# Discussion [p. 8-9]

[p. 8] Practitioners have to make important choices about the nuances of the Transformer architecture like positional encoding before undertaking the costly pretraining process. In the I.I.D evaluation of PEs, similar performance across different PEs is demonstrated, in line with observations of Haviv et al. (2022) and Scao et al. (2022b), which makes the choice of optimal positional encoding challenging.

In this paper, length generalization in downstream tasks is utilized as a means to assess the expressivity of positional encodings. This setup, in contrast to the I.I.D. evaluation, reveals a clear distinction among approaches of encoding positions. NoPE outperforms explicit PEs, and within explicit PEs, commonly used methods lag behind T5's Relative PE.

> In fact, the recent release of LLMs (Touvron et al., 2023; Chowdhery et al., 2022) suggests a shift towards adopting Rotary as a replacement for APE in the Transformer architecture. [p. 8]

However, the result in Section 4 clearly demonstrates that Rotary marginally outperforms APE at length generalization. Furthermore, it exhibits similar behavior to APE, as shown in Section 6.1, indicating potential susceptibility to the same limitations.

The disadvantages of explicit PEs over NoPE in length extrapolation contribute to the growing evidence that positional encodings pose challenges for Transformers (Sinha et al., 2022; Luo et al., 2021). The empirical results and theoretical analysis suggest that removing positional encoding holds promise as a modification to the widely used decoder-only Transformer architecture.

## Scaling up to 1B models

[p. 9] In order to study the behavior of position embeddings at scale, three 1B variants are trained post-submission -- ALiBi, Rotary and NoPE -- with context length of 1024 tokens on a subset of StarCoder training set (Li et al., 2023). For more details, refer to Appendix F.

Results on language modeling show that at I.I.D all variants have similar perplexity, but at length generalization, Rotary fails to generalize as its perplexity explodes. NoPE and ALiBi generalize similarly to larger context sizes up to almost twice their training context size, and for larger contexts ALiBi is relatively more stable than NoPE (see the discussion on *perplexity vs. downstream performance*). Preliminary exploration of fine-tuning the pretrained models, on datasets in Section 3, yielded identical performance among PE variants as the training context size of the 1.3B models is much larger than instance lengths in the datasets. A comprehensive downstream evaluation of these models remains a subject for future research.

## Perplexity vs. downstream Performance

[p. 9] Due to human cognitive constraints (Gibson, 1998; Kiyono et al., 2021), language modeling data might encompass short-range dependencies. The combination of this naturally occurring structure (which can be abundant in internet-based corpora) with the Recency Bias inherent in positional encodings like ALiBi could portray an unrealistic representation of models' length generalization performance. In fact, Chi et al. (2023) recently demonstrated that ALiBi's length generalization performance could be replicated using a window attention mask, where tokens beyond a window size $w$ are masked out. Interestingly, T5's Relative PE, which can be regarded as a trainable version of ALiBi, learns to attend both large and short range dependencies (Figure F.3). This is in line with Tay et al. (2022) observation and underscores the importance of evaluation setups on downstream tasks as compared to solely relying on perplexity.
