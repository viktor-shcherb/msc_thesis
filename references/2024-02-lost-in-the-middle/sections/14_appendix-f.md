# F Token Counts [p. 17]

Tables 2, 3, and 4 present the average and maximum number of tokens in each of the input contexts for all experimental settings. MPT-30B and MPT-30B-Instruct use the same tokenizer, GPT-3.5-Turbo and GPT-3.5-Turbo (16K) use the same tokenizer, and Claude-1.3 and Claude-1.3 (100K) use the same tokenizer. Furthermore, the Claude-1.3 tokenizer is the same as the GPT-3.5-Turbo tokenizer, modulo some additional special tokens that do not appear in the data. As a result, the token counts for these two model families are the same in the experimental settings. [p. 17]

## Table 2

**Table 2** (p. 17): Token count statistics for each of the evaluated models on the closed-book and oracle multi-document question answering settings.

| Model | Closed-Book avg +/- stdev | Closed-Book max | Oracle avg +/- stdev | Oracle max |
|---|---|---|---|---|
| LongChat-13B (16K) | 55.6 +/- 2.7 | 70 | 219.7 +/- 48.5 | 588 |
| MPT-30B | 43.5 +/- 2.2 | 58 | 187.9 +/- 41.8 | 482 |
| GPT-3.5-Turbo | 15.3 +/- 2.2 | 29 | 156.0 +/- 41.8 | 449 |
| Claude-1.3 | 15.3 +/- 2.2 | 29 | 156.0 +/- 41.8 | 449 |

## Table 3

**Table 3** (p. 17): Token count statistics for each of the evaluated models on each of the document question answering settings.

| Model | 10 docs avg +/- stdev | 10 docs max | 20 docs avg +/- stdev | 20 docs max | 30 docs avg +/- stdev | 30 docs max |
|---|---|---|---|---|---|---|
| LongChat-13B (16K) | 1749.9 +/- 112.4 | 2511 | 3464.6 +/- 202.3 | 4955 | 5181.9 +/- 294.7 | 7729 |
| MPT-30B | 1499.7 +/- 88.5 | 1907 | 2962.4 +/- 158.4 | 3730 | 4426.9 +/- 230.5 | 5475 |
| GPT-3.5-Turbo | 1475.6 +/- 86.5 | 1960 | 2946.2 +/- 155.1 | 3920 | 4419.2 +/- 226.5 | 6101 |
| Claude-1.3 | 1475.6 +/- 86.5 | 1960 | 2946.2 +/- 155.1 | 3920 | 4419.2 +/- 226.5 | 6101 |

## Table 4

**Table 4** (p. 17): Token count statistics for each of the evaluated models on each of the key-value (KV) retrieval settings.

| Model | 75 KV pairs avg +/- stdev | 75 KV pairs max | 140 KV pairs avg +/- stdev | 140 KV pairs max | 300 KV pairs avg +/- stdev | 300 KV pairs max |
|---|---|---|---|---|---|---|
| LongChat-13B (16K) | 5444.5 +/- 19.1 | 5500 | 10072.4 +/- 24.1 | 10139 | 21467.3 +/- 35.9 | 21582 |
| MPT-30B | 4110.5 +/- 23.8 | 4187 | 7600.9 +/- 31.1 | 7687 | 16192.4 +/- 46.6 | 16319 |
| GPT-3.5-Turbo | 3768.7 +/- 25.6 | 3844 | 6992.8 +/- 34.1 | 7088 | 14929.4 +/- 50.7 | 15048 |
| Claude-1.3 | 3768.7 +/- 25.6 | 3844 | 6992.8 +/- 34.1 | 7088 | 14929.4 +/- 50.7 | 15048 |
