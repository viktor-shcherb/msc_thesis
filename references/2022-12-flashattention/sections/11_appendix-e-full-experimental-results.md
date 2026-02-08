# E Full Experimental Results [p. 26–34]

## E.1 BERT

[p. 26]

BERT-large is trained following the training procedure and hyperparameters of the reference MLPerf 1.1 implementation:

- **Optimizer:** LAMB, learning rate 3.75e-3
- **Batch size:** 448
- **Max steps:** 7100
- **Stopping criterion:** Training is stopped once the validation accuracy (for masked language modeling) reaches the target of 72.0%, and the wall-clock runtime is measured.
- **Precision:** FP16 using Apex AMP (with O2 optimization level)
- **Data split:** Same train / validation data split provided by MLPerf 1.1 reference implementation. Evaluate on the same 10000 validation examples as the baseline from Nvidia.
- **Hardware:** 8xA100-80GB GPUs
- **Training time:** Each training run takes between 16 and 19 minutes, averaged over 10 runs.

Results are compared with the reported training speed from Nvidia that was submitted to MLPerf 1.1 (Table 1).

## E.2 GPT-2

[p. 26]

The standard implementations of GPT-2 [67] from Huggingface `transformers` library and from Nvidia's Megatron-LM repo are used. The training recipe of the Megatron-LM repo is followed.

- **Effective batch size:** 512, using gradient accumulation to fit into available GPU memory.
- **Optimizer:** AdamW, with learning rate 6e-4 for GPT-2 small and 1.5e-4 for GPT-2 medium, and weight decay of 0.1.
- **Training steps:** All models are trained with the same hyperparameters for 400K steps.
- **Precision:** Mixed-precision training (PyTorch AMP).
- **Dataset:** Openwebtext dataset, with the GPT-2 BPE tokenizer. 0.5% of the dataset is randomly selected as the validation set, with the rest being used as training set. This random selection of validation set is done once, and all models are evaluated on the same validation set.
- **Hardware:** 8xA100-40GB GPUs
- **Training time:** GPT-2 small takes between 2.7–9.5 days, and GPT-2 medium takes between 6.9–21.0 days (Table 2).

**Figure 4** (p. 27): "Validation perplexity of GPT-2 small/medium using two implementations. We confirm that FlashAttention yields the same validation curves as the baseline implementation from HuggingFace."

- Y-axis: Val perplexity (range ~10–30)
- X-axis: Training steps (0 to ~400K)
- Four curves: GPT-2-small HuggingFace, GPT-2-small FlashAttention, GPT-2-medium HuggingFace, GPT-2-medium FlashAttention
- GPT-2-small curves start around 28–30 at ~50K steps, decrease to ~16 by ~300K steps
- GPT-2-medium curves start around 20–22 at ~50K steps, decrease to ~13 by ~300K steps
- FlashAttention curves lie almost exactly on top of the corresponding HuggingFace baseline curves, confirming numerical equivalence

**Long Document Classification.** For MIMIC-III and ECtHR, the hyperparameters of Dai et al. [13] are followed. [p. 26]

## E.3 LRA Details

[p. 27]

