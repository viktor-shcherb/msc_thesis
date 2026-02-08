# B Proof of Lower Bound for Large Alphabets [p. 24–30]

## B.1 CSP Formulation [p. 24–25]

[p. 24] The notation and setup follow Feldman et al. [18]. Consider the following model for generating a random CSP instance on $n$ variables with a satisfying assignment $\boldsymbol{\sigma}$. The $k$-CSP is defined by the predicate $P : \{0, 1\}^k \to \{0, 1\}$. A $k$-clause is represented by an ordered $k$-tuple of literals from $\{x_1, \ldots, x_n, \bar{x}_1, \ldots, \bar{x}_n\}$ with no repetition of variables and let $X_k$ be the set of all such $k$-clauses. For a $k$-clause $C = (l_1, \ldots, l_k)$ let $\boldsymbol{\sigma}(C) \in \{0, 1\}^k$ be the $k$-bit string of values assigned by $\boldsymbol{\sigma}$ to literals in $C$, that is $\{\boldsymbol{\sigma}(l_1), \ldots, \boldsymbol{\sigma}(l_k)\}$ where $\boldsymbol{\sigma}(l_i)$ is the value of the literal $l_i$ in assignment $\boldsymbol{\sigma}$.

In the planted model, clauses are drawn with probabilities that depend on the value of $\boldsymbol{\sigma}(C)$. Let $Q : \{0, 1\}^k \to \mathbb{R}^+$, $\sum_{\mathbf{t} \in \{0,1\}^k} Q(\mathbf{t}) = 1$ be some distribution over satisfying assignments to $P$. The distribution $Q_{\boldsymbol{\sigma}}$ is then defined as follows:

$$Q_{\boldsymbol{\sigma}}(C) = \frac{Q(\boldsymbol{\sigma}(C))}{\sum_{C' \in X_k} Q(\boldsymbol{\sigma}(C'))} \tag{B.1}$$

Recall that for any distribution $Q$ over satisfying assignments we define its *complexity* $r$ as the largest $r$ such that the distribution $Q$ is $(r-1)$-wise uniform (also referred to as $(r-1)$-wise independent in the literature) but not $r$-wise uniform.

### CSP $\mathcal{C}$ with labels

[p. 24] Consider the CSP $\mathcal{C}$ defined by a collection of predicates $P(\mathbf{y})$ for each $\mathbf{y} \in \{0, 1\}^m$ for some $m \leq k/2$. Let $\mathbf{A} \in \{0, 1\}^{m \times k}$ be a matrix with full row rank over the binary field. The authors will later choose $\mathbf{A}$ to ensure the CSP has high complexity. For each $\mathbf{y}$, the predicate $P(\mathbf{y})$ is the set of solutions to the system $\mathbf{y} = \mathbf{A}\mathbf{v} \mod 2$ where $\mathbf{v} = \boldsymbol{\sigma}(C)$. For all $\mathbf{y}$ we define $Q_\mathbf{y}$ to be the uniform distribution over all consistent assignments, i.e. all $\mathbf{v} \in \{0, 1\}^k$ satisfying $\mathbf{y} = \mathbf{A}\mathbf{v} \mod 2$.

The planted distribution $Q_{\boldsymbol{\sigma}, \mathbf{y}}$ is defined based on $Q_\mathbf{y}$ according to Eq. B.1. Each clause in $\mathcal{C}$ is chosen by first picking a $\mathbf{y}$ uniformly at random and then a clause from the distribution $Q_{\boldsymbol{\sigma}, \mathbf{y}}$. For any planted $\boldsymbol{\sigma}$ we define $Q_{\boldsymbol{\sigma}}$ to be the distribution over all consistent clauses along with their labels $\mathbf{y}$.

