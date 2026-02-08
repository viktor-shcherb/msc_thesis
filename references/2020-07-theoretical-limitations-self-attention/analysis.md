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
    scope: "fixed number of layers and heads, hard attention (argmax), input length growing without bound"
    magnitude: "qualitative -- for any hard attention transformer, accuracy drops below 100% for sufficiently long inputs"
  - id: C2
    claim: "For any hard attention transformer and any constant C in (0,1), there exists an input restriction fixing at most (1-C)n input symbols such that the transformer's output depends on at most a bounded number of inputs, independent of input length n"
    evidence: "Theorem 1, Section 5"
    status: supported
    scope: "fixed-size hard attention transformers, arbitrary activation functions and parameter norms"
    magnitude: "qualitative -- output dependence reduced to a constant c independent of n, while preserving at least Cn free inputs"
  - id: C3
    claim: "In soft attention transformers, exchanging a single input symbol changes the final-layer activation by O(1/n) with constants depending on parameter matrices"
    evidence: "Lemma 5, Section 6"
    status: supported
    scope: "fixed-depth soft attention transformers with Lipschitz-continuous activations (e.g., ReLU with softmax), exchanging any position i < n"
    magnitude: "O(1/n) change in activation norm, with constant C = 2(1 + exp(2A) + L_{f^{act}})"
  - id: C4
    claim: "Soft attention transformers' cross-entropy on PARITY next-symbol prediction converges to unigram chance level as input length increases"
    evidence: "Theorem 6, Section 6"
    status: supported
    scope: "fixed-size soft attention transformers with Lipschitz-continuous activations, PARITY distribution with termination probability p"
    magnitude: "cross-entropy converges to unigram chance level (no better than predicting marginal symbol frequencies)"
  - id: C5
    claim: "Soft attention transformers' cross-entropy on 2DYCK next-symbol prediction is separated from the optimal cross-entropy by a constant epsilon > 0 as input length increases"
    evidence: "Theorem 6, Section 6"
    status: supported
    scope: "fixed-size soft attention transformers with Lipschitz-continuous activations, 2DYCK PCFG distribution with expansion probability p"
    magnitude: "cross-entropy gap of at least P_0 * (1 - p) * log 2 > 0, where P_0 is the probability prefix is unbalanced and ends with closing bracket"
  - id: C6
    claim: "The depth reduction method generalizes to all sufficiently sensitive languages: if fixing a constant fraction of inputs cannot force language membership, then hard attention transformers cannot recognize the language"
    evidence: "Section 5, Discussion paragraph"
    status: supported
    scope: "hard attention only, languages where for some C in (0,1) fixing Cn symbols cannot force membership"
    magnitude: "qualitative -- complete failure to recognize the language for sufficiently long inputs"
  - id: C7
    claim: "Proving that soft attention transformers cannot achieve perfect accuracy on evaluating Boolean formulas would separate complexity classes LTC^0 and NC^1, a major open problem"
    evidence: "Section 6, Footnote 3"
    status: supported
    scope: "general complexity-theoretic observation about soft attention and Boolean formula evaluation"
    magnitude: "qualitative -- identifies a complexity-theoretic barrier preventing accuracy bounds for soft attention"
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

**Authors:** Michael Hahn (Stanford University)
**Date:** 2020, TACL Volume 8:156--171, DOI: 10.1162/tacl_a_00306 (arXiv:1906.06755)

---

## Core Research Problem

Transformers built entirely on self-attention have achieved state-of-the-art results across NLP tasks, yet their **computational expressiveness** relative to recurrent architectures was poorly understood at the time of writing. Prior work suggested informally that the lack of sequential processing limits transformers (Dehghani et al., 2019; Shen et al., 2018a; Chen et al., 2018; Hao et al., 2019), but no formal proofs existed (Section 1). Experimental evidence from Tran et al. (2018) -- *The Importance of Being Recurrent for Modeling Hierarchical Structure* -- suggested LSTMs outperform transformers at learning hierarchical structure, while analysis studies showed that BERT encodes syntactic knowledge (Clark et al., 2019; Lin et al., 2019; Tenney et al., 2019).

