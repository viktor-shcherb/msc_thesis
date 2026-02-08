# 5 MATH-QWEN: Specialized Model for Mathematics Reasoning [p. 17]

[p. 17] A mathematics-specialized model series called MATH-QWEN-CHAT has been created, built on top of the QWEN pretrained language models. Specifically, assistant models have been developed that are specifically designed to excel in arithmetic and mathematics and are aligned with human behavior. Two versions of this model series are released: MATH-QWEN-14B-CHAT and MATH-QWEN-7B-CHAT, which have 14 billion and 7 billion parameters, respectively.

## 5.1 Training [p. 17, 20]

[p. 17] Math SFT is carried out on an augmented math instructional dataset for mathematics reasoning, and therefore the chat model, MATH-QWEN-CHAT, is obtained directly. Owing to shorter average lengths of the math SFT data, a sequence length of 1024 is used for faster training. Most user inputs in the math SFT dataset are examination questions, and it is easy for the model to predict the input format and it is meaningless for the model to predict the input condition and numbers which could be random. Thus, the inputs of the system and user are masked to avoid loss computation on them, and it is found that masking them accelerates the convergence during preliminary experiments.

[p. 20] For optimization, the AdamW optimizer is used with the same hyperparameters of SFT except that a peak learning rate of 2 x 10^{-5} and a training step of 50,000 are used.
