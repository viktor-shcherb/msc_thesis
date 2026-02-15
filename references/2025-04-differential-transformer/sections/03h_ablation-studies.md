# 3.8 Ablation Studies [p. 10]

The authors conduct ablation studies with 1.4B-size language models [p. 10]. The training setup is the same as the 1.4B model in Section 3.2 [p. 10]. The models have L = 24 layers, h = 16 heads for Transformer, and h = 8 heads for DIFF Transformer [p. 10]. The head dimension is d = 128 [p. 10]. Detailed hyperparameters are described in Appendix E [p. 10].

Table 6 reports fine-grained loss on the validation set [p. 10]. They follow Zoology (Arora et al., 2023) and divide loss into "AR-Hit" and "Others" [p. 10]. Specifically, "AR-Hit" combines slices of an n-gram previously seen in the context, which evaluates the associative recall capability [p. 10]. The "Others" slice represents the tokens that cannot be recalled from the context or frequent tokens [p. 10].

As shown in Table 6, the authors ablate various design choices of DIFF Transformer and present several Transformer variants [p. 10]. Notice that all models have comparable size and training FLOPs for fair comparisons [p. 10]. The first and fourth rows are results of Transformer and DIFF Transformer, respectively, which are directly taken from Figure 3a [p. 10]. Their method outperforms Transformer in terms of both overall and fine-grained loss [p. 10]. As DIFF Transformer halves the number of heads to match model size, the second row shows that the configuration change does not have much impact [p. 10]. They ablate GroupNorm from DIFF Transformer, which degrades performance due to training instability [p. 10]. Because multiple heads tend to have large variance in their activations, GroupNorm plays a key role in normalizing them to similar values [p. 10]. In contrast, comparing the third and first rows, adding GroupNorm to Transformer has negligible effect on performance [p. 10]. The results indicate that the improvements of their method come from the differential attention mechanism, instead of configurations or normalization modules [p. 10]. Moreover, they compare different initializations [p. 10]. As described in Section 2.1, the default setting uses exponential initialization, i.e., λ_init = 0.8 − 0.6 × exp(−0.3 · (l − 1)), where l is the layer index [p. 10]. The last two rows employ λ_init = 0.8, 0.5 [p. 10]. The minimal change in the validation loss suggests that the models are robust to the choice of λ initialization [p. 10].

| Model | #heads | d | GN | Valid. Set. | Fine-Grained Slices |  |
|-------|--------|---|-----|-------------|----------|----------|
|       |        |   |     |             | AR-Hit↓  | Others↓  |
| Transformer | 16 | 128 | ✗ | 3.087 | 0.898 | 3.272 |
| Transformer | 8 | 256 | ✗ | 3.088 | 0.899 | 3.273 |
| + GroupNorm | 8 | 256 | ✓ | 3.086 | 0.899 | 3.271 |
| DIFF Transformer | 8 | 128 | ✓ | 3.062 | 0.880 | 3.247 |
| − GroupNorm | 8 | 128 | ✗ | 3.122 | 0.911 | 3.309 |
| with λ_init = 0.8 | 8 | 128 | ✓ | 3.065 | 0.883 | 3.250 |
| with λ_init = 0.5 | 8 | 128 | ✓ | 3.066 | 0.882 | 3.251 |

Table 6: Ablation studies of 1.4B-size models [p. 10]. They report language modeling loss on the validation set [p. 10]. They also follow Arora et al. (2023) to report fine-grained metrics, where "AR-Hit" evaluates n-grams previously seen in the context [p. 10]. "#Heads" is number of heads [p. 10]. "d" is head dimension [p. 10]. "GN" indicates whether GroupNorm is used [p. 10].
