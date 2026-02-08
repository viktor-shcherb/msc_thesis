# 3.3 Measuring Effective Context Window Size through Passkey Retrieval [p. 7–9]

[p. 7] The authors study the effective context window size, i.e. the maximum distance of a token can *effectively* attend to during inference, of their models after extension. They follow a synthetic evaluation task of passkey retrieval proposed by Mohtashami & Jaggi (2023). In this task, the models are asked to recover a random passkey hidden in a long document. See Figure 3 for the format of the document.

## Methodology

[p. 7] Given a language model, the authors estimate the upper and lower bounds of effective context windows as follows. Suppose the random passkey is $k$ tokens away from the end of the input:
- When a model persistently fails to retrieve the correct passkey value across several independent attempts, it suggests that the effective context window size of the model is less than $k$.
- Conversely, if a model consistently succeeds in retrieving the correct passkey value, the effective context window size of the model is at least $k$.

[p. 7–9] The 7B and 33B LLaMA model variants extended via Position Interpolation or direct fine-tuning are evaluated. For each model, 32 different $k$ uniformly spaced in the targeted context window $L'$ are used, and the tests are run 10 times for each $k$, where each time a random passkey of 5 random digits is used.

$k_{\max}$ is defined as the maximum $k$ such that, for all $k' \leq k$, the model has a success rate of at least 20% on $k'$. [p. 9]

## Results

[p. 9] Models extended via Position Interpolation all successfully attain their desired extension objectives in terms of effective context window sizes, indicated by the effective context window size reaching maximum $k_{\max} = L'$, after merely fine-tuning for 200 steps, consistently across both 7B and 33B model sizes and up to 32768 context windows.

In contrast, LLaMA models that are extended via direct fine-tuning only saw a minimal increase of the effective context window size $k_{\max}$ from 2048 to 2560, even after fine-tuning for more than 10000 steps, with no clear indication of an acceleration in the increase of window size. [p. 9]

## Table 4: Effective context window sizes after fine-tuning [p. 9]

FT: Direct fine-tuning. PI: Position Interpolation.

| Size | Context Window | Method | 200 | 400 | 600 | 800 | 1000 | 10000 |
|------|---------------|--------|------|------|------|------|------|-------|
| 7B | 8192 | FT | 1792 | 2048 | 2048 | 2048 | 2304 | 2560 |
| 33B | 8192 | FT | 1792 | 2048 | 1792 | 2048 | 2304 | - |
| 7B | 8192 | PI | 8192 | 8192 | 8192 | 8192 | 8192 | - |
| 7B | 16384 | PI | 16384 | 16384 | 16384 | 16384 | 16384 | - |
| 7B | 32768 | PI | 32768 | 32768 | 18432 | 32768 | 32768 | - |
| 33B | 8192 | PI | 8192 | 8192 | 8192 | 8192 | 8192 | - |
| 33B | 16384 | PI | 16384 | 16384 | 16384 | 16384 | 16384 | - |

## Figure 3: Prompt format for passkey retrieval [p. 9]

**Figure 3** (p. 9): "Prompt format for passkey retrieval. We use the exact same prompt as proposed by Mohtashami & Jaggi (2023). Here the passkey 12345 is replaced with a random 5-digit numbers during test."

The prompt format is:
```
There is an important info hidden inside a lot of irrelevant text. Find
it and memorize them. I will quiz you about the important information
there.
The grass is green. The sky is blue. The sun is yellow. Here we go.
There and back again. (repeat X times)
The pass key is 12345. Remember it. 12345 is the pass key.
The grass is green. The sky is blue. The sun is yellow. Here we go.
There and back again. (repeat Y times)
What is the pass key? The pass key is
```
