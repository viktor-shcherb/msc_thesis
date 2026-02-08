# 1. Introduction [p. 1-4]

## Overview of Gemini 1.5

[p. 1] The paper presents two multimodal models from the Gemini line: Gemini 1.5 Pro and Gemini 1.5 Flash. They are members of Gemini 1.5, a family of highly-capable multimodal models incorporating innovations in sparse and dense scaling, as well as advances in training, distillation, and serving infrastructure. The models push the boundary of efficiency, reasoning, planning, multi-linguality, function calling, and long-context performance.

Gemini 1.5 models are built to handle extremely long contexts: they can recall and reason over fine-grained information from up to at least 10M tokens. This scale is unprecedented among contemporary LLMs, enabling processing of long-form mixed-modality inputs including entire collections of documents, multiple hours of video, and almost five days long of audio. [p. 1]

The Gemini 1.5 Pro presented in this report is an update over the previous Gemini 1.5 Pro February version; it outperforms its predecessor on most capabilities and benchmarks. The Gemini 1.5 series represents a generational leap in model performance and training efficiency: Gemini 1.5 Pro surpasses Gemini 1.0 Pro and 1.0 Ultra on a wide array of benchmarks while requiring significantly less compute to train. Similarly, Gemini 1.5 Flash performs uniformly better compared to 1.0 Pro and even performs at a similar level to 1.0 Ultra on several benchmarks. [p. 1]

## Historical context of long-context modeling

[p. 2] The ability to model increasingly longer contexts has tracked the development of more general and capable language models: from the toy 2-gram language model proposed by Shannon (1948), to modern n-gram models of the 1990s and 2000s typically constrained to 5 tokens of context (Brants et al., 2007; Chen and Goodman, 1999; Jelinek, 1998; Kneser and Ney, 1995), to recurrent neural networks language models from the 2010s which could effectively condition on hundreds of tokens (Jozefowicz et al., 2016; Mikolov et al., 2010), to the modern Transformer (Vaswani et al., 2017) which can condition on hundreds of thousands of tokens (Anthropic, 2023a). Gemini 1.5 Pro continues this trend by extending language model context lengths by over an order of magnitude.

Scaling to millions of tokens yields: continued improvement in predictive performance (Section 5.2.1.1), near-perfect recall (>99%) on synthetic retrieval tasks (Figure 1 and Section 5.2.1.2), and new capabilities like in-context learning from entire long documents and multimodal content (Section 5.2.2). [p. 2]

## Needle-in-a-haystack experiments

[p. 2-3] To measure the effectiveness of multimodal long-context capabilities, the authors conduct experiments on both synthetic and real-world tasks. In synthetic "needle-in-a-haystack" tasks inspired by Kamradt (2023), both Gemini 1.5 Pro and Gemini 1.5 Flash achieve near-perfect (>99%) "needle" recall up to multiple millions of tokens of "haystack" in all modalities (text, video, and audio). The performance of Gemini 1.5 Pro was also assessed when extending the context to 10M tokens across all three modalities; recall performance was maintained even with this significant increase in context size. [p. 2-3]

**Figure 1** (p. 2): "Gemini 1.5 Pro achieves near-perfect 'needle' recall (>99.7%) up to 1M tokens of 'haystack' in all modalities, i.e., text, video and audio. It even maintains this recall performance when extending to 10M tokens in the text modality (approximately 7M words); 9.7M tokens in the audio modality (up to 107 hours); 9.9M tokens in the video modality (up to 10.5 hours). The x-axis represents the context window, and the y-axis the depth percentage of the needle placed for a given context length. The results are color-coded to indicate: green for successful retrievals and red for unsuccessful ones. Note that the performance for all modalities is obtained with the previously reported Gemini 1.5 Pro version from February."

The figure shows three panels (Video Haystack, Audio Haystack, Text Haystack). The Video Haystack panel shows context windows from 6 to 60 minutes (left sub-panel) and 120 to 600 minutes (right sub-panel), with depth percentages from 0 to 100. Nearly all cells are green (successful retrieval). The Audio Haystack panel shows context from 12 to 636 minutes (left) and 640 to 5760 minutes (right), again nearly all green. The Text Haystack panel shows context from 32k to 512k tokens (left) and 1M to 10M tokens (right), with a small number of red (unsuccessful) cells appearing at 512k, 1M, 5M, and 10M token levels, concentrated at specific depth percentages (around 57-86% depth range).

## Win-rate comparisons

[p. 3] **Table 1** | **Gemini 1.5 Pro Win-rates** compared to Gemini 1.5 Pro from the February release, as well as the Gemini 1.0 family. Detailed results are presented in Table 10. * In speech recognition, any difference in Word Error Rate (WER) that falls within a 3% relative range is not statistically significant and is grouped as wins.

