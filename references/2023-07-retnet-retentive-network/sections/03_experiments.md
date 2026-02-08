# 3 Experiments [p. 6–10]

Experiments on language modeling are conducted to evaluate RetNet. The proposed architecture is evaluated with various benchmarks, i.e., language modeling performance, and zero-/few-shot learning on downstream tasks. Moreover, for training and inference, speed, memory consumption, and latency are compared. [p. 6]

## 3.1 Setup

[p. 7]

**Parameter Allocation** — Parameters in MSR and FFN are re-allocated for fair comparisons. Let d denote d_model for simplicity. In Transformers, there are about 4d^2 parameters in self-attention where W_Q, W_K, W_V, W_O in R^{d x d}, and 8d^2 parameters in FFN where the intermediate dimension is 4d. In comparison, RetNet has 8d^2 parameters in retention, where W_Q, W_K in R^{d x d}, W_G, W_V in R^{d x 2d}, W_O in R^{2d x d}. The head dimension of V is twice Q, K. The widened dimension is projected back to d by W_O. In order to keep the parameter number the same as Transformer, the FFN intermediate dimension in RetNet is 2d. [p. 7]

The head dimension is set to 256 in experiments, i.e., 256 for queries and keys, and 512 for values. For fair comparison, gamma is kept identical among different model sizes, where gamma = 1 - e^{linspace(log 1/32, log 1/512, h)} in R^h instead of the default value in Equation (8). [p. 7]

**Language Model Training** — Language models are trained with various sizes (i.e., 1.3B, 2.7B, and 6.7B) from scratch. The training corpus is a curated compilation of The Pile [GBB+20], C4 [DMI+21], and The Stack [KLBA+22]. The <bos> token is appended to indicate the start of a sequence (footnote 2: appending the <bos> token at the beginning benefits training stability and performance). The training batch size is 4M tokens with 2048 maximal length. The models are trained with 100B tokens, i.e., 25k steps. The AdamW [LH19] optimizer is used with beta_1 = 0.9, beta_2 = 0.98, and weight decay is set to 0.05. The number of warmup steps is 375 with linear learning rate decay. The parameters are initialized following DeepNet [WMD+22] to guarantee training stability. The implementation is based on TorchScale [MWH+22]. The models are trained with 512 AMD MI200 GPUs. [p. 7]

**Table 2** (p. 7): "Sizes, and learning hyper-parameters of the models in language modeling experiments."

| Size | Hidden Dim. | #Layers | Batch Size | # Tokens | Learning Rate |
|---|---|---|---|---|---|
| 1.3B | 2048 | 24 | 4M | 100B | 6 x 10^-4 |
| 2.7B | 2560 | 32 | 4M | 100B | 3 x 10^-4 |
| 6.7B | 4096 | 32 | 4M | 100B | 3 x 10^-4 |

## 3.2 Comparisons with Transformer

[p. 7–8]

**Language Modeling** — As shown in Figure 5, perplexity is reported on the validation set for the language models based on Transformer and RetNet. Scaling curves are presented with three model sizes, i.e., 1.3B, 2.7B, and 6.7B. RetNet achieves comparable results with Transformers. More importantly, the results indicate that RetNet is favorable regarding size scaling. Besides performance, the RetNet training is quite stable in experiments. Experimental results show that RetNet is a strong competitor to Transformer for large language models. Empirically, RetNet starts to outperform Transformer when the model size is larger than 2B. Language modeling results with different context lengths are also summarized in Appendix B. [p. 7]

**Figure 5** (p. 7): "Perplexity decreases along with scaling up the model size. We empirically observe that RetNet tends to outperform Transformer when the model size is larger than 2B."

The figure shows validation perplexity (y-axis, range approximately 12.5–15.0) vs. model size (x-axis: 1.3B, 2.7B, 6.7B). Two lines are plotted: RetNet (solid blue) and Transformer (dashed orange). Both decrease as model size increases. At 1.3B, Transformer has slightly lower perplexity than RetNet. The lines cross between 1.3B and 2.7B, and at 2.7B RetNet is slightly better. At 6.7B, RetNet clearly outperforms Transformer (approximately 12.8 vs. 13.0). [p. 7]

