# 7 Capability Extension [p. 14–16]

Post-training methods are discussed to extend the Yi base model to 200K long-context, equip it with visual understanding capability, and enhance the 6B model by depth upscaling. [p. 14]

## 7.1 Long Context Modeling [p. 14–15]

The long-context solution consists of a continual pretraining and a finetuning phase, both lightweight. The basic hypothesis is that the potential of utilizing information anywhere within the 200K input context is already in the base model (same as Fu et al. [22]), and the continue pretraining phase "unlocks" such capability, evidenced by a strong performance on Needle-in-a-Haystack test. The finetuning phase then further adapts the style of response to follow human instruction and preference. [p. 14]

### Continue Pretraining

[p. 14] The full-attention model is continued pretrained using sequence parallelism [43] and distributed attention. No sparse or linear attention is used; a brute force implementation of full attention is applied. The Yi 6B/34B base model is continue pretrained on the data mixture of: [p. 14]

1. Original pretraining data, as introduced in section 2.
2. Length-upsampled long-context data, where the long documents are mostly from books.
3. Multi-document question-answering synthetic data, where QA pairs are constructed so that the answer contains a recitation of the related paragraph before the answer.

The data approach mostly follows the data engineering practice in Fu et al. [22] and Yu et al. [87]. The model is continue pretrained on 5B tokens with 4M batch size, which translates to 100 optimization steps. Aligning with the concurrent work from Fu et al. [22], the authors observe that such light-weight continue pretraining is already able to enable a strong performance on Needle-in-a-Haystack test, as shown in Figure 6. [p. 14]

### Supervised Finetuning

[p. 14–15] Short-context SFT data is mixed with long-context document question-answering data. Model-assisted automated methods (i.e., synthetic data) are used to construct document QA. Specifically, multiple documents are randomly concatenated into a sequence, one or more paragraphs are sampled from the long sequence, and a chat model is asked to construct question and answer pairs based on the sampled paragraph. One important detail is recitation and rephrasing: before giving the answer, the model is asked to recite or paraphrase the original paragraph. This data format encourages the model's retrieval behavior and consequently discourages hallucination behavior: given a question, the model is more likely to use the information within the input to construct the answer, rather than use its internal knowledge, which may be related but inaccurate. The finetuned model is deployed at www.wanzhi01.com. [p. 15]

### Performance

[p. 15] The performance of the 200K models is shown in Figure 6 and Table 6. Figure 6 shows the famous Needle-in-a-Haystack test of Yi-34B-200K, though the authors tend to view that this level of retrieval is relatively easy for long-context LLMs. Table 6 shows that context scaling does not significantly influence the short-context generic capability. [p. 15]

**Figure 6** (p. 15): "Needle-in-a-Haystack performance of Yi-34B-200K. X-axis means length of the document, and Y-axis means the depth of the needle sentence within the document. We continue pretrain the model on 5B tokens long-context data mixture and demonstrates a near-all-green performance."

Heatmap with x-axis showing document length (1K to 200K) and y-axis showing depth percentage (0% at top to 100% at bottom). The plot is almost entirely green (successful retrieval), with only two small red/pink patches visible around 50% depth at ~150K length and ~50% depth at ~200K length. The overall performance is near-perfect across the full 200K context window. [p. 15]

**Table 6** (p. 15): "Performance on MMLU after 200K adaptation. Extending the context length to 200K does not significantly change the short context capability."

| Model | Average | Humanity | STEM | Social Science | Other |
|-------|---------|----------|------|----------------|-------|
| Yi-6B 4K | 63.24 | 59.10 | 53.15 | 73.83 | 69.26 |
| Yi-6B 200K | 61.73 | 56.17 | 52.36 | 72.54 | 68.94 |
| Yi-34B 4K | 76.32 | 73.17 | 68.03 | 85.11 | 80.78 |
| Yi-34B 200K | 75.56 | 72.20 | 66.83 | 84.76 | 80.40 |

## 7.2 Vision-Language [p. 15–16]

[p. 15] In the field of multimodal research, the integration of image understanding capabilities into large language models has become increasingly viable. Drawing inspiration from the open-sourced LLaVA [46, 47], the Yi Vision Language (Yi-VL) models are presented, i.e., Yi-VL-6B and Yi-VL-34B, based on Yi-6B-Chat and Yi-34B-Chat language models. [p. 15]

The architecture of Yi-VL models, as illustrated in Figure 7, comprises three primary modules: [p. 15]

1. **Vision Transformer (ViT):** used for image encoding, initialized with CLIP ViT-H/14 model [33].
2. **Projection Module:** designed to align image features with text feature space, consists of a two-layer Multilayer Perceptron (MLP) with layer normalizations.
3. **Large Language Model:** initialized with the Yi-Chat models, demonstrating exceptional proficiency in understanding and generating both English and Chinese.

To enhance the performance of Yi-VL models in bilingual multimodal understanding and generation, a rich dataset of bilingual image-text pairs is leveraged. [p. 15]

