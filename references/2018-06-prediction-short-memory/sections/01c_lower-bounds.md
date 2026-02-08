# 1.3 Lower bounds [p. 5-6]

## Data requirements for the Markov model

[p. 5] The positive results show that accurate prediction is possible via an algorithmically simple model -- a Markov model that only depends on the most recent observations -- which can be learned in an algorithmically straightforward fashion by using empirical statistics of short sequences, compiled over a sufficient amount of data. Nevertheless, the Markov model has $d^\ell$ parameters and hence requires data scaling as $\Omega(d^\ell)$ to learn, where $d$ is the alphabet size. This raises the question of whether a successful predictor can be learned from significantly less data.

## Information-theoretic parameters of HMMs

[p. 5] An HMM with $n$ hidden states and output alphabet of size $d$ is defined via only $O(n^2 + nd)$ parameters, and $O_\epsilon(n^2 + nd)$ samples *are* sufficient from an information-theoretic standpoint to learn a model that will predict accurately. While learning an HMM is computationally hard (see e.g. [17]), this begs the question of whether accurate (average) prediction can be achieved via a computationally efficient algorithm with significantly less than the $d^{\Theta(\log n)}$ data that the naive Markov model would require.

## Theorem 2 (computational lower bound)

[p. 5] The main lower bound shows that there exists a family of HMMs such that the $d^{\Omega(\log n / \epsilon)}$ sample complexity requirement is necessary for any computationally efficient algorithm that predicts accurately on average, assuming the hardness of strongly refuting a certain class of CSPs. This hardness was conjectured in Feldman et al. [18] and studied in related works Allen et al. [19] and Kothari et al. [20]. See Section 5 for a description of this class and the conjectured hardness.

**Theorem 2.** *Assuming the hardness of strongly refuting a certain class of CSPs, for all sufficiently large $n$ and any $\epsilon \in (1/n^c, 0.1)$ for some fixed constant $c$, there exists a family of HMMs with $n$ hidden states and an output alphabet of size $d$ such that any algorithm that runs in time polynomial in $d$, namely time $f(n, \epsilon) \cdot d^{g(n,\epsilon)}$ for any functions $f, g$, and achieves average KL or $\ell_1$ error $\epsilon$ (with respect to the optimal predictor) for a random HMM in the family must observe $d^{\Omega(\log n / \epsilon)}$ observations from the HMM.*

## Implications of Theorem 2

[p. 5] Since the mutual information of the generated sequence of an HMM with $n$ hidden states is bounded by $\log n$, Theorem 2 directly implies that there are families of data-generating distributions $\mathcal{M}$ with mutual information $I(\mathcal{M})$ and observations drawn from an alphabet of size $d$ such that any computationally efficient algorithm requires $d^{\Omega(I(\mathcal{M})/\epsilon)}$ samples from $\mathcal{M}$ to achieve average error $\epsilon$.

The above bound holds when $d$ is large compared to $\log n$ or $I(\mathcal{M})$. In a different but equally relevant regime where the alphabet size $d$ is small compared to the scale of dependencies in the sequence (e.g., when predicting characters [21]), lower bounds of the same flavor are shown based on the problem of learning a noisy parity function; the (very slightly) subexponential algorithm of Blum et al. [22] for this task means a superconstant factor is lost in the exponent compared to the positive results of Proposition 1.

## Proposition 2 (noisy parity lower bound)

[p. 5-6] **Proposition 2.** *Let $f(k)$ denote a lower bound on the amount of time and samples required to learn parity with noise on uniformly random $k$-bit inputs. For all sufficiently large $n$ and $\epsilon \in (1/n^c, 0.1)$ for some fixed constant $c$, there exists a family of HMMs with $n$ hidden states such that any algorithm that achieves average prediction error $\epsilon$ (with respect to the optimal predictor) for a random HMM in the family requires at least $f(\Omega(\log n / \epsilon))$ time or samples.*

## Information-theoretic optimality (Proposition 3)

[p. 6] The authors also establish the *information theoretic* optimality of the results of Proposition 1, in the sense that among (even computationally unbounded) prediction algorithms that predict based only on the most recent $\ell$ observations, an average KL prediction error of $\Omega(I(\mathcal{M})/\ell)$ and $\ell_1$ error $\Omega(\sqrt{I(\mathcal{M})/\ell})$ with respect to the optimal predictor, is necessary.

**Proposition 3.** *There is an absolute constant $c < 1$ such that for all $0 < \epsilon < 1/4$ and sufficiently large $n$, there exists an HMM with $n$ hidden states such that it is not information-theoretically possible to obtain average KL prediction error less than $\epsilon$ or $\ell_1$ error less than $\sqrt{\epsilon}$ (with respect to the optimal predictor) while using only the most recent $c \log n / \epsilon$ observations to make each prediction.*