Let $U_k$ be the uniform distribution over $k$-clauses, with each clause assigned a uniformly chosen label $\mathbf{y}$. Define $Q_{\boldsymbol{\sigma}}^\eta = (1 - \eta)Q_{\boldsymbol{\sigma}} + \eta U_k$, for some fixed noise level $\eta > 0$. We consider $\eta$ to be a small constant less than 0.05. This corresponds to adding noise to the problem by mixing the planted and the uniform clauses. The problem gets harder as $\eta$ becomes larger, for $\eta = 0$ it can be efficiently solved using Gaussian Elimination.

### CSP $\mathcal{C}_0$ and reduction

[p. 24] A second CSP $\mathcal{C}_0$ is defined which reduces to $\mathcal{C}$ and for which hardness can be obtained using Conjecture 1. The label $\mathbf{y}$ is fixed to be the all zero vector in $\mathcal{C}_0$. Hence $Q_0$, the distribution over satisfying assignments for $\mathcal{C}_0$, is the uniform distribution over all vectors in the null space of $\mathbf{A}$ over the binary field. The planted distribution in this case is referred to as $Q_{\boldsymbol{\sigma}, 0}$. Let $U_{k,0}$ be the uniform distribution over $k$-clauses, with each clause now having the label 0. For any planted assignment $\boldsymbol{\sigma}$, denote the distribution of consistent clauses of $\mathcal{C}_0$ by $Q_{\boldsymbol{\sigma}, 0}$. As before define $Q_{\boldsymbol{\sigma}, 0}^\eta = (1 - \eta)Q_{\boldsymbol{\sigma}, 0} + \eta U_{k,0}$ for the same $\eta$.

### Distinguishing problems $L$ and $L_0$

[p. 24–25] Let $L$ be the problem of distinguishing between $U_k$ and $Q_{\boldsymbol{\sigma}}^\eta$ for some randomly and uniformly chosen $\boldsymbol{\sigma} \in \{0, 1\}^n$ with success probability at least $2/3$. Similarly, let $L_0$ be the problem of distinguishing between $U_{k,0}$ and $Q_{\boldsymbol{\sigma},0}^\eta$ for some randomly and uniformly chosen $\boldsymbol{\sigma} \in \{0, 1\}^n$ with success probability at least $2/3$. $L$ and $L_0$ can be thought of as the problem of distinguishing random instances of the CSPs from instances with a high value. Note that $L$ and $L_0$ are at least as hard as the problem of refuting the random CSP instances $U_k$ and $U_{k,0}$, as this corresponds to the case where $\eta = 0$. The claim is that an algorithm for $L$ implies an algorithm for $L_0$.

**Lemma 10.** *If $L$ can be solved in time $t(n)$ with $s(n)$ clauses, then $L_0$ can be solved in time $O(t(n) + s(n))$ and $s(n)$ clauses.*

### Complexity of $Q_0$

[p. 25] Let the complexity of $Q_0$ be $\gamma k$, with $\gamma \geq 1/10$ (we demonstrate how to achieve this next). By Conjecture 1 distinguishing between $U_{k,0}$ and $Q_{\boldsymbol{\sigma},0}^\eta$ requires at least $\tilde{\Omega}(n^{\gamma k/2})$ clauses. We now discuss how $\mathbf{A}$ can be chosen to ensure that the complexity of $Q_0$ is $\gamma k$.

## B.2 Ensuring High Complexity of the CSP [p. 25–26]

[p. 25] Let $\mathcal{N}$ be the null space of $\mathbf{A}$. Note that the rank of $\mathcal{N}$ is $(k - m)$. For any subspace $\mathcal{D}$, let $\mathbf{w}(\mathcal{D}) = (w_1, \ldots, w_k)$ be a randomly chosen vector from $\mathcal{D}$. To ensure that $Q_0$ has complexity $\gamma k$, it suffices to show that the random variables $\mathbf{w}(\mathcal{N}) = (w_1, w_2, \ldots, w_k)$ are $(\gamma k - 1)$-wise uniform. The theory of error correcting codes is used to find such a matrix $\mathbf{A}$.

