# 3.3 Pre-Training LLMs with Attention Sinks [p. 6]

As elaborated in Section 3.1, a significant reason for the model's excessive attention to multiple initial tokens is the absence of a designated sink token to offload excessive attention scores. Due to this, the model inadvertently uses globally visible tokens, primarily the initial ones, as attention sinks. A potential remedy can be the intentional inclusion of a global trainable attention sink token, denoted as a "Sink Token", which would serve as a repository for unnecessary attention scores. [p. 6]

## Alternative: SoftMax-off-by-One [p. 6]

Alternatively, replacing the conventional SoftMax function with a variant like SoftMax-off-by-One (Miller, 2023):

$$\text{SoftMax}_1(x)_i = \frac{e^{x_i}}{1 + \sum_{j=1}^{N} e^{x_j}} \tag{2}$$

Equation 2: SoftMax$_1$ variant which does not require the attention scores on all contextual tokens to sum up to one, and may also be effective. SoftMax$_1$ is equivalent to prepending a token with an all-zero Key and Value features in the attention computation. The authors denote this method as "Zero Sink" to fit their framework. [p. 6]

## Pre-training Validation [p. 6]

For validation, three language models with 160 million parameters are pre-trained from scratch under identical settings:
1. **Vanilla**: standard SoftMax attention
2. **Zero Sink**: replaced the regular attention mechanism with SoftMax$_1$
3. **Sink Token**: prepending a learnable placeholder token in all training samples

**Table 3** (p. 6): "Comparison of vanilla attention with prepending a zero token and a learnable sink token during pre-training. To ensure stable streaming perplexity, the vanilla model requires several initial tokens. While Zero Sink shows a slight improvement, it still needs other initial tokens. Conversely, the model trained with a learnable Sink Token shows stable streaming perplexity with only the sink token added. Cache config $x$+$y$ denotes adding $x$ initial tokens with $y$ recent tokens. Perplexity is evaluated on the first sample in the PG19 test set."

| Cache Config | 0+1024 | 1+1023 | 2+1022 | 4+1020 |
|---|---|---|---|---|
| Vanilla | 27.87 | 18.49 | 18.05 | 18.05 |
| Zero Sink | 29214 | 19.90 | 18.27 | 18.01 |
| Learnable Sink | 1235 | **18.01** | 18.01 | 18.02 |

Note: The Learnable Sink model with cache config 1+1023 achieves perplexity of **18.01**, matching the performance of larger cache configurations (2+1022 and 4+1020), demonstrating that a single dedicated sink token suffices. The Vanilla and Zero Sink models show very high perplexity (27.87 and 29214, respectively) when no initial tokens are kept (0+1024 config).

As shown in Table 3, while the zero sink alleviates the attention sink problem to some extent, the model still relies on other initial tokens as attention sinks. Introducing a sink token is highly effective in stabilizing the attention mechanism. Simply pairing this sink token with recent tokens sufficiently anchors the model's performance, and the resulting evaluation perplexity is even marginally improved. Given these findings, the authors recommend training future LLMs with a sink token in all samples to optimize streaming deployment. [p. 6]
