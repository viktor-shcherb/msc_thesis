# Positional Encoding for Long Text [p. 7–8]

## Motivation [p. 7]

[p. 7] Early experiments used a synthetic "FIRST-SENTENCE-RETRIEVAL" task to probe the effective context window of the pretrained models, where the model is simply prompted to return the first sentence of the input. Initial results suggest that, with the original LLAMA 2 architecture untouched, the model was unable to effectively attend beyond 4,000–6,000 tokens even after extensive long-context continual pretraining. The authors hypothesize that the bottleneck comes from the RoPE positional encoding used in LLAMA 2 series, which imposes a heavy decay on the attention scores for distant tokens (footnote 3).

Footnote 3 [p. 7]: The quantity that heavily decays is E_{q,k}[RoPE(q, m)^T RoPE(k, n) | m, n] as the relative position |m - n| gets larger where q, k are the query and key of the two tokens at position m and n.

## Proposed Modification: Adjusted Base Frequency (ABF) [p. 7]

[p. 7] A simple modification to the default RoPE encoding to reduce the decaying effect: increasing the "base frequency b" of RoPE from 10,000 to 500,000, which essentially reduces the rotation angles of each dimension. The idea is also concurrently suggested in the Reddit r/LocalLLaMA community and Roziere et al. (2023). The effect of the base frequency change is visualized in Figure 4.

## Position Interpolation (PI) [p. 7]

[p. 7] Another concurrent approach named "position interpolation" (PI) (Chen et al., 2023) proposes to linearly scale the input positions such that the positions of tokens in the long sequences will be mapped to the model's original position range. As shown by the figure, it also implicitly achieves a decay reduction effect.

## xPOS [p. 7]

[p. 7] Another interesting observation from the visualization is that RoPE introduces large "oscillation" in the long-range regions, which could be undesirable for language modeling (Sun et al., 2022). To investigate whether this effect hurts performance, the authors also explored xPOS (Sun et al., 2022), a recently proposed variant of rotary encoding which smooths the high-frequency component. Note that xPOS with the default parameters suffers from the same decaying issue as RoPE and therefore, a similar decay fix (ABF) is applied to xPOS.

## Experimental Setup [p. 7–8]

[p. 7–8] Specifically, the following methods are compared: the RoPE baseline, PI, RoPE with adjusted base frequency (denoted as RoPE ABF), and xPOS ABF (visual comparisons in Figure 4). Results reported on: 1) long-sequence validation perplexity in Table 5 and Figure 5a, 2) the FIRST-SENTENCE-RETRIEVAL context probing task (footnote 4) in Figure 5b, and 3) some representative regular context tasks in Table 6 (to validate that long models do not degenerate on short-context tasks). All model variants are continually pretrained from the 7B LLAMA 2 checkpoint with additional 80B tokens organized as 32,768-token long sequences.

Footnote 4 [p. 8]: Also tested on the PASSKEY task as used in (Mohtashami and Jaggi, 2023). All the model variants except RoPE can achieve perfect accuracy. The authors believe this task is overly simple for context probing.

## Results [p. 7–8]

**Table 5** (p. 7): Validation perplexity of models with different positional encoding variants. All samples are 32,768-token sequences (CC: CommonCrawl).

| PE | Books | CC | Wikipedia |
|---|---|---|---|
| RoPE | 6.548 | 6.816 | 3.802 |
| RoPE PI | 6.341 | 6.786 | 3.775 |
| RoPE ABF | **6.323** | **6.780** | **3.771** |
| xPOS ABF | 6.331 | **6.780** | **3.771** |

**Table 6** (p. 8): The performance of models with different positional encoding variants on standard short-context benchmarks.

| | HumanEval | Math | MMLU | HellaSwag | TQA |
|---|---|---|---|---|---|
| RoPE | 14.63 | **3.62** | 45.69 | 76.31 | 65.23 |
| RoPE PI | 15.24 | 3.08 | 45.84 | 76.65 | **65.96** |
| RoPE-ABF | **17.07** | 3.52 | **46.24** | **76.73** | 66.04 |
| xPOS-ABF | 16.46 | 3.54 | 45.72 | 76.68 | **66.14** |

**Figure 4** (p. 8): "Decaying raw attention scores for distant tokens of explored positional encoding variants (assuming keys and queries are all-ones vectors)."

The figure shows Attention score before softmax (y-axis, ranging from roughly -2 to 12) vs. Distance between query and key tokens (x-axis, 0 to 30,000). Four lines are plotted:
- **RoPE** (blue): decays steeply from ~11 at distance 0 to oscillating around 0 at distance ~5,000, with large oscillation amplitude in the long-range region
- **RoPE PI** (orange): similar initial decay to RoPE but slightly less steep, also shows oscillation
- **RoPE ABF** (green): much slower decay, maintains higher scores at long distances (~2–4 range), smoother curve with less oscillation
- **xPOS ABF** (red): similar to RoPE ABF but even smoother, with minimal oscillation at long distances

**Figure 5** (p. 9): "Comparison of positional encoding variants on synthetic sentence retrieval task and validation perplexity evolution during continual pretraining."

(a) "Validation PPL (16k-token sequences) on a held-out long-context dataset."
- Y-axis: Validation perplexity (range approximately 6.475 to 6.675)
- X-axis: Continual train steps (5,000 to 20,000)
- RoPE PI, RoPE ABF, and xPOS ABF lines are plotted. All three decrease over training steps, converging to similar perplexity values around 6.48–6.50 by 20,000 steps. RoPE ABF and xPOS ABF are slightly lower than RoPE PI throughout.

(b) "Performance on FIRST-SENTENCE-RETRIEVAL task."
- Y-axis: ROUGE-L (0 to 100)
- X-axis: Task length (256, 1k, 2k, 4k, 8k, 10k, 12k, 14k, 16k, 20k, 24k, 28k, 30k)
- **RoPE** (blue): starts near 100 at short lengths, drops sharply around 4k–8k, falling to near 0 by 10k
- **RoPE PI** (orange): maintains near 100 up to ~10k, then drops gradually, reaching ~60 by 30k
- **RoPE ABF** (green): maintains near 100 across all lengths up to 30k
- **xPOS ABF** (red): similar to RoPE ABF, maintaining near 100 across all lengths up to 30k

## Summary of Findings [p. 8]

[p. 8] Overall, results on these evaluations suggest that RoPE ABF performs the best among all explored variants. In particular, RoPE ABF is the only variant that can maintain its performance up to the full 32,768-token context window on the FIRST-SENTENCE-RETRIEVAL task. xPOS ABF with less oscillation does not lead to substantial gains, suggesting that these artifacts are not detrimental to language modeling. While xPOS is claimed to possess better extrapolation property (Sun et al., 2022), with the base frequency modification, xPOS does not extrapolate better than RoPE (see Appendix C).

[p. 8] In addition to empirical results, a theoretical analysis of RoPE ABF and its difference to PI is provided in Appendix B. The authors argue that RoPE ABF distributes the embedded vectors with an increased granularity when compared to RoPE PI, making it easier for the model to distinguish between positions. The relative distance between the embedded vectors has a linear dependence on the key parameter of RoPE PI and a logarithmic dependence on the key parameter of RoPE ABF, which coincides with the empirical observation that the base-frequency is not very sensitive and can be easily adjusted based on the max sequence length.
