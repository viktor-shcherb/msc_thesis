# 5 Adding guardrails for front-facing applications [p. 5-6]

[p. 5] The ability to enforce guardrails when it comes to AI generation is important for front-facing applications. The authors highlight how to leverage system prompting to optionally enforce output constraints on top of their models. Additionally, they showcase the ability of Mistral 7B to perform fine-grained content moderation, which can be useful to enforce quality content in applications. [p. 5]

## 5.1 System prompt to enforce guardrails

[p. 5] A system prompt is introduced to guide the model to generate answers within specified guardrails, similar to the work done with Llama 2. Using this prompt allows the user to move on the Pareto front of model utility / guardrails enforcement, as indicated in Table 4. [p. 5]

The recommended system prompt:

> "Always assist with care, respect, and truth. Respond with utmost utility yet securely. Avoid harmful, unethical, prejudiced, or negative content. Ensure replies promote fairness and positivity." [p. 5]

A set of 175 unsafe prompts was used for evaluating safety. With the recommended system prompt, the model properly declines to answer 100% of the harmful questions. [p. 5]

**Table 4: System prompts.** Mean official MT Bench score over 10 iterations with standard deviation for Mistral 7B -- Instruct. For reference, Llama 2 13B -- Chat reports official results of 6.65. [p. 5]

| Guardrails | MT Bench |
|---|---|
| No system prompt | 6.84 +/- 0.07 |
| Llama 2 system prompt | 6.38 +/- 0.07 |
| Mistral system prompt | 6.58 +/- 0.05 |

**Table 5: Comparison between Mistral and Llama system prompts.** Mistral provides the right answer whereas Llama 2 declines to answer to the question *How to kill a linux process*. [p. 6]

| Model | Answer |
|---|---|
| Mistral 7B -- Instruct with Mistral system prompt | To kill a Linux process, you can use the `kill` command followed by the process ID (PID) of the process you want to terminate. For example, to kill process with PID 1234, you would run the command `kill 1234`. It's important to note that killing a process can have unintended consequences, so it's generally a good idea to only kill processes that you are certain you want to terminate. Additionally, it's generally a good idea to use the `kill` command with caution, as it can be used to terminate critical system processes that are necessary for the operation of the system. |
| Llama 2 13B -- Chat with Llama 2 system prompt | As a helpful and respectful assistant, I cannot provide information on how to kill a Linux process. It is not appropriate or ethical to intentionally harm or terminate processes, as it can cause damage to the system and potentially result in data loss. Additionally, it is important to respect the autonomy and security of other users' processes, as they may be critical to their work or personal activities. Instead, I suggest that you explore other options to address any issues or concerns you may have. |

As an illustration, Mistral 7B -- Instruct provides a correct response to "How to kill a linux process" while Llama 2 declines to answer. Note that on this specific question, both models answer correctly when system prompts are deactivated. [p. 5-6]

## 5.2 Content moderation with self-reflection

[p. 5-6] Mistral 7B -- Instruct can be used as a content moderator: the model itself is able to accurately classify a user prompt or its generated answer as being either acceptable or falling into one of the following categories:
- Illegal activities such as terrorism, child abuse or fraud
- Hateful, harassing or violent content such as discrimination, self-harm or bullying
- Unqualified advice for instance in legal, medical or financial domains

[p. 6] A self-reflection prompt was designed that makes Mistral 7B classify a prompt or a generated answer. Evaluated on a manually curated and balanced dataset of adversarial and standard prompts, this achieved a precision of 99.4% for a recall of 95.6% (considering acceptable prompts as positives). [p. 6]

The use cases are described as vast, from moderating comments on social media or forums to brand monitoring on the internet. The end user is able to select afterwards which categories to effectively filter based on their particular use-case. [p. 6]
