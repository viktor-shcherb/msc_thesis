---
title: "Prediction with a Short Memory"
authors: "Sharan, Kakade, Liang, Valiant"
year: 2018
venue: "STOC 2018"
paper_type: conference-paper
categories: ["learning-theory"]
scope: ["prediction from bounded memory", "mutual information bounds on context usage", "HMM prediction with short windows", "computational lower bounds for sequence prediction"]
benchmarks_used: []
models_introduced: []
models_evaluated: []
key_claims:
  - id: C1
    claim: "For any distribution with mutual information I(M) between past and future, the best l-th order Markov model achieves average KL error I(M)/l and l_1 error sqrt(I(M)/l) relative to the optimal predictor with full history"
    evidence: "Proposition 1, Section 4"
    status: supported
  - id: C2
    claim: "For HMMs with n hidden states, a window of length O(log n / epsilon) suffices for average KL error epsilon, regardless of mixing time"
    evidence: "Corollary 1, Section 1"
    status: supported
  - id: C3
    claim: "The naive empirical Markov model (counting (l+1)-gram frequencies) achieves sqrt(epsilon) l_1 error for HMMs with n states using window length O(log n / epsilon) and d^{O(log n / epsilon)} samples"
    evidence: "Theorem 1, Section 2"
    status: supported
  - id: C4
    claim: "A window length of log n / epsilon is information-theoretically necessary for KL error epsilon on HMMs with n states"
    evidence: "Proposition 3, Section 7"
    status: supported
  - id: C5
    claim: "Any computationally tractable algorithm requires d^{Omega(log n / epsilon)} samples for HMMs with n states and alphabet size d, assuming hardness of strongly refuting certain CSPs"
    evidence: "Theorem 2, Section 5"
    status: supported
cross_references:
  - target: 2018-07-sharp-nearby-fuzzy-far-away
    type: formalizes
    detail: "Provides theoretical explanation via bounded mutual information for why LSTM LMs effectively use only ~200 tokens of context, as observed empirically by Khandelwal et al."
  - target: 2021-11-long-range-models-use-context
    type: formalizes
    detail: "Sun et al. cite this paper as providing theoretical grounding for the empirical finding that long-range Transformer LMs show limited benefit from distant context under perplexity evaluation"
  - target: 2024-02-lost-in-the-middle
    type: complementary
    detail: "Liu et al. cite this paper's bounded mutual information theory as explaining the diminishing returns of longer context for average prediction"
open_questions:
  - question: "Can noise stability or robustness properties of Markov models be exploited to reduce the sample complexity from d^{O(log n / epsilon)} to poly(d, I(M), 1/epsilon)?"
    addressed_by: null
  - question: "Do alternative metrics (e.g., re-weighted prediction error emphasizing rare observations) render short-memory predictors insufficient, thereby better driving progress toward models that capture long-range dependencies?"
    addressed_by: null
  - question: "Can the mutual information framework be extended to characterize the prediction error of Transformer-based models as a function of context window length?"
    addressed_by: null
---

# Prediction with a Short Memory

**Authors:** Vatsal Sharan, Sham Kakade, Percy Liang, Gregory Valiant (Stanford University, University of Washington)
**Date:** June 2018, STOC 2018, arXiv:1612.02526

---

## Core Research Problem

Sequential prediction -- predicting the next observation given past observations -- is fundamental to natural language modeling, speech synthesis, and financial forecasting. Enormous effort has gone into designing architectures that store and reference information about the past: n-gram models, HMMs, LSTMs (Hochreiter & Schmidhuber, 1997; Gers et al., 2000), neural Turing machines (Graves et al., 2014), memory networks (Weston et al., 2015), and attention-based models (Vaswani et al., 2017). Yet consistently learning long-range dependencies remains an open challenge, and the theoretical understanding of when and why long-range memory is needed for accurate prediction is lacking.

The paper addresses four fundamental questions: (1) how much memory is necessary for accurate prediction, and what sequence properties determine this? (2) must one remember significant information about the distant past, or does short-term memory suffice? (3) what is the computational complexity of accurate prediction? (4) how do answers depend on the error metric?

