# D Self-Instruct Data [p. 22–23]

[p. 22] As described in Section 4.3, LLAMA 2 CHAT is used to bootstrap self-instruct data for instruct finetuning. The main challenge is the need for an automated process of generating long context instruct data with only short context models at hand. The core idea is to split long documents into chunks of text that can fit into the short model's context and apply self-instruct. The focus is primarily on question answering datasets.

The procedure:
1. Split the long document into smaller chunks.
2. For each chunk, construct a prompt as in Figure 10, which gets fed into LLAMA 2 CHAT to get a question-answer pair.
3. To diversify the question types, randomly choose between two prompts that ask for either normal or short answers.
4. Extract the question and answer from the response (using tags as required by the prompt).
5. Construct long question answering instruct data by combining the question-answer pair with the original long document, using the templates in Figure 11 for the corresponding answer type.

## Figures

**Figure 10** (p. 23): "Prompts used for generating question and answer pairs by bootstrapping LLAMA 2 CHAT. We split the long documents into chunks and feed each chunk into one of the prompts with equal probability. We prompt the models to wrap the answer with XML tags, which enables more accurate answer extraction."

Two prompts are shown:

**Normal Answer Prompt:**
```
[INST] You are given a text chunk (delimited by triple quotes) taken from a long
text. Write a question about this text and provide the correct answer. The answer
needs to be based on the text. This question will later be used as a reading
comprehension test over the entire document. Wrap the question and answer using
XML tags (<question> and </question>, <answer> and </answer>).
"""
{TEXT_CHUNK}
"""
[/INST]
```

**Short Answer Prompt:**
```
[INST] You are given a text chunk (delimited by triple quotes) from a long
document. Based on information from the text, come up with a specific question
**which can be answered in a few words or a single phrase** and provide the
correct answer without explanation. The answer needs to be based on the text.
This question will later be used as a reading comprehension test over the
entire document. Wrap the question and answer using XML tags (<question>
and </question>, <answer> and </answer>). Again, the answer needs to be short.
"""
{TEXT_CHUNK}
"""
[/INST]
```

**Figure 11** (p. 23): "Data templates for constructing long question-answer data. The question and answer pair is extracted from the response of LLAMA 2 CHAT."

Two templates are shown:

**Normal Answer Data Template:**
```
[INST] You are given a long text (delimited by triple quotes) and a question.
Read the text and answer the question in the end.
"""
{FULL_DOCUMENT}
"""
Question: {QUESTION}
[/INST]
{ANSWER}
```

**Short Answer Data Template:**
```
[INST] You are given a long text (delimited by triple quotes) and a question.
Read the text and answer the question in the end as concisely as you can,
using a single phrase or sentence if possible. Do not provide any explanation.
"""
{FULL_DOCUMENT}
"""
Question: {QUESTION}
[/INST]
{ANSWER}
```
