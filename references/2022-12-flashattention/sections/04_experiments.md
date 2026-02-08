# 4 Experiments [p. 7–10]

[p. 7]

The impact of using FlashAttention to train Transformer models is evaluated. Two claims about training time and model accuracy are validated, and attention runtime and memory benchmarks are reported.

- **Training Speed.** FlashAttention outperforms the MLPerf 1.1 [58] speed record for BERT by 15%, and speeds up GPT-2 up to 3x over HuggingFace [87] and 1.8x over Megatron [77] over standard Transformers. FlashAttention speeds up the long-range arena (LRA) benchmark 2.4x.

- **Quality.** FlashAttention scales Transformers to longer sequences, yielding higher quality. FlashAttention trains GPT-2 with context length 4K faster than Megatron trains GPT-2 with context length 1K, while achieving 0.7 better perplexity. Modeling longer sequences yields 6.4 points of lift on two long-document classification tasks. FlashAttention yields the **first Transformer** that can achieve better-than-random performance on the challenging Path-X task (sequence length 16K), and block-sparse FlashAttention yields the **first sequence model** that we know of that can achieve better-than-random performance on Path-256 (sequence length 64K).

- **Benchmarking Attention.** Runtime and memory performance of FlashAttention and block-sparse FlashAttention are measured based on sequence length. The memory footprint of FlashAttention scales linearly with sequence length and is up to 3x faster than standard attention for common sequence lengths (up to 2K). The runtime of block-sparse FlashAttention scales linearly in sequence length and is faster than all existing approximate attention baselines. Additional experiment details are in Appendix E.

## 4.1 Faster Models with FlashAttention [p. 7–8]

### BERT

[p. 7]

FlashAttention yields the fastest single-node BERT training speed that the authors know of. They train a BERT-large [22] model with FlashAttention on Wikipedia. Table 1 compares their training time to the implementation from Nvidia that set the training speed record for MLPerf 1.1 [58]. Their implementation is 15% faster.

**Table 1:** Training time of BERT-large, starting from the same initialization provided by the MLPerf benchmark, to reach the target accuracy of 72.0% on masked language modeling. Averaged over 10 runs on 8xA100 GPUs.

| BERT Implementation | Training time (minutes) |
|---|---|
| Nvidia MLPerf 1.1 [58] | 20.0 +/- 1.5 |
| FlashAttention (ours) | **17.4 +/- 1.4** |

### GPT-2

[p. 7–8]

FlashAttention yields faster training times for GPT-2 [67] on the large OpenWebtext dataset [32] than the widely used HuggingFace [87] and Megatron-LM [77] implementations. Table 2 shows up to 3x end-to-end speedup compared to HuggingFace and 1.7x speedup compared to Megatron-LM. FlashAttention achieves the same perplexity as the other two implementations, as the model definition is not changed. Appendix E includes plots of the validation perplexity throughout training, confirming that FlashAttention is as numerically stable as the baselines and produces the same training / validation curves.

**Table 2:** GPT-2 small and medium using FlashAttention achieve up to 3x speed up compared to HuggingFace implementation and up to 1.7x compared to Megatron-LM. Training time reported on 8xA100s GPUs.

| Model implementations | OpenWebText (ppl) | Training time (speedup) |
|---|---|---|
| GPT-2 small - Huggingface [87] | 18.2 | 9.5 days (1.0x) |
| GPT-2 small - Megatron-LM [77] | 18.2 | 4.7 days (2.0x) |
| GPT-2 small - FlashAttention | 18.2 | **2.7 days (3.5x)** |
| GPT-2 medium - Huggingface [87] | 14.2 | 21.0 days (1.0x) |
| GPT-2 medium - Megatron-LM [77] | 14.3 | 11.5 days (1.8x) |
| GPT-2 medium - FlashAttention | 14.3 | **6.9 days (3.0x)** |

### Long-range Arena

[p. 8]

Vanilla Transformer (with either standard implementation or FlashAttention) is compared on the long-range arena (LRA [80]) benchmark. Accuracy, throughput, and training time of all models are measured. Each task has a different sequence length varying between 1024 and 4096. The implementation and experimental setting of Tay et al. [80] and Xiong et al. [90] are followed. ^3

Table 3 shows that FlashAttention achieves up to 2.4x speed-up compared to standard attention. Block-sparse FlashAttention is faster than all of the approximate attention methods that have been tested.

