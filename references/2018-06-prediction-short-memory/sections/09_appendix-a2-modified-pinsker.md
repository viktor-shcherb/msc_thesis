# A.2 Proof of Modified Pinsker's Inequality (Lemma 6) [p. 22–23]

[p. 22] **Lemma 6** (restated). *(Modified Pinsker's inequality)* For any two distributions $\mu(x)$ and $\nu(x)$ defined on $x \in X$, define the $C$-truncated KL divergence as $\tilde{D}_C(\mu \| \nu) = \mathbb{E}_\mu\left[\log\left(\min\left\{\frac{\mu(x)}{\nu(x)}, C\right\}\right)\right]$ for some fixed $C$ such that $\log C \geq 8$. Then $\tilde{D}_C(\mu \| \nu) \geq \frac{1}{2}\|\mu - \nu\|_1^2$.

## Auxiliary lemma

[p. 23] The proof relies on the following lemma which bounds the KL-divergence for binary distributions.

**Lemma 9.** *For every $0 \leq q \leq p \leq 1$, we have*

1. $p \log \frac{p}{q} + (1 - p) \log \frac{1-p}{1-q} \geq 2(p - q)^2$.
2. $3p + (1 - p) \log \frac{1-p}{1-q} \geq 2(p - q)^2$.

*Proof.* For the second result, first observe that $\log(1/(1-q)) \geq 0$ and $(p - q) \leq p$ as $q \leq p$. Both the results then follow from standard calculus. $\square$

## Main proof

[p. 23] Let $A := \{x \in X : \mu(x) \geq \nu(x)\}$ and $B := \{x \in X : \mu(x) \geq C\nu(x)\}$. Let $\mu(A) = p$, $\mu(B) = \delta$, $\nu(A) = q$ and $\nu(B) = \epsilon$. Note that $\|\mu - \nu\|_1 = 2(\mu(A) - \nu(A))$. By the log-sum inequality:

$$\tilde{D}_C(\mu \| \nu) = \sum_{x \in B} \mu(x) \log \frac{\mu(x)}{\nu(x)} + \sum_{x \in A - B} \mu(x) \log \frac{\mu(x)}{\nu(x)} + \sum_{x \in X - A} \mu(x) \log \frac{\mu(x)}{\nu(x)}$$

$$= \delta \log C + (p - \delta) \log \frac{p - \delta}{q - \epsilon} + (1 - p) \log \frac{1 - p}{1 - q}.$$

### Case 1: $0.5 \leq \frac{\delta}{p} \leq 1$

$$\tilde{D}_C(\mu \| \nu) \geq \frac{p}{2} \log C + (1 - p) \log \frac{1 - p}{1 - q}$$

$$\geq 2(p - q)^2 = \frac{1}{2}\|\mu - \nu\|_1^2.$$

### Case 2: $\frac{\delta}{p} < 0.5$

$$\tilde{D}_C(\mu \| \nu) = \delta \log C + (p - \delta) \log \frac{p}{q - \epsilon} + (p - \delta) \log\left(1 - \frac{\delta}{p}\right) + (1 - p) \log \frac{1 - p}{1 - q}$$

$$\geq \delta \log C + (p - \delta) \log \frac{p}{q} - (p - \delta)\frac{2\delta}{p} + (1 - p) \log \frac{1 - p}{1 - q}$$

$$\geq \delta(\log C - 2) + (p - \delta) \log \frac{p}{q} + (1 - p) \log \frac{1 - p}{1 - q}.$$

#### Sub-case 1: $\log \frac{p}{q} \geq 6$

$$\tilde{D}_C(\mu \| \nu) \geq (p - \delta) \log \frac{p}{q} + (1 - p) \log \frac{1 - p}{1 - q}$$

$$\geq 3p + (1 - p) \log \frac{1 - p}{1 - q}$$

$$\geq 2(p - q)^2 = \frac{1}{2}\|\mu - \nu\|_1^2.$$

#### Sub-case 2: $\log \frac{p}{q} < 6$

$$\tilde{D}_C(\mu \| \nu) \geq \delta(\log C - 2 - \log \frac{p}{q}) + p \log \frac{p}{q} + (1 - p) \log \frac{1 - p}{1 - q}$$

$$\geq 2(p - q)^2 = \frac{1}{2}\|\mu - \nu\|_1^2. \quad \square$$
