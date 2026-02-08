# B Analysis [p. 22-25]

[p. 22]

> "In this section we investigate why ALiBi works so effectively. We find that ALiBi's decrease in perplexity when given longer sequences is largely explained by its improved avoidance of the early token curse. We hypothesize that future work building on ALiBi might achieve further gains by more efficiently exploiting longer histories." [p. 22]

## B.1 Defining Sliding Window Evaluation and the Early Token Curse [p. 23]

### Figure 10

**Figure 10** (p. 23): "Sliding window evaluation (top; blue) compared to nonoverlapping evaluation (bottom; red) on a sequence of 8 words using a model with $L_{valid}$ = 4. Nonoverlapping evaluation is much faster since it requires just two inference passes (as opposed to the five passes required by the sliding window approach). But the sliding window approach provides more context for each prediction."

The figure shows a diagram of the sentence "The big gray cat sat on the mat" (8 words) evaluated with $L_{valid}$ = 4:
- Top (blue): Sliding window evaluation with multiple overlapping windows, requiring five inference passes to evaluate all tokens.
- Bottom (red): Nonoverlapping evaluation with two non-overlapping windows of 4 tokens each, requiring only two inference passes.

[p. 23]

**Sliding Window Inference**: As mentioned in Section 2, nonoverlapping inference is commonly used to evaluate sequences longer than $L$ (the number of tokens in each training subsequence). An alternative is to use a sliding window during evaluation (Baevski & Auli, 2018).

A stride $S$ is picked between 1 and $L - 1$, and the window is advanced by $S$ tokens after each forward pass.^{12} This means that $L - S$ tokens from the previous subsequence are re-encoded, and only $S$ new tokens are output. The advantage is that all outputs in each subsequence after the first have at least $L - S$ previous tokens to condition on. However, since tokens must be re-encoded multiple times, this approach is much slower than the nonoverlapping one. When $S = 1$, one token is output every inference pass, each using the maximal context window that the model can handle; however, this is the slowest approach. Figure 10 is a visualization of the nonoverlapping and sliding window evaluation approaches. [p. 23]

The authors use sliding window inference as a tool to analyze their models, but note that it is normally prohibitively slow in practice (Press et al., 2021). [p. 23]

^{12} Nonoverlapping inference can be viewed as sliding window inference with stride $L$. [p. 23]

**Early Token Curse**: Splitting an evaluation set into subsequences means that predictions occurring early in each subsequence cannot access many previous context tokens (appearing at the end of the previous subsequence). The result, referred to as the *early token curse* (Press et al., 2021), increases (i.e., degrades) perplexity scores. A workaround is to evaluate the model using a sliding window, giving each prediction more context. This solution is slow since it requires many more forward passes of the model. [p. 23]

## B.2 Extrapolation Reduces the Early Token Curse [p. 23-25]

[p. 23]

The authors presented results showing that their ALiBi method (and, to a lesser extent, the T5 bias) allows LMs to extrapolate during inference. Two reasons could explain why these methods enable LMs to achieve better perplexity given longer input subsequences:

1. Performance improves because the models can use longer contexts to make more accurate predictions. For example, the average article length in the WikiText-103 corpus is about 3600 tokens; therefore, if a model trained on $L$ = 512 tokens extrapolates to $L_{valid}$ = 3072 tokens during inference and achieves better results, that might be because it can spot patterns occurring across more than 512 tokens. [p. 23]

2. Performance improves because longer input sequences mean the early token curse is reduced. For example, during nonoverlapping evaluation on sequences of length $L_{valid}$ = 1000, 10% of predictions have 100 tokens of context or less. If we rerun nonoverlapping evaluation on that model with $L_{valid}$ = 2000 tokens, now only 5% of predictions have 100 tokens of context or less. So, by simply being able to handle longer sequences, a model can substantially reduce the early token curse and improve performance.^{13} [p. 23-24]

^{13} 100 tokens is an arbitrary small number used here to represent a short history context, i.e., one in which making predictions for the next output token would be harder. [p. 24]

[p. 24]

To better understand what might be occurring, the authors re-evaluate the development set of WikiText-103 with their models and the sinusoidal baseline with $L$ = 512, 1024, 3072. However, this time they use sliding window evaluation with a stride of $S$ = 1, meaning that they move the sliding window just one token after every inference pass, giving each prediction the maximum number of context tokens that the model can use. [p. 24]

### Figure 11

**Figure 11** (p. 24): "ALiBi models evaluated on different input lengths on WikiText-103 with sliding window evaluation (with stride $S$ = 1). Unlike results shown in Figure 4, where performance improves in each of our models as we increase the validation sequence length, here performance stays relatively flat as we increase $L_{valid}$. This might mean that ALiBi increases performance when $L_{valid} > L$ not because it uses longer contexts, but because fewer tokens suffer from the early token curse. Note that as in §2, the perplexity of the sinusoidal model explodes when $L_{valid} > L$ even when using sliding window evaluation."