### Binary linear codes

[p. 25] A binary linear code $\mathcal{B}$ of length $k$ and rank $m$ is a linear subspace of $\mathbb{F}_2^k$ (the notation is different from the standard notation in the coding theory literature to suit the authors' setting). The rate of the code is defined to be $m/k$. The generator matrix of the code is the matrix $\mathbf{G}$ such that $\mathcal{B} = \{\mathbf{G}\mathbf{v}, \mathbf{v} \in \{0, 1\}^m\}$. The parity check matrix of the code is the matrix $\mathbf{H}$ such that $\mathcal{B} = \{\mathbf{c} \in \{0, 1\}^k : \mathbf{H}\mathbf{c} = 0\}$. The distance $d$ of a code is the weight of the minimum weight codeword and the relative distance $\delta$ is defined to be $\delta = d/k$.

For any codeword $\mathcal{B}$ we define its dual codeword $\mathcal{B}^T$ as the codeword with generator matrix $\mathbf{H}^T$ and parity check matrix $\mathbf{G}^T$. Note that the rank of the dual codeword of a code with rank $m$ is $(k - m)$.

**Fact 1.** *If $\mathcal{B}^T$ has distance $l$, then $\mathbf{w}(\mathcal{B})$ is $(l - 1)$-wise uniform.*

Hence, the job of finding $\mathbf{A}$ reduces to finding a dual code with distance $\gamma k$ and rank $m$, where $\gamma = 1/10$ and $m \leq k/2$. The Gilbert-Varshamov bound is used to argue for the existence of such a code. Let $H(p)$ be the binary entropy of $p$.

**Lemma 11.** *(Gilbert-Varshamov bound)* *For every $0 \leq \delta < 1/2$, and $0 < \epsilon \leq 1 - H(\delta)$, there exists a code with rank $m$ and relative distance $\delta$ if $m/k = 1 - H(\delta) - \epsilon$.*

[p. 25–26] Taking $\delta = 1/10$, $H(\delta) \leq 0.5$, hence there exists a code $\mathcal{B}$ whenever $m/k \leq 0.5$, which is the setting of interest. We choose $\mathbf{A} = \mathbf{G}^T$, where $\mathbf{G}$ is the generator matrix of $\mathcal{B}$. Hence the null space of $\mathbf{A}$ is $(k/10 - 1)$-wise uniform, hence the complexity of $Q_0$ is $\gamma k$ with $\gamma \geq 1/10$. Hence for all $k$ and $m \leq k/2$ we can find a $\mathbf{A} \in \{0, 1\}^{m \times k}$ to ensure that the complexity of $Q_0$ is $\gamma k$.

## B.3 Sequential Model of CSP and Sample Complexity Lower Bound [p. 26–30]

[p. 26] A sequential model is constructed which derives hardness from the hardness of $L$. Here the construction slightly differs from the outline presented in the beginning of Section 5 as the sequential model cannot be based directly on $L$ as generating random $k$-tuples without repetition increases the mutual information, so a slight variation $L'$ of $L$ is formulated which is shown to be at least as hard as $L$. The CSP instance is not defined allowing repetition as that is different from the setting examined in Feldman et al. [18], and hardness of the setting with repetition does not follow from hardness of the setting allowing repetition, though the converse is true.

### B.3.1 Constructing sequential model [p. 26]

[p. 26] Consider the following family of sequential models $\mathcal{R}(n, \mathbf{A}_{m \times k})$ where $\mathbf{A} \in \{0, 1\}^{m \times k}$ is chosen as defined previously. The output alphabet of all models in the family is $\mathcal{X} = \{a_i, 1 \leq i \leq 2n\}$ of size $2n$, with $2n/k$ even. A subset $\mathcal{S}$ of $\mathcal{X}$ of size $n$ is chosen; each choice of $\mathcal{S}$ corresponds to a model $\mathcal{M}$ in the family. Each letter in the output alphabet is encoded as a 1 or 0 representing whether or not the letter is included in the set $\mathcal{S}$. Let $\mathbf{u} \in \{0, 1\}^{2n}$ be the vector which stores this encoding so $u_i = 1$ whenever the letter $a_i$ is in $\mathcal{S}$. Let $\boldsymbol{\sigma} \in \{0, 1\}^n$ determine the subset $\mathcal{S}$ such that entry $u_{2i-1}$ is 1 and $u_{2i}$ is 0 when $\boldsymbol{\sigma}_i$ is 1 and $u_{2i-1}$ is 0 and $u_{2i}$ is 1 when $\boldsymbol{\sigma}_i$ is 0, for all $i$. We choose $\boldsymbol{\sigma}$ uniformly at random from $\{0, 1\}^n$ and each choice of $\boldsymbol{\sigma}$ represents some subset $\mathcal{S}$, and hence some model $\mathcal{M}$.

The output alphabet $\mathcal{X}$ is partitioned into $k$ subsets of size $2n/k$ each so the first $2n/k$ letters go to the first subset, the next $2n/k$ go to the next subset and so on. Let the $i$th subset be $\mathcal{X}_i$. Let $\mathcal{S}_i$ be the set of elements in $\mathcal{X}_i$ which belong to the set $\mathcal{S}$.

At time 0, $\mathcal{M}$ chooses $\mathbf{v} \in \{0, 1\}^k$ uniformly at random from $\{0, 1\}^k$. At time $i$, $i \in \{0, \ldots, k-1\}$, if $v_i = 1$, then the model chooses a letter uniformly at random from the set $\mathcal{S}_i$, otherwise if $v_i = 0$ it chooses a letter uniformly at random from $\mathcal{X}_i - \mathcal{S}_i$. With probability $(1 - \eta)$ the outputs for the next $m$ time steps from $k$ to $(k + m - 1)$ are $\mathbf{y} = \mathbf{A}\mathbf{v} \mod 2$, with probability $\eta$ they are $m$ uniform random bits. The model resets at time $(k + m - 1)$ and repeats the process.

Recall that $I(\mathcal{M})$ is at most $m$ and $\mathcal{M}$ can be simulated by an HMM with $2^m(2k + m) + m$ hidden states (see Section 5.1).

### B.3.2 Reducing sequential model to CSP instance [p. 26–27]

[p. 26] The matrix $\mathbf{A}$ is revealed to the algorithm (this corresponds to revealing the transition matrix of the underlying HMM), but the encoding $\boldsymbol{\sigma}$ is kept secret. The task of finding the encoding $\boldsymbol{\sigma}$ given samples from $\mathcal{M}$ can be naturally seen as a CSP. Each sample is a clause with the literal corresponding to the output letter $a_i$ being $x_{(i+1)/2}$ whenever $i$ is odd and $\bar{x}_{i/2}$ when $i$ is even. We refer the reader to the outline at the beginning of the section for an example.

We denote $\mathcal{C}'$ as the CSP $\mathcal{C}$ with the modification that the $i$th literal of each clause is the literal corresponding to a letter in $\mathcal{X}_i$ for all $1 \leq i \leq k$. Define $Q'_{\boldsymbol{\sigma}}$ as the distribution of consistent clauses for the CSP $\mathcal{C}'$. Define $U'_k$ as the uniform distribution over $k$-clauses with the additional constraint that the $i$th literal of each clause is the literal corresponding to a letter in $\mathcal{X}_i$ for all $1 \leq i \leq k$. Define $Q'^{\eta}_{\boldsymbol{\sigma}} = (1 - \eta)Q'_{\boldsymbol{\sigma}} + \eta U'_k$. Note that samples from the model $\mathcal{M}$ are equivalent to clauses from $Q'^{\eta}_{\boldsymbol{\sigma}}$. We show that hardness of $L'$ follows from hardness of $L$.

**Lemma 12.** *If $L'$ can be solved in time $t(n)$ with $s(n)$ clauses, then $L$ can be solved in time $t(n)$ with $O(s(n))$ clauses. Hence if Conjecture 1 is true then $L'$ cannot be solved in polynomial time with less than $\tilde{\Omega}(n^{\gamma k/2})$ clauses.*

### Proof of Theorem 2 [p. 27–28]

[p. 27] **Theorem 2.** *Assuming Conjecture 1, for all sufficiently large $T$ and $1/T^c < \epsilon \leq 0.1$ for some fixed constant $c$, there exists a family of HMMs with $T$ hidden states and an output alphabet of size $n$ such that, any prediction algorithm that achieves average KL-error, $\ell_1$ error or relative zero-one error less than $\epsilon$ with probability greater than $2/3$ for a randomly chosen HMM in the family, and runs in time $f(T, \epsilon) \cdot n^{g(T,\epsilon)}$ for any functions $f$ and $g$, requires $n^{\Omega(\log T / \epsilon)}$ samples from the HMM.*

*Proof.* We describe how to choose the family of sequential models $\mathcal{R}(n, \mathbf{A}_{m \times k})$ for each value of $\epsilon$ and $T$. Recall that the HMM has $T = 2^m(2k + m) + m$ hidden states. Let $T' = 2^{m+2}(k + m)$. Note that $T' \geq T$. Let $t = \log T'$. We choose $m = t - \log(1/\epsilon) - \log(t/5)$, and $k$ to be the solution of $t = m + \log(k + m) + 2$, hence $k = t/(5\epsilon) - m - 2$. Note that for $\epsilon \leq 0.1$, $k \geq m$. Let $\epsilon' = \frac{2}{9} \frac{m}{k+m}$. We claim $\epsilon \leq \epsilon'$. To verify, note that $k + m = t/(5\epsilon) - 2$. Therefore,

$$\epsilon' = \frac{2m}{9(k+m)} = \frac{10\epsilon(t - \log(1/\epsilon) - \log(t/5))}{9t(1 - 10\epsilon/t)} \geq \epsilon,$$

for sufficiently large $t$ and $\epsilon \geq 2^{-ct}$ for a fixed constant $c$. Hence proving hardness for obtaining error $\epsilon'$ implies hardness for obtaining error $\epsilon$. We choose the matrix $\mathbf{A}_{m \times k}$ as outlined earlier. For each vector $\boldsymbol{\sigma} \in \{0, 1\}^n$ we define the family of sequential models $\mathcal{R}(n, \mathbf{A})$ as earlier. Let $\mathcal{M}$ be a randomly chosen model in the family.

#### Relative zero-one loss [p. 27]

[p. 27] The proof first shows the result for the relative zero-one loss. The idea is that any algorithm which does a good job of predicting the outputs from time $k$ through $(k + m - 1)$ can be used to distinguish between instances of the CSP with a high value and uniformly random clauses. This is because it is not possible to make good predictions on uniformly random clauses.

The zero-one error from time $k$ through $(k + m - 1)$ is related to the relative zero-one error from time $k$ through $(k + m - 1)$ and the average zero-one error for all time steps to get the required lower bounds.

Let $\rho_{01}(\mathcal{A})$ be the average zero-one loss of some polynomial time algorithm $\mathcal{A}$ for the output time steps $k$ through $(k + m - 1)$ and $\delta'_{01}(\mathcal{A})$ be the average relative zero-one loss of $\mathcal{A}$ for the output time steps $k$ through $(k + m - 1)$ with respect to the optimal predictions. For the distribution $U'_k$ it is not possible to get $\rho_{01}(\mathcal{A}) < 0.5$ as the clauses and the label $\mathbf{y}$ are independent and $\mathbf{y}$ is chosen uniformly at random from $\{0, 1\}^m$. For $Q'^{\eta}_{\boldsymbol{\sigma}}$ it is information theoretically possible to get $\rho_{01}(\mathcal{A}) = \eta/2$. Hence any algorithm which gets error $\rho_{01}(\mathcal{A}) \leq 2/5$ can be used to distinguish between $U'_k$ and $Q'^{\eta}_{\boldsymbol{\sigma}}$. Therefore by Lemma 12 any polynomial time algorithm which gets $\rho_{01}(\mathcal{A}) \leq 2/5$ with probability greater than 2/3 over the choice of $\mathcal{M}$ needs at least $\tilde{\Omega}(n^{\gamma k/2})$ samples.

Note that $\delta'_{01}(\mathcal{A}) = \rho_{01}(\mathcal{A}) - \eta/2$. As the optimal predictor $\mathcal{P}_\infty$ gets $\rho_{01}(\mathcal{P}_\infty) = \eta/2 < 0.05$, therefore $\delta'_{01}(\mathcal{A}) \leq 1/3 \implies \rho_{01}(\mathcal{A}) \leq 2/5$. Note that $\delta_{01}(\mathcal{A}) \geq \delta'_{01}(\mathcal{A}) \frac{m}{k+m}$. This is because $\delta_{01}(\mathcal{A})$ is the average error for all $(k+m)$ time steps, and the contribution to the error from time steps 0 to $(k-1)$ is non-negative. Also, $\frac{1}{3} \frac{m}{k+m} > \epsilon'$, therefore, $\delta_{01}(\mathcal{A}) < \epsilon' \implies \delta'_{01}(\mathcal{A}) < \frac{1}{3} \implies \rho_{01}(\mathcal{A}) \leq 2/5$. Hence any polynomial time algorithm which gets average relative zero-one loss less than $\epsilon'$ with probability greater than 2/3 needs at least $\tilde{\Omega}(n^{\gamma k/2})$ samples. The result for $\ell_1$ loss follows directly from the result for relative zero-one loss.

#### KL loss [p. 27]

[p. 27] Let $\delta'_{KL}(\mathcal{A})$ be the average KL error of the algorithm $\mathcal{A}$ from time steps $k$ through $(k + m - 1)$. By application of Jensen's inequality and Pinsker's inequality, $\delta'_{KL}(\mathcal{A}) \leq 2/9 \implies \delta'_{01}(\mathcal{A}) \leq 1/3$. Therefore, by the previous argument any algorithm which gets $\delta'_{KL}(\mathcal{A}) < 2/9$ needs $\tilde{\Omega}(n^{\gamma k/2})$ samples. But as before, $\delta_{KL}(\mathcal{A}) \leq \epsilon' \implies \delta'_{KL}(\mathcal{A}) \leq 2/9$. Hence any polynomial time algorithm which succeeds with probability greater than 2/3 and gets average KL loss less than $\epsilon'$ needs at least $\tilde{\Omega}(n^{\gamma k/2})$ samples.

#### Lower bounding $k$ in terms of $\log T / \epsilon$ [p. 28]

[p. 28] We lower bound $k$ by a linear function of $\log T / \epsilon$ to express the result directly in terms of $\log T / \epsilon$. The claim is that $\log T / \epsilon$ is at most $10k$. This follows because:

$$\log T / \epsilon \leq t / \epsilon = 5(k + m) + 10 \leq 15k$$

Hence any polynomial time algorithm needs $n^{\Theta(\log T / \epsilon)}$ samples to get average relative zero-one loss, $\ell_1$ loss, or KL loss less than $\epsilon$ on $\mathcal{M}$. $\square$

## B.4 Proof of Lemma 10 [p. 28–29]

**Lemma 10.** *If $L$ can be solved in time $t(n)$ with $s(n)$ clauses, then $L_0$ can be solved in time $O(t(n) + s(n))$ and $s(n)$ clauses.*

[p. 28] *Proof.* We show that a random instance of $\mathcal{C}_0$ can be transformed to a random instance of $\mathcal{C}$ in time $s(n)O(k)$ by independently transforming every clause $C$ in $\mathcal{C}_0$ to a clause $C'$ in $\mathcal{C}$ such that $C$ is satisfied in the original CSP $\mathcal{C}_0$ with some assignment $\mathbf{t}$ to $\mathbf{x}$ if and only if the corresponding clause $C'$ in $\mathcal{C}$ is satisfied with the same assignment $\mathbf{t}$ to $\mathbf{x}$. For every $\mathbf{y} \in \{0, 1\}^m$ we pre-compute and store a random solution of the system $\mathbf{y} = \mathbf{A}\mathbf{v} \mod 2$, let the solution be $v(\mathbf{y})$.

Given any clause $C = (x_1, x_2, \ldots, x_k)$ in $\mathcal{C}_0$, choose $\mathbf{y} \in \{0, 1\}^m$ uniformly at random. We generate a clause $C' = (x'_1, x'_2, \ldots, x'_k)$ in $\mathcal{C}$ from the clause $C$ in $\mathcal{C}_0$ by choosing the literal $x'_i = \bar{x}_i$ if $v_i(\mathbf{y}) = 1$ and $x'_i = x_i$ if $v_i(\mathbf{y}) = 0$. By the linearity of the system, the clause $C'$ is a consistent clause of $\mathcal{C}$ with some assignment $\mathbf{x} = \mathbf{t}$ if and only if the clause $C$ was a consistent clause of $\mathcal{C}_0$ with the same assignment $\mathbf{x} = \mathbf{t}$.

