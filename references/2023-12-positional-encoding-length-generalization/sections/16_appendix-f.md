# Appendix F: Pretraining at 1.3B Scale [p. 26]

[p. 26] This section elucidates the preliminary assessment of length generalization on a pretrained LLM scaled to 1.3B. Ensuring a fair evaluation, models are pretrained across varied positional encodings, all on identical data with consistent parameters. Given the intrinsic significance of element positions in code data, the choice leaned towards code-based pretraining.

## F.1 Model Architecture [p. 26]

[p. 26] The approach remains consistent with the original codebase, merely increasing the model dimensions. A decoder-only Transformer structure encompassing 24 layers is adopted. The configuration details:

- $d_{\text{model}} = 1024$
- $d_{\text{kv}} = 128$
- $d_{\text{ff}} = 16{,}384$
- 32 attention heads
- 1.3B parameters total

The models are trained with a context size of 1024 tokens. For the rest of training hyperparameters, Allal et al. (2023) is followed [Note: The paper cites "Allal et al. (2023)" but no such entry exists in the bibliography; this likely refers to Li et al. (2023), the StarCoder paper, which has Loubna Ben Allal as second author]. Specifically:

- Global batch size: 256
- Optimizer: AdamW with $\beta_1 = 0.9$, $\beta_2 = 0.95$
- $\epsilon = 10^{-8}$
- Weight decay: 0.1
- Learning rate: $2 \times 10^{-4}$ with cosine decay
- 2% warm-up

## F.2 Dataset Selection [p. 26]

[p. 26] A subset of 30M documents from the StarCoder dataset (Li et al., 2023) is utilized, constituting a blend of 40% Python, 25% Java, 25% JavaScript, 5% GitHub issues, and 5% GitHub commits. Processed through the StarCoder tokenizer with a vocab size of 49,152, the dataset results in 30B tokens. The model has been trained for a single epoch. For comprehensive details on the remaining hyperparameters, Allal et al. (2023) is referenced [likely Li et al. (2023)].

---
[p. 27 continued]

## F.3 Generalization Evaluation [p. 27]

[p. 27] The evaluation aims to assess how the model's performance in predicting a given token varies with changes in context size, especially when the context size exceeds the training context size. Ideally, perplexity should generally improve as the context size increases since the model has access to more information.

**Evaluation setup:**
- 1500 validation documents selected, each representing a single source code file
- Perplexity calculated on the last tokens, considering various context sizes ranging from 512 to 2560 (model pretrained with context size of 1024)
- This evaluates both in-distribution (I.I.D., context length $\leq$ 1024) and out-of-distribution (O.O.D., context length > 1024) conditions
- Perplexity measured on a maximum of last 200 tokens in the document to keep computation tractable and ensure exactly the same set of tokens are evaluated per each context size

**Length bucketing:**
- Documents categorized into buckets based on their lengths
- Average perplexity calculated within each bucket
- This enables examining the nature of dependencies within each bucket, recognizing that longer documents do not always imply longer dependencies

**Key findings** (from Figure F.2 and Tables 3 and 4):

- **I.I.D. case (context length $\leq$ 1024):** All models benefit from a larger context up to the training size of 1024. No significant differences among the models are discernible across all length buckets.
- **O.O.D. case (context length > 1024):** The model trained with Rotary fails to generalize as its perplexity explodes in all cases, aligning with the findings in Section 4.
- NoPE and ALiBi effectively generalize to larger context sizes up to 1800.
- Beyond context size 1800, ALiBi exhibits relative stability compared to NoPE, though both models show a pattern of increasing perplexity, potentially indicating inefficiencies to capture longer dependencies.

**Figure F.2** (p. 28): > "Perplexity of the three pretrained models on examples from various length buckets. Each model is trained with different positional encoding schemes on identical training data and hyperparameters."

Grid of 15 subplots arranged in 5 rows x 3 columns. Each subplot corresponds to a document length bucket (from [750, 1000] to [4250, 4500]). X-axis: Context Size; Y-axis: Perplexity. Three lines per subplot: NoPE (purple circles), ALiBi (light blue squares), Rotary (red triangles).

