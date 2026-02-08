# 6 Lower Bound for Small Alphabets [p. 16-17]

[p. 16] The lower bounds for the sample complexity in the binary alphabet case are based on the average case hardness of the decision version of the parity with noise problem, and the reduction is straightforward.

## Parity with noise problem

[p. 16] In the parity with noise problem on $n$ bit inputs, examples $\mathbf{v} \in \{0, 1\}^n$ are drawn uniformly from $\{0, 1\}^n$ along with their noisy labels $\langle \mathbf{s}, \mathbf{v} \rangle + \epsilon \mod 2$ where $\mathbf{s} \in \{0, 1\}^n$ is the (unknown) support of the parity function, and $\epsilon \in \{0, 1\}$ is the classification noise such that $Pr[\epsilon = 1] = \eta$ where $\eta < 0.05$ is the noise level.

Let $Q_{\mathbf{s}}^\eta$ be the distribution over examples of the parity with noise instance with $\mathbf{s}$ as the support of the parity function and $\eta$ as the noise level. Let $U_n$ be the distribution over examples and labels where each label is chosen uniformly from $\{0, 1\}$ independent of the example. The strength of the lower bounds depends on the level of hardness of parity with noise.

Currently, the fastest algorithm for the problem due to Blum et al. [22] runs in time and samples $2^{n / \log n}$.

## Definition 2

[p. 16] **Definition 2.** Define $f(n)$ to be the function such that for a uniformly random support $\mathbf{s} \in \{0, 1\}^n$, with probability at least $(1 - 1/n^2)$ over the choice of $\mathbf{s}$, any (randomized) algorithm that can distinguish between $Q_{\mathbf{s}}^\eta$ and $U_n$ with success probability greater than $2/3$ over the randomness of the examples and the algorithm, requires $f(n)$ time or samples.

## Sequential model construction

[p. 16-17] The model is the natural sequential version of the parity with noise problem, where each example is coupled with several parity bits. The model is denoted $\mathcal{M}(\mathbf{A}_{m \times n})$ for some $\mathbf{A} \in \{0, 1\}^{m \times n}$, $m \leq n/2$.

- From time $0$ through $(n - 1)$ the outputs of the model are i.i.d. and uniform on $\{0, 1\}$.
- Let $\mathbf{v} \in \{0, 1\}^n$ be the vector of outputs from time $0$ to $(n - 1)$.
- The outputs for the next $m$ time steps are given by $\mathbf{y} = \mathbf{A}\mathbf{v} + \boldsymbol{\epsilon} \mod 2$, where $\boldsymbol{\epsilon} \in \{0, 1\}^m$ is the random noise and each entry $\epsilon_i$ of $\boldsymbol{\epsilon}$ is an i.i.d random variable such that $Pr[\epsilon_i = 1] = \eta$, where $\eta$ is the noise level.

Note that if $\mathbf{A}$ is full row-rank, and $\mathbf{v}$ is chosen uniformly at random from $\{0, 1\}^n$, the distribution of $\mathbf{y}$ is uniform on $\{0, 1\}^m$. Also $I(\mathcal{M}(\mathbf{A})) \leq m$ as at most the $m$ binary bits from time $n$ to $n + m - 1$ can be predicted using the past inputs.

As for the large alphabet case, $\mathcal{M}(\mathbf{A}_{m \times n})$ can be simulated by an HMM with $2^m(2n + m) + m$ hidden states (see Section 5.1).

## Family of sequential models

[p. 17] A set of $\mathbf{A}$ matrices specifies a family of sequential models. Let $\mathcal{S}$ be the set of all $(m \times n)$ matrices $\mathbf{A}$ such that the $\mathbf{A}$ is full row rank. This restriction is needed as otherwise the bits of the output $\mathbf{y}$ will be dependent. The family of models $\mathcal{R}$ is denoted as $\mathcal{M}(\mathbf{A})$ for $\mathbf{A} \in \mathcal{S}$.

## Lemma 3

[p. 17] **Lemma 3.** *Let $\mathbf{A}$ be chosen uniformly at random from the set $\mathcal{S}$. Then, with probability at least $(1 - 1/n)$ over the choice $\mathbf{A} \in \mathcal{S}$, any (randomized) algorithm that can distinguish the outputs from the model $\mathcal{M}(\mathbf{A})$ from the distribution over random examples $U_n$ with success probability greater than $2/3$ over the randomness of the examples and the algorithm needs $f(n)$ time or examples.*

The proof of Proposition 2 follows from Lemma 3 and is similar to the proof for the large alphabet case.
