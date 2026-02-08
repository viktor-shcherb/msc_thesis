# Appendix E: Experimental Details and Additional Results [p. 29–31]

## E.1 Synthetic Tasks

[p. 29]

**Selective Copying.** The setting is on sequences of length 4096, with a vocab size of 16 possible tokens (including the white "noise" token from Figure 2) and requiring models to memorize 16 "data" tokens. They use 2 layer models with a model dimension of $D = 64$.

Models are trained for 400K steps at a constant learning rate of 0.0001 with a batch size of 64.

**Induction Heads.** Training consists of randomly generating data every step, with a batch size of 8. They choose an "epoch" size of 8192 steps, and track the accuracy on fixed validation sets (also randomly generated) of each target sequence length. For the MHA-Abs and Mamba models, results are reported after the 25th epoch ($8192 \times 25 = 204800$ steps). For the MHA-RoPE and MHA-xPos models, results are reported after the 50th epoch ($8192 \times 50 = 409600$ steps). For the LTI H3 and Hyena models, results are reported after the 10th epoch (81920 steps) because they had converged by then and failed to improve further.

The authors use the Adam optimizer with no weight decay. All models are trained at constant learning rates $2e-4$ and $1e-3$, and the better results are reported for each model ($2e-4$ for all models except Mamba). The attention and Hyena models did not learn at LR $1e-3$. H3 learned at both LRs, but interestingly generalized better to shorter sequences at the smaller LR of $2e-4$. Mamba learned at both LRs, but extrapolated better at the larger LR of $1e-3$.

**Table 11:** (Induction heads.) Models are trained on sequence length $2^8 = 256$, and tested on various sequence lengths of $2^6 = 64$ up to $2^{20} = 1048576$. Checkmark denotes perfect generalization accuracy, while X denotes out of memory. [p. 29]

| Model | Params | $2^6$ | $2^7$ | $2^8$ | $2^9$ | $2^{10}$ | $2^{11}$ | $2^{12}$ | $2^{13}$ | $2^{14}$ | $2^{15}$ | $2^{16}$ | $2^{17}$ | $2^{18}$ | $2^{19}$ | $2^{20}$ |
|-------|--------|-------|-------|-------|-------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|
| MHA-Abs | 137K | ✓ | 99.6 | 100.0 | 58.6 | 26.6 | 18.8 | 9.8 | 10.9 | 7.8 | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ |
| MHA-RoPE | 137K | ✓ | 100.0 | 83.6 | 31.3 | 18.4 | 8.6 | 9.0 | 5.5 | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ |
| MHA-xPos | 137K | ✓ | 100.0 | 99.6 | 67.6 | 25.4 | 7.0 | 9.0 | 7.8 | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ |
| H3 | 153K | ✓ | ✓ | 100.0 | 80.9 | 39.5 | 23.8 | 14.8 | 8.2 | 5.9 | 6.6 | 8.2 | 4.7 | 8.2 | 6.3 | 7.4 |
| Hyena | 69M* | 97.7 | 100.0 | ✓ | 44.1 | 12.5 | 6.6 | 5.1 | 7.0 | 5.9 | 6.6 | 6.6 | 5.9 | 6.3 | 9.8 | |
| Mamba | 74K | ✓ | ✓ | 100.0 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |

\* Most of the parameters are in learnable positional encodings.

## E.2 Language Modeling

### E.2.1 Scaling Law Details

[p. 29–30]

Scaling law experiments generally followed the GPT3 recipe. All models were trained on the Pile with the GPT2 tokenizer.

**Model Sizes.** Table 12 specifies the model sizes used for scaling laws. This is taken directly from the GPT3 specifications (Brown et al. 2020), with very minor modifications. First, the batch size of the 1.3B model was changed from 1M tokens to 0.5M tokens, since they did not use enough parallelization to require the larger batch size. Second, the number of training steps and total tokens was changed to roughly match Chinchilla scaling laws (Hoffmann et al. 2022), which specify that training tokens should increase proportionally to model size.

