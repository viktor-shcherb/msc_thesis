# Overview

## Paper Metadata

**Title:** FlashAttention-3: Fast and Accurate Attention with Asynchrony and Low-precision

**Authors:** Jay Shah¹*, Ganesh Bikshandi¹*, Ying Zhang², Vijay Thakkar³⁴, Pradeep Ramani³, and Tri Dao⁵⁶
- *Equal contribution

**Affiliations:**
- ¹ Colfax Research
- ² Meta
- ³ NVIDIA
- ⁴ Georgia Tech
- ⁵ Princeton University
- ⁶ Together AI

**Contact:** {jayshah,ganesh}@colfax-intl.com, yingz@meta.com, {vthakkar,peraman}@nvidia.com, tri@tridao.me

**Date:** July 16, 2024

## Abstract

> "Attention, as a core layer of the ubiquitous Transformer architecture, is the bottleneck for large language models and long-context applications. FLASHATTENTION elaborated an approach to speed up attention on GPUs through minimizing memory reads/writes. However, it has yet to take advantage of new capabilities present in recent hardware, with FLASHATTENTION-2 achieving only 35% utilization on the H100 GPU. We develop three main techniques to speed up attention on Hopper GPUs: exploiting asynchrony of the Tensor Cores and TMA to (1) overlap overall computation and data movement via warp-specialization and (2) interleave block-wise matmul and softmax operations, and (3) block quantization and incoherent processing that leverages hardware support for FP8 low-precision. We demonstrate that our method, FLASHATTENTION-3, achieves speedup on H100 GPUs by 1.5-2.0× with FP16 reaching up to 740 TFLOPS (75% utilization), and with FP8 reaching close to 1.2 PFLOPS/s. We validate that FP8 FLASHATTENTION-3 achieves 2.6× lower numerical error than a baseline FP8 attention."

## Section Headings

1. Introduction [p. 1]
2. Background: Multi-Head Attention and GPU Characteristics [p. 2-4]
   - 2.1 Multi-Head Attention [p. 2-3]
   - 2.2 GPU hardware characteristics and execution model [p. 3]
   - 2.3 Standard Attention and Flash Attention [p. 4]
3. FlashAttention-3: Algorithm [p. 4-9]
   - 3.1 Producer-Consumer asynchrony through warp-specialization and pingpong scheduling [p. 4-6]
   - 3.2 Intra-warpgroup overlapping GEMMs and softmax [p. 6-7]
   - 3.3 Low-precision with FP8 [p. 7-9]
4. Empirical Validation [p. 9-11]
   - 4.1 Benchmarking Attention [p. 9-10]
   - 4.2 Ablation Study: 2-Stage Pipelining Experiments [p. 9, 11]
   - 4.3 Numerical Error Validation [p. 10-11]
5. Discussion, Limitations, Conclusion [p. 12]
6. Acknowledgments [p. 12]
7. References [p. 12-16]
A. Related Work [p. 17]
   - Attention variants and distributed attention
   - Alternative architectures
   - Low-precision attention
   - Hardware-aware Algorithms
B. Addition Details on Algorithms [p. 18-20]
   - B.1 Asynchrony Through Warp Specialization for the Backward Pass [p. 18]
   - B.2 2-Stage Pipelining SASS Analysis [p. 19]
   - B.3 3-Stage Pipelining Algorithm [p. 20]
C. Addition Details on Experiments and Benchmarking [p. 21-22]
   - C.1 System and libraries [p. 21]
   - C.2 FP8 Attention Full Results [p. 21-22]
