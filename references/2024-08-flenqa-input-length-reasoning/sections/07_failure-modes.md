# 7 Length-induced Failure Modes [p. 8-9]

[p. 8] The authors find four *failure modes* (footnote 7: All failure modes can be measured automatically using the code in their repository): consistent patterns that correlate with incorrect responses.

## Failure to answer

All of the samples in the dataset can be answered with either "True" or "False", as instructed in the prompts (Appendix B). However, some of LLMs responded with a refusal answer the question, often preceded by a sentence such as "There is not enough information in the text".

> "This tendency grows as the input length increases," [p. 8]

indicating a failure to comply to the instruction that specified a clear choice between "True" and "False". The trend is demonstrated in Figure 7, and results over all models in Appendix C.

## Label bias

As discussed in Section 3, the dataset is completely balanced in the label distribution. The authors find that certain LLMs tend to favour one of the labels, typically "false", as the input length grows. Results for all models are in Appendix C.

**Figure 7** (p. 8): "The models exhibit two types of input-length dependent biases: (a) They tend to generate 'False' more often than 'True', and (b) they ignore instructions and generate answers which do not contain neither."
- Title: "Gemini Pro bias in answer generation, and non-answers"
- X-axis: Input length (# tokens), values: 250, 500, 1000, 2000, 3000
- Y-axis: Frequency, range 0 to ~400
- Bars for True (green), Other/Refused (dark/black), False (orange)
- Dashed line at 300 indicating Samples Per Label
- At 250 tokens, True and False bars are roughly balanced near the 300 line. As input length increases, False answers grow (reaching ~400 at 3000 tokens), True answers shrink (dropping to ~100 at 3000 tokens), and Other/Refused answers increase from near 0 to a noticeable proportion.

## Answer first, reason later

[p. 8-9] When using Chain-of-Thought prompting, some LLMs were much more likely to output the final true/false answer *before* the expected reasoning steps, as inputs grow longer. In recent work, Kojima et al. 2022 found that when models are elicited to provide the reasoning steps after the answer their performance does not increase (as expected when using auto-regressive models that only attend to earlier tokens). This can be viewed as a case of failing to follow prompt instructions (see prompt instructions in Appendix B) as the length increases. In testing, the authors found that incorrect responses are statistically dependent on the occurrence of answers before the reasoning steps.

Footnote 8: Corresponding odds-ratio is 3.643 with p < 0.001 obtained through Fisher exact test.

**Figure 8** (p. 9): "Most of the models tend to generate an answer before the reasoning steps, in a zero-shot CoT prompt setting, and do so more as input length increases."
- Title: "Early responses in CoT"
- X-axis: Input length (# tokens), values: 250, 500, 1000, 2000, 3000
- Y-axis: Frequency, range 0 to ~300
- Grouped bars for GPT3.5 (blue), GPT4 (green), Gemini Pro (yellow), Mistral Medium (purple), Mixtral 8x7B (pink)
- Most models show increasing frequency of early responses (answer before reasoning) as input length grows. GPT3.5 shows the most dramatic increase, reaching ~300 at 3000 tokens. GPT4 remains relatively low across all lengths. Gemini Pro and Mistral Medium show moderate increases.

## Chain-of-Thought lack of coverage

[p. 9] All the tasks in FLenQA require the LLM to: (1) locate the relevant texts within the input; and (2) perform the relevant reasoning over them. Ideally, the CoT prompt would elicit the LLM to first locate each of the relevant texts and copy them to the "steps" part, hence avoiding the effect of long input on reasoning. However, the authors find that as input length grows, LLMs ability to do this degrades (Figure 9).

They measure this by computing the coverage of the relevant text (the key sentences in each sample in the models' "steps" part of the outputs, details in Appendix B.4). They find that in most models, the ability to locate the relevant text within the input *decreases* as the input length gets longer. They found incorrect responses were statistically dependent on the incomplete coverage of the facts.

Footnote 9: Corresponding odds-ratio is 3.138 with p < 0.001 obtained through Fisher exact test.

**Figure 9** (p. 9): "CoT coverage of relevant facts. As input grows, all models fail more often in outputting the task-relevant information at the CoT reasoning steps stage."
- Title: "CoT coverage per model"
- X-axis: Input length (# tokens), values: 250, 500, 1000, 1500, 2000, 2500, 3000
- Y-axis: Coverage rate, range 0.0 to ~0.6
- Lines for GPT3.5, GPT4, Gemini Pro, Mistral Medium, Mixtral 8x7B
- All models show declining coverage rates as input length increases. GPT4 starts highest (~0.6 at 250 tokens) and declines to ~0.3 at 3000 tokens. GPT3.5 starts around 0.4-0.5 and drops sharply. Gemini Pro starts around 0.3 and declines. Mistral Medium and Mixtral 8x7B remain lower throughout, both declining to near 0.1-0.2 at 3000 tokens.
