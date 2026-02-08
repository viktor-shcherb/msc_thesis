# 5 Analysis [p. 4-5]

[p. 4] This section examines whether the NoPos model is able to encode positional information and shows that such information is essential for its success.

## NoPos models acquire positional information

[p. 4] Do NoPos LMs learn some form of positional encoding to compensate for the absence of explicit positional modeling? To answer this question, the authors probe each layer of their trained models for positional information. Specifically, they use the tokens' last hidden representation after each transformer layer, produced by the evaluated LM, and train a 2-layer feed-forward ReLU network to predict the absolute position (0 to 1023) of each token (i.e., as a multiclass classification problem). Notably, they do not change the weights of the evaluated LMs and thus, do not provide any position information of the tokens to the LM in this experiment, which ensures the validity of their findings.

Footnote 4: They used the 1.3B parameter models trained over 1024-token sequences of the Pile (Section 3).

Each layer's probe was trained separately (hyperparameters are provided in App. C). As a soft accuracy metric, they measured the mean absolute distance between the probe's prediction and the token's actual position.

[p. 4] Figure 2 shows that even though the NoPos model starts, as expected, with no positional information in the first layer (on par with a random baseline), it becomes position-aware within four layers and appears to contain more positional information than ALiBi. By the middle layer, NoPos can predict absolute positions about as well as the model with learned positional embeddings. Finally, all models shed off a significant amount of positional information in the final layers, in line with the findings of Voita et al. (2019). Overall, the probe reveals that the NoPos models learn an implicit notion of absolute positions.

**Figure 2** (p. 4): "Through probing, we find that the NoPos model behaves similarly to models that use absolute learned position embeddings. We evaluated performance using mean absolute distance on 1.3B parameter models trained on the Pile."

Line plot with X-axis: Layer (0 to 24), Y-axis: Mean Absolute Distance (0 to ~350). Five lines are shown: NoPos (blue circle), Learned (orange square), Sinusoidal (green square), ALiBi (red triangle), Random (gray dashed). NoPos starts at ~340 (matching Random) at layer 0, drops sharply to ~20 by layer 4, reaches near 0 by middle layers (~12), and rises slightly in final layers (~20-30 at layer 24). Learned stays near 0 across all layers. Sinusoidal starts low and stays near 0. ALiBi starts at ~50 and gradually decreases to near 0 by middle layers. All models show a slight uptick in the final layers. Random baseline stays flat at ~340 throughout.

[p. 4-5] To elucidate what positional information the NoPos model learns, the authors visualize the predictions of the probe. They examine a sample of 100 predictions from the validation set of the best-performing probe trained over the NoPos model. Figure 3 shows the predictions over the 512 token sequences sampled randomly from the validation set and a single example from the same set. They observe that the probe is more accurate at the beginning of the sequence, but becomes fuzzier as it progresses.

**Figure 3** (p. 5): "A visualization of the absolute position predictions of a probe trained over a NoPos language model. The blue line shows the mean of the generated predictions for every target position and the blue area represents the 95%-confidence interval. The predictions for a single random sequence are depicted as green dots."

Scatter/line plot with X-axis: Target Position (0 to 512), Y-axis: Predicted Position (0 to 512). A diagonal dashed gray line represents ground truth (perfect prediction). The blue line (mean predictions) closely follows the ground truth diagonal, with a blue shaded area (95% confidence interval) that widens as target position increases, indicating predictions become fuzzier for later positions. Green dots (single example predictions) scatter around the diagonal, clustering tightly near position 0 and spreading more at higher positions.

## Positional information matters

[p. 5] NoPos is able to infer absolute positions, but are they necessary? The authors answer this using a trained NoPos model. Instead of computing the loss over the entire sequence, they select a single random token, shuffle the previous tokens that it is conditioned on, and compare to a baseline where the prefix remains intact. They find that in the case where the suffix is shuffled, the average token-level loss increases dramatically (from ~4 to ~11). Details of this experiment are given in App. B.

This finding indicates that the NoPos model indeed uses the positional information it acquires, as otherwise similar loss values would be expected in these two settings.
