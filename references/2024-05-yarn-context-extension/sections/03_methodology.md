# 3 Methodology [p. 4-6]

Whereas PI stretches all RoPE dimensions equally, the authors find that the theoretical interpolation bound described by PI [9] is insufficient at predicting the complex dynamics between RoPE and the LLM's internal embeddings. The following subsections describe the main issues with PI that have been individually identified and solved, giving readers the context, origin and justifications of each method which are used in concert to obtain the full YaRN method. [p. 4]

## 3.1 Loss of High Frequency information - "NTK-aware" interpolation [p. 4-5]

If we look at RoPE only from an information encoding perspective, it was shown in [36], using Neural Tangent Kernel (NTK) theory, that deep neural networks have trouble learning high frequency information if the input dimension is low and the corresponding embeddings lack high frequency components. The similarities: a token's positional information is one-dimensional, and RoPE expands it to an n-dimensional complex vector embedding. [p. 4-5]

RoPE closely resembles Fourier Features [36], as it is possible to define RoPE as a special 1D case of a Fourier Feature. Stretching the RoPE embeddings indiscriminately results in the loss of important high frequency details which the network needs in order to resolve tokens that are both very similar and very close together (the rotation describing the smallest distance needs to not be too small for the network to be able to detect it). [p. 5]

The authors hypothesise that the slight increase of perplexity for short context sizes after fine-tuning on larger context sizes seen in PI [9] might be related to this problem. Under ideal circumstances, there is no reason that fine-tuning on larger context sizes should degrade the performance of smaller context sizes. [p. 5]

In order to resolve the problem of losing high frequency information when interpolating the RoPE embeddings, the "NTK-aware" interpolation was developed in [6]. Instead of scaling every dimension of RoPE equally by a factor $s$, the interpolation pressure is spread across multiple dimensions by scaling high frequencies less and low frequencies more. One can obtain such a transformation in many ways, but the simplest would be to perform a base change on the value of $\theta$. [p. 5]

**Definition 1** *The "NTK-aware" interpolation is a modification of RoPE by using Eq. 12 with the following functions.* [p. 5]

$$g(m) = m \tag{14}$$

$$h(\theta_d) = b'^{-2d/|D|}, \tag{15}$$

*where*

$$b' = b \cdot s^{\frac{|D|}{|D|-2}}. \tag{16}$$

Equations (14)-(16): NTK-aware interpolation definition. Position function $g(m)$ is identity (no position scaling). Frequency function $h(\theta_d)$ changes the base from $b$ to $b'$, effectively spreading interpolation pressure across dimensions -- high frequencies are scaled less, low frequencies more.

Given the results from [6], this method performs much better at extending the context size of non-fine-tuned models compared to PI [9]. However, one major disadvantage is that given it is not just an interpolation scheme, some dimensions are slightly extrapolated to "out-of-bound" values, thus fine-tuning with "NTK-aware" interpolation [6] yields inferior results to PI [9]. Furthermore, due to the "out-of-bound" values, the theoretical scale factor $s$ does not accurately describe the true context extension scale. In practice, the scale value $s$ has to be set higher than the expected scale for a given context length extension. [p. 5]

The authors note that shortly before the release of this article, Code Llama [31] was released and uses "NTK-aware" scaling by manually scaling the base $b$ to 1M. [p. 5]

## 3.2 Loss of Relative Local Distances - "NTK-by-parts" interpolation [p. 5-6]

In the case of blind interpolation methods like PI and "NTK-aware" interpolation, all RoPE hidden dimensions are treated equally (as in they have the same effect on the network). However, there are strong clues pointing towards the need for targeted interpolation methods. [p. 5]

The authors think heavily in terms of the wavelengths $\lambda_d$ defined in Eq. 13. For simplicity, the subscript $d$ in $\lambda_d$ is omitted and the reader is encouraged to think about $\lambda$ as the wavelength of an arbitrary periodic function. [p. 5]

