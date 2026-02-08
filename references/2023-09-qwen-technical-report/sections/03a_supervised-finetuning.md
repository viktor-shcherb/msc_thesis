# 3 Alignment [p. 9]

[p. 9] Pretrained large language models have been found to be not aligned with human behavior, making them unsuitable for serving as AI assistants in most cases. Recent research has shown that the use of alignment techniques, such as supervised finetuning (SFT) and reinforcement learning from human feedback (RLHF), can significantly improve the ability of language models to engage in natural conversation. This section details how QWEN models have been trained using SFT and RLHF, and evaluates their performance in the context of chat-based assistance.

# 3.1 Supervised Finetuning [p. 9–10]

[p. 9] The initial step is to carry out SFT, which finetunes a pretrained LLM on chat-style data, including both queries and responses.

## 3.1.1 Data [p. 10]

[p. 10] To enhance the capabilities of the supervised finetuning datasets, conversations are annotated in multiple styles. While conventional datasets (Wei et al., 2022a) contain a vast amount of data prompted with questions, instructions, and answers in natural language, the approach takes it a step further by annotating human-style conversations. This practice, inspired by Ouyang et al. (2022), aims at improving the model's helpfulness by focusing on natural language generation for diverse tasks.

To ensure the model's ability to generalize to a wide range of scenarios, data formatted in prompt templates that could potentially limit its capabilities is specifically excluded. Furthermore, safety of the language model is prioritized by annotating data related to safety concerns such as violence, bias, and pornography.

### Data format

[p. 10] The training method can significantly impact the final performance of the model. The ChatML-style format (OpenAI, 2022) is utilized, which is a versatile meta language capable of describing both the metadata (such as roles) and the content of a turn. This format enables the model to effectively distinguish between various types of information, including system setup, user inputs, and assistant outputs.

## 3.1.2 Training [p. 10]

[p. 10] Consistent with pretraining, next-token prediction is applied as the training task for SFT. Loss masks are applied for the system and user inputs. More details are demonstrated in Section A.1.1.

### SFT hyperparameters

- Optimizer: AdamW
- beta_1 = 0.9, beta_2 = 0.95, epsilon = 10^{-8}
- Sequence length: 2048
- Batch size: 128
- Total steps: 4000
- Learning rate warmup: over the first 1430 steps, reaching a peak of 2 x 10^{-6}
- Weight decay: 0.1
- Dropout: 0.1
- Gradient clipping: limit of 1.0
