# 4 Experiments [p. 5-6]

## 4.1 Main Results [p. 5-6]

Transformer-XL is applied to a variety of datasets on both word-level and character-level language modeling, including: [p. 6]
- WikiText-103 (Merity et al., 2016)
- enwiki8 (LLC, 2009)
- text8 (LLC, 2009)
- One Billion Word (Chelba et al., 2013)
- Penn Treebank (Mikolov and Zweig, 2012)

### WikiText-103

The largest available word-level language modeling benchmark with long-term dependency. Contains 103M training tokens from 28K articles, with an average length of 3.6K tokens per article, which allows testing the ability of long-term dependency modeling. [p. 6]

- Attention length: 384 during training, 1600 during evaluation.
- Adopted adaptive softmax and input representations (Baevski and Auli, 2018; Grave et al., 2016a).
- Transformer-XL reduces the previous SoTA perplexity from 20.5 to 18.3, demonstrating the superiority of the Transformer-XL architecture. [p. 6]

**Table 1** (p. 6): Comparison with state-of-the-art results on WikiText-103. (degree sign) indicates contemporary work.

| Model | #Param | PPL |
|---|---|---|
| Grave et al. (2016b) - LSTM | - | 48.7 |
| Bai et al. (2018) - TCN | - | 45.2 |
| Dauphin et al. (2016) - GCNN-8 | - | 44.9 |
| Grave et al. (2016b) - LSTM + Neural cache | - | 40.8 |
| Dauphin et al. (2016) - GCNN-14 | - | 37.2 |
| Merity et al. (2018) - QRNN | 151M | 33.0 |
| Rae et al. (2018) - Hebbian + Cache | - | 29.9 |
| Ours - Transformer-XL Standard | 151M | 24.0 |
| Baevski and Auli (2018) - Adaptive Input* | 247M | 20.5 |
| Ours - Transformer-XL Large | 257M | **18.3** |

### enwiki8

Contains 100M bytes of unprocessed Wikipedia text. [p. 6]

Under the model size constraint, the 12-layer Transformer-XL achieves a new SoTA result, outperforming the 12-layer vanilla Transformer from Al-Rfou et al. (2018) by 0.05, while both Transformer variants have a large margin over conventional RNN-based models. Notably, the 12-layer architecture achieves the same result as the 64-layer network from Al-Rfou et al. (2018), using only 17% of the parameter budget. [p. 6]

To see whether better performance can be obtained by increasing model size, 18-layer and 24-layer Transformer-XLs are trained with increased model sizes. With the attention length 784 during training and 3,800 during evaluation, a new SoTA result is obtained and the method is the first to break through 1.0 on widely-studied character-level benchmarks. Different from Al-Rfou et al. (2018), Transformer-XL does not need any auxiliary losses, and thus all benefits are credited to a better architecture. [p. 6]

**Table 2** (p. 6): Comparison with state-of-the-art results on enwiki8.

| Model | #Param | bpc |
|---|---|---|
| Ha et al. (2016) - LN HyperNetworks | 27M | 1.34 |
| Chung et al. (2016) - LN HM-LSTM | 35M | 1.32 |
| Zilly et al. (2016) - RHN | 46M | 1.27 |
| Mujika et al. (2017) - FS-LSTM-4 | 47M | 1.25 |
| Krause et al. (2016) - Large mLSTM | 46M | 1.24 |
| Knol (2017) - cmix v13 | - | 1.23 |
| Al-Rfou et al. (2018) - 12L Transformer | 44M | 1.11 |
| Ours - 12L Transformer-XL | 41M | **1.06** |
| Al-Rfou et al. (2018) - 64L Transformer | 235M | 1.06 |
| Ours - 18L Transformer-XL | 88M | 1.03 |
| Ours - 24L Transformer-XL | 277M | **0.99** |

### text8

Similar to enwiki8 but contains 100M processed Wikipedia characters created by lowering case and removing any character other than the 26 letters a through z, and space. The best model and same hyper-parameters on enwiki8 are adapted to text8 without further tuning. [p. 6]

