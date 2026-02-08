# 7 Information Theoretic Lower Bounds [p. 17-18]

[p. 17] This section shows that *information theoretically*, windows of length $cI(\mathcal{M})/\epsilon^2$ are necessary to get expected relative zero-one loss less than $\epsilon$. As the expected relative zero-one loss is at most the $\ell_1$ loss, which can be bounded by the square of the KL-divergence, this automatically implies that the window length requirement is also tight for $\ell_1$ loss and KL loss.

For the KL loss, it is very easy to show tightness: choose the simple model which emits uniform random bits from time $0$ to $n - 1$ and repeats the bits from time $0$ to $m - 1$ for time $n$ through $n + m - 1$. One can then choose $n, m$ to get the desired error $\epsilon$ and mutual information $I(\mathcal{M})$.

To get a lower bound for the zero-one loss, the probabilistic method is used to argue that there exists an HMM such that long windows are required to perform optimally with respect to the zero-one loss for that HMM.

## Proposition 3

[p. 17] **Proposition 3.** *There is an absolute constant $c$ such that for all $0 < \epsilon < 1/4$ and sufficiently large $n$, there exists an HMM with $n$ states such that it is not information theoretically possible to get average relative zero-one loss or $\ell_1$ loss less than $\epsilon$ using windows of length smaller than $c \log n / \epsilon^2$, and KL loss less than $\epsilon$ using windows of length smaller than $c \log n / \epsilon$.*

## Proof sketch construction

[p. 17-18] The construction is illustrated in Fig. 2, and the high-level proof idea is given with respect to Fig. 2 below.

The goal is to show that no predictor $\mathcal{P}$ using windows of length $\ell = 3$ can make a good prediction. The transition matrix of the HMM is a permutation and the output alphabet is binary. Each state is assigned a label which determines its output distribution. The states labeled 0 emit 0 with probability $0.5 + \epsilon$ and the states labeled 1 emit 1 with probability $0.5 + \epsilon$.

The labels for the hidden states are chosen randomly and uniformly. Over the randomness in choosing the labels for the permutation, it is shown that the expected error of the predictor $\mathcal{P}$ is large, which means that there must exist some permutation such that the predictor $\mathcal{P}$ incurs a high error.

### Rough proof idea

[p. 17-18] Say the Markov model is at hidden state $h_2$ at time 2, this is unknown to the predictor $\mathcal{P}$. The outputs for the first three time steps are $(x_0, x_1, x_2)$. The predictor $\mathcal{P}$ only looks at the outputs from time 0 to 2 for making the prediction for time 3. It is shown that with high probability over the choice of labels to the hidden states and the outputs $(x_0, x_1, x_2)$, the output $(x_0, x_1, x_2)$ from the hidden states $(h_0, h_1, h_2)$ is close in Hamming distance to the label of some other segment of hidden states, say $(h_4, h_5, h_6)$. Hence any predictor using only the past 3 outputs cannot distinguish whether the string $(x_0, x_1, x_2)$ was emitted by $(h_0, h_1, h_2)$ or $(h_4, h_5, h_6)$, and hence cannot make a good prediction for time 3 (we actually need to show that there are many segments like $(h_4, h_5, h_6)$ whose label is close to $(x_0, x_1, x_2)$). The proof proceeds via simple concentration bounds.

## Figure 2

**Figure 2** (p. 18): `"Lower bound construction, n = 16."`

The figure shows a circular permutation HMM with 16 hidden states arranged in a ring. Each state has a binary label (0 or 1) and the hidden states cycle deterministically through the ring. Hidden states are labeled $h_0, h_1, \ldots, h_6$ (visible portion), with outputs shown as 0 or 1 in circles. The structure illustrates how the predictor cannot distinguish which segment of the ring it is currently observing based only on a short window of outputs.
