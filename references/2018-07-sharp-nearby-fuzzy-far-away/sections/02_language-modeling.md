# 2 Language Modeling [p. 2]

Language models assign probabilities to sequences of words. In practice, the probability can be factorized using the chain rule:

$$P(w_1, \ldots, w_t) = \prod_{i=1}^{t} P(w_i | w_{i-1}, \ldots, w_1)$$

Language models compute the conditional probability of a *target word* $w_t$ given its preceding context $w_1, \ldots, w_{t-1}$.

Language models are trained to minimize the negative log likelihood of the training corpus:

$$\text{NLL} = -\frac{1}{T} \sum_{t=1}^{T} \log P(w_t | w_{t-1}, \ldots, w_1)$$

The model's performance is usually evaluated by perplexity (PP) on a held-out set:

$$\text{PP} = \exp(\text{NLL})$$

When testing the effect of ablations, the authors focus on comparing differences in the language model's losses (NLL) on the dev set, which is equivalent to relative improvements in perplexity.
