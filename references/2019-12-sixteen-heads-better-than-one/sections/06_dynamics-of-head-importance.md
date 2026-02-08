# 6 Dynamics of Head Importance during Training [p. 8]

Previous sections established that some heads are more important than others in *trained* models. To get more insight into the dynamics of head importance *during training*, the authors perform the same incremental pruning experiment of Section 4.2 at every epoch.

## Experimental setup

This experiment is performed on a smaller version of the WMT model (6 layers and 8 heads per layer), trained for German to English translation on the smaller IWSLT 2014 dataset (Cettolo et al., 2015). This model is referred to as **IWSLT**.

## Results

**Figure 5** (p. 8): Relationship between percentage of heads pruned and relative score decrease during training of the IWSLT model.
- **Left side**: X-axis: Epoch (logarithmic scale; 1, 2, 3, 5, 10, 20, 30, 40; un-pruned BLEU score shown in brackets: [3.0], [6.2], [18.1], [26.9], [30.6], [34.5], [34.7], [34.9]). Y-axis: Percentage of un-pruned model BLEU score (0%-100%). Lines for each pruning percentage (0%-90% in 10% increments).
- **Right side**: X-axis: Percentage pruned (0%-100%). Y-axis: Percentage of original BLEU (0%-100%). Lines for Epoch 1, Epoch 2, Epoch 35, Epoch 40.
- Focus: difference in behaviour at the beginning (epochs 1 and 2) and end (epochs 35 and 40) of training.

Two distinct regimes are observed:

1. **Early epochs (especially 1 and 2):** Performance decreases linearly with the pruning percentage, *i.e.* the relative decrease in performance is independent from $I_h$, indicating that most heads are more or less equally important.

2. **From epoch 10 onwards:** There is a concentration of unimportant heads that can be pruned while staying within 85-90% of the original BLEU score (up to 40% of total heads).

This suggests that the important heads are determined early (but not immediately) during the training process. The two phases of training are reminiscent of the analysis by Shwartz-Ziv and Tishby (2017), according to which the training of neural networks decomposes into an "empirical risk minimization" phase, where the model maximizes the mutual information of its intermediate representations with the labels, and a "compression" phase where the mutual information with the input is minimized. A more principled investigation of this phenomenon is left to future work.
