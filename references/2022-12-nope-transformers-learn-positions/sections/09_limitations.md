# 9 Limitations [p. 6]

[p. 6] The work explores language models in the 125M to 1.3B parameter range. The authors show that as parameter count increases the gap between the NoPos method and the other position methods narrows. This trend leads them to believe that their findings should hold for even larger models, but the current biggest models are more than one hundred times bigger (in terms of parameters) than the 1.3B parameter models, and so the results in that setting can be unexpected.

Additionally, training models at the 1.3B parameter scale is resource-intensive and might hinder reproducibility. They therefore release their trained models.

When comparing the perplexity of NoPos to other models, although the margins are very small, NoPos is always slightly worse, suggesting that the inductive bias of positional encoding is indeed important.
