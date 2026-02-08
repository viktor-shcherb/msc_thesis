# 12.14. Vision tasks [p. 137–140]

[p. 137] All vision tasks are evaluated 0-shot with an instruction-tuned model. Preamble instructions are added to ensure that each task follows the answer format the task expects.

## 12.14.1. V* benchmark [p. 137]

[p. 137] High resolution images contain a large amount of detailed content and semantics. Responding to queries about those details (hi-res queries) is a relatively easy task for humans as long as the information is in the image. Multimodal LLMs require special care to answer hi-res queries well. The performance of Gemini is evaluated on the V* benchmark (Wu and Xie, 2023) which is a high resolution subset of SA-1B dataset (Kirillov et al., 2023) with an average resolution of 2246 x 1582. It consists of two sub-tasks: (a) attribute recognition with 115 samples and (b) spatial reasoning with 76 samples. The attribute recognition task asks about attributes of small objects in the image such as their color or material. The spatial reasoning task asks about the relative position of small objects in the image. The dataset is in a question answering format with multiple options that are carefully crafted by human annotators. While previous performance of Multimodal LLMs was quite low, Gemini 1.5 Pro obtains better performance than other commercial chatbots such as GPT-4V and is within a few points of the expensive LLM guided visual search solution (SEAL) proposed in Wu and Xie (2023). The answer options in each example are randomized so that the correct answer is not always at the same position.

Prompt:

```
Question: You are given an image, a question, and a number of options to answer the
question as follows:

Question:
Is the flag red or white?

Options:
The color of the flag is white.
The color of the flag is red.

Answer instructions: Choose the most likely option. If you find that it is impossible to
 answer the question or none of the options are correct choose the most likely option.
Only answer with the most likely option verbatim without any extra words or changes to
the option.
```

## 12.14.2. AI2D [p. 137]

[p. 137] Prompt:

```
Answer exactly as one of the choices.
<image>
Question: {question} The Choices are: {options} Answer:
```

## 12.14.3. MMMU [p. 137–138]

[p. 138] Prompt:

```
Question: {question with images} Options: {options}
Try to reason about the question step by step to help you get the correct answer. You
might find that sometimes no reasoning is needed if the answer is straightforward.
Sometimes listing out a few reasoning steps will be helpful. In any case, please keep
the reasoning concise.

First, please describe what is included in the image. Then, respond with your reason
first and output the final answer in the format "Final Answer: <answer>" where <answer>
is the single correct letter choice (A), (B), (C), (D), (E), (F), etc, when options are
provided. If you find that your reasoning lead to none of the choice, reject your
reasoning and choose the most likely answer. You have to answer with one of the choices.
 If no options are provided, <answer> is your answer. If you would like to skip
reasoning, just directly output the "Final Answer" part.
```

## 12.14.4. MathVista [p. 138]

[p. 138] Prompt:

```
<MathVista preamble>
<image>
Question: <Question>
Try to reason about the question below step by step to help you get the correct answer.
Formulate your answer as follows.
**Image and question:** Please describe what is the image about and what does the
question ask for. If there are technical terms, privide a brief definition. For math
questions, point out what technique is needed to solve the question. If the question
involves number of objects, enumearte over the objects you see.
**Reasoning:** Please include your reasoning to solve this question.
**Final Answer:** <answer>" where <answer> is your answer to the question.
Keep the answer short and terse. Do not paraphrase or reformat the text you see in the
image.
For question about age difference, try to identify who are the people and on which year
were they born. Then calculate their age difference.
For multiple choice questions, if you find that your reasoning lead to none of the
choice, reject your reasoning and choose the most likely answer. You have to answer with
 one of the choices for multiple choice questions. In any case, never refuse to answer.
Make your best guess if not sure.
```

Where the MathVista preamble is given by Table 9 from the MathVista paper (e.g. "Hint: Please answer the question requiring an integer answer and provide the final value, e.g., 1, 2, 3, at the end.").

## 12.14.5. ChartQA [p. 138]

[p. 138] Prompt:

```
Think step by step before giving a final answer to this question.Format your final
answer as 'Final Answer: X'. For the final answer X, follow the following instructions:
* X should contain as few words as possible.
* Don't paraphrase or reformat the text you see in the image.
* If the final answer has two or more items, provide it in the list format like [1, 2].
* When asked to give a ratio, give out the decimal value like 0.25 instead of 1:4.
* When asked to give a percentage, give out the whole value like 17 instead of decimal
like 0.17%.
* Don't include any units in the answer.
* Try to include the full label from the graph when asked about an entity.
Remember, don't give a final answer before step by step reasoning and always format your
 final answer as 'Final Answer: X'.
```

## 12.14.6. ChemicalDiagramQA [p. 139]

[p. 139] Understanding of scientific literature is an important capability for the models and one very common visual element of scientific communication are chemical structure diagrams (McMurry, 2012; Wikipedia contributors, 2024). To evaluate the models' understanding of these diagrams in the context of figures from real publications, a set of 76 multiple choice questions bucketed into 3 levels of difficulty was created. Easy problems have a scope of a single structure diagram, medium problems have a scope of a single paper subfigure, and hard problems have a scope of a full paper figure. Each figure is self-contained and has all the necessary information to answer the question. The figures are sourced from randomly selected biorxiv papers in synthetic biology, biochemistry, bioengineering sections and US patents. Figure 30 shows examples of questions used.

Each question test is suffixed with the following prompt:

```
Write your reasoning, then end with the answer in the format "Answer: <a,b,c,d>"
```

**Figure 30** (p. 139): "Examples of questions used to evaluate chemical structure understanding."

The figure shows three columns of increasing difficulty:
- **Isolated Diagram:** A single chemical structure (appears to show a purine-based molecule with amino groups) with the question "What is a chemical formula for the following diagram?" and four multiple choice answers (a–d) of molecular formulas (e.g., C16H32N8O4, C16H28N8O4, C15H30N8O6, C15H30N8O4).
- **Sub-Figure:** A subfigure labeled "A" showing several chemical structures (AzF, CMF, AcK) with the question "How many Nitrogen atoms are in chemical structure diagram AzF?" and choices a) 2, b) 3, c) 4, d) 5.
- **Full Figure:** A complex figure depicting a biosynthetic pathway from *Burkholderia thailandensis* E264 with gene clusters and enzyme structures, with the question "How many oxygen atoms are in MNiO part of the chemical structure?" and choices a) 1, b) 3, c) 5, d) 9.

## 12.14.7. DocVQA [p. 139]

[p. 139] Prompt:

```
Give a short and terse answer to the following question. Do not paraphrase or reformat
the text you see in the image. Do not include any full stops. Just give the answer
without additional explanation.
<image>
Question: {question} Answer:
```

## 12.14.8. DUDE [p. 139]

[p. 139] Prompt:

```
Give a short and terse answer to the following question. Do not paraphrase or reformat
the text you see in the images. Do not include any full stops. Just give the answer
without additional explanation. Use newline to separate multiple answers. If the
question cannot be answered based on the images, output <no_answer>. <images> Question: {
question} Answer:
```

## 12.14.9. TAT-DQA [p. 139]

[p. 139] Prompt:

```
Give a short and terse answer to the following question. Do not paraphrase or reformat
the text you see in the images. Do not include any full stops. Just give the answer
without additional explanation. Use ", " for separation where applicable. <images>
Question: {question} Answer:
```

## 12.14.10. InfographicVQA [p. 140]

[p. 140] Prompt:

```
Give a short and terse answer to the following question. Do not paraphrase or reformat
the text you see in the image. Do not include any full stops. Just give the answer
without additional explanation.
<image>
Question: {question} Answer:
```

## 12.14.11. TextVQA [p. 140]

[p. 140] Prompt:

```
Answer the following question about the image using as few words as possible. Follow
these additional instructions:
* Always answer a binary question with Yes or No.
* When asked what time it is, reply with the time seen in the image.
* Do not put any full stops at the end of the answer.
* Do not put quotation marks around the answer.
* An answer with one or two words is favorable.
* Do not apply common sense knowledge. The answer can be found in the image.
<image>
Question: {question} Answer:
```

## 12.14.12. VQAv2 [p. 140]

[p. 140] Prompt:

```
Answer the following question about the image using only a word or two. Always answer a
binary question with Yes or No.'
<image>
Question: {question} Answer:
```