A key subtlety is that the mutual information `I(X_past; X_future)` is not an upper bound on the memory an optimal algorithm needs. Harsha et al. (2007) showed there exist joint distributions where the minimum advice string making `X_future` independent of `X_past` is exponential in the mutual information. **The core challenge is: characterizing the fundamental relationship between memory, mutual information, and prediction accuracy for sequential processes.**

---

## Problem Solutions

The paper proves that for a broad class of sequences, accurate average prediction requires only recent observations, not complex long-range memory.

1. **Mutual information bound.** For any distribution where the mutual information between past and future is bounded by `I(M)`, a Markov model over the most recent `I(M)/epsilon` observations achieves average KL error `epsilon` relative to the optimal predictor with full history.
2. **HMM specialization.** For HMMs with `n` hidden states, `I(M) <= log n`, yielding a window length of `O(log n / epsilon)` that is independent of the mixing time.
3. **Matching lower bounds.** Both the window length and the `d^{Theta(log n / epsilon)}` sample complexity are shown to be necessary -- information-theoretically and computationally, respectively.

---

## Approach Details

### Method

The paper considers a stationary stochastic process generating observations `x_1, x_2, ...` from a finite alphabet of size `d`. An `l`-th order predictor `A_l` maps the most recent `l` observations to a predicted distribution over the next observation. Performance is measured as the average error relative to the Bayes-optimal predictor `P_infinity` that has access to the full history and knows the data-generating distribution:

> `delta_F(A_l) = lim_{T->inf} (1/T) sum_{t=0}^{T-1} E[ F(Pr(x_t | x_{-inf}^{t-1}), Q_{A_l}(x_t | x_{t-l}^{t-1})) ]`

where `F` is KL divergence, `l_1` distance, or relative zero-one loss.

The crucial quantity is the **mutual information between past and future**:

> `I(M) = lim_{T->inf} (1/T) sum_{t=0}^{T-1} I(x_{-inf}^{t-1}; x_t^{inf})`

For stationary processes, this simplifies to `I(M) = I(x_{-inf}^{-1}; x_0^{inf})`.

### Key Technical Components

**Proposition 1 (General upper bound).** For any distribution `M` with mutual information `I(M)`, the best `l`-th order Markov model `P_l` satisfies:

> `delta_{KL}(P_l) <= I(M) / l`

and by Pinsker's inequality:

> `delta_{l_1}(P_l) <= sqrt(I(M) / (2l))`

**Proof mechanism.** The total error decomposes as `delta_{KL}^{(t)}(A_l) = delta_{KL}^{(t)}(P_l) + hat{delta}_{KL}^{(t)}(A_l)`. The key identity is:

> `delta_{KL}^{(t)}(P_l) = I(x_{-inf}^{t-l-1}; x_t | x_{t-l}^{t-1})`

This says that the Markov model's prediction error at time `t` equals the conditional mutual information between the distant past and the current observation given recent context. Splitting time into blocks of length `l` and applying the chain rule:

> `I(x_{-inf}^{tau-1}; x_tau^{inf}) >= sum_{t=tau}^{tau+l-1} delta_{KL}^{(t)}(P_l)`

Averaging over blocks yields the bound. The core intuition is: if prediction is poor at time `t`, then `x_t` carries substantial information about the distant past; since total mutual information is bounded by `I(M)`, this can only happen for a fraction `I(M)/l` of time steps on average.

**Corollary 1 (HMM specialization).** For an HMM with at most `n` hidden states, `I(M) <= log n` (since the hidden state is a sufficient statistic of bounded entropy). Therefore a window of `log n / epsilon` observations suffices for average KL error `epsilon`, regardless of mixing time.

### Theoretical Analysis

#### Learning Result (Theorem 1)

**Theorem 1.** For an HMM with at most `n` hidden states and output alphabet of size `d`, for `epsilon > 1/log^{0.25} n`, there exists a window length `l = O(log n / epsilon)` such that for sequence length `T >= d^{cl}` (for an absolute constant `c`), the naive empirical `l`-th order Markov model -- which simply outputs the empirical conditional frequencies of length-`l` contexts -- achieves expected `l_1` error bounded by `sqrt(epsilon)` at a uniformly random time step.

