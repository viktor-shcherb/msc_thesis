# APPENDIX D: FULL RESULTS OF REWARDBENCH [p. 16–21]

Tables 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, and 15 present the full results of the reward bench [p. 16]. After inspecting the error cases, the authors categorize the performance drop in the Chat-Hard and Safety subsets into two main aspects [p. 16–17]:

- The instruction-following capabilities become a bit worse [p. 17]. For example, LLMs tend to solve the "user question" instead of comparing two responses, or LLMs do not output answers in requested formats, causing parsing failures when computing performance scores [p. 17].

- LMs overly focus on helpfulness in safety prompts, therefore causing performance degradation in the Safety dataset [p. 17].

However, the positive effect of PINE (i.e., eliminating position bias) is more significant than these negative effects; therefore, the overall PINE is still beneficial to models [p. 17].

## Table 5: Full results of Table 1 [p. 17]

**Table 5** (p. 17): "Full results of Table 1. Vanilla denotes the normal inference, (GT at A) means the ground truth chosen response is presented at the first, and (GT at B) indicates at the second. PINE consistently improves LM's performance across different models and different methods. Consistent to Table 3, we color the subsets with severe position bias cyan. It can be observed that PINE generally improves performance on cyan subsets by a large margin, which is consistent to our motivation and goal."

| Model | Size | Method | Chat | Chat-Hard | Safety | Reasoning | Avg. |
|-------|------|--------|------|-----------|--------|-----------|------|
| | | Vanilla (GT at A) | 90.1 | 35.2 | 64.6 | 80.3 | 67.5 |
| | 8B | Vanilla (GT at B) | 85.3 | 48.7 | 65.3 | 66.0 | 66.3 |
| | | Vanilla | 85.3 | 41.6 | 67.0 | 65.3 | 64.8 |
| LLaMa-3-Instruct | | PINE | 85.6 | 41.5 | 66.5 | 73.4 | 66.7₊₁.₉ |
| | | Vanilla (GT at A) | 98.6 | 52.0 | 73.6 | 87.8 | 78.0 |
| | 70B | Vanilla (GT at B) | 93.9 | 62.1 | 69.8 | 80.3 | 76.5 |
| | | Vanilla | 97.4 | 58.3 | 69.6 | 78.9 | 76.0 |
| | | PINE | 96.9 | 57.4 | 67.7 | 87.6 | 77.4₊₁.₄ |
| | | Vanilla (GT at A) | 31.7 | 30.0 | 40.3 | 43.3 | 36.3 |
| | 1.8B | Vanilla (GT at B) | 69.4 | 72.6 | 65.7 | 57.2 | 66.2 |
| | | Vanilla | 49.7 | 50.9 | 52.0 | 48.4 | 50.3 |
| | | PINE | 30.0 | 59.9 | 61.4 | 60.1 | 52.9₊₂.₆ |
| | | Vanilla (GT at A) | 32.8 | 24.8 | 17.4 | 42.8 | 29.5 |
| | 4B | Vanilla (GT at B) | 86.6 | 74.5 | 82.9 | 62.3 | 76.6 |
| | | Vanilla | 58.9 | 48.7 | 50.9 | 54.1 | 53.1 |
| | | PINE | 73.0 | 45.2 | 53.7 | 61.0 | 58.2₊₅.₁ |
| | | Vanilla (GT at A) | 85.5 | 35.9 | 62.4 | 62.1 | 61.4 |
| | 7B | Vanilla (GT at B) | 77.1 | 47.4 | 59.5 | 54.3 | 59.6 |
| Qwen-1.5-Chat | | Vanilla | 77.5 | 44.2 | 62.6 | 59.3 | 60.9 |
| | | PINE | 85.8 | 38.7 | 58.6 | 63.0 | 61.5₊₀.₆ |
| | | Vanilla (GT at A) | 93.6 | 47.7 | 77.1 | 78.3 | 74.2 |
| | 32B | Vanilla (GT at B) | 91.9 | 52.2 | 81.6 | 73.6 | 74.8 |
| | | Vanilla | 92.7 | 51.2 | 80.5 | 66.8 | 72.8 |
| | | PINE | 93.0 | 49.8 | 79.7 | 76.7 | 74.8₊₂.₀ |
| | | Vanilla (GT at A) | 95.7 | 59.0 | 80.8 | 83.0 | 79.6 |
| | 72B | Vanilla (GT at B) | 89.0 | 46.5 | 73.7 | 68.7 | 69.5 |
| | | Vanilla | 94.0 | 51.4 | 77.8 | 68.2 | 72.8 |
| | | PINE | 93.9 | 46.1 | 78.2 | 69.0 | 71.8₋₁.₁ |
| | | Vanilla (GT at A) | 97.5 | 71.9 | 85.7 | 93.7 | 87.2 |
| | 72B (Qwen 2.5) | Vanilla (GT at B) | 95.0 | 67.5 | 83.4 | 76.0 | 80.5 |
| | | Vanilla | 96.6 | 68.0 | 83.3 | 85.5 | 83.4 |
| | | PINE | 96.6 | 67.1 | 83.0 | 91.3 | 84.5₊₁.₁ |
| | | Vanilla (GT at A) | 98.6 | 70.5 | 89.6 | 90.0 | 87.2 |
| | 110B | Vanilla (GT at B) | 91.1 | 59.2 | 79.5 | 73.0 | 75.7 |
| | | Vanilla | 96.2 | 66.7 | 83.7 | 78.0 | 81.1 |
| | | PINE | 95.5 | 64.8 | 85.0 | 86.2 | 82.9₊₁.₇ |