The theoretical study of self-attention had only recently begun: Perez et al. (2019) -- *On the Turing Completeness of Modern Neural Network Architectures* -- showed that Seq2Seq Transformers with unbounded decoding steps can emulate Turing machines, and Hsieh et al. (2019) -- *On the Robustness of Self-Attentive Models* -- studied adversarial robustness of a single attention head under distributional assumptions (Section 2). Neither addressed **limitations** of self-attention.

Meanwhile, the computational power of RNNs was well-studied: finite-precision LSTMs recognize a subset of counter languages (Merrill, 2019), arbitrary-precision RNNs can emulate pushdown automata (Korsky and Berwick, 2019), and RNNs with unlimited computation time can emulate Turing machines (Siegelman and Sontag, 1995) (Section 2).

**The core question: can models built entirely on self-attention, with a fixed number of layers and heads, recognize fundamental formal languages (periodic regular languages and context-free languages) as input length grows without bound?**

---

## Problem Solutions

The paper proves that fixed-size self-attention transformers **cannot** recognize two fundamental formal languages:

1. **PARITY** (the set of bitstrings with an even number of 1s) -- a simple periodic regular language that represents the simplest non-counter-free language. Inability to compute PARITY entails inability to recognize any regular language whose syntactic morphism is not quasi-aperiodic (Barrington et al., 1992, Footnote 2, Section 4).
2. **2DYCK** (correctly bracketed strings with two bracket types) -- a context-free language that models hierarchical structure, via the Chomsky-Schutzenberger theorem (Chomsky and Schutzenberger, 1963; Section 4).

The results hold for both hard and soft attention, using different proof techniques:

- **Hard attention:** A depth reduction method inspired by Boolean circuit lower bounds (Furst et al., 1984), adapted to handle real-valued activations. The proof constructs input restrictions that "capture" the attention of each layer, forcing the transformer to ignore almost all input positions.
- **Soft attention:** A Lipschitz continuity argument showing that the influence of any single input on the final activation decays as O(1/n), preventing robust modeling of input-sensitive languages.

---

## Approach Details

### Method

The paper considers transformers in the standard formulation of Vaswani et al. (2017) (Section 3). An input `x = x_1 ... x_n` from a finite alphabet V is encoded via input embeddings `v_i` and positional embeddings `p_i` into layer-0 activations:

> `y_i^{(0)} = f(v_i, p_i)`

Each layer `k` (k = 1, ..., L) computes attention scores and weighted combinations through `H` attention heads (Section 3, equations 1--3):

> `a_{i,j}^{(k,h)} = f_{k,h}^{att}(y_i^{(k-1)}, y_j^{(k-1)})`

> `b_{i,k,h} = sum_{j=1}^{n} hat{a}_{i,j}^{(k,h)} y_j^{(k-1)}`

> `y_i^{(k)} = f^{act}(y_i^{(k-1)}, b_{i,k,1}, ..., b_{i,k,H})`

where `f^{act}` is a feedforward network with skip connection.

In the **soft attention** version, weights are obtained via softmax: `hat{a}_{i,*}^{(k,h)} = softmax(a_{i,*}^{(k,h)})`. In the **hard attention** variant (Perez et al., 2019), one takes the argmax: `hat{a}_{i,j}^{(k,h)} = delta_{j, argmax_{j'} a_{i,j'}^{(k,h)}}`, with ties broken by choosing the first position in sequence order (Footnote 1, Section 3).

The paper notes that attention often concentrates on one or a few positions in trained models (Voita et al., 2019; Clark et al., 2019), suggesting hard attention is a reasonable approximation of practical behavior (Section 3).

Language recognition is formalized as classifying the final activation `y_n^{(L)}` (after reading an end-of-sequence symbol) into class 1 (in the language) or 0 (not in the language), following Weiss et al. (2018) (Section 3).

### Key Technical Components

#### Input Restrictions

An **input restriction** `rho` is a family of maps `rho_n : {1, ..., n} -> {*, 0, 1}` that fixes some input positions to specific values while leaving others free (`*`) (Section 5). This technique is borrowed from Boolean circuit complexity (Furst et al., 1984; Hastad et al., 1994) but adapted to handle real-valued activations rather than Boolean gates.

#### c-Transformer Generalization

After removing the first layer of a transformer via the depth reduction method, the resulting structure is not a standard transformer, because each head in the lowest layer now depends on a combination of input positions. The paper introduces a generalization (Definition 3, Section 5):

