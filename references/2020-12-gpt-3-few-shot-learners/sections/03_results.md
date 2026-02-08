# 3. Results [p. 10-11]

[p. 10] In Figure 3.1 the authors display training curves for the 8 models described in Section 2. For this graph 6 additional extra-small models with as few as 100,000 parameters are also included. As observed in [KMH+20], language modeling performance follows a power-law when making efficient use of training compute. After extending this trend by two more orders of magnitude, only a slight (if any) departure from the power-law is observed. One might worry that these improvements in cross-entropy loss come only from modeling spurious details of the training corpus. However, the following sections show that improvements in cross-entropy loss lead to consistent performance gains across a broad spectrum of natural language tasks.

[p. 10] Below, the 8 models described in Section 2 (the 175 billion parameter GPT-3 and 7 smaller models) are evaluated on a wide range of datasets. The datasets are grouped into 9 categories representing roughly similar tasks:

- Section 3.1: Traditional language modeling tasks and tasks similar to language modeling, such as Cloze tasks and sentence/paragraph completion tasks.
- Section 3.2: "Closed book" question answering tasks: tasks which require using the information stored in the model's parameters to answer general knowledge questions.
- Section 3.3: The model's ability to translate between languages (especially one-shot and few-shot).
- Section 3.4: Winograd Schema-like tasks.
- Section 3.5: Datasets that involve commonsense reasoning or question answering.
- Section 3.6: Reading comprehension.
- Section 3.7: The SuperGLUE benchmark suite.
- Section 3.8: NLI (briefly).
- Section 3.9: Additional tasks designed especially to probe in-context learning abilities -- these tasks focus on on-the-fly reasoning, adaptation skills, or open-ended text synthesis.

All tasks are evaluated in the few-shot, one-shot, and zero-shot settings.

## Figures

**Figure 3.1** (p. 11): "Smooth scaling of performance with compute."
- Performance (measured in terms of cross-entropy validation loss) follows a power-law trend with the amount of compute used for training. The power-law behavior observed in [KMH+20] continues for an additional two orders of magnitude with only small deviations from the predicted curve. For this figure, embedding parameters are excluded from compute and parameter counts.
- X-axis: Compute (PetaFLOP/s-days), log scale from 10^-6 to 10^4. Y-axis: Validation Loss, from ~1.5 to 6. Color scale: Parameters, from 10^5 to 10^11.
- Multiple training curves shown (one per model size), each descending from upper-left to lower-right. Larger models (more parameters, shown in warmer colors) achieve lower validation loss for a given compute budget.
- Dashed line shows fitted power law: L = 2.57 * C^(-0.048).

---

## 3.1 Language Modeling, Cloze, and Completion Tasks [p. 11]

[p. 11] This section tests GPT-3's performance on the traditional task of language modeling, as well as related tasks that involve predicting a single word of interest, completing a sentence or paragraph, or choosing between possible completions of a piece of text.

### 3.1.1 Language Modeling [p. 11]

[p. 11] Zero-shot perplexity is calculated on the Penn Tree Bank (PTB) [MKM+94] dataset measured in [RWC+19]. The 4 Wikipedia-related tasks in that work are omitted because they are entirely contained in GPT-3's training data, and the one-billion word benchmark is also omitted due to a high fraction of the dataset being contained in the training set. PTB escapes these issues due to predating the modern internet. The largest model sets a new SOTA on PTB by a substantial margin of 15 points, achieving a perplexity of 20.50. Note that since PTB is a traditional language modeling dataset it does not have a clear separation of examples to define one-shot or few-shot evaluation around, so only zero-shot is measured.

### Table 3.1: Zero-shot results on PTB language modeling dataset. Many other common language modeling datasets are omitted because they are derived from Wikipedia or other sources which are included in GPT-3's training data.

| Setting | PTB |
|---|---|
| SOTA (Zero-Shot) | 35.8^a |
| GPT-3 Zero-Shot | **20.5** |

^a [RWC+19]

### 3.1.2 LAMBADA [p. 11]

[p. 11] The LAMBADA dataset [PKL+16] tests the modeling of long-range dependencies in text -- the model is asked to predict the last word of sentences which require reading a paragraph of context. It has recently been suggested that the continued scaling of language models is yielding diminishing returns on this difficult benchmark. [BHT+20] reflect on the small 1.5% improvement achieved by a doubling of model size between two recent state of the art results ([SPP+19] and [Tur20]) and argue that "continuing to expand hardware and data sizes by orders of magnitude is not the path forward". The authors find that path is still promising and in a zero-shot setting GPT-3 achieves 76% on LAMBADA, a gain of 8% over the previous state of the art. [p. 12]

