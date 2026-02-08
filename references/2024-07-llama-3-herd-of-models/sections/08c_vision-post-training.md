# 7.5 Post-Training [p. 58–61]

[p. 58] The post-training recipe for the vision adapters is described. After pre-training, the model is fine-tuned on highly curated multi-modal conversational data to enable chat capabilities. Direct preference optimization (DPO) is further implemented to boost human evaluation performance and rejection sampling to improve multi-modal reasoning capabilities. Finally, a quality-tuning stage is added where the model is fine-tuned on a very small set of high-quality conversational data which further boosts human evaluation while retaining performance across benchmarks. [p. 58]

## 7.5.1 Supervised Finetuning Data [p. 58–59]

The supervised finetuning (SFT) data for image and video capabilities is described separately.

### Image [p. 58–59]

A mix of different datasets is utilized for supervised finetuning:

- **Academic datasets.** A highly filtered collection of existing academic datasets is converted to question-answer pairs using templates or via LLM rewriting. The LLM rewriting's purpose is to augment the data with different instructions and to improve the language quality of answers. [p. 58]

- **Human annotations.** Multi-modal conversation data is collected via human annotators for a wide range of tasks (open-ended question-answering, captioning, practical use cases, etc.) and domains (e.g., natural images and structured images). Annotators are provided with images and asked to write conversations. To ensure diversity, large-scale datasets are clustered and images are sampled uniformly across different clusters. Further, additional images for a few specific domains are acquired by expanding a seed via k-nearest [p. 58–59] neighbors. Annotators are also provided with intermediate checkpoints of existing models to facilitate model-in-the-loop style annotations, so that model generations can be utilized as a starting point by the annotators to then provide additional human edits. This is an iterative process, in which model checkpoints are regularly updated with better performing versions trained on the latest data. This increases the volume and efficiency of human annotations, while also improving their quality. [p. 59]

- **Synthetic data.** Different ways to generate synthetic multi-modal data by using text-representations of images and a text-input LLM are explored. The high-level idea is to utilize the reasoning capabilities of text-input LLMs to generate question-answer pairs in the text domain, and replace the text representation with its corresponding images to produce synthetic multi-modal data. Examples include rendering texts from question-answer datasets as images or rendering table data into synthetic images of tables and charts. Additionally, captions and OCR extractions from existing images are used to generate additional conversational or question-answer data related to the images. [p. 59]

### Video [p. 59]

[p. 59] Similar to the image adapter, academic datasets with pre-existing annotations are used and converted into appropriate textual instructions and target responses. The targets are converted to open-ended responses or multiple-choice options, whichever is more appropriate. Humans are asked to annotate videos with questions and corresponding answers. The annotators are asked to focus on questions that could not be answered based on a single frame, to steer the annotators towards questions that require temporal understanding. [p. 59]

## 7.5.2 Supervised Finetuning Recipe [p. 59]

The supervised finetuning (SFT) recipe for image and video capabilities is described separately.

### Image [p. 59]

[p. 59] Initialization is from the pre-trained image adapter, but the pre-trained language model's weights are hot-swapped with the instruction tuned language model's weights. The language model weights are kept frozen to maintain text-only performance, i.e., only the vision encoder and image adapter weights are updated. [p. 59]

The approach to finetune the model is similar to Wortsman et al. (2022). First, a hyperparameter sweep using multiple random subsets of data, learning rates and weight decay values is run. Next, the models are ranked based on their performance. Finally, the weights of the top-*K* models are averaged to obtain the final model. The value of *K* is determined by evaluating the averaged models and selecting the instance with highest performance. The averaged models are observed to consistently yield better results compared to the best individual model found via grid search. Further, this strategy reduces sensitivity to hyperparameters. [p. 59]

### Video [p. 59]

[p. 59] For video SFT, the video aggregator and cross-attention layers are initialized using the pre-trained weights. The rest of the parameters in the model, the image weights and the LLM, are initialized from corresponding models following their finetuning stages. Similar to video pre-training, only the video parameters are finetuned on the video SFT data. For this stage, the video length is increased to 64 frames, and an aggregation factor of 32 is used to get two effective frames. The resolution of the chunks is also increased to be consistent with the corresponding image hyperparameters. [p. 59]

## 7.5.3 Preference Data [p. 59–60]

[p. 59] Multimodal pair-wise preference datasets are built for reward modeling and direct preference optimization.