**Figure 7** (p. 16): "Architecture of Yi-VL models. Symbols are used to denote the training status of various modules at three training stages: a fire icon indicates the parameters of the module are trainable, while a snowflake icon signifies that parameters are frozen. The image resolution used in ViT at each stage, either 224^2 or 448^2, is also marked."

The diagram shows the processing pipeline: an Image is fed into a Vision Transformer (with resolution increasing from 224 to 448), which produces Image Features. These pass through a Projection Module. Text input produces Text Features. Both feature types are concatenated and fed into the Large Language Model, which generates the Response. Training status icons show which modules are trainable vs. frozen at each stage. [p. 16]

### Training Stages

[p. 16] Yi-VL models undergo a three-stage training process:

**Stage 1:** The parameters of the ViT and the projection module are trained using an image resolution of 224^2. The training leverages a substantial dataset comprising 100 million image-text pairs from LAION-400M [66]. The primary objective is to enhance the ViT's knowledge acquisition within the specified architecture and to achieve better alignment between the ViT and the LLM. [p. 16]

**Stage 2:** The image resolution of ViT is scaled up to 448^2, aiming to further boost the model's capability for discerning intricate visual details. The dataset used in this stage includes 20 million image-text pairs derived from LAION-400M. Additionally, around 4.8 million image-text pairs are incorporated from diverse sources, e.g., CLLaVA [45], LLaVAR [91], Flickr [85], VQAv2 [25], RefCOCO [37], Visual7w [95] and so on. [p. 16]

**Stage 3:** The parameters of the entire model are trained. The primary goal is to enhance the model's proficiency in multimodal chat interactions, thereby endowing it with the ability to seamlessly integrate and interpret visual and linguistic inputs. The training dataset encompasses a diverse range of sources, totalling approximately 1 million image-text pairs, including GQA [32], VizWiz VQA [26], TextCaps [71], OCR-VQA [51], Visual Genome [39], ShareGPT4V [6] and so on. To ensure data balancing, a cap on the maximum data contribution from any single source is imposed, restricting it to no more than 50,000 pairs. [p. 16]

### Training Hyperparameters

[p. 16] In Stage 1 and 2, the global batch size, the learning rate, the gradient clip and the number of epoch are set to 4096, 1e-4, 0.5 and 1, respectively. In Stage 3, these parameters are adjusted to 256, 2e-5, 1.0 and 2. The training consumes 128 NVIDIA A100 GPUs. The total training time amounted to approximately 3 days for Yi-VL-6B and 10 days for Yi-VL-34B. [p. 16]

Table 7 shows the MMMU test set leaderboard by Yi-VL's release. The authors note that this area is currently actively under research, and they will continuously improve and update Yi-VL's performance. [p. 16]

### MMMU Performance

**Table 7** (p. 17): "MMMU test set performance by the time of Yi-VL's release."

| Model | Overall | Art | Business | Science | Health | Society | Engineering |
|-------|---------|-----|----------|---------|--------|---------|-------------|
| GPT-4V | 55.7 | 65.3 | 64.3 | 48.4 | 63.5 | 76.3 | 41.7 |
| Yi-VL-34B | 41.6 | 56.1 | 33.3 | 32.9 | 45.9 | 66.5 | 36.0 |
| Qwen-VL-PLUS | 40.8 | 59.9 | 34.5 | 32.8 | 43.7 | 65.5 | 32.9 |
| Marco-VL | 40.4 | 56.5 | 31.0 | 31.0 | 46.9 | 66.5 | 33.8 |
| Yi-VL-6B | 37.8 | 53.4 | 30.3 | 30.0 | 39.3 | 58.5 | 34.1 |
| InfMIM-Zephyr-7B | 35.5 | 50.0 | 29.6 | 28.2 | 37.5 | 54.6 | 31.1 |
| SVIT | 34.1 | 48.9 | 28.0 | 26.8 | 35.5 | 50.9 | 30.7 |
| Emu2-Chat | 34.1 | 50.6 | 27.7 | 28.0 | 32.4 | 50.3 | 31.3 |
| BLIP-2 FLAN-T5-XXL | 34.0 | 49.2 | 28.6 | 27.3 | 33.7 | 51.5 | 30.4 |
| InstructBLIP-T5-XXL | 33.8 | 48.5 | 30.6 | 27.6 | 33.6 | 49.8 | 29.4 |
| LLaVA-1.5-13B | 33.6 | 49.8 | 28.2 | 25.9 | 34.9 | 54.7 | 28.3 |
| Qwen-VL-7B-Chat | 32.9 | 47.7 | 29.8 | 25.6 | 33.6 | 45.3 | 30.2 |
| SPHINX* | 32.9 | 50.9 | 27.2 | 25.3 | 34.1 | 51.2 | 27.8 |
| mPLUG-OWL2 | 32.1 | 48.5 | 25.6 | 24.9 | 32.8 | 46.7 | 29.6 |
| BLIP-2 FLAN-T5-XL | 31.0 | 43.0 | 25.6 | 25.1 | 31.8 | 48.0 | 27.8 |
| InstructBLIP-T5-XL | 30.6 | 43.3 | 25.2 | 25.2 | 29.3 | 45.8 | 28.6 |
| CogVLM | 30.1 | 38.0 | 25.6 | 25.1 | 31.2 | 41.5 | 28.9 |