Key observations from the plots:
- For short length buckets ([750, 1000] through [1250, 1500]), all three models show similar low perplexity (1-6 range) with only small differences.
- Starting from bucket [1500, 1750], Rotary's perplexity begins to spike dramatically at larger context sizes (e.g., reaching 251.684 at context size 1400 in bucket [1500, 1750]).
- For longer buckets ([2000, 2250] onward), Rotary explodes to hundreds or thousands in perplexity at O.O.D. context sizes, while NoPE and ALiBi remain relatively controlled.
- In the longest buckets ([3500, 3750] through [4250, 4500]), NoPE and ALiBi both show rising perplexity beyond context 1800 but remain far below Rotary. ALiBi tends to show slightly better stability than NoPE at the largest context sizes.

**Table 3:** The detailed perplexity (represented along with Figure F.2 for completeness) of the three pretrained models on examples from various length buckets (Part I) [p. 29]

Length Bucket [750, 1000]:

| Model | 512 | 640 | 760 | 878 | 1024 | 1200 | 1400 | 1600 | 1800 | 2048 | 2304 | 2560 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| NoPE | 2.456 | 2.314 | - | - | - | - | - | - | - | - | - | - |
| ALiBi | 2.427 | 2.310 | - | - | - | - | - | - | - | - | - | - |
| Rotary | 2.401 | 2.271 | - | - | - | - | - | - | - | - | - | - |

Length Bucket [1000, 1250]:

| Model | 512 | 640 | 760 | 878 | 1024 | 1200 | 1400 | 1600 | 1800 | 2048 | 2304 | 2560 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| NoPE | 2.958 | 2.372 | 2.282 | 2.192 | - | - | - | - | - | - | - | - |
| ALiBi | 2.944 | 2.392 | 2.375 | 2.263 | - | - | - | - | - | - | - | - |
| Rotary | 2.920 | 2.344 | 2.259 | 2.170 | - | - | - | - | - | - | - | - |

Length Bucket [1250, 1500]:

| Model | 512 | 640 | 760 | 878 | 1024 | 1200 | 1400 | 1600 | 1800 | 2048 | 2304 | 2560 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| NoPE | 3.122 | 2.951 | 2.722 | 2.676 | 2.618 | 2.570 | - | - | - | - | - | - |
| ALiBi | 3.077 | 2.940 | 2.816 | 2.723 | 2.678 | 2.670 | - | - | - | - | - | - |
| Rotary | 3.044 | 2.882 | 2.657 | 2.619 | 2.559 | 3.508 | - | - | - | - | - | - |

Length Bucket [1500, 1750]:

| Model | 512 | 640 | 760 | 878 | 1024 | 1200 | 1400 | 1600 | 1800 | 2048 | 2304 | 2560 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| NoPE | 2.620 | 2.541 | 2.467 | 2.258 | 2.187 | 2.158 | 2.121 | - | - | - | - | - |
| ALiBi | 2.616 | 2.564 | 2.527 | 2.305 | 2.226 | 2.249 | 2.307 | - | - | - | - | - |
| Rotary | 2.580 | 2.502 | 2.418 | 2.220 | 2.146 | 2.749 | 251.684 | - | - | - | - | - |

Length Bucket [1750, 2000]:

| Model | 512 | 640 | 760 | 878 | 1024 | 1200 | 1400 | 1600 | 1800 | 2048 | 2304 | 2560 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| NoPE | 3.002 | 2.911 | 2.853 | 2.704 | 2.436 | 2.397 | 2.399 | 4.581 | - | - | - | - |
| ALiBi | 2.966 | 2.908 | 2.954 | 2.774 | 2.480 | 2.487 | 2.595 | 4.114 | - | - | - | - |
| Rotary | 2.929 | 2.845 | 2.790 | 2.646 | 2.390 | 3.098 | 248.698 | 2054.099 | - | - | - | - |

Length Bucket [2000, 2250]:

| Model | 512 | 640 | 760 | 878 | 1024 | 1200 | 1400 | 1600 | 1800 | 2048 | 2304 | 2560 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| NoPE | 4.130 | 3.998 | 3.892 | 3.849 | 3.751 | 3.348 | 3.338 | 6.325 | 39.413 | - | - | - |
| ALiBi | 4.087 | 3.988 | 4.049 | 3.983 | 3.823 | 3.479 | 3.616 | 5.365 | 18.731 | - | - | - |
| Rotary | 4.007 | 3.878 | 3.787 | 3.744 | 3.657 | 4.190 | 146.958 | 531.824 | 722.276 | - | - | - |

Length Bucket [2250, 2500]:

