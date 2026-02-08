# 6 Inference [p. 51–54]

[p. 51] Two main techniques to make inference with the Llama 3 405B model efficient are investigated: **(1)** pipeline parallelism and **(2)** FP8 quantization. The implementation of FP8 quantization has been publicly released.

## 6.1 Pipeline Parallelism [p. 51–52]

[p. 51] When using a BF16 number representation for the model parameters, Llama 3 405B does not fit in the GPU memory of a single machine with 8 Nvidia H100 GPUs. To address this issue, model inference is parallelized using BF16 precision across 16 GPUs on two machines. Within each machine, the high NVLink bandwidth enables the use of tensor parallelism (Shoeybi et al., 2019). Across nodes, however, connectivity has lower bandwidth and higher latency, so pipeline parallelism (Huang et al., 2019) is used instead. [p. 52]

[p. 52] During training with pipeline parallelism, bubbles are a major efficiency concern (see Section 3.3). However, they are not an issue during inference, since inference does not involve a backward pass that requires a pipeline flush. Therefore, micro-batching is used to improve inference throughput with pipeline parallelism.

The effect of using two micro-batches in inference workloads of 4,096 input tokens and 256 output tokens is evaluated both during the key-value cache *pre-fill* stage of inference and during the *decoding* stage. Micro-batching is found to improve throughput of inference with the same local batch size; see Figure 24. These improvements result from micro-batching enabling concurrent execution of micro batches in both these stages. The additional synchronization points due to micro-batching also increase latency but, overall, micro-batching still leads to a better throughput-latency trade-off. [p. 52]

**Figure 24** (p. 52): "Effect of micro-batching on inference throughput and latency during *Left:* pre-filling and *Right:* decoding stage. The numbers in the plot correspond to the (micro-)batch size."

*Left panel:* Prefill Throughput (tokens/sec) on y-axis (0–8000) vs. Prefill Latency (time-to-first-token, ms) on x-axis (~20–120 ms). Two series: TP8/PP2 (BF16) and TP8/PP2 (BF16) + Microbatching. The microbatching line shows higher throughput at each latency point. Batch sizes labeled on points range from 1 to beyond 4. Throughput with microbatching reaches ~7000–8000 tokens/sec at the highest batch sizes, compared to ~5000–6000 without microbatching.

*Right panel:* Decode Throughput (tokens/sec) on y-axis (0–1500) vs. Decode Latency (time-to-incremental-token, ms) on x-axis (0–140 ms). Two series: TP8/PP2 (BF16) and TP8/PP2 (BF16) + Microbatching. The microbatching line again shows higher throughput. The highest throughput with microbatching reaches ~1500 tokens/sec at batch size 128. Without microbatching, peak throughput is somewhat lower.

## 6.2 FP8 Quantization [p. 52–54]

[p. 52] Experiments leveraging the native FP8 support of H100 GPUs are performed to enable low-precision inference. FP8 quantization is applied to most matrix multiplications inside the model. In particular, most parameters and activations in the feedforward network layers in the model are quantized, which account for roughly 50% of the inference compute time. Parameters in the self-attention layers of the model are not quantized. Dynamic scaling factors are leveraged for better accuracy (Xiao et al., 2024b), optimizing CUDA kernels^15 to reduce the overhead of calculating the scales. The quality of Llama 3 405B is found to be sensitive to certain types of quantization, and a few additional changes are made to increase the model output quality: [p. 52]

1. Akin to Zhang et al. (2021), quantization is not performed in the first and last Transformer layers.

2. High-perplexity tokens such as dates can lead to large activation values. In turn, these can lead to high dynamic scaling factors in FP8 and a non-negligible number of underflows, leading to errors in decoding. [p. 52]

^15 FP8 kernels are available at https://github.com/pytorch/FBGEMM/tree/main/fbgemm_gpu/experimental/gen_ai. Usage examples at https://github.com/meta-llama/llama-agentic-system.

