# D Experimental Details [p. 50–52]

## D.1 MQAR Details

[p. 50] A harder version of the task introduced in Based (Arora, Eyuboglu, Zhang, et al. 2024) is used, where tokens that are not query/key/values are replaced with random tokens. More key-value pairs, longer sequences, and smaller model sizes than the usual variant of MQAR used by prior work are also used, all of which make the task harder.

- Sequence lengths: $T \in \{256, 512, 1024\}$, using $T/4$ key-value pairs
- Total vocab size: 8192
- Curriculum training: cycles through datasets using $(T/32, T/16, T/8, T/4)$ key-value pairs, where each dataset has $2^{18} \approx 250000$ examples, for a total of 8 epochs through each dataset (total of $2^{28} \approx 270M$ examples)
- Total batch size: $2^{18} \approx 0.25M$ tokens (e.g. for $T = 1024$, the batch size is 256)
- All methods use 2 layers with default settings; the attention baseline additionally receives positional embeddings
- Model dimensions: $D = \{32, 64, 128, 256\}$
- Learning rates: $\{10^{-3.5}, 10^{-2}, 10^{-2.5}\}$
- Linear decay schedule that drops on every epoch (e.g. the last epoch would have a learning rate $1/8$ of the maximum/starting learning rate)

## D.2 Scaling Law Details

[p. 50] All models were trained on the Pile. The GPT2 tokenizer is used for the scaling law experiments.

**Model Sizes.** Table 9 specifies the model sizes used for scaling experiments following GPT3 (Brown et al. 2020). Two changes from the original GPT3 recipe were made: First, the batch size of the 1.3B model was changed from 1M tokens to 0.5M tokens for uniformity. Second, the number of training steps and total tokens were changed to roughly match Chinchilla scaling laws (Hoffmann et al. 2022), which specify that training tokens should increase proportionally to model size.

**Table 9:** (**Scaling Law Model Sizes.**) Model sizes and hyperparameters for scaling experiments. (Model dimension and number of heads applies only to Transformer models.)

| Params | n_layers | d_model | n_heads / d_head | Training steps | Learning Rate | Batch Size | Tokens |
|--------|----------|---------|-------------------|----------------|---------------|------------|--------|
| 125M   | 12       | 768     | 12 / 64           | 4800           | 6e-4          | 0.5M tokens | 2.5B |
| 350M   | 24       | 1024    | 16 / 64           | 13500          | 3e-4          | 0.5M tokens | 7B   |
| 760M   | 24       | 1536    | 16 / 96           | 29000          | 2.5e-4        | 0.5M tokens | 15B  |
| 1.3B   | 24       | 2048    | 32 / 64           | 50000          | 2e-4          | 0.5M tokens | 26B  |

[p. 51] By default, the peak learning rate is the GPT3 specification.

**Training Recipes.** All models used the AdamW optimizer with:
- gradient clip value 1.0
- weight decay 0.1
- no dropout

Compared to the GPT3 recipe, an "improved recipe" is used, inspired by changes adopted by popular large language models such as PaLM (Chowdhery et al. 2023) and LLaMA (Touvron, Lavril, et al. 2023). These include:
- linear learning rate warmup with cosine decay to $1e-5$, with a peak value of $5\times$ the GPT3 value
- no linear bias terms
- RMSNorm instead of LayerNorm
- AdamW hyperparameter $\beta = (.9, .95)$ (the GPT3 value) instead of the PyTorch default of $\beta = (.9, .999)$

## D.3 Downstream Evaluation Details

[p. 51] To evaluate downstream performance of fully trained models, Mamba-2 is trained on 300B tokens on the Pile, using the GPT-NeoX (Black et al. 2022) tokenizer.

The same hyperparameters as the scaling experiments are used, except with batch size 1M for the 1.3B and 2.7B model. For the 2.7B model, the GPT3 specification is also followed (32 layers, dimension 2560).

For all models, $5\times$ the learning rate of the corresponding GPT3 model is used.

