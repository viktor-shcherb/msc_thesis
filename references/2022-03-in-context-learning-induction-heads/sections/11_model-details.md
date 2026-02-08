# Model Details [p. 39-40]

## Small Models [p. 39]

The small models are 1- through 6-layer Transformers. These include models both with MLPs and without MLPs (i.e. "attention only" models). They have a context window of 8192 tokens, a 2^16 token vocabulary, an activation dimension $d_{\text{model}} = 768$, and 12 attention heads per layer regardless of total model size. They were trained for 10,000 steps (~10 billion tokens), saving 200 snapshots at intervals of every 50 steps. Their positional embeddings are implemented with a variant on the standard positional embeddings (similar to Press *et al.* [17]). The training dataset is described earlier at the start of the Model Analysis Table. [p. 39]

### Phase change and hyperparameter schedules [p. 39]

A "phase change" phenomenon appears at approximately 1-3 billion tokens in the small models. It might be reasonable to ask whether these phenomena are driven by scheduled changes to the hyperparameters, such as learning rate or weight decay. Weight decay was reduced at 4750 steps (approximately 5 billion tokens), the effects of which can be seen as a slight deviation about halfway through the displayed loss curves, occurring at the exact same point for all models; this is not related to the phase change, as this step number is notably beyond the range in which the phase change occurs. The only other hyperparameter change that occurs within the range of the phase change is the learning rate warm-up, which ramps up over the first 1.5e9 tokens. [p. 39]

## Full-Scale Models [p. 39-40]

The "full-scale models" are from the same set of models as described in Askell *et al.* [18]. The context window and vocabulary size are the same as the small models (that is, 8192 tokens and 2^16 tokens respectively). Unlike the small models, their dimensions are adjusted to scale up with increasing size, with an activation dimension $d_{\text{model}} = 128 * n_{\text{layer}}$, and a varying number of attention heads (See Appendix for full details). The models have both dense and local attention heads. In a local attention head, each token may only attend to earlier tokens within a fixed window of relative positions. Dense heads are the standard head, where a token may attend to *any* earlier token (including itself). The training dataset is described earlier at the start of the Model Analysis Table. [p. 39-40]

### Snapshot schedule [p. 40]

Snapshots from these models were saved at exponential step numbers, at an interval of 2x. For the analyses, the authors use snapshots at steps from 2^5 through 2^17, plus one or two final saves thereafter, for a total of 15 saved snapshots (except the 40L which has 14 saved snapshots).^26 This corresponds to a consistent number of tokens across all models up through 2^11 steps (= 2.15E+09 tokens), after which adjustments to the training schedule cause the number of tokens per step to increase for the 24L and 40L models. [p. 40]

### Table of Model Properties for Full-Scale Models [p. 40]

| $n_{\text{layer}}$ | Non-embedding parameter counts | Activation dimension $d_{\text{model}} = 128 * n_{\text{layer}}$ | Attention heads per layer | Attention dimension $d_{\text{head}}$ |
|---|---|---|---|---|
| 4 | 13M | 512 | 8 | 64 |
| 6 | 42M | 768 | 12 | 64 |
| 10 | 200M | 1280 | 20 | 64 |
| 16 | 810M | 2048 | 32 | 64 |
| 24 | 2.7B | 3072 | 48 | 64 |
| 40 | 13B | 5120 | 40 | 128 |

Note: All models have $d_{\text{head}} = 64$ except the 40-layer model which has $d_{\text{head}} = 128$. [p. 40]

## Smeared Key Models [p. 40]

The "smeared key" architecture modification described in Argument 2 is as follows: a trainable real parameter $\alpha$ is introduced, used as $\sigma(\alpha) \in [0, 1]$, that interpolates between the key for the current token and previous token: [p. 40]

$$k_j = \sigma(\alpha) k_j + (1 - \sigma(\alpha)) k_{j-1}$$

(In the case of the very first token in the context, no interpolation happens). These models were otherwise proportioned and trained exactly the same as the small models. They are presented only at one-layer and two-layer sizes. [p. 40]
