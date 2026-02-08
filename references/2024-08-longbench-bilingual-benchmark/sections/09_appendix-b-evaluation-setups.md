# B Evaluation Setups [p. 14-17]

[p. 14] In this section, a collection of customized prompt templates designed for each dataset within LongBench is presented, utilized during evaluation. Each data instance is accompanied by an input *I* as well as a context *C*. The instruction is placed both at the beginning and end of the prompt, ensuring the models fully grasp what to do.

## Evaluation Prompts [p. 14-16]

### Single-Document QA

**NarrativeQA** [p. 14]:
```
NarrativeQA: You are given a story, which can be either a novel or a movie script, and a question.
Answer the question as concisely as you can, using a single phrase if possible. Do not provide any
explanation.
Story: {context}
Now, answer the question based on the story as concisely as you can, using a single phrase if possible.
Do not provide any explanation.
Question: {input}
Answer:
```

**Qasper** [p. 14-15]:
```
Qasper: You are given a scientific article and a question. Answer the question as concisely as you
can, using a single phrase or sentence if possible. If the question cannot be answered based on the
information in the article, write "unanswerable". If the question is a yes/no question, answer "yes",
"no", or "unanswerable". Do not provide any explanation.
Article: {context}
Answer the question based on the above article as concisely as you can, using a single phrase or
sentence if possible. If the question cannot be answered based on the information in the article, write
"unanswerable". If the question is a yes/no question, answer "yes", "no", or "unanswerable". Do not
provide any explanation.
Question: {input}
Answer:
```

**MultiField-en** [p. 15]:
```
MultiField-en: Read the following text and answer briefly.
{context}
Now, answer the following question based on the above text, only give me the answer and do not
output any other words.
Question: {input}
Answer:
```

**MultiField-zh** [p. 15]:
```
MultiField-zh: 阅读以下文字并用中文简短回答：
{context}
现在请基于上面的文章回答下面的问题，只告诉我答案，不要输出任何其他字词。
问题：{input}
回答：
```

### Multi-Document QA

**HotpotQA** [p. 15]:
```
HotpotQA: Answer the question based on the given passages. Only give me the answer and do not
output any other words.
The following are given passages.
{context}
Answer the question based on the given passages. Only give me the answer and do not output any
other words.
Question: {input}
Answer:
```

**2WikiMultihopQA** [p. 15]:
```
2WikiMultihopQA: Answer the question based on the given passages. Only give me the answer and
do not output any other words.
The following are given passages.
{context}
Answer the question based on the given passages. Only give me the answer and do not output any
other words.
Question: {input}
Answer:
```

**MuSiQue** [p. 15]:
```
MuSiQue: Answer the question based on the given passages. Only give me the answer and do not
output any other words.
The following are given passages.
{context}
Answer the question based on the given passages. Only give me the answer and do not output any
other words.
Question: {input}
Answer:
```

**DuReader** [p. 15-16]:
```
DuReader: 请基于给定的文章回答下述问题。
文章：{context}
请基于上述文章回答下面的问题。
问题：{input}
回答：
```

### Summarization

**GovReport** [p. 16]:
```
GovReport: You are given a report by a government agency. Write a one-page summary of the
report.
Report:
{context}
Now, write a one-page summary of the report.
Summary:
```

**QMSum** [p. 16]:
```
QMSum: You are given a meeting transcript and a query containing a question or instruction. Answer
the query in one or more sentences.
Transcript:
{context}
Now, answer the query based on the above meeting transcript in one or more sentences.
Query: {input}
Answer:
```

**MultiNews** [p. 16]:
```
MultiNews: You are given several news passages. Write a one-page summary of all news.
News:
{context}
Now, write a one-page summary of all the news.
Summary:
```

**VCSUM** [p. 16]:
```
VCSUM: 下面有一段会议记录，请你阅读后，写一段总结，总结会议的内容。
会议记录：
{context}
会议总结：
```

### Few-shot Learning

**TREC** [p. 16]:
```
TREC: Please determine the type of the question below. Here are some examples of questions.
{context}
{input}
```

**TriviaQA** [p. 16]:
```
TriviaQA: Answer the question based on the given passage. Only give me the answer and do not
output any other words. The following are some examples.
{context}
{input}
```

**SAMSum** [p. 16]:
```
SAMSum: Summarize the dialogue into a few short sentences. The following are some examples.
{context}
{input}
```

**LSHT** [p. 16]:
```
LSHT: 请判断给定新闻的类别，下面是一些例子。
{context}
{input}
```

### Synthetic Task

**PassageCount** [p. 16-17]:
```
PassageCount: There are some paragraphs below sourced from Wikipedia. Some of them may be
duplicates. Please carefully read these paragraphs and determine how many unique paragraphs there
are after removing duplicates. In other words, how many non-repeating paragraphs are there in total?
{context}
Please enter the final count of unique paragraphs after removing duplicates. The output format should
only contain the number, such as 1, 2, 3, and so on.
The final answer is:
```

**PassageRetrieval-en** [p. 17]:
```
PassageRetrieval-en: Here are 30 paragraphs from Wikipedia, along with an abstract. Please
determine which paragraph the abstract is from.
{context}
The following is an abstract.
{input}
Please enter the number of the paragraph that the abstract is from. The answer format must be like
"Paragraph 1", "Paragraph 2", etc.
The answer is:
```

**PassageRetrieval-zh** [p. 17]:
```
PassageRetrieval-zh: 以下是若干段落文字，以及其中一个段落的摘要。请确定给定的摘要
出自哪一段。
{context}
下面是一个摘要
{input}
请输入摘要所属段落的编号。答案格式必须是"段落1"，"段落2"等格式
答案是：
```

### Code Completion

**LCC** [p. 17]:
```
LCC: Please complete the code given below.
{context}Next line of code:
```

**RepoBench-P** [p. 17]:
```
RepoBench-P: Please complete the code given below.
{context}{input}Next line of code:
```

## Maximum Output Length [p. 17]

A maximum output length is set on each dataset during evaluation to prevent the models from non-stop generation.

| Task-Dataset | 1-1 | 1-2 | 1-3 | 1-4 | 2-1 | 2-2 | 2-3 | 2-4 | 3-1 | 3-2 | 3-3 | 3-4 | 4-1 | 4-2 | 4-3 | 4-4 | 5-1 | 5-2 | 5-3 | 6-1 | 6-2 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Max Output Length | 128 | 128 | 64 | 64 | 32 | 32 | 32 | 128 | 512 | 512 | 512 | 64 | 32 | 128 | 64 | 32 | 32 | 32 | 64 | 64 | 64 |