**Zero-Shot and Few-Shot Evaluation on Downstream Tasks** — The language models are also compared on a wide range of downstream tasks. Zero-shot and 4-shot learning are evaluated with the 6.7B models. As shown in Table 3, the datasets include HellaSwag (HS) [ZHB+19], BoolQ [CLC+19], COPA [WPN+19], PIQA [BZB+20], Winograd, Winogrande [LDM12], and StoryCloze (SC) [MRL+17]. The accuracy numbers are consistent with language modeling perplexity presented in Figure 5. RetNet achieves comparable performance with Transformer on zero-shot and in-context learning settings. [p. 8]

**Table 3** (p. 8): "Zero-shot and few-shot learning with Transformer and RetNet. The model size is 6.7B."

| | HS | BoolQ | COPA | PIQA | Winograd | Winogrande | SC | Avg |
|---|---|---|---|---|---|---|---|---|
| *Zero-Shot* | | | | | | | | |
| Transformer | 55.9 | 62.0 | 69.0 | 74.6 | 69.5 | 56.5 | 75.0 | 66.07 |
| RetNet | **60.7** | **62.2** | **77.0** | **75.4** | **77.2** | **58.1** | **76.0** | **69.51** |
| *4-Shot* | | | | | | | | |
| Transformer | 55.8 | 58.7 | 71.0 | 75.0 | 71.9 | 57.3 | 75.4 | 66.44 |
| RetNet | **60.5** | **60.1** | **78.0** | **76.0** | **77.9** | **59.9** | **75.9** | **69.76** |

Note: Bold values indicate best in each column within each setting (zero-shot / 4-shot).

## 3.3 Training Cost

[p. 8]

As shown in Table 4, the training speed and memory consumption of Transformer and RetNet are compared, where the training sequence length is 8192. FlashAttention [DFE+22] is also compared, which improves speed and reduces GPU memory IO by recomputation and kernel fusion. In comparison, RetNet is implemented using vanilla PyTorch code, and leaves kernel fusion or FlashAttention-like acceleration for future work. The chunkwise recurrent representation of retention as described in Equation (7) is used. The chunk size is set to 512. Results are evaluated with eight Nvidia A100-80GB GPUs, because FlashAttention is highly optimized for A100. Tensor parallelism is enabled for 6.7B and 13B models. [p. 8]

Experimental results show that RetNet is more memory-efficient and has higher throughput than Transformers during training. Even compared with FlashAttention, RetNet is still competitive in terms of speed and memory cost. Moreover, without relying on specific kernels, it is easy to train RetNet on other platforms efficiently. For example, the RetNet models are trained on an AMD MI200 cluster with decent throughput. It is notable that RetNet has the potential to further reduce cost via advanced implementation, such as kernel fusion. [p. 8]

**Table 4** (p. 8): "Training cost of Transformer (Trm), Transformer with FlashAttention (Trm+FlashAttn), and RetNet. We report memory consumption and training throughput (word per second; wps)."

| Model Size | Memory (GB) -- Trm | Memory (GB) -- Trm+FlashAttn | Memory (GB) -- RetNet | Throughput (wps) -- Trm | Throughput (wps) -- Trm+FlashAttn | Throughput (wps) -- RetNet |
|---|---|---|---|---|---|---|
| 1.3B | 74.8 | 38.8 | 34.5 | 10832.4 | 63965.2 | 73344.8 |
| 2.7B | 69.6 | 42.1 | 42.0 | 5186.0 | 34990.2 | 38921.2 |
| 6.7B | 69.0 | 51.4 | 48.0 | 2754.4 | 16230.1 | 17458.6 |
| 13B | 61.4 | 46.3 | 45.9 | 1208.9 | 7945.1 | 8642.2 |

## 3.4 Inference Cost

[p. 8–9]