One interesting observation of RoPE embeddings is that given a context size $L$, there are some dimensions $d$ where the wavelength is longer than the maximum context length seen during pretraining ($\lambda > L$), suggesting that some dimensions' embeddings might not be distributed evenly in the rotational domain. In such cases, the authors presume having all unique position pairs implies that the absolute positional information remains intact. On the contrary, when the wavelength is short, only relative positional information is accessible to the network. [p. 5]

Moreover, when stretching all the RoPE dimensions either by a scale $s$ or using a base change $b'$, all tokens become closer to each other, as the dot product of two vectors rotated by a lesser amount is bigger. This scaling severely impairs a LLM's ability to understand small and local relationships between its internal embeddings. The authors hypothesize that such compression leads to the model being confused on the positional order of close-by tokens, and consequently harming the model's abilities. [p. 5]

In order to remedy this issue, given the two previous observations, the authors choose not to interpolate the higher frequency dimensions at all while always interpolating the lower frequency dimensions. In particular: [p. 6]

- if the wavelength $\lambda$ is much smaller than the context size $L$, we do not interpolate;
- if the wavelength $\lambda$ is equal to or bigger than the context size $L$, we want to only interpolate and avoid any extrapolation (unlike the previous "NTK-aware" method);
- dimensions in-between can have a bit of both, similar to the "NTK-aware" interpolation.

The ratio $r = \frac{L}{\lambda}$ between the original context size $L$ and the wavelength $\lambda$ is introduced. In the $d$-th hidden state, the ratio $r$ depends on $d$ as follows: [p. 6]

