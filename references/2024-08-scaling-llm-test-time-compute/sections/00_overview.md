# Overview

**Title:** Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters

**Authors:** Charlie Snell (equal advising, UC Berkeley), Jaehoon Lee (Google DeepMind), Kelvin Xu (Google DeepMind), Aviral Kumar (Google DeepMind)
- Work done during an internship at Google DeepMind
- Corresponding author: csnell22@berkeley.edu

**Affiliations:** UC Berkeley, Google DeepMind

**Venue:** arXiv preprint (arXiv:2408.03314v1, cs.LG)

**Date:** 6 Aug 2024

## Abstract

> "Enabling LLMs to improve their outputs by using more test-time computation is a critical step towards building generally self-improving agents that can operate on open-ended natural language. In this paper, we study the scaling of inference-time computation in LLMs, with a focus on answering the question: *if an LLM is allowed to use a fixed but non-trivial amount of inference-time compute, how much can it improve its performance on a challenging prompt?* Answering this question has implications not only on the achievable performance of LLMs, but also on the future of LLM pretraining and how one should tradeoff inference-time and pre-training compute. Despite its importance, little research attempted to understand the scaling behaviors of various test-time inference methods. Moreover, current work largely provides negative results for a number of these strategies. In this work, we analyze two primary mechanisms to scale test-time computation: (1) searching against dense, process-based verifier reward models; and (2) updating the model's distribution over a response adaptively, given the prompt at test time. We find that in both cases, the effectiveness of different approaches to scaling test-time compute critically varies depending on the difficulty of the prompt. This observation motivates applying a 'compute-optimal' scaling strategy, which acts to most effectively allocate test-time compute adaptively per prompt. Using this compute-optimal strategy, we can improve the efficiency of test-time compute scaling by more than 4x compared to a best-of-N baseline. Additionally, in a FLOPs-matched evaluation, we find that on problems where a smaller base model attains somewhat non-trivial success rates, test-time compute can be used to outperform a 14x larger model." [p. 1]

## Section Headings

1. Introduction
2. A Unified Perspective on Test-Time Computation: Proposer and Verifier
3. How to Scale Test-Time Computation Optimally
   - 3.1. Test-Time Compute-Optimal Scaling Strategy
   - 3.2. Estimating Question Difficulty for Compute-Optimal Scaling
4. Experimental Setup
5. Scaling Test-Time Compute via Verifiers
   - 5.1. Training Verifiers Amenable to Search
   - 5.2. Search Methods Against a PRM
   - 5.3. Analysis Results: Test-Time Scaling for Search with Verifiers
6. Refining the Proposal Distribution
   - 6.1. Setup: Training and Using Revision Models
   - 6.2. Analysis Results: Test-Time Scaling with Revisions
7. Putting it Together: Exchanging Pretraining and Test-Time Compute
8. Discussion and Future Work
Acknowledgements
