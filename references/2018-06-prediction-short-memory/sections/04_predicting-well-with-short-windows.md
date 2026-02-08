# 4 Predicting Well with Short Windows [p. 11-13]

[p. 11] This section establishes the general proposition (Proposition 1) via an elementary and purely information-theoretic proof, which applies beyond the HMM setting.

## Proposition 1

**Proposition 1.** *For any data-generating distribution $\mathcal{M}$ with mutual information $I(\mathcal{M})$ between past and future observations, the best $\ell$-th order Markov model $\mathcal{P}_\ell$ obtains average KL-error, $\delta_{KL}(\mathcal{P}_\ell) \leq I(\mathcal{M})/\ell$ with respect to the optimal predictor with access to the infinite history. Also, any predictor $\mathcal{A}_\ell$ with $\hat{\delta}_{KL}(\mathcal{A}_\ell)$ average KL-error in estimating the joint probabilities over windows of length $\ell$ gets average error $\delta_{KL}(\mathcal{A}_\ell) \leq I(\mathcal{M})/\ell + \hat{\delta}_{KL}(\mathcal{A}_\ell)$.*

## Proof of Proposition 1

[p. 11] The expected error is bounded by splitting the time interval $0$ to $T - 1$ into blocks of length $\ell$. Consider any block starting at time $\tau$. The average error of the predictor from time $\tau$ to $\tau + \ell - 1$ is found, then averaged across all blocks.

The error is decomposed as the sum of:
1. The error due to not knowing the past history beyond the most recent $\ell$ observations, and
2. The error in estimating the true joint distribution of the data over a $\ell$-length block.

Consider any time $t$. Recall the definition of $\delta_{KL}^{(t)}(\mathcal{A}_\ell)$:

$$\delta_{KL}^{(t)}(\mathcal{A}_\ell) = \mathbb{E}_{x_{-\infty}^{t-1}} \left[ D_{KL}(Pr(x_t | x_{-\infty}^{t-1}) \| Q_{\mathcal{A}_\ell}(x_t | x_{t-\ell}^{t-1})) \right]$$

$$= \mathbb{E}_{x_{-\infty}^{t-1}} \left[ D_{KL}(Pr(x_t | x_{-\infty}^{t-1}) \| Pr(x_t | x_{t-\ell}^{t-1})) \right]$$

$$+ \mathbb{E}_{x_{-\infty}^{t-1}} \left[ D_{KL}(Pr(x_t | x_{t-\ell}^{t-1}) \| Q_{\mathcal{A}_\ell}(x_t | x_{t-\ell}^{t-1})) \right]$$

$$= \delta_{KL}^{(t)}(\mathcal{P}_\ell) + \hat{\delta}_{KL}^{(t)}(\mathcal{A}_\ell).$$

Therefore, $\delta_{KL}(\mathcal{A}_\ell) = \delta_{KL}(\mathcal{P}_\ell) + \hat{\delta}_{KL}(\mathcal{A}_\ell)$.

[p. 11-12] It is easy to verify that $\delta_{KL}^{(t)}(\mathcal{P}_\ell) = I(x_{-\infty}^{t-\ell-1}; x_t | x_{t-\ell}^{t-1})$. This relation formalizes the intuition that the current output $x_t$ has significant extra information about the past $(x_{-\infty}^{t-1})$ if we cannot predict it as well using the $\ell$ most recent observations $(x_{t-\ell}^{t-1})$ as can be done by using the entire past $(x_{-\infty}^{t-1})$.

### Upper bound via chain rule

[p. 12] The total error for the window $[\tau, \tau + \ell - 1]$ is upper bounded. Expand $I(x_{-\infty}^{\tau-1}; x_\tau^\infty)$ using the chain rule:

$$I(x_{-\infty}^{\tau-1}; x_\tau^\infty) = \sum_{t=\tau}^{\infty} I(x_{-\infty}^{\tau-1}; x_t | x_\tau^{t-1}) \geq \sum_{t=\tau}^{\tau+\ell-1} I(x_{-\infty}^{\tau-1}; x_t | x_\tau^{t-1}).$$

