# 2.3 Pre-Training Stages [p. 4-5]

As illustrated in Figure 4 and Table 1, after loading the intermediate language model discussed above, Kimi-VL's pre-training comprises a total of 4 stages consuming 4.4T tokens after text-only pre-training of its language model. To preserve text abilities, all stages that update the language model are joint training stages. The details are as follows.

**Figure 4** (p. 4): "The pre-training stages of Kimi-VL consume a total of 4.4T tokens after text-only pre-training of its language model. To preserve text abilities, all stages that update the language model are joint training stages."

Description: Flow diagram
- Key elements: Four blue boxes showing training stages from left to right: (1) "Text Pre-training: 5.2T data, Pure text data" (2) "ViT Training: 2.0T -> 0.1T data, CoCa loss with text activation decoder -> align to LLM" (3) "Joint Pre-training: 1.4T data, All except Multimodal Data, Progressive Multimodal Data" (4) "Joint Cooldown: 0.6T data, High-quality Text & Multimodal Data, No warmup for longer LR" (5) "Joint Long-context: 0.3T data, Long Text & Long Video & Long Doc, NOPE decay: 50,000 -> 800,000". Green circular arrows labeled "requires LR scheduler" and "requires LR scheduler" between stages
- Notable patterns: Progressive increase in multimodal data, final stage extends context length dramatically
- Supports claim: Shows systematic multi-stage pre-training approach preserving text abilities through joint training

## ViT Training Stages [p. 4]

The MoonViT is trained on image-text pairs, where the text components consist of a variety of targets: image alt texts, synthetic captions, grounding bboxes, and OCR texts. The training incorporates two objectives: a SigLIP (Zhai et al. 2023) loss L_sigllp (a variant of contrastive loss) and a cross-entropy loss L_caption for caption generation conditioned on input images. Following CoCa's approach (J. Yu et al. 2022), the final loss function is formulated as:

L = L_sigllp + λL_caption, where λ = 2

Specifically, the image and text encoders compute the contrastive loss, while the text decoder performs next-token prediction (NTP) conditioned on features from the image encoder. To accelerate training, we initialized both encoders with SigLIP SO-400M (Zhai et al. 2023) weights and implemented a progressive resolution sampling strategy. This gradually allow larger and larger images as the text decoder is initialized from a tiny decoder-only language model. During training, we observed an emergence in the caption loss while scaling up OCR data, indicating that the text decoder had developed some OCR capabilities. To facilitate transferring the ViT to the stage with 2T tokens, we align the MoonViT to the MoE language model using another 0.1T tokens, where only MoonViT MLP-projector are updated and are significantly reduces the initial perplexity of MoonViT embeddings in the language model, allowing a smoother joint pre-training stage as follows.

## Joint Pre-training Stage [p. 4-5]

In the joint pre-training stage, we train the model with a combination of pure text data (sampled from the same distribution as the text-only pre-training stage) and a variety of multimodal data (as discussed in Sec. 3.1). We continue training from the loaded LLM checkpoint using the same learning rate scheduler, consuming an additional 1.4T tokens. The initial steps utilize solely language data, after which the proportion of multimodal data gradually increases. Through this progressive approach, we observe that joint pre-training preserves the model's language capabilities while successfully integrating visual comprehension abilities.

## Joint Cooldown Stage [p. 5]

The stage following the pre-training stage is a multimodal cooldown phase, where the model is continued trained with high-quality language and multimodal datasets to ensure superior performance. For the language part, through empirical investigation, we observe that the incorporation of synthetic data during the cooling phase yields substantial performance improvements, particularly in mathematical reasoning, knowledge-based tasks, and code generation. The general text components of the cooldown dataset are curated from high-fidelity subsets of the pre-training corpus. For math, knowledge, and code domains, we employ a hybrid approach: utilizing selected pre-training subsets while augmenting them with synthetically generated content. Specifically, we leverage existing mathematical knowledge and code corpora as source material to generate question-answer (QA) pairs through a proprietary language model, implementing rejection sampling techniques to maintain quality standards (Yue, Qu, et al. 2023; D. Su et al. 2024). These synthesized QA pairs undergo comprehensive validation before being integrated into the cooldown dataset. For the multimodal part, in addition to the two strategies as employed in text cooldown data preparation, i.e. question-answer synthesis and high-quality subset replay, to allow more comprehensive visual-centric perception and understanding (B. Li et al. 2024; Tong et al. 2024; J. Guo et al. 2024), we filter and rewrite a variety of academic visual or vision-language data sources to QA pairs. Unlike post-training stages, these language and multimodal QA pairs in the cooldown stage are only included for activating specific abilities and henceforth facilitating learning high-quality data, thus we keep their ratio at a low portion to avoid overfitting these QA patterns. The joint cooldown stage significantly improves both language and multimodal abilities of the model.

## Joint Long-context Activation Stage [p. 5]

In the final pre-training stage, we extend the context length of the model from 8192 (8K) to 131072 (128K), with the inverse frequency of its RoPE (J. Su et al. 2023) embeddings reset from 50,000

Table 1: Overview of training stages: data composition, token volumes, sequence lengths, and trainable components.

| Stages | ViT Training | Joint Pre-training | Joint Cooldown | Joint Long-context |
|--------|--------------|-------------------|----------------|-------------------|
| Data | All text<br>Synthesis Caption<br>Grounding<br>OCR | +<br>Text, Knowledge<br>Interleaving<br>Video, Agent | +<br>High-quality Text<br>High-quality Multimodal<br>Academic Sources | +<br>Long Text<br>Long Video<br>Long Document |
| Tokens | 2T + 0.1T | 1.4T | 0.6T | 0.3T |
| Sequence length | 8192 | 8192 | 8192 | 32768->131072 |
| Training | ViT | ViT & LLM | ViT & LLM | ViT & LLM |

Table 2: Needle-in-a-Haystack (NIAH) test on text/video haystacks, where needles are uniformly distributed at various positions within the haystack. We report recall accuracy across different haystack lengths up to 131,072 tokens (128K).

| Haystack Length | [0, 2048] | [2048, 4096] | [4096, 8192] | [8192, 16384] | [16384, 32768] | [32768, 65536] | [65536, 131072] |
|-----------------|-----------|--------------|--------------|---------------|----------------|----------------|-----------------|
| text haystack | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 87.0 |
| video haystack | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 91.7 |