As shown in Figure 6, memory cost, throughput, and latency of Transformer and RetNet are compared during inference. Transformers reuse KV caches of previously decoded tokens. RetNet uses the recurrent representation as described in Equation (6). The 6.7B model is evaluated on the A100-80GB GPU. Figure 6 shows that RetNet outperforms Transformer in terms of inference cost. [p. 8]

**Memory** — As shown in Figure 6a, the memory cost of Transformer increases linearly due to KV caches. In contrast, the memory consumption of RetNet remains consistent even for long sequences, requiring much less GPU memory to host RetNet. The additional memory consumption of RetNet is almost negligible (i.e., about 3%) while the model weights occupy 97%. [p. 8–9]

**Throughput** — As presented in Figure 6b, the throughput of Transformer drops along with the decoding length increases. In comparison, RetNet has higher and length-invariant throughput during decoding, by utilizing the recurrent representation of retention. [p. 9]

**Latency** — Latency is an important metric in deployment, which greatly affects user experience. Decoding latency is reported in Figure 6c. Experimental results show that increasing batch size renders Transformer's latency larger. Moreover, the latency of Transformers grows faster with longer input. In order to make latency acceptable, the batch size has to be restricted, which harms the overall inference throughput of Transformers. By contrast, RetNet's decoding latency outperforms Transformers and keeps almost the same across different batch sizes and input lengths. [p. 9]

**Figure 6** (p. 9): "Inference cost of Transformer and RetNet with a model size of 6.7B. RetNet outperforms Transformers in terms of memory consumption, throughput, and latency."

Three subplots:

(a) GPU memory cost of Transformer and RetNet. X-axis: Sequence Length (2048 to 8192). Y-axis: GPU Memory (GB), range approximately 13–45. Three lines: Model Weights (dashed black, flat around 13 GB), RetNet (solid blue, flat around 14 GB, almost overlapping with model weights), Transformer (dashed orange, increasing linearly from about 20 GB at 2048 to about 45 GB at 8192). Shows that RetNet memory stays constant while Transformer memory grows linearly with sequence length. [p. 9]

(b) Throughput of Transformer and RetNet. X-axis: Sequence Length (2048 to 8192). Y-axis: Throughput (wps), range approximately 25–300. Two lines: RetNet (solid blue, flat around 300 wps across all sequence lengths), Transformer (orange with squares, decreasing from about 150 wps at 2048 to about 50 wps at 8192). RetNet has consistently higher and length-invariant throughput. [p. 9]

(c) Inference latency with different batch sizes. X-axis: Batch Size (1 to 8). Y-axis: Latency (ms), range approximately 25–350. Five lines: Transformer (1024) (blue, starting around 50 ms, increasing to about 75 ms), Transformer (2048) (orange, starting around 50 ms, increasing to about 100 ms), Transformer (4096) (green, starting around 75 ms, increasing to about 175 ms), Transformer (8192) (red, starting around 100 ms, increasing to about 350 ms), RetNet (8192) (light blue, flat around 25–30 ms across all batch sizes). RetNet latency stays flat and low regardless of batch size, while Transformer latency increases with both batch size and sequence length. [p. 9]

## 3.5 Comparison with Transformer Variants

[p. 9–10]

RetNet is compared with various efficient Transformer variants, including Linear Transformer [KVPF20], RWKV [PAA+23], H3 [DFS+22], and Hyena [PMN+23]. All models have 200M parameters with 16 layers and a hidden dimension of 1024. For H3, the head dimension is set as 8. For RWKV, the TimeMix module is used to substitute self-attention layers while keeping FFN layers consistent with other models for fair comparisons. The models are trained with 10k steps with a batch size of 0.5M tokens. Most hyperparameters and training corpora are kept the same as in Section 3.1. [p. 9]

Table 5 reports the perplexity numbers on the in-domain validation set and other out-of-domain corpora, e.g., Project Gutenberg 2019-2022 (PG22) [SDP+22], QMSum [ZYY+21], GovReport [HCP+21], SummScreen [CCWG21, SSI+22]. Overall, RetNet outperforms previous methods across different datasets. RetNet not only achieves better evaluation results on the in-domain corpus but also obtains lower perplexity on several out-of-domain datasets. The favorable performance makes RetNet a strong successor to Transformer, besides the benefits of significant cost reduction (Sections 3.3 and 3.4). [p. 9–10]

