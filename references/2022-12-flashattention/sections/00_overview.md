# Overview

**Title:** FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness
**Authors:** Tri Dao, Daniel Y. Fu, Stefano Ermon, Atri Rudra, Christopher Re
**Affiliations:**
- Tri Dao, Daniel Y. Fu, Stefano Ermon, Christopher Re: Department of Computer Science, Stanford University
- Atri Rudra: Department of Computer Science and Engineering, University at Buffalo, SUNY

**Venue:** NeurIPS 2022
**Date:** June 24, 2022 (arXiv v2)

## Abstract

> "Transformers are slow and memory-hungry on long sequences, since the time and memory complexity of self-attention are quadratic in sequence length. Approximate attention methods have attempted to address this problem by trading off model quality to reduce the compute complexity, but often do not achieve wall-clock speedup. We argue that a missing principle is making attention algorithms IO-aware---accounting for reads and writes between levels of GPU memory. We propose FlashAttention, an IO-aware exact attention algorithm that uses tiling to reduce the number of memory reads/writes between GPU high bandwidth memory (HBM) and GPU on-chip SRAM. We analyze the IO complexity of FlashAttention, showing that it requires fewer HBM accesses than standard attention, and is optimal for a range of SRAM sizes. We also extend FlashAttention to block-sparse attention, yielding an approximate attention algorithm that is faster than any existing approximate attention method. FlashAttention trains Transformers faster than existing baselines: 15% end-to-end wall-clock speedup on BERT-large (seq. length 512) compared to the MLPerf 1.1 training speed record, 3x speedup on GPT-2 (seq. length 1K), and 2.4x speedup on long-range arena (seq. length 1K-4K). FlashAttention and block-sparse FlashAttention enable longer context in Transformers, yielding higher quality models (0.7 better perplexity on GPT-2 and 6.4 points of lift on long-document classification) and entirely new capabilities: the first Transformers to achieve better-than-chance performance on the Path-X challenge (seq. length 16K, 61.4% accuracy) and Path-256 (seq. length 64K, 63.1% accuracy)." [p. 1]

## Section Headings

1. Introduction [p. 1–3]
2. Background [p. 3–4]
   - 2.1 Hardware Performance [p. 3]
   - 2.2 Standard Attention Implementation [p. 4]
3. FlashAttention: Algorithm, Analysis, and Extensions [p. 4–7]
   - 3.1 An Efficient Attention Algorithm With Tiling and Recomputation [p. 4–5]
   - 3.2 Analysis: IO Complexity of FlashAttention [p. 5–6]
   - 3.3 Extension: Block-Sparse FlashAttention [p. 6–7]
4. Experiments [p. 7–10]
   - 4.1 Faster Models with FlashAttention [p. 7–8]
   - 4.2 Better Models with Longer Sequences [p. 8–9]
   - 4.3 Benchmarking Attention [p. 9–10]
5. Limitations and Future Directions [p. 10]
6. Acknowledgements [p. 10–11]
7. References [p. 11–16]
A. Related Work [p. 17]
B. Algorithm Details [p. 17–21]
   - B.1 Memory-efficient forward pass [p. 18]
   - B.2 Memory-efficient backward pass [p. 18–19]
   - B.3 FlashAttention: Forward Pass [p. 19–20]
   - B.4 FlashAttention: Backward Pass [p. 20–21]
   - B.5 Comparison with Rabe and Staats [66] [p. 22]
C. Proofs [p. 22–24]
D. Extension Details [p. 25–26]
   - D.1 Block-Sparse FlashAttention [p. 25]
   - D.2 Potential Extensions [p. 25–26]
E. Full Experimental Results [p. 26–34]
   - E.1 BERT [p. 26]
   - E.2 GPT-2 [p. 26–27]
   - E.3 LRA Details [p. 27]
   - E.4 Comparison with Apex FMHA [p. 27–28]
   - E.5 Speedup On Different Hardware and Configurations [p. 28–30]
   - E.6 Full Benchmarking Results [p. 30–34]
