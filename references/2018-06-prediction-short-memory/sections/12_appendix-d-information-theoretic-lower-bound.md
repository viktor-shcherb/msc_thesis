# D Proof of Information Theoretic Lower Bound [p. 31-34]

## Proposition 3

[p. 31] **Proposition 3.** *There is an absolute constant $c$ such that for all $0 < \epsilon < 0.5$ and sufficiently large $n$, there exists an HMM with $n$ states such that it is not information theoretically possible to get average relative zero-one loss or $\ell_1$ loss less than $\epsilon$ using windows of length smaller than $c \log n / \epsilon^2$, and KL loss less than $\epsilon$ using windows of length smaller than $c \log n / \epsilon$.*

## Proof construction

[p. 31] *Proof.* Consider a Hidden Markov Model with the Markov chain being a permutation on $n$ states. The output alphabet of each hidden state is binary. Each state $i$ is marked with a label $l_i$ which is 0 or 1, let $G(i)$ be mapping from hidden state $h_i$ to its label $l_i$. All the states labeled 1 emit 1 with probability $(0.5 + \epsilon)$ and 0 with probability $(0.5 - \epsilon)$. Similarly, all the states labeled 0 emit 0 with probability $(0.5 + \epsilon)$ and 1 with probability $(0.5 - \epsilon)$. Fig. 3 illustrates the construction and provides the high-level proof idea.

## Figure 3

**Figure 3** (p. 31): `"Lower bound construction, l = 3, n = 16."`

The figure shows a circular permutation HMM with hidden states arranged in a ring, each with a binary label. A note on notation: $r(0)$ corresponds to the label of $h_0$, $h_1$ and $h_2$ and is $(0, 1, 0)$ in this case. Similarly, $r(1) = (1, 1, 0)$. The segments between the shaded nodes comprise the set $\mathcal{S}_1$ and are the possible sequences of states from which the last $\ell = 3$ outputs could have come. The shaded nodes correspond to the states in $\mathcal{S}_2$, and are the possible predictions for the next time step. In this example $\mathcal{S}_1 = \{(0, 1, 0), (1, 1, 0), (0, 1, 0), (1, 1, 1)\}$ and $\mathcal{S}_2 = \{1, 1, 0, 0\}$.

## Setup and notation

[p. 31] Assume $n$ is a multiple of $(\ell + 1)$, where $(\ell + 1) = c \log n / \epsilon^2$, for a constant $c = 1/33$. Regard $\epsilon$ as a constant with respect to $n$. Let $n/(\ell + 1) = t$. Refer to the hidden states by $h_i$, where $0 \leq i \leq (n - 1)$, and $h_i^j$ refers to the sequence of hidden states $i$ through $j$. The paper shows that a model looking at only the past $\ell$ outputs cannot get average zero-one loss less than $0.5 - o(1)$ (as the optimal prediction looking at all past outputs can be determined to an arbitrarily high probability if we are allowed to look at an arbitrarily long past), this proves that windows of length $\ell$ do not suffice to get average zero-one error less than $\epsilon - o(1)$ with respect to the optimal predictions.

Note that the Bayes optimal prediction at time $(\ell + 1)$ to minimize the expected zero-one loss given outputs from time 1 to $\ell$ is to predict the mode of the distribution $Pr(x_{\ell+1} | x_1^\ell = s_1^\ell)$ where $s_1^\ell$ is the sequence of outputs from time 1 to $\ell$. Also, $Pr(x_{\ell+1} | x_1^\ell = s_1^\ell) = \sum_i Pr(h_{i_\ell} = i | x_1^\ell = s_1^\ell) Pr(x_{\ell+1} | h_{i_\ell} = i)$ where $h_{i_\ell}$ is the hidden state at time $\ell$. Hence the predictor is a weighted average of the prediction of each hidden state with the weight being the probability of being at that hidden state.

## Indexing the permutation

