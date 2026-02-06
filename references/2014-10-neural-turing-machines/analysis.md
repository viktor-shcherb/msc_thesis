---
title: "Neural Turing Machines"
authors: "Graves, Wayne, Danihelka"
year: 2014
venue: "arXiv preprint"
paper_type: preprint
categories: ["architecture", "attention-efficiency"]
scope: ["memory-augmented neural networks", "algorithmic learning", "differentiable computing"]
benchmarks_used: []
models_introduced: []
models_evaluated: []
key_claims:
  - id: C1
    claim: "NTM learns copy task much faster than LSTM and generalises to sequences longer than training (up to 120 vs trained on 20)"
    evidence: "Figures 3-6, Section 4.1"
    status: supported
  - id: C2
    claim: "NTM learns associative recall significantly faster than LSTM, reaching near-zero cost in ~30K episodes vs LSTM not reaching zero after 1M episodes"
    evidence: "Figure 10, Section 4.3"
    status: supported
  - id: C3
    claim: "NTM with feedforward controller generalises nearly perfectly to 2x training sequence length on associative recall"
    evidence: "Figure 11, Section 4.3"
    status: supported
  - id: C4
    claim: "NTM achieves near-optimal performance on dynamic N-gram prediction, outperforming LSTM"
    evidence: "Figure 13, Section 4.4"
    status: supported
  - id: C5
    claim: "The entire NTM architecture is differentiable end-to-end and trainable with gradient descent"
    evidence: "Section 3, Equations 1-9"
    status: supported
cross_references:
  - target: 2020-04-compressive-transformer-pg19
    type: extended-by
    detail: "Compressive Transformer extends the memory-augmented approach with compression of old memories; the 'most-used' compression scheme is inspired by NTM's garbage collection concept"
open_questions:
  - question: "Can NTMs scale to more complex algorithmic tasks beyond simple copying, sorting, and associative recall?"
    addressed_by: null
  - question: "How does NTM performance compare to attention mechanisms in Transformers for sequence-to-sequence tasks?"
    addressed_by: 2017-12-attention-is-all-you-need
  - question: "Can the addressing mechanisms be improved to support more complex data structures like trees or graphs?"
    addressed_by: null
---

# Neural Turing Machines

**Authors:** Alex Graves, Greg Wayne, Ivo Danihelka (Google DeepMind)
**Date:** October 2014, arXiv:1410.5401

---

## Core Research Problem

Computer programs use three fundamental mechanisms: elementary operations, logical flow control (branching), and external memory that can be written to and read from during computation (Von Neumann, 1945). Despite wide-ranging success in modelling data, modern machine learning has largely neglected external memory.

Recurrent neural networks (RNNs) can learn complicated transformations over extended time periods and are theoretically Turing-Complete (Siegelmann and Sontag, 1995). However, what is possible in principle is not always simple in practice. Standard RNNs, including LSTM, store information in fixed-size hidden states that must encode all relevant past information. This creates fundamental limitations:

1. **Memory capacity is bounded** by the hidden state dimension, which grows quadratically with the number of LSTM parameters.
2. **Long-range dependencies** are difficult to learn due to vanishing/exploding gradients, even with LSTM's gating mechanisms.
3. **Variable binding** -- the assignment of data to specific memory slots -- is not explicitly supported, limiting algorithmic reasoning.

The core challenge is: **how to extend neural networks with external, addressable memory that supports both content-based and location-based access, while remaining fully differentiable for end-to-end training with gradient descent.**

---

## Problem Solutions

The paper proposes the **Neural Turing Machine (NTM)**, a neural network architecture that couples a controller network to an external memory matrix via attention-based read and write operations. The solution rests on three key components:

1. **External memory matrix.** An N x M memory bank where N is the number of locations and M is the vector dimension at each location. Unlike LSTM's hidden state, memory size can be increased without changing the controller's parameters.

2. **Attention-based addressing.** Read and write operations use normalised weightings over memory locations, computed via content-based similarity (like Hopfield networks) and location-based shifting (for iteration). This makes all operations differentiable.

3. **Separation of memory and computation.** The controller (feedforward or LSTM) determines what to read/write and where, while the memory matrix stores the data. This separation allows the network to learn algorithms that generalise beyond training sequence lengths.

---

## Approach Details

### Method

The NTM architecture consists of two components: a neural network **controller** and a **memory matrix** M_t of size N x M. The controller interacts with external inputs/outputs and with memory via **read heads** and **write heads** (Figure 1, Section 3).

At each time step t:
1. The controller receives external input and read vectors from the previous step
2. The controller emits output and head parameters (keys, strengths, gates, shifts)
3. Read and write heads interact with memory using attention-based addressing
4. Memory is updated based on write operations

