# 12.13. Prompts and answer extraction strategies [p. 132–136]

## 12.13.1. BBH [p. 132]

[p. 132] For BIG-Bench Hard (BBH), the following preamble is used before the 10 shots:

```
Continue the following text without adding any additional information or formatting.
```

This is followed by a snippet describing the specific Big Bench task, e.g.:

```
Evaluate the result of a random Boolean expression.
```

Then few-shot examples are provided as in Srivastava et al. (2022), in the form:

```
Q: <question>
A: Let's think step by step.
<gold chain of thought>. So the answer is <gold answer>.
```

The prompt ends by posing the final question as:

```
Q: <question>
A: Let's think step by step.
```

For answer extraction, the answer is parsed out from `"So the answer is {answer}"`.

## 12.13.2. DROP [p. 133–134]

[p. 133] For DROP, three fixed examples are used. Each example consists of a passage followed by Q/A pairs. The examples are:

1. A passage about a Chicago Bears vs. New York Jets game (week eleven), with:
   - Q: "How many points did the Jets score?" A: 0

2. A passage about Philip Rivers throwing touchdowns and Dak Prescott throwing picks, with:
   - Q: "Who threw two interceptions?" A: Dak Prescott

3. A passage from a reference work entry (Kalma, J.J., De Tille, ed. Grote Pier Van Kimswerd), with:
   - Q: "Who published The Age of Erasmus, Lectures Delivered in the Universities of Oxford and London?" A: Clarendon Press

[p. 133] Furthermore, for each paragraph in the DROP dataset, the order of questions is standardized. The prompt incorporates three predetermined examples alongside additional examples derived from previously posed questions related to the same paragraph. An illustrative paragraph with two associated questions is provided (a passage about a Raiders vs. Houston Texans game):
- Q: "Who scored the first touchdown of the game?" A: Chaz Schilens
- Q: "How many field goals did Kris Brown kick?" A: (left blank for the model to answer)

[p. 133] An additional instruction is also added:

```
You are an expert at reasoning. I am going to give you a variable number of
demonstrations of paragraphs and questions and answers about those paragraphs. The
questions are marked with "Q:", and the answers are marked with "A:". After the
demonstrations, I am going to give one final question whose answer is blank, and I want
you to answer it. When you provide the final answer, please give only the answer, with
no commentary, formatting, or markup.\n\n
```

[p. 134] When postprocessing the answer, all the model output before a newline is taken and compared to the ground truth.^38

^38 For the metric calculation we use an implementation similar to https://github.com/google-research/text-to-text-transfer-transformer/blob/main/t5/evaluation/qa_utils.py#L71.

## 12.13.3. Hellaswag [p. 134]

[p. 134] For Hellaswag, this preamble is added before the 10 shots:

```
Continue the following text without adding any additional information or formatting:
```

Shots are formatted as:

```
<prefix>
A) <completion A>
B) <completion B>
C) <completion C>
D) <completion D>
What is the right option? <gold choice of ABCD>
```

The final question is posed in the same format as the shots, leaving out the final gold answer, and then each possible letter answer is scored. There is no postprocessing since this is run as a scoring task.

## 12.13.4. MMLU [p. 134]

[p. 134] For MMLU, this preamble is added before the shots:

```
Continue the following text without adding any additional information or formatting:
```

Shots are formatted as:

```
<question>
(A) <answer A>
(B) <answer B>
(C) <answer C>
(D) <answer D>
Answer: <gold choice of ABCD>
```

After the shots, the final question is posed as above, leaving out the gold choice and ending with `Answer:`. There is no postprocessing, since this is run as a scoring eval. Each of the letters A, B, C, or D is scored and the one with highest score is taken. Few-shot examples are as in the original MMLU repository.^39

^39 https://github.com/hendrycks/test

## 12.13.5. AMC [p. 134–135]

[p. 134] For AMC, this preamble is added before the shots:

```
You are a math expert. I am going to give you a series of demonstrations of math
Problems and Solutions. When you respond, respond only with the Solution of the final
Problem, thinking step by step. End the Solution with the final answer in the form "
Final Answer: The final answer is ?. I hope it is correct.", where ? is replaced by one
of the letters A, B, C, D or E.
```

[p. 135] In the AMC prompt, four examples from previous AMC competitions are used:

**Example 1:**
- Problem: When Clara totaled her scores, she inadvertently reversed the units digit and the tens digit of one score. By which of the following might her incorrect sum have differed from the correct one?
- Choices: $A: 45 \quad B: 46 \quad C: 47 \quad D: 48 \quad E: 49$
- Final Answer: A

**Example 2:**
- Problem: Hammie is in the $6^\text{th}$ grade and weighs 106 pounds. His quadruplet sisters are tiny babies and weigh 5, 5, 6, and 8 pounds. Which is greater, the average (mean) weight of these five children or the median weight, and by how many pounds?
- Choices: $A: \text{median, by 60} \quad B: \text{median, by 20} \quad C: \text{average, by 5} \quad D: \text{average, by 15} \quad E: \text{average, by 20}$
- Final Answer: E