[p. 29] It is next claimed that $C'$ is a randomly generated clause from the distribution $U_k$ if $C$ was drawn from $U_{k,0}$ and is a randomly generated clause from the distribution $Q_{\boldsymbol{\sigma}}$ if $C$ was drawn from $Q_{\boldsymbol{\sigma},0}$. By construction, the label of the clause $\mathbf{y}$ is chosen uniformly at random. Note that choosing a clause uniformly at random from $U_{k,0}$ is equivalent to first uniformly choosing a $k$-tuple of un-negated literals and then choosing a negation pattern for the literals uniformly at random. It is clear that a clause is still uniformly random after adding another negation pattern if it was uniformly random before. Hence, if the original clause $C$ was drawn to the uniform distribution $U_{k,0}$, then $C'$ is distributed according to $U_k$. Similarly, choosing a clause uniformly at random from $Q_{\boldsymbol{\sigma}, \mathbf{y}}$ for some $\mathbf{y}$ is equivalent to first uniformly choosing a $k$-tuple of unnegated literals and then choosing a negation pattern uniformly at random which makes the clause consistent. As the original negation pattern corresponds to a $\mathbf{v}$ randomly chosen from the null space of $\mathbf{A}$, the final negation pattern on adding $v(\mathbf{y})$ corresponds to the negation pattern for a uniformly random chosen solution of $\mathbf{y} = \mathbf{A}\mathbf{v} \mod 2$ for the chosen $\mathbf{y}$. Therefore, the clause $C'$ is a uniformly random chosen clause from $Q_{\boldsymbol{\sigma}, y}$ if $C$ is a uniformly random chosen clause from $Q_{\boldsymbol{\sigma}, 0}$.