For downstream evaluation, the LM evaluation harness from EleutherAI (L. Gao, Tow, et al. 2021) is used, on the same tasks as Mamba (Gu and Dao 2023) with one additional one:
- LAMBADA (Paperno et al. 2016)
- HellaSwag (Zellers et al. 2019)
- PIQA (Bisk et al. 2020)
- ARC-challenge (P. Clark et al. 2018)
- ARC-easy: an easy subset of ARC-challenge
- WinoGrande (Sakaguchi et al. 2021)
- OpenBookQA (Mihaylov et al. 2018)

## D.4 Ablation Details

[p. 51] **(Re)Based Details.** The ablations in Section 9.4.3 considered the Based (Arora, Eyuboglu, Zhang, et al. 2024) and ReBased (Aksenov et al. 2024) models.

Based approximates the exp kernel with a quadratic Taylor expansion $\exp(x) \approx 1 + x + x^2/2$, which can be accomplished by the feature map

$$\psi_{\text{Taylor}}(x) = \text{concatenate}(1, x, 1/\sqrt{2} x \otimes x).$$

ReBased proposes to use the simpler feature map $\psi_{\text{Quadratic}}(x) = x \otimes x$ corresponding to the kernel transformation $x^2$, but also applies a layer normalization beforehand. The layer normalization is viewed as an alternative non-linear activation to the default Swish activation, and combinations of these are ablated.

[p. 52] Note that because these expand the feature dimension, projection to smaller $B, C$ dimensions is needed; in Table 7, state size $N = 64$ for 130M models and $N = 256$ for 380M models. For the (Re)Based methods, projection is to 8 and 16 dimensions respectively before applying their feature maps; this results in a total state size of $8^2 = 64$ for ReBased and $1 + 8 + 8^2 = 73$ for Based in the 130M model case. Because the $B$ and $C$ projections are smaller, these methods use fewer parameters, and the layer count is adjusted appropriately.

**Table 10:** (**Zero-shot Evaluations.**) Best results for each size in bold, second best underlined. Comparison against open source LMs with various tokenizers, trained for up to 300B tokens. Pile refers to the validation split, comparing only against models trained on the same dataset and tokenizer (GPT-NeoX-20B). For each model size, Mamba-2 outperforms Mamba, and generally matches Pythia at twice the model size.

