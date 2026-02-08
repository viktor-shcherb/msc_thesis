# 2.3 Proposed Approach: Position Interpolation (PI) [p. 4-5]

[p. 4] In Fig. 2, thanks to the smoothness of bases functions $\phi_j$, interpolation is much more stable and will not lead to wild values. Therefore, instead of extrapolating the attention score in Eqn. 3 to $s > L$, the authors define an attention score $\tilde{a}(s) = a(Ls/L')$ where $L'$ is the longer context window.

Formally, they replace RoPE $\mathbf{f}$ by $\mathbf{f}'$ defined as follows:

$$\mathbf{f}'(\mathbf{x}, m) = \mathbf{f}\left(\mathbf{x}, \frac{mL}{L'}\right). \tag{4}$$

They call this transformation on the position encoding **Position Interpolation**. In this step, position indices are reduced from $[0, L')$ to $[0, L)$ to match the original range of indices before computing RoPE. Consequently, as inputs to RoPE, the maximum relative distance between any two tokens has been reduced from $L'$ to $L$. Since the ranges of position indices and relative distances before and after extension are aligned, the effect on attention score computation due to context window extensions is mitigated, which can allow the model easier to adapt. [p. 4]

## Theorem 2.1 (Interpolation bound)

[p. 5] **Theorem 2.1** (Interpolation bound). For attention score $a(s) = \mathrm{Re}\left[\sum_{j=0}^{d/2-1} h_j e^{\mathrm{i}s\theta_j}\right]$, where $\theta_j = c^{-2j/d}$, its interpolation value $a(s)$ for $s \in [s_1, s_2]$ is bounded as follows:

$$|a(s) - a_{\text{linear}}(s)| \leq d \left(\max_j |h_j|\right) \frac{(s - s_1)(s_2 - s)}{8 \ln c} \tag{5}$$

where $a_{\text{linear}}(s)$ is the linear interpolation of two grid point $a(s_1)$ and $a(s_2)$ that are known to behave well, enforced by LLM pre-training:

$$a_{\text{linear}}(s) := (1 - \lambda(s))a(s_1) + \lambda(s)a(s_2), \qquad \lambda(s) := \frac{s - s_1}{s_2 - s_1} \tag{6}$$

Please check Appendix A for the proof.

Intuitively, in LLM pre-training, the attention score $a(s)$ behaves well on integer grid $s_1$ and $s_2$. Therefore, for any interpolation $s \in [s_1, s_2]$, $(s - s_1)(s_2 - s) \leq 1/4$. Note that $c = 10000$, the bound becomes:

$$|a(s) - a_{\text{linear}}(s)| \leq \frac{d}{32 \ln c} \max_j |h_j| \approx \frac{d \max_j |h_j|}{294.73} \tag{7}$$

## Extrapolation bound (comparison)

[p. 5] In comparison, Sec. 3.4.3 in RoPE (Su et al., 2021) yields an extrapolation bound (i.e., it works for all positional distance $s$):

$$|a(s)| \leq \left(\max_j |h_j - h_{j+1}|\right) \sum_{k=0}^{d/2-1} |A_{k+1}(s)| \leq 2\left(\max_j |h_j|\right) \sum_{k=0}^{d/2-1} |A_{k+1}(s)|, \tag{8}$$

where $A_k(s) := \sum_{j=0}^{k-1} e^{\mathrm{i}s\theta_j}$. While there is no close form for $B(s) := \sum_{k=0}^{d/2-1} |A_{k+1}(s)|$, numerically it is at least larger than $d$, and for many positional difference $s$, $B(s)$ is much larger than $d$ (check Appendix B for the plot). Therefore, the interpolation bound is at least $2 \cdot 294.73 \sim 600\times$ smaller than the extrapolation bound, and thus the interpolated attention score is much more stable than extrapolated one. [p. 5]

## Practical advantages

[p. 5] The method of rescaling position indices does not introduce extra weight, or modify the model architecture in any way. This makes it attractive in practical applications, since most infrastructure and optimization for the original model can be reused after the extension.

## Fine-tuning

[p. 5] The interpolated model can be further fine-tuned using the next token prediction task with interpolated position encodings on the extended context window size using a pre-training corpus such as the Pile (Gao et al., 2020). The authors show that the fine-tuning process only needs tens to hundreds of thousands of examples. They also find that the result of the fine-tuning is not sensitive to the choice of examples. The reason may be that the model is only adapting to the new context window during the fine-tuning phase, starting from a good initialization, as opposed to acquiring new knowledge. [p. 5]

## Other ways to reduce interpolation/extrapolation bound

[p. 5] From the expression of the interpolation (Eqn. 5) and extrapolation bound (Eqn. 8), a common term is $\max_j |h_j|$, which is the maximal magnitude of query/key products. If a regularization on $|h_j|$ is enforced during LLM training, it is possible that the catastrophic extrapolation error can be mitigated or even resolved. In fact, if ridge regression with proper regularization is applied to fit a curve in Fig. 2, the magnitude of extrapolated $a(s)$ when $s > L$ can be comparable to that within $[0, L]$. The authors are not aware of existing LLM pre-training techniques that leverage this regularization and leave it for future work. [p. 5]
