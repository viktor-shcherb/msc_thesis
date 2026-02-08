# 4 Related Work [p. 4-5]

This work is focused on achieving a better tradeoff between decoder quality and inference time through reducing the memory bandwidth overhead (Williams et al., 2009) from loading keys and values. [p. 4]

Shazeer (2019) first proposed reducing this overhead through multi-query attention. Follow-up work showed that multi-query attention is especially helpful for long inputs (Pope et al., 2022; de Jong et al., 2022). Rabe (2023) independently developed GQA with public implementation. Other works have explored grouping attention heads for computational efficiency (Park et al., 2020; Luo et al., 2022; Ni et al., 2023) without focusing specifically on key-value heads, which determine memory bandwidth overhead. [p. 4-5]

A number of other methods have been proposed to reduce memory bandwidth overhead from keys and values, as well as parameters: [p. 5]

- **Flash attention** (Dao et al., 2022): Structures the attention computation to avoid materializing the quadratic attention scores, reducing memory and speeding up training. [p. 5]
- **Quantization** (Dettmers et al., 2022; Frantar et al., 2022): Reduces the size of weights and activations, including keys and values, by lowering precision. [p. 5]
- **Model distillation** (Hinton et al., 2015; Gou et al., 2021): Reduces model size at a given precision, using data generated from the larger model to finetune the smaller model. [p. 5]
- **Layer-sparse cross-attention** (de Jong et al., 2022): Eliminates most cross-attention layers which make up the primary expense for longer inputs. [p. 5]
- **Speculative sampling** (Chen et al., 2023; Leviathan et al., 2022): Ameliorates the memory bandwidth bottleneck by proposing multiple tokens with a smaller model which are then scored in parallel by a larger model. [p. 5]

The uptraining procedure is inspired by Komatsuzaki et al. (2022), which uptrains standard T5 checkpoints into sparsely activated Mixture-of-Experts models. [p. 5]
