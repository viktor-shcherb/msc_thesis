# 1 Introduction [p. 3–4]

The Yi model series comprises 6B and 34B language models pretrained from scratch on 3.1T highly-engineered tokens, then finetuned on a small but meticulously polished alignment data. Due to data quality from substantial engineering efforts, Yi achieves near GPT-3.5 benchmark scores and human preferences. [p. 3]

## Design Dimensions

The authors describe four design dimensions concerning *model scale, data scale, and data quality*: [p. 3]

1. **Model scale:** The desiderata is a model small enough for inference on consumer-grade hardware like the RTX 4090 (limited 24G memory), yet large enough for complex reasoning and emergent abilities. 34B provides a good performance-cost balance; 34B is smaller than the conventional 70B used by Chinchilla [30] and LLaMA [77]. [p. 3]

2. **Data scale:** The pretrain data scale is increased to 3.1T tokens to compensate for reduced compute flops. This places the model-data combination in the post-Chinchilla optimal regime [64] -- the model is overtrained on more tokens (3T) than the compute optimal (around 1T). The benefit is from inference: after int4 [81] quantization, one can serve the 34B chat model on 24G GPU memory with almost no performance drop. [p. 3]

3. **Data engineering principle:** Promote quality over quantity for both pretraining and finetuning. Pretraining data quality is guaranteed by a sophisticated data cleaning pipeline with cascaded filtering methods and intentionally increased deduplication strength. [p. 3]

4. **Finetuning data:** Heavily emphasize quality by handcrafting less than 10K instructions over multiple iterations based on user feedback. This approach significantly deviates from quantity-scaling styled instruction tuning works like FLAN [9] and UltraChat [19], but aligns more with handcrafting styled works like LIMA [94]. [p. 3]

## Data Cleaning System

The pretraining data cleaning system features a sophisticated filtering pipeline based on language, heuristic textual features, perplexity, semantics, topic, and safety, as well as a cascaded deduplication process based on paragraph, MinHash, and exact matching. This leads to a much higher removal ratio than existing pipelines like CCNet [80], RefinedWeb [56], and RedPajama [13]. [p. 3]

The underlying principle: although pretraining requires data scaling, the data used are of high quality -- > "we prefer 3T tokens over sophisticated engineering over 10T tokens without extensive filtering" [p. 3].

## Model Architecture

Standard implementation of the Transformer architecture with Grouped-Query Attention (GQA) [1], SwiGLU [68] activation, and RoPE with an adjusted base frequency (RoPE ABF) [82]. This design choice is the standard approach rooted from the Transformer original paper [78], later modified by GPT-3 and Chinchilla [30], then followed by LLaMA [77], Baichuan [84], Qwen [3] and many related works. [p. 3]

## Finetuning Approach

The finetuning dataset is curated from carefully selected multi-turn instruction-response pairs, annotated directly by their team of machine learning engineers, then polished over multiple iterations of user feedback. The finetuning dataset size is less than 10K, but improved over and over across the model development timeline. An extensive grid search was employed to identify the optimal data composition, promote diversity, and discover effective hyperparameters. After 8-bit and 4-bit quantization, the final chat model can be deployed on consumer-grade GPUs nearly without performance degradation compared to the bf16 format. [p. 3]

## Capability Extensions

[p. 3]

- **Context scaling:** To achieve 200K context length, continue pretraining on about 5B length-upsampled data, similar to the concurrent work in Fu et al. [22].
- **Vision-language:** Integrate a vision encoder and develop a multi-stage training method, following and improving the practice of Liu et al. [47].
- **Depth-upscaling:** Study the effectiveness of depth-upscaling [38], making the model deeper by continual pretraining, confirming its effectiveness to further improve model performance.

## Infrastructure and Results

[p. 4]

Infrastructure provides strong support for the full-stack development of the Yi model series, from pretraining to finetuning to serving. For pretraining: cross-cloud elastic task scheduling, automatic failure recovery, and topology-aware resource allocation enabling task runs on real-time available GPU nodes across clusters with limited switching overhead. For finetuning: a hierarchical scheduling framework supporting different distributed backends for different models (e.g., Megatron [70] for the policy model and DeepSpeed [60] for the reward model). For efficient inference: 4-bit model and 8-bit KV cache quantization, combining with PagedAttention [41] and Dynamic Batching. [p. 4]

Extensive experiments demonstrate that Yi-34B can match GPT-3.5 in both performance and efficiency. On most standard benchmarks like MMLU [27] (for the base model) and LMSys ELO Rating [93] (for the chat model), Yi-34B generally achieves scores on par with GPT-3.5. After model parameter and KV cache quantization, inference cost is also controlled such that a wide range of the community can deploy the model on cost effective devices. [p. 4]

## Community Benefits

Since its release, the Yi model series has benefited the community from three perspectives: [p. 4]

1. It provides GPT-3.5-matching quality yet cost-effective models to researchers, and enables developers to build AI-native applications like language model based agents.
2. It empowers end users with locally runnable chatbots, which consequently helps protecting user data privacy.
3. It sheds light on the direction of further data and model scaling to achieve even stronger frontier models, for both research and commercial use.
