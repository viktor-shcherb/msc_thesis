# 2 Related work [p. 1-2]

## Probing BERT's linguistic abilities

[p. 1-2] Goldberg (2019) demonstrated that BERT consistently assigns higher scores to the correct verb forms as opposed to the incorrect one in a masked language modeling task, suggesting some ability to model subject-verb agreement.

Jawahar et al. (2019) extended this work to multiple layers and tasks, supporting the claim that BERT's intermediate layers capture rich linguistic information.

Tran et al. (2018) concluded that LSTMs generalize to longer sequences better and are more robust with respect to agreement distractors, compared to Transformers.

Liu et al. (2019) investigated the transferability of contextualized word representations to a number of probing tasks requiring linguistic knowledge. Their findings suggest that (a) the middle layers of Transformer-based architectures are the most transferable to other tasks, and (b) higher layers of Transformers are not as task specific as the ones of RNNs.

Tang et al. (2018) argued that models using self-attention outperform CNN- and RNN-based models on a word sense disambiguation task due to their ability to extract semantic features from text.

Voita et al. (2019) analyzed the original Transformer model on a translation task and found that only a small subset of heads is important for the given task, but these heads have interpretable linguistic functions.

[p. 2] The authors position their work as contributing to this discussion, but rather than examining representations extracted from different layers, they focus on understanding the self-attention mechanism itself, since it is the key feature of Transformer-based models.

## Neural network pruning

[p. 2] Frankle and Carbin (2018) showed that widely used complex architectures suffer from overparameterization and can be significantly reduced in size without a loss in performance.

Goldberg (2019) observed that the smaller version of BERT achieves better scores on a number of syntax-testing experiments than the larger one.

Adhikari et al. (2019) questioned the necessity of computation-heavy neural networks, proving that a simple yet carefully tuned BiLSTM without attention achieves the best or at least competitive results compared to more complex architectures on the document classification task.

Wu et al. (2019) presented more evidence of unnecessary complexity of the self-attention mechanism, and proposed a more lightweight and scalable dynamic convolution-based architecture that outperforms the self-attention baseline.

Michel et al. (2019) demonstrated that some layers in Transformer can be reduced down to a single head without significant degradation of model performance.

These studies suggest a potential direction for future research, and are in good accordance with the authors' observations.
