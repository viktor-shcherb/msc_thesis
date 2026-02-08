# 4 Empirical Validation [p. 9-11]

[p. 9-10] The impact of using FlashAttention-2 to train Transformer models is evaluated along two axes:

- **Benchmarking attention.** The runtime of FlashAttention-2 is measured across different sequence lengths and compared to a standard implementation in PyTorch, FlashAttention, and FlashAttention in Triton. FlashAttention-2 is confirmed to be 1.7-3.0x faster than FlashAttention, 1.3-2.5x faster than FlashAttention in Triton, and 3-10x faster than a standard attention implementation. FlashAttention-2 reaches up to 230 TFLOPs/s, 73% of the theoretical maximum TFLOPs/s on A100 GPUs. [p. 10]

- **End-to-end training speed.** When used end-to-end to train GPT-style models of size 1.3B and 2.7B on sequence lengths either 2k or 8k, FlashAttention-2 yields up to 1.3x speedup compared to FlashAttention and 2.8x speedup compared to a baseline without FlashAttention. FlashAttention-2 reaches up to 225 TFLOPs/s (72% model FLOPs utilization) per A100 GPU. [p. 10]

## 4.1 Benchmarking Attention [p. 10-11]

[p. 10] The runtime of different attention methods is measured on an A100 80GB SXM4 GPU for different settings (without / with causal mask, head dimension 64 or 128). Results are reported in Fig. 4, Fig. 5, and Fig. 6, showing that FlashAttention-2 is around 2x faster than FlashAttention and FlashAttention in xformers (the "cutlass" implementation). FlashAttention-2 is around 1.3-1.5x faster than FlashAttention in Triton in the forward pass and around 2x faster in the backward pass. Compared to a standard attention implementation in PyTorch, FlashAttention-2 can be up to 10x faster.

**Benchmark setting:** [p. 10] Sequence length is varied from 512, 1k, ..., 16k, and batch size is set so that the total number of tokens is 16k. Hidden dimension is set to 2048, and head dimension to be either 64 or 128 (i.e., 32 heads or 16 heads). To calculate the FLOPs of the forward pass:

$$4 \cdot \text{seqlen}^2 \cdot \text{head dimension} \cdot \text{number of heads}$$

With causal mask, this number is divided by 2 to account for the fact that approximately only half of the entries are calculated. To get the FLOPs of the backward pass, the forward pass FLOPs are multiplied by 2.5 (since there are 2 matmuls in the forward pass and 5 matmuls in the backward pass, due to recomputation). [p. 10]

**Figure 4** (p. 10): "Attention forward + backward speed on A100 GPU"

The figure contains four bar chart subplots showing speed in TFLOPs/s (y-axis) across sequence lengths 512, 1k, 2k, 4k, 8k, 16k (x-axis), comparing PyTorch, FlashAttention, xformers, FlashAttention Triton, and FlashAttention-2.

(a) Without causal mask, head dimension 64:

| Seq len | PyTorch | FlashAttention | xformers | FA Triton | FA-2 |
|---------|---------|----------------|----------|-----------|------|
| 512     | 36      | 91             | 90       | 58        | 132  |
| 1k      | 40      | 102            | 73       | 76        | 162  |
| 2k      | 43      | 104            | 98       | 102       | 171  |
| 4k      | 43      | 108            | 101      | 104       | 175  |
| 8k      | OOM     | 110            | 101      | 73        | 176  |
| 16k     | OOM     | 46             | 46       | 110       | 176  |

(b) Without causal mask, head dimension 128:

| Seq len | PyTorch | FlashAttention | xformers | FA Triton | FA-2 |
|---------|---------|----------------|----------|-----------|------|
| 512     | 53      | 74             | 78       | 57        | 131  |
| 1k      | 63      | 91             | 85       | 75        | 181  |
| 2k      | 63      | 95             | 90       | 79        | 196  |
| 4k      | 63      | 95             | 86       | 82        | 201  |
| 8k      | OOM     | 98             | 95       | 83        | 203  |
| 16k     | OOM     | 45             | 95       | 83        | 203  |

(c) With causal mask, head dimension 64:

| Seq len | PyTorch | FlashAttention | xformers | FA Triton | FA-2 |
|---------|---------|----------------|----------|-----------|------|
| 512     | 15      | 58             | 59       | 38        | 88   |
| 1k      | 16      | 70             | 60       | 75        | 119  |
| 2k      | 17      | 77             | 79       | 68        | 140  |
| 4k      | 18      | 87             | 78       | 73        | 158  |
| 8k      | OOM     | 92             | 92       | 80        | 165  |
| 16k     | OOM     | 18             | 57       | 97        | 171  |

(d) With causal mask, head dimension 128:

| Seq len | PyTorch | FlashAttention | xformers | FA Triton | FA-2 |
|---------|---------|----------------|----------|-----------|------|
| 512     | 23      | 53             | 58       | 28        | 99   |
| 1k      | 28      | 72             | 62       | 61        | 131  |
| 2k      | 32      | 81             | 76       | 74        | 155  |
| 4k      | 32      | 87             | 80       | 80        | 182  |
| 8k      | OOM     | 91             | 92       | 83        | 189  |
| 16k     | OOM     | 19             | 31       | 92        | 189  |

