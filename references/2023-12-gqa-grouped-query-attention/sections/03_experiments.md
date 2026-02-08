# 3 Experiments [p. 2-4]

## 3.1 Experimental setup [p. 2-3]

### Configurations [p. 2]

All models are based on the T5.1.1 architecture (Raffel et al., 2020), implemented with JAX (Bradbury et al., 2018), Flax (Heek et al., 2020), and Flaxformer (https://github.com/google/flaxformer). For main experiments, T5 Large and XXL with multi-head attention are considered, as well as uptrained versions of T5 XXL with multi-query and grouped-query attention. Adafactor optimizer with the same hyperparameters and learning rate schedule as T5 (Raffel et al., 2020) is used. MQA and GQA are applied to decoder self-attention and cross-attention, but not encoder self-attention. [p. 2]

### Uptraining [p. 2]

Uptrained models are initialized from public T5.1.1 checkpoints. The key and value heads are mean-pooled to the appropriate MQA or GQA structure, and then pre-trained for a further alpha proportion of original pre-training steps with the original pre-training setup and dataset from Raffel et al. (2020). For alpha = 0.05, training took approximately 600 TPUv3 chip-days. [p. 2]

### Data [p. 2-3]

Evaluation on summarization datasets: [p. 2-3]
- CNN/Daily Mail (Nallapati et al., 2016)
- arXiv and PubMed (Cohan et al., 2018)
- MediaSum (Zhu et al., 2021)
- Multi-News (Fabbri et al., 2019)

Translation dataset: WMT 2014 English-to-German [p. 3]

Question answering dataset: TriviaQA (Joshi et al., 2017) [p. 3]

The authors do not evaluate on popular classification benchmarks such as GLUE (Wang et al., 2019) as autoregressive inference is less applicable for those tasks. [p. 3]

### Fine-tuning [p. 3]

- Constant learning rate of 0.001, batch size 128, dropout rate 0.1 for all tasks [p. 3]
- CNN/Daily Mail and WMT: input length 512, output length 256 [p. 3]
- Other summarization datasets: input length 2048, output length 512 [p. 3]
- TriviaQA: input length 2048, output length 32 [p. 3]
- Train until convergence and select checkpoint with highest dev performance [p. 3]
- Greedy decoding for inference [p. 3]

### Timing [p. 3]

Time per sample reported per TPUv4 chip, as measured by xprof (Google, 2020). For timing experiments, 8 TPUs are used with the largest batch size that fits up to 32 per TPU, and parallelization optimized separately for each model. [p. 3]

## 3.2 Main results [p. 3]

Figure 3 shows average performance over all datasets as a function of average inference time for MHA T5-Large and T5-XXL, and uptrained MQA and GQA-8 XXL models with uptraining proportion alpha = 0.05. [p. 3]

Key findings: [p. 3]
- A larger uptrained MQA model provides a favorable tradeoff relative to MHA models, with higher quality and faster inference than MHA-Large.
- GQA achieves significant additional quality gains, achieving performance close to MHA-XXL with speed close to MQA.
- Table 1 contains full results for all datasets.

**Table 1** (p. 3): Inference time and average dev set performance comparison of T5 Large and XXL models with multi-head attention, and 5% uptrained T5-XXL models with multi-query and grouped-query attention on summarization datasets CNN/Daily Mail, arXiv, PubMed, MediaSum, and MultiNews, translation dataset WMT, and question-answering dataset TriviaQA.

| Model | T_infer (s) | Average | CNN (R1) | arXiv (R1) | PubMed (R1) | MediaSum (R1) | MultiNews (R1) | WMT (BLEU) | TriviaQA (F1) |
|---|---|---|---|---|---|---|---|---|---|
| MHA-Large | 0.37 | 46.0 | 42.9 | 44.6 | 46.2 | 35.5 | 46.6 | 27.7 | 78.2 |
| MHA-XXL | 1.51 | 47.2 | 43.8 | 45.6 | 47.5 | 36.4 | 46.9 | 28.4 | 81.9 |
| MQA-XXL | 0.24 | 46.6 | 43.0 | 45.0 | 46.9 | 36.1 | 46.5 | 28.5 | 81.3 |
| GQA-8-XXL | 0.28 | 47.1 | 43.5 | 45.4 | 47.7 | 36.3 | 47.2 | 28.4 | 81.6 |

**Figure 3** (p. 3): "Uptrained MQA yields a favorable tradeoff compared to MHA with higher quality and faster speed than MHA-Large, and GQA achieves even better performance with similar speed gains and comparable quality to MHA-XXL." Average performance on all tasks as a function of average inference time per sample for T5-Large and T5-XXL with multi-head attention, and 5% uptrained T5-XXL with MQA and GQA-8 attention.
- X-axis: Time per sample (ms), from 0 to ~1.5
- Y-axis: Performance, from ~46 to ~47
- MHA-Large: ~46.0 performance at ~0.37 ms (bottom-left region)
- MQA-XXL: ~46.5 performance at ~0.24 ms
- GQA-XXL: ~47.0 performance at ~0.28 ms (top-left region)
- MHA-XXL: ~47.2 performance at ~1.51 ms (top-right region)

## 3.3 Ablations [p. 3-4]

This section presents experiments to investigate the effect of different modeling choices. Evaluation on a representative subsample of tasks: CNN/Daily Mail (short-form summarization), MultiNews (long-form summarization), and TriviaQA (question-answering). [p. 3]

### Checkpoint conversion [p. 3-4]

**Figure 4** (p. 4): "Performance comparison of different checkpoint conversion methods for T5-Large uptrained to MQA with proportion alpha = 0.05. 'Mean' mean-pools key and value heads, 'First' selects the first head and 'Random' initializes heads from scratch."
- Horizontal bar chart showing performance for three conversion methods
- Mean: ~55.6
- First: ~55.1
- Random: ~54.6
- Mean pooling appears to work best, followed by selecting a single head and then random initialization. Results are ordered by the degree to which information is preserved from the pre-trained model. [p. 3-4]

### Uptraining steps [p. 4]

**Figure 5** (p. 4): "Performance as a function of uptraining proportion for T5 XXL models with MQA and GQA-8."
- X-axis: Uptraining proportion alpha, from 0 to 0.1
- Y-axis: Performance, from ~54 to ~57
- MHA shown as dotted horizontal line at ~57 (baseline)
- GQA already achieves reasonable performance after conversion (alpha = 0) while MQA requires uptraining to be useful
- Both MQA and GQA gain from 5% uptraining with diminishing returns from 10% [p. 4]

### Number of groups [p. 4]

**Figure 6** (p. 4): "Time per sample for GQA-XXL as a function of the number of GQA groups with input length 2048 and output length 512. Going from 1 (MQA) to 8 groups adds modest inference overhead, with increasing cost to adding more groups."
- X-axis: GQA groups (1, 4, 8, 16, 32, 64), logarithmic scale
- Y-axis: Time per sample (s), from 0 to ~2
- MHA shown as dotted horizontal line at ~2s
- MQA (1 group) at the fastest end
- GQA shows modest slowdown from 1 to 8 groups initially
- Sharper increase in time as groups increase beyond 8 toward MHA [p. 4]

For larger models the memory bandwidth overhead from the KV cache is less constraining (Shazeer, 2019), while the reduction in key-value size is sharper due to the increased number of heads. As a result, increasing the number of groups from MQA only results in modest slowdowns initially, with increasing cost as we move closer to MHA. 8 groups was selected as a favorable middle ground. [p. 4]
