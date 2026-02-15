# 2.3 Reinforcement Learning (continued) [p. 6]

## 2.3.3 Length Penalty (continued) [p. 6]

$(y_1, z_1), \ldots, (y_k, z_k)$ of problem $x$ with true answer $y^*$, let $\text{len}(i)$ be the length of $(y_i, z_i)$, min_len = $\min_i \text{len}(i)$ and max_len = $\max_i \text{len}(i)$. If max_len = min_len, we set length reward zero for all responses, as they have the same length. Otherwise the length reward is given by

$$\text{len\_reward}(i) = \begin{cases} \lambda & \text{If } r(x, y_i, y^*) = 1 \\ \min(0, \lambda) & \text{If } r(x, y_i, y^*) = 0 \end{cases} \quad \text{where } \lambda = 0.5 - \frac{\text{len}(i) - \text{min\_len}}{\text{max\_len} - \text{min\_len}} \,.$$

In essence, we promote shorter responses and penalize longer responses among correct ones, while explicitly penalizing long responses with incorrect answers. This length-based reward is then added to the original reward with a weighting parameter.

In our preliminary experiments, length penalty may slow down training during the initial phases. To alleviate this issue, we propose to gradually warm up the length penalty during training. Specifically, we employ standard policy optimization without length penalty, followed by a constant length penalty for the rest of training.

## 2.3.4 Sampling Strategies [p. 6]

Although RL algorithms themselves have relatively good sampling properties (with more difficult problems providing larger gradients), their training efficiency is limited. Consequently, some well-defined prior sampling methods can yield potentially greater performance gains. We exploit multiple signals to further improve the sampling strategy. First, the RL training data we collect naturally come with different difficulty labels. For example, a math competition problem is more difficult than a primary school math problem. Second, because the RL training process samples the same problem multiple times, we can also track the success rate for each individual problem as a metric of difficulty. We propose two sampling methods to utilize these priors to improve training efficiency.

**Curriculum Sampling** We start by training on easier tasks and gradually progress to more challenging ones. Since the initial RL model has limited performance, spending a restricted computation budget on very hard problems often yields few correct samples, resulting in lower training efficiency. Meanwhile, our collected data naturally includes grade and difficulty labels, making difficulty-based sampling an intuitive and effective way to improve training efficiency.

**Prioritized Sampling** In addition to curriculum sampling, we use a prioritized sampling strategy to focus on problems where the model underperforms. We track the success rates $s_i$ for each problem $i$ and sample problems proportional to $1 - s_i$, so that problems with lower success rates receive higher sampling probabilities. This directs the model's efforts toward its weakest areas, leading to faster learning and better overall performance.

## 2.3.5 More Details on Training Recipe [p. 6]

**Test Case Generation for Coding** Since test cases are not available for many coding problems from the web, we design a method to automatically generate test cases that serve as a reward to train our model with RL. Our focus is primarily on problems that do not require a special judge. We also assume that ground truth solutions are available for these problems so that we can leverage the solutions to generate higher quality test cases.

We utilize the widely recognized test case generation library, CYaRon<sup>1</sup>, to enhance our approach. We employ our base Kimi k1.5 to generate test cases based on problem statements. The usage statement of CYaRon and the problem description are provided as the input to the generator. For each problem, we first use the generator to produce 50 test cases and also randomly sample 10 ground truth submissions for each test case. We run the test cases against the submissions. A test case is deemed valid if at least 7 out of 10 submissions yield matching results. After this round of filtering, we obtain a set of selected test cases. A problem and its associated selected test cases are added to our training set if at least 9 out of 10 submissions pass the entire set of selected test cases.

In terms of statistics, from a sample of 1,000 online contest problems, approximately 614 do not require a special judge. We developed 463 test case generators that produced at least 40 valid test cases, leading to the inclusion of 323 problems in our training set.

**Reward Modeling for Math** One challenge in evaluating math solutions is that different written forms can represent the same underlying answer. For instance, $a^2 - 4$ and $(a + 2)(a - 2)$ may both be valid solutions to the same problem. We adopted two methods to improve the reward model's scoring accuracy:

1. Classic RM: Drawing inspiration from the InstructGPT (Ouyang et al. 2022) methodology, we implemented a value-head based reward model and collected approximately 800k data points for fine-tuning. The model ultimately

<sup>1</sup>https://github.com/luogu-dev/cyaron
