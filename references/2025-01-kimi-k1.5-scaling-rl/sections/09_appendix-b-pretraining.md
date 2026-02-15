# Appendix B: Pretraining [p. 21–25]

## Introduction [p. 21]

Reinforcement learning (RL) efficiency is closely tied to the performance of the underlying base model [p. 21]. Frontier models such as Gemini (Team et al. 2024) and Llama (Grattafiori et al. 2024) highlight the importance of pretraining data quality in achieving high performance [p. 21]. However, **many recent open-source models lack full transparency regarding their data processing pipelines and recipes**, creating challenges for broader community understanding [p. 21].

While the authors are not open-sourcing their proprietary model at this time, they are committed to providing a comprehensive disclosure of their data pipeline and methodologies [p. 21]. In this appendix section, they focus primarily on the multimodal pretraining data recipe, followed by a brief discussion of the model architecture and training stages [p. 21].

## B.1 Language Data [p. 21–22]

The pretrain corpus is designed to provide comprehensive and high-quality data for training large language models (LLMs) [p. 21]. It encompasses five domains [p. 21]:

1. English
2. Chinese
3. Code
4. Mathematics & Reasoning
5. Knowledge

The authors employ sophisticated filtering and quality control mechanisms for each domain to ensure the highest quality training data [p. 21]. For all pretrain data, they conducted **rigorous individual validation for each data source** to assess its specific contribution to the overall training recipe [p. 21]. This systematic evaluation ensures the quality and effectiveness of their diverse data composition [p. 21].

### English and Chinese textual data [p. 21]

The authors developed a multi-dimensional quality filtering framework that combines multiple scoring methods to reduce individual biases and ensure comprehensive quality assessment [p. 21].

The framework incorporates [p. 21]:

**1. Rule-based filtering** [p. 21]:
- Implements domain-specific heuristics to remove problematic content, including duplicate content, machine-translated text, and low-quality web scrapes [p. 21]
- Filters out documents with excessive special characters, unusual formatting, or spam patterns [p. 21]

**2. FastText-based classification** (Joulin et al. 2016; J. Li et al. 2024) [p. 21]:
- Trained specialized FastText models to identify content quality based on linguistic features and semantic coherence [p. 21]
- Helps identify documents with natural language flow and proper grammatical structure [p. 21]

**3. Embedding-based similarity analysis** (Jianlv Chen et al. 2024) [p. 21]:
- Uses document embeddings to compute document-level similarity scores [p. 21]
- Identifies and removes near-duplicates while preserving semantically valuable variations [p. 21]
- This approach helps maintain diversity in the training corpus [p. 21]

**4. LLM-based quality assessment** (following Penedo et al. 2024) [p. 21]:
- Leverages LLMs to score documents based on coherence, informativeness, and potential educational value [p. 21]
- This method is particularly effective at identifying nuanced quality indicators that simpler methods might miss [p. 21]

**Final quality scoring and sampling** [p. 21]:

The final quality score for each document is calculated as a combination of these individual scores [p. 21]. Based on extensive empirical analysis, the authors implement **dynamic sampling rates**, where high-quality documents are upsampled, while low-quality documents are downsampled during training [p. 21].

### Code data [p. 21]

The code data primarily consists of two categories [p. 21]:

**Pure code data from code files** [p. 21]:

The authors adhered to the methodology of BigCode (R. Li et al. 2023; Lozhkov et al. 2024) and conducted a comprehensive preprocessing of the dataset [p. 21]:

- Initially eliminated miscellaneous languages [p. 21]
- Applied a rule-based cleaning procedure to enhance data quality [p. 21]
- Addressed language imbalance through strategic sampling techniques [p. 21]
- Specifically:
  - **Markup languages** such as JSON, YAML, and YACC were down-sampled [p. 21]
  - **32 major programming languages**, including Python, C, C++, Java, and Go, were up-sampled to ensure a balanced representation [p. 21]

**Text-code interleaved data** [p. 21]:

For text-code interleaved data sourced from various data sources, the authors use an **embedding-based method to recall high-quality data** [p. 21]. This approach ensures the diversity of the data and maintains its high quality [p. 21].

### Math & Reasoning data [p. 21–22]

