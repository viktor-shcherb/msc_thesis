# 3.1 Copying [p. 5]

providing concrete evidence that motivates the theoretical analysis presented in the following sections.

The authors start by providing motivating examples that show surprisingly simple failure cases of frontier LLMs specifically on copying (Section 3.1) and counting (Section 3.2) tasks. By copying they specifically mean tasks that involve the 'copying' or 'recalling' of a single or multiple tokens from the prompt. Instead, by counting, they mean the task of counting how many times a specific token appears in a sequence. The authors focus their evaluation on Gemini 1.5 [10] as their frontier LLM (referred as Gemini). They later analyse the internal representations of the open-sourced Gemma model [27]. The goal is to showcase intriguing failure cases which will motivate their signal propagation analysis.

**Figure 3** (p. 5): "Gemini 1.5 being prompted to sum $1 + \cdots + 1$ (Column 1), Count the number of ones in a sequence of 1s (Column 2), Count the number of ones in a sequence of ones and zeroes (the sequence is a Bernoulli sequence with probability of sampling a one being 0.7) (Column 3), and to counter the number of times a word appears in a sentence (Column 4)."

Description: Grid of 12 histograms (4 columns × 3 rows) showing model performance across different tasks
- Key elements: Row 1 labeled "No CoT", Row 2 labeled "Absolute Error w Zero-shot", Row 3 labeled "CoT Few-Shot"; Columns show different tasks: "Sum 1 + ... + 1", "Count Ones in 1...1", "Count Ones in 1[0...1]0", "Count Words in a Sentence"; x-axis shows sequence length (0-200) or value (0-200), y-axis shows frequency (0-175)
- Notable patterns: All rows show similar distribution patterns with peaks around certain values; performance varies across prompting strategies (No CoT, Zero-shot, Few-Shot); error distributions are concentrated but with some spread
- Supports claim: Demonstrates that even with different prompting strategies, Gemini 1.5 struggles with these simple counting and summing tasks, with errors that increase with sequence length

In this Section, the authors present surprising results on simple copying tasks. In particular, they focus on tasks that involve the copying of a single token — i.e. what is the token occurring at a particular position? The copy of a single token is in principle the most straightforward type of copying task, but still requires the LLM to accurately identify the token based on a prompt and to then propagate its information correctly.

Importantly, the authors study cases in which the LLM is prompted to copy tokens either at the start or at the end of a sequence. They avoid tasks that involve the copy of tokens at the 'n-th' position as most frontier LLMs do not have absolute positional information, making it very challenging for them to solve tasks that require absolute position. They focus on tasks that involve sequences of 'zeros' and 'ones' growing in length with specific patterns.

In Figure 2 (a), they prompt Gemini to copy the last element of a sequence '1...10' or the first element of a sequence '01...1'. The answer for both is zero, but they progressively grow the number of ones. They observe how the task seems considerably easier when asked to return the first rather than the last element. Surprisingly, already at a sequence length of only 300 elements, Gemini incorrectly starts to output 'one' when trying to copy the last element. In Figure 2 (b), they show that providing hints in the form of: "*Hint* It's not necessarily a 1, check carefully", helps significantly with the performance. Finally, in Figure 2 (c), they show that replacing the constant sequence of ones with alternating ones and zeros seems to also help. They refer to the Appendix (Section C.1) for further details on the experiments.

These three motivating experiments seem to point towards a type of vanishing of information, caused by the growing number of ones dominating the sequence. Interestingly, such a