**Example 3:**
- Problem: The Incredible Hulk can double the distance he jumps with each succeeding jump. If his first jump is 1 meter, the second jump is 2 meters, the third jump is 4 meters, and so on, then on which jump will he first be able to jump more than 1 kilometer (1,000 meters)?
- Choices: $A: 9^\text{th} \quad B: 10^\text{th} \quad C: 11^\text{th} \quad D: 12^\text{th} \quad E: 13^\text{th}$
- Final Answer: C

**Example 4:**
- Problem: A fair coin is tossed 3 times. What is the probability of at least two consecutive heads?
- Choices: $A: \frac{1}{8} \quad B: \frac{1}{4} \quad C: \frac{3}{8} \quad D: \frac{1}{2} \quad E: \frac{3}{4}$
- Final Answer: C

Each example follows the format:
```
Problem:
<problem text>
?
<answer choices>
Solution:
<expert-written solution>
Final Answer: The final answer is [letter]. I hope it is correct.
```

[p. 135] To pose the final question, the prompt ends with:

```
Problem:
<question>
```

The answer is located by searching for the prefix `"Final Answer:  The final answer is "` and the suffix `". I hope it is correct."` The answer is identified as the first letter A, B, C, D, or E found between the prefix and suffix.

## 12.13.6. MATH [p. 135–136]

[p. 135] In the zero-shot MATH evaluations, just the problem statement is provided. Gemini 1.0 Pro is used to extract the answer.

In 4-shot evaluations, a 4-shot prompt available in Lewkowycz et al. (2022) is used. Additionally, the model receives the following instruction:

```
You are a math expert. I am going to give you a series of demonstrations of math
Problems and Solutions. When you respond, respond only with the Solution of the final
Problem, thinking step by step. At the end of the Solution, when you give your final
answer, write it in the form "Final Answer: The final answer is $answer$. I hope it is
correct."
```

[p. 136] The answer is located by searching for the prefix `"Final Answer: The final answer is "` and the suffix `". I hope it is correct."`. This process also considers markdown formatting variations, such as `"**Final Answer**"`. Between the identified prefix and suffix, the system looks for a LaTeX string in the format `$answer$`, where "answer" can be any sequence of characters. If the prefix and suffix are not found, the system searches for a LaTeX string in the format `\boxed{answer}`. If the extracted answer doesn't exactly match the target answer, a symbolic parser implemented in SymPy is employed. This helps to match equivalent expressions like `$1 + \sqrt{3}$` and `$\sqrt{3} + 1$`. In case the symbolic parser fails, SymPy is used to evaluate the LaTeX expression and compare its numerical value to the target answer. This comparison uses absolute and relative tolerances of 1e-4 to account for minor numerical discrepancies, such as those between 1 and 0.9999999.

## 12.13.7. GSM8K [p. 136]

[p. 136] For GSM8K, an 8-shot prompt provided by Cobbe et al. (2021) is utilized. In some experiments this prompt is expanded to include 11 examples. Additionally, the model is instructed with the following:

```
You are a math expert. I am going to give you a series of demonstrations of math
Problems and Solutions. When you respond, respond only with the Solution of the final
Problem, thinking step by step. At the end of the Solution, when you give your final
answer, write it in the form "The answer is <ANSWER>."
```

At evaluation time, the final number in the model response is extracted and used as the answer.

## 12.13.8. GPQA [p. 136]

[p. 136] For GPQA, the model is instructed to perform chain of thought reasoning and then give a final answer which can be parsed correctly. The prompt used is:

```
Always finish your answer with 'Final Answer: (X)', where X is the correct answer choice.
 If none or more than one of the options match, choose the closest option as the final
answer.
```

## 12.13.9. PhysicsFinals [p. 136]

[p. 136] For the unreleased PhysicsFinals benchmark, described in Section 6.1.1, there was no prompt, and the question was just inputted directly into the instruction-tuned models. An example of the complete input for one of the questions:

```
Suppose there are 8 degenerate states. We randomly (thermally) assign three
indistinguishable bosons to these 8 states. What is the probability for all three bosons
to be found in the same state?
```

The model response was then graded by a human expert.

## 12.13.10. HumanEval and Natural2Code [p. 136]

[p. 136] HumanEval and Natural2Code prompts were designed to test the model on the completion of a function. The prompt is slightly modified to allow the generalist agent to understand that this is a completion task with the chat preamble. Without this modification, the agent often asks clarifying questions. The prompt format is:

```
Write the following function:
'''
{original prompt}
'''
```

[p. 137] The postprocessing is adjusted to expect a full code markdown block. The hidden unit tests are appended to this block and are executed inside a sandbox environment to compute the final pass rate.
