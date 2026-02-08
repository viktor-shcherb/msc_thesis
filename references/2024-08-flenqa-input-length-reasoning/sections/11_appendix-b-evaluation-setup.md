# B Full Evaluation Setup [p. 12-13]

## B.1 Prompts [p. 12-13]

[p. 12-13] The following prompt templates are used for each task, in both Normal (direct) and Chain-of-Thought (CoT) variants.

**Ruletaker prompt - Normal:**
```
Answer whether the statement {statement} can
be derived from the rule and the facts. Answer
with either "True" or "False".
Rule: {rule}
Facts: {facts + padding}
Answer with either "True" or "False".
```

**Ruletaker prompt - CoT:**
```
Answer whether the statement {statement} can
be derived from the rule and the facts.
Show your steps then answer with either "True"
or "False".
Rule: {rule}
Facts: {facts + padding}
Answer with either "True" or "False". Let's
work this out in a step by step way to be sure
we have the right answer.
```

**MonoRel prompt - Normal:**
```
Here are some facts. Answer the exact
following question based on the text:
{question} Answer the question as it appears
exactly. {facts + padding}
{question}
Answer only True or False.
```

**MonoRel prompt - CoT:**
```
Here are some facts. Answer the exact
following question based on the text:
{question} Answer the question as it appears
exactly.
Show your steps then answer with 'true' or
'false'.
{facts + padding}
{question}
Let's work this out in a step by step way to be
sure we have the right answer. Show your work
and finally answer with 'true' or 'false'. The
final step should include the exact text of
the question and the answer.
```

**PIR prompt - Normal:**
```
{facts + padding}
True/False Question: {question}
Answer only True or False.
```

**PIR prompt - CoT:**
```
Show your steps then answer with 'true' or
'false'.
{facts + padding}
True/False Question: {question}
Let's work this out in a step by step way to
be sure we have the right answer.
```

## B.2 Parameters [p. 13]

[p. 13] All models were evaluated with a temperature of 0 and "top p" of 0 where available to make results as reproducible as possible. Additionally, they configured Gemini Pro to ignore safety guardrails ("HARM_CATEGORY" configurations) to overcome its blank answers in some samples.

## B.3 Locating the answer in models' replies [p. 13]

[p. 13] To identify the models' answers in their responses, they searched for the occurrences of "false" or "true," disregarding case sensitivity. In cases where these words appeared multiple times, only the last instance was considered relevant. They tested the reliability of this method by manually examining a random sample of 100 responses and confirmed its accuracy in all instances.

## B.4 Evaluating the coverage of key facts in CoT [p. 13]

[p. 13] Coverage of the key facts that are relevant to the reasoning task in CoT outputs was done by searching for (case-insensitive) match of the key sentences in the key paragraphs, within the output of each model. Full coverage means that both key sentences from the input appear in the CoT output. They verified the reliability of this method manually on a sample of 100 responses.
