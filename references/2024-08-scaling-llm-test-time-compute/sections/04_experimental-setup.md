# 4. Experimental Setup [p. 6]

[p. 6] The authors outline their experimental setup for conducting the analysis with multiple verifier design choices and proposal distributions, followed by the analysis results in subsequent sections.

## Datasets

[p. 6] Test-time compute is expected to be most helpful when models already have all the basic "knowledge" needed to answer a question, and instead the primary challenge is about drawing (complex) inferences from this knowledge. The authors focus on the **MATH** [13] benchmark, which consists of high-school competition level math problems with a range of difficulty levels. For all experiments, they use the dataset split consisting of **12k train** and **500 test questions**, used in Lightman et al. [22].

## Models

[p. 6] The analysis is conducted using the **PaLM 2-S*** [3] **(Codey)** base model. The authors believe this model is representative of the capabilities of many contemporary LLMs, and therefore think that their findings likely transfer to similar models. Most importantly, this model attains a non-trivial performance on MATH and yet has not saturated, so it is expected to provide a good test-bed.

## Difficulty Estimation for Compute-Optimal Scaling

[p. 6] In practice, researchers are only given access to test prompts that they don't know the answer to. In order to be feasible in practice, a compute-optimal scaling strategy conditioned on difficulty needs to first assess difficulty and then utilize the right scaling strategy to solve this problem. Therefore, the authors approximate the problem's difficulty via a **model-predicted notion of difficulty**, which performs the same binning procedure over the averaged final answer score from a learned verifier (and not groundtruth answer correctness checks) on the same set of **2048 samples per problem**. They refer to this setting as **model-predicted difficulty** and the setting which relies on the actual groundtruth correctness as **oracle difficulty**.

While model-predicted difficulty removes the need for knowing the ground truth label, estimating difficulty in this way still incurs additional computation cost during inference. That said, this one-time inference cost can be subsumed within the cost for actually running an inference-time strategy (e.g., when using a verifier, one could use the same inference computation for also running beam search). More generally, this is akin to exploration-exploitation tradeoff in reinforcement learning: in actual deployment conditions, we must balance the compute spent in assessing difficulty vs applying the most compute-optimal approach. This is a crucial avenue for future work (see Section 8) and their experiments do not account for this cost largely for simplicity, since their goal is to present some of the first results of *what is in fact possible* by effectively allocating test-time compute.

[p. 6] So as to avoid confounders with using the same test set for computing difficulty bins and for selecting the compute-optimal strategy, the authors use two-fold cross validation on each difficulty bin in the test set. They select the best-performing strategy according to performance on one fold and then measure performance using that strategy on the other fold and vice versa, averaging the results of the two test folds.
