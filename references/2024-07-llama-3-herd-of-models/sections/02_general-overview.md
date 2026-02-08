# 2 General Overview [p. 3-4]

[p. 3] The model architecture of Llama 3 is illustrated in Figure 1. The development of the Llama 3 language models comprises two main stages:

- **Language model pre-training.** A large, multilingual text corpus is converted to discrete tokens and a large language model (LLM) is pre-trained on the resulting data to perform next-token prediction. In the pre-training stage, the model learns the structure of language and obtains large amounts of knowledge about the world from the text it is "reading". Pre-training is performed at massive scale: a model with 405B parameters on 15.6T tokens using a context window of 8K tokens. This standard pre-training stage is followed by a continued pre-training stage that increases the supported context to 128K tokens. See Section 3 for details. [p. 3]

- **Language model post-training.** The pre-trained language model has a rich understanding of language but does not yet follow instructions or behave as expected of an assistant. It is aligned with human feedback in several rounds, each involving supervised finetuning (SFT) on instruction tuning data and Direct Preference Optimization (DPO; Rafailov et al., 2024). At post-training, new capabilities such as tool-use are also integrated, and strong improvements in coding and reasoning are observed. Safety mitigations are also incorporated at the post-training stage (details in Section 5.4). See Section 4 for details. [p. 3]

Note: In this paper, "post-training" refers to any model training that happens outside of pre-training. [p. 3, footnote 2]

The resulting models have a rich set of capabilities: answering questions in at least eight languages, writing high-quality code, solving complex reasoning problems, and using tools out-of-the-box or in a zero-shot way. [p. 3]

Image, video, and speech capabilities are added to Llama 3 using a compositional approach. The approach comprises three additional stages illustrated in Figure 28: [p. 3-4]

- **Multi-modal encoder pre-training.** Separate encoders are trained for images and speech. The image encoder is trained on large amounts of image-text pairs, teaching the model the relation between visual content and natural language descriptions. The speech encoder is trained using a self-supervised approach that masks out parts of the speech inputs and tries to reconstruct the masked out parts via a discrete-token representation. See Section 7 for image encoder and Section 8 for speech encoder details. [p. 3-4]

- **Vision adapter training.** An adapter integrates the pre-trained image encoder into the pre-trained language model. The adapter consists of a series of cross-attention layers that feed image-encoder representations into the language model, trained on text-image pairs. During adapter training, the parameters of the image encoder are also updated but language-model parameters are intentionally not updated. A video adapter is also trained on top of the image adapter on paired video-text data, enabling the model to aggregate information across frames. See Section 7 for details. [p. 4]

- **Speech adapter training.** The speech encoder is integrated into the model via an adapter that converts speech encodings into token representations fed directly into the finetuned language model. The parameters of the adapter and encoder are jointly updated in a supervised finetuning stage. The language model is not changed during speech adapter training. A text-to-speech system is also integrated. See Section 8 for details. [p. 4]

The multimodal experiments lead to models that can recognize the content of images and videos, and support interaction via a speech interface. These models are still under development and not yet ready for release. [p. 4]

## Figure 1 [p. 4]

**Figure 1** (p. 4): "Illustration of the overall architecture and training of Llama 3. Llama 3 is a Transformer language model trained to predict the next token of a textual sequence. See text for details."

The figure shows a pipeline: INPUT Text tokens -> Token embeddings -> [Self-attention -> Feedforward network] -> ... -> [Self-attention -> Feedforward network] -> OUTPUT Text token. Labeled "AUTOREGRESSIVE DECODING" at the bottom. This illustrates the standard dense Transformer architecture with repeated self-attention and feedforward blocks.

## Table 2 [p. 3]

**Table 2: Performance of finetuned Llama 3 models on key benchmark evaluations.** The table compares performance of the 8B, 70B, and 405B versions of Llama 3 with competing models. Best-performing model in each of three model-size equivalence classes is boldfaced. ^delta = Results obtained using 5-shot prompting (no CoT). ^diamond = Results obtained using zero-shot prompting.

