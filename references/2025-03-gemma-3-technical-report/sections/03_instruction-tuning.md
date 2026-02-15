# Instruction-Tuning [p. 4]

Pre-trained models are tuned into instruction-tuned models with an improved post-training approach compared to prior recipe (see Table 6).

## Techniques [p. 4]

The authors' post-training approach relies on an improved version of knowledge distillation (Agarwal et al., 2024; Anil et al., 2018; Hinton et al., 2015) from a large IT teacher, along with a RL finetuning phase that combines several versions of BOND (Sessa et al., 2024), WARM (Ramé et al., 2024b), and WARP (Ramé et al., 2024a).

## Reinforcement learning objectives [p. 4]

The authors use a variety of reward functions to improve helpfulness, math, coding, reasoning, instruction-following, and multilingual abilities, while minimizing model harmfulness. This includes learning from weight averaged reward models (Ramé et al., 2024b) trained with human feedback data, code execution feedback (Gehring et al., 2024), and ground-truth rewards for solving math problems (Deepseek-AI, 2025; Lambert et al., 2024).

## Data filtering [p. 4]

The authors carefully optimize the data used in post-training to maximize model performance. They filter examples that show certain personal information, unsafe or toxic model outputs, mistaken self-identification data, and duplicated examples. Including subsets of data that encourage better in-context attribution, hedging, and refusals to minimize hallucinations also improves performance on factuality metrics, without degrading model performance on other metrics.

## [BOS] token [p. 4]

For both PT and IT models, text starts with a [BOS] token, that needs to be added explicitly since the text "[BOS]" does not map to the [BOS] token. For instance, Flax has an option, add_bos=True, to add this token automatically when tokenizing. An example of the formatting for an IT model is shown in Table 4.

**Table 4** | Formatting for Gemma IT models. Explicitly add the [BOS] token when tokenizing, or use the add_bos=True option in the tokenizer. *Do not tokenize the text "[BOS]"*.

| Context      | Formatting                      |
|--------------|---------------------------------|
| User turn    | `<start_of_turn>user`           |
| Model turn   | `<start_of_turn>model`          |
| End of turn  | `<end_of_turn>`                 |

**Example of discussion:**

```
User: Who are you?
Model: My name is Gemma!
User: What is 2+2?
Model: 2+2=4.
```

**Model input:**

```
[BOS]<start_of_turn>user
Who are you?<end_of_turn>
<start_of_turn>model
My name is Gemma!<end_of_turn>
<start_of_turn>user
What is 2+2?<end_of_turn>
<start_of_turn>model
```

**Model output:**

```
2+2=4.<end_of_turn>
```

## PT versus IT Formatting [p. 4]

All models share the same tokenizer, with some control tokens dedicated to IT formatting. A key difference is that PT models output a `<eos>` token at the end of generation, while IT models output a `<end_of_turn>` at the end of the generation, as shown for IT in Table 4. Fine-tuning either model type thus also requires adding their respective end tokens.
