# APPENDIX C: STATISTICS OF POSITION BIAS IN REWARDBENCH [p. 16]

The authors show the statistics of position bias in RewardBench in Table 4 [p. 16].

**Table 4** (p. 16): "The portion of data (%) that models have position bias in RewardBench, i.e., models change answers after swapping candidate responses orders. We color the subsets that have more than 25% data causing position bias with cyan."

| Model | Size | Chat | Chat-Hard | Safety | Reasoning | Avg. |
|-------|------|------|-----------|--------|-----------|------|
| LLaMA-3-Instruct | 8B | 10.3 | 21.5 | 11.4 | 27.6 | 17.7 |
| LLaMA-3-Instruct | 70B | 3.6 | 16.0 | 5.8 | 15.2 | 10.2 |
| Qwen-1.5-Chat | 1.8B | 33.5 | 37.3 | 24.7 | 13.3 | 27.4 |
| Qwen-1.5-Chat | 4B | 48.0 | 38.6 | 57.1 | 12.7 | 39.2 |
| Qwen-1.5-Chat | 7B | 17.0 | 20.6 | 10.9 | 26.5 | 18.8 |
| Qwen-1.5-Chat | 32B | 7.8 | 20.0 | 9.6 | 26.4 | 16.0 |
| Qwen-1.5-Chat | 72B | 10.9 | 22.6 | 9.6 | 24.7 | 17.0 |
| Qwen-1.5-Chat | 110B | 8.7 | 16.0 | 11.5 | 23.5 | 14.9 |

Note: Values highlighted in cyan in the original table (indicating >25% position bias) are: Qwen-1.5-Chat 1.8B (33.5% Chat, 37.3% Chat-Hard, 27.4% Avg.), Qwen-1.5-Chat 4B (48.0% Chat, 38.6% Chat-Hard, 57.1% Safety, 39.2% Avg.), LLaMA-3-Instruct 8B (27.6% Reasoning), Qwen-1.5-Chat 7B (26.5% Reasoning), Qwen-1.5-Chat 32B (26.4% Reasoning) [p. 16].
