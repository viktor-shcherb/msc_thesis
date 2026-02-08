# A Hyperparameter settings [p. 12]

They train a vanilla LSTM language model, augmented with dropout on recurrent connections, embedding weights, and all input and output connections (Wan et al., 2013; Gal and Ghahramani, 2016), weight tying between the word embedding and softmax layers (Inan et al., 2017; Press and Wolf, 2017), variable length backpropagation sequences and the averaging SGD optimizer (Merity et al., 2018). Key hyperparameter settings are provided in Table 2. These are the default settings suggested by Merity et al. (2018). [p. 12]

## Table 2: Hyperparameter Settings [p. 12]

| Hyperparameter      | PTB              | Wiki             |
|---------------------|------------------|------------------|
| Word Emb. Size      | 400              | 400              |
| Hidden State Dim    | 1150             | 1150             |
| Layers              | 3                | 3                |
| Optimizer           | ASGD             | ASGD             |
| Learning Rate       | 30               | 30               |
| Gradient clip       | 0.25             | 0.25             |
| Epochs (train)      | 500              | 750              |
| Epochs (finetune)   | 500 (max)        | 750 (max)        |
| Batch Size          | 20               | 80               |
| Sequence Length      | 70               | 70               |
| LSTM Layer Dropout  | 0.25             | 0.2              |
| Recurrent Dropout   | 0.5              | 0.5              |
| Word Emb. Dropout   | 0.4              | 0.65             |
| Word Dropout        | 0.1              | 0.1              |
| FF Layers Dropout   | 0.4              | 0.4              |
| Weight Decay        | 1.2 x 10^-6      | 1.2 x 10^-6      |