**Reading (Section 3.1).** Given a weighting vector w_t over N locations (normalised: sum to 1, all elements in [0,1]), the read vector r_t is a convex combination of memory rows:

> r_t = sum_i w_t(i) M_t(i)

**Writing (Section 3.2).** Inspired by LSTM's input and forget gates, writing decomposes into erase and add operations. Given weighting w_t, erase vector e_t (elements in (0,1)), and add vector a_t:

> M̃_t(i) = M_{t-1}(i) [1 - w_t(i) e_t]  (erase)
> M_t(i) = M̃_t(i) + w_t(i) a_t  (add)

Both operations are differentiable with respect to all parameters.

### Key Technical Components

**Addressing Mechanism (Section 3.3).** The weighting vector w_t is produced by combining content-based and location-based addressing through four stages (Figure 2):

1. **Content addressing.** Each head emits a key vector k_t and key strength β_t. The content-based weighting is:

> w^c_t(i) = exp(β_t K[k_t, M_t(i)]) / sum_j exp(β_t K[k_t, M_t(j)])

where K[u,v] = (u · v) / (||u|| · ||v||) is cosine similarity.

2. **Interpolation.** A scalar gate g_t in (0,1) blends between the content weighting and the previous time step's weighting:

> w^g_t = g_t w^c_t + (1 - g_t) w_{t-1}

This allows the head to ignore content addressing and continue from its previous location.

3. **Convolutional shift.** A shift weighting s_t (normalised distribution over allowed integer shifts, e.g., {-1, 0, 1}) rotates the weighting via circular convolution:

> w̃_t(i) = sum_{j=0}^{N-1} w^g_t(j) s_t(i - j mod N)

4. **Sharpening.** A scalar γ_t >= 1 sharpens the final weighting to counteract dispersion from repeated shifts:

> w_t(i) = w̃_t(i)^{γ_t} / sum_j w̃_t(j)^{γ_t}

**Controller Network (Section 3.4).** The controller can be either feedforward or recurrent (LSTM). Feedforward controllers offer greater interpretability but are limited to unary/binary operations per time step based on the number of read heads. LSTM controllers have internal memory that complements the external matrix.

### Experimental Setup

Five algorithmic tasks were used to evaluate NTM (Section 4):

**Copy task (Section 4.1):** Input a sequence of 8-bit random vectors (length 1-20), followed by a delimiter; output the same sequence. Tests storage and recall.

**Repeat copy task (Section 4.2):** Same as copy, but output the sequence a specified number of times (1-10), then emit an end marker. Tests nested iteration.

**Associative recall (Section 4.3):** Input a sequence of 2-6 items (each item = 3 six-bit vectors bounded by delimiters), then query with one item; output the next item in the sequence. Tests content-based lookup with indirection.

**Dynamic N-grams (Section 4.4):** Predict next bit in a sequence generated from a random 6-gram distribution (200 bits per sequence). Tests rapid adaptation to new distributions. Optimal Bayesian estimator: P(B=1|N_1, N_0, c) = (N_1 + 0.5) / (N_1 + N_0 + 1).

**Priority sort (Section 4.5):** Input 20 random 8-bit vectors with scalar priorities in [-1, 1]; output the 16 highest-priority vectors in sorted order. Tests sorting algorithms.

**Training details (Section 4.6):**
- Optimiser: RMSProp with momentum 0.9
- Gradient clipping: elementwise to (-10, 10)
- Memory size: 128 x 20 for all tasks
- All tasks use binary targets with cross-entropy loss
- LSTM baselines: 3 stacked hidden layers

| Task | #Heads | Controller Size | Learning Rate | #Params (FF) | #Params (LSTM ctrl) |
|---|---|---|---|---|---|
| Copy | 1 | 100 | 10^-4 | 17,162 | 67,561 |
| Repeat Copy | 1 | 100 | 10^-4 | 16,712 | 66,111 |
| Associative | 4 (FF) / 1 (LSTM) | 256 / 100 | 10^-4 | 146,845 | 70,330 |
| N-Grams | 1 | 100 | 3x10^-5 | 14,656 | 61,749 |
| Priority Sort | 8 (FF) / 5 (LSTM) | 512 / 2x100 | 3x10^-5 | 508,305 | 269,038 |

### Key Results

**Copy task (Figure 3):**

| Model | Convergence (sequences) | Final cost |
|---|---|---|
| LSTM (3x256) | >1M | ~2 bits |
| NTM (LSTM controller) | ~200K | ~0 bits |
| NTM (Feedforward controller) | ~100K | ~0 bits |

