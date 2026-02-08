# B Theoretical Analysis of Positional Encodings [p. 17–21]

## RoPE Formulation [p. 17]

[p. 17] RoPE maps an argument vector $x \in \mathbb{R}^d$ into the embedding curve on a sphere in $\mathbb{C}^{d/2}$ parametrized by a real parameter $t \in \mathbb{R}$ and "base frequency" $b$:

$$f^{RoPE}(x, t)_j = (x_{2j} + ix_{2j+1}) \, e^{ib^{-\frac{2j}{d}}t}.$$

The purpose of this mapping is to help the attention module to separate the vectors corresponding to two instances of the same token that are situated at different positions in the input sequence.

## Problem Formulation [p. 18]

[p. 18] Aiming at extending the sequence length of a transformer pretrained with a particular positional embedding $f$ from $L$ to $\hat{L}$, the goal is to come up with a positional embedding $\hat{f}$ that minimizes the distance between the old and the new images of the embedded vectors:

$$d(f, \hat{f}) = \max_{x \in \mathcal{X}} \min_{\substack{k \in \{0,..N-1\} \\ j \in \{0,..\hat{N}-1\}}} \text{dist}[f(x,k), \hat{f}(x,j)],$$

where $\mathcal{X} \subset \mathbb{R}^d$ is the set of vectors that would need to be positionally embedded. Chen et al. (2023) computed this distance through the magnitude of the attention scores, but still argued for the efficiency of their method "position interpolation" due to its reduced value of the distance to the original RoPE images when compared to the naive extrapolation of the positional embedding.

## PI and ABF Embedding Curves [p. 18]

[p. 18] Two different methods are considered to extend the sequence length of a trained transformer: Position Interpolation (PI) parameterized with $\alpha$, and Adjusted Base Frequency (ABF) parameterized with $\beta$. These two methods correspond to the following embedding curves:

$$f^{RoPE+PI}(x, t)_j = (x_{2j} + ix_{2j+1}) \, e^{i\alpha \cdot (b^{-\frac{2j}{d}})t}$$

$$f^{RoPE+ABF}(x, t)_j = (x_{2j} + ix_{2j+1}) \, e^{i(\beta b)^{-\frac{2j}{d}}t}$$

## Embedding Granularity Metric [p. 18]

[p. 18] Evaluating a positional embedding a-priori, one should consider the degree of granularity with which the embedding images are being distributed over the embedding space. Comparing alternative positional embeddings $\hat{f}$ mapping $\mathbb{R}^d \times \mathbb{N}$ into $\mathbb{C}^{d/2}$, one should prefer the one with the maximal value of the distance between the two closest images:

$$q(\hat{f}) = \min_{\substack{x \in \mathcal{X}: k \neq j \in \{0..\hat{N}-1\}}} \text{dist}[\hat{f}(x,k), \hat{f}(x,j)].$$

## Multi-Objective Decision [p. 19]

[p. 19] This leaves a multi-objective decision selecting the positional embedding for a model with extended context: on one hand, $\hat{f}$ should be chosen so that it minimizes $d(f, \hat{f})$, while on the other hand its value of $q(\hat{f})$ should be big enough.

## Geometric Intuition [p. 19]

[p. 19] To provide a geometric intuition for the positional embeddings considered, while it is difficult to visualize a mapping $\mathbb{R}^d \times \mathbb{N} \to \mathbb{C}^{d/2}$, one can consider $x \in \mathbb{R}^d$ to be fixed and visualize the projection $\mathbb{R} \to \mathbb{R}^3$. To get the intuition behind PI and ABF, the helix formed by $\text{Re}[f^{RoPE}(x,t)_0]$, $\text{Im}[f^{RoPE}(x,t)_0]$ and $\text{Re}[f^{RoPE}(x,t)_j]$ is considered. The example on Figure 8a depicts a black helix line given with the system:

$$x = \cos t; \quad y = \sin t; \quad z = \sin at.$$

The red dots on the line correspond to 11 integer values of $t$.

**Figure 8** (p. 19): "RoPE variants visualization as helices."

Three 3D helix plots side by side:
- **(a) RoPE**: A helix with widely spaced red dots (integer positions) and moderate frequency oscillation in the z-axis. The helix has relatively large spacing between consecutive points.
- **(b) RoPE+PI**: A helix where the red dots are much closer together compared to (a). The distance between consecutive points is reduced considerably, illustrating how Position Interpolation compresses the positional embeddings into a smaller range.
- **(c) RoPE+ABF**: A helix that looks almost the same as (a) in terms of the distance between consecutive points, but with increased frequency of the helix (more oscillations). The minimal distance between points is considerably reduced due to the increased helix frequency, though the consecutive-point spacing remains similar to (a).