The proof has two main components:

**(A) Submartingale argument (Lemma 1).** The posterior probability of the true initial hidden state `h_0` given observations `x_0, ..., x_s` satisfies: the log-odds `log(H_0^s(h_0) / (1 - H_0^s(h_0)))` minus `(1/2) sum_{i=0}^{s} ||OPT_i - M_i||_1^2` forms a submartingale, where `OPT_s` is the optimal prediction knowing `h_0` and `M_s` is the Markov prediction. A technical complication is that the log-odds increments can be unbounded. This is handled by introducing a **modified Pinsker's inequality** (Lemma 6):

> For any two distributions `mu` and `nu`, the `C`-truncated KL divergence `D_tilde_C(mu || nu) = E_mu[log min{mu(x)/nu(x), C}]` satisfies `D_tilde_C(mu || nu) >= (1/2) ||mu - nu||_1^2` whenever `log C >= 8`.

This enables "clipping" the martingale differences, after which Azuma-Hoeffding concentration yields: with probability at least `1 - epsilon^2`, the total squared prediction error over a window of `l = c log n / epsilon^2` steps is at most `4c log n`, giving average `l_1` error at most `3 epsilon` by Jensen's inequality.

**(B) Concentration of empirical frequencies (Lemma 4).** A second martingale argument shows that the empirical Markov model (based on observed frequencies) concentrates around the true Markov model with failure probability at most `3/n^2` per context string, using `d^{cl}` samples and a union bound over all `d^l` possible length-`l` contexts.

#### Information-Theoretic Lower Bound (Proposition 3)

**Proposition 3.** There exists a constant `c` such that for all `0 < epsilon < 1/4` and sufficiently large `n`, there exists an HMM with `n` hidden states for which no predictor using windows shorter than `c log n / epsilon` achieves average KL error less than `epsilon`, and no predictor using windows shorter than `c log n / epsilon^2` achieves average `l_1` or zero-one error less than `epsilon`.

The construction uses an HMM whose transition matrix is a random permutation on `n` states with binary outputs: states labeled 0 emit 0 with probability `0.5 + epsilon`, states labeled 1 emit 1 with probability `0.5 + epsilon`. The proof uses the probabilistic method to show that many distinct segments of hidden states produce output strings at similar Hamming distance from the observed output, making it impossible for a short-window predictor to distinguish the true segment.

This establishes that the window length `Theta(I(M)/epsilon)` for KL loss and `Theta(I(M)/epsilon^2)` for `l_1` loss in Proposition 1 are tight.

#### Computational Lower Bounds

**Theorem 2 (Large alphabets).** Assuming the hardness of strongly refuting a class of CSPs (Conjecture 1 of Feldman et al., 2015), for any computationally tractable algorithm, `d^{Omega(log n / epsilon)}` samples are necessary for HMMs with `n` states and alphabet size `d`. The construction encodes a planted CSP instance into an HMM: the first `k` time steps output random literals (alphabet size `2n`), and the next `m` steps output `y = Av mod 2` (with noise), where `A` is a binary matrix chosen as a good error-correcting code. Any efficient predictor achieving low error could distinguish planted from random CSP instances, contradicting the hardness conjecture.

**Proposition 2 (Small alphabets).** Under the hardness of learning parity with noise, any algorithm achieving average prediction error `epsilon` on a family of HMMs with `n` hidden states requires `f(Omega(log n / epsilon))` time or samples, where `f(k) = 2^{k/log k}` with the best known algorithm (Blum et al., 2003).

### Key Results

Since the paper is entirely theoretical with no experiments, results are summarized as proved bounds:

| Result | Quantity | Upper Bound | Lower Bound | Tight? |
|---|---|---|---|---|
| Window length for KL error epsilon | l | I(M)/epsilon (Prop. 1) | c log n / epsilon (Prop. 3) | Yes (for HMMs) |
| Window length for l_1 error sqrt(epsilon) | l | I(M)/epsilon (Cor. 2) | c log n / epsilon^2 (Prop. 3) | Yes (for HMMs) |
| Sample complexity (large alphabet) | T | d^{O(log n / epsilon)} (Thm. 1) | d^{Omega(log n / epsilon)} (Thm. 2, conditional) | Yes (conditional) |
| Sample complexity (small alphabet) | T | -- | f(Omega(log n / epsilon)) (Prop. 2, conditional) | Open |

