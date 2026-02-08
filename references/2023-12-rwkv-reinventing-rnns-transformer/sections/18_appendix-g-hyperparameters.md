# G Hyperparameters [p. 19]

[p. 19]

To train the models mentioned, we use $\epsilon = (0.9, 0.99)$ without weight decay for the Adam optimizer, and switch batch size dynamically between 128 or 256 sequences, each of 1024 tokens. The training is further organized into multiple mini-epochs, each of 40320 samples, to guide the learning rate schedule. The training process takes 8043 mini-epochs to make one pass over the Pile. The initial warming up mini-epochs have a constant learning rate of "Init LR". After the warming up mini-epochs, the learning rate exponentially decays until the last mini-epoch, in which the model finishes training on the entire Pile, the learning rate arrives at the "End LR". The related hyperparameters are shown in Table 3.

**Table 3:** Hyperparameters for our learning rate (LR) schedule of the pretrained models. [p. 19]

| Model             | 169M    | 430M    | 1.5B    | 3B      | 7B      | 14B      |
|-------------------|---------|---------|---------|---------|---------|----------|
| Init LR           | 0.0006  | 0.0004  | 0.0003  | 0.00015 | 0.00015 | 0.0001   |
| Warmup Mini-Epochs| 361     | 411     | 443     | 451     | 465     | 544      |
| End LR            | 0.00001 | 0.00001 | 0.00001 | 0.00001 | 0.00001 | 0.000007 |
