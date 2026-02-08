# Instruction Tuning [p. 4-5]

Gemma 2B and 7B are finetuned with supervised fine-tuning (SFT) on a mix of text-only, English-only synthetic and human-generated prompt-response pairs and reinforcement learning from human feedback (RLHF) with the reward model trained on labelled English-only preference data and the policy based on a set of high-quality prompts. Both stages are found to be important for improved performance on downstream automatic evaluations and human preference evaluations of model outputs. [p. 4]

The final data mixtures and supervised fine-tuning recipe, which includes tuned hyperparameters, were chosen on the basis of improving helpfulness while minimizing model harms related to safety and hallucinations. [p. 4]

## Supervised Fine-Tuning

Data mixtures for supervised fine-tuning are selected based on LM-based side-by-side evaluations (Zheng et al., 2023). Given a set of held-out prompts, responses are generated from a test model, responses on the same prompts are generated from a baseline model, these are shuffled randomly, and a larger, high capability model is asked to express a preference between two responses. Different prompt sets are constructed to highlight specific capabilities, such as instruction following, factuality, creativity, and safety. The LM-based judges employ a number of known strategies, such as chain-of-thought prompting (Wei et al., 2022), rubrics and constitutions (Bai et al., 2022), to be aligned with human preferences. [p. 4]

## Filtering

When using synthetic data, several stages of filtering are run over it, removing examples that show certain personal information, unsafe or toxic model outputs, mistaken self-identification data, or duplicated examples. Following Gemini, including subsets of data that encourage better in-context attribution, hedging, and refusals to minimize hallucinations improves performance on factuality metrics, without degrading model performance on other metrics. [p. 4]

## Formatting

Instruction tuned models are trained with a specific formatter that annotates all instruction tuning examples with extra information, both at training and inference time. It has two purposes: 1) indicating roles in a conversation, such as the User role, and 2) delineating turns in a conversation, especially in a multi-turn conversation. Special control tokens are reserved in the tokenizer for this purpose. While it is possible to get coherent generations without the formatter, it will be out-of-distribution for the model, and will very likely produce worse generations. [p. 4]

**Table 3** (p. 4): Relevant formatting control tokens used for both SFT and RLHF of Gemma models.

| Context                      | Relevant Token       |
|------------------------------|----------------------|
| User turn                    | user                 |
| Model turn                   | model                |
| Start of conversation turn   | \<start_of_turn\>    |
| End of conversation turn     | \<end_of_turn\>      |

**Table 4** (p. 4): Example dialogue with user and model control tokens.

```
User:   <start_of_turn>user
        Knock knock.<end_of_turn>
        <start_of_turn>model
Model:  Who's there?<end_of_turn>
User:   <start_of_turn>user
        Gemma.<end_of_turn>
        <start_of_turn>model
Model:  Gemma who?<end_of_turn>
```

## Reinforcement Learning from Human Feedback

The supervised fine-tuned model is further finetuned using RLHF (Christiano et al., 2017; Ouyang et al., 2022). Pairs of preferences are collected from human raters and a reward function is trained under the Bradley-Terry model (Bradley and Terry, 1952), similarly to Gemini. The policy is trained to optimize this reward function using a novel reinforcement learning algorithm. Similar to the SFT phase, and in order to tune hyperparameters and additionally mitigate reward hacking (Amodei et al., 2016; Skalse et al., 2022), a high capacity model is relied on as an automatic rater and computed side-by-side comparisons against baseline models. [p. 5]
