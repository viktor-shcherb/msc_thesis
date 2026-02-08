# 4 Experiments [p. 6]

StreamingLLM is evaluated using four prominent recent model families:
- **Llama-2** (Touvron et al., 2023b)
- **MPT** (Team, 2023)
- **Pythia** (Biderman et al., 2023)
- **Falcon** (Almazrouei et al., 2023)

Notably, Llama-2, Falcon, and Pythia incorporate RoPE (Su et al., 2021), whereas MPT employs ALiBi (Press et al., 2022) --- two of the most influential position encoding techniques in recent research. [p. 6]

The diverse model selection ensures the validity and robustness of the findings. StreamingLLM is benchmarked against established baselines: dense attention, window attention, and the sliding window approach with re-computation. In all subsequent experiments with StreamingLLM, four initial tokens are used as attention sinks unless stated otherwise. [p. 6]

## 4.1 Language Modeling on Long Texts Across LLM Families and Scales [p. 6]

StreamingLLM's language modeling perplexity is evaluated using the concatenated PG19 (Rae et al., 2020) test set, which contains 100 long books. [p. 6]

**Experimental setup:**
- For Llama-2 models, the cache size is set at 2048.
- For Falcon, Pythia, and MPT models, the cache size is set at 1024. This is half the pre-training window size, chosen to enhance visualization clarity. [p. 6]

**Results on 20K tokens (Figure 3):** StreamingLLM can match the oracle baseline (sliding window with re-computation) in terms of perplexity on texts spanning 20K tokens. Meanwhile, the dense attention technique fails when the input length exceeds its pre-training window, and the window attention technique struggles when the input length surpasses the cache size, leading to the eviction of the initial tokens. [p. 6]

**Results on 4M+ tokens (Figure 5):** StreamingLLM can reliably handle exceptionally extended texts, encompassing more than 4 million tokens, across a spectrum of model families and scales. This includes Llama-2-[7,13,70]B, Falcon-[7,40]B, Pythia-[2.8,6.9,12]B, and MPT-[7,30]B. [p. 6]

**Figure 5** (p. 7): "Language modeling perplexity of StreamingLLM on super long texts with 4 million tokens across various LLM families and scales. The perplexity remains stable throughout. We use the concatenated test set of PG19 (100 books) to perform language modeling, with perplexity fluctuations due to book transitions."
Four subplots, one per model family:
- Llama-2 (StreamingLLM): Llama-2-7B, Llama-2-13B, Llama-2-70B. X-axis: Input Length (0 to 4M). Y-axis: Perplexity (~0.5 to 1.5). All variants show stable perplexity around ~1.0 across the full 4M token range with minor fluctuations from book transitions.
- Pythia (StreamingLLM): Pythia-2.8B, Pythia-6.9B, Pythia-12B. Same stable trend.
- Falcon (StreamingLLM): Falcon-7B, Falcon-40B. Same stable trend.
- MPT (StreamingLLM): MPT-7B, MPT-30B. Same stable trend.
The figure demonstrates StreamingLLM maintains stable perplexity at scale across all four model families.

**Figure 7** (p. 7): "Visualization of average attention logits over 256 sentences, each 16 tokens long, comparing models pre-trained without (left) and with (right) a sink token. Both maps show the same layers and heads. Key observations: (1) Without a sink token, models show local attention in lower layers and increased attention to initial tokens in deeper layers. (2) With a sink token, there is clear attention directed at it across all layers, effectively collecting redundant attention. (3) With the presence of the sink token, less attention is given to other initial tokens, supporting the benefit of designating the sink token to enhance the streaming performance."
Left panel ("Pre-Trained without Sink Token"): Three attention heatmaps (Layer 0 Head 0, Layer 2 Head 0, Layer 10 Head 0) showing local diagonal attention in early layers and a strong first-column stripe emerging in deeper layers (Layer 10).
Right panel ("Pre-Trained with Sink Token"): Same three layers/heads. A pronounced first-column stripe (the sink token) is present across all layers including early ones. Other initial tokens receive less attention compared to the left panel.

## 4.2 Results of Pre-Training with a Sink Token [p. 7]

To validate that introducing a sink token to all pre-training samples improves streaming LLMs, two language models were trained, each with 160 million parameters, under identical conditions. One model adhered to the original training settings, the other incorporated a sink token at the start of every training sample. [p. 7]

**Training details:**
- Architecture: Pythia-160M (Biderman et al., 2023) codebase and training recipe
- Hardware: 8xA6000 NVIDIA GPU server
- Dataset: deduplicated Pile (Gao et al., 2020)
- Batch size: reduced from original to 256
- All other Pythia training configurations retained: learning rate schedules, model initialization, dataset permutations
- Training duration: 143,000 steps [p. 7]

### Convergence and Normal Model Performance [p. 7]

Including a sink token during pre-training has no negative impact on model convergence and subsequent performance on a range of NLP benchmarks. Models trained with a sink token exhibit similar convergence dynamics compared to their vanilla counterparts (Figure 6). [p. 7]

**Figure 6** (p. 7): "Pre-training loss curves of models w/ and w/o sink tokens. Two models have a similar convergence trend."
X-axis: Steps (0 to ~140K, labeled as 0 to 140 in units of K). Y-axis: Training Loss (~2.5 to 2.8). Both Vanilla and +Sink Token curves decrease smoothly and overlap closely, confirming that the sink token does not harm convergence.