| Gemini 1.5 Pro | Relative to 1.5 Pro (Feb) | Relative to 1.0 Pro | Relative to 1.0 Ultra |
|---|---|---|---|
| Long-Context Text, Video & Audio | no change | from 32k up to 10M tokens | from 32k up to 10M tokens |
| Core Capabilities | Win-rate: 78.1% (25/32 benchmarks) | Win-rate: 88.0% (44/50 benchmarks) | Win-rate: 77.8% (35/45 benchmarks) |
| Text | Win-rate: 78.6% (11/14 benchmarks) | Win-rate: 95.8% (23/24 benchmarks) | Win-rate: 84.2% (16/19 benchmarks) |
| Vision | Win-rate: 92.3% (12/13 benchmarks) | Win-rate: 95.2% (20/21 benchmarks) | Win-rate: 85.7% (18/21 benchmarks) |
| Audio* | Win-rate: 80% (4/5 benchmarks) | Win-rate: 60% (3/5 benchmarks) | Win-rate: 40% (2/5 benchmarks) |

[p. 3] **Table 2** | **Gemini 1.5 Flash Win-rates** compared to Gemini 1.0 family. Gemini 1.5 Flash, while being smaller and way more efficient and faster to serve, maintains high levels of performance even as its context window increases. Detailed results are presented in Table 10.

| Gemini 1.5 Flash | Relative to 1.0 Pro | Relative to 1.0 Ultra |
|---|---|---|
| Long-Context Text, Video & Audio | from 32k up to 10M tokens | from 32k up to 10M tokens |
| Core Capabilities | Win-rate: 82.0% (41/50 benchmarks) | Win-rate: 46.7% (21/44 benchmarks) |
| Text | Win-rate: 94.7% (18/19 benchmarks) | Win-rate: 42.1% (8/19 benchmarks) |
| Vision | Win-rate: 90.5% (19/21 benchmarks) | Win-rate: 61.9% (13/21 benchmarks) |
| Audio | Win-rate: 0% (0/5 benchmarks) | Win-rate: 0% (0/5 benchmarks) |

## Long-context benchmarks and in-context learning

[p. 3-4] In realistic multimodal long-context benchmarks requiring retrieval *and* reasoning over multiple parts of the context (e.g., answering questions from long documents or long videos), Gemini 1.5 Pro outperforms all competing models across all modalities even when these models are augmented with external retrieval methods.

The authors showcase in-context learning abilities enabled by very long context: learning to translate a new language from a single set of linguistic documentation. With only instructional materials (a 500-page reference grammar, a dictionary, and approximately 400 extra parallel sentences) all provided in context, Gemini 1.5 Pro and Gemini 1.5 Flash are capable of learning to translate from English to Kalamang -- a Papuan language with fewer than 200 speakers and almost no online presence -- with quality similar to a person who learned from the same materials. [p. 3-4]

Additionally, 45 minutes of transcribed Kalamang speech recordings demonstrate that Gemini 1.5, for the first time with an LLM, can leverage mixed-modal documentation to learn speech recognition for a new language in context. [p. 4]

## Core capabilities are preserved

[p. 4] The leap in long-context performance does not come at the expense of the core multimodal capabilities of the model. (The authors define "core capabilities" as those capabilities of the model that are primarily non long-context, e.g., math, science, reasoning, code, similar to capabilities covered in the Gemini 1.0 Technical Report (Gemini-Team et al., 2023).^3) Across an extensive battery of evaluations, both Gemini 1.5 Pro and Gemini 1.5 Flash greatly surpass Gemini 1.0 Pro (44/50 for Gemini 1.5 Pro and 41/50 for Gemini 1.5 Flash). These include core capabilities such as:

- Math, Science and Reasoning: +49.6% and +30.8%, respectively (Sec. 6.1.1)
- Multilinguality: +21.4% and +16.7% (Sec. 6.1.4)
- Video Understanding: +18.7% and +7.5% (Sec. 6.2.4)
- Natural Image Understanding: +21.7% and +18.9% (Sec. 6.2.3)
- Chart and Document Understanding: +63.9% and +35.9% (Sec. 6.2.2)
- Multimodal Reasoning: +31.5% and +15.6% (Sec. 6.2.1)
- Code: +21.5% and +10.3% (Sec. 6.1.3)
- Function Calling: +72.8% and +54.6% (Sec. 6.1.5)
- Planning: (Sec. 5.2.2.7)
- Improving job productivity for professionals: (Sec. 6.1.7)

(See Table 10 and Table 2 for full breakdowns.) [p. 4]

Despite using significantly less training compute and being more efficient to serve, Gemini 1.5 Pro performs better on more than half of the overall benchmarks (35/45), and the majority of vision (18/21) and text (16/19) benchmarks when compared to Gemini 1.0 Ultra. For Gemini 1.5 Flash, it is better than Ultra 1.0 on the majority of vision benchmarks (13/21) and almost half the text benchmarks (8/18). [p. 4]

## Paper structure

[p. 4] The following sections provide: an overview of the model architecture, large-scale quantitative evaluations comparing Gemini 1.5 Pro and 1.5 Flash to other LLMs, detailed evaluations for long context capabilities followed by core capabilities, covering well-studied benchmarks across text, code, image, video and audio, and a discussion of responsible deployment (impact assessment, model policies, evaluations, mitigations of harm). The evaluation structure is similar to the Gemini 1.0 Technical Report (Gemini-Team et al., 2023). A model card (Mitchell et al., 2019a) is provided in Appendix Section 12.1.