## 7.3 Depth Upscaling [p. 16–18]

[p. 16] Recent studies on scaling laws [29, 30, 36] have underscored the predictable improvement in model performance with increases in computational budget, model size, and data size. Yet, identifying the most effective distribution of resources between model and data sizes upon expanding the computational budget remains a formidable challenge in the field of scaling laws. Additionally, research conducted by DeepSeek-AI et al. [17] has highlighted that the allocation of an increased computational budget towards model scaling should be proportional to the quality of the data available. [p. 16]

In light of these insights, a novel approach is proposed aimed at dynamically adjusting the resource allocation between data and model sizes through a series of staged training processes. This strategy iteratively fine-tunes the balance between data characteristics and model size according to scaling laws, enhancing both model training efficiency and performance. [p. 16]

### Method

[p. 17] Following the methodology outlined by Kim et al. [38], the goal is to upscale the Yi-6B base model, which has 32 layers, to a 9B model named the Yi-9B base model, featuring 48 layers, by duplicating the original 16 middle layers 12-28. Depth up-scaling involves expanding the base model's depth and subsequently continuing the pretraining phase for the enhanced model. [p. 17]

The investigations reveal that the decision on which layers to replicate could be informed by evaluating the cosine similarity scores between the inputs and outputs of each layer. Such an approach allows for targeted model scaling without necessitating additional pretraining, leading only to minimal performance impacts. This minimal impact on performance is attributed to the high cosine similarity, approaching one, between the inputs and outputs of the duplicated layers, as evidenced in Figure 8. This observation suggests that the replication of these layers does not significantly alter the output logits produced by the original model. This method ensures the efficient scaling of the model by optimizing its architecture based on the internal processing dynamics of its layers. [p. 17–18]

**Figure 8** (p. 17): "Input/output cosine similarity score of each token per layer for text 'Write a quiz about bits'. The cosine similarity scores of the 16 newly added layers(layers 28-44), as depicted in the lower figure, are observed to be nearly 1."

Two line plots stacked vertically, both with x-axis "layer_number" (0 to ~48) and y-axis "cosine" (0.5 to 1.0):
- **Top plot (Yi-6B):** Shows cosine similarity per layer for the original 32-layer Yi-6B model. Multiple colored lines represent different tokens. The first few layers show a sharp drop in cosine similarity (down to ~0.5–0.6), then values rise and stabilize around 0.8–0.95 for the middle and later layers. A noticeable drop occurs at the final layer.
- **Bottom plot (Yi-9B Initialization):** Shows cosine similarity per layer for the 48-layer Yi-9B model after initialization (before continual training). The pattern is similar to Yi-6B for the first ~28 layers. The 16 newly added layers (layers 28-44) show cosine similarity scores very close to 1.0, confirming that the duplicated layers produce nearly identical input and output. The final original layers (44-48) show the same drop pattern as the end of Yi-6B. [p. 17]

### Continual Training

[p. 18] The dataset is composed of approximately 800 billion tokens across two stages, with around 70% having been recently collected and carefully selected. The code coverage in the final stage has been enhanced to improve code performance. [p. 18]

To optimize the training process, a constant learning rate of 3e-5 is maintained, and a strategic approach is adopted to gradually increase the batch size from 4M tokens whenever the model's loss plateaued. This incremental adjustment of the batch size, alongside maintaining all other parameters in alignment with the established Yi-6B base model configuration, was instrumental in navigating the challenges of training at scale. [p. 18]

The effectiveness of these strategies is demonstrated in Table 8, which details the Yi-9B base model's performance across a variety of benchmarks, including common sense, reasoning, knowledge, coding, and mathematics. It underscores the competitive advantages of Yi-9B base model in specific domains, illustrating the efficacy of the methodology in enhancing model performance by optimally adjusting the interplay between data characteristics and model size. [p. 18]

**Table 8** (p. 18): "Performance between Yi-6B and Yi-9B: Arc Challenge (25-shot), HellaSwag (10-shot), MMLU (5-shot), Winogrande (5-shot), GSM8K (5-shot), MATH (4-shot), HumanEval pass@1, MBPP pass@1(3-shot). Yi-9B Init is just depthwise upscaling from Yi-6B by duplicating layers 12-28 without further training."

| Model | Arc-C | HellaSwag | MMLU | Winogrande | GSM8K | MATH | HumanEval | MBPP |
|-------|-------|-----------|------|------------|-------|------|-----------|------|
| Yi-6B | 50.3 | 74.4 | 63.2 | 71.3 | 32.5 | 4.6 | 15.9 | 26.3 |
| Yi-9B Init | 52.1 | 73.3 | 63.0 | 69.4 | 31.3 | 4.1 | 12.8 | 25.8 |
| Yi-9B | **55.6** | **76.4** | **68.4** | **73.0** | **52.3** | **15.9** | **39.0** | **54.4** |