**Figure 5** (p. 11): "Attention forward speed on A100 GPU"

The figure contains four bar chart subplots showing forward-pass-only speed in TFLOPs/s (y-axis) across sequence lengths 512, 1k, 2k, 4k, 8k, 16k (x-axis), comparing the same five implementations.

(a) Without causal mask, head dimension 64:

| Seq len | PyTorch | FlashAttention | xformers | FA Triton | FA-2 |
|---------|---------|----------------|----------|-----------|------|
| 512     | 29      | 91             | 94       | 94        | 128  |
| 1k      | 34      | 94             | 97       | 100       | 149  |
| 2k      | 35      | 99             | 97       | 152       | 193  |
| 4k      | 37      | 104            | 100      | 152       | 192  |
| 8k      | OOM     | 106            | 104      | 152       | 192  |
| 16k     | OOM     | 37             | 37       | 152       | 192  |

Note: At longer sequence lengths in 5(a), FA Triton (~152 TFLOPs/s) and FA-2 (~192 TFLOPs/s) are the dominant methods, with FA-2 approximately 1.3x faster. At 16k, PyTorch, FlashAttention, and xformers show greatly reduced throughput (possibly OOM or memory-limited).

(b) Without causal mask, head dimension 128:

| Seq len | PyTorch | FlashAttention | xformers | FA Triton | FA-2 |
|---------|---------|----------------|----------|-----------|------|
| 512     | 42      | 69             | 56       | 102       | 122  |
| 1k      | 60      | 69             | 63       | 71        | 157  |
| 2k      | 63      | 71             | 67       | 71        | 200  |
| 4k      | 73      | 122            | 120      | 122       | 224  |
| 8k      | OOM     | 122            | 122      | 160       | 222  |
| 16k     | OOM     | 73             | 122      | 163       | 225  |

(c) With causal mask, head dimension 64:

| Seq len | PyTorch | FlashAttention | xformers | FA Triton | FA-2 |
|---------|---------|----------------|----------|-----------|------|
| 512     | 10      | 78             | 82       | 71        | 115  |
| 1k      | 10      | 82             | 89       | 88        | 131  |
| 2k      | 10      | 89             | 92       | 91        | 167  |
| 4k      | 10      | 91             | 94       | 93        | 177  |
| 8k      | OOM     | 94             | 93       | 106       | 181  |
| 16k     | OOM     | 10             | 10       | 106       | 185  |

(d) With causal mask, head dimension 128:

| Seq len | PyTorch | FlashAttention | xformers | FA Triton | FA-2 |
|---------|---------|----------------|----------|-----------|------|
| 512     | 15      | 49             | 59       | 63        | 108  |
| 1k      | 18      | 63             | 68       | 70        | 126  |
| 2k      | 19      | 88             | 76       | 115       | 133  |
| 4k      | 19      | 80             | 91       | 115       | 148  |
| 8k      | OOM     | 70             | 92       | 111       | 148  |
| 16k     | OOM     | 19             | 71       | 111       | 148  |

**Figure 6** (p. 12): "Attention backward speed on A100 GPU"

The figure contains four bar chart subplots showing backward-pass-only speed in TFLOPs/s (y-axis) across sequence lengths 512, 1k, 2k, 4k, 8k, 16k (x-axis), comparing the same five implementations.

(a) Without causal mask, head dimension 64:

| Seq len | PyTorch | FlashAttention | xformers | FA Triton | FA-2 |
|---------|---------|----------------|----------|-----------|------|
| 512     | 39      | 91             | 90       | 32        | 120  |
| 1k      | 43      | 81             | 82       | 48        | 152  |
| 2k      | 44      | 87             | 86       | 88        | 163  |
| 4k      | 49      | 88             | 87       | 112       | 169  |
| 8k      | OOM     | 31             | 31       | 122       | 170  |
| 16k     | OOM     | 88             | 87       | 113       | 170  |

(b) Without causal mask, head dimension 128:

| Seq len | PyTorch | FlashAttention | xformers | FA Triton | FA-2 |
|---------|---------|----------------|----------|-----------|------|
| 512     | 39      | 78             | 58       | 56        | 114  |
| 1k      | 73      | 73             | 74       | 77        | 175  |
| 2k      | 84      | 86             | 88       | 84        | 187  |
| 4k      | 89      | 89             | 87       | 89        | 193  |
| 8k      | OOM     | 90             | 90       | 97        | 196  |
| 16k     | OOM     | 81             | 82       | 91        | 196  |

(c) With causal mask, head dimension 64:

| Seq len | PyTorch | FlashAttention | xformers | FA Triton | FA-2 |
|---------|---------|----------------|----------|-----------|------|
| 512     | 19      | 58             | 46       | 39        | 81   |
| 1k      | 21      | 70             | 68       | 40        | 111  |
| 2k      | 24      | 76             | 71       | 85        | 149  |
| 4k      | 23      | 53             | 53       | 67        | 160  |
| 8k      | OOM     | 26             | 26       | 98        | 166  |
| 16k     | OOM     | 68             | 68       | 98        | 166  |

