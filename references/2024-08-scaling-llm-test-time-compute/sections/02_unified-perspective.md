# 2. A Unified Perspective on Test-Time Computation: Proposer and Verifier [p. 3-4]

## Framework

[p. 3-4] The authors unify approaches for using test-time computation by viewing the use of additional test-time compute through the lens of modifying the model's predicted distribution *adaptively* at test-time, conditioned on a given prompt. Ideally, test-time compute should modify the distribution so as to generate better outputs than naively sampling from the LLM itself would.

Two knobs to induce modifications to an LLM's distribution:

1. **(1) At the input level:** augmenting the given prompt with an additional set of tokens that the LLM conditions on to obtain the modified distribution
2. **(2) At the output level:** sampling multiple candidates from the standard LM and performing surgery on these candidates

In other words, we could either modify the **proposal distribution** induced by the LLM itself such that it is an improvement over naively conditioning on the prompt, or we could use some post-hoc **verifiers or scorers** to perform output modifications. [p. 4]

This process is reminiscent of Markov chain Monte Carlo (MCMC) sampling [2] from a complex target distribution but by combining a simple proposal distribution and a score function. Modifying the proposal distribution directly by altering input tokens and using a verifier form two independent axes of the study. [p. 4]

## Modifying the Proposal Distribution

[p. 4] One way to improve the proposal distribution is to directly optimize the model for a given reasoning task via RL-inspired finetuning methods such as STaR or ReST^EM [35, 50]. These techniques do not utilize any additional input tokens but specifically finetune the model to induce an improved proposal distribution.

Alternatively, techniques such as self-critique [4, 8, 23, 30] enable the model itself to improve its own proposal distribution at test time by instructing it to critique and revise its own outputs in an iterative fashion. Since prompting off-the-shelf models is not effective at enabling effective revisions at test time, the authors specifically finetune models to iteratively revise their answers in complex reasoning-based settings. They utilize the approach of finetuning on on-policy data with Best-of-N guided improvements to the model response [28]. [p. 4]

## Optimizing the Verifier

[p. 4] In the proposer-verifier abstraction, the verifier is used to aggregate or select the best answer from the proposal distribution. The most canonical way to use a verifier is by applying best-of-N sampling: sample N complete solutions and select the best one according to a verifier [7].

This approach can be further improved by training a process-based verifier [22], or a **process reward model (PRM)**, which produces a prediction of the correctness of each intermediate step in a solution, rather than just the final answer. These per-step predictions can then be used to perform tree search over the space of solutions, enabling a potentially more efficient and effective way to search against a verifier, compared to naive best-of-N [6, 10, 48]. [p. 4]
