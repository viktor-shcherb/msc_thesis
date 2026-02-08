# 5 Training [p. 7-8]

This section describes the training regime for the models.

## 5.1 Training Data and Batching [p. 7]

Training was performed on the standard WMT 2014 English-German dataset consisting of about 4.5 million sentence pairs. Sentences were encoded using byte-pair encoding [3], which has a shared source-target vocabulary of about 37000 tokens. For English-French, the significantly larger WMT 2014 English-French dataset consisting of 36M sentences was used, with tokens split into a 32000 word-piece vocabulary [38]. Sentence pairs were batched together by approximate sequence length. Each training batch contained a set of sentence pairs containing approximately 25000 source tokens and 25000 target tokens. [p. 7]

## 5.2 Hardware and Schedule [p. 7]

Models were trained on one machine with 8 NVIDIA P100 GPUs. For the base models using the hyperparameters described throughout the paper, each training step took about 0.4 seconds. The base models were trained for a total of 100,000 steps or 12 hours. For the big models (described on the bottom line of Table 3), step time was 1.0 seconds. The big models were trained for 300,000 steps (3.5 days). [p. 7]

## 5.3 Optimizer [p. 7-8]

The Adam optimizer [20] was used with beta_1 = 0.9, beta_2 = 0.98, and epsilon = 10^{-9}. The learning rate was varied over the course of training, according to the formula: [p. 7]

**Equation (3):**

lrate = d_model^{-0.5} * min(step_num^{-0.5}, step_num * warmup_steps^{-1.5})

Computes a learning rate schedule that increases linearly for the first warmup_steps training steps, and decreases thereafter proportionally to the inverse square root of the step number. [p. 7-8]

warmup_steps = 4000. [p. 8]

## 5.4 Regularization [p. 8]

Three types of regularization were employed during training: [p. 8]

**Residual Dropout:** Dropout [33] is applied to the output of each sub-layer, before it is added to the sub-layer input and normalized. In addition, dropout is applied to the sums of the embeddings and the positional encodings in both the encoder and decoder stacks. For the base model, a rate of P_drop = 0.1 is used. [p. 8]

**Label Smoothing:** During training, label smoothing of value epsilon_ls = 0.1 [36] was employed. This hurts perplexity, as the model learns to be more unsure, but improves accuracy and BLEU score. [p. 8]