| Model | 512 | 640 | 760 | 878 | 1024 | 1200 | 1400 | 1600 | 1800 | 2048 | 2304 | 2560 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| NoPE | 2.778 | 2.642 | 2.555 | 2.493 | 2.450 | 2.321 | 2.159 | 2.859 | 30.012 | 146.219 | - | - |
| ALiBi | 2.764 | 2.655 | 2.647 | 2.570 | 2.499 | 2.441 | 2.361 | 3.695 | 14.173 | 44.089 | - | - |
| Rotary | 2.732 | 2.600 | 2.514 | 2.448 | 2.415 | 2.864 | 155.077 | 532.601 | 669.556 | 750.022 | - | - |

Length Bucket [2500, 2750]:

| Model | 512 | 640 | 760 | 878 | 1024 | 1200 | 1400 | 1600 | 1800 | 2048 | 2304 | 2560 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| NoPE | 2.805 | 2.716 | 2.645 | 2.614 | 2.574 | 2.534 | 2.367 | 2.954 | 25.694 | 114.870 | 259.222 | - |
| ALiBi | 2.801 | 2.732 | 2.721 | 2.726 | 2.651 | 2.681 | 2.575 | 3.585 | 12.350 | 37.746 | 93.094 | - |
| Rotary | 2.776 | 2.686 | 2.615 | 2.587 | 2.554 | 3.302 | 120.402 | 503.155 | 621.873 | 676.160 | 732.808 | - |

Length Bucket [2750, 3000]:

| Model | 512 | 640 | 760 | 878 | 1024 | 1200 | 1400 | 1600 | 1800 | 2048 | 2304 | 2560 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| NoPE | 2.850 | 2.776 | 2.728 | 2.694 | 2.666 | 2.620 | 2.504 | 3.839 | 41.194 | 151.810 | 311.138 | 536.225 |
| ALiBi | 2.830 | 2.789 | 2.825 | 2.766 | 2.735 | 2.742 | 2.741 | 3.680 | 13.814 | 42.951 | 102.930 | 150.322 |
| Rotary | 2.774 | 2.702 | 2.656 | 2.629 | 2.607 | 3.323 | 156.282 | 506.789 | 674.506 | 676.882 | 780.594 | 760.104 |

Length Bucket [3000, 3250]:

| Model | 512 | 640 | 760 | 878 | 1024 | 1200 | 1400 | 1600 | 1800 | 2048 | 2304 | 2560 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| NoPE | 2.783 | 2.697 | 2.639 | 2.595 | 2.555 | 2.519 | 2.498 | 4.239 | 32.277 | 153.248 | 312.356 | 521.752 |
| ALiBi | 2.782 | 2.746 | 2.750 | 2.688 | 2.665 | 2.692 | 2.763 | 3.847 | 13.542 | 41.208 | 97.685 | 143.644 |
| Rotary | 2.733 | 2.649 | 2.589 | 2.542 | 2.506 | 3.107 | 169.800 | 471.389 | 619.115 | 670.209 | 804.750 | 824.417 |

Length Bucket [3250, 3500]:

| Model | 512 | 640 | 760 | 878 | 1024 | 1200 | 1400 | 1600 | 1800 | 2048 | 2304 | 2560 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| NoPE | 3.260 | 3.140 | 3.061 | 3.009 | 2.878 | 2.828 | 2.866 | 6.048 | 36.581 | 143.613 | 296.817 | 479.934 |
| ALiBi | 3.206 | 3.116 | 3.127 | 3.073 | 2.922 | 2.940 | 3.104 | 5.077 | 16.838 | 47.832 | 106.607 | 151.288 |
| Rotary | 3.181 | 3.061 | 2.985 | 2.935 | 2.823 | 3.525 | 169.851 | 664.657 | 729.844 | 861.122 | 870.443 | 943.464 |

**Table 4:** The detailed perplexity (represented along with Figure F.2 for completeness) of the three pretrained models on examples from various length buckets (Part II) [p. 30]

Length Bucket [3500, 3750]:

| Model | 512 | 640 | 760 | 878 | 1024 | 1200 | 1400 | 1600 | 1800 | 2048 | 2304 | 2560 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| NoPE | 3.070 | 3.003 | 2.969 | 2.942 | 2.894 | 2.826 | 2.816 | 3.808 | 30.840 | 122.338 | 278.935 | 473.120 |
| ALiBi | 3.054 | 3.011 | 3.069 | 3.006 | 2.954 | 2.971 | 3.107 | 4.845 | 15.691 | 46.406 | 106.966 | 158.849 |
| Rotary | 3.020 | 2.958 | 2.923 | 2.892 | 2.844 | 3.719 | 169.445 | 604.442 | 771.338 | 766.585 | 833.169 | 888.627 |