Hence if it is possible to distinguish $U_k$ and $Q_{\boldsymbol{\sigma}}^\eta$ for some randomly chosen $\boldsymbol{\sigma} \in \{0, 1\}^n$ with success probability at least 2/3 in time $t(n)$ with $s(n)$ clauses, then it is possible to distinguish between $U_{k,0}$ and $Q_{\boldsymbol{\sigma}, 0}^\eta$ for some randomly chosen $\boldsymbol{\sigma} \in \{0, 1\}^n$ with success probability at least 2/3 in time $t(n) + s(n)O(k)$ with $s(n)$ clauses. $\square$

## B.5 Proof of Lemma 12 [p. 29–30]

**Lemma 12.** *If $L'$ can be solved in time $t(n)$ with $s(n)$ clauses, then $L$ can be solved in time $t(n)$ with $O(s(n))$ clauses. Hence if Conjecture 1 is true then $L'$ cannot be solved in polynomial time with less than $\tilde{\Omega}(n^{\gamma k/2})$ clauses.*

[p. 29–30] *Proof.* Define $E$ to be the event that a clause generated from the distribution $Q_{\boldsymbol{\sigma}}$ of the CSP $\mathcal{C}$ has the property that for all $i$ the $i$th literal belongs to the set $\mathcal{X}_i$; we also refer to this property of the clause as $E$ for notational ease. It is easy to verify that the probability of the event $E$ is $1/k^k$.