The mathematics and reasoning component of the dataset is crucial for developing strong analytical and problem-solving capabilities [p. 21]. The mathematical pre-training data are mainly retrieved from web text and PDF documents collected from publicly available internet sources (Paster et al. 2023) [p. 21].

**Key challenge identified** [p. 21]:

Initially, the authors discovered that their general-domain text extraction, data cleaning process and OCR models exhibited **high false negative rates in the mathematical domain** [p. 21]. Therefore, they first developed specialized data cleaning procedures and OCR models specifically for mathematical content, aiming to maximize the recall rate of mathematical data [p. 22].

**Two-stage data cleaning process** [p. 22]:

1. Using FastText model for initial cleaning to remove most irrelevant data [p. 22]
2. Utilizing a fine-tuned language model to further clean the remaining data, resulting in high-quality mathematical data [p. 22]

### Knowledge data [p. 22]

The knowledge corpus is meticulously curated to ensure a comprehensive coverage in academic disciplines [p. 22]. The knowledge base primarily consists of academic exercises, textbooks, research papers, and other general educational literature [p. 22]. A significant portion of these materials is digitized through OCR processing, for which the authors have developed proprietary models optimized for academic content, particularly for handling mathematical formulas and special symbols [p. 22].

**Multi-dimensional annotation** [p. 22]:

The authors employ internal language models to annotate documents with multi-dimensional labels, including:

1. OCR quality metrics to assess recognition accuracy [p. 22]
2. Educational value indicators measuring pedagogical relevance [p. 22]
3. Document type classification (e.g., exercises, theoretical materials) [p. 22]

**Filtering and sampling pipeline** [p. 22]:

Based on these multi-dimensional annotations, the authors implement a sophisticated filtering and sampling pipeline:

- **First:** Documents are filtered through OCR quality thresholds [p. 22]. The OCR quality assessment framework places special attention on detecting and filtering out common OCR artifacts, particularly repetitive text patterns that often indicate recognition failures [p. 22].

- **Second:** The authors carefully evaluate the educational value of each document through their scoring system [p. 22]. Documents with high pedagogical relevance and knowledge depth are prioritized, while maintaining a balance between theoretical depth and instructional clarity [p. 22]. This helps ensure that the training corpus contains high-quality educational content that can effectively contribute to the model's knowledge acquisition [p. 22].

- **Finally:** The sampling strategy for different document types is empirically determined through extensive experimentation [p. 22]. The authors conduct isolated evaluations to identify document subsets that contribute most significantly to the model's knowledge acquisition capabilities [p. 22]. These high-value subsets are upsampled in the final training corpus [p. 22]. However, to maintain data diversity and ensure model generalization, they carefully preserve a balanced representation of other document types at appropriate ratios [p. 22]. This data-driven approach helps optimize the trade-off between focused knowledge acquisition and broad generalization capabilities [p. 22].

## B.2 Multimodal Data [p. 22–23]

The multi-modal pretraining corpus is designed to provide high-quality data that enables models to process and understand information from multiple modalities, including text, images, and videos [p. 22]. The authors have curated high-quality data from five categories—captioning, interleaving, OCR (Optical Character Recognition), knowledge, and general question answering—to form the corpus [p. 22].

When constructing the training corpus, the authors developed several multi-modal data processing pipelines to ensure data quality, encompassing filtering, synthesis, and deduplication [p. 22]. Establishing an effective multi-modal data strategy is crucial during the joint training of vision and language, as it both preserves the capabilities of the language model and facilitates alignment of knowledge across diverse modalities [p. 22].

### Caption data [p. 22]

Caption data provides the model with fundamental modality alignment and a broad range of world knowledge [p. 22]. By incorporating caption data, the multi-modal LLM gains wider world knowledge with high learning efficiency [p. 22]. 

**Data sources** [p. 22]:
- Integrated various open-source Chinese and English caption datasets like Schuhmann et al. 2022; S. Y. Gadre et al. 2024 [p. 22]
- Collected substantial in-house caption data from multiple sources [p. 22]

**Quality control** [p. 22]:
- Throughout the training process, the authors **strictly limit the proportion of synthetic caption data** to mitigate the risk of hallucination stemming from insufficient real-world knowledge [p. 22]
- For general caption data, they follow a rigorous quality control pipeline that avoids duplication and maintains high image-text correlation [p. 22]
- They also vary image resolution during pretraining to ensure that the vision tower remains effective when processing images of both high- and low-resolution [p. 22]

