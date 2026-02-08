# 5 Analysis [p. 7–9]

[p. 7–8] While GPT-4 has the highest score on the ZeroSCROLLS leaderboard, the authors find it surprising that other models score higher on a number of question answering tasks. They analyze model generations and observe that GPT-4 responses do not match the desired output format (despite explicit instructions in the prompt), which results in penalization by the automatic metrics. Further analysis reveals that format discrepancy is a phenomenon that occurs across different LLMs and tasks, and is not unique to GPT-4 and question answering.

## Discrepancies in Question Answering

[p. 7–8] The authors analyze the responses of GPT-4 and Claude for NarrativeQA (where Claude scores 5 points higher), and the responses of GPT-4 and Flan-UL2 for Qasper and MuSiQue (where Flan-UL2 scores 6.2 and 10.2 points higher, respectively). Specifically, they sample 100 instances from each dataset, and annotate whether the answer is correct, ignoring formatting, fluency, or other factors. Figure 4 shows that, in contrast to the F1 scores, GPT-4 performs better than Claude and Flan-UL2 on NarrativeQA and Qasper, respectively, and that the gap between GPT-4 and Flan-UL2 on MuSiQue is smaller in practice. [p. 8]

From examining the generated texts, the authors learn that GPT-4 consistently generates complete answers even though the prompt instructs otherwise (see Section 3.2 and Appendix A). They further analyze 200 random instances from NarrativeQA and check whether GPT-4 and Claude respond in the specified format, i.e. "using a single phrase if possible," regardless of whether the content is correct or not. While Claude answers 191 questions in the correct format, GPT-4 does so for only 71 out of the 200 analyzed examples -- explaining why GPT-4 is penalized harder by the F1 metric, despite being "correct" more often than Claude.^9 [p. 8]

> ^9 "Another interesting observation from analyzing NarrativeQA is that GPT-4 sometimes responds that it is unable to answer the question because the (trimmed) context does not contain the answer. It does so for 30 out of 200 cases, while Claude generates a similar response for only 5, despite both models having similar context lengths (8k)." [p. 8, footnote]

## Format Discrepancy

[p. 8–9] Figure 5 surveys the distribution of output lengths across multiple tasks and models. In most cases, models generate outputs that fall within the distribution of reference lengths, indicating that the format criteria provided in the prompts are sufficient. However, certain task-model combinations fall outside of the reference distribution. While the NarrativeQA plot confirms the previous observation that GPT-4 generates longer answers for this task, the authors find that format discrepancy is not unique to this dataset or GPT-4, as different models struggle to generate texts in the correct format on different tasks: Claude generates long answers for QMSum, Flan-UL2 generates long summaries in SummScreenFD, and all models generate short summaries for GovReport, which negatively impacts their scores. [p. 8–9]

**Figure 5** (p. 8–9): "Distribution of the number of generated words."

The figure shows violin plots for the distribution of output lengths (number of generated words) for Flan-UL2, ChatGPT, Claude, GPT-4, and the Reference distribution, across seven tasks: MuSiQue, SQuALITY, NarrativeQA, Qasper, QMSum, SummScreenFD, and GovReport. Key observations from the plots:
- MuSiQue: all models produce very short outputs (under ~15 words), similar to references.
- SQuALITY: reference distribution peaks around 200–300 words; model outputs are generally shorter, around 100–200 words.
- NarrativeQA: reference distribution is concentrated under ~10 words; GPT-4 produces substantially longer outputs (up to ~30 words).
- Qasper: reference distribution is short; models generally match, with some longer tails.
- QMSum: reference peaks near 50 words; Claude generates notably longer outputs.
- SummScreenFD: reference peaks around 100–150 words; Flan-UL2 generates longer summaries.
- GovReport: reference distribution peaks around 500–750 words; all models generate much shorter summaries (under ~250 words). [p. 8–9]