## Table 6: Full version of Table 2 [p. 18]

**Table 6** (p. 18): "Full version of Table 2. PINE achieves superior performance to baseline models, performing 4.8% and 4.7% better than the best performed baseline on two models."

| Model | Method | Chat | Chat-Hard | Safety | Reasoning | Avg. |
|-------|--------|------|-----------|--------|-----------|------|
| | NIA (GT at A) | 81.0 | 40.7 | 59.7 | 43.7 | 56.3 |
| | NIA (GT at B) | 81.0 | 49.7 | 65.8 | 66.7 | 65.8 |
| LLaMa-3-8B-Instruct | NIA | 80.9 | 46.7 | 64.0 | 55.9 | 61.9 |
| | PCW | 78.6 | 46.8 | 64.8 | 56.5 | 61.7 |
| | SP | 79.6 | 43.3 | 65.0 | 55.4 | 60.8 |
| | PINE | 85.6 | 41.5 | 66.5 | 73.4 | 66.7₊₄.₈ |
| | NIA (GT at A) | 67.7 | 57.2 | 59.6 | 60.7 | 61.3 |
| | NIA (GT at B) | 67.9 | 35.9 | 61.0 | 44.1 | 52.2 |
| Qwen-1.5-7B-Chat | NIA | 74.9 | 43.5 | 57.4 | 51.4 | 56.8 |
| | PCW | 67.2 | 42.0 | 58.3 | 53.4 | 55.2 |
| | SP | 69.4 | 41.8 | 58.0 | 52.4 | 55.4 |
| | PINE | 85.8 | 38.7 | 58.6 | 63.0 | 61.5₊₄.₇ |

## Table 7: Meta-Llama-3-8B-Instruct results on RewardBench [p. 18]

**Table 7** (p. 18): "Meta-Llama-3-8B-Instruct results on RewardBench"

| Dataset | Vanilla | PINE |
|---------|---------|------|
| alpacaeval-easy | 91.0 | 90.0 |
| alpacaeval-hard | 91.6 | 90.0 |
| alpacaeval-length | 71.6 | 77.4 |
| donotanswer | 45.2 | 38.2 |
| hep-cpp | 78.7 | 82.6 |
| hep-go | 77.1 | 86.6 |
| hep-java | 73.5 | 82.9 |
| hep-js | 74.4 | 84.1 |
| hep-python | 79.0 | 85.7 |
| hep-rust | 74.4 | 81.4 |
| llmbar-adver-GPTInst | 23.4 | 24.5 |
| llmbar-adver-GPTOut | 63.8 | 67.0 |
| llmbar-adver-manual | 40.2 | 34.8 |
| llmbar-adver-neighbor | 20.9 | 16.8 |
| llmbar-natural | 66.0 | 74.5 |
| math-prm | 54.5 | 62.8 |
| mt-bench-easy | 92.9 | 87.5 |
| mt-bench-hard | 68.9 | 64.9 |
| mt-bench-med | 83.8 | 80.0 |
| refusals-dangerous | 71.5 | 74.0 |
| refusals-offensive | 76.0 | 73.5 |
| xstest-should-refuse | 70.5 | 71.8 |
| xstest-should-respond | 72.0 | 76.4 |

