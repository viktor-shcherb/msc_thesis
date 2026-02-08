# 1.4 Future Directions [p. 6-7]

## Re-examining average error as a metric

[p. 6] For settings where capturing long-range dependencies seems essential, the authors suggest re-examining the choice of "average prediction error" as the metric used to train and evaluate models. One possibility with a more worst-case flavor is to only evaluate the algorithm at a chosen set of time steps instead of all time steps. The naive Markov model can no longer do well just by predicting well on the time steps when prediction is easy.

In the context of natural language processing, learning with respect to such a metric intuitively corresponds to training a model to do well on, say, a question answering task instead of a language modeling task. A potential middle ground between average error (which gives too much reward for correctly guessing common words like "a" and "the") and worst-case error might be a re-weighted prediction error that provides more reward for correctly guessing less common observations. The techniques used to prove Proposition 1 seem extensible to yield analogous statements for such error metrics.

## Robustness as additional structure

[p. 6-7] Given the upper bounds of Proposition 1, it is natural to consider what additional structure might avoid the (conditional) computational lower bounds of Theorem 2. One possibility is a *robustness* property -- the property that a Markov model would continue to predict well even when each observation were obscured or corrupted with some small probability. The lower bound instances rely on parity-based constructions and hence are very sensitive to noise and corruptions.

For learning over *product* distributions, there are well-known connections between noise stability and approximation by low-degree polynomials [23, 24]. Additionally, low-degree polynomials can be learned agnostically over *arbitrary* distributions via polynomial regression [25]. The authors suggest establishing a connection between natural notions of noise stability over arbitrary distributions and accurate low-degree polynomial approximations could lead to significantly better sample complexity requirements for prediction on such "robust" distributions of sequences, perhaps requiring only poly($d$, $I(\mathcal{M})$, $1/\epsilon$) data. Such sample-efficient approaches to learning succinct representations of large Markov models may also inform the many practical prediction systems that currently rely on Markov models.
