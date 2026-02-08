# B Additional tables and charts [p. 15-18]

## B.1 GovReport evaluations [p. 15-16]

In Section 4.3.1, the authors mention the evaluation on GovReport documents. The evaluation results are detailed in Table 4. [p. 15]

**Table 4** (p. 16): "Sliding window perplexity ($S = 256$) of 50 long GovReport documents with a fixed context window size of 32k"

| Model Size | Model Name | Context Window | Extension Method | Perplexity |
|---|---|---|---|---|
| 7B | Together | 32k | PI | 3.67 |
| 7B | Code Llama | 100k | NTK | 4.44 |
| 7B | YaRN ($s = 16$) | 64k | YaRN | **3.59** |
| 7B | YaRN ($s = 32$) | 128k | YaRN | 3.64 |
| 13B | Code Llama | 100k | NTK | 4.22 |
| 13B | YaRN ($s = 16$) | 64k | YaRN | **3.35** |
| 13B | YaRN ($s = 32$) | 128k | YaRN | 3.39 |

## B.2 Passkey Retrieval [p. 15, 17]

[p. 15] The authors observe that the lowest perplexity point alone does not provide a comprehensive depiction on the "effective context size" that an LLM can attend to. While the Code Llama 13b model exhibits increasing perplexity above 100k context lengths, it was still able to accurately retrieve the passkey at a context length of 128k. This suggests that while the output of Code Llama might start to degrade in quality above 100k context size, it is still able to maintain strong retrieval capabilities. [p. 15]

In addition, as YaRN with $s = 32$ was trained for 200 more steps than YaRN with $s = 16$ while having a higher passkey accuracy with similar perplexity, the authors hypothesize that perplexity may not be a great indicator of whether an LLM is able to attend to all tokens and does not exhaustively determine long context performance. This also suggests that the YaRN models with $s = 16$ might be relatively undertrained for the passkey retrieval task. [p. 15]

**Table 5** (p. 17): "Passkey retrieval performance of various models. The passkey context denotes the maximum tested context window size where the accuracy of passkey retrieval was >= 80%, and the passkey accuracy is the average accuracy of passkey retrieval on all context sizes tested that were smaller or equal than the passkey context size."

| Model Size | Model Name | Scaling Factor ($s$) | Context Window | Training Data Context | Extension Method | Passkey Context | Passkey Accuracy |
|---|---|---|---|---|---|---|---|
| 7B | Together | 4 | 32k | 32k | PI | 32k | 100% |
| 7B | Code Llama | 88.6 | 100k | 16k | NTK | 112k | 94.3% |
| 7B | YaRN | 16 | 64k | 64k | YaRN | 64k | 96.3% |
| 7B | YaRN | 32 | 128k | 64k | YaRN | 128k | 99.4% |
| 13B | Code Llama | 88.6 | 100k | 16k | NTK | 128k | 99.4% |
| 13B | YaRN | 16 | 64k | 64k | YaRN | 64k | 97.5% |
| 13B | YaRN | 32 | 128k | 64k | YaRN | 128k | 99.4% |

## B.3 Dynamic scaling on models without any fine-tuning [p. 15, 17]

[p. 15] The authors first recall from Section 3.3 that the Dynamic Scaling technique is an inference-time technique that dynamically updates the factor $s$ in interpolation methods such as PI, "NTK-by-parts" and YaRN. They choose the original Llama 2, fix a sample in GovReport and calculate its perplexity on a sliding window of 256 tokens using RoPE, Dynamic-PI and Dynamic-YaRN. Since the original maximal context length of Llama 2 is 4096, they observe that Dynamic Scaling effectively extends the inference length and Dynamic-YaRN achieves better performance than Dynamic-PI. The resulting chart is in Figure 5. [p. 15]

Observations: [p. 15]
- Dynamic Scaling effectively prevents the blow-up of perplexity score beyond pretrained context window.
- Dynamic-YaRN outperforms Dynamic-PI in terms of long-range perplexity on pretrained Llama-2 without any finetuning.

