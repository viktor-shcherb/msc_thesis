# Appendix D: Prompt Templates [p. 20-21]

## Input Prompt Structure

The authors decompose the input prompt template into the model template in Table 6 and the task template in Table 7 (S-NIAH) [p. 20]. The model template is the model chat format while the task template combines instruction, context, and query [p. 20]. To prevent models from refusing to answer their questions, the authors append the input with an answer prefix to elicit model responses [p. 20]. For VT and CWE, the authors use one task sample as in-context demonstration [p. 20].

**Table 6: Model chat templates** [p. 20]

| Model | Template |
|-------|----------|
| GPT-4 | {task_template} Do not provide any explanation. Please directly give me the answer. {task_answer_prefix} |
| Yi/Base | {task_template} {task_answer_prefix} |
| Command-R | ⟨BOS_TOKEN⟩<br>⟨|START_OF_TURN_TOKEN|⟩<br>⟨|USER_TOKEN|⟩{task_template}<br>⟨|END_OF_TURN_TOKEN|⟩<br>⟨|START_OF_TURN_TOKEN|⟩<br>⟨|CHATBOT_TOKEN|⟩{task_answer_prefix} |
| LWM/LongChat | {system_prompt} USER: {task_template} ASSISTANT: {task_answer_prefix} |
| GLM | [gMASK]sop⟨user⟩<br>{task_template}⟨|assistant|⟩<br>{task_answer_prefix} |
| Phi3 | ⟨user⟩<br>{task_template}⟨|end|⟩<br>⟨|assistant|⟩<br>{task_answer_prefix} |
| Qwen/DBRX | ⟨|im_start|⟩system<br>{system_prompt}⟨|im_end|⟩<br>⟨|im_start|⟩user<br>{task_template}⟨|im_end|⟩<br>⟨|im_start|⟩assistant<br>{task_answer_prefix} |
| Llama3/Llama3.1 | ⟨|begin_of_text|⟩⟨|start_header_id|⟩user⟨|end_header_id|⟩<br>{task_template}⟨|eot_id|⟩<br>⟨|start_header_id|⟩assistant⟨|end_header_id|⟩<br>{task_answer_prefix} |
| Llama2/Others | [INST] {task_template} [/INST] {task_answer_prefix} |

Note: The authors append a task answer prefix in model response to prevent models from refusing to answer their questions [p. 20]. The addition of answer prefix does not break the models' chat template [p. 20].

## Task Templates

**Table 7: S-NIAH and MK-NIAH templates** [p. 21]

### S-NIAH Subtask-1

**Task Template:**
```
Some special magic numbers are hidden within the following text. Make sure to memorize it. I will quiz you about the numbers afterwards.
[The grass is green. The sky is blue. The sun is yellow. Here we go. There and back again.]
One of the special magic numbers for {word} is: {number}.
What is the special magic number for {word} mentioned in the provided text?
```

**Task Answer Prefix:**
```
The special magic number for {word} mentioned in the provided text is
```

### S-NIAH Subtask-2

**Task Template:**
```
Some special magic numbers are hidden within the following text. Make sure to memorize it. I will quiz you about the numbers afterwards.
[Paul Graham essay...]
One of the special magic numbers for {word} is: {number}.
What is the special magic number for {word} mentioned in the provided text?
```

**Task Answer Prefix:**
```
The special magic number for {word} mentioned in the provided text is
```

### S-NIAH Subtask-3

**Task Template:**
```
Some special magic words are hidden within the following text. Make sure to memorize it. I will quiz you about the words afterwards.
[Paul Graham essay...]
One of the special magic words for {word} is: {word}.
What is the special magic word for {word} mentioned in the provided text?
```

**Task Answer Prefix:**
```
The special magic word for {word} mentioned in the provided text is
```

### MK-NIAH Subtask-1

**Task Template:**
```
Some special magic numbers are hidden within the following text. Make sure to memorize it. I will quiz you about the numbers afterwards.
[Paul Graham essay...]
One of the special magic numbers for {word-1} is: {number-1}.
One of the special magic numbers for {word-2} is: {number-2}.
One of the special magic numbers for {word-3} is: {number-3}.
One of the special magic numbers for {word-4} is: {number-4}.
What is the special magic number for {word-4} mentioned in the provided text?
```

**Task Answer Prefix:**
```
The special magic number for {word-4} mentioned in the provided text is
```

### MK-NIAH Subtask-2

**Task Template:**
```
Some special magic numbers are hidden within the following text. Make sure to memorize it. I will quiz you about the numbers afterwards.
[One of the special magic numbers for {word-1} is: {number-1}.]
One of the special magic numbers for {word-2} is: {number-2}.
...
One of the special magic numbers for {word-x} is: {number-x}.
[One of the special magic numbers for {word-n-1} is: {number-n-1}.]
One of the special magic numbers for {word-n} is: {number-n}.
What is the special magic number for {word-x} mentioned in the provided text?
```

