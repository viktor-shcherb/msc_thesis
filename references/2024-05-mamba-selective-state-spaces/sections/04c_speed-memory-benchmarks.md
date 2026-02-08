# 4.5 Speed and Memory Benchmarks [p. 15]

[p. 15]

The authors benchmark the speed of the SSM scan operation (state expansion $N = 16$), as well as the end-to-end inference throughput of Mamba, in Figure 8. Their efficient SSM scan is faster than the best attention implementation they know of (FlashAttention-2 (Dao 2024)) beyond sequence length 2K, and up to 20-40x faster than a standard scan implementation in PyTorch. Mamba achieves 4-5x higher inference throughput than a Transformer of similar size, because without the KV cache it can use much higher batch sizes. For example, a Mamba-6.9B (untrained) would have higher inference throughput than a 5x smaller Transformer-1.3B. Details in Appendix E.5, which additionally includes a benchmark of memory consumption. [p. 15]

## Figures

**Figure 8** (p. 15): "(**Efficiency Benchmarks.**) (*Left*) Training: our efficient scan is 40x faster than a standard implementation. (*Right*) Inference: as a recurrent model, Mamba can achieve 5x higher throughput than Transformers."

The figure contains two plots:
- **Left plot** ("Scan vs Convolution vs Attention time (A100 80GB PCIe)"): x-axis is Sequence Length (log scale, from 512 to 512k), y-axis is Time in ms (log scale, from 0.1 to ~1000). Lines shown: FlashAttention-2 (blue), Convolution (orange), Scan (PyTorch) (green), Scan (ours) (red), with OOM markers (x) for methods that run out of memory. The efficient scan (red) remains fast and flat across all sequence lengths, while FlashAttention-2 grows quadratically. Scan (PyTorch) is 20-40x slower than the efficient scan. FlashAttention-2 goes OOM at the longest sequence lengths.
- **Right plot** ("Inference Throughput on A100 80GB (prompt length 2048)"): x-axis is Batch Size (from 1 to 128), y-axis is Throughput (tokens/s). Bar chart showing: Mamba 1.4B (blue), Transformer 1.3B (orange), Mamba 6.9B (green), Transformer 6.7B (red). Mamba models consistently achieve higher throughput than Transformers, with the gap widening at higher batch sizes. Mamba 1.4B achieves the highest throughput overall (over 1500 tokens/s at batch size 128). Even Mamba 6.9B achieves higher throughput than Transformer 1.3B at most batch sizes.