> `y_j^{(0)} = f_{n,j}^{inp}((v_{i_1}, p_{i_1}), ..., (v_{i_c}, p_{i_c}))`

A **c-transformer** with L layers allows layer-0 activations to depend on at most `c` input positions rather than just one. This enables the iterative layer removal to be formalized cleanly.

#### Satisfaction and k-Dependence

The proof introduces the notion of a layer-1 head being **satisfied** if, for every possible value `z` of `y_i^{(0)}`, one of the top-k attended positions is already fixed by the restriction (Section 5.1). A satisfied head can only depend on `c * (2^c * k + 1)` input bits. Two layer-1 heads are **k-neighbors** if they share a k-dependent input bit.

### Theoretical Analysis

#### Hard Attention Results

**Theorem 1 (Main result, Section 5).** Let any hard attention transformer be given, and let `C in (0, 1)`. Then there is a restriction `rho` and an integer `c > 0` such that `|{i <= n : rho_n(i) = *}| >= Cn` for all sufficiently large `n`, and the function computed by the transformer on the restricted input depends only on `<= c` inputs, independent of input length `n`. This result holds without assumptions on activation functions or parameter norms (formal proof, strong evidence).

**Corollary 2 (Section 5).** Transformers with hard attention cannot model PARITY or 2DYCK.

*Proof sketch for PARITY:* After applying the restriction, the transformer depends on `c` inputs. For sufficiently large `n`, there exist unrestricted inputs that do not influence the output. But flipping a single bit changes PARITY membership, so the transformer must misclassify (Section 5).

*Proof sketch for 2DYCK:* Even the simpler 1DYCK (single bracket type) cannot be solved. By pre-restricting the first 0.2n positions to `(` and the last 0.2n to `)`, then applying the theorem with `C = 0.9`, the restricted input is compatible with both well-bracketed and non-well-bracketed strings, but the prediction depends on only boundedly many positions (Section 5).

**Lemma 4 (Depth Reduction Lemma, Section 5.1).** Given a c-transformer with `L` layers and a restriction preserving at least `Cn` free inputs, one can find a new restriction preserving at least `C'n` free inputs (`C' < C`) such that the function is computed by a `(c * (2^c * k * H + 1))`-transformer with `L - 1` layers, for some integer `k` depending on `C'`.

The proof of the Depth Reduction Lemma proceeds in three stages (Section 5.1):

1. **Stage 1:** Ensure each input feeds into at most `(1/eta) * c/C` layer-0 activations by fixing the few inputs that violate this bound. After this step, at least `(1 - eta) * C * n` inputs remain free.
2. **Stage 2:** Iteratively fix inputs to "satisfy" layer-1 attention heads -- ensuring each head attends to at most `k` positions -- until every head's attention is captured. This is repeated at most `(2^c * n) / k` times. After this step, at least `(1 - 2*eta) * C * n` inputs remain free.
3. **Stage 3:** Apply the **probabilistic method** with the **Lovasz Local Lemma** (Mitzenmacher and Upfal, 2017, Theorem 6.17) to show a suitable random restriction exists. The key bounds are:

> `P(X_0) <= exp(-delta^2 * q * (1 - 2*eta) * C * n / 3)` (Chernoff bound, equation 8)

> `P(X_{i,h}^{(z)}) <= (1 - (q/2)^c)^{k/((1/eta)*c^2/C)}` (exponential decay, equation 9)

where `X_0` is the event that too many inputs are fixed and `X_{i,h}^{(z)}` is the event that head `(h,i)` is not satisfied for value `z`. The Lovasz Local Lemma conditions (equations 10--11) can be satisfied for sufficiently large `k` (chosen independently of `n`), because `A^{1/k} -> 1` and `(1 - A)^{f/k} -> 1` as `k -> infinity`.

After applying `rho_n^{(3)}`, every layer-1 head depends on at most `c * (2^c * k * H + 1)` input bits. Iterating the Depth Reduction Lemma `L` times removes all layers, leaving the output dependent on a bounded number of inputs.

**Discussion of sensitive vs. insensitive languages (Section 5).** Languages immune to the depth reduction method are those where fixing a few inputs can force membership:
- `1*` (all-ones strings): a single `0` forces non-membership, so a transformer can attend to a zero and reject.
- `a^n b^n`: a single `a` in the second half forces non-membership.

