# Introduction [p. 3–4]

## Overview

[p. 3] Advancements in Large Language Models (LLMs) have significantly impacted Natural Language Processing (NLP) tasks. The field has traditionally been dominated by the transformer architecture (Vaswani et al., 2023). However, the expressive attention mechanism of transformers leads them to suffer from quadratic time complexity with respect to input sequence length. Various methods have been proposed to achieve sub-quadratic time complexity without significantly changing the core attention mechanism, typically relying on some form of sparsity techniques (Child et al., 2019a; Beltagy et al., 2020; Zaheer et al., 2020).

Recent works have achieved sub-quadratic time complexity without significantly sacrificing performance by introducing new mechanisms to replace attention at the core of the Transformer architecture. These models include gated recurrences (Fu et al., 2023; Gu & Dao, 2024; Gu et al., 2021; Sun et al., 2023; Katsch, 2023; Qin et al., 2023; Smith et al., 2023), gated convolutions (Poli et al., 2023; Peng et al., 2023), data-dependent linear attention (Yang et al., 2023; Katharopoulos et al., 2020b), sparse attentions (Tay et al., 2020; Child et al., 2019b; Zaheer et al., 2020; Qiu et al., 2019) and their combinations (De et al., 2024; Qin et al., 2024; 2022). The authors build off RWKV-4 introduced in Peng et al. (2023), which provides efficient inference and training along with a parallelizable implementation compared to competing architectures as shown in Table 1.

### Table 1: Architecture Comparison [p. 3]

| Architecture | Inference Time | Inference Memory | Parallel | Training Time | Training Memory |
|--------------|----------------|------------------|----------|---------------|-----------------|
| LSTM/LMU | O(1) | O(1) | ✗ | O(N) | O(N) |
| Transformer | O(N) | O(N)^a | ✓ | O(N²) | O(N)^b |
| Linear Transformer | O(1) | O(1) | ✓ | O(N) | O(N) |
| H3/S4 | O(1) | O(1) | ✓ | O(N log N) | O(N) |
| Hyena | O(N) | O(N) | ✓ | O(N log N) | O(N) |
| RWKV/Mamba/RetNet | O(1) | O(1) | ✓ | O(N) | O(N) |

Caption: Comparative analysis of RWKV-4/5/6 and other LLM architectures regarding time and memory complexity for both inference per token and training per sequence, and training parallelizability across the sequence dimension. The context/sequence length is denoted by N.

^a O(1) without KV cache; ^b With Flash Attention

## Main Contributions

[p. 3–4] The paper introduces two new architectures: **Eagle** (RWKV-5) and **Finch** (RWKV-6). First, Eagle improves upon the architecture and learned schedule from RWKV-4 (Peng et al., 2023) through the use of expressive multi-headed matrix-valued states (as opposed to vector-valued states), a reformulated receptance, and an additional gating mechanism. Finch further improves the expressivity and flexibility of the architecture by introducing new data-dependent functions for both the time-mixing and token-shift modules, consisting of parameterized linear interpolations. Additionally, Finch proposes a novel use of the Low Rank Adaptation (Hu et al., 2022) function to allow for trainable weight matrices to efficiently augment the learned data decay vectors in a context-dependent manner. Finally, the authors introduce a new tokenizer, the RWKV World Tokenizer, and a new dataset, RWKV World v2 (1.12 trillion tokens), specially designed to improve performance on multilingual and code data.

[p. 4] Through extensive experimentation, the authors show that the Eagle and Finch models perform competitively, or improve upon existing models under a wide variety of sequence modeling domains and tasks. Specifically, they evaluate trained models on commonly used English-only and multilingual text benchmarks, associative recall, music modeling, and vision-language benchmarks. The experiments demonstrate that the advancements in Eagle and Finch provide significant progress towards developing more efficient AI models.

## Summary of Contributions

[p. 4] The main contributions are:

• The Eagle (RWKV-5) and Finch (RWKV-6) RWKV architectures, which significantly improve over RWKV-4 on benchmarks for LLMs.

• The RWKV World Tokenizer which contains underrepresented languages' vocabulary and which performs fast tokenization with trie-based greedy matching.

• The RWKV World v2 public dataset, comprised of 1.12 trillion tokens of publicly available multilingual data.

• Public release of four pre-trained Eagle models, scaling from 0.46 to 7.5 billion parameters, and two Finch models, with 1.6 and 3.1 billion parameters. The authors demonstrate that these novel architectures are competitive to transformers when trained using enough FLOPs to make meaningful scaling conclusions.

• A completely open training pipeline to enable interpretability and reproducibility of alternative-architecture LLMs (See Table 2).

### Table 2: Model Openness Comparison [p. 4]

| Model | Context Length | Training Tokens | Open Weights | Open Code Inference | Open Code Training | Open Dataset |
|-------|----------------|-----------------|--------------|---------------------|-------------------|--------------|
| GPT-4 | 128k^a | Undisclosed | ○ | ○ | ○ | ○ |
| LLaMA2 7B | 4k | 2.0 × 10^12 | ● | ● | ○ | ○ |
| Mistral 7B v0.1 | 32k^b | Undisclosed | ● | ● | ○ | ○ |
| Gemma 7B | 8k | 6.0 × 10^12 | ⦿ | ● | ● | ○ |
| StableLM 7B v2 | 4k | 1.1 × 10^12 | ● | ● | ● | ● |
| Pythia 6.9B | 2k | 3.3 × 10^11 | ● | ● | ● | ● |
| Eagle 7B | Indefinite^c | 1.1 × 10^12 | ● | ● | ● | ● |

Caption: Comparison of the openness and accessibility of public foundational LLMs with 7B+ parameters regarding model weights, official inference/training code, and dataset. Widely available but not under an open source license is indicated by ⦿.

^a OpenAI's gpt-4-0125-preview model; ^b With sliding window; ^c Pretrained with context length 4096, but no fundamental context length limitation or relationship to speed, see 8.3 for extrapolation details