**Table 12:** (Scaling Law Model Sizes.) Model sizes and hyperparameters for scaling experiments. (Model dimension and number of heads applies only to Transformer models.) [p. 30]

| Params | n_layers | d_model | n_heads / d_head | Training steps | Learning Rate | Batch Size | Tokens |
|--------|----------|---------|------------------|----------------|---------------|------------|--------|
| 125M | 12 | 768 | 12 / 64 | 4800 | 6e-4 | 0.5M tokens | 2.5B |
| 350M | 24 | 1024 | 16 / 64 | 13500 | 3e-4 | 0.5M tokens | 7B |
| 760M | 24 | 1536 | 16 / 96 | 29000 | 2.5e-4 | 0.5M tokens | 15B |
| 1.3B | 24 | 2048 | 32 / 64 | 50000 | 2e-4 | 0.5M tokens | 26B |

**Training Recipes.** All models used the AdamW optimizer with:

- gradient clip value 1.0
- weight decay 0.1
- no dropout
- linear learning rate warmup with cosine decay

By default, the peak learning rate is the GPT3 specification.

The authors give several models an "improved recipe", inspired by changes adopted by popular large language models such as PaLM (Chowdhery et al. 2023) and LLaMa (Touvron et al. 2023). These include:

- linear learning rate warmup with cosine decay to $1e-5$, with a peak value of 5x the GPT3 value
- no linear bias terms
- RMSNorm instead of LayerNorm
- AdamW hyperparameter $\beta = (.9, .95)$ (the GPT3 value) instead of the PyTorch default of $\beta = (.9, .999)$

**Architecture and Training Details.** The models are: [p. 30]

- **Transformer**: The standard Transformer based on GPT3 (Table 12).
- **Transformer++**: A Transformer with an improved architecture, namely rotary positional encodings (Su et al. 2021) and SwiGLU MLP (Shazeer 2020), and the improved training recipe above.
- **Hyena**: Interleaving a Hyena block (the H3 block with S4 replaced by a global convolution parameterized by an MLP) with standard MLP blocks. The MLP blocks have expansion factor 2 instead of 4 and the number of layers is correspondingly increased by 1.5x to preserve parameter count.
- **H3++**: The H3 architecture with a few modifications, including (i) using the same "thin" Hyena dimensions above (ii) the improved training recipe above (iii) a linear attention *head dimension* of 8.
- **RWKV**: The default RWKV model from B. Peng et al. (2023), including its modified MLP block. They also used as much of its specified training recipe as possible, such as increasing the learning rates by 2x or 3x on certain parameters.
- **RetNet**: The default RetNet model from Y. Sun et al. (2023). They also gave it the improved training recipe above.
- **Mamba**: The standard Mamba architecture, with the improved training recipe.

### E.2.2 Additional Scaling Law Ablations

[p. 30–31]

The authors perform additional ablations on the architecture using the same protocol as the 2k context length scaling laws in Figure 4 (*Left*).

**Mamba Architecture: Interleaving Blocks.** They test the effect of different architectural blocks combined with the Mamba block. They focus on the viewpoint that the Mamba block is simply the standard SwiGLU block with an extra conv $\to$ SSM path added. This leads to two natural ablations: [p. 30]

- What if the Mamba block is interleaved with a standard MLP block, instead of stacked homogenously? This can also be interpreted as taking Mamba and removing half of the SSMs.
- What if the Mamba block is interleaved with MHA (multi-head attention) blocks? This can also be interpreted as taking a Transformer with SwiGLU MLPs (i.e. what we call Transformer++) and simply adding SSMs to the MLP blocks.

