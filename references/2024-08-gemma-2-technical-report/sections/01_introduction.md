# 1. Introduction [p. 1]

Large language models (LLMs) have demonstrated strong capabilities in language understanding, generation, and reasoning (Brown et al., 2020; Radford et al., 2019; Raffel et al., 2019). Scaling has been key to this progress, with many new capabilities only emerging at scale (Brown et al., 2020). The newest large models reach unprecedented performance on reasoning benchmarks (Achiam et al., 2023), demonstrate multimodal and multilingual capabilities (Gemini Team, 2024), and can use context lengths of over 1M tokens (Gemini Team, 2024).

Small-scale models have also shown rapid performance increases, largely derived from increasing training length (Gemma Team, 2024; Jiang et al., 2023; Touvron et al., 2023). However, this approach only scales logarithmically with dataset size (Hoffmann et al., 2022), and the latest small models require up to 15T tokens to improve state of the art by less than 1-2% (AI@Meta, 2024). [p. 1]

The authors argue that small models are still under-trained and explore alternatives to improve small model performance without solely increasing training length. Their key approach is to improve the quality of information received by the network at each training step by replacing the next token prediction task with a richer objective. [p. 1]

## Knowledge Distillation Approach

The authors focus on knowledge distillation (Hinton et al., 2015), which replaces the one-hot token target with the distribution of potential next tokens computed from a large model. This approach is often used to reduce training time of smaller models by giving them richer gradients. In this work, they instead train for large quantities of tokens with distillation to simulate training beyond the number of available tokens. Concretely, they use a large language model as a teacher to train the 2B and 9B models on a quantity of tokens that is more than 50x the compute-optimal quantity predicted by theory (Hoffmann et al., 2022). They also release a 27B model trained from scratch. [p. 1]

## Architectural Modifications

The authors leverage several known modifications of Transformers: the interleaving of global and local attention layers from Beltagy et al. (2020a), and Grouped-Query Attention (GQA) from Ainslie et al. (2023). [p. 1]

## Key Claims

Overall, Gemma 2 is stated to significantly advance state-of-the-art performance relative to comparable-scale open models and to be competitive with some models more than twice their size (AI@Meta, 2024; Almazrouei et al., 2023; Jiang et al., 2023; xAI, 2024), across a variety of automated benchmarks and human evaluations. Example domains include question answering (Clark et al., 2019; Kwiatkowski et al., 2019), commonsense reasoning (Sakaguchi et al., 2019; Suzgun et al., 2022), mathematics and science (Cobbe et al., 2021; Hendrycks et al., 2020), and coding (Austin et al., 2021; Chen et al., 2021). [p. 1]
