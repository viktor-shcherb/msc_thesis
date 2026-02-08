# 4.6 Model Ablations [p. 15–16]

[p. 15]

The authors perform a series of detailed ablations on components of the model, focusing on the setting of language modeling with size $\approx 350M$ models at Chinchilla token counts (same setting as Figure 4). [p. 15]

## 4.6.1 Architecture

[p. 15–16]

Table 6 investigates the effects of the architecture (block) and its inner SSM layer (Figure 3). The authors find that:

- Among previous non-selective (LTI) SSMs, which are equivalent to global convolutions, performance is very similar. [p. 15]
- Replacing the complex-valued S4 variant from previous work with a real-valued one does not affect performance much, suggesting that (at least for LM) real-valued SSMs may be a better choice when accounting for hardware efficiency. [p. 15]
- Replacing any of these with a selective SSM (S6) significantly improves performance, validating the motivation of Section 3. [p. 15]
- The Mamba architecture performs similarly to the H3 architecture (and seems slightly better when using a selective layer). [p. 16]

The authors also investigate interleaving the Mamba block with other blocks such as MLP (a traditional architecture) and MHA (a hybrid attention architecture) in Appendix E.2.2. [p. 16]

## 4.6.2 Selective SSM

[p. 16]

Table 7 ablates the selective SSM layer by considering different combinations of selective $\Delta$, **B**, and **C** parameters (Algorithm 2), showing that $\Delta$ is the most important parameter due to its connection to RNN gating (Theorem 1). [p. 16]

Table 8 considers different initializations of the SSM, which have been shown to make a large difference in some data modalities and settings (Gu, Goel, and Re 2022; Gu, Gupta, et al. 2022). On language modeling, the authors find that simpler real-valued diagonal initializations (S4D-Real, row 3) instead of more standard complex-valued parameterizations (S4D-Lin, row 1) perform better. Random initializations also work well, consistent with findings from prior work (Mehta et al. 2023). [p. 16]

Table 9 and Table 10 consider varying the dimension of the $\Delta$ and ($\boldsymbol{B}, \boldsymbol{C}$) projections respectively. Changing them from static to selective provides the most benefit, while increasing the dimensions further generally improves performance modestly with a small increase in parameter count. [p. 16]

Of particular note is the dramatic improvement of the selective SSM when the state size $N$ is increased, with over a 1.0 perplexity improvement for a cost of only 1% additional parameters. This validates the core motivation in Sections 3.1 and 3.3. [p. 16]

## Tables

**Table 6** (p. 16): "(**Ablations: Architecture and SSM layer.**) The Mamba block performs similarly to H3 while being simpler. In the inner layer, there is little difference among different parameterizations of LTI models, while selective SSMs (S6) provide a large improvement. More specifically, the S4 (real) variant is S4D-Real and the S4 (complex) variant is S4D-Lin."

| Model | Arch. | SSM Layer | Perplexity | | Model | Arch. | SSM Layer | Perplexity |
|-------|-------|-----------|------------|-|-------|-------|-----------|------------|
| Hyena | H3 | Hyena | 10.24 | | - | Mamba | Hyena | 10.75 |
| H3 | H3 | S4 (complex) | 10.30 | | - | Mamba | S4 (complex) | 10.54 |
| - | H3 | S4 (real) | 10.34 | | - | Mamba | S4 (real) | 10.56 |
| - | H3 | S6 | **8.95** | | Mamba | Mamba | S6 | **8.69** |

**Table 7** (p. 16): "(**Ablations: Selective parameters.**) $\Delta$ is the most important parameter (Theorem 1), but using multiple selective parameters together synergizes."

| Selective $\Delta$ | Selective $\boldsymbol{B}$ | Selective $\boldsymbol{C}$ | Perplexity |
|---|---|---|---|
| ✗ | ✗ | ✗ | 10.93 |
| ✗ | ✓ | ✗ | 10.15 |
| ✗ | ✗ | ✓ | 9.98 |
| ✓ | ✗ | ✗ | 9.81 |
| ✓ | ✓ | ✓ | 8.71 |

**Table 8** (p. 16): "(**Ablations: Parameterization of $\boldsymbol{A}$.**) The more standard initializations based on S4D-Lin (Gu, Gupta, et al. 2022) perform worse than S4D-Real or a random initialization, when the SSM is selective."

| $\boldsymbol{A}_n$ Initialization | Field | Perplexity |
|---|---|---|
| $A_n = -\frac{1}{2} + ni$ | Complex | 9.16 |
| $A_n = -1/2$ | Real | 8.85 |
| $A_n = -(n+1)$ | Real | 8.71 |
| $A_n \sim \exp(\mathcal{N}(0,1))$ | Real | 8.71 |

**Table 9** (p. 17): "(**Ablations: Expressivity of $\Delta$.**) The selection mechanism of $\Delta$ constructs it with a projection of the input. Projecting it even to dim. 1 provides a large increase in performance; increasing it further provides further improvements at the cost of a modest increase in parameters. State size fixed to $N = 16$."

| Size of $\Delta$ proj. | Params (M) | Perplexity |
|---|---|---|
| - | 358.9 | 9.12 |
| 1 | 359.1 | 8.97 |
| 2 | 359.3 | 8.97 |
| 4 | 359.7 | 8.91 |
| 8 | 360.5 | 8.83 |
| 16 | 362.1 | 8.84 |
| 32 | 365.2 | 8.80 |
| 64 | 371.5 | 8.71 |

**Table 10** (p. 17): "(**Ablations: SSM state dimension.**) (*Top*) Constant $\boldsymbol{B}$ and $\boldsymbol{C}$. (*Bottom*) Selective $\boldsymbol{B}$ and $\boldsymbol{C}$. Increasing the SSM state dimension $N$, which can be viewed as an expansion factor on the dimension of the recurrent state, can significantly improve performance for a negligible cost in parameters/FLOPs, but only when $\boldsymbol{B}$ and $\boldsymbol{C}$ are also selective. Size of $\Delta$ projection fixed to 64."

*Constant $\boldsymbol{B}$ and $\boldsymbol{C}$:*

| State dimension $N$ | Params (M) | Perplexity |
|---|---|---|
| 1 | 367.1 | 9.88 |
| 2 | 367.4 | 9.86 |
| 4 | 368.0 | 9.82 |
| 8 | 369.1 | 9.82 |
| 16 | 371.5 | 9.81 |

*Selective $\boldsymbol{B}$ and $\boldsymbol{C}$:*

| State dimension $N$ | Params (M) | Perplexity |
|---|---|---|
| 1 | 367.1 | 9.73 |
| 2 | 367.4 | 9.40 |
| 4 | 368.0 | 9.09 |
| 8 | 369.1 | 8.84 |
| 16 | 371.5 | 8.71 |