### Image-text interleaving data [p. 22–23]

During the pretraining phase, the model benefits from interleaving data for many aspects [p. 23]:
- Multi-image comprehension ability can be boosted by interleaving data [p. 23]
- Interleaving data always provides detailed knowledge for the given image [p. 23]
- A longer multi-modal context learning ability can also be gained by the interleaving data [p. 23]
- The authors also find that interleaving data contributes positively to maintaining the model's language abilities [p. 23]

Thus, image-text interleaving data is an important part in the training corpus [p. 23].

**Data sources** [p. 23]:
- Considered open-sourced interleave datasets like Zhu et al. 2024; Laurençon et al. 2024 [p. 23]
- Constructed large-scale in-house data using resources like textbooks, webpages and tutorials [p. 23]

**Quality control** [p. 23]:
- The authors also find that synthesizing the interleaving data benefits the performance of multi-modal LLM for keeping the text knowledges [p. 23]
- To ensure each image's knowledge is sufficiently studied, for all the interleaving data, other than the standard filtering, deduping and other quality control pipeline, they also integrated a **data reordering procedure** for keeping all the image and text in the correct order [p. 23]

### OCR data [p. 23]

Optical Character Recognition (OCR) is a widely adopted technique that converts text from images into an editable format [p. 23]. In k1.5, a robust OCR capability is deemed essential for better aligning the model with human values [p. 23]. The OCR data sources are diverse, ranging from open-source to in-house datasets, and encompassing both clean and augmented images [p. 23].

**In-house OCR datasets** [p. 23]:
In addition to the publicly available data, the authors have developed a substantial volume of in-house OCR datasets, covering:
- Multilingual text [p. 23]
- Dense text layouts [p. 23]
- Web-based content [p. 23]
- Handwritten samples [p. 23]

**OCR 2.0 capabilities** [p. 23]:
Following the principles outlined in OCR 2.0 (H. Wei et al. 2024), the model is also equipped to handle a variety of optical image types, including:
- Figures [p. 23]
- Tables [p. 23]
- Geometry diagrams [p. 23]
- Mermaid plots [p. 23]
- Natural scene text [p. 23]

**Data augmentation** [p. 23]:
The authors apply extensive data augmentation techniques—such as rotation, distortion, color adjustments, and noise addition—to enhance the model's robustness [p. 23]. As a result, the model achieves a high level of proficiency in OCR tasks [p. 23].

### Knowledge data [p. 23]

The concept of multi-modal knowledge data is analogous to the previously mentioned text pretraining data, except here the focus is on assembling a comprehensive repository of human knowledge from diverse sources to further enhance the model's capabilities [p. 23]. For example, carefully curated geometry data in the dataset is vital for developing visual reasoning skills, ensuring the model can interpret the abstract diagrams created by humans [p. 23].

**Data sources and processing** [p. 23]:
- The knowledge corpus adheres to a standardized taxonomy to balance content across various categories, ensuring diversity in data sources [p. 23]
- Similar to text-only corpora, which gather knowledge from textbooks, research papers, and other academic materials, multi-modal knowledge data employs both a layout parser and an OCR model to process content from these sources [p. 23]
- The authors also include filtered data from internet-based and other external resources [p. 23]

**Handling infographics** [p. 23]:
Because a significant portion of the knowledge corpus is sourced from internet-based materials, infographics can cause the model to focus solely on OCR-based information [p. 23]. In such cases, relying exclusively on a basic OCR pipeline may limit training effectiveness [p. 23]. To address this, the authors have developed an **additional pipeline that better captures the purely textual information embedded within images** [p. 23].

### General QA Data [p. 23]

During the training process, the authors observed that **incorporating a substantial volume of high-quality QA datasets into pretraining offers significant benefits** [p. 23]. 

**Data sources** [p. 23]:
- Included rigorous academic datasets addressing tasks such as grounding, table/chart question answering, web agents, and general QA [p. 23]
- Compiled a large amount of in-house QA data to further enhance the model's capabilities [p. 23]

**Quality control** [p. 23]:
To maintain balanced difficulty and diversity, the authors applied scoring models and meticulous manual categorization to their general question answering dataset, resulting in overall performance improvements [p. 23].

