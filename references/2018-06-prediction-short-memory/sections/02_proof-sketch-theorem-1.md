# 2 Proof Sketch of Theorem 1 [p. 8-10]

[p. 8] The authors provide a sketch of the proof of Theorem 1, which gives stronger guarantees than Proposition 1 but only applies to sequences generated from an HMM. The core of the proof is a lemma guaranteeing that the Markov model that knows the true marginal probabilities of all short sequences will end up predicting well. Additionally, the bound on the expected prediction error will hold in expectation over *only* the randomness of the HMM during the short window, and with high probability over the randomness of when the window begins (the more general results hold in expectation over the randomness of when the window begins).

For settings such as financial forecasting, this additional guarantee is particularly pertinent: one does not need to worry about the possibility of choosing an "unlucky" time to begin a trading regime, as long as one plans to trade for a duration that spans an entire short window. Beyond the extra strength of this result for HMMs, the proof approach is intuitive and pleasing, in comparison to the more direct information-theoretic proof of Proposition 1.

## Lemma 1

[p. 8] **Lemma 1.** *Consider an HMM with $n$ hidden states, let the hidden state at time $s = 0$ be chosen according to an arbitrary distribution $\pi$, and denote the observation at time $s$ by $x_s$. Let $OPT_s$ denote the conditional distribution of $x_s$ given observations $x_0, \ldots, x_{s-1}$, and knowledge of the hidden state at time $s = 0$. Let $M_s$ denote the conditional distribution of $x_s$ given only $x_0, \ldots, x_{s-1}$, which corresponds to the naive $s$-th order Markov model that knows only the joint probabilities of sequences of the first $s$ observations. Then with probability at least $1 - 1/n^{c-1}$ over the choice of initial state, for $\ell = c \log n / \epsilon^2$, $c \geq 1$ and $\epsilon \geq 1/\log^{0.25} n$,*

$$\mathbb{E}\Big[\sum_{s=0}^{\ell-1} \|OPT_s - M_s\|_1\Big] \leq 4\epsilon\ell,$$

*where the expectation is with respect to the randomness in the outputs $x_0, \ldots, x_{\ell-1}$.*

## Proof sketch of Lemma 1

[p. 8] The proof hinges on establishing a connection between $OPT_s$ -- the Bayes optimal model that knows the HMM and the initial hidden state $h_0$, and at time $s$ predicts the true distribution of $x_s$ given $h_0, x_0, \ldots, x_{s-1}$ -- and the naive order $s$ Markov model $M_s$ that knows the joint probabilities of sequences of $s$ observations (given that the initial state is drawn according to $\pi$) and predicts accordingly. This latter model is precisely the same as the model that knows the HMM and distribution $\pi$ (but not $h_0$), and outputs the conditional distribution of $x_s$ given the observations.

[p. 8] The two models are related via a martingale argument that leverages the intuition that, at each time step either $OPT_s \approx M_s$, or, if they differ significantly, the $s$-th observation $x_s$ is expected to contain a significant amount of information about the hidden state at time zero, $h_0$, which will then improve $M_{s+1}$. The submartingale precisely captures the sense that for any $s$ where there is significant deviation between $OPT_s$ and $M_s$, the probability of the initial state being $h_0$ conditioned on $x_0, \ldots, x_s$ is expected to be significantly more than the probability of $h_0$ conditioned on $x_0, \ldots, x_{s-1}$.

### Submartingale construction

[p. 8] Let $H_0^s$ denote the distribution of the hidden state at time 0 conditioned on $x_0, \ldots, x_s$, and let $h_0$ denote the true hidden state at time 0. Let $H_0^s(h_0)$ be the probability of $h_0$ under the distribution $H_0^s$. The following expression is shown to be a submartingale:

$$\log\left(\frac{H_0^s(h_0)}{1 - H_0^s(h_0)}\right) - \frac{1}{2}\sum_{i=0}^{s} \|OPT_i - M_i\|_1^2.$$

[p. 9] The submartingale property follows from defining $R_s$ as the conditional distribution of $x_s$ given observations $x_0, \ldots, x_{s-1}$ and initial state drawn according to $\pi$ but *not* being at hidden state $h_0$ at time 0. Note that $M_s$ is a convex combination of $OPT_s$ and $R_s$, hence $\|OPT_s - M_s\|_1 \leq \|OPT_s - R_s\|_1$. By Bayes Rule, the change in the LHS at any time step $s$ is the log of the ratio of the probability of observing the output $x_s$ according to the distribution $OPT_s$ and the probability of $x_s$ according to the distribution $R_s$. The expectation of this is the KL-divergence between $OPT_s$ and $R_s$, which can be related to the $\ell_1$ error using Pinsker's inequality.

### Concentration argument

[p. 9] At a high level, the proof then proceeds via concentration bounds (Azuma's inequality), to show that, with high probability, if the error from the first $\ell = c \log n / \epsilon^2$ timesteps is large, then $\log\left(\frac{H_0^{\ell-1}(h_0)}{1 - H_0^{\ell-1}(h_0)}\right)$ is also likely to be large, in which case the posterior distribution of the hidden state, $H_0^{\ell-1}$, will be sharply peaked at the true hidden state, $h_0$, unless $h_0$ had negligible mass (less than $n^{-c}$) in distribution $\pi$.

Several slight complications arise because the submartingale does not necessarily have nicely concentrated or bounded differences, as the first term in the submartingale could change arbitrarily. This is addressed by noting that the first term should not decrease too much except with tiny probability, as this corresponds to the posterior probability of the true hidden state sharply dropping. For the other direction, the deviations are "clipped" to prevent them from exceeding $\log n$ in any timestep, and the submartingale property continues to hold despite this clipping by proving a modified version of Pinsker's inequality.

## Lemma 2 (Modified Pinsker's inequality)

[p. 9] **Lemma 2.** *(Modified Pinsker's inequality) For any two distributions $\mu(x)$ and $\nu(x)$ defined on $x \in X$, define the $C$-truncated KL divergence as $\tilde{D}_C(\mu \| \nu) = \mathbb{E}_\mu\left[\log\left(\min\left\{\frac{\mu(x)}{\nu(x)}, C\right\}\right)\right]$ for some fixed $C$ such that $\log C \geq 8$. Then $\tilde{D}_C(\mu \| \nu) \geq \frac{1}{2}\|\mu - \nu\|_1^2$.*

## From Lemma 1 to Theorem 1

[p. 9] Given Lemma 1, the proof of Theorem 1 follows relatively easily. Recall that Theorem 1 concerns the expected prediction error at a timestep $t \leftarrow \{0, 1, \ldots, d^{c\ell}\}$, based on the model $M_{emp}$ corresponding to the empirical distribution of length $\ell$ windows that have occurred in $x_0, \ldots, x_t$. The connection between the lemma and theorem is established by showing that, with high probability, $M_{emp}$ is close to $M_{\hat{\pi}}$, where $\hat{\pi}$ denotes the empirical distribution of (unobserved) hidden states $h_0, \ldots, h_t$, and $M_{\hat{\pi}}$ is the distribution corresponding to drawing the hidden state $h_0 \leftarrow \hat{\pi}$ and then generating $x_0, x_1, \ldots, x_\ell$. The full proof is provided in Appendix A.
