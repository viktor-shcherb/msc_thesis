# Approach [p. 2-4]

[p. 2] The training approach is similar to methods described in previous work (Brown et al., 2020; Chowdhery et al., 2022), and is inspired by the Chinchilla scaling laws (Hoffmann et al., 2022). They train large transformers on a large quantity of textual data using a standard optimizer.

## 2.1 Pre-training Data

[p. 2] The training dataset is a mixture of several sources, reported in Table 1, covering a diverse set of domains. Data sources are reused from those leveraged to train other LLMs, with the restriction of only using data that is publicly available and compatible with open sourcing. The following mixture of data and percentages represent the training set:

**Table 1** (p. 2): **Pre-training data.** Data mixtures used for pre-training, for each subset listing the sampling proportion, number of epochs performed on the subset when training on 1.4T tokens, and disk size. The pre-training runs on 1T tokens have the same sampling proportion.

| Dataset | Sampling prop. | Epochs | Disk size |
|---|---|---|---|
| CommonCrawl | 67.0% | 1.10 | 3.3 TB |
| C4 | 15.0% | 1.06 | 783 GB |
| Github | 4.5% | 0.64 | 328 GB |
| Wikipedia | 4.5% | 2.45 | 83 GB |
| Books | 4.5% | 2.23 | 85 GB |
| ArXiv | 2.5% | 1.06 | 92 GB |
| StackExchange | 2.0% | 1.03 | 78 GB |

**English CommonCrawl [67%].** Five CommonCrawl dumps preprocessed, ranging from 2017 to 2020, with the CCNet pipeline (Wenzek et al., 2020). This process deduplicates the data at the line level, performs language identification with a fastText linear classifier to remove non-English pages, and filters low quality content with an n-gram language model. Additionally, they trained a linear model to classify pages used as references in Wikipedia *v.s.* randomly sampled pages, and discarded pages not classified as references. [p. 2]

**C4 [15%].** During exploratory experiments, they observed that using diverse pre-processed CommonCrawl datasets improves performance. They included the publicly available C4 dataset (Raffel et al., 2020). The preprocessing of C4 also contains deduplication and language identification steps; the main difference with CCNet is the quality filtering, which mostly relies on heuristics such as presence of punctuation marks or the number of words and sentences in a webpage. [p. 2]

**Github [4.5%].** The public GitHub dataset available on Google BigQuery. Only projects distributed under the Apache, BSD and MIT licenses are kept. Low quality files filtered with heuristics based on line length or proportion of alphanumeric characters, and boilerplate removed (headers, regular expressions). The resulting dataset is deduplicated at the file level, with exact matches. [p. 2]

**Wikipedia [4.5%].** Wikipedia dumps from the June-August 2022 period, covering 20 languages which use either the Latin or Cyrillic scripts: bg, ca, cs, da, de, en, es, fr, hr, hu, it, nl, pl, pt, ro, ru, sl, sr, sv, uk. The data is processed to remove hyperlinks, comments and other formatting boilerplate. [p. 2]

**Gutenberg and Books3 [4.5%].** Two book corpora: the Gutenberg Project (public domain books) and the Books3 section of ThePile (Gao et al., 2020), a publicly available dataset for training large language models. Deduplication at the book level, removing books with more than 90% content overlap. [p. 2]

**ArXiv [2.5%].** arXiv Latex files processed to add scientific data. Following Lewkowycz et al. (2022), everything before the first section as well as the bibliography is removed. Comments from the .tex files are also removed, and inline-expanded definitions and macros written by users to increase consistency across papers. [p. 2]

**Stack Exchange [2%].** A dump of Stack Exchange, a website of high quality questions and answers covering a diverse set of domains, from computer science to chemistry. Data kept from the 28 largest websites, HTML tags removed from text, and answers sorted by score (highest to lowest). [p. 2]

**Tokenizer.** Data tokenized with the byte-pair encoding (BPE) algorithm (Sennrich et al., 2015), using the implementation from SentencePiece (Kudo and Richardson, 2018). Notably, all numbers are split into individual digits, and fallback to bytes to decompose unknown UTF-8 characters. [p. 2]