**Table 3:** The performance of standard attention, FlashAttention, block-sparse FlashAttention, and approximate attention baselines on the Long-Range-Arena benchmarks.

| Models | ListOps | Text | Retrieval | Image | Pathfinder | Avg | Speedup |
|---|---|---|---|---|---|---|---|
| Transformer | 36.0 | 63.6 | 81.6 | 42.3 | 72.7 | 59.3 | - |
| FlashAttention | 37.6 | 63.9 | 81.4 | 43.5 | 72.7 | 59.8 | 2.4x |
| Block-sparse FlashAttention | 37.0 | 63.0 | 81.3 | 43.6 | 73.3 | 59.6 | **2.8x** |
| Linformer [84] | 35.6 | 55.9 | 77.7 | 37.8 | 67.6 | 54.9 | 2.5x |
| Linear Attention [50] | 38.8 | 63.2 | 80.7 | 42.6 | 72.5 | 59.6 | 2.3x |
| Performer [12] | 36.8 | 63.6 | 82.2 | 42.1 | 69.9 | 58.9 | 1.8x |
| Local Attention [80] | 36.1 | 60.2 | 76.7 | 40.6 | 66.6 | 56.0 | 1.7x |
| Reformer [51] | 36.5 | 63.8 | 78.5 | 39.6 | 69.4 | 57.6 | 1.3x |
| Smyrf [19] | 36.1 | 64.1 | 79.0 | 39.6 | 70.5 | 57.9 | 1.7x |

^3 LRA accuracy results are known to be highly dependent on the tuning procedure [90]. The reproduced baselines perform better than as reported in the original comparison [80].

## 4.2 Better Models with Longer Sequences [p. 8–9]

### Language Modeling with Long Context

[p. 8]

The runtime and memory-efficiency of FlashAttention allow increasing the context length of GPT-2 by 4x while still running faster than the optimized implementation from Megatron-LM. Table 4 shows that GPT-2 with FlashAttention and context length 4K is still 30% faster than GPT-2 from Megatron with context length 1K, while achieving 0.7 better perplexity.

**Table 4:** GPT-2 small with FlashAttention, with 4x larger context length compared to Megatron-LM, is still 30% faster while achieving 0.7 better perplexity. Training time on 8xA100 GPUs is reported.

| Model implementations | Context length | OpenWebText (ppl) | Training time (speedup) |
|---|---|---|---|
| GPT-2 small - Megatron-LM | 1k | 18.2 | 4.7 days (1.0x) |
| GPT-2 small - FlashAttention | 1k | 18.2 | **2.7 days (1.7x)** |
| GPT-2 small - FlashAttention | 2k | 17.6 | 3.0 days (1.6x) |
| GPT-2 small - FlashAttention | 4k | **17.5** | 3.6 days (1.3x) |

### Long Document Classification

[p. 8–9]

Training Transformers with longer sequences with FlashAttention improves performance on the MIMIC-III [47] and ECtHR [6, 7] datasets. MIMIC-III contains intensive care unit patient discharge summaries, each annotated with multiple labels. ECtHR contains legal cases from the European Court of Human Rights, each of which is mapped to articles of the Convention of Human Rights that were allegedly violated. Both of these datasets contain very long text documents; the average number of tokens in MIMIC is 2,395 tokens, and the longest document contains 14,562 tokens, while the average and longest numbers in ECtHR are 2,197 and 49,392, respectively. The lift from increasing the sequence length of a pretrained RoBERTa model [56] is evaluated (repeating the positional embeddings, as in Beltagy et al. [3]).

[p. 9]

Table 5 shows that sequence length 16K outperforms length 512 by 4.3 points on MIMIC, and that length 8K outperforms length 512 by 8.5 points on ECtHR. The discrepancies may be due to subtle distribution shifts: MIMIC-III contains specialized medical text and thus may be more susceptible to a distribution shift in the document length, whereas ECtHR contains general language.

**Table 5:** Long Document performance (micro $F_1$) at different sequence lengths using FlashAttention.

|  | 512 | 1024 | 2048 | 4096 | 8192 | 16384 |
|---|---|---|---|---|---|---|
| MIMIC-III [47] | 52.8 | 50.7 | 51.7 | 54.6 | 56.4 | **57.1** |
| ECtHR [6] | 72.2 | 74.3 | 77.1 | 78.6 | **80.7** | 79.2 |

### Path-X and Path-256

[p. 9]