[p. 31-32] We index each state $h_i$ of the permutation by a tuple $(f(i), g(i)) = (j, k)$ where $j = i \mod (\ell + 1)$ and $k = \lfloor \frac{i}{\ell+1} \rfloor$ hence $0 \leq j \leq \ell$, $0 \leq k \leq (t - 1)$ and $i = k(\ell + 1) + j$. We help the predictor to make the prediction at time $(\ell + 1)$ by providing it with the index $f(i_\ell) = i_\ell \mod (\ell + 1)$ of the true hidden state $h_{i_\ell}$ at time $\ell$. Hence this narrows down the set of possible hidden states at time $\ell$ (in Fig. 3, the set of possible states given this side information are all the hidden states before the shaded states). The Bayes optimal prediction at time $(\ell + 1)$ given outputs $s_1^\ell$ from time 1 to $\ell$ and index $f(h_{i_\ell}) = j$ is to predict the mode of $Pr(x_{\ell+1} | x_1^\ell = s_1^\ell, f(h_{i_\ell}) = j)$. Note that by the definition of Bayes optimality, the average zero-one loss of the prediction using $Pr(x_{\ell+1} | x_1^\ell = s_1^\ell, f(h_{i_\ell}) = j)$ cannot be worse than the average zero-one loss of the prediction using $Pr(x_{\ell+1} | x_1^\ell = s_1^\ell)$. Hence we only need to show that the predictor with access to this side information is poor.

[p. 32] We refer to this predictor using $Pr(x_{\ell+1} | x_1^\ell = s_1^\ell, f(h_{i_\ell}) = j)$ as $\mathcal{P}$. We will now show that there exists some permutation for which the average zero-one loss of the predictor $\mathcal{P}$ is $0.5 - o(1)$. We argue this using the probabilistic method. We choose a permutation uniformly at random from the set of all permutations. We show that the expected average zero-one loss of the predictor $\mathcal{P}$ over the randomness in choosing the permutation is $0.5 - o(1)$. This means that there must exist some permutation such that the average zero-one loss of the predictor $\mathcal{P}$ on that permutation is $0.5 - o(1)$.

## Finding the expected zero-one loss

[p. 32] To find the expected zero-one loss of the predictor $\mathcal{P}$ over the randomness in choosing the permutation, we will find the expected zero-one loss of the predictor $\mathcal{P}$ given that we are in some state $h_{i_\ell}$ at time $\ell$. Without loss of generality let $f(i_\ell) = 0$ and $g(i_\ell) = (\ell - 1)$, hence we were at the $(\ell - 1)$th hidden state at time $\ell$. Fix any sequence of labels for the hidden states $h_0^{\ell-1}$. For any string $s_0^{\ell-1}$ emitted by the hidden states $h_0^{\ell-1}$ from time 0 to $\ell - 1$, let $\mathbb{E}[\delta(s_0^{\ell-1})]$ be the expected average zero-one error of the predictor $\mathcal{P}$ over the randomness in the rest of the permutation. Also, let $\mathbb{E}[\delta(h_{\ell-1})] = \sum_{s_0^{\ell-1}} \mathbb{E}[\delta(s_0^{\ell-1})] Pr[s_0^{\ell-1}]$ be the expected error averaged across all outputs. We will argue that $\mathbb{E}[\delta(h_{\ell-1})] = 0.5 - o(1)$.

The set of hidden states $h_i$ with $g(i) = k$ defines a segment of the permutation, let $r(k)$ be the label $G(h_{(k-1)(\ell+1)}^{k(\ell+1)-2})$ of the segment $k$, excluding its last bit which corresponds to the predictions. Let $\mathcal{S}_1 = \{r(k), \forall\, k \neq 0\}$ be the set of all the labels excluding the first label $r(0)$ and $\mathcal{S}_2 = \{G(h_{k(\ell+1)+\ell}), \forall\, k\}$ be the set of all the predicted bits (refer to Fig. 3 for an example).

## Hamming distance argument

[p. 32] Consider any assignment of $r(0)$. To begin, we show that with high probability over the output $s_0^{\ell-1}$, the Hamming distance $D(s_0^{\ell-1}, r(0))$ of the output $s_0^{\ell-1}$ of the set of hidden states $h_0^{\ell-1}$ from $r(0)$ is at least $\frac{\ell}{2} - 2\epsilon\ell$. This follows directly from Hoeffding's inequality (footnote 5) as all the outputs are independent conditioned on the hidden state:

$$Pr[D(s_0^{\ell-1}, r(0)) \leq \ell/2 - 2\epsilon\ell] \leq e^{-2\ell\epsilon^2} \leq n^{-2c} \tag{D.1}$$

