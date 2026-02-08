# A. GSM-IC Details [p. 13–14]

[p. 13] Each of the 100 base problems requires two to seven steps to solve (Figure 5).

**Figure 5** (p. 13): "Base problem distribution of GSM-IC with respect to the number of reasoning steps in the ground truth problem solution."

Bar chart showing # Problems (y-axis) vs. # Steps (x-axis):
- 2 steps: 60 problems
- 3 steps: 15 problems
- 4 steps: 12 problems
- 5 steps: 9 problems
- 6 steps: 3 problems
- 7 steps: 1 problem

Starting from the base problems, the following protocols are used to create GSM-IC (Section 3.1):

## 1. Irrelevant sentence template

[p. 13] (a) For in-topic sentences, templates are manually written within the topic that is close to the original problem description. The authors are particularly careful about shareable stuff; for example, money is sometimes considered shareable between family members. They make sure that the added content does not change the amount of shareable stuff to ensure that the final standard answer is not affected.

(b) For off-topic sentences, general templates (Table 9) are used for all problems unless some of them can be considered as in-topic sentences for some problems -- for example, the sentence "The height of {role} is {number} feet." is considered as an in-topic sentence for problems about heights of people.

**Table 9** (p. 13): Off-topic sentence templates for GSM-IC.

| Template |
|---|
| The shoe size of [ROLE] is [NUMBER]. |
| [ROLE] is [NUMBER] years old. |
| The height of [ROLE] is [NUMBER] feet. |
| [ROLE] bought [NUMBER] tomatoes from the grocery store. |
| [ROLE] has read [NUMBER] books in the past year. |

(c) All sentences derived by each template are verified to be grammatical English sentences.

(d) Four in-topic and four off-topic distractor sentence templates are written and chosen for each problem.

## 2. Blank fillers: role names

[p. 13] (a) A role name X is randomly chosen, and `X's father`, `X's mother`, `X's brother`, `X's sister`, and `X's neighbor` are used as the overlapped role names.

(b) The name set {Ada, David, Emma, Jack, John, Mary, Max, Tom} is used for non-overlapped role names.

(c) Five names that have overlap with the original character and five names that do not have overlap are written for each problem.

## 3. Blank fillers: numbers

[p. 13–14] (a) For in-range numbers, positive integers are randomly sampled in the range of $[\frac{\ell}{10}, 10r]$, where $\ell$ and $r$ denote the smallest and the largest number that appear in the problem description and standard solution, respectively.

(b) For out-of-range numbers, numbers are chosen from the range of $[2, +\infty) \setminus [\frac{\ell}{10}, 10r]$. For very few problems that $\ell$ is relatively large (i.e., $\ell > 10^5$), out-of-range numbers are chosen from the range of $[2, \frac{\ell}{10}]$; for other problems, out-of-range numbers $n = a \times 10^b$ are chosen from the range $[10r, \infty)$, where $a$ and $b$ are both non-negative integers.

(c) Four in-range numbers and four out-of-range numbers are written for each problem.

## 4. Ambiguity resolution

[p. 14] Finally, if adding the irrelevant sentence causes ambiguity (e.g., Table 10), the question is fixed to ensure that the standard solution to the generated problem remains the same as the base problem.

**Table 10** (p. 14): An example that adding irrelevant contexts causes ambiguity: after adding the sentence, it is unclear whether "she" refers to Kim or Kim's mother. To ensure that the standard answer is unchanged, the final question is modified to make it clear and faithful to the original problem.

| | Text |
|---|---|
| *Original Problem* | Kim plants 80 cherry pits. 25% of them sprout and Kim sells 6 of the saplings. How many cherry saplings does she have left? |
| *Added Sentence* | Kim's mother plants 20 more potatoes. |
| *Ambiguous Problem* | Kim plants 80 cherry pits. 25% of them sprout and Kim sells 6 of the saplings. Kim's mother plants 20 more potatoes. How many cherry saplings does she have left? |
| *Fixed Problem* | Kim plants 80 cherry pits. 25% of them sprout and Kim sells 6 of the saplings. Kim's mother plants 20 more potatoes. How many cherry saplings does Kim have left? |