[p. 19] Figure 8b illustrates the impact of Position Interpolation on the relative position of the mapped vectors. The distance between the consecutive points got reduced considerably compared to Figure 8a. The impact of Adjusted Base Frequency is illustrated on Figure 8c. The distance between the consecutive points remained almost the same as on Figure 8a, although the minimal distance between points got considerably reduced due to the increased frequency of the helix. This effect of increased frequency of the helix would be reduced in the high dimension setting. The value of the coefficient $a$ for the helix depicted on Figure 8a is two times larger than the value of the coefficient $a$ for the helix depicted on Figure 8c. If the dimension of the input of the attention mechanism is $d = 128$, then the difference between $\theta_1 = b^{-\frac{2}{d}}$ at $b = 10{,}000$ and $\theta_1 = b^{-\frac{2}{d}}$ at $b = 500{,}000$ is only 6%. Thus, the authors further focus specifically on the distance between the consecutive images of the embeddings.

## Sine Similarity Metric [p. 19]

[p. 19] A formal comparison between Positional Interpolation and Adjusted Base Frequency is made by analytically comparing the pairwise distances between the images given by $f^{RoPE+PI}$ and $f^{RoPE+ABF}$ for consecutive integer values of $t$. This corresponds to the evaluation of $q(\hat{f})$ discussed earlier. The distance between embedding images is measured in terms of the Euclidean sine similarity metric since all versions of RoPE are norm-preserving:

$$\sin \angle(a, b) = \frac{Im\langle a, b \rangle}{\|a\| \|b\|}$$

[p. 19] The following result states that in a high-dimensional space, the sine similarity $\sin \angle(f^{RoPE+ABF}(x, n+1), f^{RoPE+ABF}(x, n))$ between two consecutive embedding images of a vector $x$ can be bounded with a value proportional to $(\log b + \log \beta)^{-1}$. Moreover, the similarity $\sin \angle(f^{RoPE+PI}(x, n+1), f^{RoPE+PI}(x, n))$ can be bounded using $\alpha(\log b)^{-1}$.

## Theorem 1 [p. 19–20]

**Theorem 1.** For $x \in \mathbb{R}^d$ and $n \in \mathbb{N}$, the Euclidean sine similarity between the two consecutive images of a positional embedding can be bounded as

$$\frac{\min_k x_k^2}{\|x\|^2} C_d \le \sin \angle(f(x, n+1), f(x, n)) \le \frac{\max_k x_k^2}{\|x\|^2} C_d$$

where $\lim_{d \to \infty} C_d \approx \begin{cases} (\log b + \log \beta)^{-1} & \text{if } f = f^{RoPE+ABF} \\ \alpha(\log b)^{-1} & \text{if } f = f^{RoPE+PI} \end{cases}$ under the assumptions of $\alpha \ll 1$ and $b \gg 1$.

## Proof [p. 20]

[p. 20] *Proof.* The proof begins by writing down the expressions for the inner product between two images of RoPE variants:

$$\langle f^{RoPE+PI}(x, m), f^{RoPE+PI}(x, n) \rangle = \sum_{j=0}^{\frac{d}{2}-1} (x_{2j}^2 + x_{2j+1}^2) \, e^{ib^{-\frac{2j}{d}} \alpha(m-n)}$$

$$\langle f^{RoPE+ABF}(x, m), f^{RoPE+ABF}(x, n) \rangle = \sum_{j=0}^{\frac{d}{2}-1} (x_{2j}^2 + x_{2j+1}^2) \, e^{ib^{-\frac{2j}{d}} \beta^{-\frac{2j}{d}} (m-n)}$$

From them, the expressions for the Euclidean sine similarity between the images of the positional embeddings are derived:

$$\sin \angle(f^{RoPE+PI}(x, m), f^{RoPE+PI}(x, n)) = \frac{\sum_{j=0}^{\frac{d}{2}-1} (x_{2j}^2 + x_{2j+1}^2) \sin(b^{-\frac{2j}{d}} \alpha(m-n))}{\sum_{j=0}^{d-1} x_j^2}$$

$$\sin \angle(f^{RoPE+ABF}(x, m), f^{RoPE+ABF}(x, n)) = \frac{\sum_{j=0}^{\frac{d}{2}-1} (x_{2j}^2 + x_{2j+1}^2) \sin(b^{-\frac{2j}{d}} \beta^{-\frac{2j}{d}} (m-n))}{\sum_{j=0}^{d-1} x_j^2}$$

[p. 20] Setting $m = n + 1$ to compare the distance between two consecutive positional embedding images of the same vector $x$:

$$\|x\|^2 \sin \angle(f^{RoPE+PI}(x, n+1), f^{RoPE+PI}(x, n)) = \sum_{j=0}^{\frac{d}{2}-1} (x_{2j}^2 + x_{2j+1}^2) \sin(b^{-\frac{2j}{d}} \alpha)$$

$$\|x\|^2 \sin \angle(f^{RoPE+ABF}(x, n+1), f^{RoPE+ABF}(x, n)) = \sum_{j=0}^{\frac{d}{2}-1} (x_{2j}^2 + x_{2j+1}^2) \sin(b^{-\frac{2j}{d}} \beta^{-\frac{2j}{d}})$$

[p. 20] Due to the range of $b$, $\alpha$ and $\beta$ that is typically considered, the arguments of the sine functions are bounded as $0 < \alpha b^{-\frac{2j}{d}} \le 1$ as well as $0 < (\beta b)^{-\frac{2j}{d}} \le 1$. Using that $\sin(b^{-\frac{2j}{d}} \beta^{-\frac{2j}{d}})$ and $\sin(b^{-\frac{2j}{d}} \alpha)$ are non-negative as well as $x_j^2$ for any $j \in \{1, \ldots d\}$, the following inequalities hold:

$$\sum_{j=0}^{\frac{d}{2}-1} \min_k x_k^2 \sin(b^{-\frac{2j}{d}} \beta^{-\frac{2j}{d}}) \le \sum_{j=0}^{\frac{d}{2}-1} (x_{2j}^2 + x_{2j+1}^2) \sin(b^{-\frac{2j}{d}} \beta^{-\frac{2j}{d}}) \le \sum_{j=0}^{\frac{d}{2}-1} \max_k x_k^2 \sin(b^{-\frac{2j}{d}} \beta^{-\frac{2j}{d}}),$$

$$\sum_{j=0}^{\frac{d}{2}-1} \min_k x_k^2 \sin(b^{-\frac{2j}{d}} \alpha) \le \sum_{j=0}^{\frac{d}{2}-1} (x_{2j}^2 + x_{2j+1}^2) \sin(b^{-\frac{2j}{d}} \alpha) \le \sum_{j=0}^{\frac{d}{2}-1} \max_k x_k^2 \sin(b^{-\frac{2j}{d}} \alpha).$$

[p. 20] Carrying $\min_k x_k^2$ and $\max_k x_k^2$ out of the summation signs, the result is obtained:

$$\min_k x_k^2 \sum_{j=0}^{\frac{d}{2}-1} \sin(b^{-\frac{2j}{d}} \beta^{-\frac{2j}{d}}) \le \sum_{j=0}^{\frac{d}{2}-1} (x_{2j}^2 + x_{2j+1}^2) \sin(b^{-\frac{2j}{d}} \beta^{-\frac{2j}{d}}) \le \max_k x_k^2 \sum_{j=0}^{\frac{d}{2}-1} \sin(b^{-\frac{2j}{d}} \beta^{-\frac{2j}{d}}),$$

$$\min_k x_k^2 \sum_{j=0}^{\frac{d}{2}-1} \sin(b^{-\frac{2j}{d}} \alpha) \le \sum_{j=0}^{\frac{d}{2}-1} (x_{2j}^2 + x_{2j+1}^2) \sin(b^{-\frac{2j}{d}} \alpha) \le \max_k x_k^2 \sum_{j=0}^{\frac{d}{2}-1} \sin(b^{-\frac{2j}{d}} \alpha).$$

[p. 20] Introducing $C_d^{ABF} = \sum_{j=0}^{\frac{d}{2}-1} \sin(b^{-\frac{2j}{d}} \beta^{-\frac{2j}{d}})$ and $C_d^{PI} = \sum_{j=0}^{\frac{d}{2}-1} \sin(b^{-\frac{2j}{d}} \alpha)$ proves the first part of the Theorem:

$$\frac{\min_k x_k^2}{\|x\|^2} C_d^{ABF} \le \sin \angle(f^{RoPE+ABF}(x, n+1), f^{RoPE+ABF}(x, n)) \le \frac{\max_k x_k^2}{\|x\|^2} C_d^{ABF},$$

$$\frac{\min_k x_k^2}{\|x\|^2} C_d^{PI} \le \sin \angle(f^{RoPE+PI}(x, n+1), f^{RoPE+PI}(x, n)) \le \frac{\max_k x_k^2}{\|x\|^2} C_d^{PI},$$

## Asymptotic Bounds on $C_d$ [p. 21]

[p. 21] Considering the limit of $C_d$, due to the inequalities on the arguments of the sines, the following bounds hold:

$$(b\beta)^{-\frac{2j}{d}} \left(1 - (b\beta)^{-\frac{2j}{d}}/\pi \right) \le \sin(b^{-\frac{2j}{d}} \beta^{-\frac{2j}{d}}) \le (b\beta)^{-\frac{2j}{d}},$$

$$\alpha b^{-\frac{2j}{d}} \left(1 - \alpha b^{-\frac{2j}{d}}/\pi \right) \le \sin(b^{-\frac{2j}{d}} \alpha) \le \alpha b^{-\frac{2j}{d}}$$

[p. 21] Using the formula of geometric sums and a corollary of the exponential (second) foundational limit, the limits of the sums of these bounds as $d \to \infty$ are established:

$$\sum_{j=0}^{\frac{d}{2}-1} \alpha b^{-\frac{2j}{d}} = \frac{\alpha(b-1)b^{2/d}}{b^{2/d+1} - b} \to \alpha \frac{b-1}{b \log b} \text{ as } d \to \infty$$

$$\sum_{j=0}^{\frac{d}{2}-1} \alpha^2 b^{-\frac{4j}{d}} = \frac{\alpha^2(b^2-1)b^{4/d}}{b^{4/d+2} - b^2} \to \alpha^2 \frac{b^2 - 1}{b^2 \log b} \text{ as } d \to \infty$$

$$\sum_{j=0}^{\frac{d}{2}-1} (b\beta)^{-\frac{2j}{d}} = \frac{(b\beta-1)(b\beta)^{2/d}}{(b\beta)^{2/d+1} - b\beta} \to \frac{(b\beta) - 1}{(b\beta) \log(b\beta)} \text{ as } d \to \infty$$

$$\sum_{j=0}^{\frac{d}{2}-1} (b\beta)^{-\frac{4j}{d}} = \frac{(b^2\beta^2 - 1)(b\beta)^{4/d}}{(b\beta)^{4/d+2} - b^2\beta^2} \to \frac{(b\beta)^2 - 1}{(b\beta)^2 \log(b\beta)} \text{ as } d \to \infty$$

[p. 21] Substituting these into the bounds on $\lim_{d \to \infty} C_d$, one achieves:

$$(\log b + \log \beta)^{-1} \left( \frac{(b\beta) - 1}{(b\beta)} - \frac{(b\beta)^2 - 1}{\pi(b\beta)^2} \right) \le \lim_{d \to \infty} C_d^{ABF} \le (\log b + \log \beta)^{-1} \frac{(b\beta) - 1}{(b\beta)},$$

$$\alpha(\log b)^{-1} \left( \frac{b - 1}{b} - \frac{\alpha}{\pi} \frac{b^2 - 1}{b^2} \right) \le \lim_{d \to \infty} C_d^{PI} \le \alpha(\log b)^{-1} \frac{b - 1}{b}$$

[p. 21] From these bounds, one can see that in the setting considered within this paper, where $b = 10000$ and $\alpha < 1/4$, the approximation of $\lim_{d \to \infty} C_d$ used in the statement of the Theorem is of a high quality. $\square$

## Interpretation of Experimental Results [p. 21]

[p. 21] Based on this theoretical derivation, the authors return to the interpretation of experimental results. On one hand, the experiments have shown that the model can adapt to the new sequence length with both RoPE PI ($\alpha = 1/4$ or $\alpha = 1/8$) and RoPE ABF ($\beta = 50$). Thus, the chosen hyperparameters provide a sufficient degree of approximation of RoPE images under $b = 10000$. In other words, both $d(f, f^{RoPE+ABF})$ and $d(f, f^{RoPE+PI})$ are small enough to allow rapid adaptation.

[p. 21] On the other hand, comparing the expressions of $C_d$ for RoPE ABF and RoPE PI, the granularity (the distance between two consecutive images of RoPE) is much lower for the RoPE PI ($\alpha(\log b)^{-1} \approx 0.027$) than for RoPE ABF (($\log b + \log \beta)^{-1} \approx 0.076$) with $\beta = 50$. The authors further hypothesise that the higher degree of granularity is related to the higher evaluation on the downstream tasks of the RoPE ABF variant compared to RoPE PI because it makes the task of distinguishing between the positional embedding images simpler for the model. In other words, this corresponds to the case of $q(f^{RoPE+ABF}) > q(f^{RoPE+PI})$.

[p. 21] Throughout this consideration, the authors implicitly assumed that the distance between the consecutive images of an embedding is smaller than the distance between any other pair of the images. While this assumption is likely to hold true in a high-dimensional space, significantly increasing the parameter of $\beta$ in RoPE ABF may violate this assumption due to the changed geometry of the embedding curve.
