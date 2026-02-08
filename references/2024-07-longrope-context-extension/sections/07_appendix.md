# A. Appendix [p. 12-13]

## A.1. Settings [p. 12]

**Environments.** All experiments are conducted on 16 A100 GPUs. Flash Attention-2 (Dao, 2023) is employed to accelerate both training and inference. As the GPU memory and computation time increase exponentially with the sequence length, it is challenging to serve the fine-tuning and inference with context length beyond 512k. As a result, an internal platform, CUBE (Lin et al., 2023), is utilized to reduce both the training and inference costs. [p. 12]

**Passkey prompt.** The authors follow existing literature (Mohtashami & Jaggi, 2023; Chen et al., 2023a; Peng et al., 2023; Chen et al., 2023b; Zhu et al., 2023) for the document format of passkey retrieval. The prompt template is as follows: [p. 12]

```
There is an important info hidden inside a lot of irrelevant text. Find it and
memorize them. I will quiz you about the important information there.

The grass is green. The sky is blue. The sun is yellow. Here we go. There and
back again. (repeat x times)

The pass key is 17865. Remember it. 17865 is the pass key.

The grass is green. The sky is blue. The sun is yellow. Here we go. There and
back again. (repeat y times)

What is the pass key? The pass key is
```

The document length varies with the value of x and y. 17865 is the passkey number to retrieve. It is randomly sampled and varies at each testing time. [p. 12]

## A.2. Additional Details on Fine-tuning [p. 12-13]

As introduced in Section 4.2, two context window lengths are fine-tuned, namely 128k and 256k, for both LLaMA2 and Mistral. Specifically, the model with a 256k context window begins its fine-tuning from the 128k-length checkpoint. Fig. 5(ab) illustrates the training loss for LLaMA2 and Mistral during this fine-tuning process. Three key observations are highlighted: [p. 12]

**(1)** The model with a 128k context window experiences a large initial loss due to a 32x extension. However, the loss rapidly decreases after a few steps. [p. 12]

**(2)** LLaMA2 and Mistral employ different fine-tuning settings. Mistral achieves the desired long context window by fine-tuning on 16k-length data, while LLaMA2 necessitates text lengths that match the context window size. Furthermore, YaRN's strategy of using a constant learning rate is adopted. As a result, it can be observed that Mistral's loss begins to fluctuate after dropping to around 2.2. [p. 12]

**(3)** For both Mistral and LLaMA2, the model with a 256k context window, which starts fine-tuning from the 128k checkpoint, exhibits a low initial training loss. This suggests that fine-tuning from 128k-length checkpoints is effective and significantly facilitates convergence. [p. 12]

**Figure 5** (p. 12): "(ab): Loss curve in fine-tuning LLaMA2-7B and Mistral-7B with extended context window size. (c) The training loss of fine-tuning LLaMA2-7B with a 256k context window under different fine-tuning settings."

The figure has three subplots:
- **(a)** LLaMA2 fine-tuning loss (y-axis: Fine-tuning loss ~2-5, x-axis: Steps 0-600). Two lines: LLaMA2 128k starts at ~5 and drops rapidly to ~2.5; LLaMA2 256k starts at ~3 and drops to ~2.5.
- **(b)** Mistral fine-tuning loss (y-axis: ~2.0-2.8, x-axis: Steps 0-400). Two lines: Mistral 128k starts at ~2.8 and drops to fluctuate around ~2.2; Mistral 256k starts at ~2.2 and remains relatively stable with fluctuations.
- **(c)** LLaMA2-7B 256k fine-tuning under different settings (y-axis: ~2-6, x-axis: Steps 0-600). Three lines: "FT from LLaMA2 at 256k length" starts highest (~5-6) and decreases slowly; "FT from LLaMA2 at 128k length" starts at ~4 and decreases moderately; "FT from 128k-length LLaMA2" starts lowest (~3) and reaches lowest values.

---
[p. 13 continued]

