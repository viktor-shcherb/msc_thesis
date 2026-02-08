# 1 Introduction [p. 1]

[p. 1] Models based on the Transformer architecture (Vaswani et al., 2017) have become the de-facto standard for state-of-the-art performance on many NLP tasks (Radford et al., 2018; Devlin et al., 2018). Their key feature is the self-attention mechanism that provides an alternative to conventionally used recurrent neural networks (RNN).

BERT is one of the most popular Transformer-based models, learning text representations using a bi-directional Transformer encoder pre-trained on the language modeling task (Devlin et al., 2018). BERT-based architectures have produced new state-of-the-art performance on a range of NLP tasks of different nature, domain, and complexity, including question answering, sequence tagging, sentiment analysis, and inference. State-of-the-art performance is usually obtained by fine-tuning the pre-trained model on the specific task. BERT-based models currently dominate leaderboards for SQuAD (Rajpurkar et al., 2016) and GLUE benchmarks (Wang et al., 2018).

The exact mechanisms contributing to BERT's outstanding performance remain unclear. The authors address this through selecting linguistic features of interest and conducting experiments to provide insights about how well these features are captured by BERT.

## Contributions

- Propose a methodology and offer the first detailed analysis of BERT's capacity to capture different kinds of linguistic information by encoding it in its self-attention weights. [p. 1]
- Present evidence of BERT's overparametrization and suggest a counter-intuitive yet simple way of improving its performance, showing absolute gains of up to 3.2%. [p. 1]
