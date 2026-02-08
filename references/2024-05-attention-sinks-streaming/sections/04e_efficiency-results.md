# 4.5 Efficiency Results [p. 9]

StreamingLLM's decoding latency and memory usage are benchmarked against the sliding window with re-computation, which is the only baseline with acceptable quality. Both methods are implemented using the Huggingface Transformers library (Wolf et al., 2020) and tested on a single NVIDIA A6000 GPU using the Llama-2-7B and Llama-2-13B models. [p. 9]

**Figure 10** (p. 9): "Comparison of per-token decoding latency and memory usage between the sliding window approach with re-computation baseline and StreamingLLM, plotted against the cache size (attention window size) on the X-axis. StreamingLLM delivers a remarkable speedup of up to 22.2x per token and retains a memory footprint similar to the re-computation baseline."
Four panels (Llama-2-7B Latency, Llama-2-7B Memory, Llama-2-13B Latency, Llama-2-13B Memory). Cache sizes on X-axis: 256, 512, 1024, 2048, 4096.

Llama-2-7B Latency (ms):

| Cache size | Sliding Window w/ Re-comp | StreamingLLM |
|---|---|---|
| 256 | 83 | 31 |
| 512 | 103 | 35 |
| 1024 | 223 | 45 |
| 2048 | 523 | 75 |
| 4096 | 1411 | 145 |

Llama-2-7B Memory (GB):

| Cache size | Sliding Window w/ Re-comp | StreamingLLM |
|---|---|---|
| 256 | 13 | 13 |
| 512 | 13 | 13 |
| 1024 | 14 | 14 |
| 2048 | 16 | 16 |
| 4096 | 21 | 19 |

Llama-2-13B Latency (ms):

| Cache size | Sliding Window w/ Re-comp | StreamingLLM |
|---|---|---|
| 256 | 99 | 48 |
| 512 | 109 | 69 |
| 1024 | 361 | 110 |
| 2048 | 860 | 175 |
| 4096 | 2355 | [unclear: bar label partially visible; ~106 implied by 22.2x speedup claim] |

Llama-2-13B Memory (GB):

| Cache size | Sliding Window w/ Re-comp | StreamingLLM |
|---|---|---|
| 256 | 25 | 25 |
| 512 | 28 | 26 |
| 1024 | 26 | 27 |
| 2048 | 29 | 29 |
| 4096 | 36 | 34 |

As the cache size increases, StreamingLLM's decoding speed has a linear growth. The sliding window with re-computation baseline has a quadratic rise in decoding latency. StreamingLLM achieves an impressive speedup, reaching up to 22.2x per token. Despite its reduced latency, StreamingLLM sustains a memory footprint consistent with the re-computation baseline. [p. 9]