Length Bucket [3750, 4000]:

| Model | 512 | 640 | 760 | 878 | 1024 | 1200 | 1400 | 1600 | 1800 | 2048 | 2304 | 2560 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| NoPE | 2.703 | 2.593 | 2.564 | 2.517 | 2.466 | 2.440 | 2.427 | 3.447 | 35.851 | 135.291 | 281.145 | 438.679 |
| ALiBi | 2.657 | 2.570 | 2.614 | 2.553 | 2.515 | 2.541 | 2.639 | 4.049 | 14.112 | 40.070 | 94.953 | 138.232 |
| Rotary | 2.645 | 2.536 | 2.506 | 2.461 | 2.416 | 2.981 | 147.012 | 508.386 | 671.961 | 707.306 | 861.924 | 873.948 |

Length Bucket [4000, 4250]:

| Model | 512 | 640 | 760 | 878 | 1024 | 1200 | 1400 | 1600 | 1800 | 2048 | 2304 | 2560 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| NoPE | 3.096 | 3.021 | 2.947 | 2.905 | 2.862 | 2.843 | 2.809 | 3.459 | 27.171 | 109.982 | 244.809 | 414.226 |
| ALiBi | 3.086 | 3.040 | 3.064 | 3.028 | 2.931 | 2.983 | 3.058 | 4.316 | 13.509 | 37.900 | 88.864 | 129.419 |
| Rotary | 3.054 | 2.973 | 2.906 | 2.868 | 2.831 | 3.626 | 158.974 | 723.175 | 1114.522 | 989.245 | 1057.793 | 960.442 |

Length Bucket [4250, 4500]:

| Model | 512 | 640 | 760 | 878 | 1024 | 1200 | 1400 | 1600 | 1800 | 2048 | 2304 | 2560 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| NoPE | 3.056 | 2.992 | 2.921 | 2.869 | 2.815 | 2.786 | 2.872 | 8.839 | 42.054 | 133.110 | 255.307 | 418.937 |
| ALiBi | 3.004 | 3.008 | 3.022 | 2.975 | 2.913 | 2.975 | 3.097 | 4.915 | 15.522 | 43.614 | 98.910 | 142.342 |
| Rotary | 2.958 | 2.899 | 2.838 | 2.775 | 2.731 | 3.603 | 174.717 | 528.865 | 694.649 | 741.368 | 806.988 | 857.006 |

**Figure F.3** (p. 30): > "The learnt bias value $b_{\text{bucket}(\cdot)}$ (taken from the pretrained T5-3b model) visualized for relative distance bucket $\text{bucket}(\cdot) \in [0, 31]$ and 12 heads. Bucket 31 is exclusively used for all distances larger than 128 tokens. These results demonstrate that while T5 has heads that mask distant tokens, other heads attend to distant tokens when required."

Grid of 12 subplots (Dimensions 1-12), each showing a bar chart with X-axis "Index" (0 to 30) and Y-axis "Embedding Value". The patterns vary significantly across heads:
- Some heads (e.g., Dimension 1) show monotonically increasing values, indicating preference for attending to more distant tokens.
- Other heads (e.g., Dimension 6, 7, 9, 10, 11) show generally decreasing values, indicating the head masks distant tokens (similar to ALiBi).
- Some heads (e.g., Dimension 5, 12) show non-monotonic patterns with both increases and decreases.

This demonstrates the heterogeneity of learned T5 relative PE biases across attention heads — some heads focus locally while others attend globally.

**Figure F.4** (p. 31): > "Generalization behavior of positional encoding schemes on Primitive tasks."

Grid of 8 subplots arranged in 4 rows x 2 columns. Each subplot shows accuracy (Y-axis, 0 to 1) vs Problem Length (X-axis, 0 to 40) for five positional encoding schemes: NoPE (purple), T5's Relative PE (orange triangles), ALiBi (light blue), Rotary (red), Absolute Position Embedding (green). The gray shaded region marks the training distribution (problem lengths up to approximately 20). Tasks shown:

1. **Copy (Variant 1):** NoPE and T5's Relative PE maintain near-perfect accuracy across all lengths. ALiBi, Rotary, and APE drop to 0 around length 25-30.
2. **Copy (Variant 1 (2x)):** NoPE and T5's Relative PE generalize well. Others degrade around length 25-30.
3. **Copy (Variant 2):** NoPE maintains highest accuracy. All others drop, with T5's Relative PE degrading more gradually than ALiBi/Rotary/APE.
4. **Copy (Variant 3):** All methods degrade beyond the training distribution. NoPE and T5's Relative PE degrade more gracefully.
5. **Copy (Variant 3 (2x)):** NoPE and T5's Relative PE maintain near-perfect accuracy longest, degrading around length 30-35. Others drop around 25.
6. **Reverse (Variant 1):** NoPE and T5's Relative PE generalize well. ALiBi drops sharply around length 22. Rotary and APE drop around 20-25.
7. **Reverse (Variant 1 (2x)):** Similar pattern: NoPE and T5's Relative PE best, others drop earlier.
8. **Reverse (Variant 2):** NoPE and T5's Relative PE generalize well. Others degrade sharply beyond training distribution.

**Figure F.5** (p. 32): > "Generalization behavior of positional encoding schemes on Mathematical & Reasoning tasks."

Grid of 7 subplots arranged in 3 rows (2 columns in the first two rows, 1 in the last). Each subplot shows accuracy (Y-axis, 0 to 1) vs Problem Length (X-axis, 2 to 16) for five positional encoding schemes: NoPE (purple), T5's Relative PE (orange triangles), ALiBi (light blue squares), Rotary (red circles), Absolute Position Embedding (green). The gray shaded region marks the training distribution (problem lengths up to approximately 8). Shaded bands around lines indicate confidence intervals. Tasks shown:

1. **Addition:** All methods achieve near-perfect accuracy up to length 8. Beyond training distribution, all degrade. NoPE and T5's Relative PE degrade more gradually, while ALiBi, Rotary, and APE drop more sharply by length 12-16. Rotary shows the steepest drop.
2. **Summation:** Similar pattern to Addition. All methods near-perfect up to length 8. Beyond training distribution, ALiBi and Rotary degrade fastest. NoPE and T5's Relative PE maintain somewhat higher accuracy but still degrade.
3. **Parity:** All methods achieve near-perfect accuracy in-distribution. Beyond length 8, all methods degrade. NoPE maintains highest accuracy. APE and ALiBi drop close to 0 earliest.
4. **Sorting (Single Token):** NoPE maintains high accuracy across all lengths, degrading only slightly. T5's Relative PE also generalizes well. ALiBi, Rotary, and APE degrade more significantly, with APE dropping fastest.
5. **Sorting (Multi Token):** All methods achieve near-perfect accuracy up to length 8. Beyond training distribution, all methods show degradation. NoPE and T5's Relative PE degrade more gradually.
6. **Polynomial Evaluation:** All methods degrade significantly beyond training distribution. NoPE and Rotary show somewhat higher accuracy at longer lengths. All methods converge toward low accuracy by length 16.
7. **LEGO:** All methods show roughly similar performance in-distribution. Beyond length 8, all degrade. No single method shows clear superiority; NoPE and ALiBi show slightly better resilience. High variance (wide confidence intervals) visible for most methods.

**Figure F.6** (p. 33): > "Generalization behavior of positional encoding schemes on Classic Length Generalization tasks."

Grid of 2 subplots side by side. Each subplot shows accuracy (Y-axis, 0 to 1) vs Problem Length. Five PE schemes: NoPE (purple), T5's Relative PE (orange triangles), ALiBi (light blue squares), Rotary (red circles), Absolute Position Embedding (green). Gray shaded region marks training distribution. Tasks shown:

1. **SCAN:** (X-axis: 0 to 50) NoPE maintains near-perfect accuracy up to around length 25-30, then degrades to about 0.2 by length 40-50. T5's Relative PE and ALiBi degrade more steeply around length 20-30. Rotary shows a sudden drop around length 25. APE drops early around length 15-20.
2. **PCFG:** (X-axis: 0 to 30) All methods degrade rapidly beyond the training distribution. NoPE shows slightly better initial generalization but all converge to near-zero by length 25-30. High variability visible across methods.

**Figure F.7** (p. 33): > "Layer-wise distance of No PE's attention patterns with other positional encoding schemes measured across instances of SCAN dataset."