**Table 3** (p. 6): Comparison with state-of-the-art results on text8.

| Model | #Param | bpc |
|---|---|---|
| Cooijmans et al. (2016) - BN-LSTM | - | 1.36 |
| Chung et al. (2016) - LN HM-LSTM | 35M | 1.29 |
| Zilly et al. (2016) - RHN | 45M | 1.27 |
| Krause et al. (2016) - Large mLSTM | 45M | 1.27 |
| Al-Rfou et al. (2018) - 12L Transformer | 44M | 1.18 |
| Al-Rfou et al. (2018) - 64L Transformer | 235M | 1.13 |
| Ours - 24L Transformer-XL | 277M | **1.08** |

### One Billion Word

**Table 4** (p. 6): Comparison with state-of-the-art results on One Billion Word. (degree sign) indicates contemporary work.

| Model | #Param | PPL |
|---|---|---|
| Shazeer et al. (2014) - Sparse Non-Negative | 33B | 52.9 |
| Chelba et al. (2013) - RNN-1024 + 9 Gram | 20B | 51.3 |
| Kuchaiev and Ginsburg (2017) - G-LSTM-2 | - | 36.0 |
| Dauphin et al. (2016) - GCNN-14 bottleneck | - | 31.9 |
| Jozefowicz et al. (2016) - LSTM | 1.8B | 30.6 |
| Jozefowicz et al. (2016) - LSTM + CNN Input | 1.04B | 30.0 |
| Shazeer et al. (2017) - Low-Budget MoE | ~5B | 34.1 |
| Shazeer et al. (2017) - High-Budget MoE | ~5B | 28.0 |
| Shazeer et al. (2018) - Mesh Tensorflow | 4.9B | 24.0 |
| Baevski and Auli (2018) - Adaptive Input* | 0.46B | 24.1 |
| Baevski and Auli (2018) - Adaptive Input* | 1.0B | 23.7 |
| Ours - Transformer-XL Base | 0.46B | 23.5 |
| Ours - Transformer-XL Large | 0.8B | **21.8** |

[p. 7] One Billion Word does not preserve any long-term dependency because sentences have been shuffled. Consequently, this dataset mainly tests the ability of modeling only short-term dependency. Although Transformer-XL is mainly designed to better capture longer-term dependency, it dramatically improves the single-model SoTA from 23.7 to 21.8. Specifically, Transformer-XL significantly outperforms a contemporary method using vanilla Transformers (Baevski and Auli, 2018), suggesting the advantage of Transformer-XL is generalizable to modeling short sequences. [p. 7]

### Penn Treebank

[p. 7] Word-level Penn Treebank results are reported in Table 5. Similar to AWD-LSTM (Merity et al., 2017), variational dropout and weight average are applied to Transformer-XL. With proper regularization, Transformer-XL achieves a new SoTA result among models without two-step finetuning. Penn Treebank has only 1M training tokens, which implies that Transformer-XL also generalizes well even on small datasets. [p. 7]

**Table 5** (p. 7): Comparison with state-of-the-art results on Penn Treebank. dagger indicates using two-step finetuning.

| Model | #Param | PPL |
|---|---|---|
| Inan et al. (2016) - Tied Variational LSTM | 24M | 73.2 |
| Zilly et al. (2016) - Variational RHN | 23M | 65.4 |
| Zoph and Le (2016) - NAS Cell | 25M | 64.0 |
| Merity et al. (2017) - AWD-LSTM | 24M | 58.8 |
| Pham et al. (2018) - Efficient NAS | 24M | 58.6 |
| Liu et al. (2018) - Differentiable NAS | 23M | 56.1 |
| Yang et al. (2017) - AWD-LSTM-MoS | 22M | 55.97 |
| Melis et al. (2018) - Dropout tuning | 24M | 55.3 |
| Ours - Transformer-XL | 24M | **54.52** |
| Merity et al. (2017) - AWD-LSTM+Finetune^dagger | 24M | 57.3 |
| Yang et al. (2017) - MoS+Finetune^dagger | 22M | 54.44 |
