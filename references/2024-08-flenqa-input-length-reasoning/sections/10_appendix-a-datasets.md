# A Datasets [p. 11]

[p. 11] Each task of the following contains 100 base instances. In each sample, there are two paragraph-length texts (*key paragraphs*). To achieve paragraphs of similar length, they edit them by truncating sentences beyond a specific length, resulting in an average paragraph length of 125 tokens.

## A.1 Ruletaker [p. 11]

The key paragraphs in the task are as evidence for the reasoning task, a rule and a question. In the original data (Clark et al., 2021), the samples contain different number of reasoning steps. In this study, they generate new, simpler samples of the task: each sample is composed of only two facts and one logical rule. The samples they generate are of similar flavor to those that exist in the original Ruletaker data, but are generated with new statements, rules and facts. The key paragraphs and the padding appear as the facts of each sample.

**Figure 10** (p. 11): "Summary of statistics of the ruletaker* task data."

| Padding Type | Target Input Length | Mean Number Tokens |
|---|---|---|
| Books | 250 | 249.8 |
| Books | 500 | 508.78 |
| Books | 1000 | 1009.56 |
| Books | 2000 | 2009.64 |
| Books | 3000 | 3008.38 |
| Same | 250 | 249.8 |
| Same | 500 | 503.535 |
| Same | 1000 | 1004.41 |
| Same | 2000 | 2005.51 |
| Same | 3000 | 3005.125 |

## A.2 MonoRel [p. 11-12]

The key paragraphs in the task act as evidence for the reasoning task, and a question. Both key paragraphs describe a monotonic relation between two people, where one person is shared between both. The key paragraphs are embedded in padding text to create a text mixture.

**Figure 11** (p. 12): "Summary of statistics of the MonoRel task data."

| Padding Type | Target Input Length | Mean Number Tokens |
|---|---|---|
| Books | 250 | 238.06 |
| Books | 500 | 490.84 |
| Books | 1000 | 991.41 |
| Books | 2000 | 1990.34 |
| Books | 3000 | 2990.95 |
| Same | 250 | 238.06 |
| Same | 500 | 491.69 |
| Same | 1000 | 991.43 |
| Same | 2000 | 1991.31 |
| Same | 3000 | 2991.44 |

## A.3 People in Rooms (PIR) [p. 12]

One key paragraph describes the location of an individual, and the other describes some attribute of that location. The key paragraphs are embedded in padding text to create a text mixture.

**Figure 12** (p. 12): "Summary of statistics of the People In Rooms (PIR) task data."

| Padding Type | Target Input Length | Mean Number Tokens |
|---|---|---|
| Books | 250 | 305.36 |
| Books | 500 | 491.85 |
| Books | 1000 | 989.91 |
| Books | 2000 | 1992.00 |
| Books | 3000 | 2988.67 |
| Same | 250 | 305.36 |
| Same | 500 | 484.63 |
| Same | 1000 | 985.82 |
| Same | 2000 | 1985.04 |
| Same | 3000 | 2984.80 |
