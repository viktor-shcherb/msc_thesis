# 3 Data Construction [p. 8]

**Figure 6** (p. 8): "Manuscript reasoning visualization. Kimi-VL-Thinking demonstrates the ability to perform historical and scientific inference by analyzing handwritten manuscripts step by step. In this example, our model identifies the author as Albert Einstein based on handwriting style, content analysis, and language cues. It reasons that the manuscripts relate to gravitational field equations, consistent with Einstein's contributions to general relativity."

Description: Two-panel visualization
- Key elements: Left panel shows "Instruction" with a handwritten manuscript image and prompt "Please step by step analyze who this manuscript belongs to and what it is about". Right panel shows detailed response with sections for Introduction, Analysis, Key Observations (Concerning Style, Content Language, Subject Matter, Context), and Conclusion with "Final Answer"
- Notable patterns: The model provides structured multi-step reasoning including handwriting analysis, content analysis (identifying mathematical equations and physical theories), contextual analysis (mentioning German terms and Einstein's contributions), leading to conclusion about authorship and topic (gravitational field equations and general relativity)
- Supports claim: Demonstrates the model's capability for complex historical and scientific inference through systematic visual analysis of handwritten documents

## 3.1 Pre-Training Data [p. 8]

Our multimodal pre-training corpus is designed to provide high-quality data that enables models to process and understand information from multiple modalities and sources including images and videos. To this end, we have also curated high-quality data from six categories – caption, interleaving, OCR, knowledge, video, and agent – to form the corpus.

When constructing our training corpus, we developed several multimodal data processing pipelines to ensure data quality, encompassing filtering, synthesis, and deduplication. Establishing an effective multimodal data strategy is crucial during the joint training of vision and language, as it both preserves the capabilities of the language model and facilitates alignment of knowledge across these modalities.

We provide a detailed description of these sources in this section, which is organized into the following categories:

### Caption Data [p. 8]

Our caption data provides the model with fundamental modality alignment and a broad range of world knowledge. By incorporating caption data, the multimodal LLM gains wider world knowledge with high learning efficiency. We have integrated various open-source Chinese and English caption datasets like (Schuhmann et al. 2022; Gadre et al. 2024) and also collected substantial in-house caption data from multiple sources. However, throughout the training process, we strictly limit the proportion of synthetic caption data to mitigate the risk of hallucination stemming from insufficient real-world knowledge.

---
[p. 9 continued]

For general caption data, we follow a rigorous quality control pipeline that avoids duplication and maintain high image text correlation. We also vary resolution during fine-training to ensure that the vision tower remains effective when processing images of both high- and low-resolution.

### Image-text Interleaving Data [p. 9]

During the pre-training phase, the multi-image comprehension ability can be boosted by interleaving data for many aspects. For example, multi-image comprehension ability can be boosted by interleaving data; interleaving data always provides detailed knowledge for the given image; a longer multimodal context learning ability can also be gained by interleaving data. What is more, we also hypothesize that interleaving can contribute positively to maintaining the model's language abilities. Thus, image-text interleaving data is an important part in our training corpus. Our multimodal corpus considered open-sourced interleave datasets like (Zhu et al. 2024; Laurençon et al. 2024) and also constructed large-scale in-house data using resources like textbooks, webpages, and tutorials. Further, we also find that synthesizing the interleaving data benefits the performance of multimodal LLM for knowledge. For example, we ensure each image's knowledge is sufficiently studied, for all the interleaving data, despite standard filtering, deduping, and other quality control pipeline, we also introduce a data ordering procedure to keep each image and text in the correct order.

### OCR Data [p. 9]

Optical Character Recognition (OCR) is a widely adopted technique that converts text from images into an editable format. In our model, a robust OCR capability is deemed essential for better aligning the model with human values. Accordingly, our OCR data are sampled from various diverse, dense source to in-house datasets, encompassing both clean and augmented images, and spanning over single-page and multi-page inputs.

In addition to the publicly available data, we have developed a substantial volume of in-house OCR datasets, covering multiple text layouts, web-based content, and handwritten examples. Furthermore, following the principles outlined in OCR 2.0 (Wei et al. 2024), our model is also equipped to handle a variety of optical image types, including figures, charts, geometry diagrams, music sheets, and mind maps. We apply several scene and augmentation techniques—such as rotation, distortion, color adjustments, and noise addition—to enhance the model's robustness. As a result, our model achieves a high level of OCR accuracy.

In addition to single-page OCR data, we collect and convert a large volume of in-house multi-page OCR data to activate the model's understanding of long documents in the real world. With the help of these data, our model is capable of performing accurate OCR on a single page or can even comprehend an entire academic paper or a scanned book.

### Knowledge Data [p. 9]

The concept of multimodal knowledge data is analogous to the previously mentioned text pre-training data, except here we focus on assembling a comprehensive repository of human knowledge from diverse sources to further enhance the model's capabilities. For example, carefully curated geometry data in our dataset is vital for developing visual reasoning skills, ensuring the model can interpret the abstract diagrams created by humans.

Our knowledge corpus adheres to a standardized taxonomy to balance content across various categories, ensuring diversity in data sources. Similar to text-only corpora, which gather knowledge from textbooks, research papers, and other academic materials, multimodal knowledge data cannot be simply sourced from these sources. While we also include filtered data from internet-based and other external resources.

Because a significant portion of our knowledge corpus is sourced from internet-based materials, infographics can cause the model to focus solely on OCR-based information. In such cases, relying exclusively on a basic OCR pipeline may limit training effectiveness. To address this, we have developed an additional pipeline that better captures the purely textual information embedded within images.

### Agent Data [p. 9]

For agent tasks, the model's grounding and planning capabilities have been significantly enhanced. In addition to utilizing publicly available data, a platform has been established to efficiently manage and execute virtual machine environments in bulk. Within these environments, heuristic methods were employed to collect screenshots and corresponding action data. This data was then processed into dense grounding formats and continuous trajectory formats. The design of the Action Space categorizes according to Desktop, Mobile, and Web environments. Furthermore, icon data was collected to strengthen the model's understanding of the meanings of icons within software graphical user interfaces (GUIs). To enhance the model's planning ability for solving multi-step desktop tasks, it as well as collected user-use trajectories with natural annotations, each accompanied by synthesized Chain-of-Thought (Agayts (Yiheng Xu et al. 2024)). These multi-step agent demonstrations equip Kimi-VL with the capability to complete real-world desktop tasks (on both Ubuntu and Windows).

### Video Data [p. 9]

In addition to image-only and image-text interleaved data, we also incorporate large-scale video data during pre-training, covering long videos, cooldown, and long-context activation stages to complete two directions of essential abilities of our model: first, to understand a long-context sequence dominated by images (e.g. hour-long videos) in addition to long text; second, to perceive fine-grained spatio-temporal correspondence in short video clips.

Our video data are sourced from diverse resources, including open-source datasets as well as in-house web-scale video data, and span videos of varying durations. Similarly, to ensure sufficient generalization ability, our video data cover a

---
[p. 10 continued]

wide range of scenes and diverse tasks. We cover tasks such as video description and video grounding, among others. For long videos, we carefully design a pipeline to produce dense captions. Similar to processing the caption data, we strictly limit the proportion of the synthetic dense video description data to reduce the risk of hallucinations.

### Text Data [p. 10]

Our text pretrain corpus directly reuses the data of our base LLM (J. Liu et al. 2025a), which is designed to provide comprehensive and high-quality data for training large language models (LLMs). It encompasses five domains: English, Chinese, Code, Mathematics & Reasoning, and Knowledge. We employ sophisticated filtering and quality control mechanisms for each data domain to ensure the highest quality training data. For all pretrain data, we conducted rigorous individual validation for each data source to assess its specific contribution to the overall training recipe. This systematic evaluation ensures the quality and effectiveness of our entire data composition for our model's overall composition of our training corpus; the sampling strategy for different document types is empirically determined through extensive experimentation. We consider not only identify document subsets that contribute most significantly to the model's knowledge acquisition capabilities. These high-value subsets are upsampled in the final training corpus. However, to maintain data diversity and ensure broader generalization, we carefully preserve a balanced representation of other document types at appropriate ratios. This data-driven approach helps us optimize the trade-off between focused knowledge acquisition and broad generalization capabilities.

## 3.2 Instruction Data [p. 10]

At this stage, the data is primarily aimed at enhancing the model's conversational abilities and instruction-following capabilities. To cover as many scenarios as possible, we rewrite the data across different domains. For non-reasoning tasks, including chart interpretation, agent grounding, OCR, image-grounded conversations, question-answering, writing, and text processing, we initially construct a seed dataset through human annotation. This seed dataset is used to train a seed model. Subsequently, we collect a diverse set of prompts and employ the seed model to generate multiple responses to each prompt. Annotators then rate these responses and refine the top-ranked responses to produce the final version. For reasoning tasks like visual coding, visual reasoning, and math/science problems, where rule-based and model-based verifications are more accurate and efficient than human judgment, we utilize rejection sampling to expand the SFT dataset. The complete vanilla SFT dataset comprises approximately a 1:1 ratio of text tokens to image tokens.

## 3.3 Reasoning Data [p. 10]

Our reasoning data is meticulously constructed for activation and enhancement of the model's multimodal reasoning capabilities during both the long-CoT supervised fine-tuning and reinforcement learning stages. Through developing a general pipeline that resembles rejection sampling for data engineering, we collect and synthesize an amount of high-quality long-CoT data. Specifically, we first assemble a collection of QA data with ground truth annotations that require multi-step reasoning, such as mathematical problem-solving and domain-specific VQA. Subsequently, we sample multiple detailed reasoning trajectories for each question by leveraging a powerful long-CoT model - Kimi k1.5 (K. Team et al. 2025) with curated reasoning prompts. In rejection sampling, we feed the true labels and model predictions into an off-the-shelf reward model. Wrong chain-of-thought responses are filtered out according to the model evaluation as well as some rule-based rewards, thus improving the reasoning data quality.