**Task Answer Prefix:**
```
The special magic number for {word-x} mentioned in the provided text is
```

### MK-NIAH Subtask-3

**Task Template:**
```
Some special magic uuids are hidden within the following text. Make sure to memorize it. I will quiz you about the uuids afterwards.
[One of the special magic uuids for {uuid-1} is: {uuid-1}.]
One of the special magic uuids for {uuid-2} is: {uuid-2}.
...
One of the special magic uuids for {uuid-x} is: {uuid-x}.
[One of the special magic uuids for {uuid-n-1} is: {uuid-n}.]
One of the special magic uuids for {uuid-n} is: {uuid-n}.
What is the special magic number for {uuid-x} mentioned in the provided text?
```

**Task Answer Prefix:**
```
The special magic number for {uuid-x} mentioned in the provided text is
```

Note: Text shown in gray/lighter formatting in the original table represents placeholder content or examples. Square brackets [] indicate content that fills the haystack context.

---
[p. 22 continued]

**Table 8: MV-NIAH, MQ-NIAH, VT, CWE, and FWE templates** [p. 22]

### MV-NIAH

**Task Template:**
```
Some special magic numbers are hidden within the following text. Make sure to memorize it. I will quiz you about the numbers afterwards.
[Paul Graham essay...]
One of the special magic numbers for {word} is: {number-1}.
One of the special magic numbers for {word} is: {number-2}.
One of the special magic numbers for {word} is: {number-3}.
One of the special magic numbers for {word} is: {number-4}.
What are all the special magic numbers for {word} mentioned in the provided text?
```

**Task Answer Prefix:**
```
The special magic numbers for {word} mentioned in the provided text are
```

### MQ-NIAH

**Task Template:**
```
Some special magic numbers are hidden within the following text. Make sure to memorize it. I will quiz you about the numbers afterwards.
[Paul Graham essay...]
One of the special magic numbers for {word-1} is: {number-1}.
One of the special magic numbers for {word-2} is: {number-2}.
One of the special magic numbers for {word-3} is: {number-3}.
One of the special magic numbers for {word-4} is: {number-4}.
What are all the special magic numbers for {word-1}, {word-2}, {word-3}, and {word-4} mentioned in the provided text?
```

**Task Answer Prefix:**
```
The special magic numbers for {word-1}, {word-2}, {word-3}, and {word-4} mentioned in the provided text are
```

### VT (Variable Tracking)

**Task Template:**
```
{one task example}
Memorize and track the chain(s) of variable assignment hidden in the following text.

The grass is green. The sky is blue. The sun is yellow. Here we go. There and back again.
VAR {X1} = {number}
VAR {X2} = {X1}
VAR {X3} = {X2}
VAR {X4} = {X3}
VAR {X5} = {X4}
Question: Find all variables that are assigned the value {number} in the text above.
```

**Task Answer Prefix:**
```
Answer: According to the chain(s) of variable assignment in the text above, 5 variables are assigned the value {number}, they are:
```

### CWE (Common Words Extraction)

**Task Template:**
```
{one task example}
Below is a numbered list of words. In these words, some appear more often than others. Memorize the ones that appear most often.
1. word-a 2. word-b 3. word-c 4. word-d 5. word-e 6. word-f 7. word-g 8. word-f
Question: What are the 10 most common words in the above list?
```

**Task Answer Prefix:**
```
Answer: The top 10 words that appear most often in the list are:
```

### FWE (Frequent Words Extraction)

**Task Template:**
```
{one task example}
Read the following coded text and track the frequency of each coded word. Find the three most frequently appeared coded words. ... word-a ... word-b ... ... word-c ... word-a ... word-d ... word-a ... word-b ... word-e ... word-f ... ... word-g ... word-h ... ... word-i ...
Question: Do not provide any explanation. Please ignore the dots '...'. What are the three most frequently appeared coded words in the above coded text?
```

**Task Answer Prefix:**
```
Answer: According to the coded text above, the three most frequently appeared words are:
```

---
[p. 23 continued]

**Table 9: QA templates** [p. 23]

### Single Hop QA

**Task Template:**
```
Answer the question based on the given documents. Only give me the answer and do not output any other words.

The following are given documents.

Document 1:
{document-1}
...
Document x:
{document-x}
...
Document n:
{document-n}

Answer the question based on the given documents. Only give me the answer and do not output any other words.

Question: {question}
```

**Task Answer Prefix:**
```
Answer:
```

### Multi Hop QA

**Task Template:**
```
Answer the question based on the given documents. Only give me the answer and do not output any other words.

The following are given documents.

Document 1:
{document-1}
...
Document x:
{document-x}
...
Document y:
{document-y}
...
Document n:
{document-n}

Answer the question based on the given documents. Only give me the answer and do not output any other words.

Question: {question}
```

**Task Answer Prefix:**
```
Answer:
```
