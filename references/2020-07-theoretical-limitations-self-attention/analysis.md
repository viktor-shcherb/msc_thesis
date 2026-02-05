---
title: "Theoretical Limitations of Self-Attention in Neural Sequence Models"
authors: "Hahn"
year: 2020
venue: "TACL 2020"
paper_type: journal-paper
categories: ["attention-analysis", "architecture"]
scope: ["computational expressiveness of self-attention", "formal language recognition", "PARITY and Dyck languages", "hard vs soft attention", "depth reduction via input restrictions"]
benchmarks_used: []
models_introduced: []
models_evaluated: []
key_claims:
  - id: C1
    claim: "Hard attention transformers cannot model PARITY or 2DYCK; for any fixed-size hard attention transformer, there exist sufficiently long inputs that it must misclassify"
    evidence: "Corollary 2, Section 5"
    status: supported
  - id: C2
    claim: "For any hard attention transformer and any constant C in (0,1), there exists an input restriction fixing at most (1-C)n input symbols such that the transformer's output depends on at most a bounded number of inputs, independent of input length n"
    evidence: "Theorem 1, Section 5"
    status: supported
  - id: C3
    claim: "In soft attention transformers, exchanging a single input symbol changes the final-layer activation by O(1/n) with constants depending on parameter matrices"
    evidence: "Lemma 5, Section 6"
    status: supported
  - id: C4
    claim: "Soft attention transformers' cross-entropy on PARITY next-symbol prediction converges to unigram chance level as input length increases"
    evidence: "Theorem 6, Section 6"
    status: supported
  - id: C5
    claim: "Soft attention transformers' cross-entropy on 2DYCK next-symbol prediction is separated from the optimal cross-entropy by a constant epsilon > 0 as input length increases"
    evidence: "Theorem 6, Section 6"
    status: supported
  - id: C6
    claim: "The depth reduction method generalizes to all sufficiently sensitive languages: if fixing a constant fraction of inputs cannot force language membership, then hard attention transformers cannot recognize the language"
    evidence: "Section 5, Discussion paragraph"
    status: supported
  - id: C7
    claim: "Proving that soft attention transformers cannot achieve perfect accuracy on evaluating Boolean formulas would separate complexity classes LTC^0 and NC^1, a major open problem"
    evidence: "Section 6, Footnote 3"
    status: supported
cross_references:
  - target: 2017-12-attention-is-all-you-need
    type: extends
    detail: "Proves fundamental computational limitations of the self-attention mechanism introduced by Vaswani et al."
  - target: 2024-12-transformers-need-glasses-over-squashing
    type: extended-by
    detail: "Barbero et al. extend the theoretical analysis to decoder-only Transformers, proving representational collapse and over-squashing that cause counting and copying failures"
  - target: 2019-07-specialized-attention-heads-pruning
    type: complementary
    detail: "Voita et al. provide empirical evidence that trained attention heads concentrate on few positions, supporting the relevance of the hard attention analysis"
open_questions:
  - question: "Can non-asymptotic bounds be derived that quantify exactly how many layers and heads are needed for a transformer to solve PARITY or 2DYCK up to a given input length?"
    addressed_by: null
  - question: "Does the practical success of transformers on natural language imply that natural language is approximable by counter-free (star-free) regular languages, or are other mechanisms (e.g., large parameter counts, approximate solutions) responsible?"
    addressed_by: null
  - question: "Can the depth reduction method be tightened to yield non-asymptotic accuracy bounds for soft attention transformers, or does the LTC^0 vs NC^1 barrier fundamentally prevent this?"
    addressed_by: null
  - question: "How do extensions of self-attention with recurrence (Universal Transformers, Transformer-XL) change the formal language recognition capabilities?"
    addressed_by: null
---

# Theoretical Limitations of Self-Attention in Neural Sequence Models

**Author:** Michael Hahn (Stanford University)
**Date:** 2020, TACL Volume 8:156--171 (arXiv:1906.06755)

---

## Core Research Problem

