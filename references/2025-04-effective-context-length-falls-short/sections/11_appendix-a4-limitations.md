# A.4 Limitations [p. 18-19]

[p. 18-19]

## Pretraining Length Constraint [p. 18]

One limitation of this work is that it only investigates pretraining lengths smaller than 4K tokens, while the question of how to effectively implement long-context training remains an open open. The open-source community's approaches to this problem remains diverse (Hu et al., 2024; Fu et al., 2024b; An et al., 2024a; Jin et al., 2024). For companies, Llama3.1 (Llama Team, 2024) reported using a 6-stage training approach to gradually implement long-context training, but this makes it difficult to analyze position frequencies because the data distribution used in each stage is unknown.

## Training Data Distribution Considerations [p. 18]

STRING achieves surprising results by only using frequent position during inference. It is clear that there are many ways to adjust the distribution of frequent positions during training, but this may require data with a distribution similar to the Llama training corpus to avoid the model losing its reasoning ability. A key feature of STRING is that it can be easily applied to all existing models without requiring the collection of high-quality data for training. We leave the problem of addressing the left-skewed distribution from a training perspective as a future work.