We claim that conditioned on the event $E$, the CSP $\mathcal{C}$ and $\mathcal{C}'$ are equivalent. This is verified as follows. Note that for all $\mathbf{y}$, $Q_{\boldsymbol{\sigma}, \mathbf{y}}$ and $Q'_{\boldsymbol{\sigma}, \mathbf{y}}$ are uniform on all consistent clauses. Let $\mathcal{U}$ be the set of all clauses with non-zero probability under $Q_{\boldsymbol{\sigma}, \mathbf{y}}$ and $\mathcal{U}'$ be the set of all clauses with non-zero probability under $Q'_{\boldsymbol{\sigma}, \mathbf{y}}$. Furthermore, for any $\mathbf{v}$ which satisfies the constraint that $\mathbf{y} = \mathbf{A}\mathbf{v} \mod 2$, let $\mathcal{U}(\mathbf{v})$ be the set of clauses $C \in \mathcal{U}$ such that $\boldsymbol{\sigma}(C) = \mathbf{v}$. Similarly, let $\mathcal{U}'(\mathbf{v})$ be the set of clauses $C \in \mathcal{U}'$ such that $\boldsymbol{\sigma}(C) = \mathbf{v}$. Note that the subset of clauses in $\mathcal{U}(\mathbf{v})$ which satisfy $E$ is the same as the set $\mathcal{U}'(\mathbf{v})$. As this holds for every consistent $\mathbf{v}$ and the distributions $Q'_{\boldsymbol{\sigma}, \mathbf{y}}$ and $Q_{\boldsymbol{\sigma}, \mathbf{y}}$ are uniform on all consistent clauses, the distribution of clauses from $Q_{\boldsymbol{\sigma}}$ is identical to the distribution of clauses $Q'_{\boldsymbol{\sigma}}$ conditioned on the event $E$. The equivalence of $U_k$ and $U'_k$ conditioned on $E$ also follows from the same argument.

[p. 29] Note that as the $k$-tuples in $C$ are chosen uniformly at random from satisfying $k$-tuples, with high probability there are $s(n)$ tuples having property $E$ if there are $O(k^k s(n))$ clauses in $\mathcal{C}$. As the problems $L$ and $L'$ are equivalent conditioned on event $E$, if $L'$ can be solved in time $t(n)$ with $s(n)$ clauses, then $L$ can be solved in time $t(n)$ with $O(k^k s(n))$ clauses. From Lemma 10 and Conjecture 1, $L$ cannot be solved in polynomial time with less than $\tilde{\Omega}(n^{\gamma k/2})$ clauses. Hence $L'$ cannot be solved in polynomial time with less than $\tilde{\Omega}(n^{\gamma k/2} / k^k)$ clauses. As $k$ is a constant with respect to $n$, $L'$ cannot be solved in polynomial time with less than $\tilde{\Omega}(n^{\gamma k/2})$ clauses. $\square$
