# Speed and Memory Benchmarks [p. 14]

### Figure 6: Memory Usage vs. Sequence Length [p. 14]

**Figure 6:** Memory Usage vs. Sequence Length (A100 80GB)

The figure is a bar chart showing memory usage (GB) on y-axis (0 to 35) versus sequence length on x-axis (512, 1024, 2048, 4096, 8192, 16384). Three model types are shown:
- Finch (blue bars)
- Mamba (orange bars)
- Flash Attention v2 (beige bars)

Values shown:
- At 512: Finch 0.5, Mamba 0.8, Flash Attention 1
- At 1024: Finch 1.5, Mamba 1.7, Flash Attention 2.1
- At 2048: Finch 2.9, Mamba 3.5, Flash Attention 4.1
- At 4096: Finch 5.9, Mamba 6.9, Flash Attention 8.2
- At 8192: Finch 11.8, Mamba 13.9, Flash Attention 16.4
- At 16384: Finch 23.6, Mamba 27.7, Flash Attention 32.8

Memory usage increases with sequence length, with Finch consistently using less memory than Mamba, which uses less than Flash Attention v2.

### Figure 7: Time vs. Sequence Length [p. 14]

**Figure 7:** Time vs. Sequence Length (A100 80GB)

The figure is a line chart showing time (ms) on y-axis (0 to 800) versus sequence length on x-axis (0 to 16k). Four lines are plotted:
- Finch (blue solid line with squares)
- Flash Attention v2 (orange solid line with circles)
- Mamba (red solid line with diamonds)
- Mamba 2x (red dotted line with x markers)

Time increases with sequence length. Flash Attention v2 shows the steepest increase, reaching ~800ms at 16k. Mamba 2x reaches ~270ms, Mamba reaches ~250ms, and Finch shows the most efficient scaling, reaching ~180ms at 16k sequence length.

## Main Text

[p. 14] We compare the speed and memory utilization of the Attention-like kernels for Finch, Mamba^2, and Flash Attention^3 (Dao, 2023) in Figures 6 and 7. For all benchmarks, we use a batch size of 8, a model dimension of 4096, and a head size of 64 for both Flash Attention and Finch. For Mamba, we employ a state dimension of 16, a model dimension of 8192, to mimic Mamba's usage of an expansion factor of 2. Our findings indicate that Finch's speed in training scales linearly with respect to sequence length, exhibiting similar scaling to Mamba. We find Finch

^2 We also plot Mamba 2x which uses 2 runs through the Mamba kernel instead of one. This is done to mimic the usage of twice the number of layers in Mamba vs Finch and Transformers

^3 We use the PyTorch implementation of Flash Attention v2

---

[p. 14–15 continued]

is significantly faster than Flash Attention for sequence lengths beyond 4k, being around 4.2x faster for a sequence length of 16k. Furthermore, Finch consistently outperforms Mamba and Flash Attention in terms of memory usage, using 40% and 17% less memory usage than Flash Attention and Mamba respectively. Further optimization of our Finch CUDA implementation, including algorithmic improvements, and optimizations, could lead to speed increases and greater parallelization. However, this optimization is left for future work.
