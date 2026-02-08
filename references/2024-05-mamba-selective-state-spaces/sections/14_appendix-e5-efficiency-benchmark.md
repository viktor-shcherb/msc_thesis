# E.5 Efficiency Benchmark [p. 35–36]

## Scan Operation

[p. 35–36]

The core operation of selective SSMs, which is the parallel scan (Section 3.3), is compared against convolution and attention, measured on an A100 80GB PCIe GPU. Note that these do not include the cost of other operations outside of this core operation, such as computing the convolutional kernel in global-convolution models, or computing the QKV projections in attention.

As a baseline, a standard parallel scan in PyTorch with no kernel fusion is implemented. This requires materializing the parameters $\overline{A}$, $\overline{B}$, $C$ in HBM.

The authors' scan implementation fuses the discretization step and the parallel scan, avoiding the cost of materializing all the large parameters in HBM.

For convolution, the standard implementation in PyTorch is used, which separately performs FFTs on the inputs and the filters, multiplies them in frequency domain, then performs an inverse FFT to obtain the result. The theoretical complexity is $O(L \log(L))$ for sequence length $L$. [p. 36]

For attention, the fastest implementation the authors are aware of (FlashAttention-2 (Dao 2024)) is compared against, with causal mask. Note that FlashAttention-2 with causal mask is about $1.7\times$ faster than without causal mask, since approximately only half of the attention entries are computed.

Batch size of 1 is used and the sequence length is increased from $2^9 = 512$, $2^{10} \approx 1K$, $2^{11} \approx 2K$, up to $2^{19} \approx 500K$ (some of the baselines run out of memory before reaching 500K). A model dimension of $D = 1024$ and state dimension $N = 16$ are used. Measurements are with BF16 inputs, which is the data type most commonly used for large scale training.

## End-to-end Inference

[p. 36]

The inference throughput of a Mamba 1.4B model and an untrained Mamba 6.9B model is measured, against a standard Transformer (GPT3 architecture) at 1.3B and 6.7B size. The standard Transformer implementation in the Huggingface `transformers` library is used.

The prompt length is set to 2048 and the generation length to 128. The batch size is varied from 1, 2, 4, 8, 16, 32, 64, to 128, and the time taken to generate 128 tokens is measured. The throughput (tokens/s) is calculated as batch size $\times$ 128 / time taken. Measurements are repeated 3 times and the average is taken. Measurements are done on an A100 80GB PCIe GPU.

## Memory Benchmark

[p. 36]

The memory usage simply scales proportionally to the size of the activation tensors, as with most deep sequence models. Measurements of the training memory requirements of 125M models on 1 A100 80GB GPU are reported. Each batch consists of sequences of length 2048. The comparison is against the most memory-efficient Transformer implementation the authors are aware of (with kernel fusion from `torch.compile` and with FlashAttention-2).

**Table 15:** (Memory benchmark.) Mamba's memory footprint is comparable to the most optimized Transformer. Results for 125M models. [p. 36]

| Batch size | Transformer (w/ FlashAttention-2) | Mamba |
|------------|----------------------------------|-------|
| 1 | 4.6GB | 4.8GB |
| 2 | 5.2GB | 5.8GB |
| 4 | 6.9GB | 7.3GB |
| 8 | 11.5GB | 12.3GB |
| 16 | 20.7GB | 23.1GB |
| 32 | 34.5GB | 38.2GB |

Table 15 shows that Mamba's memory requirement is comparable to a similar-sized Transformer with an extremely optimized implementation, and the authors expect further improvement in Mamba's memory footprint in the future.
