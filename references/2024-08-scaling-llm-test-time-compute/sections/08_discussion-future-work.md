# 8. Discussion and Future Work [p. 15-16]

[p. 15-16] The authors conducted a thorough analysis of the efficacy of different techniques that aim to either improve search against a verifier or to refine an LLM's proposal distribution, for scaling test-time compute for math reasoning. In general, they found that the efficacy of a given approach heavily correlates with the difficulty of the problem from the perspective of the base LLM's capabilities. This motivated them to introduce the notion of "compute-optimal" scaling of test-time computation, which prescribes an adaptive, prompt-dependent strategy to improve performance under a given test-time compute budget. By applying such a compute-optimal scaling strategy, they find that they can improve the efficiency of test-time compute scaling by a factor of **2-4x**. When comparing benefits obtained from additional test-time compute against benefits from additional pre-training compute in a FLOPs-matched setting, they show for the first time that using test-time computation with seemingly simple methods (i.e., revisions and search) can already scale well on certain types of prompts, providing gains over spending those FLOPs in pretraining. [p. 15-16]

That said, there are also limitations associated with the study that future work can aim to address. [p. 16]

## Further improving test-time compute scaling

[p. 16] In this work the authors focused on improving the test-time compute scaling of two primary mechanisms: the verifier and the proposal distribution (via revisions). While they combined verifiers with revisions in Section 6, they did not experiment with PRM tree-search techniques in combination with revisions. Neither did they study other techniques such as critique and revise [23]. Future work should investigate how test-time compute scaling can be further improved by combining a variety of these approaches. Additionally, the authors found that across the board these schemes provided small gains on hard problems; future work should develop new ways of using test-time compute which can circumvent this limitation. [p. 16]

## Assessing question difficulty quickly

[p. 16] The authors used a notion of question difficulty as a simple sufficient statistic for approximating the compute-optimal test-time scaling strategy. While this scheme was effective, estimating their notion of difficulty requires applying a non-trivial amount of test-time compute itself. Future work should consider alternative ways of more efficiently estimating question difficulty (e.g., by pretraining or finetuning models to directly predict difficulty of a question) or dynamically switching between assessing difficulty and attempting to solve a question. [p. 16]

## Interleaving test-time and training-time compute

[p. 16] The authors focused purely on test-time compute scaling in this work and the degree to which test-time compute can be traded off for additional pretraining. However, in the future, they envision that the outputs of applying additional test-time compute can be distilled back into the base LLM, enabling an iterative self-improvement loop that operates on open-ended natural language. To this end, future work should extend these findings and study how the outputs of applying test-time compute can be used to improve the base LLM itself. [p. 16]