**Figure 9** (p. 31): (Scaling laws: extra ablations.) (*Left*) Mamba vs. Mamba-MLP vs. Mamba-MHA on scaling laws on The Pile (Sequence Length 2048). Y-axis: Perplexity (log scale). X-axis: FLOPs (log scale). (*Right*) Hyena vs. Hyena+ vs. H3+ vs. H3++ on scaling laws on The Pile (Sequence Length 2048). Y-axis: Perplexity (log scale). X-axis: FLOPs (log scale). Both panels show roughly linear scaling on log-log axes. In the left panel, Mamba, Mamba-MLP, and Mamba-MHA all perform similarly, with Mamba slightly better. In the right panel, H3++ is best, followed by H3+, then Hyena+, then Hyena, showing the impact of the improved training recipe and architectural changes.

Figure 9 (*Left*) shows these variants compared to the original (homogenous) Mamba architecture. Interestingly, neither change matters too much. The Mamba-MLP architecture is only slightly worse, and still better than all models except Transformer++. The Mamba-MHA architecture is only slightly better, which is somewhat surprising in light of the fact that many recent works have found that combining (LTI) SSMs with Attention can lead to substantial improvements (Dao, Fu, Saab, et al. 2023; Fathi et al. 2023; Fathullah et al. 2023; Saon, Gupta, and Cui 2023; Zuo et al. 2022). [p. 31]

**H3 Architecture: Training Recipes.** Next the authors ablate differences between the Hyena and H3++ models, their weakest and strongest models outside of Transformer++ and Mamba, particularly to isolate the effect of training recipes.

- **Hyena**: The Hyena block with its original architecture and GPT3 training recipe (same as Figure 4).
- **Hyena+**: The same architecture but with the improved training recipe described above.
- **H3+**: The same architecture as Hyena+ but with the Hyena convolution kernel swapped out for S4D convolution kernel.
- **H3++**: The same as H3+, but with a linear attention *head dimension* of 8. This increases computation inside the SSM recurrence but does not increase parameters.

The general convention is that "Model+" represents the base model with the improved training recipe, and "Model++" also allows for architectural changes.

Figure 9 (*Right*) shows that: [p. 31]

- A large improvement is achieved by the improved training recipe, which was used for many of the models in the main Figure 4 (RetNet, H3++, Transformer++, Mamba).
- The choice of the inner LTI SSM does not matter (e.g. Hyena vs. S4), consistent with findings throughout this paper.
- The head dimension expansion improves performance, consistent with one of the main themes that expanded state dimension improves performance for SSMs (Section 3).

### E.2.3 Downstream Evaluation Details

[p. 31]

The pretraining procedure is the same as the scaling law protocol, but extended to 300B tokens and with the GPT-NeoX tokenizer (Black et al. 2022) instead of GPT2 tokenizer. For the 1.3B model, a batch size of 1M tokens is used to be consistent with the GPT3 specifications. The perplexity on the Pile validation set is reported, and for this metric only compared to models trained on the same dataset and with the same tokenizer, in particular Pythia and RWKV.

For downstream evaluation, the LM evaluation harness from EleutherAI (L. Gao, Tow, et al. 2021) is used, as done by most work in this area. They evaluate on the following tasks/datasets that measure common sense reasoning:

- LAMBADA (Paperno et al. 2016)
- HellaSwag (Zellers et al. 2019)

---
[p. 32 continued]

- PIQA (Bisk et al. 2020)
- ARC-challenge (P. Clark et al. 2018)
- ARC-easy: an easy subset of ARC-challenge
- WinoGrande (Sakaguchi et al. 2021)

Accuracy is reported for LAMBADA, WinoGrande, PIQA, and ARC-easy, and accuracy normalized by sequence length for HellaSwag and ARC-challenge (since normalized accuracy is higher for almost all models for these tasks).

## E.3 DNA Modeling

### E.3.1 Pretraining Details

[p. 32]

The dataset and training procedure of the HG38 pretraining task is described in more detail.

The dataset follows the splits from the prior Enformer work on genomics (Avsec et al. 2021); the training split contains a total of $S = 34021$ segments of length $2^{17} = 131072$ that cover the genome, for a total of approximately 4.5 billion tokens (DNA base pairs). These segments are pairs of (chromosome number, starting index, ending index), and can be extended if necessary (e.g. to get longer segments).

