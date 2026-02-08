# B Additional Pruning Experiments [p. 12-13]

[p. 12] Additional results for the importance-driven pruning approach from Section 4 on 4 additional datasets:

- **SST-2**: The GLUE version of the Stanford Sentiment Treebank (Socher et al., 2013). A fine-tuned BERT is used as the model.
- **CoLA**: The GLUE version of the Corpus of Linguistic Acceptability (Warstadt et al., 2018). A fine-tuned BERT is used as the model.
- **MRPC**: The GLUE version of the Microsoft Research Paraphrase Corpus (Dolan and Brockett, 2005). A fine-tuned BERT is used as the model.
- **IWSLT**: The German to English translation dataset from IWSLT 2014 (Cettolo et al., 2015). The same smaller model described in Section 6 is used.

[p. 12] Figure 6 shows that in some cases up to 60% (SST-2) or 50% (CoLA, MRPC) of heads can be pruned without a noticeable impact on performance.

**Figure 6** (p. 13): "Evolution of score by percentage of heads pruned."
- (a) Evolution of accuracy on the validation set of **SST-2** when heads are pruned from BERT according to $I_h$. X-axis: Percentage pruned (0%-100%). Y-axis: Accuracy (0.0-1.0). Accuracy remains approximately flat (~0.92) up to about 60% pruned, then drops sharply, reaching near 0 at 100%.
- (b) Evolution of Matthew's correlation on the validation set of **CoLA** when heads are pruned from BERT according to $I_h$. X-axis: Percentage pruned (0%-100%). Y-axis: Matthew's correlation (0.0-0.6). Correlation remains approximately flat (~0.57) up to about 50% pruned, then drops sharply, reaching near 0 at ~80-90%.
- (c) Evolution of F-1 score on the validation set of **MRPC** when heads are pruned from BERT according to $I_h$. X-axis: Percentage pruned (0%-100%). Y-axis: F-1 (0.0-1.0). F-1 remains approximately flat (~0.88) up to about 50% pruned, then drops, reaching near 0 at 100%.
- (d) Evolution of the BLEU score of the **IWSLT** model when heads are pruned according to $I_h$ (solid blue). X-axis: Percentage pruned (0%-100%). Y-axis: BLEU (0-35). BLEU remains approximately flat (~33) up to about 20% pruned, then gradually declines, with a sharper drop after ~60%, reaching near 0 at 100%.