## B.3 Model Architecture [p. 23]

Kimi k-series models employ a variant of the Transformer decoder (Vaswani et al. 2017) that integrates multimodal capabilities alongside improvements in architecture and optimization strategies, illustrated in Figure 11 [p. 23]. These advancements collectively support stable large-scale training and efficient inference, tailored specifically to large-scale reinforcement learning and the operational requirements of Kimi users [p. 23].

**Figure 11** (p. 24): "Kimi k1.5 supports interleaved images and text as input, leveraging large-scale reinforcement learning to enhance the model's reasoning capabilities."

Description: Architecture diagram showing the model's processing of text sequences and interleaved image-text sequences through a Transformer, leading to large-scale reinforcement learning.
- Key elements: Two input paths (Text Sequences and Interleave Image-text Sequences) feeding into a Transformer block, which connects to Large Scale Reinforcement Learning
- Notable patterns: The diagram illustrates the multimodal input handling and the connection to the RL training process
- Supports claim: This figure illustrates the model's capability to handle both pure text and multimodal inputs for enhanced reasoning through RL [p. 23]

**Note on scaling experiments** [p. 23]:
Extensive scaling experiments indicate that most of the base model performance comes from improvements in the quality and diversity of the pretraining data [p. 23]. Specific details regarding model architecture scaling experiments lie beyond the scope of this report and will be addressed in future publications [p. 23].

## B.4 Training Stages [p. 23–24]

The Kimi k1.5 model is trained in three stages: the vision-language pretraining stage, the vision-language cooldown stage, and the long-context activation stage [p. 23–24]. Each stage of the Kimi k1.5 model's training focuses on a particular capability enhancement [p. 24].

### Vision-language pretraining stage [p. 24]

In this stage, the model is firstly trained solely on language data, establishing a robust language model foundation [p. 24]. Then the model is gradually introduced to interleaved vision-language data, acquiring multimodal capabilities [p. 24]. 

**Training procedure** [p. 24]:
1. The visual tower is initially trained in isolation without updating the language model parameters [p. 24]
2. Then the authors unfreeze the language model layers [p. 24]
3. Ultimately increase the proportion of vision-text data to 30% [p. 24]

The final data mixtures and their respective weights were determined through ablation studies conducted on smaller models [p. 24].

### Vision-language cooldown stage [p. 24]

The second stage serves as a cooldown phase, where the model is continue trained with high-quality language and vision-language datasets to ensure superior performance [p. 24]. Through empirical investigation, the authors observed that **the incorporation of synthetic data during the cooldown phase yields significant performance improvements**, particularly in mathematical reasoning, knowledge-based tasks, and code generation [p. 24].

**Data composition** [p. 24]:
- The English and Chinese components of the cooldown dataset are curated from high-fidelity subsets of the pre-training corpus [p. 24]
- For math, knowledge, and code domains, the authors employ a hybrid approach: utilizing selected pre-training subsets while augmenting them with synthetically generated content [p. 24]

**Synthetic data generation** [p. 24]:
- The authors leverage existing mathematical, knowledge and code corpora as source material to generate question-answer pairs through a proprietary language model [p. 24]
- They implement rejection sampling techniques to maintain quality standards (Yue, Qu, et al. 2023; D. Su et al. 2024) [p. 24]
- These synthesized QA pairs undergo comprehensive validation before being integrated into the cooldown dataset [p. 24]

### Long-context activation stage [p. 24]

Finally, in the third stage, k1.5 is trained with upsampled long-context cooldown data, enabling it to process extended sequences and support tasks that demand longer context [p. 24]. 

**Data composition** [p. 24]:
To ensure excellent long-text capabilities of the base model, the authors upsampled long-context data and used:
- **40% full attention data**: came partly from high-quality natural data and partly from synthetic long context Q&A and summary data [p. 24]
- **60% partial attention data**: came from uniform sampling of cooldown data [p. 24]

**Training parameters** [p. 24]:
- The RoPE frequency (J. Su et al. 2024) was set to 1,000,000 [p. 24]
- During this stage, the authors gradually extended length activation training by increasing the maximum sequence length from 4,096 to 32,768, and ultimately to 131,072 [p. 24]