Note that $I(x_{-\infty}^{\tau-1}; x_t | x_\tau^{t-1}) \geq I(x_{-\infty}^{t-\ell-1}; x_t | x_{t-\ell}^{t-1}) = \delta_{KL}^{(t)}(\mathcal{P}_\ell)$ as $t - \ell \leq \tau$ and $I(X, Y; Z) \geq I(X; Z|Y)$.

The proposition then follows from averaging the error across the $\ell$ time steps and using Eq. 3.1 to average over all blocks of length $\ell$ in the window $[0, T-1]$:

$$\frac{1}{\ell} \sum_{t=\tau}^{\tau+\ell-1} \delta_{KL}^{(t)}(\mathcal{P}_\ell) \leq \frac{1}{\ell} I(x_{-\infty}^{\tau-1}; x_\tau^\infty) \implies \delta_{KL}(\mathcal{P}_\ell) \leq \frac{I(\mathcal{M})}{\ell}.$$

[p. 12] Note that Proposition 1 also directly gives guarantees for the scenario where the task is to predict the distribution of the next block of outputs instead of just the next immediate output, because KL-divergence obeys the chain rule.

## Corollary 2 (relating KL error to $\ell_1$ error)

[p. 12] The following easy corollary relates KL error to $\ell_1$ error. It also trivially applies to zero/one loss, as the expected relative zero/one loss at any time step is at most the $\ell_1$ loss at that time step.

**Corollary 2.** *For any data-generating distribution $\mathcal{M}$ with mutual information $I(\mathcal{M})$ between past and future observations, the best $\ell$-th order Markov model $\mathcal{P}_\ell$ obtains average $\ell_1$-error $\delta_{\ell_1}(\mathcal{P}_\ell) \leq \sqrt{I(\mathcal{M})/2\ell}$ with respect to the optimal predictor that has access to the infinite history. Also, any predictor $\mathcal{A}_\ell$ with $\hat{\delta}_{\ell_1}(\mathcal{A}_\ell)$ average $\ell_1$-error in estimating the joint probabilities gets average prediction error $\delta_{\ell_1}(\mathcal{A}_\ell) \leq \sqrt{I(\mathcal{M})/2\ell} + \hat{\delta}_{\ell_1}(\mathcal{A}_\ell)$.*

### Proof of Corollary 2

[p. 12-13] The error is again decomposed as the sum of the error in estimating $\hat{P}$ (due to not knowing the past) and the error due to the algorithm's estimation quality, using the triangle inequality:

$$\delta_{\ell_1}^{(t)}(\mathcal{A}_\ell) = \mathbb{E}_{x_{-\infty}^{t-1}} \left[ \|Pr(x_t | x_{-\infty}^{t-1}) - Q_{\mathcal{A}_\ell}(x_t | x_{t-\ell}^{t-1})\|_1 \right]$$

$$\leq \mathbb{E}_{x_{-\infty}^{t-1}} \left[ \|Pr(x_t | x_{-\infty}^{t-1}) - Pr(x_t | x_{t-\ell}^{t-1})\|_1 \right]$$

$$+ \mathbb{E}_{x_{-\infty}^{t-1}} \left[ \|Pr(x_t | x_{t-\ell}^{t-1}) - Q_{\mathcal{A}_\ell}(x_t | x_{t-\ell}^{t-1})\|_1 \right]$$

$$= \delta_{\ell_1}^{(t)}(\mathcal{P}_\ell) + \hat{\delta}_{\ell_1}^{(t)}(\mathcal{A}_\ell)$$

Therefore, $\delta_{\ell_1}(\mathcal{A}_\ell) \leq \delta_{\ell_1}(\mathcal{P}_\ell) + \hat{\delta}_{\ell_1}(\mathcal{A}_\ell)$.

[p. 13] By Pinsker's inequality and Jensen's inequality, $\delta_{\ell_1}^{(t)}(\mathcal{A}_\ell)^2 \leq \delta_{KL}^{(t)}(\mathcal{A}_\ell)/2$. Using Proposition 1:

$$\delta_{KL}(\mathcal{A}_\ell) = \frac{1}{T} \sum_{t=0}^{T-1} \delta_{KL}^{(t)}(\mathcal{A}_\ell) \leq \frac{I(\mathcal{M})}{\ell}$$

Therefore, using Jensen's inequality again, $\delta_{\ell_1}(\mathcal{A}_\ell) \leq \sqrt{I(\mathcal{M})/2\ell}$.