**Figure 5** (p. 17): "The comparison between RoPE, Dynamic-PI and Dynamic-YaRN using Llama 2 on a long GovReport sample. This model has not been finetuned for long context."

The figure shows Perplexity (y-axis, range ~4.00 to ~5.50) vs. Context length in number of tokens (x-axis, range 0 to ~8000). Three lines are plotted:
- **RoPE** (blue): Perplexity stays around 4.2-4.3 until approximately 4000 tokens, then shoots up sharply to ~5.50 at ~5000 tokens (the 4096 context limit).
- **Dynamic-PI** (green): Follows RoPE closely until ~4000 tokens, then shows a moderate bump to ~4.5 before declining and stabilizing around 4.1-4.2 from ~5000 tokens onward through 8000.
- **Dynamic-YaRN** (orange): Very similar to Dynamic-PI but achieves slightly lower perplexity in the extended region (~5000-8000 tokens), stabilizing around 4.05-4.15.

This demonstrates that Dynamic Scaling prevents the catastrophic perplexity blow-up seen with unmodified RoPE beyond the pretrained context window, and Dynamic-YaRN provides a slight edge over Dynamic-PI.

## B.4 Mistral [p. 18]

The authors additionally extended the Mistral 7B v0.1 model [20], which broadly follows the Llama architecture. For Mistral they trained a 64k context window model ($s = 8$) for 1000 steps using 16k sequence lengths with a constant learning rate of $1 \times 10^{-6}$. The model's sliding window attention size was set to the context window size, effectively disabling sliding window attention. They then trained for an additional 500 steps at $s = 16$ to arrive at a 128k context window model. The training data was a mix of the pre-train and fine-tune splits of Together Computer's Long-Data Collections [3]. [p. 18]

The authors evaluated the models following the same procedure as described in 4.3.1, comparing against the base v0.1 model and MistralLite [1], an NTK-aware ($\theta = 1$M) version of v0.1. The results (Figure 6 and Table 6) were consistent with those of the Llama family of models. [p. 18]

**Figure 6** (p. 18): "Sliding window perplexity ($S = 256$) of ten 128k Proof-pile documents truncated to evaluation context window size"

The figure shows Perplexity (y-axis, range ~2.0 to ~3.4, lower is better) vs. Context Window (x-axis, range 0 to ~120,000). Four lines are plotted:
- **Yarn-Mistral-7b-64k** (blue): Starts around 3.2 at short contexts, decreases steadily to around 2.2 at ~60,000 tokens, then perplexity rises sharply beyond 64k.
- **Yarn-Mistral-7b-128k** (green): Similar starting point, decreases to ~2.1-2.2, and maintains low perplexity through ~120,000 tokens.
- **amazon/MistralLite** (orange/red): Starts around 3.2, decreases to ~2.4 at ~20,000 tokens, then rises back up beyond that.
- **mistralai/Mistral-7B-v0.1** (pink/red): Starts around 3.3, decreases to ~2.3 at ~8,000 tokens, then rises very sharply beyond the 8k context limit.

The YaRN-Mistral models maintain low perplexity across their respective context windows, consistent with the Llama results.

**Table 6** (p. 18): "Sliding window perplexity ($S = 256$) of ten 128k Proof-pile documents truncated to evaluation context window size"

| Model Size | Model Name | Context Window | Extension Method | 4096 | 8192 | 16384 | 65536 | 131072 |
|---|---|---|---|---|---|---|---|---|
| 7B | Mistral v0.1 | 8k | - | **3.09** | **2.96** | 36.8 | $> 10^3$ | $> 10^3$ |
| 7B | MistralLite | 16k | NTK | 3.26 | 3.13 | 47.3 | $> 10^3$ | $> 10^3$ |
| 7B | YaRN ($s = 8$) | 64k | YaRN | 3.18 | 3.04 | **2.65** | **2.20** | 57.4 |
| 7B | YaRN ($s = 16$) | 128k | YaRN | 3.21 | 3.08 | 2.68 | 2.24 | **2.19** |