Transformers built entirely on self-attention have achieved state-of-the-art results across NLP tasks, yet their computational expressiveness relative to recurrent architectures is poorly understood. Prior work suggested informally that the lack of sequential processing limits transformers (Dehghani et al., 2019; Shen et al., 2018a; Chen et al., 2018; Hao et al., 2019), but no formal proofs existed. Experimental evidence from Tran et al. (2018) suggested LSTMs are better at learning hierarchical structure, while analysis studies showed that BERT encodes syntactic knowledge (Clark et al., 2019; Lin et al., 2019; Tenney et al., 2019).

The theoretical study of self-attention had only recently begun: Perez et al. (2019) showed that Seq2Seq Transformers with unbounded decoding steps can emulate Turing machines, and Hsieh et al. (2019) studied adversarial robustness of a single attention head under distributional assumptions. Neither addressed **limitations** of self-attention.

Meanwhile, the computational power of RNNs was well-studied: finite-precision LSTMs recognize a subset of counter languages (Merrill, 2019), arbitrary-precision RNNs can emulate pushdown automata (Korsky and Berwick, 2019), and RNNs with unlimited computation time can emulate Turing machines (Siegelman and Sontag, 1995).

**The core question: can models built entirely on self-attention, with a fixed number of layers and heads, recognize fundamental formal languages (periodic regular languages and context-free languages) as input length grows without bound?**

---

## Problem Solutions

The paper proves that fixed-size self-attention transformers **cannot** recognize two fundamental formal languages:

1. **PARITY** (the set of bitstrings with an even number of 1s) -- a simple periodic regular language that represents the simplest non-counter-free language.
2. **2DYCK** (correctly bracketed strings with two bracket types) -- a context-free language that models hierarchical structure, via the Chomsky-Schutzenberger theorem.

The results hold for both hard and soft attention, using different proof techniques:

- **Hard attention:** A depth reduction method inspired by Boolean circuit lower bounds (Furst et al., 1984), adapted to handle real-valued activations. The proof constructs input restrictions that "capture" the attention of each layer, forcing the transformer to ignore almost all input positions.
- **Soft attention:** A Lipschitz continuity argument showing that the influence of any single input on the final activation decays as O(1/n), preventing robust modeling of input-sensitive languages.

---

## Approach Details

### Method

The paper considers transformers in the standard formulation of Vaswani et al. (2017). An input `x = x_1 ... x_n` from a finite alphabet V is encoded via input embeddings `v_i` and positional embeddings `p_i` into layer-0 activations:

> `y_i^(0) = f(v_i, p_i)`

Each layer `k` (k = 1, ..., L) computes attention scores and weighted combinations through `H` attention heads:

> `a_{i,j}^{(k,h)} = f_{k,h}^{att}(y_i^{(k-1)}, y_j^{(k-1)})`

> `b_{i,k,h} = sum_j hat{a}_{i,j}^{(k,h)} y_j^{(k-1)}`

> `y_i^{(k)} = f^{act}(y_i^{(k-1)}, b_{i,k,1}, ..., b_{i,k,H})`

where `f^{act}` is a feedforward network with skip connection.

Language recognition is formalized as classifying the final activation `y_n^{(L)}` (after reading an end-of-sequence symbol) into class 1 (in the language) or 0 (not in the language).

### Theoretical Analysis

#### Hard Attention Results

**Theorem 1 (Main result).** Let any hard attention transformer be given, and let `C in (0, 1)`. Then there is an input restriction `rho` and an integer `c > 0` such that `|{i <= n : rho_n(i) = *}| >= Cn` for all sufficiently large `n`, and the function computed by the transformer on the restricted input depends only on `<= c` inputs, independent of input length `n`.

An **input restriction** `rho` is a family of maps `rho_n : {1, ..., n} -> {*, 0, 1}` that fixes some input positions to specific values while leaving others free (`*`). The theorem states that for any transformer, one can fix a small fraction of inputs to "attract" the attention, rendering the transformer dependent on only a bounded number of remaining inputs.

**Corollary 2.** Transformers with hard attention cannot model PARITY or 2DYCK.

*Proof sketch for PARITY:* After applying the restriction, the transformer depends on `c` inputs. For sufficiently large `n`, there exist unrestricted inputs that do not influence the output. But flipping a single bit changes PARITY membership, so the transformer must misclassify.