**Table 5** (p. 10): "Perplexity results on language modeling. RetNet outperforms other architectures on both the in-domain evaluation set and various out-of-domain corpora."

| Method | In-Domain | PG22 | QMSum | GovReport | SummScreen |
|---|---|---|---|---|---|
| RWKV | 30.92 | 51.41 | 28.17 | 19.80 | 25.78 |
| H3 | 29.97 | 49.17 | 24.29 | 19.19 | 25.11 |
| Hyena | 32.08 | 52.75 | 28.18 | 20.55 | 26.51 |
| Linear Transformer | 40.24 | 63.86 | 28.45 | 25.33 | 32.02 |
| RetNet | **26.05** | **45.27** | **21.33** | **16.52** | **22.48** |

In addition, the training and inference efficiency of the compared methods is discussed. Let d denote the hidden dimension, and n the sequence length. For training, RWKV's token-mixing complexity is O(dn) while Hyena's is O(dn log n) with Fast Fourier Transform acceleration. The above two methods reduce training FLOPS via employing element-wise operators to trade-off modeling capacity. In comparison with retention, the chunk-wise recurrent representation is O(dn(b + h)), where b is the chunk size, h is the head dimension, and usually b = 512, h = 256. For either large model size (i.e., larger d) or sequence length, the additional b + h has negligible effects. So the RetNet training is quite efficient without sacrificing the modeling performance. For inference, among the compared efficient architectures, Hyena has the same complexity (i.e., O(n) per step) as Transformer while the others can perform O(1) decoding. [p. 10]

## 3.6 Ablation Studies

[p. 10–11]

Various design choices of RetNet are ablated and the language modeling results are reported in Table 6. The evaluation settings and metrics are the same as in Section 3.5. [p. 10]

**Architecture** — The swish gate and GroupNorm as described in Equation (8) are ablated. Table 6 shows that the above two components improve the final performance. Firstly, the gating module is essential for enhancing non-linearity and improving model capability. Notice that the same parameter allocation as Transformers is used after removing the gate. Secondly, group normalization in retention balances the variances of multi-head outputs, which improves training stability and language modeling results. [p. 10]

**Multi-Scale Decay** — Equation (8) shows that different gamma are used as the decay rates for the retention heads. In the ablation studies, removing gamma decay (i.e., "- gamma decay") and applying the same decay rate across heads (i.e., "- multi-scale decay") are examined. Specifically, ablating gamma decay is equivalent to gamma = 1. In the second setting, gamma = 127/128 for all heads. Table 6 indicates that both the decay mechanism and using multiple decay rates can improve the language modeling performance. [p. 10]

**Head Dimension** — From the recurrent perspective of Equation (1), the head dimension implies the memory capacity of hidden states. In the ablation study, the default head dimension is reduced from 256 to 64, i.e., 64 for queries and keys, and 128 for values. The hidden dimension d_model is kept the same so the number of heads increases. Experimental results in Table 6 show that the larger head dimension achieves better performance. [p. 10–11]

**Table 6** (p. 10): "Ablation results on in-domain and out-of-domain corpora."

| Method | In-Domain | PG22 | QMSum | GovReport | SummScreen |
|---|---|---|---|---|---|
| RetNet | **26.05** | **45.27** | **21.33** | **16.52** | **22.48** |
| - swish gate | 27.84 | 49.44 | 22.52 | 17.45 | 23.72 |
| - GroupNorm | 27.54 | 46.95 | 22.61 | 17.59 | 23.73 |
| - gamma decay | 27.86 | 47.85 | 21.99 | 17.49 | 23.70 |
| - multi-scale decay | 27.02 | 47.18 | 22.08 | 17.17 | 23.38 |
| Reduce head dimension | 27.68 | 47.72 | 23.09 | 17.46 | 23.41 |
