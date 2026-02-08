# Language Modeling Experiments (continued) [p. 11–14]

## 8.2 Associative Recall (continued)

[p. 11–12] using identical criteria with various model dimensions and sequence lengths. Our findings reveal significant improvements in MQAR with Eagle and Finch. Notably, Finch achieves extremely high accuracy in MQAR in our tests, and outperforms all well-known non-transformer architectures previously used to train large language models. Our experiments reveal performance disparities between Mamba (Gu & Dao, 2023) and Finch, despite their shared architectural features such as matrix-valued state and data-dependent memory modification, suggesting different combinations of these elements result in superior performance.

### Figure 4: MQAR Tasks [p. 12]

**Figure 4:** MQAR tasks. An increase in sequence length correlates with increased task difficulty.

The figure shows four subplots displaying accuracy vs model dimension for different sequence lengths (64, 128, 256, 512). Each subplot plots the performance of:
- Dove (RWKV-4) - green line with squares
- Eagle (RWKV-5) - blue line with circles
- Finch (RWKV-6) - red line with triangles
- Hyena - orange line
- Mamba - purple line
- Based - gray line

The plots show that accuracy generally increases with model dimension. For shorter sequences (64, 128), most models achieve high accuracy (~1.00). For longer sequences (256, 512), performance varies more dramatically, with Finch and Eagle maintaining higher accuracy at larger model dimensions, while some other models struggle, particularly at sequence length 512.

## 8.3 Long Context Experiments

[p. 12] We test loss versus sequence position on the PG19 (Rae et al., 2019) test set of books from token 2048 onward across RWKV-4, Eagle, and Finch. We find that Eagle improves dramatically over RWKV-4 on this long sequence task, despite having been trained solely on sequence length 4096. Finch further improves on this test beyond Eagle, with loss continuing to drop further into the sequence. See Figure 5 for details.

### Figure 5: Long Context Loss [p. 13]

**Figure 5:** Loss along sequence offset for 3B RWKV-4 World, Eagle and Finch on PG19 dataset. All models were pretrained with context length 4096.

The figure shows loss on y-axis (ranging from ~2.2 to 3.7) versus position from start on x-axis (logarithmic scale from 10^2 to beyond 10^4). Three lines are plotted:
- PG19 RWKV-4 3B (blue line)
- PG19 Eagle 3B (green line)
- PG19 Finch 3B (red line)

All three models maintain relatively stable loss around 2.4-2.6 up to position ~10^4. After that point, RWKV-4 shows dramatic loss increase reaching ~3.6, while Eagle and Finch remain much more stable, with Finch showing the best (lowest) loss staying around 2.2-2.3.

## 8.4 Bamboo Benchmark

[p. 12] The Bamboo benchmark (Dong et al., 2023) evaluates the overall long-context language modeling capability of LLMs from five aspects: question answering, hallucination detection, text sorting, language modeling, and code completion, comprising a total of ten evaluation tasks. We test models on the 4k version of the benchmark, which includes all ten tasks with a maximum context window length of 4k. We choose not to report results on the code completion since all tested models failed to generate correct code completions for this task. In Table 5, we present the results of nine tasks, with either accuracy or F1 score, alongside their average scores. With the 1.5b and 3b scales, the latest Finch and Eagle models outperform the vanilla Mamba by at least a 7% average score, while remaining comparable with the Mamba trained on Hermes data (i.e., only a 0.7% drop in the average score). Note that, despite being trained on only 1.1T tokens, Eagle-7b consistently outperforms Pythia by an average of 13.5% at the 7b scale, and it also surpasses LLaMA2-Chat-7b on several tasks in the Bamboo benchmark. These results demonstrate the superior capacity of the proposed Finch and Eagle models on a vast range of long-context tasks.

### Table 5: Bamboo Benchmark Results [p. 13]

| Model | meetingqa Acc.↑ | paperqa Acc.↑ | meetingpred Acc.↑ | showspred Acc.↑ | reportsumsort Acc.↑ | showssort Acc.↑ | senhallu F1↑ | abshallu F1↑ | altqa Acc.↑ | Avg.↓ |
|-------|-----------------|---------------|-------------------|-----------------|---------------------|-----------------|--------------|--------------|-------------|-------|
| Pythia-1.4b | 15.0% | 4.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 2.1% |
| Mamba-1.4b | 15.0% | 2.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 2.0% | 0.0% | 2.1% |
| Eagle-1.5b | 21.0% | 19.0% | 1.0% | 0.0% | 0.0% | 0.0% | 13.2% | 23.5% | 5.5% | 9.2% |
| Finch-1.6b | 19.0% | 22.0% | 1.0% | 8.0% | 0.0% | 0.0% | 10.7% | 17.3% | 2.5% | 8.9% |
| Pythia-2.8b | 16.0% | 4.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 2.2% |
| Mamba-2.8b | 11.0% | 4.0% | 0.0% | 3.0% | 0.0% | 0.0% | 0.0% | 3.9% | 0.0% | 2.4% |
| Mamba-2.8b-Hermes | 27.0% | 25.0% | 0.0% | 9.0% | 0.0% | 0.0% | 19.7% | 26.4% | 0.0 | 11.9% |
| Eagle-3b | 16.0% | 14.0% | 0.0% | 4.0% | 0.0% | 0.0% | 25.0% | 29.2% | 1.0% | 9.9% |
| Finch-3b | 20.0% | 26.0% | 4.0% | 7.0% | 0.0% | 0.0% | 14.4% | 23.6% | 6.5% | 11.3% |
| Pythia-6.9b | 19.0% | 7.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 3.3% |
| Eagle-7b-Hermes | 31.0% | 23.0% | 0.0% | 0.0% | 0.0% | 0.0% | 50.3% | 46.9% | 0.0% | 16.8% |
| LLaMA2-Chat-7b | 6.0% | 17.0% | 4.0% | 12.0% | 0.0% | 0.0% | 64.7% | 63.4% | 46.0% | 24.1% |
| Mistral-Instruct-7b | 65.0% | 73.0% | 17.0% | 32.0% | 0.0% | 0.0% | 80.5% | 72.8% | 13.5% | 39.3% |

Caption: Results on the long context reasoning benchmark: Bamboo. We compare both transformer and linear attention language models on three different scales: 1.5b, 3b, and 7b.

## 8.3 Long Context Experiments (continued)

[p. 12] (See Figure 5 description above)

## 8.4 Bamboo Benchmark (continued)

[p. 12–13] (See Table 5 and discussion above)
