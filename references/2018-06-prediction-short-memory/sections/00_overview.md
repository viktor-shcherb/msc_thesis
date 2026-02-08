# Overview

**Title:** Prediction with a Short Memory

**Authors:**
- Vatsal Sharan (Stanford University, vsharan@stanford.edu)
- Sham Kakade (University of Washington, sham@cs.washington.edu)
- Percy Liang (Stanford University, pliang@cs.stanford.edu)
- Gregory Valiant (Stanford University, valiant@stanford.edu)

**Venue:** arXiv:1612.02526v5 [cs.LG]

**Date:** 28 Jun 2018

## Abstract

> "We consider the problem of predicting the next observation given a sequence of past observations, and consider the extent to which accurate prediction requires complex algorithms that explicitly leverage long-range dependencies. Perhaps surprisingly, our positive results show that for a broad class of sequences, there is an algorithm that predicts well on average, and bases its predictions only on the most recent few observation together with a set of simple summary statistics of the past observations. Specifically, we show that for any distribution over observations, if the mutual information between past observations and future observations is upper bounded by I, then a simple Markov model over the most recent I/epsilon observations obtains expected KL error epsilon---and hence l_1 error sqrt(epsilon)---with respect to the optimal predictor that has access to the entire past and knows the data generating distribution. For a Hidden Markov Model with n hidden states, I is bounded by log n, a quantity that does not depend on the mixing time, and we show that the trivial prediction algorithm based on the empirical frequencies of length O(log n / epsilon) windows of observations achieves this error, provided the length of the sequence is d^{Omega(log n / epsilon)}, where d is the size of the observation alphabet.
>
> We also establish that this result cannot be improved upon, even for the class of HMMs, in the following two senses: First, for HMMs with n hidden states, a window length of log n / epsilon is information-theoretically necessary to achieve expected KL error epsilon, or l_1 error sqrt(epsilon). Second, the d^{Theta(log n / epsilon)} samples required to accurately estimate the Markov model when observations are drawn from an alphabet of size d is necessary for any computationally tractable learning/prediction algorithm, assuming the hardness of strongly refuting a certain class of CSPs."

## Section headings (visible so far)

1. Memory, Modeling, and Prediction
   1.1 Interpretation of Mutual Information of Past and Future
   1.2 Implications of Proposition 1 and Corollary 1
   1.3 Lower bounds
   1.4 Future Directions
   1.5 Related Work
2. Proof Sketch of Theorem 1
3. Definitions and Notation
4. Predicting Well with Short Windows
5. Lower Bound for Large Alphabets
   5.1 Sketch of Lower Bound Construction
6. Lower Bound for Small Alphabets
7. Information Theoretic Lower Bounds
A. Proof of Theorem 1
   A.1 Proof of Lemma 1
   A.2 Proof of Modified Pinsker's Inequality (Lemma 6)
B. Proof of Lower Bound for Large Alphabets
   B.1 CSP Formulation
   B.2 Ensuring High Complexity of the CSP
   B.3 Sequential Model of CSP and Sample Complexity Lower Bound
      B.3.1 Constructing sequential model
      B.3.2 Reducing sequential model to CSP instance
   B.4 Proof of Lemma 10
   B.5 Proof of Lemma 12
C. Proof of Lower Bound for Small Alphabets
   C.1 Proof of Lemma 3
   C.2 Proof of Proposition 2
D. Proof of Information Theoretic Lower Bound
Acknowledgements
References