Hyperparameters are taken from the Long-range arena paper [80], the Long-range arena repo (https://github.com/google-research/long-range-arena), and the Nystromformer reproduction [90]. To be generous to the baseline methods, if the authors are unable to reproduce the performance of any baseline for any of the five tasks, they report the better performance from Tay et al. [80] or Xiong et al. [90] for that baseline on that task.

After hyperparameter tuning, almost all of the attention methods achieve similar accuracy on all of the five LRA tasks.

All methods are run with mixed-precision training, except for Performer (not stable with mixed precision) and Local Attention (implementation does not support FP16).

To calculate the overall wallclock-time speedup, the geometric mean of the wallclock-time speedup of each of the five tasks is taken.

**Path-X.** For Path-X and Path-256, the hyperparameters from the PathFinder-32 experiments from the long-range arena paper [80] are followed. For both, a model is first pretrained on Path-64. The checkpoint is taken after 200 epochs, its positional embedding is upsampled (duplicating the positional embeddings gridwise in space), and it is fine-tuned on the downstream task for 200 epochs with one epoch of linear warmup and cosine decay of the learning rate. For Path-X, the best performing checkpoint (according to val accuracy) is taken, and additionally fine-tuned for 200 epochs with the same warmup and learning rate (this adds roughly 4 points of accuracy to FlashAttention for Path-X, but the model starts overfitting afterwards). [p. 27]

## E.4 Comparison with Apex FMHA

[p. 27–28]

The authors compare their method/implementation with Apex FMHA (https://github.com/NVIDIA/apex/tree/master/apex/contrib/csrc/fmha).

When the project started, Apex FMHA was the fastest implementation of attention (that the authors knew of), tailored for short sequences of length at most 512. In fact, almost all MLPerf submissions for BERT training benchmark running on Nvidia GPUs use FMHA for their model code, as of MLPerf 1.1 [58]. [p. 27]

FMHA targets BERT models: it only supports head dimension 64, and only runs on A100 GPUs. FMHA fuses the attention computation dropout(softmax(MASK($\mathbf{Q}\mathbf{K}^\top$)))$\mathbf{V}$ into one CUDA kernel. In the forward pass, it stores the attention matrix softmax(MASK($\mathbf{Q}\mathbf{K}^T$)) to HBM to be used in gradient computation. As a result, it does not offer substantial memory saving (though for shorter sequences memory footprint is often not a primary concern). [p. 28]

The authors use FMHA code as a starting point, and apply two well-established techniques (tiling and recomputation) to deal with long sequences and to save memory as mentioned in Section 3. As a result, FlashAttention can support much longer sequences (e.g., up to length 64K), support more head dimensions (16, 32, 64, 128), and broader GPU types (all Turing and Ampere GPUs at the time of writing). [p. 28]

**Table 7** (p. 28): Runtime (ms) of FlashAttention compared to FMHA by sequence length, with masking and dropout, measured on an A100-SXM4-40GB GPU. Batch size 64, 16 heads, head dimension 64 (i.e., BERT-large size).

| Attention Method | 128 | 256 | 512 |
|---|---|---|---|
| Apex FMHA forward | 0.10 | 0.29 | 1.14 |
| FlashAttention forward | **0.08** | **0.22** | **0.81** |
| Apex FMHA backward | **0.17** | **0.52** | **1.81** |
| FlashAttention backward | 0.20 | 0.53 | 2.00 |
| Apex FMHA forward + backward | **0.27** | 0.81 | 2.95 |
| FlashAttention forward + backward | 0.28 | **0.75** | **2.81** |

Generally FlashAttention is slightly faster than FMHA in the forward pass and slightly slower than FMHA in the backward pass. This is because FlashAttention does not store the attention matrix in the forward pass and recomputes it in the backward pass. Compared to FMHA, the overall runtime of FlashAttention is about 4% slower for sequence length 128, 8% faster for sequence length 256, and 5% faster for sequence length 512. [p. 28]

## E.5 Speedup On Different Hardware and Configurations

[p. 28–30]

Speedup varies between different types of GPU types and generations depending on HBM bandwidth and SRAM size. FlashAttention speedup is profiled on different GPUs and configurations.

**Figure 5** (p. 28): "Speedup over standard PyTorch attention at different sequence lengths, on A100."

- Bar chart with X-axis: Sequence Length (128, 256, 512, 1024, 2048, 4096)
- Y-axis: Speedup (X times faster), range 0–5
- Three bar groups: Dropout + Masking (blue), Masking Only (orange), No Masking No Dropout (red)
- Speedup generally ranges from ~2x to ~4x across sequence lengths
- Higher speedup observed with Dropout + Masking due to kernel fusion

**A100.** Figure 5 shows speedup on an A100 GPU with batch size 8, head dimension 64, and 12 attention heads, across different sequence lengths. Generally 2–4x speedup is observed, and more speedup is seen when using dropout and masking due to kernel fusion. [p. 28]

**Figure 6** (p. 29): "Speedup over standard PyTorch attention at different sequence lengths, on A100, with head dimension 128."

- Bar chart with X-axis: Sequence Length (128, 256, 512, 1024, 2048)
- Y-axis: Speedup (X times faster), range 0–3.5
- Four bar groups: Dropout + Padding Masking (blue), Padding Masking Only (orange), Causal Mask (red), No Masking No Dropout (green)
- Causal Mask shows highest speedup (up to ~3.5x at seq len 2048)
- Other configurations generally 1–2.5x speedup
- Less overall speedup compared to head dimension 64

**A100, Head Dimension 128.** Speedup also changes when the head dimension is increased. Each block requires more memory, so smaller block sizes must be used to fit into SRAM. Figure 6 shows speedup with head dimension 128 on an A100 (batch size 16, 12 heads). Less speedup overall is observed, but significant speedup (up to 3x) can still be seen with a causal mask, where half the blocks are masked out. [p. 29]

**Figure 7** (p. 29): "Speedup over standard PyTorch attention at different sequence lengths, on RTX 3090."

- Bar chart with X-axis: Sequence Length (128, 256, 512, 1024, 2048)
- Y-axis: Speedup (X times faster), range 0–5
- Three bar groups: Dropout + Masking (blue), Masking Only (orange), No Masking No Dropout (red)
- Speedup generally ranges from ~2.5x to ~4.5x
- Slightly higher speedups than A100

**RTX 3090.** Figure 7 shows speedup on an RTX 3090 GPU. Batch size 12 with 12 attention heads is used. Slightly higher speedups on the RTX 3090 (between 2.5–4.5x) are observed, since the memory bandwidth on an RTX 3090 is lower than on an A100 (roughly 900 GB/s vs. 1.5 TB/s). [p. 29]

**Figure 8** (p. 30): "Speedup over standard PyTorch attention at different sequence lengths, on T4. **Top:** Combined forward pass + backward pass. **Bottom:** Forward pass only."

- Two bar charts stacked vertically
- **Top chart** (T4, forward + backward):
  - X-axis: Sequence Length (128, 256, 512, 1024, 2048)
  - Y-axis: Speedup (X times faster), range 0–3.5
  - Three bar groups: Dropout + Masking (blue), Masking Only (orange), No Masking No Dropout (red)
  - Speedup ranges from ~1.5x to ~3.5x
- **Bottom chart** (T4, Forward Only):
  - Same axes and groups
  - Speedup ranges from ~2.5x to ~4.5x
  - Higher speedup for forward-only than combined

**T4.** Figure 8 shows speedup on a T4 GPU. T4 SRAM is smaller than A100, so smaller block sizes are needed in FlashAttention. As a result, less speedup is observed on T4, which matches the IO complexity analysis in Section 3.2. T4 GPUs are commonly used for inference, so speedup on the forward pass only is also reported. [p. 29–30]

## E.6 Full Benchmarking Results

[p. 30–31]

Full benchmarking results and experimental details are reported on A100.

**Baselines.** For exact attention: reference implementations from PyTorch/HuggingFace and Megatron. For approximate attention: reference implementations of Reformer [51], Local Attention [68], Linformer [84], Smyrf [19], and LongShortFormer (LSFormer) [94]. For sparse attention: reference implementations of Block-Sparse Attention from OpenAI [11], Longformer [3], and BigBird Attention [92]. For the approximate and sparse attention, a compression ratio of 1/8 or a compressed sequence length of 256 is used, whichever is smaller. [p. 30]

**Setup.** Runtime and memory usage of the attention computation are measured with 8 heads of dimension 64, and batch size 16 on a machine with one A100 GPU with 40 GB of GPU HBM. Sequence length is varied. Attention is computed on random vectors for **Q**, **K**, and **V** (the projection from the hidden layer is not measured). For dropout, 0.1 is used; for masking, a padding mask with uniformly-random mask lengths between the total sequence length and the total sequence length minus 20 is used. To measure runtime, the average of 100 measurements of the attention call is taken. Memory footprint is only measured once, since it does not vary between runs. [p. 30]

**Table 8** (p. 31): Pointers to results tables.

| Dropout | Masking | Pass | Table |
|---|---|---|---|
| Yes | Yes | Forward | Table 9 |
| Yes | Yes | Backward | Table 10 |
| Yes | Yes | Combined | Table 11 |
| No | Yes | Forward | Table 12 |
| No | Yes | Backward | Table 13 |
| No | Yes | Combined | Table 14 |
| Yes | No | Forward | Table 15 |
| Yes | No | Backward | Table 16 |
| Yes | No | Combined | Table 17 |
| No | No | Forward | Table 18 |
| No | No | Backward | Table 19 |
| No | No | Combined | Table 20 |
| No | No | Memory Usage (Combined) | Table 21 |

**Table 9** (p. 31): Forward pass runtime (ms) of various exact/approximate/sparse attention mechanisms by sequence length, **with dropout and masking**. Best in **bold**, second best underlined.

| Attention Method | 128 | 256 | 512 | 1024 | 2048 | 4096 | 8192 | 16384 | 32768 | 65536 |
|---|---|---|---|---|---|---|---|---|---|---|
| PyTorch Attention | 0.36 | 0.34 | 0.78 | 2.54 | 9.33 | 36.33 | - | - | - | - |
| Megatron | 0.40 | 0.40 | 1.10 | 3.65 | 16.19 | - | - | - | - | - |
| Reformer | 2.03 | 3.15 | 5.67 | 11.02 | 22.59 | 46.14 | 97.38 | 212.13 | - | - |
| Local Attention | 0.83 | 0.86 | 1.01 | 2.20 | 7.13 | 14.32 | 28.60 | 57.79 | 117.67 | - |
| Linformer | 0.67 | 0.52 | 0.69 | 0.71 | 1.65 | 3.18 | 6.15 | 12.16 | 24.17 | 52.39 |
| Smyrf | 2.27 | 2.34 | 3.91 | 7.44 | 14.71 | 29.22 | 58.27 | 116.41 | - | - |
| LSFormer | 1.18 | 1.27 | 1.34 | 3.38 | 11.40 | 22.55 | 44.95 | 89.76 | 179.66 | - |
| Block Sparse | 1.12 | 1.11 | 2.13 | 2.77 | 6.95 | 20.91 | - | - | - | - |
| Longformer | 1.22 | 1.14 | 1.08 | 1.95 | 5.72 | 12.98 | - | - | - | - |
| BigBird | 1.13 | 1.12 | 1.12 | 1.77 | 6.03 | 13.68 | - | - | - | - |
| **FlashAttention** | **0.04** | **0.06** | **0.21** | **0.82** | **2.85** | **10.41** | **41.74** | **167.19** | **670.76** | **2682.35** |
| Block-Sparse FlashAttention | 0.06 | **0.06** | **0.06** | **0.12** | **0.44** | **0.86** | **1.70** | **3.29** | **6.55** | **13.34** |

Note: "-" indicates the method ran out of memory on the GPU at that sequence length. The Megatron implementation does not support sequence lengths longer than 2048. Block-Sparse (OpenAI) does not support sequence lengths longer than 4096. Longformer and BigBird do not support sequence lengths longer than 8092. [p. 31]

Timing results are reported on the forward pass, backward pass, and combined forward + backward pass. Each method is measured with and without dropout, masking, or both — except for Block Sparse, Longformer, and BigBird. These methods did not successfully run the backward pass with masking due to a bug in external libraries, so they were measured without masking to be generous. FP16 is used for all measurements, except for Local Attention, whose implementation only supports FP32. [p. 31]

For each baseline, sequence length is increased until it runs out of memory on the GPU, with exceptions: the Megatron implementation does not support sequence lengths longer than 2048; Block-Sparse (OpenAI) does not support sequence lengths longer than 4096; Longformer and BigBird do not support sequence lengths longer than 8092. [p. 31]

Memory usage is measured on the combined forward + backward pass, without dropout or masking.

**Results.** Table 8 summarizes all the experimental configurations and contains pointers to the results tables. [p. 31]

---
[p. 31–32 continued]

**Table 10** (p. 32): Backward pass runtime (ms) of various exact/approximate/sparse attention mechanisms by sequence length, **with dropout and masking**. Best in **bold**, second best underlined.

| Attention Method | 128 | 256 | 512 | 1024 | 2048 | 4096 | 8192 | 16384 | 32768 | 65536 |
|---|---|---|---|---|---|---|---|---|---|---|
| PyTorch Attention | 0.37 | 0.49 | 1.66 | 5.81 | 22.32 | 87.67 | - | - | - | - |
| Megatron | 0.35 | 0.32 | 0.77 | 2.42 | 8.43 | - | - | - | - | - |
| Reformer | 2.37 | 4.59 | 8.91 | 17.68 | 35.13 | 70.05 | 140.01 | - | - | - |
| Local Attention | 0.55 | 0.62 | 1.49 | 4.03 | 13.78 | 27.61 | 55.20 | 110.27 | 221.40 | - |
| Linformer | 0.89 | 0.80 | 0.81 | 0.93 | 2.48 | 4.75 | 9.29 | 18.27 | 36.53 | - |
| Smyrf | 1.41 | 2.83 | 5.43 | 10.72 | 21.25 | 42.31 | 84.48 | 168.95 | - | - |
| LSFormer | 1.75 | 1.76 | 3.01 | 7.50 | 20.07 | 39.08 | 76.39 | 150.82 | - | - |
| Block Sparse | 1.29 | 1.28 | 2.18 | 3.04 | 7.27 | 21.16 | - | - | - | - |
| Longformer | 1.27 | 1.31 | 1.29 | 2.04 | 5.24 | 10.74 | 25.95 | - | - | - |
| BigBird | 1.33 | 1.28 | 1.32 | 1.81 | 5.55 | 11.44 | 27.45 | - | - | - |
| **FlashAttention** | **0.30** | **0.26** | **0.68** | **2.02** | **6.84** | **26.89** | **105.70** | **418.96** | **1666.89** | **6660.44** |
| Block-Sparse FlashAttention | **0.30** | 0.27 | **0.29** | **0.59** | **1.50** | **2.94** | **5.82** | **11.85** | **23.98** | **47.61** |

**Table 11** (p. 32): Forward pass + backward pass runtime (ms) of various exact/approximate/sparse attention mechanisms by sequence length, **with dropout and masking**. Best in **bold**, second best underlined.

| Attention Method | 128 | 256 | 512 | 1024 | 2048 | 4096 | 8192 | 16384 | 32768 | 65536 |
|---|---|---|---|---|---|---|---|---|---|---|
| PyTorch Attention | 0.84 | 0.86 | 2.35 | 8.29 | 31.75 | 124.19 | - | - | - | - |
| Megatron | 0.87 | 0.89 | 1.33 | 4.21 | 16.50 | - | - | - | - | - |
| Reformer | 4.30 | 7.76 | 14.60 | 28.74 | 57.79 | 116.34 | 237.57 | - | - | - |
| Local Attention | 1.40 | 1.60 | 2.06 | 6.06 | 20.94 | 42.01 | 84.08 | 168.48 | 339.45 | - |
| Linformer | 1.57 | 1.49 | 1.55 | 1.60 | 4.19 | 8.04 | 15.71 | 30.92 | 61.47 | - |
| Smyrf | 3.41 | 5.08 | 9.35 | 18.18 | 36.03 | 71.68 | 143.04 | 285.87 | - | - |
| LSFormer | 3.08 | 3.10 | 4.26 | 10.90 | 31.59 | 61.72 | 121.51 | 241.18 | - | - |
| Block Sparse | 2.54 | 2.52 | 3.71 | 5.44 | 13.29 | 39.19 | - | - | - | - |
| Longformer | 2.47 | 2.49 | 2.51 | 3.10 | 10.39 | 22.49 | 60.14 | - | - | - |
| BigBird | 2.51 | 2.49 | 2.52 | 3.40 | 10.97 | 23.89 | 63.28 | - | - | - |
| **FlashAttention** | **0.43** | **0.41** | **0.95** | **2.55** | **9.56** | **37.49** | **147.75** | **586.61** | **2339.11** | **9341.30** |
| Block-Sparse FlashAttention | **0.44** | **0.44** | **0.45** | **0.89** | **1.95** | **4.12** | **7.64** | **16.60** | **32.73** | **64.11** |

**Table 12** (p. 32): Forward pass runtime (ms) of various exact/approximate/sparse attention mechanisms by sequence length, **with masking**. Best in **bold**, second best underlined.

| Attention Method | 128 | 256 | 512 | 1024 | 2048 | 4096 | 8192 | 16384 | 32768 | 65536 |
|---|---|---|---|---|---|---|---|---|---|---|
| PyTorch Attention | 0.30 | 0.30 | 0.63 | 1.93 | 7.08 | 27.45 | 112.90 | - | - | - |
| Megatron | 0.45 | 0.41 | 0.43 | 1.52 | 5.80 | - | - | - | - | - |
| Reformer | 1.87 | 3.00 | 5.37 | 10.43 | 21.40 | 43.83 | 92.80 | 203.24 | - | - |
| Local Attention | 0.70 | 0.81 | 1.02 | 2.09 | 6.64 | 13.34 | 26.77 | 54.02 | 110.11 | - |
| Linformer | 0.63 | 0.50 | 0.67 | 0.65 | 1.36 | 2.60 | 5.04 | 9.92 | 19.69 | 43.47 |
| Smyrf | 2.38 | 2.32 | 3.76 | 7.16 | 14.14 | 28.09 | 55.98 | 111.73 | - | - |
| LSFormer | 1.22 | 1.29 | 1.44 | 3.28 | 10.99 | 21.72 | 44.29 | 86.32 | 172.76 | - |
| Block Sparse | 0.96 | 1.04 | 1.66 | 2.16 | 5.41 | 16.15 | - | - | - | - |
| Longformer | 0.99 | 0.98 | 0.99 | 1.56 | 4.79 | 11.07 | 32.98 | - | - | - |
| BigBird | 0.96 | 1.02 | 1.02 | 1.48 | 5.05 | 11.59 | 34.16 | - | - | - |
| **FlashAttention** | **0.03** | **0.04** | **0.17** | **0.68** | **2.28** | **8.40** | **33.55** | **134.11** | **537.50** | **2150.88** |
| Block-Sparse FlashAttention | 0.05 | **0.04** | **0.05** | **0.11** | **0.35** | **0.68** | **1.33** | **2.54** | **5.34** | **10.73** |

**Table 13** (p. 32): Backward pass runtime (ms) of various exact/approximate/sparse attention mechanisms by sequence length, **with masking**. Best in **bold**, second best underlined.

| Attention Method | 128 | 256 | 512 | 1024 | 2048 | 4096 | 8192 | 16384 | 32768 | 65536 |
|---|---|---|---|---|---|---|---|---|---|---|
| PyTorch Attention | 0.44 | 0.46 | 1.53 | 5.33 | 20.34 | 79.87 | - | - | - | - |
| Megatron | 0.29 | 0.31 | 0.65 | 1.95 | 6.49 | - | - | - | - | - |
| Reformer | 2.31 | 4.47 | 8.68 | 17.20 | 34.14 | 68.09 | 136.02 | - | - | - |
| Local Attention | 0.51 | 0.62 | 1.30 | 3.81 | 13.33 | 26.72 | 53.41 | 106.82 | 214.15 | - |
| Linformer | 0.76 | 0.81 | 0.94 | 0.87 | 2.24 | 4.25 | 8.35 | 16.38 | 32.67 | 72.11 |
| Smyrf | 1.34 | 2.77 | 5.30 | 10.46 | 20.73 | 41.27 | 82.41 | 164.86 | - | - |
| LSFormer | 1.66 | 1.61 | 3.09 | 7.42 | 19.68 | 38.35 | 74.92 | 147.86 | - | - |
| Block Sparse | 1.24 | 1.25 | 2.04 | 2.91 | 6.78 | 19.67 | - | - | - | - |
| Longformer | 1.27 | 1.23 | 1.24 | 1.85 | 4.99 | 10.21 | 24.89 | - | - | - |
| BigBird | 1.43 | 1.50 | 1.44 | 1.69 | 5.25 | 10.86 | 26.26 | - | - | - |
| **FlashAttention** | **0.21** | **0.22** | **0.62** | **1.84** | **5.77** | **22.25** | **86.21** | **338.91** | **1343.91** | **5361.09** |
| Block-Sparse FlashAttention | 0.22 | **0.22** | **0.26** | **0.57** | **1.55** | **3.13** | **5.98** | **12.21** | **23.49** | **47.85** |

---
[p. 33 continued]

**Table 14** (p. 33): Forward pass + backward pass runtime (ms) of various exact/approximate/sparse attention mechanisms by sequence length, **with masking**. Best in **bold**, second best underlined.

| Attention Method | 128 | 256 | 512 | 1024 | 2048 | 4096 | 8192 | 16384 | 32768 | 65536 |
|---|---|---|---|---|---|---|---|---|---|---|
| PyTorch Attention | 0.80 | 0.81 | 2.08 | 7.23 | 27.51 | 107.58 | - | - | - | - |
| Megatron | 0.81 | 0.83 | 1.09 | 3.36 | 12.39 | - | - | - | - | - |
| Reformer | 4.16 | 7.46 | 14.06 | 27.68 | 55.66 | 112.15 | 229.37 | - | - | - |
| Local Attention | 1.39 | 1.68 | 2.08 | 5.83 | 20.04 | 40.16 | 80.44 | 161.35 | 325.11 | - |
| Linformer | 1.51 | 1.42 | 1.56 | 1.67 | 3.67 | 6.99 | 13.63 | 26.77 | 53.36 | 117.56 |
| Smyrf | 3.38 | 4.93 | 9.07 | 17.66 | 34.94 | 69.55 | 138.72 | 277.41 | - | - |
| LSFormer | 3.08 | 3.10 | 4.26 | 10.90 | 31.59 | 61.72 | 121.51 | 241.18 | - | - |
| Block Sparse | 2.39 | 2.40 | 3.31 | 5.02 | 12.25 | 35.94 | - | - | - | - |
| Longformer | 2.36 | 2.34 | 2.38 | 2.94 | 9.83 | 21.35 | 58.12 | - | - | - |
| BigBird | 2.35 | 2.35 | 2.37 | 3.25 | 10.36 | 22.57 | 60.63 | - | - | - |
| **FlashAttention** | **0.32** | **0.30** | **0.83** | **2.37** | **7.95** | **30.77** | **119.98** | **473.65** | **1883.43** | **7513.01** |
| Block-Sparse FlashAttention | **0.34** | **0.34** | **0.36** | **0.69** | **1.85** | **3.89** | **7.16** | **14.85** | **30.46** | **60.03** |

**Table 15** (p. 33): Forward pass runtime (ms) of various exact/approximate/sparse attention mechanisms by sequence length, **with dropout**. Best in **bold**, second best underlined.

| Attention Method | 128 | 256 | 512 | 1024 | 2048 | 4096 | 8192 | 16384 | 32768 | 65536 |
|---|---|---|---|---|---|---|---|---|---|---|
| PyTorch Attention | 0.26 | 0.24 | 0.57 | 1.80 | 6.56 | 25.34 | - | - | - | - |
| Megatron | 0.27 | 0.27 | 0.56 | 1.88 | 6.56 | - | - | - | - | - |
| Reformer | 1.83 | 2.96 | 5.31 | 10.33 | 21.19 | 43.42 | 91.96 | 201.34 | - | - |
| Local Attention | 0.51 | 0.60 | 0.78 | 2.01 | 6.23 | 12.52 | 25.07 | 50.50 | 102.18 | - |
| Linformer | 0.47 | 0.37 | 0.49 | 0.52 | 1.37 | 2.65 | 5.12 | 10.13 | 20.25 | 44.16 |
| Smyrf | 2.12 | 2.01 | 3.15 | 5.97 | 11.83 | 23.36 | 46.48 | 92.72 | - | - |
| LSFormer | 1.28 | 1.33 | 1.51 | 3.39 | 11.40 | 22.54 | 44.96 | 89.85 | 179.73 | - |
| Block Sparse | 1.03 | 1.00 | 1.72 | 2.39 | 5.96 | 17.88 | - | - | - | - |
| Longformer | 1.02 | 1.03 | 1.03 | 1.73 | 5.10 | 11.63 | 34.22 | - | - | - |
| BigBird | 0.99 | 1.03 | 1.01 | 1.58 | 5.36 | 12.27 | 35.56 | - | - | - |
| **FlashAttention** | **0.10** | **0.10** | **0.22** | **0.83** | **2.81** | **10.38** | **41.63** | **167.01** | **668.74** | **2678.11** |
| Block-Sparse FlashAttention | 0.54 | 0.51 | 0.68 | 0.61 | **0.67** | **1.10** | **1.89** | **3.71** | **7.18** | **14.41** |

**Table 16** (p. 33): Backward pass runtime (ms) of various exact/approximate/sparse attention mechanisms by sequence length, **with dropout**. Best in **bold**, second best underlined.

| Attention Method | 128 | 256 | 512 | 1024 | 2048 | 4096 | 8192 | 16384 | 32768 | 65536 |
|---|---|---|---|---|---|---|---|---|---|---|
| PyTorch Attention | 0.44 | 0.35 | 0.90 | 2.94 | 10.77 | 41.67 | - | - | - | - |
| Megatron | 0.28 | 0.33 | 0.92 | 2.94 | 10.80 | - | - | - | - | - |
| Reformer | 2.24 | 4.34 | 8.39 | 16.62 | 33.02 | 65.77 | 131.52 | - | - | - |
| Local Attention | 0.51 | 0.58 | 1.41 | 3.71 | 12.96 | 25.98 | 51.94 | 103.72 | 207.78 | - |
| Linformer | 0.84 | 0.74 | 0.79 | 0.85 | 2.28 | 4.37 | 8.66 | 17.02 | 33.78 | - |
| Smyrf | 1.27 | 2.56 | 4.90 | 9.66 | 19.16 | 38.13 | 76.17 | 152.39 | - | - |
| LSFormer | 1.67 | 1.77 | 3.03 | 7.52 | 20.10 | 39.13 | 76.35 | 150.83 | - | - |
| Block Sparse | 1.27 | 1.36 | 2.15 | 3.04 | 7.27 | 21.18 | - | - | - | - |
| Longformer | 1.28 | 1.34 | 1.38 | 1.98 | 5.24 | 10.74 | 25.95 | - | - | - |
| BigBird | 1.48 | 1.47 | 1.50 | 1.81 | 5.57 | 11.38 | 27.43 | - | - | - |
| **FlashAttention** | **0.15** | **0.18** | **0.58** | **1.86** | **6.50** | **26.21** | **104.27** | **416.10** | **1661.92** | **6643.01** |
| Block-Sparse FlashAttention | 0.17 | **0.17** | **0.17** | **0.40** | **1.10** | **2.04** | **4.43** | **9.33** | **18.28** | **37.31** |

**Table 17** (p. 33): Forward pass + backward pass runtime (ms) of various exact/approximate/sparse attention mechanisms by sequence length, **with dropout**. Best in **bold**, second best underlined.

| Attention Method | 128 | 256 | 512 | 1024 | 2048 | 4096 | 8192 | 16384 | 32768 | 65536 |
|---|---|---|---|---|---|---|---|---|---|---|
| PyTorch Attention | 0.66 | 0.67 | 1.43 | 4.82 | 17.47 | 67.29 | - | - | - | - |
| Megatron | 0.88 | 0.90 | 1.49 | 4.73 | 17.41 | - | - | - | - | - |
| Reformer | 4.06 | 7.28 | 13.68 | 26.98 | 54.27 | 109.39 | 223.80 | - | - | - |
| Local Attention | 1.09 | 1.40 | 1.99 | 5.61 | 19.23 | 38.62 | 77.30 | 154.63 | 311.12 | - |
| Linformer | 1.31 | 1.21 | 1.30 | 1.39 | 3.73 | 7.15 | 14.05 | 27.69 | 55.00 | - |
| Smyrf | 3.00 | 4.37 | 8.05 | 15.66 | 31.04 | 61.64 | 123.04 | 245.65 | - | - |
| LSFormer | 3.07 | 3.17 | 4.31 | 10.89 | 31.54 | 61.78 | 121.56 | 240.94 | - | - |
| Block Sparse | 2.54 | 2.54 | 3.71 | 5.44 | 13.29 | 39.19 | - | - | - | - |
| Longformer | 2.47 | 2.49 | 2.51 | 3.10 | 10.39 | 22.49 | 60.44 | - | - | - |
| BigBird | 2.51 | 2.49 | 2.52 | 3.40 | 10.97 | 23.89 | 63.28 | - | - | - |
| **FlashAttention** | **0.35** | **0.36** | **0.80** | **2.52** | **9.16** | **36.70** | **146.13** | **583.45** | **2332.01** | **9323.63** |
| Block-Sparse FlashAttention | 0.91 | 0.83 | 0.94 | **0.92** | **1.83** | **3.50** | **7.02** | **13.56** | **26.71** | **53.92** |

---
[p. 34 continued]

**Table 18** (p. 34): Forward pass runtime (ms) of various exact/approximate/sparse attention mechanisms by sequence length. Best in **bold**, second best underlined.

| Attention Method | 128 | 256 | 512 | 1024 | 2048 | 4096 | 8192 | 16384 | 32768 | 65536 |
|---|---|---|---|---|---|---|---|---|---|---|
| PyTorch Attention | 0.21 | 0.22 | 0.43 | 1.27 | 4.32 | 16.47 | 67.77 | - | - | - |
| Megatron | 0.24 | 0.26 | 0.42 | 1.33 | 4.28 | - | - | - | - | - |
| Reformer | 1.77 | 2.82 | 5.01 | 9.74 | 20.03 | 41.11 | 87.39 | 192.40 | - | - |
| Local Attention | 0.48 | 0.57 | 0.80 | 1.90 | 5.76 | 11.56 | 23.13 | 46.65 | 94.74 | - |
| Linformer | 0.46 | 0.36 | 0.45 | **0.50** | 1.09 | 2.09 | 4.01 | 7.90 | 15.70 | 35.40 |
| Smyrf | 1.94 | 1.96 | 3.01 | 5.69 | 11.26 | 22.23 | 44.21 | 88.22 | - | - |
| LSFormer | 1.21 | 1.34 | 1.34 | 3.31 | 11.01 | 21.71 | 43.27 | 86.32 | 172.85 | - |
| Block Sparse | 0.96 | 1.04 | 1.66 | 2.16 | 5.41 | 16.15 | - | - | - | - |
| Longformer | 0.99 | 0.98 | 0.99 | 1.56 | 4.79 | 11.07 | 32.98 | - | - | - |
| BigBird | 0.96 | 1.02 | 1.02 | 1.48 | 5.05 | 11.59 | 34.16 | - | - | - |
| **FlashAttention** | **0.08** | **0.09** | **0.18** | 0.68 | **2.40** | **8.42** | **35.54** | **134.03** | **535.95** | **2147.05** |
| Block-Sparse FlashAttention | 0.56 | 0.52 | 0.63 | **0.61** | **0.61** | **0.96** | **1.69** | **3.02** | **5.69** | **11.77** |

**Table 19** (p. 34): Backward pass runtime (ms) of various exact/approximate/sparse attention mechanisms by sequence length. Best in **bold**, second best underlined.

| Attention Method | 128 | 256 | 512 | 1024 | 2048 | 4096 | 8192 | 16384 | 32768 | 65536 |
|---|---|---|---|---|---|---|---|---|---|---|
| PyTorch Attention | 0.29 | 0.29 | 0.78 | 2.44 | 8.82 | 33.87 | - | - | - | - |
| Megatron | 0.29 | 0.30 | 0.80 | 2.59 | 8.86 | - | - | - | - | - |
| Reformer | 2.18 | 4.21 | 8.14 | 16.12 | 32.02 | 63.84 | 127.60 | - | - | - |
| Local Attention | 0.51 | 0.64 | 1.28 | 3.60 | 12.52 | 25.08 | 50.22 | 100.23 | 200.66 | - |
| Linformer | 0.69 | 0.76 | 0.69 | 0.80 | 2.01 | 3.88 | 7.67 | 15.04 | 30.11 | 63.15 |
| Smyrf | 1.24 | 2.49 | 4.77 | 9.42 | 18.65 | 37.12 | 74.15 | 148.35 | - | - |
| LSFormer | 1.68 | 1.61 | 3.02 | 7.40 | 19.72 | 38.27 | 74.89 | 147.99 | - | - |
| Block Sparse | 1.24 | 1.25 | 2.04 | 2.91 | 6.78 | 19.67 | - | - | - | - |
| Longformer | 1.27 | 1.23 | 1.24 | 1.85 | 4.99 | 10.21 | 24.89 | - | - | - |
| BigBird | 1.43 | 1.50 | 1.44 | 1.69 | 5.25 | 10.86 | 26.26 | - | - | - |
| **FlashAttention** | **0.11** | **0.12** | **0.52** | **1.62** | **5.45** | **21.57** | **84.75** | **336.00** | **1338.56** | **5343.19** |
| Block-Sparse FlashAttention | **0.11** | **0.12** | **0.16** | **0.38** | **1.20** | **2.34** | **4.69** | **9.10** | **18.74** | **37.04** |

**Table 20** (p. 34): Forward pass + backward pass runtime (ms) of various exact/approximate/sparse attention mechanisms by sequence length. Best in **bold**, second best underlined.

| Attention Method | 128 | 256 | 512 | 1024 | 2048 | 4096 | 8192 | 16384 | 32768 | 65536 |
|---|---|---|---|---|---|---|---|---|---|---|
| PyTorch Attention | 0.67 | 0.70 | 1.18 | 3.67 | 13.22 | 50.44 | - | - | - | - |
| Megatron | 0.74 | 0.65 | 1.23 | 3.80 | 13.21 | - | - | - | - | - |
| Reformer | 3.93 | 7.01 | 13.15 | 25.89 | 52.09 | 105.00 | 215.13 | - | - | - |
| Local Attention | 1.09 | 1.27 | 1.99 | 5.38 | 18.32 | 36.77 | 73.67 | 147.29 | 296.35 | - |
| Linformer | 1.31 | 1.25 | 1.30 | 1.29 | 3.20 | 6.10 | 11.93 | 23.39 | 46.72 | 100.52 |
| Smyrf | 2.98 | 4.23 | 7.78 | 15.12 | 29.96 | 59.45 | 118.60 | 237.02 | - | - |
| LSFormer | 3.03 | 3.05 | 4.26 | 10.70 | 30.77 | 60.15 | 118.33 | 234.94 | - | - |
| Block Sparse | 2.39 | 2.40 | 3.31 | 5.02 | 12.25 | 35.94 | - | - | - | - |
| Longformer | 2.36 | 2.34 | 2.38 | 2.94 | 9.83 | 21.35 | 58.12 | - | - | - |
| BigBird | 2.35 | 2.35 | 2.37 | 3.25 | 10.36 | 22.57 | 60.63 | - | - | - |
| **FlashAttention** | **0.31** | **0.31** | **0.73** | **2.29** | **7.64** | **30.09** | **118.50** | **470.51** | **1876.08** | **7492.85** |
| Block-Sparse FlashAttention | 0.74 | 0.77 | 0.82 | **0.88** | **1.71** | **3.21** | **6.56** | **12.60** | **24.93** | **50.39** |

**Table 21** (p. 34): Memory usage (MB) of various exact/approximate/sparse attention mechanisms by sequence length. Best in **bold**, second best underlined.

| Attention Method | 128 | 256 | 512 | 1024 | 2048 | 4096 | 8192 | 16384 | 32768 | 65536 |
|---|---|---|---|---|---|---|---|---|---|---|
| PyTorch Attention | 36 | 104 | 336 | 1184 | 4416 | 17024 | - | - | - | - |
| Megatron | 36 | 104 | 336 | 1184 | 4416 | - | - | - | - | - |
| Reformer | 377 | 754 | 1508 | 3016 | 6033 | 12067 | 24134 | - | - | - |
| Local Attention | 53 | 110 | 232 | 592 | 1696 | 3392 | 6784 | 13568 | 27136 | - |
| Linformer | 25 | 52 | 114 | 287 | 832 | 1652 | 3292 | 6572 | 13132 | 26252 |
| Smyrf | 217 | 434 | 868 | 1737 | 3474 | 6947 | 13894 | 27788 | - | - |
| LSFormer | 72 | 152 | 333 | 796 | 2540 | 5068 | 10125 | 20240 | - | - |
| Block Sparse | 33 | 82 | 228 | 408 | 910 | 2401 | - | - | - | - |
| Longformer | 30 | 61 | 124 | 277 | 681 | 1370 | 2748 | - | - | - |
| BigBird | 33 | 66 | 131 | 294 | 708 | 1431 | 2872 | - | - | - |
| **FlashAttention** | **22** | **44** | **104** | **209** | **418** | **836** | **1672** | **3344** | **6688** | **13376** |
| Block-Sparse FlashAttention | **22** | 44 | **104** | **209** | **418** | **836** | **1672** | **3344** | **6690** | 13384 |
