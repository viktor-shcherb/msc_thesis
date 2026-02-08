# Model Analysis [p. 9-10]

## Effect of training context length

[p. 9] Do models trained with larger context sizes perform better on RULER? The authors evaluate the suite of LargeWorldModels (Liu et al., 2024a; LWM) of equal parameter size and trained up to various context lengths. Figure 4 (left & middle-left) shows that larger context sizes overall lead to better performance, but the ranking can be inconsistent for long sequences. For instance, the model trained with 1M context size (LWM-1M) is worse than the one with 512K at length of 256K, likely due to insufficient training for adjusting to the new base frequency in RoPE. Moreover, abrupt performance drops are observed when models need to extrapolate to unseen lengths (e.g., LWM-128K given input of 256K), and almost linear degradation with input length on log scale within the max training context size.

## Effect of model size

[p. 9] The top models in the main results are much larger than other models. To ablate the effect of model size, the authors evaluate Yi-34B-200k, Yi-9B-200k, and Yi-6B-200k, all trained up to the same context length using the same data blend. Figure 4 (middle-right) shows that the 34B model is significantly better than the 6B model on RULER for both performance at length of 4K and the relative degradation, suggesting the benefit of scaling model sizes for better long-context modeling.

## Effect of architecture

[p. 9-10] The authors evaluate the effective context length for two models with non-Transformer architectures: RWKV-v5 (Peng et al., 2023) and Mamba-2.8B-slimpj (Gu & Dao, 2023). Both models demonstrate significant degradation when extending context size to 8K, and both underperform the Transformer baseline Llama2-7B by large margins up till the length of 4K, beyond which Llama2 shows poor length extrapolation performance (Figure 4 right).

## Figures

**Figure 4** (p. 9): "(**Left & middle left**): Comparison of LargeWorldModel (LWM) series trained up to various context sizes with fixed parameter size of 7B. (**Middle right**): Comparison of Yi suite models with different parameter sizes with controlled training context length of 200K. (**Right**): Performance of non-Transformer architectures lags behind the Transformer baseline Llama2-7B by large margin. Length extrapolation is presented with dashed lines."

The figure contains four subplots:

- **Length Comparison (left):** x-axis "Sequence Length" (4K to 256K), y-axis "Accuracy" (0-100). Lines for LWM-1M, LWM-512K, LWM-256K, LWM-128K. All show degradation with length. LWM-1M and LWM-512K are close at short lengths (~80); at 256K, LWM-512K is slightly better than LWM-1M (~60 vs ~55). LWM-128K drops sharply beyond 128K (extrapolation shown as dashed line).
- **Length Comparison (middle-left):** x-axis "Sequence Length" (4K to 256K), y-axis "Accuracy" (0-100). Lines for LWM-base-1M, LWM-base-512K, LWM-base-256K, LWM-base-128K, LWM-base-32K. Similar trends to the left plot but for base (non-instruct) models. All models degrade; sharp drops at extrapolation lengths (dashed lines).
- **Size Comparison (middle-right):** x-axis "Sequence Length" (4K to 256K), y-axis "Accuracy" (0-100). Lines for Yi-34B-200K, Yi-9B-200K, Yi-6B-200K. Yi-34B-200K starts highest (~93 at 4K) and degrades most gradually; Yi-6B-200K starts lowest (~80 at 4K) and degrades most steeply (to ~20 by 256K).
- **Architecture Comparison (right):** x-axis "Sequence Length" (1K to 8K), y-axis "Accuracy" (0-100). Lines for Llama2-7B, RWKV-v5-7b, Mamba-2.8b-slimpj. Llama2-7B starts at ~85 at 4K; RWKV-v5-7b starts at ~50 at 1K and degrades to ~20 by 8K; Mamba-2.8b-slimpj starts at ~40 at 1K and degrades to ~15 by 8K. Both non-Transformer architectures substantially underperform the Transformer baseline.
