# 3 Finetuning [p. 6]

The finetuning method significantly emphasizes data quality over quantity. The approach does *not* follow existing data-intensive approaches like FLAN [9] and UltraChat [19], which scale the SFT data to millions of entries but each entry may not have been examined carefully because the scale is too large. Instead, the method aligns with the LIMA [94] and DEITA [48] approach, which focus on data selection rather than scaling. With the scale being less than 10K, the authors are able to examine and optimize *every single data point*. [p. 6]

## 3.1 Data Preprocessing [p. 6]

### Quality is All You Need

The finetuning dataset consists of less than 10K multi-turn instruction-response dialog pairs, with each and every one of the entries constructed and polished over multiple iterations and from user feedback. This approach is taken because in preliminary experiments, the results from a smaller, manually annotated dataset are superior compared to open-source data of several hundred thousand entries. These observations align with those reported in Gemini Team et al. [23], Touvron et al. [77], Zhou et al. [94]. [p. 6]

---
[p. 6–7 continued]

The following techniques are used to improve prompt distribution selection, response formatting, and chain-of-thought formatting: [p. 6–7]

1. **Prompt distribution selection:** Drawing inspiration from WizardLM [83], compound instructions are developed and progressively evolved to increase their complexity. This approach has significantly reduced the size of SFT data in the experiments.
2. **Response formatting:** A default style extended from LIMA [94] is generally used. Overall, the responses are structured in an introduction-body-conclusion format where the body is usually a list of bullet points.
3. **CoT data formatting:** A "Step-Back" pattern is used, inspired by Zheng et al. [92], by performing abstraction to formulate higher-level solutions before delving into reasoning about the original, more concrete questions.

Extra efforts are spent on reducing hallucination and repetition: [p. 7]
1. To reduce hallucinations, they examine and ensure that the knowledge in the responses is not contained within the model, and eliminate responses that might lead to memorization.
2. To reduce repetition, they rewrite the repetitive turns of the responses that usually exist but may be overlooked in the finetuning data.

### Diversity and Mixture

[p. 7]

To ensure the coverage of different capabilities, a wide spectrum of open-source prompt is included, encompassing areas such as question answering, creative writing, dialogue, reasoning, mathematics, coding, safety, bilingual capabilities, and others.

To obtain fine-grained control of different directions of capabilities, inspired by InsTag [49], an instruction tagging system is developed. By designing a diversity-focused sampling algorithm, the distribution of instructions across various tags is carefully balanced. This approach ensures a diverse finetuning dataset, aiming to achieve enhanced cross-task robustness.

To achieve the optimal data ratio for balancing different directions of the capability, an approximate grid search is used to determine the data mixture. Motivated by Dong et al. [20], this process involved experimenting with {1, 1/2, 1/4, 1/8, 1/16, 1/32, 1/64} proportions for each ability. The search process was guided by validation results and in-house human evaluation sets.

### ChatML Format

[p. 7]

Beyond the focus on data quality and diversity, observations revealed that the format of the data substantially influences the model's ultimate performance. The ChatML-style format [53] is implemented. This structured approach empowers the model to differentiate among various information types, such as system configurations, user inputs, and assistant responses.

## 3.2 Training Method [p. 7]

Next-word prediction loss is used for finetuning, and loss is only computed on the responses, but not system and user instructions. Training details:

- **Optimizer:** AdamW with beta_1 = 0.9, beta_2 = 0.999, epsilon = 10^-8
- **Sequence length:** 4096
- **Batch size:** 64
- **Training steps:** 300
- **Learning rate:** constant 1 x 10^-5
- **Weight decay:** 0.1
- **Gradient clipping:** maximum threshold of 1.0
- **NEFTune [34]:** noise scale of 45 for Yi-34B-Chat and 5 for Yi-6B-Chat
