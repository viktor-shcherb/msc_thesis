# A Prompts [p. 11–13]

[p. 11] Table 5 shows ZeroSCROLLS prompts for summarization tasks, and Table 6 shows prompts for question answering and aggregation tasks. The prompts are designed to be simple, natural, and explicit. In braces are placeholders for the text of every example.

**Table 5** (p. 12): "Summarization task prompts. For chat models (ChatGPT, Claude, and GPT-4), we and omit the response header, as it is less appropriate for dialogue."

| Task | Prompt |
|---|---|
| GovReport | You are given a report by a government agency. Write a one-page summary of the report. <br><br> Report: <br> {REPORT} <br><br> Summary: |
| SummScreen | You are given a script of a TV episode. Summarize the episode in a paragraph. <br><br> Episode Script: <br> {SCRIPT} <br><br> Summary: |
| QMSum | You are given a meeting transcript and a query containing a question or instruction. Answer the query in one or more sentences. <br><br> Transcript: <br> {TRANSCRIPT} <br><br> Query: <br> {QUERY} <br><br> Answer: |
| SQuALITY | You are given a story and a question. Answer the question in a paragraph. <br><br> Story: <br> {STORY} <br><br> Question: <br> {QUESTION} <br><br> Answer: |

**Table 6** (p. 13): "Question answering and aggregation task prompts. For chat models (ChatGPT, Claude, and GPT-4), we add an additional instruction (in grey), and omit the response header, as it is less appropriate for dialogue."

| Task | Prompt |
|---|---|
| Qasper | You are given a scientific article and a question. Answer the question as concisely as you can, using a single phrase or sentence if possible. If the question cannot be answered based on the information in the article, write "unanswerable". If the question is a yes/no question, answer "yes", "no", or "unanswerable". *Do not provide any explanation.* <br><br> Article: <br> {ARTICLE} <br><br> Question: <br> {QUESTION} <br><br> Answer: |
| NarrativeQa | You are given a story, which can be either a novel or a movie script, and a question. Answer the question as concisely as you can, using a single phrase if possible. *Do not provide any explanation.* <br><br> Story: <br> {STORY} <br><br> Question: <br> {QUESTION} <br><br> Answer: |
| QuALITY | You are provided a story and a multiple-choice question with 4 possible answers (marked by A, B, C, D). Choose the best answer by writing its corresponding letter (either A, B, C, or D). *Do not provide any explanation.* <br><br> Story: <br> {STORY} <br><br> Question and Possible Answers: <br> {QUESTION_AND_OPTIONS} <br><br> Answer: |
| MuSiQue | You are given several paragraphs from Wikipedia and a question. Answer the question as concisely as you can, using a single phrase if possible. If the question cannot be answered based on the information in the paragraphs, write "unanswerable". *Do not provide any explanation.* <br><br> Paragraphs: <br> {PARAGRAPHS} <br><br> Question: <br> {QUESTION} <br><br> Answer: |
| SpaceDigest | You are given a list of reviews about a specific hotel. Each review is either positive or negative. What is the percentage of positive reviews (e.g. 60%, 34%, etc.)? *Do not provide any explanation.* <br><br> Reviews: <br> {REVIEWS} <br><br> Percentage of Positive Reviews: |
| BookSumSort | You are given {NUM_SUMMARIES} summaries of chapters or parts of a novel, in a shuffled order, where each summary is denoted by a numerical ID (e.g. Summary 1, Summary 3, etc.). Reorder the summaries according to the original order of chapters/parts in the novel by writing a list of length {NUM_SUMMARIES} of the summary IDs (e.g. if you were given 5 summaries, one possible answer could be "5, 1, 3, 4, 2"). *Do not provide any explanation.* <br><br> Summaries: <br> {SUMMARIES} <br><br> Summary IDs in Correct Order: |

Note: In Table 5 and Table 6, the italicized text marked with asterisks represents the grey-colored additional instructions that are added only for chat models (ChatGPT, Claude, and GPT-4). For non-chat models, those instructions are omitted and the response header is retained.