The figure is a line plot titled "ALiBi and Sinusoidal Evaluation (w/ Sliding Window) on WikiText-103":
- x-axis: Validation Input Length ($L_{valid}$), values: 512, 1024, 1536, 2048, 3072
- y-axis: Perplexity (down arrow, lower is better), range approximately 16.5 to 19.5
- Sinusoidal lines (dotted with markers):
  - Sinusoidal, $L$ = 512: starts at approximately 18.35 at 512, increases sharply to approximately 19.0+ beyond 512
  - Sinusoidal, $L$ = 1024: approximately 18.05 at 1024, increases sharply beyond 1024
  - Sinusoidal, $L$ = 3072: single triangle at approximately 18.0 at 3072
- ALiBi lines (dashed with markers):
  - ALiBi, $L$ = 512: approximately 17.98 at 512, stays relatively flat around 18.0-18.3 across all evaluation lengths
  - ALiBi, $L$ = 1024: approximately 17.46 at 1024, stays relatively flat around 17.5-17.9
  - ALiBi, $L$ = 3072: single x marker at approximately 16.96 at 3072
- Key observation: Under sliding window evaluation, ALiBi performance stays relatively flat as $L_{valid}$ increases, while sinusoidal perplexity explodes when $L_{valid} > L$.

[p. 24]

The results are shown in Figure 11 and in the corresponding Tables 13 (sinusoidal) and 15 (ALiBi). [p. 24]

Unsurprisingly, for the sinusoidal model, as in §2, increasing $L_{valid}$ causes an explosion in perplexity even when using sliding window evaluation. The ALiBi models cannot improve perplexity when looking at longer sequences in this setting, but they keep perplexity flat when $L_{valid}$ increases. [p. 24]

This leads the authors to believe that their perplexity improvement when increasing $L_{valid}$ and using nonoverlapping evaluation is caused by explanation 2, not explanation 1. Because sliding window evaluation provides long context windows for *every* prediction made, it curtails the early token curse. In this setting, ALiBi's performance remains flat when $L_{valid}$ increases, leading them to hypothesize that the gains seen while increasing $L_{valid}$ in §4 were the result of larger $L_{valid}$ values mitigating the early token curse. [p. 24]

The ALiBi results mirror what occurs in the model using the T5 bias: when using sliding window evaluation, perplexity remains relatively flat when evaluating longer sequences (see Table 14). [p. 24]

The analysis reveals that when $L_{valid} > L$, ALiBi might not be using contexts longer than the ones it was trained on. This highlights a research direction that could be pursued in future work. [p. 24]

These findings do not lessen the value of ALiBi. When $L_{valid}$ = $L$, ALiBi achieves either superior or similar results to the sinusoidal method and other alternatives even though it is simpler and requires no learned parameters. When evaluating with $L_{valid} > L$ tokens, even if ALiBi does not attend to more than $L$ tokens, it yields better results than the other alternatives that can be used in this case, i.e., standard nonoverlapping inference (which is cheap, but does not perform as well) and the more accurate sliding window approach (which is very slow). [p. 24]

## Table 13

**Table 13** (p. 25): "Perplexities of the **sinusoidal** models evaluated with sliding window evaluation with stride $S$ = 1 on the WikiText-103 validation dataset."

| | Evaluation Length ($S$ = 1) |||||
| Train Length | 512 | 1024 | 1536 | 2048 | 3072 |
|---|---|---|---|---|---|
| 512 | 18.35 | 204.42 | 264.74 | 306.19 | 360.12 |
| 1024 | - | 18.05 | 206.55 | 302.6 | 393.71 |
| 3072 | - | - | - | - | 18.03 |

## Table 14

**Table 14** (p. 25): "Perplexities of the **T5 bias** models evaluated with sliding window evaluation with stride $S$ = 1 on the WikiText-103 validation dataset."

| | Evaluation Length ($S$ = 1) |||||
| Train Length | 512 | 1024 | 1536 | 2048 | 3072 |
|---|---|---|---|---|---|
| 512 | 17.92 | 18.51 | 20.36 | 22.62 | 30.77 |
| 1024 | - | 17.65 | 17.87 | 18.51 | 20.66 |
| 3072 | - | - | - | - | 17.41 |

## Table 15

**Table 15** (p. 25): "Perplexities of the **ALiBi** models evaluated with sliding window evaluation with stride $S$ = 1 on the WikiText-103 validation dataset."

| | Evaluation Length ($S$ = 1) |||||
| Train Length | 512 | 1024 | 1536 | 2048 | 3072 |
|---|---|---|---|---|---|
| 512 | 17.98 | 17.92 | 18.2 | 18.28 | 18.3 |
| 1024 | - | 17.46 | 17.47 | 17.62 | 17.92 |
| 3072 | - | - | - | - | 16.96 |
