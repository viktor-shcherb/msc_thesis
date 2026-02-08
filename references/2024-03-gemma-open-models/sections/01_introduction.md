# Introduction [p. 1-2]

Gemma is a family of open models based on Google's Gemini models (Gemini Team, 2023). [p. 1]

Gemma models are trained on up to 6T tokens of text, using architectures, data, and training recipes inspired by the Gemini model family. Like Gemini, these models achieve strong generalist capabilities in text domains, alongside state-of-the-art understanding and reasoning skills at scale. The authors release both pre-trained and fine-tuned checkpoints, as well as an open-source codebase for inference and serving. [p. 1]

Gemma comes in two sizes: a 7 billion parameter model for efficient deployment and development on GPU and TPU, and a 2 billion parameter model for CPU and on-device applications. Each size is designed to address different computational constraints, applications, and developer requirements. At each scale, raw pre-trained checkpoints and checkpoints fine-tuned for dialogue, instruction-following, helpfulness, and safety are released. [p. 1]

The authors thoroughly evaluate shortcomings on a suite of quantitative and qualitative benchmarks. They believe the release of both pretrained and fine-tuned checkpoints will enable thorough research and investigation into the impact of current instruction-tuning regimes, as well as the development of increasingly safe and responsible model development methodologies. [p. 1]

Gemma advances state-of-the-art performance relative to comparable-scale (and some larger) open models (Almazrouei et al., 2023; Jiang et al., 2023; Touvron et al., 2023a,b) across a wide range of domains including both automated benchmarks and human evaluation. Example domains include question answering (Clark et al., 2019; Kwiatkowski et al., 2019), commonsense reasoning (Sakaguchi et al., 2019; Suzgun et al., 2022), mathematics and science (Cobbe et al., 2021; Hendrycks et al., 2020), and coding (Austin et al., 2021; Chen et al., 2021). [p. 1]

Like Gemini, Gemma builds on recent work on sequence models (Sutskever et al., 2014) and transformers (Vaswani et al., 2017), deep learning methods based on neural networks (LeCun et al., 2015), and techniques for large-scale training on distributed systems (Barham et al., 2022; Dean et al., 2012; Roberts et al., 2023). Gemma also builds on Google's long history of open models and ecosystems, including Word2Vec (Mikolov et al., 2013), the Transformer (Vaswani et al., 2017), BERT (Devlin et al., 2018), and T5 (Raffel et al., 2019) and T5X (Roberts et al., 2022). [p. 1]

The authors believe the responsible release of LLMs is critical for improving the safety of frontier models, for ensuring equitable access to this breakthrough technology, for enabling rigorous evaluation and analysis of current techniques, and for enabling the development of the next wave of innovations. While thorough testing of all Gemma models has been conducted, testing cannot cover all applications and scenarios in which Gemma may be used. All Gemma users should conduct rigorous safety testing specific to their use case before deployment or use. [p. 1-2]

**Figure 1** (p. 2): "Language understanding and generation performance of Gemma 7B across different capabilities compared to similarly sized open models. We group together standard academic benchmark evaluations by capability and average the respective scores; see Table 6 for a detailed breakdown of performance."

The bar chart compares LLaMA 2 (7B), LLaMA 2 (13B), Mistral (7B), and Gemma (7B) across four capability categories:
- **Question Answering:** All models score roughly 55-65. Gemma 7B is competitive with or slightly above the others.
- **Reasoning:** LLaMA 2 (13B) and Gemma (7B) both score around 60-65; LLaMA 2 (7B) and Mistral (7B) are slightly lower.
- **Math / Science:** Gemma (7B) scores approximately 35-40, followed by Mistral (7B) around 30. LLaMA 2 (7B) scores around 15, and LLaMA 2 (13B) around 25.
- **Coding:** Gemma (7B) scores approximately 35-40, Mistral (7B) around 30. LLaMA 2 (13B) around 25, LLaMA 2 (7B) around 15.

The figure supports the claim that Gemma 7B demonstrates particularly strong performance on mathematics and coding benchmarks relative to similarly sized open models.

The technical report provides a detailed overview of the model architecture, training infrastructure, and pretraining and fine-tuning recipes for Gemma, followed by thorough evaluations of all checkpoints across a wide variety of quantitative and qualitative benchmarks, as well as both standard academic benchmarks and human-preference evaluations. The approach to safe and responsible deployment is discussed in detail. [p. 2]
