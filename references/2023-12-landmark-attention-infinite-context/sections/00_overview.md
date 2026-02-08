# Overview

**Title:** Random-Access Infinite Context Length for Transformers

**Authors:**
- Amirkeivan Mohtashami (EPFL, amirkeivan.mohtashami@epfl.ch)
- Martin Jaggi (EPFL, martin.jaggi@epfl.ch)

**Venue:** 37th Conference on Neural Information Processing Systems (NeurIPS 2023)

**Date:** 20 Nov 2023 (arXiv v2: 2305.16300v2)

**Code:** https://github.com/epfml/landmark-attention/

## Abstract

> "While Transformers have shown remarkable success in natural language processing, their attention mechanism's large memory requirements have limited their ability to handle longer contexts. Prior approaches, such as recurrent memory or retrieval augmentation, have either compromised the random-access flexibility of attention (i.e., the capability to select any token in the entire context) or relied on separate mechanisms for relevant context retrieval, which may not be compatible with the model's attention. In this paper, we present a novel approach that allows access to the complete context while retaining random-access flexibility, closely resembling running attention on the entire context. Our method uses a landmark token to represent each block of the input and trains the attention to use it for selecting relevant blocks, enabling retrieval of blocks directly through the attention mechanism instead of by relying on a separate mechanism. Our approach seamlessly integrates with specialized data structures and the system's memory hierarchy, enabling processing of arbitrarily long context lengths. We demonstrate that our method can obtain comparable performance with Transformer-XL while significantly reducing the number of retrieved tokens in each step. Finally, we show that fine-tuning LLaMA 7B with our method successfully extends its context length capacity to over 32k tokens, allowing for inference at the context lengths of GPT-4. We release the implementation of landmark attention and the code to reproduce our experiments at https://github.com/epfml/landmark-attention/." [p. 1]

## Section Headings

1. Introduction
2. Related Work
3. Methodology
   - 3.1 Training Landmark Tokens
   - 3.2 Inference
     - 3.2.1 Positional Encoding
   - 3.3 Memory & Computation
4. Experiments
   - 4.1 Language Modeling
   - 4.2 Fine-Tuning Pre-Trained Models
5. Future Work
6. Conclusion
Acknowledgment
