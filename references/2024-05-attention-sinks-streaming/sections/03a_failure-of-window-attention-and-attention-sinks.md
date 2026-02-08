# 3.1 The Failure of Window Attention and Attention Sinks [p. 4-5]

While the window attention technique offers efficiency during inference, it results in exceedingly high language modeling perplexity. Consequently, the model's performance is unsuitable for deployment in streaming applications. This section uses the concept of *attention sink* to explain the failure of window attention, serving as the inspiration behind StreamingLLM. [p. 4]

**Figure 3** (p. 4): "Language modeling perplexity on texts with 20K tokens across various LLM."
The figure shows four panels (Llama-2-7B, Pythia-12B, Falcon-7B, MPT-7B), each plotting log perplexity (y-axis) vs. input length (x-axis, 0K to 20K). Four methods are compared: Dense Attention (blue), Window Attention (orange), Sliding Window w/ Re-computation (green), and StreamingLLM (red). Observations reveal consistent trends:
1. Dense attention fails once the input length surpasses the pre-training attention window size.
2. Window attention collapses once the input length exceeds the cache size, i.e., the initial tokens are evicted.
3. StreamingLLM demonstrates stable performance, with its perplexity nearly matching that of the sliding window with re-computation baseline.
Each panel also shows the KV Cache Size and Pre-training Length markers on the x-axis.

## Identifying the Point of Perplexity Surge [p. 4]

Figure 3 shows the perplexity of language modeling on a 20K token text. It is evident that perplexity spikes when the text length surpasses the cache size, led by the exclusion of initial tokens. This suggests that the initial tokens, regardless of their distance from the predicted tokens, are crucial for maintaining the stability of LLMs. [p. 4]

## Why Do LLMs Break When Removing Initial Tokens' KV? [p. 4]

Visualizing attention maps from all layers and heads of Llama-2-7B and models in Figure 2, the authors find that beyond the bottom two layers, the model consistently focuses on the initial tokens across all layers and heads. Removing these initial tokens' KV will remove a considerable portion of the denominator in the SoftMax function (Equation 1) in attention computation. This alteration leads to a significant shift in the distribution of attention scores away from what would be expected in normal inference settings. [p. 4]

$$\text{SoftMax}(x)_i = \frac{e^{x_i}}{e^{x_1} + \sum_{j=2}^{N} e^{x_j}}, \quad x_1 \gg x_j, j \in 2, \ldots, N \tag{1}$$

Equation 1: The SoftMax function where $x_1$ (the attention logit for the first token) is much larger than all other logits. [p. 4]

Two possible explanations for the importance of the initial tokens in language modeling: (1) either their semantics are crucial, or (2) the model learns a bias towards their absolute position. To distinguish between these possibilities, experiments are conducted (Table 1), wherein the first four tokens are substituted with the linebreak token "\n". The observations indicate that the model still significantly emphasizes these initial linebreak tokens. Furthermore, reintroducing them restores the language modeling perplexity to levels comparable to having the original initial tokens. This suggests that the absolute position of the starting tokens, rather than their semantic value, holds greater significance. [p. 4-5]

**Table 1** (p. 5): "Window attention has poor performance on long text. The perplexity is restored when we reintroduce the initial four tokens alongside the recent 1020 tokens (4+1020). Substituting the original four initial tokens with linebreak tokens '\n' (4'\n'+1020) achieves comparable perplexity restoration. Cache config x+y denotes adding x initial tokens with y recent tokens. Perplexities are measured on the first book (65K tokens) in the PG19 test set."

| Llama-2-13B | PPL (lower is better) |
|---|---|
| 0 + 1024 (Window) | 5158.07 |
| 4 + 1020 | 5.40 |
| 4"\n"+1020 | 5.60 |

**Table 2** (p. 5): "Effects of reintroduced initial token numbers on StreamingLLM. (1) Window attention (0+y) has a drastic increase in perplexity. (2) Introducing one or two initial tokens doesn't fully restore model perplexity, showing that the model doesn't solely use the first token as the attention sink. (3) Introducing four initial tokens generally suffices; further additions have diminishing returns. Cache config x+y denotes adding x initial tokens to y recent tokens. Perplexities are evaluated on 400K tokens in the concatenated PG19 test set."

| Cache Config | 0+2048 | 1+2047 | 2+2046 | 4+2044 | 8+2040 |
|---|---|---|---|---|---|
| Falcon-7B | 17.90 | 12.12 | 12.12 | 12.12 | 12.12 |
| MPT-7B | 460.29 | 14.99 | 15.00 | 14.99 | 14.98 |
| Pythia-12B | 21.62 | 11.95 | 12.09 | 12.09 | 12.02 |

| Cache Config | 0+4096 | 1+4095 | 2+4094 | 4+4092 | 8+4088 |
|---|---|---|---|---|---|
| Llama-2-7B | 3359.95 | 11.88 | 10.51 | 9.59 | 9.54 |

## LLMs Attend to Initial Tokens as Attention Sinks [p. 4-5]

To explain why the model disproportionately focuses on initial tokens---regardless of their semantic relevance to language modeling---the authors introduce the concept of "attention sink". The nature of the SoftMax function (Equation 1) prevents all attended tokens from having zero values. This requires aggregating some information from other tokens across all heads in all layers, even if the current embedding has sufficient self-contained information for its prediction. Consequently, the model tends to dump unnecessary attention values to specific tokens. A similar observation has been made in the realm of quantization outliers (Xiao et al., 2023; Bondarenko et al., 2023), leading to the proposal of SoftMax-Off-by-One (Miller, 2023) as a potential remedy. [p. 4-5]

## Why Initial Tokens Become Attention Sinks [p. 5]

Why do various autoregressive LLMs, such as Llama-2, MPT, Falcon, and Pythia, consistently focus on *initial tokens* as their attention sinks, rather than other tokens? The explanation is straightforward: due to the sequential nature of autoregressive language modeling, initial tokens are visible to all subsequent tokens, while later tokens are only visible to a limited set of subsequent tokens. As a result, initial tokens are more easily trained to serve as attention sinks, capturing unnecessary attention. [p. 5]

The authors note that LLMs are typically trained to utilize multiple initial tokens as attention sinks rather than just one. As illustrated in Figure 2, the introduction of four initial tokens, as attention sinks, suffices to restore the LLM's performance. In contrast, adding just one or two does not achieve full recovery. The authors believe this pattern emerges because these models did not include a consistent starting token across all input samples during pre-training. Although Llama-2 does prefix each paragraph with a "<s>" token, it is applied before text chunking, resulting in a mostly random token occupying the zeroth position. This lack of a uniform starting token leads the model to use several initial tokens as attention sinks. The authors hypothesize that by incorporating a stable learnable token at the start of all training samples, it could singularly act as a committed attention sink, eliminating the need for multiple initial tokens to ensure consistent streaming. This hypothesis is validated in Section 3.3. [p. 5]
