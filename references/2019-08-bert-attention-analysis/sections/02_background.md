# 2 Background: Transformers and BERT [p. 2]

Although the analysis methods are applicable to any model with an attention mechanism, this paper analyzes BERT (Devlin et al., 2019), a large Transformer (Vaswani et al., 2017) network. [p. 2]

## Transformer attention mechanism

Transformers consist of multiple layers where each layer contains multiple attention heads. An attention head takes as input a sequence of vectors h = [h_1, ..., h_n] corresponding to the n tokens of the input sentence. Each vector h_i is transformed into query, key, and value vectors q_i, k_i, v_i through separate linear transformations. [p. 2]

The head computes attention weights alpha between all pairs of words as softmax-normalized dot products between query and key vectors. The output o of the attention head is a weighted sum of the value vectors: [p. 2]

$$\alpha_{ij} = \frac{\exp(q_i^T k_j)}{\sum_{l=1}^{n} \exp(q_i^T k_l)} \qquad o_i = \sum_{j=1}^{n} \alpha_{ij} v_j$$

- alpha_{ij}: attention weight from token i to token j
- o_i: output of the attention head for token i

Attention weights can be viewed as governing how "important" every other token is when producing the next representation for the current token. [p. 2]

## BERT specifics

- Pre-trained on 3.3 billion tokens of English text. [p. 2]
- Two pre-training tasks: [p. 2]
  1. **Masked language modeling:** the model predicts the identities of words that have been masked out of the input text.
  2. **Next sentence prediction:** the model predicts whether the second half of the input follows the first half in the corpus, or is a random paragraph.
- Fine-tuning on supervised data yields impressive performance on tasks ranging from sentiment analysis to question answering. [p. 2]
- Preprocessing: a special token [CLS] is added to the beginning of the text and another token [SEP] is added to the end. If the input consists of multiple separate texts (e.g., a reading comprehension example with a question and context), [SEP] tokens also separate them. [p. 2]
- The authors use the "base" sized BERT model: 12 layers, 12 attention heads each (144 total heads). [p. 2]
- Notation: <layer>-<head_number> denotes a particular attention head. [p. 2]
