# 2 Approach [p. 2-4]

[p. 2] A **language model** (LM) places a probability distribution p(x) over discrete token sequences x. Most learned LMs decompose p(x) according to the chain rule, modeling the conditional distribution over a single **target token** given a (fixed- or variable-length) **context** of previous tokens:

$$p(x) = \prod_i p(x_i \mid x_0, x_1, \ldots, x_{i-1}) \,. \tag{1}$$

Eq. (1) defines the standard autoregressive factorization of a sequence probability.

In **transformer language models**, this conditional distribution is modeled via a sequence of alternating neural feed-forward layers and self-attention layers; see Vaswani et al. (2017) for more details.

While input sequences x can in principle be made arbitrarily long, there are both theoretical and practical limits to transformers' ability to make effective use of it (Hahn, 2020; Wang et al., 2019).

## Usable information

[p. 2] A motivating example: consider a hypothetical LM context consisting of the tokens *The user's password is...*. This context suggests subsequent tokens will be a password: a high-entropy sequence. If this context is extended to include earlier tokens, becoming *The user's hashed password is ave$@To9!. The user's password is...*, this context is extremely informative information-theoretically: only a small number of passwords will hash to the given string. But in practice, this extra context is useless: no known efficient predictor can learn anything about the password from its hash code, and the extra context has not made the language modeling problem any easier.

[p. 2] A framework for answering questions of this kind was introduced by Xu et al. (2020):

**Definition 1.** The usable predictive information (formally, predictive **V-information**) from a random variable X to a random variable Y as:

$$I_{\mathcal{V}}(X \to Y) = \Big[\inf_{p_1 \in \mathcal{V}} -\mathbb{E} \log p_1(Y)\Big] - \Big[\inf_{p_2 \in \mathcal{V}} -\mathbb{E} \log p_2(Y \mid X)\Big] \tag{2}$$

for a class V of distributions p.

Eq. (2) measures how much extra information about Y can be extracted from X by any predictor in V. In language modeling, Y is the target word, X is its context, and V is a class of parametric models. This definition generalizes Shannon mutual information (Shannon, 1948) and has deep connections to other information-theoretic quantities (see Xu et al. 2020 for details). It ultimately corresponds to a simple evaluation: train a model p_1 without access to X, train a model p_2 with access to X, and compare the accuracy of their predictions.

## Measuring what is used

[p. 2-3] The question is not just *how much* information is contributed by context, but *what* information is actually used by models.

As a prototypical example, the authors hypothesize that more than five tokens away from the target, models are *only* able to extract usable information from nouns. (In the experiments in Section 3, "long-range context" will be considerably longer than 5 words.) For example, given the sentence:

> *Pierre Vinken, 61 years old, will join the board as a nonexecutive director Nov. 29.* [p. 3]

they hypothesize that the LM distributions:

$$p_1(\text{director} \mid \text{Pierre Vinken, 61 years old, will join the board as a nonexecutive}) \tag{3}$$

$$\approx p_2(\text{director} \mid \underbrace{\text{Pierre Vinken years,}}_{\text{noun-only context}} \underbrace{\text{the board as a nonexecutive}}_{\text{ordinary context}}) \,, \tag{4}$$

and more generally that:

$$I_{\mathcal{V}}(X_{0:n} \to X_n) \approx I_{\mathcal{V}}([\text{nouns}(X_{0:n-5}), X_{n-5:n}] \to X_n) \tag{5}$$

where X_{i:j} is the sequence of tokens [X_i, X_{i+1}, \ldots, X_{j-1}], V is a class of LMs, and nouns is a **context ablation** that extracts only the nouns from a given string. The hypothesis is that the amount of usable information contributed by the full context X_{0:n} is the same as the amount contributed by the ablated context [nouns(X_{0:n-5}), X_{n-5:n}], so ablation removes no information.

## Ablated context formalization

[p. 3] The experiments generalize this framework to other context ablations and hypotheses. Let f be an ablation and k an integer offset, and denote an **ablated context**:

$$f_k(X) = [f(X_{0:n-k}), X_{n-k:n}] \tag{6}$$

and an **ablated negative log-likelihood**:

$$\mathcal{L}(\theta, f, k) = -\mathbb{E} \log p_\theta(X_n \mid f_k(X_{0:n})) \tag{7}$$

Then, the effect of each ablation f on usable information can be measured via:

**Definition 2.** The **ablated information** due to an ablation f at an offset k is:

$$\mathcal{A}(f, k) = \frac{I_{\mathcal{V}}(X_{0:n} \to X_n) - I_{\mathcal{V}}(f_k(X_{0:n}) \to X_n)}{I_{\mathcal{V}}(X_{0:n} \to X_n) - I_{\mathcal{V}}(X_{n-k:n} \to X_n)} \tag{8}$$

$$= \frac{\inf_\theta \mathcal{L}(\theta, f, k) - \inf_{\theta'} \mathcal{L}(\theta', n)}{\inf_{\theta''} \mathcal{L}(\theta'', n-k) - \inf_{\theta'} \mathcal{L}(\theta', n)} \,, \tag{9}$$

where L(theta, i) is the (unablated) negative log-likelihood -E log p_theta(X_n | X_{n-i:n}).

Intuitively, A(f, k) measures how much of the usable information *added* by an extra k tokens (the denominator) is *removed* by applying the ablation f to those k tokens (the numerator). If it is close to 0, almost no information is removed; if it is close to 1, almost all information is removed.

## Evaluation in practice

[p. 3] Eq. (9) provides a general framework for answering the paper's core question: for a diverse set of context ablations and offsets, measuring how much information is lost when a given ablation is applied at a given offset. Several modifications are required for practical evaluation:

**Held-out evaluation:** Eq. (7) involves an expectation over the sequence distribution p(X). In practice, LMs must be trained on finite corpora, creating a risk of overfitting (Zhang et al., 2016). The authors approximate the infimum in Eq. (7) by fitting theta_1 on a training set, and computing ablated information on a held-out validation set. All reported results are an average of held-out likelihoods from two random initializations.

**Batching:** Given a fixed (training or test) dataset of strings X and a maximum context size of m, Eq. (7) should be estimated empirically as $-\frac{1}{|\mathcal{X}|} \sum_x \frac{1}{|x|} \sum_{i=0}^{|x|} \log p(X_i \mid f_k(X_{i-m:i}))$. This requires re-computing model predictions once for every token in the dataset. However, the transformer models used here support efficient **batch inference**: training data is pre-segmented into sequences of at most length n, and $-\frac{1}{|\mathcal{X}|n} \sum_x \sum_{i=0}^{n} \log p(X_i \mid f_k(X_{0:i}))$ can be computed in a single forward pass. This is considerably more efficient but means that most tokens are evaluated with a context of length < n. As a compromise to ensure evaluations contain long-range context, losses are accumulated on a subset:

$$\mathcal{L}(\theta, f, \ell : m \sim n) = -\frac{1}{|\mathcal{X}|(n - m)} \sum_x \sum_{i=\ell+m}^{\ell+n} \log p_\theta(X_i \mid [f(X_{0:\ell}), X_{\ell:i}]) \tag{10}$$

(visualized in Fig. 1). This can be read as "ell tokens of f-ablated context, followed by m to n tokens of unablated context". The authors write L(theta, m ~ n) when only unablated context is used.

**Figure 1** (p. 3): "Calculation of the ablated likelihood L(nouns, ell : m ~ n) (Eq. (10)). A context ablation nouns (which deletes all non-noun words) is applied to the first ell tokens of the context, and likelihood is computed on the last n - m (unablated) context tokens."
- The figure shows a transformer LM receiving a sequence of tokens from a sentence about Pierre Vinken. The first ell tokens are labeled "ablated context" (showing noun-only words: "Pierre Vinken years"), followed by tokens from position ell + m to ell + n labeled "ordered context". The output at the top shows the ablated likelihood computation A(nouns, ell : m ~ n) predicting tokens like "a director Nov".