Two additional fine-tuning settings for LLaMA2 with 256k context window are explored. As shown in Fig. 5(c), the experiments use: (i) using the RoPE rescale factors corresponding to 256k, directly fine-tuning on LLaMA2-7B, and (ii) using RoPE rescale factors for 256k, fine-tuning on LLaMA2-7B, but truncating the text lengths to 128k. The loss curves are displayed in Fig. 5(c). Using 128k text lengths to fine-tune a model with a 256k context window results in a sharp increase in the initial loss. Directly fine-tuning from LLaMA2-7B to achieve 256k results in a relatively slow decrease in loss. [p. 13]

**Table 12** (p. 13): Proof-pile perplexity of extended LLaMA2-7B via different fine-tuning settings. Tuples of three values represent the fine-tuning text length, context window size, and initial checkpoint.

| Method (fine-tune L', L', base LLM) | 32768 | 65536 | 98304 | 131072 | 262144 |
|---|---|---|---|---|---|
| (128k, 256k, LLaMA2-7B) | 9.75 | 6.56 | 5.15 | 5.19 | 2.21 |
| (256k, 256k, LLaMA2-7B) | 4.51 | 2.87 | 2.53 | 2.39 | 1.95 |
| (128k, 256k, LLaMA2-7B (ft=128k)) | **2.66** | **2.38** | **2.28** | **2.26** | **1.87** |

This indicates that the current approach of fine-tuning from a 128k-checkpoint is the most effective. [p. 13]

**Fine-tuning cost.** LLaMA2-128k uses 8 A100 GPUs for a week to fine-tune 400 steps. LLaMA2-256k doubles the resources to 16 A100 GPUs for two weeks to fine-tune 600 steps. For Mistral-128k and 256k, with a training length of 16k, 4 A100 GPUs are employed for a 2-day fine-tuning period. [p. 13]

## A.3. Additional Details on the Search [p. 13]

**Figure 6** (p. 13): "Perplexity on the validation samples at each evolution search iteration. (a) The 64x extension for LLaMA2-7B to reach 256k context window size. (b) The 8x extension for LLaMA2-7B-256k to reach 2048k context window size. (c) The 16x extension for LLaMA2-7B-128k to reach 2048k context window size."

The figure has three subplots:
- **(a)** 4k to 256k (64x) search (y-axis: Perplexity on validation samples 0-1000+, x-axis: Evolution iterations 0-60). Three lines: PI (dashed, constant ~600), YaRN (dashed, constant ~400), and the search line (solid blue) starts above 1000 and drops rapidly to below 200 within ~10 iterations, continuing to decrease.
- **(b)** 256k to 2048k (8x) search (y-axis: ~4.1-4.4, x-axis: Evolution iterations 0-10). The search line starts at ~4.4 and decreases to ~4.1 over ~10 iterations.
- **(c)** 128k to 2048k (16x) search (y-axis: ~4.5-4.8, x-axis: Evolution iterations 0-15). The search line starts at ~4.8 and decreases to ~4.5 over ~15 iterations.

**Search efficiency.** Fig. 6 illustrates the perplexity on the validation samples at each evolution search iteration. The search algorithm can efficiently find high-quality non-uniform RoPE rescale factors. Specifically, on the 256k context window search (Fig. 6(a)), after the first iteration, solutions significantly better than PI and YaRN are found. As searching more iterations, the validation perplexity is significantly reduced from 273.27 to 118.47. Furthermore, YaRN, as the previous state-of-the-art non-uniform interpolation method, performs even worse than PI (linear interpolation) at the 64x extension. This also indicates that human-heuristic-based non-uniform interpolation is challenging to perform well in all scenarios. [p. 13]

For the extremely long context window at 2048k, the fine-tuned 128k and 256k context window LLaMA2-7B models are used for 16x and 8x extension, respectively. As shown in Fig. 6(bc), as expected, the perplexity of the 16x extension is larger than that of the 8x extension. Additionally, due to the time required for a single perplexity evaluation at 2048k is about 50 minutes, the search iterations are constrained. If more search time is allowed, it is highly possible to search better results. [p. 13]

**Search cost.** The search cost is primarily dependent on the time required to evaluate the perplexity of input context at a given context window size. For context window lengths up to 256k, the total search time is relatively quick, achievable within 3 days using a single A100 GPU. For a 512k context window, 2 A100 GPUs are employed. For larger context windows of 1024k and 2048k, 4 and 8 A100 GPUs respectively are utilized, managing to keep the total search time within a 5-day limit. [p. 13]