- NTM learns ~10x faster than LSTM and converges to lower cost
- NTM generalises to sequences of length 120 (trained on max 20); LSTM fails beyond length 20 (Figures 4-5)
- NTM learns an interpretable algorithm: write inputs sequentially, return to start, read sequentially (Figure 6, pseudocode in Section 4.1)

**Repeat copy task (Figure 7):**
- Both NTM and LSTM solve the task perfectly on training distribution
- NTM generalises to longer sequences and more repetitions; LSTM fails both (Figure 8)
- NTM uses iterative reads with a "goto" mechanism to return to sequence start (Figure 9)

**Associative recall (Figures 10-11):**

| Model | Episodes to near-zero cost | Generalisation (12 items, trained on 6) |
|---|---|---|
| LSTM | >1M (never reaches zero) | ~35 bits |
| NTM (LSTM controller) | ~50K | ~5 bits |
| NTM (Feedforward controller) | ~30K | ~0 bits |

- NTM learns content-based lookup: compresses each item into a representation stored at the delimiter, uses content addressing to find the query, then shifts by 1 to read the next item (Figure 12)

**Dynamic N-grams (Figure 13):**

| Model | Final cost (bits/sequence) | vs Optimal |
|---|---|---|
| Optimal Bayesian | ~133 | -- |
| NTM (Feedforward) | ~135 | +2 |
| NTM (LSTM controller) | ~136 | +3 |
| LSTM | ~137 | +4 |

- NTM approaches optimal performance and outperforms LSTM
- Memory analysis suggests NTM counts context-specific ones and zeros (Figure 15)

**Priority sort (Figure 18):**
- NTM substantially outperforms LSTM
- NTM uses priority values to determine write locations via a linear mapping (Figure 17)
- Requires 8 parallel read/write heads for feedforward controller (reflecting sorting complexity)

---

## Limitations and Failure Modes

- **Limited task complexity.** The experiments are restricted to simple algorithmic tasks (copy, sort, associative recall). Scaling to more complex programs is not demonstrated.

- **Repeat copy counting limitation.** NTM succeeds at longer sequences and more repetitions than training but cannot correctly predict the end marker beyond 10 repetitions when the repeat count is represented numerically (Figure 8, Section 4.2).

- **Priority sort requires many heads.** The feedforward controller needed 8 parallel read/write heads for best performance on sorting, suggesting difficulty with complex operations using unary transformations (Section 4.5).

- **Dynamic N-gram sub-optimality.** NTM approaches but never quite reaches optimal Bayesian performance on the N-gram task, occasionally accessing wrong memory locations (Figure 14-15, Section 4.4).

- **No language modelling evaluation.** The paper does not evaluate on standard language modelling benchmarks, making comparison with subsequent work difficult.

- **Fixed memory size.** The memory matrix has fixed size N x M; there is no mechanism for dynamic allocation or memory management.

---

## Conclusions

### Contributions

1. **Differentiable external memory.** The NTM architecture couples a neural network controller to an external memory matrix via attention-based read and write operations that are fully differentiable, enabling end-to-end training with gradient descent (Section 3).

2. **Combined content and location addressing.** The addressing mechanism supports both content-based lookup (via key similarity) and location-based iteration (via convolutional shifts), allowing the network to learn algorithms that combine random access with sequential traversal (Section 3.3).

3. **Learning from algorithmic examples.** NTM can infer simple algorithms (copying, sorting, associative recall) from input-output examples and generalise well beyond training sequence lengths, unlike LSTM which fails to generalise (Section 4).

4. **Interpretable memory access patterns.** The attention-based addressing produces interpretable memory access patterns that can be analysed to understand the learned algorithms (Figures 6, 9, 12, 15, 17).

5. **Separation of memory and computation.** By decoupling memory capacity from controller parameters, NTM's memory can be increased without quadratic parameter growth (unlike LSTM), enabling scalable storage (Section 3.4).

### Implications

1. **Memory-augmented architectures are a viable path to algorithmic learning.** The dramatic gap between NTM and LSTM on generalisation suggests that explicit external memory is crucial for learning algorithms, not just memorising training examples. [Inference: this insight influenced subsequent work on memory-augmented networks and attention mechanisms.]

2. **Attention as a general-purpose memory access mechanism.** The paper demonstrates that soft attention can implement both content-based retrieval (like associative memory) and location-based iteration (like array indexing), providing a unified differentiable interface to memory. [Inference: this attention mechanism is a precursor to the attention in Transformers, though the Transformer uses it differently.]

3. **Neural networks can learn to use working memory.** The analogy to human working memory and Turing machines suggests that neural architectures can bridge the gap between connectionist and symbolic computation, learning to manipulate rapidly-created variables rather than deploying fixed procedures (Section 1).