The authors deviate from HyenaDNA when the training sequence length is not $2^{17}$. HyenaDNA always takes a fixed sub-segment (e.g. the beginning or middle of the prescribed segment), and thus for any training sequence length each epoch is fixed to 34021 samples and does not necessarily go through the whole genome. The authors instead use the entire training data:

- When the context length $L$ is less than (or equal to) $2^{17}$, each segment is divided into non-overlapping sub-segments of length $L$, so that there are $S \times \frac{2^{17}}{L}$ total samples and $S \times 2^{17} \approx 4.5B$ tokens per epoch.
- When the context length $L$ is greater than $2^{17}$, each segment is turned into two samples, one that begins with the prescribed segment and one that ends with the prescribed segment. Thus each epoch has $2S$ items and $2SL$ tokens per epoch. For example, at sequence length $2^{18} = 262144$ there are $4\times$ as many tokens as the default, and at sequence length $2^{20}$ there are $16\times$ as many tokens.

Other training details generally follow the same protocol as the language modeling experiments (Appendix E.2). For example, AdamW is used with $(\beta_1, \beta_2) = (0.9, 0.95)$, no dropout, weight decay 0.1. A cosine learning rate scheduler with linear warmup for 10% of total steps is used.

### E.3.2 Scaling: Model Size Details

[p. 32]

**Models.** The models considered are:

- **Transformer++**: a Transformer with improved architecture, notably the usage of RoPE positional encodings (Su et al. 2021). Informally, the authors found these to be noticeably better than vanilla positional encodings from (Vaswani et al. 2017).
- **HyenaDNA**: the Hyena model from Nguyen, Poli, et al. (2023) and Poli et al. (2023), which is roughly a Transformer with the MHA block replaced by an H3 block using a global convolution parameterized by an MLP.
- **Mamba**: the standard Mamba architecture.

**Model Sizes.** The following model sizes are used:

| Blocks | 4 | 5 | 6 | 7 | 8 | 10 | 12 |
|--------|---|---|---|---|---|----|----|
| Model Dimension | 64 | 96 | 128 | 192 | 256 | 384 | 512 |
| Params (Approx.) | 250K | 700K | 1.4M | 3.5M | 7.0M | 19.3M | 40.7M |

Note that the number of blocks for Mamba is doubled, because one Transformer "layer" includes both the MHA and MLP blocks (and similarly for Hyena), which requires two Mamba blocks to match parameters (Section 3.4). [p. 32]

### E.3.3 Scaling: Context Length Details

[p. 33]

**Training.** For each model (Transformer++, HyenaDNA, Mamba), the learning rate was swept across $\{1e-3, 2e-3, 4e-3, 8e-3\}$. The optimal Transformer and HyenaDNA learning rates were 2e-3 across all sizes. The optimal Mamba learning rate was 8e-3; note that Mamba performed better than baselines with matched learning rates (2e-3), but was more stable and improved even more at higher learning rates. (Furthermore, as this LR is on the upper range of the sweep, it is possible that the results are still suboptimal.)

Note that, in contrast to standard LM scaling laws (Table 12), the LR held constant across model sizes for simplicity. The optimal LR should go down for larger models, but the authors did not find a noticeable effect at the small model sizes (at most a few million parameters) they considered.

A total batch size of $2^{24} \approx 16M$ tokens per training step is used, for every sequence length (e.g. at length $2^{20}$ there are 16 segments per batch and at length $2^{10}$ there are 16384 segments per batch). This is a large batch size relative to the model size by usual LM standards, but note that a batch size of $2^{23}$ is the minimum possible on a machine with 8 GPUs and sequence length of $2^{20}$, and that HyenaDNA used much larger batches of $2^{28}$.

The learning rate used was 0.008 for Mamba and 0.001 for HyenaDNA; the authors initially attempted to use the same learning rate of 0.002 from the previous section for HyenaDNA, but found that it was unstable at the longest context length.

