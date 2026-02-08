# G Full Multi-Document Question Answering Results [p. 18]

This section tabulates model performance when evaluated on the multi-document QA task with varying numbers of documents (Figure 5). "Index n" indicates performance when the document with the answer occurs at position n + 1, where lower indices are closer to the start of the input context. For example, index 0 refers to performance when the document with the answer is placed at the very start of the context (i.e., first amongst all documents). [p. 18]

## G.1 10 Total Retrieved Documents

**Table 5** (p. 18): Model performance when evaluated on the multi-document QA task with 10 total retrieved documents.

| Model | Index 0 | Index 4 | Index 9 |
|---|---|---|---|
| Claude-1.3 | 62.9% | 58.3% | 59.7% |
| Claude-1.3 (100K) | 63.1% | 58.3% | 59.7% |
| GPT-3.5-Turbo | 76.8% | 61.2% | 62.4% |
| GPT-3.5-Turbo (16K) | 76.9% | 61.0% | 62.5% |
| MPT-30B-Instruct | 60.2% | 56.2% | 59.7% |
| LongChat-13B (16K) | 72.1% | 58.9% | 58.5% |

## G.2 20 Total Retrieved Documents

**Table 6** (p. 18): Model performance when evaluated on the multi-document QA task with 20 total retrieved documents.

| Model | Index 0 | Index 4 | Index 9 | Index 14 | Index 19 |
|---|---|---|---|---|---|
| Claude-1.3 | 59.9% | 55.9% | 56.8% | 57.2% | 60.1% |
| Claude-1.3 (100K) | 59.8% | 55.9% | 57.0% | 57.4% | 60.0% |
| GPT-3.5-Turbo | 75.8% | 57.2% | 53.8% | 55.4% | 63.2% |
| GPT-3.5-Turbo (16K) | 75.7% | 57.3% | 54.1% | 55.4% | 63.1% |
| MPT-30B-Instruct | 53.7% | 51.8% | 52.2% | 52.7% | 56.3% |
| LongChat-13B (16K) | 68.6% | 57.4% | 55.3% | 52.5% | 55.0% |

## G.3 30 Total Retrieved Documents

**Table 7** (p. 18): Model performance when evaluated on the multi-document QA task with 30 total retrieved documents.

| Model | Index 0 | Index 4 | Index 9 | Index 14 | Index 19 | Index 24 | Index 29 |
|---|---|---|---|---|---|---|---|
| Claude-1.3 | 59.1% | 55.1% | 54.8% | 55.7% | 56.4% | 56.2% | 59.9% |
| Claude-1.3 (100K) | 59.1% | 55.1% | 54.9% | 55.7% | 56.6% | 56.1% | 60.0% |
| GPT-3.5-Turbo (16K) | 73.4% | 55.1% | 50.5% | 50.9% | 51.8% | 54.9% | 63.7% |
| MPT-30B-Instruct | 51.6% | 51.3% | 51.2% | 49.0% | 49.6% | 51.3% | 54.1% |
| LongChat-13B (16K) | 66.9% | 54.8% | 52.5% | 52.9% | 52.2% | 51.3% | 55.1% |
