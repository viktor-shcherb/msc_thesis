# Autoregressive Language Modeling [p. 4-6]

[p. 4-5] Autoregressive or left-to-right language modeling is loosely defined as estimating the probability distribution of an existing token/character given its previous tokens/characters in an input sequence. This task is considered one of the fundamental tasks in natural language and recent prior work on modeling long sequences using transformers has relied on this task as their primary evaluation (Dai et al., 2019; Rae et al., 2020; Sukhbaatar et al., 2019). Similarly, the authors develop and evaluate their model on autoregressive language modeling.

## 4.1 Attention Pattern

[p. 5] For autoregressive language modeling, the dilated sliding window attention is used. Following Sukhbaatar et al. (2019), different window sizes are used across the layers. In particular, small window sizes for the lower layers and increased window sizes moving to higher layers. This allows the top layers to learn higher-level representation of the entire sequence while having the lower layers capture local information. In addition, it provides balance between efficiency (smaller window sizes are less computationally expensive due to fewer nonzero values) and performance (larger window sizes have richer representation power and often result in performance improvements).

Dilated sliding windows are not used for lower layers to maximize their capacity to learn and utilize the immediate local context. For the higher layers, a small amount of increasing dilation is used only on 2 heads. This gives the model the ability to directly attend to distant tokens without sacrificing local context.

## 4.2 Experiment Setup

[p. 5] Comparison to prior work focuses on character-level LM (`text8` and `enwik8`; Mahoney, 2009).

### Training

[p. 5] A staged training procedure is adopted where the attention window size and sequence length are increased across multiple training phases. In the first phase, start with a short sequence length and window size, then on each subsequent phase, double the window size and the sequence length, and halve the learning rate. This makes training fast, while keeping the slow part (longest sequences and window sizes) to the end. The model is trained over 5 total phases with starting sequence length of 2,048 and ending sequence length of 23,040 on the last phase (see Appendix B for detailed configurations of each phase, and for all other hyperparameters).

### Evaluation

[p. 5] Evaluation with sequences of length 32,256. Following Dai et al. (2019), the dataset is split into overlapping sequences of size 32,256 with a step of size 512, and performance is reported on the last 512 tokens on the sequence.

## 4.2.1 Results

[p. 5] Tab. 2 and Tab. 3 summarize evaluation results on `text8` and `enwik8` datasets.

- New state-of-the-art on both `text8` and `enwik8` using the small models with BPC of **1.10** on `text8` and **1.00** on `enwik8` respectively.
- For large models, given how expensive these experiments are, and following recent work (Kitaev et al., 2020; Rae et al., 2020), the authors evaluate only on `enwik8`. Tab. 3 shows that Longformer outperforms the comparable Transformer-XL model, matches the performance of the comparable Sparse Transformer (Child et al., 2019), and matches or slightly underperforms recent models that have more than twice the number of parameters.
- Adaptive Span (Sukhbaatar et al., 2019) and Compressive Transformer (Rae et al., 2020) are noted as not a good fit for the pretraining-finetuning paradigm as discussed in section 2.

### Table 2: Small model BPC on `text8` & `enwik8` [p. 5]

| Model | #Param | Dev | Test |
|---|---|---|---|
| **Dataset `text8`** | | | |
| T12 (Al-Rfou et al., 2018) | 44M | - | 1.18 |
| Adaptive (Sukhbaatar et al., 2019) | 38M | 1.05 | 1.11 |
| BP-Transformer (Ye et al., 2019) | 39M | - | 1.11 |
| Our Longformer | 41M | 1.04 | **1.10** |
| **Dataset `enwik8`** | | | |
| T12 (Al-Rfou et al., 2018) | 44M | - | 1.11 |
| Transformer-XL (Dai et al., 2019) | 41M | - | 1.06 |
| Reformer (Kitaev et al., 2020) | - | - | 1.05 |
| Adaptive (Sukhbaatar et al., 2019) | 39M | 1.04 | 1.02 |
| BP-Transformer (Ye et al., 2019) | 38M | - | 1.02 |
| Our Longformer | 41M | 1.02 | **1.00** |

### Table 3: Performance of *large* models on `enwik8` [p. 5]

| Model | #Param | Test BPC |
|---|---|---|
| Transformer-XL (18 layers) | 88M | 1.03 |
| Sparse (Child et al., 2019) | ~100M | 0.99 |
| Transformer-XL (24 layers) | 277M | 0.99 |
| Adaptive (Sukhbaatar et al., 2019) | 209M | 0.98 |
| Compressive (Rae et al., 2020) | 277M | 0.97 |
| Routing (Roy et al., 2020) | ~223M | 0.99 |
| Our Longformer | 102M | 0.99 |

## 4.2.2 Ablation Study

[p. 6] To show the importance of the design choices of the attention patterns, different variants are tried and controlled experiment results reported. To make the ablation study more manageable, each configuration is trained for 150K steps^4 with phase 1 configuration on a small model on `text8`, then BPC performance is reported on the dev set.

^4 One caveat is that the ordering of end performance will not agree with that at step 150K. However, this approximation saves the huge cost of running every experiment to completion. [p. 6, footnote 4]

### Table 4: Changing window size across layers & dilation impact [p. 6]

**Top: changing window size across layers. Bottom: with/without dilation (@ 150K steps on phase1)**

| Model | Dev BPC |
|---|---|
| Decreasing w (from 512 to 32) | 1.24 |
| Fixed w (= 230) | 1.23 |
| Increasing w (from 32 to 512) | **1.21** |
| | |
| No Dilation | 1.21 |
| Dilation on 2 heads | **1.20** |

Key findings:
- Increasing the window size from the bottom to the top layer leads to the best performance.
- Arranging them in the reverse way leads to worse performance.
- Using a fixed window size (the average of window sizes of the other configuration) leads to a performance that is in between.
- Adding dilation to two heads leads to some improvement compared with no dilation at all.
