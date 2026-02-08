# 3. LongRoPE [p. 4-6]

Motivated by the findings, the authors present LongRoPE, which first introduces an efficient search algorithm to fully exploit the two non-uniformities, and then uses it to extend LLM context window beyond 2 million tokens.

## 3.1. Problem Formulation [p. 4]

The two non-uniformities can lead to a vast solution space and introduce complexities in optimization. To address it, the authors frame the multidimensional non-uniform position interpolation optimization as a search problem.

For a LLM targeting a context window size of $L'$ and lengthy input documents $\mathbf{X}$, where each $\mathbf{x} \in \mathbf{X}$ surpasses $L'$ in token length, denote the original rotary angle of the $i^{th}$ dimension in RoPE embedding at token position $n$ as $\frac{n}{\beta^i}$. The optimization problem is then formulated as follows:

$$\arg\min_{\mathbf{x} \in \mathbf{X}; |\mathbf{x}| \geq L'} \mathcal{L} \text{ (LLM(RoPE, } \mathbf{X}\text{))} \text{, where}$$

$$\text{RoPE}_i(n) = \left[\cdots, cos\left(\mathbb{I}(\hat{\lambda}_i, \hat{n}) \times \frac{n}{\beta^i}\right), sin\left(\mathbb{I}(\hat{\lambda}_i, \hat{n}) \times \frac{n}{\beta^i}\right), \cdots\right]$$

$$i = 0, \cdots, \frac{d}{2} - 1;$$
$$n \in [0, |\mathbf{x}|);$$

$$\text{where } \mathbb{I}(\hat{\lambda}_i, \hat{n}) = \begin{cases} 1 & n < \hat{n} \\ \frac{1}{\hat{\lambda}_i} & n \geq \hat{n} \end{cases}$$
(3)

where the authors introduce a set of rescale factors, $\mathbb{I}(\hat{\lambda}_i, \hat{n})$, to cover the two forms of non-uniformities. $\hat{\lambda}_i$ and $\hat{n}$ denote the non-uniformity of RoPE dimensions and token positions, respectively. $\mathbb{I}(\hat{\lambda}_i, \hat{n})$ is used to rescale the rotation angle for the $i^{th}$ RoPE dimension, where $\hat{\lambda}_i$ is the rescale factor and $\hat{n}$ is the token position threshold. For initial $\hat{n}$-1 token positions, the rescale factor $\hat{\lambda}_i$ will not take effect, and the original RoPE rotary angle $\frac{n}{\beta^i}$ is used. For tokens at positions $n \geq \hat{n}$, the rescale factor is applied.

Given a target context window size of $L'$, the objective is to find the optimal rescale factors ($\mathbb{I}(\hat{\lambda}_0, \hat{n})$, $\mathbb{I}(\hat{\lambda}_1, \hat{n})$, ..., $\mathbb{I}(\hat{\lambda}_i, \hat{n})$, ...) from the $1^{st}$ to $d^{th}$ RoPE dimension. As a result, the target LLM, with the rescaled RoPE, can achieve a minimum next token prediction loss, $\mathcal{L}$ (i.e., the perplexity), for input samples $\mathbf{X}$ with a token length of $L'$.

## 3.2. Searching the Non-uniform Position Interpolation [p. 4-5]

To solve the problem in Eq. 3, the authors introduce a simple yet highly effective method, which searches for the optimal RoPE rescale factors to fully exploit the multidimensional non-uniformities in position embedding.

**Search space.** A large search space is designed to include the two non-uniformities. Table 4 illustrates the search space. Specifically, the search allows a specialized rescale factor for each dimension in RoPE embedding. To simplify search space design, the authors search $\lambda_i$ and $\hat{n}$ instead of searching for $\mathbb{I}(\hat{\lambda}_i, \hat{n})$, where $\hat{\lambda}_i = 1/\lambda_i$.

**Table 4.** Search space for RoPE rescale factors. Tuples of three values represent the lowest value, highest, and step size. [p. 4]

| Non-uniformity | Notation | Search Space |
|---|---|---|
| RoPE dimension | $\lambda_i$ | (1.0, extension ratio $s \times 1.25$, 0.01) |
| Starting tokens | $\hat{n}$ | {0, 1, 2, 4, 8, 12, 16, 20, 24, 28, 32, 64, 128, 256} |

As shown in Table 4, $\lambda_i$ is allowed to search from a minimum value of 1.0 (i.e., direct extrapolation) to a maximum value of $s \times 1.25$ (i.e., larger interpolation than PI) with a step size of 0.01, where $s$ is the target context window extension ratio.

$\hat{n}$ controls the number of initial token positions that are retained without position interpolation (i.e., use the original RoPE embedding). Empirically, $\hat{n}$ is allowed to search from {0, 1, 2, 4, 8, 12, 16, 20, 24, 28, 32, 64, 128, 256}. When $\hat{n} = 0$, all token positions use the searched rescale factors.

[p. 5] **Evolution-based search.** The search space in Table 4 spans numerous positional interpolation solutions, posing a significant challenge for efficient exploration. For example, a $s = 4\times$ extension leads to $400^{128/2} \times 14 = 4 \times 10^{167}$ choices. With larger extension ratio, the search space expands exponentially. To address this, the authors use evolution search (Guo et al., 2020) and introduce two optimization techniques to greatly boost search efficiency. Algorithm 1 illustrates the overall search procedure.

**Algorithm 1:** The search algorithm [p. 5]

**Input:** target LLM, input samples **X**, population size $P$, mutation size $N_1$, crossover size $N_2$, max iterations $\mathcal{T}$, mutate probability $p$

1. Top-k = $\phi$;
2. $P_0$ = Initialize_population_with_optimization ($P$, **X**, $p$);
3. **for** $i$=1 to $\mathcal{T}$ **do**
4. &emsp; Compute_perplexity (LLM, $P_{i-1}$, **X**);
5. &emsp; Top-k = Update_Topk (Top-k, $P_{i-1}$);
6. &emsp; $P_{mutation}$ = Mutation_with_mono_constraint (Top-k, $N_1$, $p$);
7. &emsp; $P_{crossover}$ = Crossover_with_mono_constraint (Top-k, $N_2$);
8. &emsp; $P_i$ = $P_{mutation} \cup P_{crossover} \cup$ Top-k;
9. **end for**
10. Return the individual with lowest perplexity in Top-k;

**Optimized initial population generation.** Instead of initializing a population of $P$ rescale factors randomly, the three RoPE rescale factors corresponding to PI, NTK, and YaRN are added as individuals into the initial population. For the remaining $P$-3 individuals, the three rescale factors are randomly mutated with a probability of $p$.

**Monotonically non-decreasing constraint.** After generating the initial population, LLM perplexity is computed for each individual. The top-k individuals become parents for evolution. However, the vast search space can cause naive mutation and crossover to explore poor solutions, leading to unnecessary perplexity computations. This is particularly inefficient when $L'$ is large, given the time-consuming inference of each perplexity calculation.

To address this, a non-decreasing monotonicity constraint is imposed on the sampled RoPE rescaled factors: $\lambda_i \leq \lambda_{i+1}$. Only RoPE that satisfies this constraint is applied to LLM for perplexity evaluation, significantly reducing the search costs. Specifically, $\lambda_i$ is required to increase monotonically with the RoPE dimension (i.e., $i$=0,...,63). This dimensional monotonicity is based on the NTK theory (Jacot et al., 2018; Tancik et al., 2020; LocalLLaMA, 2023b), suggesting that lower dimensions with higher frequency requires less interpolation (i.e., a smaller $\lambda_i$), and higher dimensions with lower frequency can do more interpolation (i.e., a larger $\lambda_i$).

**8x extension without fine-tuning.** The evolutionary search effectively identifies non-uniform RoPE rescale factors, preserving key dimensions and positions to minimize interpolation-induced information loss. As depicted in Fig. 3, the method is able to extend LLaMA2's context window from 4k to 32k without fine-tuning. In contrast, existing methods such as PI, and non-uniform NTK and YaRN cause perplexity to spike after 2x extension.

**Figure 3** (p. 5): "LLaMA-7B perplexity on PG19 and Proof-Pile after extension using different methods, measured without fine-tuning. By fully exploiting the non-uniformities, LongRoPE achieves an **8x extension without fine-tuning**."

The figure has two line plots. Left plot: Perplexity on PG19 full test (y-axis, range ~10-70) vs. context window size (x-axis, 4k to 32k). PI perplexity spikes sharply after 8k reaching ~65+. Dynamic-NTK spikes after 8k. YaRN spikes after ~7k. LongRoPE remains low (~10) out to 32k. Right plot: Perplexity on Proof-Pile (y-axis, range ~2-14) vs. context window size (4k to 32k). Similar pattern: PI, Dynamic-NTK, and YaRN spike after 8k, while LongRoPE remains low (~3-4) through 32k.

## 3.3. Extending LLM Context Window to 2048K [p. 5-6]

**Progressive extension to 2048k.** The method extends the context window of pre-trained LLMs from the traditional 4k to over 2048k. Non-uniform positional interpolation can achieve 8x extension without fine-tuning. For larger extensions (i.e., 512x) fine-tuning is necessary. One method is to search for RoPE rescaled factors under the target 2048k size and then fine-tune. However, this faces challenges due to the prohibitively expensive training resources. Moreover, it is challenging to well fine-tune the LLMs under a large extension ratio (see Appendix).

Therefore, LongRoPE introduces an efficient, progressive method that achieves the target 2048k with just 1k fine-tuning steps at within 256k training length. Three steps:

**Step 1: Extending pre-trained LLM to 256k with LongRoPE search.** Taking LLaMA2 as an example, search is conducted for target context window size of 128k and 256k. The extension ratio at this stage is 32x and 64x, respectively.

**Step 2: Fine-tuning to 256k.** The pre-trained LLM is fine-tuned to achieve the context window of 256k. Specifically, LLaMA2 is first fine-tuned for 400 steps using the RoPE rescaled factors for 128k. Then, the RoPE rescaled factors are replaced to 256k on the finished checkpoint, and an additional 600 steps of fine-tuning are conducted. This method proves more efficient than directly fine-tuning to 256k.

[p. 6] **Step 3: Extending fine-tuned extended LLM to 2048k with LongRoPE search.** A secondary search is performed on the fine-tuned 256k-length LLM. This ultimately results in an extremely large context window size of 2048k without further fine-tuning. The final extension ratio is 512x.

**Shorter context window recovery.** After extending to an extremely long 2048k context window, there is a performance drop within the original context window. This is a known issue of positional interpolation (Chen et al., 2023a), as it forces position embedding in higher dimensions within the original context window to reside in a much narrower region, negatively affecting the language model's performance. With a 512x extension ratio, positions within the original 4k context window become particularly crowded.

To mitigate this, an extra evolution search is performed on the extended LLM to adjust RoPE rescale factors for short context lengths (e.g., 4k and 8k). The maximum allowed $\lambda$ is reduced due to less positional interpolation required for shorter lengths. During inference, the LLM dynamically adjusts the corresponding RoPE rescale factors.