- The window length depends only on `I(M)` and the target error, not on the mixing time of the underlying process.
- For HMMs, `I(M) <= log n`, so the window length is `O(log n / epsilon)`.
- The naive counting algorithm (empirical `(l+1)`-gram) is essentially optimal among efficient algorithms.

### Implications for Language Modeling Evaluation

The paper explicitly frames its results as having a dual interpretation:

- **Positive (for applications where average error is the metric):** Regardless of the nature of dependencies, a sufficiently high-order Markov model trained on enough data will predict well on average.
- **Negative (for language modeling):** Average prediction error (perplexity) is not a good metric for evaluating models that should capture long-range dependencies, because a Markov model -- which is indifferent to the time scale of dependencies -- can perform well under it. The authors suggest that **re-weighted prediction error** giving more reward for correctly predicting uncommon observations, or **evaluation at selected time steps**, may be essential for driving progress toward genuine long-range understanding (Section 1.4).

---

## Limitations and Failure Modes

1. **Average-case guarantee only.** The bound holds on average over time steps. At any specific time step, the Markov model may be arbitrarily worse than the optimal predictor. This limits the result's applicability to settings where worst-case guarantees matter (Section 1.2).
2. **No KL guarantee for empirical model.** Theorem 1 guarantees `l_1` error but not KL error for the empirical Markov model, because KL error can be unbounded when rare characters have not been observed (footnote 1).
3. **Exponential sample complexity in window length.** The `d^{O(l)}` sample requirement is unavoidable (shown by Theorem 2) but severely limits practical applicability for large alphabets or large `I(M)`.
4. **Constraint on epsilon.** Theorem 1 requires `epsilon > 1/log^{0.25} n`, excluding very small error regimes.
5. **Purely theoretical.** The paper contains no experiments. The practical relevance of the bounds to neural language models, where the data-generating distribution is unknown and the model class differs from Markov models, requires empirical validation by subsequent work.
6. **Conditional computational lower bounds.** The computational lower bounds rely on unproven hardness conjectures (CSP hardness, parity with noise hardness), which are standard in complexity theory but not proven.

---

## Conclusions

### Contributions

1. **Mutual information controls short-memory prediction.** Established that for any stationary process with mutual information `I(M)`, a Markov model of order `I(M)/epsilon` achieves average KL error `epsilon`, via an elementary information-theoretic proof (Proposition 1, Section 4).
2. **Mixing-time-independent bounds for HMMs.** Showed that for HMMs with `n` hidden states, a window of `O(log n / epsilon)` suffices regardless of mixing time, and the naive counting algorithm achieves this with `d^{O(log n / epsilon)}` samples (Corollary 1, Theorem 1).
3. **Tight information-theoretic lower bound.** Proved via a permutation-HMM construction that the `O(log n / epsilon)` window length is necessary, establishing tightness (Proposition 3, Section 7).
4. **Conditional computational lower bound.** Showed that the exponential sample complexity `d^{Theta(log n / epsilon)}` is necessary for efficient algorithms, via reductions from CSP refutation (Theorem 2, Section 5) and parity with noise (Proposition 2, Section 6).
5. **Modified Pinsker's inequality.** Introduced a truncated KL divergence variant of Pinsker's inequality (Lemma 6) as a technical tool for handling unbounded martingale increments.

### Implications

1. The result that average prediction error is insensitive to the time scale of dependencies provides **theoretical grounding for empirical observations** that perplexity plateaus after relatively short contexts in both LSTMs (Khandelwal et al., 2018) and Transformers (Sun et al., 2021).
2. The dual interpretation suggests that **perplexity may be fundamentally limited as a metric** for evaluating long-context capability, since it can be dominated by easy-to-predict time steps where long-range context is irrelevant (speculative implication supported by the formal results).
3. The conditional computational lower bounds suggest that **efficient prediction inherently requires exponentially many samples in the mutual information**, unless additional structural assumptions (such as noise stability) are exploited.

