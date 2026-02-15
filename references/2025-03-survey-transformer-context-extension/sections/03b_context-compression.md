# 3.2 Context Compression [p. 4]

Existing work proposes compressing the long input sequence into a shorter one for representation. These methods can be categorized into two main types by the compression granularity: soft compression and hard compression [p. 4].

## 3.2.1 Soft Compression [p. 4]

In order to shorten the sequence length, the soft compression method uses the model to compress the original input token sequence into a shorter summary token sequence [p. 4].

These summary tokens are soft tokens which act as compression representation but do not correspond to words with actual meaning. They are inserted into the original token sequence to form a new input. During the forward pass of the model, the information from the original token sequence is gathered into the summary token sequence, which represents the original input for subsequent operations [p. 4].

Since summary tokens do not appear during the model's pre-training, additional training is necessary for the model to learn how to generate and utilize these tokens (Bulatov et al., 2022; Li et al., 2023b; Chevalier et al., 2023; Ge et al., 2023; Mu et al., 2024b) [p. 4].

This method can shorten the length of the hidden vector sequence, so that enabling it to be processed within the model's pre-trained window [p. 4].

## 3.2.2 Hard Compression [p. 4]

This method utilizes some techniques to directly shorten plain text sequence length. This process can be achieved through selection and summarization. It doesn't introduce additional tokens and targeted training, which makes it can be applied to some black box models (Jiang et al., 2023, 2024b; Chen et al., 2023a) [p. 4].