(d) With causal mask, head dimension 128:

| Seq len | PyTorch | FlashAttention | xformers | FA Triton | FA-2 |
|---------|---------|----------------|----------|-----------|------|
| 512     | 30      | 59             | 33       | 43        | 90   |
| 1k      | 37      | 65             | 71       | 58        | 122  |
| 2k      | 43      | 75             | 80       | 80        | 145  |
| 4k      | 48      | 83             | 83       | 53        | 165  |
| 8k      | OOM     | 40             | 63       | 89        | 175  |
| 16k     | OOM     | 87             | 84       | 89        | 186  |

[p. 11] Just running the same implementation on H100 GPUs (using no special instructions to make use of new features such as TMA and 4th-gen Tensor Cores), up to 335 TFLOPs/s is obtained (Fig. 7). It is expected that by using new instructions, another 1.5x-2x speedup can be obtained on H100 GPUs. This is left to future work.

**Figure 7** (p. 13): "Attention forward + backward speed on H100 GPU"

The figure contains four bar chart subplots showing forward + backward speed in TFLOPs/s (y-axis) across sequence lengths 512, 1k, 2k, 4k, 8k, 16k (x-axis), comparing PyTorch, FlashAttention, and FlashAttention-2 on an H100 80GB SXM5 GPU.

(a) Without causal mask, head dimension 64:

| Seq len | PyTorch | FlashAttention | FA-2 |
|---------|---------|----------------|------|
| 512     | 62      | 157            | 215  |
| 1k      | 72      | 136            | 254  |
| 2k      | 81      | 163            | 274  |
| 4k      | 85      | 161            | 288  |
| 8k      | OOM     | 166            | 294  |
| 16k     | OOM     | 188            | 295  |

(b) Without causal mask, head dimension 128:

| Seq len | PyTorch | FlashAttention | FA-2 |
|---------|---------|----------------|------|
| 512     | 93      | 127            | 248  |
| 1k      | 122     | 143            | 320  |
| 2k      | 127     | 143            | 326  |
| 4k      | 131     | 160            | 315  |
| 8k      | OOM     | 167            | 318  |
| 16k     | OOM     | 139            | 318  |

(c) With causal mask, head dimension 64:

| Seq len | PyTorch | FlashAttention | FA-2 |
|---------|---------|----------------|------|
| 512     | 26      | 104            | 141  |
| 1k      | 29      | 123            | 192  |
| 2k      | 31      | 136            | 232  |
| 4k      | 31      | 138            | 257  |
| 8k      | 32      | 149            | 273  |
| 16k     | 32      | 156            | 284  |

(d) With causal mask, head dimension 128:

| Seq len | PyTorch | FlashAttention | FA-2 |
|---------|---------|----------------|------|
| 512     | 40      | 98             | 163  |
| 1k      | 50      | 126            | 221  |
| 2k      | 57      | 106            | 265  |
| 4k      | 61      | 104            | 294  |
| 8k      | 63      | 135            | 308  |
| 16k     | 63      | 137            | 328  |

## 4.2 End-to-end Performance [p. 11]

[p. 11-12] The training throughput of GPT-style models with either 1.3B or 2.7B parameters is measured on 8xA100 80GB SXM. As shown in Table 1, FlashAttention-2 yields 2.8x speedup compared to a baseline without FlashAttention and 1.3x speedup compared to FlashAttention, reaching up to 225 TFLOPs/s per A100 GPU.

**Table 1** (p. 12): "Training speed (TFLOPs/s/GPU) of GPT-style models on 8xA100 GPUs. FlashAttention-2 reaches up to 225 TFLOPs/s (72% model FLOPs utilization). We compare against a baseline running without FlashAttention."

| Model               | Without FlashAttention | FlashAttention | FlashAttention-2 |
|---------------------|------------------------|----------------|------------------|
| GPT3-1.3B 2k context | 142 TFLOPs/s          | 189 TFLOPs/s   | 196 TFLOPs/s     |
| GPT3-1.3B 8k context | 72 TFLOPs/s           | 170 TFLOPs/s   | 220 TFLOPs/s     |
| GPT3-2.7B 2k context | 149 TFLOPs/s          | 189 TFLOPs/s   | 205 TFLOPs/s     |
| GPT3-2.7B 8k context | 80 TFLOPs/s           | 175 TFLOPs/s   | 225 TFLOPs/s     |

The FLOPs are calculated by the formula, following Megatron-LM [16] (and many other papers and libraries):

$$6 \cdot \text{seqlen} \cdot \text{number of params} + 12 \cdot \text{number of layers} \cdot \text{hidden dim} \cdot \text{seqlen}^2$$

The first term accounts for the FLOPs due to weight-input multiplication, and the second term accounts for the FLOPs due to attention. One can argue that the second term should be halved, as with causal mask only approximately half the number of elements in attention need to be computed. The authors choose to follow the formula from the literature (without dividing the attention FLOPs by 2) for consistency.