$$r(d) = \frac{L}{\lambda_d} = \frac{L}{2\pi b'^{\frac{2d}{|D|}}}. \tag{17}$$

Equation (17): Ratio of context length to wavelength at dimension $d$, used to determine the interpolation strategy per dimension.

Two extra parameters $\alpha, \beta$ are introduced to define the boundary of the different interpolation strategies. All hidden dimensions $d$ where $r(d) < \alpha$ are those where we linearly interpolate by a scale $s$ (exactly like PI, avoiding any extrapolation), and the $d$ where $r(d) > \beta$ are those where we do not interpolate at all. The ramp function $\gamma$ is defined as: [p. 6]

$$\gamma(r) = \begin{cases} 0, & \text{if } r < \alpha \\ 1, & \text{if } r > \beta \\ \frac{r - \alpha}{\beta - \alpha}, & \text{otherwise.} \end{cases} \tag{18}$$

Equation (18): Ramp function $\gamma$ that smoothly transitions between full interpolation ($\gamma = 0$) and no interpolation ($\gamma = 1$).

**Definition 2** *The "NTK-by-parts" interpolation is a modification of RoPE by using Eq. 12 with the following functions:*$^4$ [p. 6]

$$g(m) = m \tag{19}$$

$$h(\theta_d) = \left(1 - \gamma\big(r(d)\big)\right) \frac{\theta_d}{s} + \gamma\big(r(d)\big) \theta_d. \tag{20}$$

Equations (19)-(20): NTK-by-parts interpolation. Position function is identity. Frequency function blends between full PI-style interpolation ($\theta_d / s$) for low-frequency dimensions and no interpolation ($\theta_d$) for high-frequency dimensions, controlled by the ramp $\gamma$.

The values of $\alpha$ and $\beta$ should be tuned on a case-by-case basis. For the Llama family of models, experimentally good values are $\alpha = 1$ and $\beta = 32$. [p. 6]

A variant of this method was released under the name "NTK-by-parts" interpolation [7]. This improved method performs better than the previous PI [9] and "NTK-aware" (Section 3.1) interpolation methods, both with non-fine-tuned models and with fine-tuned models, as shown in [7]. [p. 6]

Footnote 4: The interpolation by linear ramp on $h$ may have alternatives, such as a harmonic mean over $\theta_d/s$ and $\theta_d$ converted from a linear interpolation on wavelengths. The choice of $h$ here was for the simplicity of implementation, but both would work. [p. 6]

## 3.3 Dynamic Scaling - "Dynamic NTK" interpolation [p. 6]

In a lot of use cases, multiple forward-passes are performed with varying sequence lengths from 1 to the maximal context size. A typical example is the autoregressive generation where the sequence lengths increment by 1 after each step. There are two ways of applying an interpolation method that uses a scale factor $s$ (including PI, "NTK-aware" and "NTK-by-parts"): [p. 6]

1. Throughout the whole inference cycle, the embedding layer is fixed including the scale factor $s = L'/L$ where $L'$ is the fixed number of extended context size.
2. In each forward-pass, the position embedding updates the scale factor $s = \max(1, l'/L)$ where $l'$ is the sequence length of the current sequence.

The problem of (1) is that the model may experience a performance discount at a length less than $L$ and an abrupt degradation when the sequence length is longer than $L'$.

---
[p. 6-7 continued]

But by doing Dynamic Scaling as (2), it allows the model to gracefully degrade instead of immediately breaking when hitting the trained context limit $L'$. The authors call this inference-time method the Dynamic Scaling method. When it is combined with "NTK-aware" interpolation, they call it "Dynamic NTK" interpolation. It first appeared in public as a reddit post in [14]. [p. 7]

One notable fact is that the "Dynamic NTK" interpolation works exceptionally well on models pre-trained on $L$ without any finetuning ($L' = L$). This is supported by the experiment in Appendix B.3. [p. 7]

Often in the repeated forward-passes, the kv-caching [8] is applied so that we can reuse the previous key-value vectors and improve the overall efficiency. The authors point out that in some implementations when the RoPE embeddings are cached, some care has to be taken in order to modify it for Dynamic Scaling with kv-caching. The correct implementation should cache the kv-embeddings before applying RoPE, as the RoPE embedding of every token changes when $s$ changes. [p. 7]

## 3.4 YaRN [p. 7]

In addition to the previous interpolation techniques, the authors also observe that introducing a temperature $t$ on the logits before the attention softmax has a uniform impact on perplexity regardless of the data sample and the token position over the extended context window (See Appendix A.2). More precisely, instead of Eq. 2, the computation of attention weights is modified into: [p. 7]

$$\text{softmax}\left(\frac{\mathbf{q}_m^T \mathbf{k}_n}{t\sqrt{|D|}}\right). \tag{21}$$

Equation (21): Modified attention weight computation with temperature $t$ scaling the denominator, uniformly reducing attention logit magnitudes.

The reparametrization of RoPE as a set of 2D matrices has a clear benefit on the implementation of this attention scaling: we can instead use a "length scaling" trick which scales both $\mathbf{q}_m$ and $\mathbf{k}_n$ by a constant factor $\sqrt{1/t}$ by simply scaling the complex RoPE embeddings by the same amount. With this, YaRN can effectively alter the attention mechanism without modifying its code. Furthermore, it has zero overhead during both inference and training, as RoPE embeddings are generated in advance and are reused for all forward passes. Combining it with the "NTK-by-parts" interpolation, we have the YaRN method. [p. 7]

**Definition 3** *By the "YaRN method", we refer to a combination of the attention scaling in Eq. 21 and the "NTK-by-parts" interpolation introduced in Section 3.2.* [p. 7]

For LLaMA and Llama 2 models, the recommended values are: [p. 7]

$$\sqrt{\frac{1}{t}} = 0.1 \ln(s) + 1. \tag{22}$$

Equation (22): Empirical formula for the length scaling factor $\sqrt{1/t}$ as a function of the scale factor $s$. Found by fitting $\sqrt{1/t}$ at the lowest perplexity against the scale extension by various factors $s$ using the "NTK-by-parts" method on LLaMA 7b, 13b, 33b and 65b models without fine-tuning.

The authors note that the same values of $t$ also apply fairly well to Llama 2 models (7b, 13b and 70b). This suggests that the property of increased entropy and the temperature constant $t$ may have certain degree of "universality" and may be generalizable across some models and training data. [p. 7]

The YaRN method combines all their findings and surpasses all previous methods in both fine-tuned and non-fine-tuned scenarios. Thanks to its low footprint, YaRN allows for direct compatibility with libraries that modify the attention mechanism such as Flash Attention 2 [13]. [p. 7]
