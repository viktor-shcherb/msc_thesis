# 1 Introduction [p. 1-2]

[p. 1] Foundation models are general models of language, vision, speech, and/or other modalities designed to support a large variety of AI tasks. They form the basis of many modern AI systems.

The development of modern foundation models consists of two main stages: **(1)** a pre-training stage in which the model is trained at massive scale using straightforward tasks such as next-word prediction or captioning, and **(2)** a post-training stage in which the model is tuned to follow instructions, align with human preferences, and improve specific capabilities (e.g., coding and reasoning).

The paper presents **Llama 3**, a new set of foundation models for language. The Llama 3 Herd of models natively supports multilinguality, coding, reasoning, and tool usage. The largest model is a dense Transformer with 405B parameters, processing information in a context window of up to 128K tokens. Each member of the herd is listed in Table 1. All results in this paper are for the Llama 3.1 models, referred to as Llama 3 throughout for brevity. [p. 1]

Three key levers in development of high-quality foundation models: data, scale, and managing complexity. [p. 1]

- **Data.** Compared to prior versions of Llama (Touvron et al., 2023a,b), both the quantity and quality of data used for pre-training and post-training were improved. Improvements include more careful pre-processing and curation pipelines for pre-training data and more rigorous quality assurance and filtering approaches for post-training data. Llama 3 is pre-trained on a corpus of about 15T multilingual tokens, compared to 1.8T tokens for Llama 2. [p. 1]

- **Scale.** The flagship language model was pre-trained using 3.8 x 10^25 FLOPs, almost 50x more than the largest version of Llama 2. Specifically, a flagship model with 405B trainable parameters was pre-trained on 15.6T text tokens. As expected per scaling laws, the flagship model outperforms smaller models trained using the same procedure. While scaling laws suggest the flagship model is an approximately compute-optimal size for the training budget, smaller models are also trained for much longer than is compute-optimal. The resulting models perform better than compute-optimal models at the same inference budget. The flagship model is used to further improve the quality of those smaller models during post-training. [p. 1-2]

[p. 2]

- **Managing complexity.** Design choices seek to maximize ability to scale the model development process. They opt for a standard dense Transformer model architecture (Vaswani et al., 2017) with minor adaptations, rather than a mixture-of-experts model (Shazeer et al., 2017) to maximize training stability. They adopt a relatively simple post-training procedure based on supervised finetuning (SFT), rejection sampling (RS), and direct preference optimization (DPO; Rafailov et al. (2023)) as opposed to more complex reinforcement learning algorithms (Ouyang et al., 2022; Schulman et al., 2017) that tend to be less stable and harder to scale. [p. 2]

The result is Llama 3: a herd of three multilingual language models with 8B, 70B, and 405B parameters. Performance is evaluated on a plethora of benchmark datasets spanning a wide range of language understanding tasks, plus extensive human evaluations comparing Llama 3 with competing models. An overview of flagship performance on key benchmarks is in Table 2. [p. 2]

The experimental evaluation suggests the flagship model performs on par with leading language models such as GPT-4 (OpenAI, 2023a) across a variety of tasks, and is close to matching the state-of-the-art. The smaller models are best-in-class, outperforming alternative models with similar numbers of parameters (Bai et al., 2023; Jiang et al., 2023). Llama 3 also delivers a much better balance between helpfulness and harmlessness than its predecessor (Touvron et al., 2023b). A detailed safety analysis is in Section 5.4. [p. 2]

All three Llama 3 models are publicly released under an updated version of the Llama 3 Community License, including pre-trained and post-trained versions of the 405B parameter language model and a new version of the Llama Guard model (Inan et al., 2023) for input and output safety. [p. 2]

As part of the Llama 3 development process, multimodal extensions were also developed, enabling image recognition, video recognition, and speech understanding capabilities. These models are still under active development and not yet ready for release. [p. 2]

Note: Llama 3 8B and 70B were pre-trained on multilingual data but were intended for use in English at the time. [p. 2, footnote 1]

## Table 1 [p. 2]

**Table 1: Overview of the Llama 3 Herd of models.** All results in this paper are for the Llama 3.1 models.

|                        | Finetuned | Multilingual | Long context | Tool use | Release    |
|------------------------|-----------|--------------|--------------|----------|------------|
| Llama 3 8B             | x         | x^1          | x            | x        | April 2024 |
| Llama 3 8B Instruct    | check     | x            | x            | x        | April 2024 |
| Llama 3 70B            | x         | x^1          | x            | x        | April 2024 |
| Llama 3 70B Instruct   | check     | x            | x            | x        | April 2024 |
| Llama 3.1 8B           | x         | check        | check        | x        | July 2024  |
| Llama 3.1 8B Instruct  | check     | check        | check        | check    | July 2024  |
| Llama 3.1 70B          | x         | check        | check        | x        | July 2024  |
| Llama 3.1 70B Instruct | check     | check        | check        | check    | July 2024  |
| Llama 3.1 405B         | x         | check        | check        | x        | July 2024  |
| Llama 3.1 405B Instruct| check     | check        | check        | check    | July 2024  |

(check = supported, x = not supported; ^1 = pre-trained on multilingual data but intended for English)
