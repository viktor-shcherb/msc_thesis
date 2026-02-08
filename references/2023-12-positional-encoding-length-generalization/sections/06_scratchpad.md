# Does Scratchpad Render The Choice of Positional Encoding Irrelevant? [p. 7-8]

[p. 7] In scratchpad/CoT prompting, the model generates intermediate computations required to reach the final answer as explicit parts of the output. Such mechanisms provide a direct decomposition and storage for intermediate values, which has been shown to improve the length generalization of Transformers even at small scale (Nye et al., 2021). Since scratchpad only modifies the model's input and output (not the architecture), it is unclear and unexplored how architectural choices such as positional encoding affect the length generalization in the presence of scratchpad. To answer this question, all PEs are trained *with* and *without* scratchpad on the mathematical and reasoning group of tasks, and their performance is compared.

Moreover, the decision of how to represent the intermediate computations in the scratchpad (i.e. the scratchpad format) is an important design choice that has a non-trivial impact on the model's performance (Bueno et al., 2022).

To account for this, five components in each step of scratchpad are considered: `<input>` ($\mathcal{I}$), `<computation>` ($\mathcal{C}$), `<output>` ($\mathcal{O}$), `<variable_update>` ($\mathcal{V}$), and `<remaining_input>` ($\mathcal{R}$) (Figure 5). Different variations of scratchpad format are created by enabling or disabling each component, which allows systematic study of their impact.

**Figure 5** (p. 7): "Example of an addition task depicted with its first scratchpad step. Each step consists of five components: Step Input $\mathcal{I}$, Step Computation $\mathcal{C}$, Intermediate Step Output $\mathcal{O}$, Variable Updates $\mathcal{V}$, and Remaining Input $\mathcal{R}$."

The figure shows a worked example of an addition task:
- Input: `Compute 5 3 7 2 6 + 1 9 1 7 =`
- $\mathcal{I}$: For digits 6 and 7,
- $\mathcal{C}$: We have ( 6 + 7 + carry ) % 10 = 13 % 10 = 13 % 10
- $\mathcal{O}$: Which is equal to 3 .
- $\mathcal{V}$: We update carry to 13 // 10 = 1.
- $\mathcal{R}$: So, the remaining input is 5 3 7 2 + 1 9 1
- The answer is 5 5 6 4 3.

**Figure 6** (p. 8): "Mean ranks of scratchpad format aggregated across all models per each dataset. The effectiveness of scratchpad is task dependent."

The figure is a grouped bar chart with x-axis showing tasks (Addition, LEGO, Parity, Polynomial Eval., Sort, Summation) and y-axis showing Mean Reciprocal Rank (0 to 1). Bars represent scratchpad formats: No Scratchpad, Full, Full - "Step Input", Full - "Step Computation", Full - "Step Output", Full - "Intermediate Vars", Full - "Remaining Parts", and Minimal (Only Compute+Output). Key observations:
- For Addition: Full scratchpad formats achieve the highest ranks (~0.75-1.0); No Scratchpad is lowest.
- For LEGO: Full format performs best; removing components degrades performance.
- For Parity: No Scratchpad performs comparably to Full formats.
- For Polynomial Eval.: Similar performance across formats.
- For Sort: Full format provides moderate improvement.
- For Summation: Full formats provide moderate improvement.

[p. 7-8] Figure 6 summarizes the results. Similar to the remarks made by Nye et al. (2021) and Anil et al. (2022), across all PEs and regardless of the format, scratchpad is beneficial solely for the addition task. Additionally, the findings indicate that having a positional encoding with robust length generalization is crucial since scratchpad/CoT alone may not enhance the generalization.

Footnote 1: Since using scratchpad creates very long sequences, they follow Nye et al. (2021) and set the length threshold $L = 8$ for tasks that use it to avoid out-of-memory errors.

## 6.1 Which part of the sequence is attended to?

[p. 7-8] The scratchpad format that is often used (Nye et al., 2021), similar to Figure 5, contains redundant information. One such example is the repetition of the remaining portion of an input ($\mathcal{R}$) in each step of the scratchpad. The attention can attend to this information directly from the main input. It remains unclear which specific part of the scratchpad different PEs rely on to solve the task.

To address this question, the models trained with full Format on addition (the case in which scratchpad is helpful across all PEs) are taken, and their attentions are examined. Specifically, for tokens in the output sequence, the *distance* $d$ between the current query $\mathbf{q}_t$ and the attended key $\mathbf{k}_n$ is calculated as $(t - n + 1)$ and subsequently normalized based on the length of the sequence at the present step. The normalized value is denoted as $\bar{d}$.

**Figure 7** (p. 8): "Distribution of the normalized distance between the query and the key of the self-attention (addition task + full scratchpad), averaged across all layers and heads."

The figure shows five histograms (one per PE method), each showing count (y-axis, 0 to 70000) vs Normalized Attended Distance $\bar{d}$ (x-axis, 0 to 1). Key observations:
- **NoPE**: Bimodal distribution with a large peak near $\bar{d} = 0$ (short-range) and a smaller peak near $\bar{d} = 1$ (long-range, i.e., attending to input).
- **T5's Relative PE**: Very similar bimodal distribution to NoPE, with peaks at both short-range and long-range distances.
- **ALiBi**: Strongly favors short-range attention (large peak near $\bar{d} = 0$), consistent with its recency bias. Very little long-range attention.
- **Rotary**: More uniformly distributed, resembling APE.
- **Absolute Position Embedding (APE)**: Relatively uniform distribution across distances.

NoPE and T5's Relative PE resemble each other and exhibit a bimodal distribution, reflecting both short-range and long-range attention. Conversely, ALiBi (due to its recency bias) strongly favors short-range attention. Rotary, on the other hand, produces a distribution resembling APE, which is more uniformly distributed. Notably, NoPE and T5's RPE are the top-performing PEs in this setup, which suggests the bimodal distribution to be more optimal.