Footnote 5: For $n$ independent random variables $\{X_i\}$ lying in the interval $[0, 1]$ with $\bar{X} = \frac{1}{n} \sum_i X_i$, $Pr[X \leq \mathbb{E}[\bar{X}] - t] \leq e^{-2nt^2}$. In our case $t = \epsilon$ and $n = \ell$.

[p. 32] We now show that for any $k \neq 0$, with decent probability the label $r(k)$ of the segment $k$ is closer in Hamming distance to the output $s_0^{\ell-1}$ than $r(0)$. Then we argue that with high probability there are many such segments which are closer to $s_0^{\ell-1}$ in Hamming distance as $r(0)$. Hence these other segments are assigned as much weight in predicting the next output as $r(0)$, which means that the output cannot be predicted with a high accuracy as the output bits corresponding to different segments are independent.

## Bounding probability of close segments

[p. 32-33] We first find the probability that the segment corresponding to some $k$ with label $r(k)$ has a Hamming distance less than $\frac{\ell}{2} - \sqrt{\ell \log t / 8}$ from any fixed binary string $x$ of length $\ell$. Let $F(l, m, p)$ be the probability of getting at least $l$ heads in $m$ i.i.d. trails with each trial having probability $p$ of giving a head. $F(l, m, p)$ can be bounded below by the following standard inequality:

$$F(l, m, p) \geq \frac{1}{\sqrt{2m}} \exp\left(-m D_{KL}\left(\frac{l}{m} \| p\right)\right)$$

where $D_{KL}(q \| p) = q \log \frac{q}{p} + (1-q) \log \frac{1-q}{1-p}$. We can use this to lower bound $Pr\left[D(r(k), x) \leq \ell/2 - \sqrt{\ell \log t / 8}\right]$:

$$Pr\left[D(r(k), x) \leq \ell/2 - \sqrt{\ell \log t / 8}\right] = F(\ell/2 + \sqrt{\ell \log t / 8}, \ell, 1/2)$$

$$\geq \frac{1}{\sqrt{2\ell}} \exp\left(-\ell D_{KL}\left(\frac{1}{2} + \sqrt{\frac{\log t}{8\ell}} \| \frac{1}{2}\right)\right)$$

[p. 33] Note that $D_{KL}(\frac{1}{2} + v \| \frac{1}{2}) \leq 4v^2$ by using the inequality $\log(1 + v) \leq v$. We can simplify the KL-divergence using this and write:

$$Pr\left[D(r(k), x) \leq \ell/2 - \sqrt{\ell \log t / 8}\right] \geq 1/\sqrt{2\ell t} \tag{D.2}$$

## Concentration on number of close segments

[p. 33] Let $\mathcal{D}$ be the set of all $k \neq 0$ such that $D(r(k), x) \leq \frac{\ell}{2} - \sqrt{\ell \log t / 8}$ for some fixed $x$. We argue that with high probability over the randomness of the permutation $|\mathcal{D}|$ is large. This follows from Eq. D.2 and the Chernoff bound (footnote 6) as the labels for all segments $r(k)$ are chosen independently:

$$Pr\left[|\mathcal{D}| \leq \sqrt{t/(8\ell)}\right] \leq e^{-\frac{1}{8}\sqrt{t/(2\ell)}}$$

Footnote 6: For independent random variables $\{X_i\}$ lying in the interval $[0, 1]$ with $X = \sum_i X_i$ and $\mu = \mathbb{E}[X]$, $Pr[X \leq (1 - c)\mu] \leq \exp(-c^2 \mu / 2)$. In our case $c = 1/2$ and $\mu = \sqrt{t/(2\ell)}$.

[p. 33] Note that $\sqrt{t/(8\ell)} \geq n^{0.25}$. Therefore for any fixed $x$, with probability $1 - \exp(-\frac{1}{8}\sqrt{\frac{t}{2\ell}}) \geq 1 - n^{-0.25}$ there are $\sqrt{\frac{t}{8\ell}} \geq n^{0.25}$ segments in a randomly chosen permutation which have Hamming distance less than $\ell/2 - \sqrt{\ell \log t / 8}$ from $x$. Note that by our construction $2\epsilon\ell \leq \sqrt{\ell \log t / 8}$ because $\log(\ell + 1) \leq (1 - 32c) \log n$. Hence the segments in $\mathcal{D}$ are closer in Hamming distance to the output $s_0^{\ell-1}$ if $D(s_0^{\ell-1}, r(0)) > \ell/2 - 2\epsilon\ell$.