The Path-X and Path-256 benchmarks are challenging tasks from the long-range arena benchmark designed to test long context. The task is to classify whether two points in a black and white 128x128 (or 256x256) image have a path connecting them, and the images are fed to the transformer one pixel at a time. In prior work, all transformer models have either run out of memory, or only achieved random performance [80]. There has been a search for alternative architectures that can model such long context [37].

The authors present the first result of Transformer models being able to solve Path-X and Path-256 (Table 6). They pretrain a transformer on Path-64, and then transfer to Path-X by spatially interpolating the positional embeddings. FlashAttention achieves 61.4 accuracy on Path-X. Additionally, block-sparse FlashAttention enables the Transformers to scale to sequence length 64K, achieving 63.1 accuracy ^4 on Path-256.

**Table 6:** The first Transformer model that can achieve non-random performance on Path-X and Path-256.

| Model | Path-X | Path-256 |
|---|---|---|
| Transformer | X | X |
| Linformer [84] | X | X |
| Linear Attention [50] | X | X |
| Performer [12] | X | X |
| Local Attention [80] | X | X |
| Reformer [51] | X | X |
| SMYRF [19] | X | X |
| FlashAttention | **61.4** | X |
| Block-sparse FlashAttention | 56.0 | **63.1** |

(X = fail, i.e., out of memory or random performance)

^4 Path-256 requires longer sequences but has relatively shorter paths than Path-X, so it is easier to obtain a higher accuracy.

## 4.3 Benchmarking Attention [p. 9–10]

[p. 9–10]

Sequence length is varied and runtime and memory usage of FlashAttention and block-sparse FlashAttention are measured against various attention baselines on one A100 GPU with 40 GB HBM, with dropout and a padding mask. Comparison is against reference implementations for exact attention, approximate attention, and sparse attention. A subset of baselines is reported in the main body; Appendix E contains more baselines and full details.

**Figure 3** (p. 9): "Left: runtime of forward pass + backward pass. Right: attention memory usage."

The figure shows two panels:
- **Left panel:** "Attention Runtime (Fwd Pass + Bwd Pass)" — log-scale y-axis (Runtime in ms) vs sequence length (x-axis: 128, 256, 512, 1024, 2048, 4096, 8192). Lines for: FlashAttention (dotted black), Block-Sparse FlashAttention (dashed black), PyTorch Attention (solid red), Megatron Attention (dashed red), Linformer Attention (dotted green), OpenAI Sparse Attention (dashed green). Crossover points are annotated where FlashAttention crosses approximate methods. PyTorch and Megatron grow quadratically; FlashAttention is significantly faster (up to 3x faster than PyTorch). Approximate/sparse methods grow linearly but FlashAttention is still faster for short sequences.
- **Right panel:** "Attention Memory Usage" — Memory Footprint (GB) vs Sequence Length (256 to 64K). FlashAttention and Block-Sparse FlashAttention grow linearly. Exact attention baselines grow quadratically. FlashAttention is up to 20x more memory-efficient than exact attention, and 2x more efficient than Linformer at 64K. All other algorithms except Linformer run out of memory on an A100 GPU before 64K.

### Runtime

[p. 10]

Figure 3 (left) reports the runtime in milliseconds of the forward + backward pass of FlashAttention and block-sparse FlashAttention compared to the baselines in exact, approximate, and sparse attention (exact numbers in Appendix E). Runtime grows quadratically with sequence length, but FlashAttention runs significantly faster than **exact attention** baselines, up to 3x faster than the PyTorch implementation. The runtimes of many approximate/sparse attention mechanisms grow linearly with sequence length, but FlashAttention still runs faster than approximate and sparse attention for short sequences due to fewer memory accesses. The **approximate attention** runtimes begin to cross over with FlashAttention at sequences between 512 and 1024. On the other hand, block-sparse FlashAttention is faster than all implementations of exact, sparse, and approximate attention that the authors know of, across all sequence lengths.

### Memory Footprint

[p. 10]

Figure 3 (right) shows the memory footprint of FlashAttention and block-sparse FlashAttention compared to various exact, approximate, and sparse attention baselines. FlashAttention and block-sparse FlashAttention have the same memory footprint, which grows linearly with sequence length. FlashAttention is up to 20x more memory efficient than **exact attention** baselines, and is more memory-efficient than the **approximate attention** baselines. All algorithms except for Linformer run out of memory on an A100 GPU before 64K, and FlashAttention is still 2x more efficient than Linformer.