The depth reduction applies to all **sufficiently sensitive** languages: if, for some `C in (0, 1)`, fixing `Cn` symbols cannot force membership, then hard attention transformers cannot recognize the language. Sensitivity of functions has been studied in computational complexity (Boppana, 1997; Gopalan et al., 2016) and linked to generalization in feedforward networks (De Palma et al., 2018).

#### Soft Attention Results

**Lemma 5 (Section 6).** For a soft attention transformer with input length `n`, exchanging one input symbol `x_i` (`i < n`) changes the final activation `y_n^{(L)}` by at most `O(1/n)`, with constants depending on parameter matrices.

*Proof (Section 6):* By induction over layers `k = 1, ..., L`:

> `||y_i^{(k)} - y_i^{(k)'}|| <= C^{2k} D = O(1)`

> `||y_j^{(k)} - y_j^{(k)'}|| <= H^k C^{2k} D / n = O(1/n)` for `j != i`

where `D = ||v_i - v'_i||_2`. The key insight: each attention weight is upper bounded by `exp(2A) / (n - 1)` where `A` bounds the attention logits (with `A = F^2 C_{f^{att}}` for dot product attention). This makes the influence of any single position vanish as `n` grows. The constant is `C = 2 * (1 + exp(2A) + L_{f^{act}})` where `L_{f^{act}}` is the Lipschitz constant of the ReLU feedforward network (Section 6).

This contrasts with RNNs, where a single input flip can have nonnegligible impact on the hidden state regardless of sequence length (e.g., an RNN tracking parity flips its state on every `1`).

The paper remarks that a key property for this proof is that the number `L` of layers is bounded independently of input length. A similar proof strategy can also be applied to other fixed-depth architectures that combine unboundedly many inputs in a smooth manner, such as 1D temporal convolutions with average pooling (Section 6).

**Theorem 6 (Section 6).** For soft attention transformers:
- **PARITY:** Cross-entropy on next-symbol prediction converges to unigram chance level as `n -> infinity`.
- **2DYCK:** Cross-entropy is separated from the optimal cross-entropy by at least `P_0 * (1 - p) * log 2 > 0`, where `P_0` is the probability that a prefix ends with a closing bracket and is unbalanced, and `p` is the PCFG expansion probability.

*Proof idea for PARITY (Section 6):* Exchanging a single bit flips PARITY membership. For any `x` in PARITY, there exists `x'` not in PARITY differing in one bit. Since the transformer's outputs differ by `O(1/n)`, a Lipschitz-continuous prediction function cannot robustly distinguish them.