[p. 3] Overall, the entire training dataset contains roughly 1.4T tokens after tokenization. For most of the training data, each token is used only once during training, with the exception of the Wikipedia and Books domains, over which approximately two epochs are performed.

## 2.2 Architecture

[p. 3] The network is based on the transformer architecture (Vaswani et al., 2017). Various improvements subsequently proposed and used in different models such as PaLM are leveraged. The main differences with the original architecture, and where the inspiration was found (in bracket):

**Pre-normalization [GPT3].** To improve training stability, the input of each transformer sub-layer is normalized instead of the output. The RMSNorm normalizing function is used, introduced by Zhang and Sennrich (2019). [p. 3]

**SwiGLU activation function [PaLM].** The ReLU non-linearity is replaced by the SwiGLU activation function, introduced by Shazeer (2020) to improve performance. A dimension of 2/3 * 4d is used instead of 4d as in PaLM. [p. 3]

**Rotary Embeddings [GPTNeo].** The absolute positional embeddings are removed, and instead, rotary positional embeddings (RoPE) are added, introduced by Su et al. (2021), at each layer of the network. [p. 3]

The details of the hyper-parameters for the different models are given in Table 2.

**Table 2** (p. 3): **Model sizes, architectures, and optimization hyper-parameters.**

| params | dimension | *n* heads | *n* layers | learning rate | batch size | *n* tokens |
|---|---|---|---|---|---|---|
| 6.7B | 4096 | 32 | 32 | 3.0e-4 | 4M | 1.0T |
| 13.0B | 5120 | 40 | 40 | 3.0e-4 | 4M | 1.0T |
| 32.5B | 6656 | 52 | 60 | 1.5e-4 | 4M | 1.4T |
| 65.2B | 8192 | 64 | 80 | 1.5e-4 | 4M | 1.4T |

## 2.3 Optimizer

[p. 3] Models are trained using the AdamW optimizer (Loshchilov and Hutter, 2017), with the following hyper-parameters: beta_1 = 0.9, beta_2 = 0.95. A cosine learning rate schedule is used, such that the final learning rate is equal to 10% of the maximal learning rate. A weight decay of 0.1 and gradient clipping of 1.0. 2,000 warmup steps are used, and the learning rate and batch size are varied with the size of the model (see Table 2 for details). [p. 3]

## 2.4 Efficient implementation

[p. 3-4] Several optimizations are made to improve training speed:

- **Efficient causal multi-head attention:** An efficient implementation of causal multi-head attention to reduce memory usage and runtime, available in the xformers library (https://github.com/facebookresearch/xformers), inspired by Rabe and Staats (2021) and uses the backward from Dao et al. (2022). This is achieved by not storing the attention weights and not computing the key/query scores that are masked due to the causal nature of the language modeling task. [p. 3]

- **Activation checkpointing:** The amount of activations recomputed during the backward pass is reduced with checkpointing. The activations that are expensive to compute, such as the outputs of linear layers, are saved. This is achieved by manually implementing the backward function for the transformer layers, instead of relying on the PyTorch autograd. [p. 3-4]

- **Model and sequence parallelism:** Memory usage of the model is reduced by using model and sequence parallelism, as described by Korthikanti et al. (2022). Computation of activations and communication between GPUs over the network (due to all_reduce operations) are also overlapped as much as possible. [p. 4]

**Training throughput for 65B model:** approximately 380 tokens/sec/GPU on 2048 A100 GPUs with 80GB of RAM. Training over the dataset containing 1.4T tokens takes approximately 21 days. [p. 4]

**Figure 1** (p. 3): **"Training loss over train tokens for the 7B, 13B, 33B, and 65 models."** LLaMA-33B and LLaMA-65B were trained on 1.4T tokens. The smaller models were trained on 1.0T tokens. All models are trained with a batch size of 4M tokens. The figure shows training loss (y-axis, range approximately 1.5-2.2) vs. billion of tokens (x-axis, 0-1400). All four model curves decrease steeply at first and then flatten, with larger models achieving lower loss throughout. LLaMA-65B reaches the lowest final loss (approximately 1.5), followed by 33B, 13B, and 7B in order.