| Category      | Benchmark                    | Llama 3 8B | Gemma 2 9B | Mistral 7B | Llama 3 70B | Mixtral 8x22B | GPT 3.5 Turbo | Llama 3 405B | Nemotron 4 340B | GPT-4 (0125) | GPT-4o | Claude 3.5 Sonnet |
|---------------|------------------------------|------------|------------|------------|-------------|---------------|---------------|--------------|-----------------|--------------|--------|--------------------|
| General       | MMLU (5-shot)                | 69.4       | 72.3       | 61.1       | 83.6        | 76.9          | 70.7          | **87.3**     | 82.6            | 85.1         | 89.1   | **89.9**           |
|               | MMLU (0-shot, CoT)          | 73.0       | 72.3^delta | 60.5       | **86.0**    | 79.9          | 69.8          | **88.6**     | 78.7^diamond    | 85.4         | **88.7**| 88.3              |
|               | MMLU-Pro (5-shot, CoT)      | 48.3       | --         | 36.9       | **66.4**    | 56.3          | 49.2          | 73.3         | 62.7            | 64.8         | 74.0   | **77.0**           |
|               | IFEval                      | 80.4       | 73.6       | 57.6       | **87.5**    | 72.7          | 69.9          | **88.6**     | 85.1            | 84.3         | 85.6   | 88.0               |
| Code          | HumanEval (0-shot)          | **72.6**   | 54.3       | 40.2       | **80.5**    | 75.6          | 68.0          | **89.0**     | 73.2            | 86.6         | 90.2   | **92.0**           |
|               | MBPP EvalPlus (0-shot)      | **72.8**   | 71.7       | 49.5       | **86.0**    | 78.6          | 82.0          | **88.6**     | 72.8            | 83.6         | 87.8   | **90.5**           |
| Math          | GSM8K (8-shot, CoT)         | **84.5**   | 76.7       | 53.2       | **95.1**    | 88.2          | 81.6          | **96.8**     | 92.3^diamond    | 94.2         | 96.1   | 96.4^diamond       |
|               | MATH (0-shot, CoT)          | **51.9**   | 44.3       | 13.0       | **68.0**    | 54.1          | 43.1          | 73.8         | 41.1            | 64.5         | **76.6**| 71.1              |
| Reasoning     | ARC Challenge (0-shot)      | 83.4       | **87.6**   | 74.2       | **94.8**    | 88.7          | 83.7          | **96.9**     | 94.6            | 96.4         | 96.7   | 96.7               |
|               | GPQA (0-shot, CoT)          | 32.8       | --         | 28.8       | 46.7        | 33.3          | 30.8          | 51.1         | --              | 41.4         | 53.6   | **59.4**           |
| Tool use      | BFCL                        | 76.1       | --         | 60.4       | 84.8        | --            | --            | **85.9**     | 86.5            | --           | 88.3   | **90.2**           |
|               | Nexus                       | 38.5       | 30.0       | 24.7       | **56.7**    | 48.5          | 37.2          | **58.7**     | --              | 50.3         | 56.1   | 45.7               |
| Long context  | ZeroSCROLLS/QuALITY         | 81.0       | --         | --         | 90.5        | --            | --            | **95.2**     | --              | **95.2**     | 90.5   | 90.5               |
|               | InfiniteBench/En.MC         | 65.1       | --         | --         | 78.2        | --            | --            | **83.4**     | --              | 72.1         | 82.5   | --                 |
|               | NIH/Multi-needle            | 98.8       | --         | --         | 97.5        | --            | --            | 98.1         | --              | **100.0**    | **100.0**| 90.8             |
| Multilingual  | MGSM (0-shot, CoT)          | 68.9       | 53.2       | 29.9       | **86.9**    | 71.1          | 51.4          | **91.6**     | --              | 85.9         | 90.5   | 91.6               |
