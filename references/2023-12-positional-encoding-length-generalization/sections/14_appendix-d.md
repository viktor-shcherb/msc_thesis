# Appendix D: Experimental Details [p. 23-25]

## D.1 Tasks [p. 23-25]

[p. 23] Details and additional examples of the tasks and datasets used in the evaluation. For each task, 100K examples are sampled for the training set and 10K for the test. 15% of the train is used as the validation set.

### Addition

[p. 23] (Nye et al., 2021) The model computes the sum of two numbers. Each number is represented as a sequence of digits separated by space, so the model has access to the exact digits.

Input: `Compute: 5 3 7 2 6 + 1 9 1 7 7 ?`
Output: `The answer is 5 5 6 4 3.`

Length buckets are created based on the number of digits in each number, e.g. 6-by-3, 6-by-4, etc. For the training set, buckets are used where one of the numbers has at most $L$ digits. For the test set, buckets are used where any of the numbers have at most $L$ digits. The model is evaluated on the correctness of its predicted result.

### Polynomial Evaluation

[p. 23] (Nye et al., 2021) The model evaluates a polynomial expression at a given value of $x$. The polynomial terms and digits are separated to make sure the tokenizer does not glue symbols together.

Input: `Evaluate x = 3 in ( 3 x ** 0 + 1 x ** 1 + 1 x ** 2 ) % 10 ?`
Output: `The answer is 5.`

The length bucket is created based on the number of terms in the polynomial expression. $x$ is sampled from $\mathcal{U}(-2, 2)$, the degree of each term from $\mathcal{U}(0, 3)$, and the coefficient of each term from $\mathcal{U}(-3, 3)$. The modulo of the result by 10 is taken to make the task easier for the model and ensure the generalization of the length of the problem instance is measured, not the value of the polynomial. The model is evaluated on the correctness of its predicted result.

### Sorting

[p. 23-24] (Saxton et al., 2019) The model sorts a sequence of input numbers. Two variants are used: Single Token and Multi Digit.

**Single Token variant:** An alphabet of 50 tokens from the model's vocabulary is created and a canonical ordering is fixed among them (a through task). Each instance is a sequence of tokens from the alphabet in a random order, and the model sorts them in canonical order.

Input: `Sort the following numbers: 3 1 4 1 5 ?`
Output: `The answer is 1 1 3 4 5.`

**Multi Digit variant:** A sequence of multi digit/tokens numbers is presented to the model to sort in ascending order. Each number is represented by its digits and they are separated by a space.

Input: `Sort the following numbers: 3 1, 4 1, 5 9, 1 2 6, 5 3 3 ?`
Output: `The answer is 3 1, 4 1, 5 9, 1 2 6, 5 3 3.`

[p. 24] In this case, each number is sampled from $\mathcal{U}(0, 10000)$. In both cases, the length bucket is created based on the length of the input sequence. The model is evaluated on the correctness of its predicted result.

### Summation

[p. 24] (Saxton et al., 2019) The model computes the sum of a sequence of input numbers modulo 10 to specifically measure how the model generalizes to longer sequences, not the value of summation result.

Input: `Compute: ( 1 + 2 + 3 + 4 + 7 ) % 10 ?`
Output: `The answer is 7.`

Each digit is randomly sampled from $\mathcal{U}(1, 9)$. The length bucket is created based on the length of the input sequence. The model is evaluated on the correctness of its predicted result.

### Parity

[p. 24] (Anil et al., 2022) The model computes the parity of a binary sequence.

Input: `Is the number of 1's even in [ 1 0 0 1 1] ?`
Output: `The answer is No.`

### LEGO

[p. 24] (Zhang et al., 2023) The model is provided with a simple computation graph (DAG), where each node represents a variable, and variables are connected by simple operations which created the edges in the computation graph. See Zhang et al. (2023) for a detailed description.

Input: `If a = -1; b = -a; c = +b; d = +c. Then what is c?`
Output: `The answer is +1.`

To sample each example, the list of variables is first sampled based on the length of the example, then the value of each variable is uniformly sampled to make sure all variables are represented with both -1 and +1. Finally, given the value of variables, the operation on each edge is deterministically computed. For each example, all variables from the middle of the computation graph to the end are queried. The model is evaluated on the correctness of its predicted result.

### Copy

[p. 25] The model repeats the input sequence in the output. Multiple variants are created to better understand the models' generalization behavior.

Input: `Copy the following words: <w1> <w2> <w3> <w4> <w5> .`
Output: `<w1> <w2> <w3> <w4> <w5>`

In the first variant, the input tokens are the same, so the model basically counts the number of input tokens. In the second variant, the model replaces the input tokens with another token sampled from the vocabulary. In the third variant, input tokens are sampled from the model's vocabulary and the model predicts them in the same order. 2x versions of variants 1 and 3 are also created to make the tasks more challenging.

### Reverse

[p. 25] The model reverses the order of input tokens in its output. Two variants are created.

Input: `Reverse the following words: <w1> <w2> <w3> <w4> <w5> .`
Output: `<w5> <w4> <w3> <w2> <w1> .`

In the first variant, the tokens are randomly sampled from the model's vocabulary. In the second variant, the model reverses the order of input tokens (as in the first variant) but also reverses it one more time, recreating the original input.

## D.2 Hyperparameters [p. 25-26]

[p. 25] The same hyperparameters are used for all models and positional encoding schemes. In initial experiments, a few more hyperparameters were tried such as lr $\in \{0.00001, 0.00003, 0.00005\}$ and WeightDecay $\in \{0, 0.05, 0.1\}$, but no significant difference was observed in the results.

**Table 2:** Summary of hyperparameters used in the experiments. [p. 26]

| Parameter | Value |
|---|---|
| Optimizer | AdamW |
| Learning rate | 0.00003 |
| Weight Decay | 0.05 |
| Batch size | 64 |
| Learning Rate Scheduler | Polynomial |
| Warm Up | 6% of training steps |
| # Train Steps | 40K steps |
| Decoding Method | Greedy (No Sampling) |
| Dropout *(taken from HuggingFace)* | 0.1 |
| Model dimension *(taken from HuggingFace)* | 768 |
| # Layers *(taken from HuggingFace)* | 12 |
| # Attention Heads *(taken from HuggingFace)* | 12 |

## D.3 Compute [p. 25]

[p. 25] Single-GPU training setup used for the models. Experiments ran on a mix of NVIDIA V100 32G, NVIDIA RTX8000 48G, NVIDIA A100 40G, and NVIDIA A100 80G GPUs. Depending on the GPU type and the positional encoding, each training run took 6 to 15 hours, per each seed, on average to complete. Considering all the datasets, positional encoding schemes, in addition to the scratchpad experiments, and three seeds, about 870 individual training runs were conducted for the results in the paper.

## D.4 Reproducibility [p. 25]

[p. 25] All experiments employed open-source libraries, specifically HuggingFace (Wolf et al., 2020) from which the implementation was utilized as a foundation for the training loop, optimizer, and the Transformer architecture. To ensure reproducibility, a singularity binary with all dependencies and libraries will be released to enable running experiments on any machine with NVIDIA GPUs and at any time in the future. Every reported number in the paper is linked to the source code package that deterministically (up to GPU stochasticity) reproduces the results, which are released publicly on GitHub at https://github.com/McGill-NLP/length-generalization.