The two models are evaluated on seven diverse NLP benchmarks: ARC-[Challenge, Easy] (Clark et al., 2018), HellaSwag (Zellers et al., 2019), LAMBADA (Paperno et al., 2016), OpenbookQA (Mihaylov et al., 2018), PIQA (Bisk et al., 2020), and Winogrande (Sakaguchi et al., 2019). [p. 7]

**Table 4** (p. 7): "Zero-shot accuracy (in %) across 7 NLP benchmarks, including ARC-[Challenge, Easy], HellaSwag, LAMBADA, OpenbookQA, PIQA, and Winogrande. The inclusion of a sink token during pre-training doesn't harm the model performance."

| Methods | ARC-c | ARC-e | HS | LBD | OBQA | PIQA | WG |
|---|---|---|---|---|---|---|---|
| Vanilla | 18.6 | 45.2 | 29.4 | 39.6 | 16.0 | 62.2 | 50.1 |
| +Sink Token | 19.6 | **45.6** | **29.8** | **39.9** | **16.6** | **62.6** | **50.8** |

As shown in Table 4, the model pre-trained with a sink token performs similarly to that trained using the vanilla approach. [p. 7]

### Streaming Performance [p. 7]

As illustrated in Table 3, the streaming perplexities differ between models trained using traditional methods and those augmented with a sink token. The vanilla model requires the addition of multiple tokens as attention sinks to maintain stable streaming perplexity. In contrast, the model trained with a sink token achieves satisfactory streaming performance using just the sink token. [p. 7]

## 4.3 Results on Streaming Question Answering with Instruction-tuned Models [p. 8]

To show StreamingLLM's real-world applicability, the authors emulate multi-round question-answering using instruction-tuned LLMs, commonly used in real-world scenarios. [p. 8]

All question-answer pairs from the ARC-[Challenge, Easy] datasets are concatenated, fed the continuous stream to Llama-2-[7,13,70]B-Chat models, and model completions are assessed at each answer position using an exact match criterion. [p. 8]

**Table 5** (p. 8): "Accuracy (in %) on the ARC-[Easy, Challenge] datasets. Questions were concatenated and answered in a streaming manner to mimic a real-world chat setting. The dense baseline fails due to Out-of-Memory (OOM) errors. Window attention has poor accuracy. StreamingLLM has comparable results with the one-shot sample-by-sample baseline. Window attention and StreamingLLM use cache sizes of 1024."

| Model | Llama-2-7B-Chat | | Llama-2-13B-Chat | | Llama-2-70B-Chat | |
|---|---|---|---|---|---|---|
| Dataset | Arc-E | Arc-C | Arc-E | Arc-C | Arc-E | Arc-C |
| One-shot | 71.25 | 53.16 | 78.16 | 63.31 | 91.29 | 78.50 |
| Dense | 3.58 | 1.39 | OOM | OOM | 0.12 | 0.32 |
| Window | 71.34 | 55.03 | 0.25 | 0.34 | 0.12 | 0.32 |
| StreamingLLM | 71.34 | 55.03 | 80.89 | 65.61 | 91.37 | 80.20 |

Dense attention results in Out-of-Memory (OOM) errors for Llama-2-13B-Chat, showing it unsuitable for this setting. Window attention works efficiently but exhibits low accuracy due to random outputs when the input length exceeds the cache size. StreamingLLM excels by efficiently handling the streaming format, aligning with the one-shot, sample-by-sample baseline accuracy. [p. 8]

### StreamEval Benchmark [p. 8]

A new dataset, StreamEval, is introduced, inspired by the LongEval (Li et al., 2023) benchmark. As depicted in Figure 8, diverging from LongEval's single query over a long-span setup, the model is queried every 10 lines of new information. Each query's answer is consistently 20 lines prior, reflecting real-world instances where questions typically pertain to recent information. [p. 8]

**Figure 8** (p. 8): "The first sample in StreamEval."
Shows an input content block with a record of lines containing REGISTER_CONTENT values at specific lines (line 0 = <8806>, line 10 = <24879>, line 20 = <45603>, line 21 = <29189>, line 30 = <3668>, line 31 = <42569>, line 40 = <34579>). Queries highlighted in yellow/red ask "The REGISTER_CONTENT in line 0 is", "The REGISTER_CONTENT in line 10 is", "The REGISTER_CONTENT in line 20 is" at periodic intervals. The desired output is the corresponding values: ["<8806>", "<24879>", "<45603>", ...].

**Figure 9** (p. 8): "Performance on the StreamEval benchmark. Accuracies are averaged over 100 samples."
Four subplots:
- Llama-2-7b-Chat: Dense Attention accuracy drops to ~0 at ~4K input length. Window Attention drops similarly. StreamingLLM maintains ~0.8-1.0 accuracy up to ~120K tokens.
- Llama-2-13b-Chat: Similar pattern; StreamingLLM maintains stable accuracy to 120K.
- LongChat-7b-v1.5-32k: Dense and Window drop at their respective limits. StreamingLLM maintains high accuracy to 120K.
- Llama-2-7B-32KInstruct: Same stable StreamingLLM performance to 120K. Dense Attention sustains longer (up to ~20-30K) before dropping, consistent with the extended context window.

LLMs employing StreamingLLM maintain reasonable accuracy even as input lengths approach 120K tokens. Both dense and window attention fail at the pre-training text length and the KV cache size, respectively. [p. 8]

Two context-extended models are also used: LongChat-7b-v1.5-32k (Li et al., 2023) and Llama-2-7B-32K-Instruct (Together, 2023), to show that StreamingLLM can complement context extension techniques. Within StreamingLLM, context extension means broadening the maximum cache size of streaming LLMs, enabling the capture of broader local information. [p. 8]