| Model | Token. | Pile ppl $\downarrow$ | LAMBADA ppl $\downarrow$ | LAMBADA acc $\uparrow$ | HellaSwag acc $\uparrow$ | PIQA acc $\uparrow$ | ARC-E acc $\uparrow$ | ARC-C acc $\uparrow$ | WinoGrande acc $\uparrow$ | OpenBookQA acc $\uparrow$ | Average acc $\uparrow$ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Hybrid H3-130M | GPT2 | — | 89.48 | 25.8 | 31.7 | 64.2 | 44.4 | 24.2 | 50.6 | 27.0 | 38.2 |
| Pythia-160M | NeoX | 29.64 | 38.10 | 33.0 | 30.2 | 61.4 | 43.2 | 24.1 | 51.9 | 29.2 | 39.0 |
| Mamba-130M | NeoX | 10.56 | 16.07 | **44.3** | 35.2 | 64.5 | **48.0** | 24.2 | 51.9 | 28.8 | 42.4 |
| **Mamba-2-130M** | NeoX | **10.48** | 16.86 | 43.9 | 35.3 | **64.9** | 47.4 | **24.2** | **52.1** | **30.6** | **42.6** |
| Hybrid H3-360M | GPT2 | — | 12.58 | 48.0 | 41.5 | 68.1 | 51.4 | 24.7 | 54.1 | 31.6 | 45.6 |
| Pythia-410M | NeoX | 9.95 | 10.84 | 51.4 | 40.6 | 66.9 | 52.1 | 24.6 | 53.8 | 30.0 | 45.6 |
| Mamba-370M | NeoX | 8.28 | 8.14 | **55.6** | 46.5 | 69.5 | **55.1** | **28.0** | 55.3 | 30.8 | 48.7 |
| **Mamba-2-370M** | NeoX | **8.21** | **8.02** | 55.8 | **46.9** | **70.5** | 54.9 | 26.9 | **55.7** | **32.4** | **49.0** |
| Pythia-1B | NeoX | 7.82 | 7.92 | 56.1 | 47.2 | 70.7 | 57.0 | 27.1 | 53.5 | 31.4 | 49.0 |
| Mamba-790M | NeoX | 7.33 | 6.02 | **62.7** | **55.1** | **72.1** | **61.2** | **29.5** | 56.1 | **34.2** | **53.0** |
| **Mamba-2-780M** | NeoX | **7.26** | 5.86 | 61.7 | 54.9 | 72.0 | 61.0 | 28.5 | **60.2** | 36.2 | 53.5 |
| GPT-Neo 1.3B | GPT2 | — | 7.50 | 57.2 | 48.9 | 71.1 | 56.2 | 25.9 | 54.9 | 33.6 | 49.7 |
| Hybrid H3-1.3B | GPT2 | — | 11.25 | 49.6 | 52.6 | 71.3 | 59.2 | 28.1 | 56.9 | 34.4 | 50.3 |
| OPT-1.3B | OPT | — | 6.64 | 58.0 | 53.7 | 72.4 | 56.7 | 29.6 | 59.5 | 33.2 | 51.9 |
| Pythia-1.4B | NeoX | 7.51 | 6.08 | 61.7 | 52.1 | 71.0 | 60.5 | 28.5 | 57.2 | 30.8 | 51.7 |
| RWKV4-1.5B | NeoX | 7.70 | 7.04 | 56.4 | 52.5 | 72.4 | 60.5 | 29.4 | 54.6 | 34.0 | 51.4 |
| Mamba-1.4B | NeoX | 6.80 | 5.04 | 65.0 | 59.1 | **74.2** | **65.5** | **32.8** | 61.5 | **36.4** | **56.4** |
| **Mamba-2-1.3B** | NeoX | **6.66** | **5.02** | **65.7** | **59.9** | 73.2 | 64.3 | 33.3 | **60.9** | 37.8 | 56.4 |
| GPT-Neo 2.7B | GPT2 | — | 5.63 | 62.2 | 55.8 | 72.1 | 61.1 | 30.2 | 57.6 | 33.2 | 53.2 |
| Hybrid H3-2.7B | GPT2 | — | 7.92 | 55.7 | 59.7 | 73.3 | 65.6 | 32.3 | 61.4 | 33.6 | 54.5 |
| OPT-2.7B | OPT | — | 5.12 | 63.6 | 60.6 | 74.8 | 60.8 | 31.3 | 61.0 | 35.2 | 55.3 |
| Pythia-2.8B | NeoX | 6.73 | 5.04 | 64.7 | 59.3 | 74.0 | 64.1 | 32.9 | 59.7 | 35.2 | 55.7 |
| RWKV4-3B | NeoX | 7.00 | 5.24 | 63.9 | 59.6 | 73.7 | 67.8 | 33.1 | 59.6 | 37.0 | 56.4 |
| Mamba-2.8B | NeoX | 6.22 | 4.23 | *69.2* | 66.1 | **75.2** | **69.7** | **36.3** | *63.5* | *39.6* | *59.9* |
| **Mamba-2-2.7B** | NeoX | **6.09** | **4.10** | **69.7** | **66.6** | 76.4 | *69.6* | **36.4** | **64.0** | **38.8** | **60.2** |
| GPT-J-6B | GPT2 | — | 4.10 | 68.3 | 66.3 | 75.4 | 67.0 | 36.6 | 64.1 | 38.2 | 59.4 |
| OPT-6.7B | OPT | — | 4.25 | 67.7 | 67.2 | 76.3 | 65.6 | 34.9 | 65.5 | 37.4 | 59.2 |
| Pythia-6.9B | NeoX | 6.51 | 4.45 | 67.1 | 64.0 | 75.2 | 67.3 | 35.5 | 61.3 | 38.0 | 58.3 |
| RWKV4-7.4B | NeoX | 6.31 | 4.38 | 67.2 | 65.5 | 76.1 | 67.8 | 37.5 | 61.0 | 40.2 | 59.3 |