## Main probability bound

[p. 33-34] Therefore if $D(s_0^{\ell-1}, r(0)) > \ell/2 - 2\epsilon\ell$, then with high probability over randomly choosing the segments $\mathcal{S}_1$ there is a subset $\mathcal{D}$ of segments in $\mathcal{S}_1$ with $|\mathcal{D}| \geq n^{0.25}$ such that all of the segments in $\mathcal{D}$ have Hamming distance less than $D(s_0^{\ell-1}, r(0))$ from $s_0^{\ell-1}$. Pick any $s_0^{\ell-1}$ such that $D(s_0^{\ell-1}, r(0)) > \ell/2 - 2\epsilon\ell$. Consider any set of segments $\mathcal{S}_1$ which has such a subset $\mathcal{D}$ with respect to the string $s_0^{\ell-1}$. For all such permutations, the predictor $\mathcal{P}$ places at least as much weight on the hidden states $h_i$ with $g(i) = k$, with $k$ such that $r(k) \in \mathcal{D}$ as the true hidden state $h_{\ell-1}$. The prediction for any hidden state $h_i$ is the corresponding bit in $\mathcal{S}_2$. Notice that the bits in $\mathcal{S}_2$ are independent and uniform as we've not used them in any argument so far. The average correlation of an equally weighted average of $m$ independent and uniform random bits with any one of the random bits is at most $1/\sqrt{m}$. Hence over the randomness of $\mathcal{S}_2$, the expected zero-one loss of the predictor is at least $0.5 - n^{-0.1}$. Hence we can write:

$$\mathbb{E}[\delta(s_0^{\ell-1})] \geq (0.5 - n^{-0.1}) Pr[|\mathcal{D}| \geq \sqrt{t/(8\ell)}]$$

$$\geq (0.5 - n^{-0.1})(1 - e^{-n^{0.25}})$$

$$\geq 0.5 - 2n^{-0.1}$$

[p. 34] By using Equation D.1, for any assignment $r(0)$ to $h_0^{\ell-1}$:

$$\mathbb{E}[\delta(h_{\ell-1})] \geq Pr\left[D(s_0^{\ell-1}, r(0)) > \ell/2 - 2\epsilon\ell\right] \mathbb{E}\left[\delta(s_0^{\ell-1}) \middle| D(s_0^{\ell-1}, r(0)) > \ell/2 - 2\epsilon\ell\right]$$

$$\geq (1 - n^{-2c})(0.5 - 2n^{-0.1})$$

$$= 0.5 - o(1)$$

As this is true for all assignments $r(0)$ to $h_0^{\ell-1}$ and for all choices of hidden states at time $\ell$, using linearity of expectations and averaging over all hidden states, the expected average zero-one loss of the predictor $\mathcal{P}$ over the randomness in choosing the permutation is $0.5 - o(1)$. This means that there must exist some permutation such that the average zero-one loss of the predictor $\mathcal{P}$ on that permutation is $0.5 - o(1)$. Hence there exists an HMM on $n$ states such that it is not information theoretically possible to get average zero-one error with respect to the optimal predictions less than $\epsilon - o(1)$ using windows of length smaller than $c \log n / \epsilon^2$ for a fixed constant $c$.

## Summary of results for all loss metrics

[p. 34] Therefore, for all $0 < \epsilon < 0.5$ and sufficiently large $n$, there exits an HMM with $n$ states such that it is not information theoretically possible to get average relative zero-one loss less than $\epsilon/2 < \epsilon - o(1)$ using windows of length smaller than $c\epsilon^{-2} \log n$. The result for relative zero-one loss follows on replacing $\epsilon/2$ by $\epsilon'$ and setting $c' = c/4$. The result follows immediately from this as the expected relative zero-one loss is less than the expected $\ell_1$ loss. For KL-loss we use Pinsker's inequality and Jensen's inequality. $\square$

## Acknowledgements

[p. 34] Sham Kakade acknowledges funding from the Washington Research Foundation for Innovation in Data-intensive Discovery, and the NSF Award CCF-1637360. Gregory Valiant and Sham Kakade acknowledge funding form NSF Award CCF-1703574. Gregory was also supported by NSF CAREER Award CCF-1351108 and a Sloan Research Fellowship.
