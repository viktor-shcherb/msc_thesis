# 2.3.5 More Details on Training Recipe (continued) [p. 7]

## Reward Modeling for Math (continued) [p. 7]

takes as input the "question," the "reference answer," and the "response," and outputs a single scalar that indicates whether the response is correct.

2. Chain-of-Thought RM: Recent research (Ankner et al. 2024; McAleese et al. 2024) suggests that reward models augmented with chain-of-thought (CoT) reasoning can significantly outperform classic approaches, particularly on tasks where nuanced correctness criteria matter—such as mathematics. Therefore, we collected an equally large dataset of about 800k CoT-labeled examples to fine-tune the Kimi model. Building on the same inputs as the Classic RM, the chain-of-thought approach explicitly generates a step-by-step reasoning process before providing a final correctness judgment in JSON format, enabling more robust and interpretable reward signals.

During manual spot checks, the Classic RM achieved an accuracy of approximately **84.4**, while the Chain-of-Thought RM reached **98.5** accuracy [p. 7]. In the RL training process, the authors adopted the Chain-of-Thought RM to ensure more correct feedback.

## Vision Data [p. 7]

To improve the model's real-world image reasoning capabilities and to achieve a more effective alignment between visual inputs and large language models (LLMs), their vision reinforcement learning (Vision RL) data is primarily sourced from three distinct categories [p. 7]:

1. **Real-world data**: Encompasses a range of science questions across various grade levels that require graphical comprehension and reasoning, location guessing tasks that necessitate visual perception and inference, and data analysis that involves understanding complex charts, among other types of data. These datasets improve the model's ability to perform visual reasoning in real-world scenarios.

2. **Synthetic visual reasoning data**: Artificially generated, including procedurally created images and scenes aimed at improving specific visual reasoning skills, such as understanding spatial relationships, geometric patterns, and object interactions. These synthetic datasets offer a controlled environment for testing the model's visual reasoning capabilities and provide an endless supply of training examples.

3. **Text-rendered data**: Created by converting textual content into visual format, enabling the model to maintain consistency when handling text-based queries across different modalities. By transforming text documents, code snippets, and structured data into images, the model provides consistent responses regardless of whether the input is pure text or text rendered as images (like screenshots or photos). This also helps to enhance the model's capability when dealing with text-heavy images.

Each type of data is essential in building a comprehensive visual language model that can effectively manage a wide range of real-world applications while ensuring consistent performance across various input modalities [p. 7].

# 2.4 Long2short: Context Compression for Short-CoT Models [p. 7-8]

Though long-CoT models achieve strong performance, they consume more test-time tokens compared to standard short-CoT LLMs. However, it is possible to transfer the thinking priors from long-CoT models to short-CoT models so that performance can be improved even with limited test-time token budgets. Several approaches are presented for this long2short problem, including model merging (Yang et al. 2024), shortest rejection sampling, DPO (Rafailov et al. 2024), and long2short RL [p. 7].

**Model Merging** Model merging has been found to be useful in maintaining generalization ability. The authors also discovered its effectiveness in improving token efficiency when merging a long-CoT model and a short-CoT model. This approach combines a long-CoT model with a shorter model to obtain a new one without training. Specifically, the two models are merged by simply averaging their weights [p. 7].

**Shortest Rejection Sampling** The model generates responses with a large length variation for the same problem. Based on this, the Shortest Rejection Sampling method samples the same question $n$ times (in their experiments, $n = 8$) and selects the shortest correct response for supervised fine-tuning [p. 7].

**DPO** Similar to Shortest Rejection Sampling, the Long CoT model is used to generate multiple response samples. The shortest correct solution is selected as the positive sample, while longer responses are treated as negative samples, including both wrong longer responses and correct longer responses (1.5 times longer than the chosen positive sample). These positive-negative pairs form the pairwise preference data used for DPO training [p. 7].

**Long2short RL** After a standard RL training phase, a model that offers the best balance between performance and token efficiency is selected to serve as the base model, and a separate long2short RL training phase is conducted. In this second phase, the length penalty introduced in Section 2.3.3 is applied, and the maximum rollout length is significantly reduced to further penalize responses that exceed the desired length while possibly correct [p. 8].

# 2.5 Other Training Details [p. 8]

## 2.5.1 Pretraining [p. 8]

The Kimi k1.5 base model is trained on a diverse, high-quality multimodal corpus. The language data covers five domains: English, Chinese, Code, Mathematics Reasoning, and Knowledge. Multimodal data, including Captioning, Image-text Interleaving, OCR, Knowledge, and QA datasets, enables the model to acquire vision-language capabilities. Rigorous quality control ensures relevance, diversity, and balance in the overall pretrain dataset [p. 8].

Pretraining proceeds in three stages [p. 8]:
1. **Vision-language pretraining**: A strong language foundation is established, followed by gradual multimodal integration
2. **Cooldown**: Consolidates capabilities using curated and synthetic data, particularly for reasoning and knowledge-based tasks
3. **Long-context activation**: Extends sequence processing to 131,072 tokens

More details regarding pretraining efforts can be found in Appendix B [p. 8].

## 2.5.2 Vanilla Supervised Finetuning [p. 8]

The vanilla SFT corpus covers multiple domains [p. 8]:
- **Non-reasoning tasks** (question-answering, writing, text processing): Initially a seed dataset is constructed through human annotation, used to train a seed model. Then diverse prompts are collected and the seed model generates multiple responses to each prompt. Annotators rank these responses and refine the top-ranked response to produce the final version.
- **Reasoning tasks** (math, coding): Where rule-based and reward modeling based verifications are more accurate and efficient than human judgment, rejection sampling is used to expand the SFT dataset.

**Dataset composition** [p. 8]:
- **~1 million text examples**: 500k for general question answering, 200k for coding, 200k for math and science, 5k for creative writing, and 20k for long-context tasks (summarization, doc-qa, translation, writing)
- **1 million text-vision examples**: Chart interpretation, OCR, image-grounded conversations, visual coding, visual reasoning, and math/science problems with visual aids

**Training procedure** [p. 8]:
- First trained at sequence length of 32k tokens for 1 epoch, followed by another epoch at 128k tokens
- First stage (32k): learning rate decays from $2 \times 10^{-5}$ to $2 \times 10^{-6}$
- Second stage (128k): re-warmup to $1 \times 10^{-5}$, then decay to $1 \times 10^{-6}$
- Multiple training examples packed into each single training sequence for efficiency