---

## Key Claims

1. **C1:** For any distribution with mutual information `I(M)` between past and future, the best `l`-th order Markov model achieves average KL error `I(M)/l` and average `l_1` error `sqrt(I(M)/(2l))` relative to the Bayes-optimal predictor with full history (Proposition 1, Section 4).
2. **C2:** For HMMs with `n` hidden states, `I(M) <= log n`, so a window of `O(log n / epsilon)` observations suffices for average KL error `epsilon`, independent of the mixing time (Corollary 1, Section 1).
3. **C3:** The naive empirical `l`-th order Markov model -- counting `(l+1)`-gram frequencies -- achieves `sqrt(epsilon)` average `l_1` error for HMMs with `n` states using window length `O(log n / epsilon)` and sequence length `d^{O(log n / epsilon)}` (Theorem 1, Section 2).
4. **C4:** The window length `c log n / epsilon` is information-theoretically necessary for KL error `epsilon` on HMMs with `n` states (Proposition 3, Section 7).
5. **C5:** The sample complexity `d^{Omega(log n / epsilon)}` is computationally necessary for efficient algorithms, assuming hardness of strongly refuting certain CSPs (Theorem 2, Section 5).

---

## Open Questions

1. **Can noise stability reduce sample complexity?** The computational lower bounds rely on parity-based constructions that are very sensitive to noise. For noise-stable distributions, connections between noise stability and low-degree polynomial approximation (O'Donnell, 2014; Blais et al., 2010) might reduce the sample complexity to `poly(d, I(M), 1/epsilon)`. Left as the main open problem (Section 1.4).
2. **Do alternative metrics render short-memory predictors insufficient?** The authors suggest that re-weighted prediction error (emphasizing rare observations) or evaluation at selected time steps might require genuine long-range memory. Formal analysis under such metrics is left open (Section 1.4).
3. **Can the mutual information framework characterize Transformer-based models?** The theory applies to any stationary process, but the practical implications for Transformer language models -- where the model class is different from Markov models and the data distribution is unknown -- remain unexplored.

---

## Core References and Why They Are Referenced

### Sequence Architectures and Memory

- **Hochreiter & Schmidhuber (1997)** -- *Long Short-Term Memory.* LSTM architecture that motivates the question of when long-range memory is necessary for prediction.
- **Vaswani et al. (2017)** -- *Attention Is All You Need.* Transformer architecture with attention; cited as an example of complex memory mechanisms whose necessity the paper questions.
- **Graves et al. (2014)** -- *Neural Turing Machines.* External memory architecture; cited alongside memory networks and differentiable neural computers as examples of memory-augmented systems.

### Information Theory and Prediction

- **Harsha et al. (2007)** -- *The Communication Complexity of Correlation.* Showed that the minimum advice string length can be exponential in the mutual information, making Proposition 1's result that mutual information controls short-window prediction error all the more surprising.
- **Cesa-Bianchi & Lugosi (2006)** -- *Prediction, Learning, and Games.* Standard reference for online prediction and no-regret learning.

### HMM Learning

- **Hsu, Kakade, & Zhang (2009)** -- *A Spectral Algorithm for Learning Hidden Markov Models.* Method-of-moments approach to HMM learning; contrasted with the paper's naive counting algorithm.
- **Anandkumar, Hsu, & Kakade (2012)** -- *A Method of Moments for Mixture Models and Hidden Markov Models.* Tensor decomposition methods for parameter estimation in HMMs.

### Computational Hardness

- **Feldman, Perkins, & Vempala (2015)** -- *On the Complexity of Random Satisfiability Problems with Planted Solutions.* Source of Conjecture 1 (CSP hardness) used for the computational lower bound in Theorem 2.
- **Blum, Kalai, & Wasserman (2003)** -- *Noise-Tolerant Learning, the Parity Problem, and the Statistical Query Model.* Fastest known algorithm for parity with noise, establishing the `2^{n/log n}` bound used in Proposition 2.

### Compression and Universal Prediction

- **Ziv & Lempel (1978)** -- *Compression of Individual Sequences via Variable-Rate Coding.* Lempel-Ziv compression; related approach to universal prediction through compression.
