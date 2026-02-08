# 3. How to Scale Test-Time Computation Optimally [p. 4-6]

[p. 4] Given the unification of various methods, the authors now seek to understand how to *most effectively* utilize test-time computation to improve LM performance on a given prompt.

**Problem setup** (boxed text, p. 4):
> "We are given a prompt and a test-time compute budget within which to solve the problem. Under the abstraction above, there are different ways to utilize test-time computation. Each of these methods may be more or less effective depending on the specific problem given. How can we determine the *most effective* way to utilize test-time compute for a given prompt? And how well would this do against simply utilizing a much bigger pretrained model?" [p. 4]

[p. 4-5] When either refining the proposal distribution or searching against a verifier, there are several different hyper-parameters that can be adjusted to determine how a test-time compute budget should be allocated. For example, when using a model finetuned for revisions as the proposal distribution and an ORM as the verifier, one could either:
- Spend the full test-time compute budget on generating N independent samples in parallel and then apply best-of-N
- Sample N revisions in sequence using a revision model and then select the best answer with an ORM
- Strike a balance between these extremes

Intuitively, "easier" problems may benefit more from revisions (since the model's initial samples are more likely to be on the right track), while challenging problems may require more exploration of different high-level problem solving strategies, so sampling many times independently in parallel may be preferable. [p. 5]

In the case of verifiers, there is also the option to choose between different search algorithms (e.g., beam-search, lookahead-search, best-of-N), each of which may exhibit different properties depending on the quality of the verifier and proposal distribution at hand. More sophisticated search procedures might be more useful in harder problems compared to a much simpler best-of-N or majority baseline. [p. 5]

## 3.1. Test-Time Compute-Optimal Scaling Strategy

[p. 5] The authors define the **"test-time compute-optimal scaling strategy"** as the strategy that chooses hyperparameters corresponding to a given test-time strategy for maximal performance benefits on a given prompt at test time.

Formally, define Target($\theta$, $N$, $q$) as the distribution over natural language output tokens induced by the model for a given prompt $q$, using test-time compute hyper-parameters $\theta$, and a compute budget of $N$. The goal is to select the hyper-parameters $\theta$ which maximize the accuracy of the target distribution for a given problem:

$$\theta^*_{q, a^*(q)}(N) = \text{argmax}_\theta \left( \mathbb{E}_{y \sim \text{Target}(\theta, N, q)} \left[ \mathbb{1}_{y = y^*(q)} \right] \right)$$
(Equation 1)

where $y^*(q)$ denotes the ground-truth correct response for $q$, and $\theta^*_{q, y^*(q)}(N)$ represents the test-time compute-optimal scaling strategy for the problem $q$ with compute budget $N$. [p. 5]

## 3.2. Estimating Question Difficulty for Compute-Optimal Scaling

[p. 5] To effectively analyze the test-time scaling properties of the different mechanisms discussed in Section 2, the authors prescribe an approximation to the optimal strategy $\theta^*_{q, y^*(q)}(N)$ as a function of a statistic of a given prompt. This statistic estimates a notion of *difficulty* for a given prompt. The compute-optimal strategy is defined as a function of the difficulty of the prompt. Despite being only an approximate solution to Equation 1, the authors find that it can still induce substantial improvements in performance over a baseline strategy of allocating inference-time compute in an ad-hoc or uniformly-sampled manner. [p. 5]

**Difficulty estimation procedure:** The question difficulty assigns a given question to one of **five difficulty levels**. These discrete difficulty categories are used to estimate $\theta^*_{q, y^*(q)}(N)$ on a validation set for a given test-time compute budget. The compute-optimal strategies are then applied on the test-set, selecting the best performing test-time compute strategy for each difficulty bin independently. Question difficulty acts as a sufficient statistic of a question when designing the compute-optimal strategy. [p. 5]

**Defining difficulty of a problem.** Following the approach of Lightman et al. [22], question difficulty is defined as a function of a given base LLM. Specifically, the model's pass@1 rate -- estimated from 2048 samples -- on each question in the test set is binned into **five quantiles**, each corresponding to increasing difficulty levels. This model-specific notion of difficulty bins was found to be more predictive of the efficacy of using test-time compute in contrast to the hand-labeled difficulty bins in the MATH dataset. [p. 5]

[p. 5-6] Assessing a question's difficulty as described above assumes oracle access to a ground-truth correctness checking function, which is not available upon deployment. Therefore, the authors approximate the problem's difficulty via a **model-predicted notion of difficulty**, which performs the same binning procedure over the averaged final answer score from a learned verifier (and not groundtruth answer correctness checks) on the same set of 2048 samples per problem. The setting using groundtruth correctness is referred to as **oracle difficulty** and the approximation as **model-predicted difficulty**. [p. 6]

[p. 6] While model-predicted difficulty removes the need for knowing the ground truth label, estimating difficulty this way still incurs additional computation cost during inference. However, this one-time inference cost can be subsumed within the cost for actually running an inference-time strategy (e.g., when using a verifier, one could use the same inference computation for also running search). More generally, this is akin to the exploration-exploitation tradeoff in reinforcement learning: in actual deployment conditions, we must balance the compute spent in assessing difficulty vs applying the most compute-optimal approach. This is a crucial avenue for future work (see Section 8) and the authors do not account for this cost largely for simplicity, since their goal is to present some of the first results of *what is in fact possible* by effectively allocating test-time compute. [p. 6]

[p. 6] To avoid confounders with using the same test set for computing difficulty bins and for selecting the compute-optimal strategy, the authors use **two-fold cross validation** on each difficulty bin in the test set. They select the best-performing strategy according to performance on one fold and then measure performance using that strategy on the other fold and vice versa, averaging the results of the two test folds. [p. 6]