*Proof sketch for 2DYCK:* Even the simpler 1DYCK (single bracket type) cannot be solved. By pre-restricting the first 0.2n positions to `(` and the last 0.2n to `)`, then applying the theorem with `C = 0.9`, the restricted input is compatible with both well-bracketed and non-well-bracketed strings, but the prediction depends on only boundedly many positions.

**Discussion of sensitive vs. insensitive languages.** Languages immune to the depth reduction method are those where fixing a few inputs can force membership. For example:
- `1*` (all-ones strings): a single `0` forces non-membership, so a transformer can attend to a zero and reject.
- `a^n b^n`: a single `a` in the second half forces non-membership.

The depth reduction applies to all **sufficiently sensitive** languages: if, for some `C in (0, 1)`, fixing `Cn` symbols cannot force membership, then hard attention transformers cannot recognize the language.

#### Depth Reduction Lemma

The proof proceeds by iteratively removing layers. A technical generalization, the **c-Transformer**, allows layer-0 activations to depend on at most `c` input positions (rather than just one):

> `y_j^{(0)} = f_{n,j}^{inp}((v_{i_1}, p_{i_1}), ..., (v_{i_c}, p_{i_c}))`

**Lemma 4 (Depth Reduction Lemma).** Given a c-transformer with `L` layers and a restriction preserving at least `Cn` free inputs, one can find a new restriction preserving at least `C'n` free inputs (`C' < C`) such that the function is computed by a `(c * (2^c * k * H + 1))`-transformer with `L - 1` layers.

The proof constructs restrictions in three stages:

1. **Stage 1:** Ensure each input feeds into at most `(1/eta) * c/C` layer-0 activations by fixing the few inputs that violate this bound.
2. **Stage 2:** Iteratively fix inputs to "satisfy" layer-1 attention heads -- ensuring each head attends to at most `k` positions -- until every head's attention is captured.
3. **Stage 3:** Apply the probabilistic method with the Lovasz Local Lemma to show a suitable random restriction exists that avoids all failure events, using exponential decay (equation 9) and Chernoff bounds (equation 8).

Iterating the Depth Reduction Lemma `L` times removes all layers, leaving the output dependent on a bounded number of inputs.

#### Soft Attention Results

**Lemma 5.** For a soft attention transformer with input length `n`, exchanging one input symbol `x_i` (`i < n`) changes the final activation `y_n^{(L)}` by at most `O(1/n)`, with constants depending on parameter matrices.

*Proof:* By induction over layers `k = 1, ..., L`:

> `||y_i^{(k)} - y_i^{(k)'}|| <= C^{2k} D = O(1)`

> `||y_j^{(k)} - y_j^{(k)'}|| <= H^k C^{2k} D / n = O(1/n)` for `j != i`

The key insight: each attention weight is upper bounded by `exp(2A) / (n - 1)` where `A` bounds the attention logits. This makes the influence of any single position vanish as `n` grows. The constant `C = 2 * (1 + exp(2A) + L_{f^{act}})` where `L_{f^{act}}` is the Lipschitz constant of the ReLU feedforward network.

This contrasts with RNNs, where a single input flip can have nonnegligible impact on the hidden state regardless of sequence length (e.g., an RNN tracking parity flips its state on every `1`).

**Theorem 6.** For soft attention transformers:
- **PARITY:** Cross-entropy on next-symbol prediction converges to unigram chance level as `n -> infinity`.
- **2DYCK:** Cross-entropy is separated from the optimal cross-entropy by at least `P_0 * (1 - p) * log 2 > 0`, where `P_0` is the probability that a prefix ends with a closing bracket and is unbalanced, and `p` is the PCFG expansion probability.