*Proof idea for 2DYCK (Section 6):* With constant probability `P_0`, a prefix `x` ends with a closing bracket and is unbalanced, so the bracket type of the next closing bracket is fully determined. But there exists `x'` differing in one position where the other bracket type is required. Since the transformer's outputs for `x` and `x'` differ by `O(1/n)`, it cannot reliably distinguish which bracket type to predict, incurring at-chance cross-entropy (`log 2`) on bracket type selection. The Markov chain argument in Footnote 4 establishes that `P_0 > 0` via positive recurrence of the height process `H_n` under the PCFG, whose stationary distribution assigns nonzero weight to each height (Section 6, Footnote 4).

The distribution for PARITY is defined via a two-state automaton that terminates with probability `p` if the number of 1s is even, otherwise emits 0 or 1 with equal probability. The 2DYCK distribution follows Skachkova et al. (2018), using a PCFG that expands `S -> (S)S` or `S -> [S]S` with probability `p/2` each, and `S -> epsilon` with probability `1 - p` (Section 6).

#### Complexity-Theoretic Barrier

The paper notes (Footnote 3, Section 6) that proving soft attention transformers cannot achieve perfect **accuracy** on Boolean formula evaluation would separate the complexity classes `LTC^0` and `NC^1`, a widely conjectured but long-open problem. This is why the soft attention results are limited to cross-entropy bounds rather than accuracy bounds.

---

## Limitations and Failure Modes

1. **Asymptotic nature of results.** All theorems are asymptotic: they show failures for "sufficiently long" inputs. For any fixed bound `N` on input length, a transformer with enough layers and heads can achieve perfect accuracy on all inputs of length `<= N`. The number of heads/layers or parameter norms must grow with `N`, but the paper does not provide non-asymptotic bounds on how they must grow. The author explicitly states: "practical implementations of transformers might thus be able to circumvent such asymptotic limitations by using large numbers of layers and heads, in relation to the sentence lengths typically occurring in natural language" (Section 7).

2. **Soft attention results are weaker.** The soft attention results bound only cross-entropy, not accuracy. The complexity-theoretic barrier (`LTC^0` vs `NC^1`) prevents obtaining accuracy bounds with current mathematical methods (Footnote 3, Section 6).

3. **Practical relevance caveat.** The author notes that "pending tighter nonasymptotic bounds, the results reported here need not constitute conclusive evidence for practical limitations of real-world NLP systems" (Section 7).

4. **[Inferred]** The soft attention results assume Lipschitz-continuous activation functions (e.g., ReLU with softmax output), which covers standard implementations but excludes hypothetical non-smooth architectures. The paper uses smoothness for the induction in Lemma 5 but does not explicitly discuss this as a limitation.

5. **[Inferred]** The results apply only to transformers with a fixed number of layers and heads. They do not cover architectures where depth or width scales with input length (e.g., Universal Transformers, adaptive-depth models). The author mentions Universal Transformers only as prior work (Section 2).

6. **[Inferred]** The paper is purely theoretical and does not include experiments demonstrating the predicted failures in practice. All evidence comes from mathematical proof rather than empirical validation.

#### Scope and Comparability

- **What was not tested:** No empirical experiments were conducted. The results cover only two formal languages (PARITY and 2DYCK), though the sensitivity-based generalization (Section 5 Discussion) extends the hard attention result to a broader class. Natural language tasks were not tested. No specific transformer models (e.g., BERT, GPT-2) were evaluated.
- **Comparability notes:** The hard attention setting assumes argmax attention, which is stricter than the soft attention used in practice; however, empirical evidence that attention concentrates on few positions (Voita et al., 2019; Clark et al., 2019) suggests relevance. The soft attention results bound cross-entropy rather than accuracy, making them not directly comparable to accuracy-based results in the RNN expressiveness literature (Merrill, 2019; Korsky and Berwick, 2019). The paper's notion of "fixed-size transformer" means fixed L and H independent of n, which differs from practical settings where model size is fixed but input length varies within a finite window.

---

## Conclusions

### Contributions

1. **First theoretical impossibility results for self-attention.** Proved that fixed-size transformers with hard attention cannot recognize PARITY or 2DYCK, using a novel depth reduction method adapted from Boolean circuit complexity (Theorem 1, Corollary 2, Section 5).

2. **Soft attention sensitivity bound.** Showed that the influence of any single input symbol on a soft attention transformer's output decays as `O(1/n)` (Lemma 5, Section 6), a fundamental property distinguishing self-attention from recurrent architectures.

3. **Cross-entropy lower bounds for soft attention.** Proved that soft attention transformers cannot achieve optimal cross-entropy on PARITY or 2DYCK distributions (Theorem 6, Section 6), with PARITY converging to chance and 2DYCK being bounded away from optimal by `P_0 * (1 - p) * log 2`.

4. **Generalization to sensitive languages.** The depth reduction method applies to any language that is "sufficiently sensitive" -- where fixing a constant fraction of inputs cannot force membership (Section 5 Discussion).

5. **Identification of complexity-theoretic barrier.** Identified that obtaining accuracy bounds for soft attention would require separating `LTC^0` from `NC^1` (Footnote 3, Section 6), explaining why the soft attention results are necessarily weaker.

### Implications

1. **Self-attention has provably restricted expressivity compared to recurrence.** LSTMs can perfectly model any regular language (including PARITY) and, with infinite precision, all deterministic context-free languages via stack emulation (Tabor, 2000; Gruning, 2006; Kirov and Frank, 2012), while self-attention cannot. This theoretically confirms experimental findings of Tran et al. (2018) (Section 7).

2. **Natural language may not require full context-free power.** The practical success of transformers despite these limitations suggests that natural language can be approximated well with models too weak for the formal languages typically assumed in theoretical linguistics (speculative; stated by the author, Section 7).

3. **Connection to human processing limitations.** Self-attention bears resemblance to cue-based retrieval models of human sentence processing (Lewis and Vasishth, 2005), which also predict difficulty with center embeddings because they cannot count brackets (speculative; stated by the author, Section 7).

---

## Key Claims

1. **C1: Hard attention cannot model PARITY or 2DYCK.** Any fixed-size hard attention transformer will misclassify inputs of sufficient length for both PARITY and 2DYCK. This holds without assumptions on activation functions or parameter norms. (Corollary 2, Section 5) -- **supported.** Scope: fixed number of layers and heads, hard attention, input length unbounded. Magnitude: accuracy drops below 100% for sufficiently long inputs. Evidence: formal proof using depth reduction and input restrictions (strong evidence -- the result is a mathematical theorem with no distributional assumptions for hard attention).

2. **C2: Input restrictions can force bounded dependence.** For any hard attention transformer, one can fix at most `(1-C)n` input symbols and make the transformer's output depend on at most a constant number of inputs, independent of `n`. (Theorem 1, Section 5) -- **supported.** Scope: hard attention, arbitrary fixed C in (0,1). Magnitude: output dependence reduced to constant c independent of n, while preserving at least Cn free inputs. Evidence: formal proof via iterative application of the Depth Reduction Lemma (strong evidence).

3. **C3: Soft attention sensitivity bound.** Changing one input symbol in a soft attention transformer changes the final-layer activation by `O(1/n)`. (Lemma 5, Section 6) -- **supported.** Scope: fixed-depth soft attention transformers with Lipschitz-continuous activations. Magnitude: `O(1/n)` change with constant `C = 2(1 + exp(2A) + L_{f^{act}})`. Evidence: formal proof by induction over layers (strong evidence, but requires smoothness assumption).

4. **C4: PARITY cross-entropy converges to chance.** Soft attention transformers' cross-entropy on PARITY next-symbol prediction converges to unigram chance level as input length increases. (Theorem 6, Section 6) -- **supported.** Scope: fixed-size soft attention transformers with Lipschitz-continuous activations, specific PARITY distribution. Magnitude: cross-entropy converges to unigram chance (no better than marginal frequencies). Evidence: follows from Lemma 5 and Lipschitz continuity of the prediction function (strong evidence, single proof technique).

5. **C5: 2DYCK cross-entropy gap.** Soft attention transformers' cross-entropy on 2DYCK is bounded away from optimal by at least `P_0 * (1 - p) * log 2 > 0`. (Theorem 6, Section 6) -- **supported.** Scope: fixed-size soft attention transformers with Lipschitz-continuous activations, specific PCFG distribution for 2DYCK. Magnitude: constant gap of `P_0 * (1 - p) * log 2`. Evidence: formal proof using Lemma 5, Markov chain argument for P_0 > 0, and bracket type indistinguishability (strong evidence, single proof technique).

6. **C6: Generalization via sensitivity.** The depth reduction method applies to all languages where fixing a constant fraction of inputs cannot force membership/non-membership. (Section 5 Discussion) -- **supported.** Scope: hard attention only, sensitivity condition on the language. Magnitude: complete failure for sufficiently long inputs. Evidence: stated as a general observation following from the Theorem 1 proof structure (moderate evidence -- generalization is argued informally, not stated as a separate theorem).

7. **C7: Complexity barrier for soft attention accuracy.** Proving accuracy bounds for soft attention on Boolean formulas would separate `LTC^0` and `NC^1`. (Footnote 3, Section 6) -- **supported.** Scope: general complexity-theoretic observation. Magnitude: identifies fundamental barrier. Evidence: appeals to known complexity class relationships (strong evidence -- follows from established complexity theory).

---

## Open Questions

1. **Non-asymptotic bounds.** Can tight non-asymptotic bounds be derived quantifying how many layers, heads, or what parameter norms are needed for a transformer to solve PARITY or 2DYCK up to input length `N`? The author notes that "pending tighter nonasymptotic bounds, the results reported here need not constitute conclusive evidence for practical limitations" (Section 7). *(Unresolved)*

2. **Natural language and counter-free languages.** Does the success of transformers imply that natural language is approximable by counter-free (star-free) regular languages, or are other mechanisms (large parameter counts, approximate solutions, chain-of-thought) responsible? The author raises this as an open question in Section 7. *(Unresolved)*

3. **Soft attention accuracy bounds.** Can the depth reduction method or alternative techniques be adapted to yield accuracy bounds for soft attention, or does the `LTC^0` vs `NC^1` barrier fundamentally prevent this? Footnote 3 (Section 6) identifies this as connected to a major open problem in complexity theory. *(Unresolved)*

4. **Recurrence-augmented architectures.** How do extensions of self-attention with recurrence (Universal Transformers, Transformer-XL) change formal language recognition capabilities? The paper studies only pure self-attention; Dehghani et al. (2019) introduced Universal Transformers with recurrence but their formal expressiveness was not analyzed (Section 2). *(Unresolved)*

---

## Core References and Why They Are Referenced

### Self-Attention Architecture

- **Vaswani et al. (2017)** -- *Attention Is All You Need.* Introduced the Transformer architecture whose limitations are the subject of the paper. The self-attention formulation in Section 3 follows this work directly.
- **Perez et al. (2019)** -- *On the Turing Completeness of Modern Neural Network Architectures.* Showed Seq2Seq Transformers with unbounded decoding can emulate Turing machines; contrasted with the fixed-computation setting studied here. Also provides the hard attention variant definition used in Section 5.
- **Hsieh et al. (2019)** -- *On the Robustness of Self-Attentive Models.* Provided a theoretical result on single-head robustness under distributional assumptions; Lemma 5 considerably generalizes this by avoiding distributional assumptions and applying to arbitrary numbers of heads and layers (Section 2).

### Formal Language Theory and Computational Complexity

- **Chomsky and Schutzenberger (1963)** -- *The Algebraic Theory of Context-Free Languages.* Established that all context-free languages arise from DYCK languages, motivating 2DYCK as a fundamental test language (Section 4).
- **Furst et al. (1984)** -- *Parity, Circuits, and the Polynomial-Time Hierarchy.* Proved that bounded-depth Boolean circuits cannot compute PARITY using input restrictions; the depth reduction method here adapts this approach to real-valued transformer activations (Section 5).
- **McNaughton and Papert (1971)** -- *Counter-Free Automata.* Defined counter-free (star-free) languages; PARITY is the simplest non-counter-free regular language (Section 4).
- **Barrington et al. (1992)** -- *Regular Languages in NC1.* Established the connection between quasi-aperiodic syntactic morphisms and PARITY, showing that inability to compute PARITY implies inability to recognize most non-counter-free regular languages (Footnote 2, Section 4).

### Recurrent Network Expressiveness

- **Siegelman and Sontag (1995)** -- *On the Computational Power of Neural Nets.* Classical result that RNNs with unlimited computation can emulate Turing machines (Section 2).
- **Merrill (2019)** -- *Sequential Neural Networks as Automata.* Showed finite-precision LSTMs recognize counter languages, GRUs and simple RNNs recognize regular languages (Section 2).
- **Korsky and Berwick (2019)** -- *On the Computational Power of RNNs.* Showed arbitrary-precision RNNs can emulate pushdown automata and recognize deterministic context-free languages (Section 2).
- **Weiss et al. (2018)** -- *On the Practical Computational Power of Finite Precision RNNs.* Experimentally and theoretically studied RNN capabilities on formal languages; language recognition formalization follows this work (Section 3).

### Empirical Studies of Attention and Hierarchical Structure

- **Tran et al. (2018)** -- *The Importance of Being Recurrent for Modeling Hierarchical Structure.* Experimental evidence that LSTMs outperform transformers at learning hierarchical structure, which this paper theoretically confirms (Section 7).
- **Voita et al. (2019)** -- *Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting.* Empirical evidence that trained attention concentrates on few positions, supporting the practical relevance of the hard attention analysis (Section 3).
- **Clark et al. (2019)** -- *What Does BERT Look At?* Showed BERT attention patterns often concentrate, consistent with the hard attention setting (Section 3).

### Probabilistic Tools

- **Mitzenmacher and Upfal (2017)** -- *Probability and Computing.* Source for the Chernoff bound (Theorem 4.4, used in equation 8) and Lovasz Local Lemma (Theorem 6.17, used in Stage 3 of the Depth Reduction Lemma proof) (Section 5.1).

### Psycholinguistic Models

- **Lewis and Vasishth (2005)** -- *An Activation-Based Model of Sentence Processing as Skilled Memory Retrieval.* Cue-based retrieval models of human sentence processing that also predict difficulty with center embeddings, drawing a parallel to self-attention limitations (Section 7).
