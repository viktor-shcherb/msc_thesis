# 4.5 Token-to-token attention [p. 7]

[p. 7] To complement the experiments in Sec. 4.4 and 4.2, this section investigates the attention patterns between tokens in the same sentence, i.e. whether any of the tokens are particularly important while a *given* token is being processed. The authors were interested specifically in the verb-subject relation and the noun-pronoun relation. Also, since BERT uses the representation of the *[CLS]* token in the last layer to make the prediction, they used the features from the experiment in Sec. 4.4 in order to check if they get higher attention weights while the model is processing the *[CLS]* token.

## Results

[p. 7] The token-to-token attention experiments for detecting heads that prioritize noun-pronoun and verb-subject links resulted in a set of potential head candidates that coincided with diagonally structured attention maps. The authors believe that this happened due to the inherent property of English syntax where the dependent elements frequently appear close to each other, so it is difficult to distinguish such relations from the previous/following token attention coming from language model pre-training.

Investigation of attention distribution for the *[CLS]* token in the output layer suggests that for most tasks, with the exception of STS-B, RTE and QNLI, the *[SEP]* gets attended the most, as shown in Figure 7. Based on manual inspection, for the mentioned remaining tasks (STS-B, RTE, QNLI), the greatest attention weights correspond to the punctuation tokens, which are in a sense similar to *[SEP]*.