*Proof idea for 2DYCK:* With constant probability, a prefix `x` ends with a closing bracket and is unbalanced, so the bracket type of the next closing bracket is fully determined. But there exists `x'` differing in one position where the other bracket type is required. Since the transformer's outputs for `x` and `x'` differ by `O(1/n)`, it cannot reliably distinguish which bracket type to predict, incurring at-chance cross-entropy (`log 2`) on bracket type selection.

#### Complexity-Theoretic Barrier

The paper notes (Footnote 3) that proving soft attention transformers cannot achieve perfect **accuracy** on Boolean formula evaluation would separate the complexity classes `LTC^0` and `NC^1`, a widely conjectured but long-open problem. This is why the soft attention results are limited to cross-entropy bounds rather than accuracy bounds.

---

## Limitations and Failure Modes

1. **Asymptotic nature of results.** All theorems are asymptotic: they show failures for "sufficiently long" inputs. For any fixed bound `N` on input length, a transformer with enough layers and heads can achieve perfect accuracy on all inputs of length `<= N`. The number of heads/layers or parameter norms must grow with `N`, but the paper does not provide non-asymptotic bounds on how they must grow.

2. **Practical relevance caveat.** The author explicitly notes that "practical implementations of transformers might thus be able to circumvent such asymptotic limitations by using large numbers of layers and heads, in relation to the sentence lengths typically occurring in natural language" (Section 7).

3. **Soft attention results are weaker.** The soft attention results bound only cross-entropy, not accuracy. The complexity-theoretic barrier (`LTC^0` vs `NC^1`) prevents obtaining accuracy bounds with current mathematical methods.

4. **Smoothness assumption.** The soft attention results assume Lipschitz-continuous activation functions (e.g., ReLU with softmax output), which covers standard implementations but excludes hypothetical non-smooth architectures.

5. **Fixed architecture only.** The results apply to transformers with a fixed number of layers and heads. They do not cover architectures where depth or width scales with input length (e.g., Universal Transformers, or adaptive-depth models).

6. **No empirical validation.** The paper is purely theoretical and does not include experiments demonstrating the predicted failures in practice.

---

## Conclusions

### Contributions

1. **First theoretical impossibility results for self-attention.** Proved that fixed-size transformers with hard attention cannot recognize PARITY or 2DYCK, using a novel depth reduction method adapted from Boolean circuit complexity (Theorem 1, Corollary 2).

2. **Soft attention sensitivity bound.** Showed that the influence of any single input symbol on a soft attention transformer's output decays as `O(1/n)` (Lemma 5), a fundamental property distinguishing self-attention from recurrent architectures.

3. **Cross-entropy lower bounds for soft attention.** Proved that soft attention transformers cannot achieve optimal cross-entropy on PARITY or 2DYCK distributions (Theorem 6), with PARITY converging to chance and 2DYCK being bounded away from optimal by a constant.

4. **Generalization to sensitive languages.** The depth reduction method applies to any language that is "sufficiently sensitive" -- where fixing a constant fraction of inputs cannot force membership (Section 5 Discussion).

5. **Identification of complexity-theoretic barrier.** Identified that obtaining accuracy bounds for soft attention would require separating `LTC^0` from `NC^1` (Footnote 3), explaining why the soft attention results are necessarily weaker.

### Implications

1. **Self-attention has provably restricted expressivity compared to recurrence.** LSTMs can perfectly model any regular language (including PARITY) and, with infinite precision, all deterministic context-free languages, while self-attention cannot. This theoretically confirms experimental findings of Tran et al. (2018).

2. **Natural language may not require full context-free power.** The practical success of transformers despite these limitations suggests that natural language can be approximated well with models too weak for the formal languages assumed in theoretical linguistics (speculative; stated by the author).

3. **Connection to human processing limitations.** Self-attention bears resemblance to cue-based retrieval models of human sentence processing (Lewis and Vasishth, 2005), which also predict difficulty with center embeddings (speculative).

---

## Key Claims

1. **C1: Hard attention cannot model PARITY or 2DYCK.** Any fixed-size hard attention transformer will misclassify inputs of sufficient length for both PARITY and 2DYCK. This holds without assumptions on activation functions or parameter norms. (Corollary 2, Section 5) -- **supported**

2. **C2: Input restrictions can force bounded dependence.** For any hard attention transformer, one can fix at most `(1-C)n` input symbols and make the transformer's output depend on at most a constant number of inputs, independent of `n`. (Theorem 1, Section 5) -- **supported**

3. **C3: Soft attention sensitivity bound.** Changing one input symbol in a soft attention transformer changes the final-layer activation by `O(1/n)`. (Lemma 5, Section 6) -- **supported**

4. **C4: PARITY cross-entropy converges to chance.** Soft attention transformers' cross-entropy on PARITY next-symbol prediction converges to unigram chance level as input length increases. (Theorem 6, Section 6) -- **supported**

5. **C5: 2DYCK cross-entropy gap.** Soft attention transformers' cross-entropy on 2DYCK is bounded away from optimal by at least `P_0 * (1 - p) * log 2 > 0`. (Theorem 6, Section 6) -- **supported**

6. **C6: Generalization via sensitivity.** The depth reduction method applies to all languages where fixing a constant fraction of inputs cannot force membership/non-membership. (Section 5 Discussion) -- **supported**

7. **C7: Complexity barrier for soft attention accuracy.** Proving accuracy bounds for soft attention on Boolean formulas would separate `LTC^0` and `NC^1`. (Footnote 3, Section 6) -- **supported**

---

## Open Questions

1. **Non-asymptotic bounds.** Can tight non-asymptotic bounds be derived quantifying how many layers, heads, or what parameter norms are needed for a transformer to solve PARITY or 2DYCK up to input length `N`? *(Unresolved)*

2. **Natural language and counter-free languages.** Does the success of transformers imply that natural language is approximable by counter-free (star-free) regular languages, or are other mechanisms (large parameter counts, approximate solutions, chain-of-thought) responsible? *(Unresolved)*

3. **Soft attention accuracy bounds.** Can the depth reduction method or alternative techniques be adapted to yield accuracy bounds for soft attention, or does the `LTC^0` vs `NC^1` barrier fundamentally prevent this? *(Unresolved)*

4. **Recurrence-augmented architectures.** How do extensions of self-attention with recurrence (Universal Transformers, Transformer-XL) change formal language recognition capabilities? *(Unresolved)*

---

## Core References and Why They Are Referenced

### Self-Attention Architecture

- **Vaswani et al. (2017)** -- *Attention Is All You Need.* Introduced the Transformer architecture whose limitations are the subject of the paper.
- **Perez et al. (2019)** -- *On the Turing Completeness of Modern Neural Network Architectures.* Showed Seq2Seq Transformers with unbounded decoding can emulate Turing machines; contrasted with the fixed-computation setting studied here.
- **Hsieh et al. (2019)** -- *On the Robustness of Self-Attentive Models.* Provided a theoretical result on single-head robustness under distributional assumptions; Lemma 5 generalizes this result.

### Formal Language Theory and Computational Complexity

- **Chomsky and Schutzenberger (1963)** -- *The Algebraic Theory of Context-Free Languages.* Established that all context-free languages arise from DYCK languages, motivating 2DYCK as a fundamental test language.
- **Furst et al. (1984)** -- *Parity, Circuits, and the Polynomial-Time Hierarchy.* Proved that bounded-depth Boolean circuits cannot compute PARITY using input restrictions; the depth reduction method here adapts this approach.
- **McNaughton and Papert (1971)** -- *Counter-Free Automata.* Defined counter-free (star-free) languages; PARITY is the simplest non-counter-free regular language.

### Recurrent Network Expressiveness

- **Siegelman and Sontag (1995)** -- *On the Computational Power of Neural Nets.* Classical result that RNNs with unlimited computation can emulate Turing machines.
- **Merrill (2019)** -- *Sequential Neural Networks as Automata.* Showed finite-precision LSTMs recognize counter languages, GRUs and simple RNNs recognize regular languages.
- **Korsky and Berwick (2019)** -- *On the Computational Power of RNNs.* Showed arbitrary-precision RNNs can emulate pushdown automata and recognize deterministic context-free languages.
- **Weiss et al. (2018)** -- *On the Practical Computational Power of Finite Precision RNNs.* Experimentally and theoretically studied RNN capabilities on formal languages.

### Empirical Studies of Attention and Hierarchical Structure

- **Tran et al. (2018)** -- *The Importance of Being Recurrent for Modeling Hierarchical Structure.* Experimental evidence that LSTMs outperform transformers at learning hierarchical structure, which this paper theoretically confirms.
- **Voita et al. (2019)** -- *Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting.* Empirical evidence that trained attention concentrates on few positions, supporting relevance of hard attention analysis.
- **Clark et al. (2019)** -- *What Does BERT Look At?* Showed BERT attention patterns often concentrate, consistent with the hard attention setting.
