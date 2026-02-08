# 4.3 Relative Effective Context Length [p. 8-9]

Khandelwal et al. (2018) proposed a method to evaluate the *Effective Context Length* (ECL) of a sequence model. ECL is the longest length to which increasing the context span would lead to a gain more than a threshold. However, ECL ignores the fact that it is harder to get improvement when a model already achieves a lower perplexity using only a shorter context, and thus it is not suitable for fair comparison among multiple models. [p. 8]

The authors propose a new metric called *Relative Effective Context Length* (RECL). RECL is defined on a *model group* instead of a single model, and the gain of a long context is measured by the relative improvement over the *best* short context model. As such, the model group shares the same baseline to enable fair comparison. RECL also has a parameter r, which means constraining the comparison on top-r hard examples. See Appendix C for more details about RECL. [p. 8-9]

As shown in Table 8, Transformer-XL manages to model dependency of 900 words long on average with r = 0.1. The RECL of Transformer-XL is 80% and 450% longer than recurrent networks and Transformer respectively. Both the recurrence mechanism and the positional encodings contribute to a longer RECL. This further substantiates the argument that Transformer-XL is able to model longer-term dependency. [p. 9]

**Table 8** (p. 9): Relative effective context length (RECL) comparison. See text for the definition of RECL and r. The first three models and the last four models are compared as two *model groups* when calculating RECL (RECL is computed on a model group rather than a single model). Each group has the same parameter budget.

| Model | r = 0.1 | r = 0.5 | r = 1.0 |
|---|---|---|---|
| Transformer-XL 151M | **900** | **800** | **700** |
| QRNN | 500 | 400 | 300 |
| LSTM | 400 | 300 | 200 |
| Transformer-XL 128M | **700** | **600** | **500** |
| - use Shaw et al. (2018) encoding | 400 | 400 | 300 |
| - remove recurrence | 300 | 300 | 300 |
| Transformer | 128 | 128 | 128 |