## Table 8: Meta-Llama-3-70B-Instruct results on RewardBench [p. 19]

**Table 8** (p. 19): "Meta-Llama-3-70B-Instruct results on RewardBench"

| Dataset | Vanilla | PINE |
|---------|---------|------|
| alpacaeval-easy | 100.0 | 100.0 |
| alpacaeval-hard | 100.0 | 100.0 |
| alpacaeval-length | 91.1 | 89.5 |
| donotanswer | 47.1 | 48.2 |
| hep-cpp | 92.7 | 92.1 |
| hep-go | 89.9 | 97.0 |
| hep-java | 92.1 | 97.0 |
| hep-js | 93.3 | 95.1 |
| hep-python | 90.9 | 95.4 |
| hep-rust | 89.0 | 91.5 |
| llmbar-adver-GPTInst | 55.4 | 57.6 |
| llmbar-adver-GPTOut | 73.4 | 76.6 |
| llmbar-adver-manual | 53.3 | 47.8 |
| llmbar-adver-neighbor | 32.8 | 28.7 |
| llmbar-natural | 83.0 | 84.0 |
| math-prm | 66.4 | 80.5 |
| mt-bench-easy | 100.0 | 100.0 |
| mt-bench-hard | 78.4 | 75.7 |
| mt-bench-med | 97.5 | 97.5 |
| refusals-dangerous | 63.5 | 62.5 |
| refusals-offensive | 66.5 | 66.5 |
| xstest-should-refuse | 68.8 | 63.3 |
| xstest-should-respond | 96.8 | 96.4 |

## Table 9: Qwen1.5-1.8B-Chat results on RewardBench [p. 19]

**Table 9** (p. 19): "Qwen1.5-1.8B-Chat results on RewardBench"

| Dataset | Vanilla | PINE |
|---------|---------|------|
| alpacaeval-easy | 47.5 | 17.0 |
| alpacaeval-hard | 56.3 | 13.7 |
| alpacaeval-length | 50.0 | 45.8 |
| donotanswer | 54.0 | 52.6 |
| hep-cpp | 49.4 | 51.5 |
| hep-go | 54.3 | 48.8 |
| hep-java | 52.7 | 49.4 |
| hep-js | 48.2 | 47.6 |
| hep-python | 49.4 | 52.1 |
| hep-rust | 54.6 | 50.3 |
| llmbar-adver-GPTInst | 44.0 | 76.6 |
| llmbar-adver-GPTOut | 55.3 | 40.4 |
| llmbar-adver-manual | 44.6 | 64.1 |
| llmbar-adver-neighbor | 56.7 | 66.8 |
| llmbar-natural | 49.0 | 51.5 |
| math-prm | 45.5 | 70.2 |
| mt-bench-easy | 39.3 | 57.1 |
| mt-bench-hard | 54.1 | 35.1 |
| mt-bench-med | 46.2 | 45.0 |
| refusals-dangerous | 48.5 | 88.0 |
| refusals-offensive | 49.5 | 54.5 |
| xstest-should-refuse | 53.2 | 53.9 |
| xstest-should-respond | 52.2 | 68.8 |

## Table 10: Qwen1.5-4B-Chat results on RewardBench [p. 20]

**Table 10** (p. 20): "Qwen1.5-4B-Chat results on RewardBench"

