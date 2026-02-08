# Overview

**Title:** Effective Long-Context Scaling of Foundation Models

**Authors:** Wenhan Xiong^{+*}, Jingyu Liu^{+}, Igor Molybog, Hejia Zhang, Prajjwal Bhargava, Rui Hou, Louis Martin, Rashi Rungta, Karthik Abinav Sankararaman, Barlas Oguz, Madian Khabsa, Han Fang, Yashar Mehdad, Sharan Narang, Kshitiz Malik, Angela Fan, Shruti Bhosale, Sergey Edunov, Mike Lewis, Sinong Wang*, Hao Ma*

- ^{+} Equal contribution
- * Corresponding authors: {xwhan, sinongwang, haom}@meta.com

**Affiliations:** GenAI, Meta

**Venue:** arXiv:2309.16039v3

**Date:** 14 Nov 2023

## Abstract

> "We present a series of long-context LLMs that support effective context windows of up to 32,768 tokens. Our model series is built through continual pretraining from LLAMA 2 with longer training sequences and on a dataset where long texts are upsampled. We perform extensive evaluation on language modeling, synthetic context probing tasks, and a wide range of research benchmarks. On research benchmarks, our models achieve consistent improvements on most regular tasks and significant improvements on long-context tasks over LLAMA 2. Notably, with a cost-effective instruction tuning procedure that does not require human-annotated long instruction data, the 70B variant can already surpass gpt-3.5-turbo-16k's overall performance on a suite of long-context tasks. Alongside these results, we provide an in-depth analysis on the individual components of our method. We delve into LLAMA's position encodings and discuss its limitation in modeling long dependencies. We also examine the impact of various design choices in the pretraining process, including the data mix and the training curriculum of sequence lengths -- our ablation experiments suggest that having abundant long texts in the pretrain dataset is *not* the key to achieving strong performance, and we empirically verify that long context continual pretraining is more efficient and similarly effective compared to pretraining from scratch with long sequences." [p. 1]

## Section Headings

1. Introduction
2. Method
   - 2.1 Continual Pretraining
   - 2.2 Instruction Tuning
3. Main Results
   - 3.1 Pretrained Model Evaluation
   - 3.2 Instruction Tuning Results
   - 3.3 Human Evaluation
4. Analysis
   - 4.1 Positional Encoding for Long Text
   - 4.2 Pretraining Data Mix
   - 4.3 Instruction Tuning
   - 4.4 Training Curriculum
5. AI Safety
   - 5.1 Evaluation on Safety Benchmarks
   - 5.2 Red Teaming Exercises
6. Limitations
7. Conclusion
8. Acknowledgement
A. More Results
B. Theoretical Analysis of Positional Encodings
C. Length Extrapolation Results
D. Self-Instruct Data