---

## Key Claims

1. **C1: NTM learns copy faster and generalises to longer sequences than LSTM.** On the copy task, NTM converges ~10x faster than LSTM and achieves near-zero error. NTM generalises to sequences of length 120 (6x training max of 20), while LSTM fails beyond length 20 (Figures 3-5, Section 4.1). Status: **supported**.

2. **C2: NTM learns associative recall significantly faster than LSTM.** NTM with feedforward controller reaches near-zero cost in ~30K episodes; LSTM does not reach zero after 1M episodes (Figure 10, Section 4.3). Status: **supported**.

3. **C3: NTM generalises to 2x training length on associative recall.** NTM with feedforward controller is nearly perfect for 12 items (trained on max 6) and has <1 bit error for 15 items (Figure 11, Section 4.3). Status: **supported**.

4. **C4: NTM approaches optimal Bayesian performance on dynamic N-grams.** NTM achieves ~135 bits/sequence vs optimal ~133 bits, outperforming LSTM at ~137 bits (Figure 13, Section 4.4). Status: **supported**.

5. **C5: NTM is differentiable end-to-end.** All operations (reading, writing, addressing) are defined as differentiable functions of the controller outputs and memory contents, enabling training with gradient descent (Section 3, Equations 1-9). Status: **supported**.

---

## Open Questions

1. **Can NTMs scale to more complex algorithmic tasks?** The paper demonstrates only simple tasks (copy, sort, lookup). Whether NTMs can learn more complex algorithms (graph traversal, recursion, arithmetic) remains open. Not directly addressed in this directory, though subsequent work (Differentiable Neural Computer, 2016) extended the approach.

2. **How does NTM compare to Transformer attention for sequence tasks?** The Transformer (Vaswani et al., 2017) uses attention differently -- attending to all positions in parallel rather than via sequential read/write operations. The relative merits for different tasks are not explored. Partially addressed by subsequent Transformer work.

3. **Can addressing mechanisms support complex data structures?** The NTM memory is a flat array. Supporting trees, graphs, or nested structures would require more sophisticated addressing. Not addressed.

4. **How does memory capacity affect learning and generalisation?** The paper uses fixed 128x20 memory for all tasks. The relationship between memory size, task complexity, and generalisation is not systematically studied.

---

## Core References and Why They Are Referenced

### Computational Foundations

- **Von Neumann (1945)** -- *First Draft of a Report on the EDVAC.* The foundational computer architecture with separate memory and processing, which NTM emulates in a differentiable form.

- **Siegelmann and Sontag (1995)** -- *On the Computational Power of Neural Nets.* Proves RNNs are Turing-Complete, establishing that the limitations NTM addresses are practical rather than theoretical.

- **Turing (1936)** -- Implicit reference. The NTM name invokes Turing's enrichment of finite-state machines with infinite memory tape; NTM enriches RNNs with external memory.

### Neural Network Architectures

- **Hochreiter and Schmidhuber (1997)** -- *Long Short-Term Memory.* The LSTM architecture that NTM extends with external memory. LSTM's gating mechanism inspires NTM's erase/add decomposition.

- **Hopfield (1982)** -- *Neural Networks and Physical Systems with Emergent Collective Computational Abilities.* Content-based addressing in NTM is related to Hopfield networks' content-addressable memory.

### Attention Mechanisms

- **Graves (2013)** -- *Generating Sequences with Recurrent Neural Networks.* Differentiable attention for handwriting synthesis; precursor to NTM's attention-based addressing.

- **Bahdanau et al. (2014)** -- *Neural Machine Translation by Jointly Learning to Align and Translate.* Concurrent work on attention for sequence-to-sequence models; similar soft attention mechanism applied to different problem.

### Cognitive Science and Working Memory

- **Baddeley et al. (2009)** -- *Memory.* The psychological model of working memory with a "central executive" and memory buffer, which NTM's controller-memory architecture mirrors.

- **Miller (1956)** -- *The Magical Number Seven.* Working memory capacity limits that motivate the need for external memory beyond the controller's internal state.

- **Fodor and Pylyshyn (1988)** -- *Connectionism and Cognitive Architecture.* The critique that neural networks cannot perform variable binding; NTM addresses this by providing explicit memory slots for variable storage.

### Prior Memory-Augmented Networks

- **Hazy et al. (2006)** -- *Banishing the Homunculus: Making Working Memory Work.* Neural model with gated memory slots analogous to LSTM, but lacking sophisticated addressing.

- **Das et al. (1992)** -- *Learning Context-Free Grammars.* RNN with external stack memory; precursor to differentiable memory-augmented networks.
