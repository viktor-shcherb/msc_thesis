# B. Details of Model Training [p. 43]

[p. 43] All versions of GPT-3 are trained using Adam with the following hyperparameters:

- beta_1 = 0.9
- beta_2 = 0.95
- epsilon = 10^{-8}
- Global norm of gradient clipped at 1.0
- Cosine decay for learning rate down to 10% of its value, over 260 billion tokens (after 260 billion tokens, training continues at 10% of the original learning rate)
- Linear LR warmup over the first 375 million tokens
- Batch size gradually increased linearly from a small value (32k tokens) to the full value over the first 4-12 billion tokens of training, depending on the model size
- Data sampled without replacement during training (until an epoch boundary is reached) to minimize overfitting
- Weight decay of 0.1 for all models to provide a small amount of regularization [LH17]

During training, the models always train on sequences of the full n_{ctx} = 2048 token context window, packing multiple documents into a single sequence when documents are shorter than 2048, in order to increase computational efficiency. Sequences with multiple documents are not masked in any special way but instead documents within a sequence are delimited with a special end of text token, giving the language model the information necessary to infer that context separated by the end of text token is unrelated. This allows for efficient training without need for any special sequence-specific masking.
