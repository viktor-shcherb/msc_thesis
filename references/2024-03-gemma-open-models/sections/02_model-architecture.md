# Model Architecture [p. 2-3]

The Gemma model architecture is based on the transformer decoder (Vaswani et al., 2017). The core parameters are summarized in Table 1. Models are trained on a context length of 8192 tokens. [p. 2]

**Table 1** (p. 2): Key model parameters.

| Parameters             | 2B     | 7B     |
|------------------------|--------|--------|
| d_model                | 2048   | 3072   |
| Layers                 | 18     | 28     |
| Feedforward hidden dims| 32768  | 49152  |
| Num heads              | 8      | 16     |
| Num KV heads           | 1      | 16     |
| Head size              | 256    | 256    |
| Vocab size             | 256128 | 256128 |

Several improvements proposed after the original transformer paper are utilized: [p. 2]

## Multi-Query Attention

(Shazeer, 2019). The 7B model uses multi-head attention while the 2B checkpoints use multi-query attention (with *num_kv_heads* = 1), based on ablations that showed that multi-query attention works well at small scales (Shazeer, 2019). [p. 2]

## RoPE Embeddings

(Su et al., 2021). Rather than using absolute positional embeddings, rotary positional embeddings are used in each layer; embeddings are also shared across inputs and outputs to reduce model size. [p. 2]

## GeGLU Activations

(Shazeer, 2020). The standard ReLU non-linearity is replaced by the approximated version of the GeGLU activation function. [p. 2-3]

## RMSNorm

The input of each transformer sub-layer, the attention layer and the feedforward layer, is normalized with RMSNorm (Zhang and Sennrich, 2019) to stabilize the training. [p. 3]

**Table 2** (p. 3): Parameter counts for the Gemma models. The large Gemini vocabulary (256k entries) is designed to work on large quantities of languages, hence the larger embedding parameter counts compared to models limited to one or a few languages.

| Model | Embedding Parameters | Non-embedding Parameters |
|-------|---------------------|-------------------------|
| 2B    | 524,550,144         | 1,981,884,416           |
| 7B    | 786,825,216         | 7,751,248,896           |