LAMBADA is also a demonstration of the flexibility of few-shot learning as it provides a way to address a problem that classically occurs with this dataset. Although the completion in LAMBADA is always the last word in a sentence, a standard language model has no way of knowing this detail. It thus assigns probability not only to the correct ending but also to other valid continuations of the paragraph. This problem has been partially addressed in the past with stop-word filters [RWC+19] (which ban "continuation" words). The few-shot setting instead allows the task to be "framed" as a cloze-test and allows the language model to infer from examples that a completion of exactly one word is desired. The fill-in-the-blank format used:

> Alice was friends with Bob. Alice went to visit her friend \_\_\_\_\_. -> Bob
>
> George bought some baseball equipment, a ball, a glove, and a \_\_\_\_\_. ->

[p. 12] When presented with examples formatted this way, GPT-3 achieves 86.4% accuracy in the few-shot setting, an increase of over 18% from the previous state-of-the-art. Few-shot performance improves strongly with model size. While this setting decreases the performance of the smallest model by almost 20%, for GPT-3 it improves accuracy by 10%. The fill-in-the-blank method is not effective one-shot, where it always performs worse than the zero-shot setting. Perhaps this is because all models still require several examples to recognize the pattern.

### Table 3.2: Performance on cloze and completion tasks. GPT-3 significantly improves SOTA on LAMBADA while achieving respectable performance on two difficult completion prediction datasets. [p. 12]

| Setting | LAMBADA (acc) | LAMBADA (ppl) | StoryCloze (acc) | HellaSwag (acc) |
|---|---|---|---|---|
| SOTA | 68.0^a | 8.63^b | **91.8**^c | **85.6**^d |
| GPT-3 Zero-Shot | **76.2** | **3.00** | 83.2 | 78.9 |
| GPT-3 One-Shot | 72.5 | 3.35 | 84.7 | 78.1 |
| GPT-3 Few-Shot | **86.4** | **1.92** | 87.7 | 79.3 |

^a [Tur20] ^b [RWC+19] ^c [LDL19] ^d [LCH+20]

**Figure 3.2** (p. 12): "On LAMBADA, the few-shot capability of language models results in a strong boost to accuracy. GPT-3 2.7B outperforms the SOTA 17B parameter Turing-NLG [Tur20] in this setting, and GPT-3 175B advances the state of the art by 18%. Note zero-shot uses a different format from one-shot and few-shot as described in the text."
- X-axis: Parameters in LM (Billions), from 0.1B to 175B. Y-axis: Accuracy, from 20 to 90.
- Three lines: Zero-Shot (blue), One-Shot (green), Few-Shot K=15 (orange).
- Horizontal dashed lines: "Human" at ~95 and "Zero-Shot SOTA" at ~68.
- Zero-Shot rises from ~40 at 0.1B to ~76 at 175B. One-Shot rises from ~40 to ~72.5 at 175B. Few-Shot rises from ~20 at 0.1B to ~86 at 175B.
- Few-Shot shows the strongest scaling behavior, crossing SOTA around 2.7B parameters.

[p. 13] One note of caution: an analysis of test set contamination identified that a significant minority of the LAMBADA dataset appears to be present in GPT-3's training data -- however analysis performed in Section 4 suggests negligible impact on performance.

### 3.1.3 HellaSwag [p. 13]

[p. 13] The HellaSwag dataset [ZHB+19] involves picking the best ending to a story or set of instructions. The examples were adversarially mined to be difficult for language models while remaining easy for humans (who achieve 95.6% accuracy). GPT-3 achieves 78.1% accuracy in the one-shot setting and 79.3% accuracy in the few-shot setting, outperforming the 75.4% accuracy of a fine-tuned 1.5B parameter language model [ZHR+19] but still a fair amount lower than the overall SOTA of 85.6% achieved by the fine-tuned multi-task model ALUM.

### 3.1.4 StoryCloze [p. 13]

[p. 13] GPT-3 is evaluated on the StoryCloze 2016 dataset [MCH+16], which involves selecting the correct ending sentence for five-sentence long stories. GPT-3 achieves 83.2% in the zero-shot setting and 87.7% in the few-shot setting (with K = 70). This is still 4.1% lower than the fine-tuned SOTA using a BERT based model [LDL19] but improves over previous zero-shot results by roughly 10%.
