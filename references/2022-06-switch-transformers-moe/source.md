# Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity

**Authors:** William Fedus, Barret Zoph, Noam Shazeer
**Affiliation:** Google Brain

## Publication Status

- **arXiv preprint:** January 2021, arXiv:2101.03961
- **Peer-reviewed:** Yes
- **Conference/Journal:** Journal of Machine Learning Research, Volume 23, Issue 120, Pages 1-39, 2022
- **Status:** Published journal paper

The paper introduces Switch Transformers, a simplified Mixture of Experts architecture that routes each token to a single expert instead of multiple experts as in prior MoE work. This simplification dramatically reduces computational and communication costs while enabling scaling to trillion-parameter models.

## Preferred Citation

Cite the JMLR 2022 version:

> Fedus, W., Zoph, B., & Shazeer, N. (2022). Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity. Journal of Machine Learning Research, 23(120):1-39.

## Links

- arXiv: https://arxiv.org/abs/2101.03961
- JMLR: https://jmlr.org/papers/v23/21-0998.html
- Code: https://github.com/google-research/t5x (T5X framework)