[p. 53] To address this issue, the dynamic scaling factors are upper bounded to 1200.

3. Row-wise quantization is used, computing scaling factors across rows for parameter and activation matrices (see Figure 25). This is found to work better than a tensor-wise quantization approach. [p. 53]

**Figure 25** (p. 53): "Illustration of tensor-wise and row-wise FP8 quantization. *Right:* Row-wise quantization enables the use of more granular activation factors than *Left:* tensor-wise quantization."

*Left panel (tensor-wise):* Shows BF16 Input and BF16 Weight each being quantized to FP8 Input and FP8 Weight with single scaling factors (x scaling_factor_input, x scaling_factor_weight) per tensor, then multiplied to produce BF16 Output.

*Right panel (row-wise):* Shows FP8 Input and FP8 Weight being multiplied to produce BF16 Output, but with per-row scaling factors (x scaling_factor_input applied per row of input, x scaling_factor_weight applied per row of weights), enabling more granular quantization.

### Effect of quantization errors

[p. 53] Evaluations on standard benchmarks often suggest that FP8 inference performs on par with BF16 inference even without these mitigations. However, such benchmarks are found to not adequately reflect the effects of FP8 quantization. When scaling factors are not upper bounded, the model occasionally produces corrupted responses even though the benchmark performance is strong. Instead of relying on benchmarks to measure distribution changes due to quantization, it is found to be better to analyze the distribution of reward-model scores for 100,000 responses produced using both FP8 and BF16. Figure 26 shows the resulting reward distribution for the quantization approach. The results in the figure show that the approach to FP8 quantization has very limited impact on the model's response. [p. 53]

**Figure 26** (p. 53): "Reward score distribution for Llama 3 405B using BF16 and FP8 inference. Our FP8 quantization approach has negligible impact on the model's responses."

A histogram showing the distribution of reward scores (x-axis: 0.0–1.0) for two conditions: bf16 (pinkish-red bars) and fp8_rowwise (blue bars). Both distributions are nearly identical, with a unimodal peak around 0.7–0.8 and count values (y-axis) reaching up to ~30,000. The distributions overlap almost completely, demonstrating negligible impact of FP8 quantization on response quality.

### Experimental evaluation of efficiency

[p. 53] Figure 27 depicts the throughput-latency trade-off of performing FP8 inference with Llama 3 405B in the pre-fill and decoding stages, using 4,096 input tokens and 256 output tokens. The figure compares the efficiency of FP8 inference with that of the two-machine BF16 inference approach described in Section 6.1. The results show that use of FP8 inference leads to throughput improvements of up to 50% during the pre-fill stage, and a substantially better throughput-latency trade-off during decoding. [p. 53]

**Figure 27** (p. 54): "Throughput-latency trade-off in FP8 inference with Llama 3 405B compared with BF16 inference using different pipeline parallelization setups. *Left:* Results for pre-filling. *Right:* Results for decoding."

*Left panel:* Prefill Throughput (tokens/sec) on y-axis (0–10k) vs. Prefill Latency (time-to-first-token, ms) on x-axis (0–20k). Four series: TP8/PP2 (BF16), TP8/PP2 (BF16) + Microbatching, TP4/PP4 (BF16) + Microbatching, and TP8 (FP8)*. The FP8 line achieves comparable or higher throughput at each latency point compared to all BF16 configurations. A note reads "* Throughput 2X because FP8 fits in one node." Batch sizes labeled on points range from 1 to 8.

*Right panel:* Decode Throughput (tokens/sec) on y-axis (0–beyond 1500) vs. Decode Latency (time-to-incremental-token, ms) on x-axis (0–140). Same four series. The FP8 line shows substantially higher throughput, reaching ~1700+ tokens/sec at batch size 128, compared to ~1500 for the best BF16+microbatching configuration. A note reads "* Throughput 2X because FP8 fits in one node." Batch sizes labeled include 1, 2, 4, 8, 16, 32, 64, 96, 128.