- **Human annotations.** The human-annotated preference data consists of comparisons between two different model outputs, labeled as "chosen" and "rejected", with 7-scale ratings. The models used to generate responses are sampled on-the-fly from a pool of the best recent models, each with different characteristics. The model pool is updated weekly. Besides preference labels, annotators are also requested to provide optional human edits to correct inaccuracies in "chosen" responses because vision tasks have a low tolerance for inaccuracies. Note that human editing is an optional step because there is a trade-off between volume and quality in practice. [p. 59]

- **Synthetic data.** Synthetic preference pairs can also be generated by using text-only LLMs to edit and deliberately introduce errors in the supervised finetuning dataset. The conversational data is taken as input, and an LLM is used to introduce subtle but meaningful errors (e.g., change objects, change attributes, add mistakes in calculations, etc.). These edited responses are used as negative "rejected" samples and paired with the "chosen" original supervised finetuning data. [p. 59]

- **Rejection sampling.** [p. 60] Furthermore, to create more *on-policy* negative samples, the iterative process of rejection sampling is leveraged to collect additional preference data. At a high-level, rejection sampling is used to iteratively sample high-quality generations from a model. Therefore, as a by-product, all generations that are not selected can be used as negative rejected samples and used as additional preference data pairs. [p. 60]

## 7.5.4 Reward Modeling [p. 60]

[p. 60] A vision reward model (RM) is trained on top of the vision SFT model and the language RM. The vision encoder and the cross-attention layers are initialized from the vision SFT model and unfrozen during training, while the self-attention layers are initialized from the language RM and kept frozen. Freezing the language RM part generally leads to better accuracy, especially on tasks that require the RM to judge based on its knowledge or the language quality. The same training objective as the language RM is adopted, but adding a weighted regularization term on the square of the reward logits averaged over the batch, which prevents the reward scores from drifting. [p. 60]

The human preference annotations in Section 7.5.3 are used to train the vision RM. The same practice as language preference data (Section 4.2.1) is followed to create two or three pairs with clear ranking (*edited* > *chosen* > *rejected*). In addition, the negative responses are also synthetically augmented by perturbing the words or phrases related to the information in the image (such as numbers or visual texts). This encourages the vision RM to ground its judgement based on the actual image content. [p. 60]

## 7.5.5 Direct Preference Optimization [p. 60]

[p. 60] Similar to the language model (Section 4.1.4), the vision adapters are further trained with Direct Preference Optimization (DPO; Rafailov et al. (2023)) using the preference data described in Section 7.5.3. To combat the distribution shift during post-training rounds, only recent batches of human preference annotations are kept while dropping batches that are sufficiently off-policy (e.g., if the base pre-trained model is changed). Instead of always freezing the reference model, updating it in an exponential moving average (EMA) fashion every k-steps is found to help the model learn more from the data, resulting in better performance in human evaluations. Overall, the vision DPO model is observed to consistently perform better than its SFT starting point in human evaluations for every finetuning iteration. [p. 60]

## 7.5.6 Rejection Sampling [p. 60]

[p. 60] Most available question-answer pairs only contain the final answer and lack the chain-of-thought explanation that is required to train a model that generalizes well for reasoning tasks. Rejection sampling is used to generate the missing explanations for such examples and boost the model's reasoning capabilities. [p. 60]

Given a question-answer pair, multiple answers are generated by sampling the finetuned model with different system prompts or temperature. Next, the generated answers are compared to the ground-truth via heuristics or an LLM judge. Finally, the model is retrained by adding the correct answers back into the finetuning data mix. It is found useful to keep multiple correct answers per question. [p. 60]

To ensure only high-quality examples are added back into training, two guardrails are implemented. First, some examples contain incorrect explanations, despite the final answer being correct. This pattern occurs more frequently for questions where only a small fraction of the generated answers is correct. Therefore, answers for questions where the probability of the answer being correct is below a certain threshold are dropped. Second, raters prefer some answers over others due to differences in language or style. The reward model is used to select top-*K* highest-quality answers and add them back into training. [p. 60]

## 7.5.7 Quality Tuning [p. 60–61]

[p. 60] A small but *highly* selective SFT dataset is curated where all samples have been rewritten and verified either by humans or by the best models to meet the highest standards. DPO models are trained with this data to improve response quality, calling the process Quality-Tuning (QT). QT is found to significantly improve human evaluations without affecting generalization verified by benchmarks when the QT dataset covers a wide range [p. 61] of tasks and proper early stopping is applied. Checkpoints at this stage are selected purely based on benchmarks to ensure capabilities are retained or improved. [p. 61]