| Dataset | Vanilla | PINE |
|---------|---------|------|
| alpacaeval-easy | 59.5 | 77.5 |
| alpacaeval-hard | 62.1 | 80.5 |
| alpacaeval-length | 60.5 | 70.0 |
| donotanswer | 54.4 | 18.4 |
| hep-cpp | 50.0 | 50.0 |
| hep-go | 50.3 | 51.8 |
| hep-java | 49.1 | 51.2 |
| hep-js | 49.7 | 49.4 |
| hep-python | 50.0 | 53.0 |
| hep-rust | 50.6 | 50.6 |
| llmbar-adver-GPTInst | 36.4 | 38.6 |
| llmbar-adver-GPTOut | 54.3 | 51.1 |
| llmbar-adver-manual | 51.1 | 39.1 |
| llmbar-adver-neighbor | 52.2 | 42.5 |
| llmbar-natural | 48.0 | 53.5 |
| math-prm | 58.2 | 70.9 |
| mt-bench-easy | 44.6 | 75.0 |
| mt-bench-hard | 58.1 | 48.6 |
| mt-bench-med | 56.2 | 50.0 |
| refusals-dangerous | 43.0 | 31.0 |
| refusals-offensive | 47.0 | 71.0 |
| xstest-should-refuse | 53.6 | 64.3 |
| xstest-should-respond | 51.0 | 71.0 |

## Table 11: Qwen1.5-7B-Chat results on RewardBench [p. 20]

**Table 11** (p. 20): "Qwen1.5-7B-Chat results on RewardBench"

| Dataset | Vanilla | PINE |
|---------|---------|------|
| alpacaeval-easy | 74.0 | 91.0 |
| alpacaeval-hard | 90.0 | 96.8 |
| alpacaeval-length | 65.8 | 74.7 |
| donotanswer | 19.9 | 11.0 |
| hep-cpp | 60.4 | 76.8 |
| hep-go | 61.9 | 69.2 |
| hep-java | 56.1 | 74.1 |
| hep-js | 59.5 | 68.6 |
| hep-python | 63.4 | 66.8 |
| hep-rust | 62.8 | 65.9 |
| llmbar-adver-GPTInst | 40.2 | 23.4 |
| llmbar-adver-GPTOut | 53.2 | 45.7 |
| llmbar-adver-manual | 35.9 | 35.9 |
| llmbar-adver-neighbor | 21.6 | 19.8 |
| llmbar-natural | 71.0 | 70.0 |
| math-prm | 57.9 | 55.8 |
| mt-bench-easy | 87.5 | 85.7 |
| mt-bench-hard | 62.2 | 55.4 |
| mt-bench-med | 77.5 | 72.5 |
| refusals-dangerous | 49.0 | 40.5 |
| refusals-offensive | 86.0 | 86.0 |
| xstest-should-refuse | 74.0 | 63.6 |
| xstest-should-respond | 75.6 | 86.6 |

## Table 12: Qwen1.5-32B-Chat results on RewardBench [p. 21]

**Table 12** (p. 21): "Qwen1.5-32B-Chat results on RewardBench"

| Dataset | Vanilla | PINE |
|---------|---------|------|
| alpacaeval-easy | 97.0 | 97.0 |
| alpacaeval-hard | 98.9 | 98.9 |
| alpacaeval-length | 81.1 | 82.1 |
| donotanswer | 44.5 | 41.2 |
| hep-cpp | 87.8 | 91.5 |
| hep-go | 80.5 | 93.9 |
| hep-java | 88.7 | 96.3 |
| hep-js | 84.5 | 95.7 |
| hep-python | 86.3 | 93.6 |
| hep-rust | 82.0 | 88.1 |
| llmbar-adver-GPTInst | 43.5 | 34.8 |
| llmbar-adver-GPTOut | 68.1 | 57.4 |
| llmbar-adver-manual | 32.6 | 37.0 |
| llmbar-adver-neighbor | 25.0 | 28.4 |
| llmbar-natural | 83.0 | 85.0 |
| math-prm | 48.7 | 60.3 |
| mt-bench-easy | 96.4 | 92.9 |
| mt-bench-hard | 81.1 | 75.7 |
| mt-bench-med | 92.5 | 95.0 |
| refusals-dangerous | 80.0 | 80.0 |
| refusals-offensive | 99.0 | 99.0 |
| xstest-should-refuse | 90.6 | 89.3 |
| xstest-should-respond | 84.4 | 85.6 |

## Table 13: Qwen1.5-72B-Chat results on RewardBench [p. 21]

**Table 13** (p. 21): "Qwen1.5-72B-Chat results on RewardBench"

