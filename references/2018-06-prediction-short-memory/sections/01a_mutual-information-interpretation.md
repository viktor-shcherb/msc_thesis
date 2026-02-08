# 1.1 Interpretation of Mutual Information of Past and Future [p. 3]

[p. 3] While the mutual information between past and future observations is an intuitive parameterization of the complexity of a distribution over sequences, the fact that it is the *right* quantity is subtle. The authors note it is tempting to think mutual information is a bound on the amount of memory needed to store all information about past observations relevant to the distribution of future observations. This is *not* the case.

To illustrate: given a joint distribution over random variables $X_{\text{past}}$ and $X_{\text{future}}$, suppose we wish to define a function $f$ that maps $X_{\text{past}}$ to a binary "advice"/memory string $f(X_{\text{past}})$, possibly of variable length, such that $X_{\text{future}}$ is independent of $X_{\text{past}}$ given $f(X_{\text{past}})$. As shown in Harsha et al. [14], there are joint distributions over $(X_{\text{past}}, X_{\text{future}})$ such that even on average, the minimum length of the advice/memory string necessary for this task is exponential in the mutual information $I(X_{\text{past}}; X_{\text{future}})$.

This setting can also be interpreted as a two-player communication game where one player generates $X_{\text{past}}$ and the other generates $X_{\text{future}}$ given limited communication (i.e., the ability to communicate $f(X_{\text{past}})$).

Footnote 2: If the advice/memory string $s$ is sampled first, and then $X_{\text{past}}$ and $X_{\text{future}}$ are defined to be random functions of $s$, then the length of $s$ *can* be related to $I(X_{\text{past}}; X_{\text{future}})$ (see [14]). This latter setting (where $s$ is generated first) corresponds to allowing shared randomness in the two-player communication game; however, this is not relevant to the sequential prediction problem. [p. 3]

Given that mutual information is not even an upper bound on the memory an optimal algorithm (computationally unbounded, with complete knowledge of the distribution) would require, Proposition 1 might be surprising.