Grid of 12 subplots arranged in 3 rows x 4 columns, one per layer (Layer #01 through Layer #12). Y-axis: $D(\text{NoPE}, M)$ (distance metric, range 0 to 2). X-axis: Example Length (0 to 50). Five PE schemes compared: NoPE* (purple/green), T5's Relative PE (orange), ALiBi (light blue), Rotary (red), Absolute Position Embedding (green). Shaded bands show confidence intervals.

Key observations:
- Across all layers, NoPE's attention patterns are most similar (lowest distance) to T5's Relative PE.
- The distance to ALiBi, Rotary, and APE is generally higher.
- In early layers (Layer #01-#04), distances are generally lower across all methods. The distance to T5's Relative PE stays near 0-0.5.
- In later layers (Layer #05-#12), the distance to Rotary and APE increases, often reaching 1.0-2.0, while T5's Relative PE distance remains relatively lower (0.5-1.0).
- The distance tends to increase with example length for all methods, but the gap between T5's Relative PE and other methods widens at longer lengths.

**Figure F.8** (p. 33): > "The optimal scratchpad format is aggregated across all datasets per each model. The optimal scratchpad format is different for each model."

Bar chart with X-axis showing five PE methods (No PE, T5's Rel. Bias, ALiBi, Rotary, APE) and Y-axis showing Mean Reciprocal Rank (0 to 0.75). Eight scratchpad formats shown as different colored/styled bars:

- No Scratchpad (circle marker)
- Full (solid fill)
- Full - "Step Input" (green)
- Full - "Step Computation" (blue)
- Full - "Step Output" (triangle marker)
- Full - "Intermediate Vars" (small circle)
- Full - "Remaining Parts" (open circle)
- Minimal (Only Compute+Output) (diamond marker)

Key observations:
- No single scratchpad format is universally best across all PE methods.
- For **No PE**: "Full" and "Minimal" formats perform best (MRR around 0.5-0.6). "No Scratchpad" performs relatively well.
- For **T5's Rel. Bias**: "Full - Step Input" and "Full - Remaining Parts" perform best.
- For **ALiBi**: "No Scratchpad" has relatively high MRR. "Full - Remaining Parts" also performs well.
- For **Rotary**: "Full" format performs best.
- For **APE**: "Full - Step Input" and "Full - Remaining Parts" perform well.
- The optimal scratchpad format varies by model, confirming the paper's claim that scratchpad format choice interacts with PE method.

**Figure F.9** (p. 34): > "Generalization of various scratchpad formats for each model on the **Addition** task."

Grid of 5 rows (one per PE method: No PE, T5's Relative PE, ALiBi, Rotary, Absolute Position Embedding), each showing a bar chart. X-axis: Scratchpad Config (No Scratchpad, Minimal (Only Compute+Output), Full, Full - "Step Input", Full - "Step Computation", Full - "Step Output", Full - "Intermediate Vars", Full - "Remaining Parts"). Y-axis: Accuracy (Avg. over all OOD lengths), range 0 to 0.20.

Key observations:
- For **No PE**: "Full - Step Output" and "Full - Remaining Parts" achieve highest accuracy (~0.15-0.18). "No Scratchpad" is near 0.
- For **T5's Relative PE**: "Full - Remaining Parts" achieves highest accuracy (~0.15). Other formats lower.
- For **ALiBi**: All formats show relatively low accuracy (~0.05-0.10). "Full - Remaining Parts" slightly highest.
- For **Rotary**: Most formats near 0. "Full" shows some accuracy.
- For **APE**: "Full - Remaining Parts" achieves notable accuracy (~0.10-0.15). "Full - Intermediate Vars" also notable.

**Figure F.10** (p. 34): > "Generalization of various scratchpad formats for each model on the **Summation** task."

Same layout as Figure F.9. Y-axis: Accuracy (Avg. over all OOD lengths), range 0 to 0.4.

Key observations:
- For **No PE**: "Full - Step Output" achieves highest accuracy (~0.3). "No Scratchpad" and "Full" also show moderate performance.
- For **T5's Relative PE**: "Full - Step Output" achieves highest accuracy (~0.25). "Full - Remaining Parts" also notable.
- For **ALiBi**: "Full - Step Output" and "Full - Remaining Parts" show moderate accuracy (~0.15-0.20).
- For **Rotary**: "Full - Step Output" and "Full - Remaining Parts" show moderate accuracy (~0.15-0.20).
- For **APE**: "Full - Step Output" achieves highest accuracy (~0.25). "Full - Remaining Parts" also notable.

**Figure F.11** (p. 35): > "Generalization of various scratchpad formats for each model on the **Parity** task."

Same layout as Figures F.9-F.10. Y-axis: Accuracy (Avg. over all OOD lengths), range 0 to 0.8.

Key observations:
- For **No PE**: "Minimal" format achieves highest accuracy (~0.7). "Full" also high (~0.6). "No Scratchpad" moderate (~0.4).
- For **T5's Relative PE**: "Full" achieves highest accuracy (~0.5-0.6). "Minimal" also moderate.
- For **ALiBi**: "Full" and "Full - Step Input" achieve moderate accuracy (~0.4-0.5). Most formats show moderate performance.
- For **Rotary**: "Full" achieves highest (~0.5-0.6). Other formats moderate.
- For **APE**: All formats show very low accuracy (near 0), indicating APE struggles with Parity generalization regardless of scratchpad format.

**Figure F.12** (p. 35): > "Generalization of various scratchpad formats for each model on the **Sorting** task (Single Digit)."

Same layout. Y-axis: Accuracy (Avg. over all OOD lengths), range 0 to 1.

Key observations:
- For **No PE**: "Minimal" achieves highest accuracy (~0.75). "Full" also high (~0.7). "No Scratchpad" low.
- For **T5's Relative PE**: "Full - Remaining Parts" achieves highest (~0.5). Other formats moderate.
- For **ALiBi**: "Full - Remaining Parts" achieves high accuracy (~0.5-0.6). Other formats moderate to low.
- For **Rotary**: "Full" and "Full - Remaining Parts" show moderate accuracy. Others lower.
- For **APE**: All formats show very low accuracy (near 0), similar to Parity.

**Figure F.13** (p. 36): > "Generalization of various scratchpad formats for each model on the **Sorting** task (Multi Digit)."

Same layout. Y-axis: Accuracy (Avg. over all OOD lengths), range 0 to 0.75.

Key observations:
- For **No PE**: "Minimal" achieves highest accuracy (~0.6). "Full" also moderate (~0.3-0.4). "No Scratchpad" low.
- For **T5's Relative PE**: "Minimal" and "Full - Remaining Parts" achieve moderate accuracy (~0.3-0.4).
- For **ALiBi**: "Full - Remaining Parts" and "Minimal" show some accuracy (~0.2-0.3).
- For **Rotary**: "Full" shows highest (~0.3). "Minimal" also moderate.
- For **APE**: "Full - Remaining Parts" shows some accuracy. Most formats near 0 or very low.

**Figure F.14** (p. 36): > "Generalization of various scratchpad formats for each model on the **Polynomial Evaluation** task."

Same layout. Y-axis: Accuracy (Avg. over all OOD lengths), range 0 to 0.6.

Key observations:
- For **No PE**: "No Scratchpad" achieves highest accuracy (~0.3). "Full - Step Output" and "Full - Remaining Parts" also moderate (~0.2-0.3).
- For **T5's Relative PE**: "Full - Step Output" shows some accuracy (~0.15). Other formats moderate to low.
- For **ALiBi**: "Full - Step Output" achieves highest (~0.3). "Full - Step Computation" also moderate.
- For **Rotary**: "Full - Step Output" and "Full - Remaining Parts" show moderate accuracy (~0.15-0.20).
- For **APE**: "Full - Step Output" and "Full - Remaining Parts" achieve moderate accuracy (~0.2). "Full - Intermediate Vars" shows notably high accuracy (~0.3).

**Figure F.15** (p. 37): > "Generalization of various scratchpad formats for each model on the **LEGO** task."

Same layout. Y-axis: Accuracy (Avg. over all OOD lengths), range 0 to 0.8.

Key observations:
- For **No PE**: "Full - Step Output" and "Full - Remaining Parts" achieve highest accuracy (~0.6-0.7). "No Scratchpad" moderate (~0.4).
- For **T5's Relative PE**: "Full - Remaining Parts" achieves highest accuracy (~0.5). Others moderate.
- For **ALiBi**: "Full - Remaining Parts" and "Full - Step Output" show highest accuracy (~0.5-0.6). Other formats also moderate.
- For **Rotary**: "Full - Remaining Parts" achieves highest (~0.5). "Full - Step Output" also moderate.
- For **APE**: "Full - Step Output" and "Full - Remaining Parts" achieve moderate accuracy (~0.4-0.5). "Full" also moderate.