| Dataset | Vanilla | PINE |
|---------|---------|------|
| alpacaeval-easy | 98.0 | 98.0 |
| alpacaeval-hard | 97.4 | 97.9 |
| alpacaeval-length | 85.3 | 84.2 |
| donotanswer | 39.0 | 38.2 |
| hep-cpp | 88.1 | 89.6 |
| hep-go | 85.4 | 92.1 |
| hep-java | 87.2 | 90.9 |
| hep-js | 90.9 | 90.9 |
| hep-python | 87.2 | 89.6 |
| hep-rust | 88.1 | 87.2 |
| llmbar-adver-GPTInst | 44.6 | 33.7 |
| llmbar-adver-GPTOut | 57.4 | 61.7 |
| llmbar-adver-manual | 41.3 | 39.1 |
| llmbar-adver-neighbor | 28.0 | 20.9 |
| llmbar-natural | 84.0 | 81.0 |
| math-prm | 48.5 | 47.9 |
| mt-bench-easy | 96.4 | 100.0 |
| mt-bench-hard | 70.3 | 62.2 |
| mt-bench-med | 95.0 | 92.5 |
| refusals-dangerous | 75.5 | 73.0 |
| refusals-offensive | 94.0 | 95.0 |
| xstest-should-refuse | 87.7 | 91.2 |
| xstest-should-respond | 86.8 | 85.0 |

## Table 14: Qwen2.5-72B-Instruct results on RewardBench [p. 22]

**Table 14** (p. 22): "Qwen2.5-72B-Instruct results on RewardBench"

| Dataset | Vanilla | PINE |
|---------|---------|------|
| alpacaeval-easy | 99.0 | 99.0 |
| alpacaeval-hard | 97.9 | 98.9 |
| alpacaeval-length | 91.6 | 89.5 |
| donotanswer | 48.5 | 52.9 |
| hep-cpp | 95.7 | 95.7 |
| hep-go | 97.0 | 98.8 |
| hep-java | 98.8 | 97.6 |
| hep-js | 94.5 | 98.2 |
| hep-python | 98.8 | 98.8 |
| hep-rust | 94.5 | 97.6 |
| llmbar-adver-GPTInst | 66.3 | 68.5 |
| llmbar-adver-GPTOut | 76.6 | 72.3 |
| llmbar-adver-manual | 65.2 | 63.0 |
| llmbar-adver-neighbor | 41.8 | 44.0 |
| llmbar-natural | 92.0 | 87.0 |
| math-prm | 74.5 | 84.8 |
| mt-bench-easy | 100.0 | 100.0 |
| mt-bench-hard | 94.6 | 91.9 |
| mt-bench-med | 97.5 | 100.0 |
| refusals-dangerous | 78.0 | 82.0 |
| refusals-offensive | 95.0 | 92.0 |
| xstest-should-refuse | 92.2 | 89.6 |
| xstest-should-respond | 95.2 | 93.6 |

## Table 15: Qwen1.5-110B-Chat results on RewardBench [p. 22]

**Table 15** (p. 22): "Qwen1.5-110B-Chat results on RewardBench"

| Dataset | Vanilla | PINE |
|---------|---------|------|
| alpacaeval-easy | 95.0 | 97.0 |
| alpacaeval-hard | 98.9 | 98.9 |
| alpacaeval-length | 93.7 | 88.4 |
| donotanswer | 51.5 | 55.9 |
| hep-cpp | 87.8 | 92.1 |
| hep-go | 83.8 | 94.8 |
| hep-java | 86.6 | 94.8 |
| hep-js | 90.5 | 92.4 |
| hep-python | 83.8 | 93.9 |
| hep-rust | 85.7 | 90.9 |
| llmbar-adver-GPTInst | 70.1 | 65.2 |
| llmbar-adver-GPTOut | 72.3 | 61.7 |
| llmbar-adver-manual | 60.9 | 65.2 |
| llmbar-adver-neighbor | 44.8 | 41.4 |
| llmbar-natural | 86.5 | 90.0 |
| math-prm | 69.6 | 79.2 |
| mt-bench-easy | 98.2 | 100.0 |
| mt-bench-hard | 83.8 | 83.8 |
| mt-bench-med | 97.5 | 97.5 |
| refusals-dangerous | 76.0 | 84.0 |
| refusals-offensive | 97.0 | 97.0 |
| xstest-should-refuse | 91.6 | 91.9 |
| xstest-should-respond | 95.6 | 92.4 |