**Sequence Length Warmup.** Following (Nguyen, Poli, et al. 2023), sequence length warmup (SLW) is used during pretraining. A simple schedule of 2 epochs at each power-of-two sequence length starting from $2^{10} = 1024$ is chosen. (Note that because of how data is curated, at the longest sequence lengths more steps and tokens are spent proportionally. In particular, each stage up to length $2^{17}$ processes the same number of tokens, but $4\times$ as many tokens are processed at length $2^{18}$, $8\times$ as many at length $2^{19}$, and $16\times$ as many at length $2^{20}$.)

Unlike HyenaDNA, the authors always control for the number of tokens per gradient update, so the batch size is successively halved as the sequence lengths are doubled in each stage.

**Remark E.1.** *We also note that the schedule was not tuned, and we never experimented with turning off sequence length warmup for these pretraining experiments. We later found that SLW did not help noticeably for audio pretraining at similar lengths (Section 4.4), and it is possible that it is not necessary for DNA pretraining either.* [p. 33]

### E.3.4 Species (Great Apes) Classification

[p. 33–34]

Models are causal and therefore only the last element (across the sequence length) of the model's output is used for the classification head. Note that the total number of elements in the loss function per gradient step is controlled. The pretraining objective includes all positions across the sequence length, so that `batch_size × sequence_length` is held constant; in other words, the batch size decreases as the sequence length increases. However, for a classification task, since only the last position enters the loss, the batch size itself is held constant. Note that this also means that fine-tuning models with longer sequence lengths is more computationally expensive.

Training consists of 10 epochs, each of which has 1024 gradient steps. Each gradient step uses batch size 64, which are all independently randomly drawn by uniformly picking a species, uniformly picking a chromosome, and then uniformly picking a contiguous segment of DNA.

Following (Nguyen, Poli, et al. 2023), models with a maximum context length greater than $2^{14} = 16384$ use sequence length warmup with 1 epoch at length $2^{14} = 16384$, 1 epoch at length $2^{15} = 32768$, 1 epoch at length $2^{16} = 65536$, and so on up to the maximum sequence length. For example, the model with $2^{20} = 1048576$ context undergoes 6 epochs of sequence length warmup before 4 more epochs at its maximum sequence length.

The learning rate for all Hyena models is $4e-5$, while the learning rate for all Mamba models is $1e-4$. These were found by performing learning rate sweeps for each model among $\{1e-5, 2e-5, 4e-5, 1e-4, 2e-4\}$ for the smaller sequence lengths ($2^{10}, 2^{12}, 2^{14}, 2^{16}$), and these values were consistently found to be the best for each model. An abridged learning rate sweep was done at length $2^{18}$, which agreed with these values, and a single run at length $2^{20}$ was performed (as described above, the computational cost of these experiments is proportional to the sequence length). The learning rate followed a cosine decay schedule with warmup with 5 epochs of linear warmup to the maximum learning rate, and 5 epochs of cosine decay down to $1e-6$. The unusually long learning rate warmup schedule was chosen because the sequence length warmup was also long (e.g. comprising 6 out of 10 epochs for the model with context length $2^{20}$); the authors did not experiment with this choice. [p. 33–34]

Results for the Species classification task are in Table 13.

**Table 13:** (Great Apes DNA Classification.) Accuracy after fine-tuning on sequences of length $2^{10} = 1024$ up to $2^{20} = 1048576$ using pretrained models of the same context length. Random guessing is 20%. [p. 34]

| Model | Params | $2^{10}$ | $2^{12}$ | $2^{14}$ | $2^{16}$ | $2^{18}$ | $2^{20}$ |
|-------|--------|----------|----------|----------|----------|----------|----------|
| HyenaDNA | 1.4M | 28.04 | 28.43 | 41.17 | 42.22 | 31.10 | 54.87 |
| Mamba | 1.4M | 31.47 | 27.50 | 27.66 | 40.72 | 42.41 | **71.67** |
| Mamba | 7M | 30.00 | 29.01 | 31.48 | 43.73 | 56.60 | **81.31** |
