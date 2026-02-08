# Experiments [p. 6-8]

[p. 6] The authors conduct experiments to evaluate the ability of mainstream models to handle the various long text challenges presented by SCROLLS. The code is based on the Transformers library (Wolf et al., 2020), and is available online.

## 5.1 Baselines

Two pretrained transformer variants are finetuned as baselines, as well as naive heuristic baselines to establish the floor performance on each task. Hyperparameters are detailed in Appendix D.

### BART

[p. 6] As a standard transformer baseline, the pretrained BART-base model (Lewis et al., 2020) is used. BART is a transformer encoder-decoder pretrained by reconstructing noised texts, which achieved state-of-the-art results on several summarization datasets when released. BART was pretrained on sequences of up to 1,024 tokens; therefore all inputs are truncated by retaining only their 1,024-token prefix. To examine the effect of available input length, truncating BART's inputs at 256 and 512 tokens is also considered.

### Longformer Encoder-Decoder (LED)

[p. 6-7] LED-base is used, the encoder-decoder version of the efficient transformer architecture Longformer (Beltagy et al., 2020). Longformer avoids computing quadratic-complexity attention via sliding-window attention, where each word only attends to a constant number of nearby tokens, in addition to a few tokens that compute global attention over the entire input. LED is initialized with BART's parameters, without further pretraining. In the experiments, a sliding window of 1,024 is used, and the total input length is restricted to 16,384 tokens via truncation, following Beltagy et al. Experiments with maximum sequence lengths of 1,024 and 4,096 tokens are also conducted. While the original work on LED selects the globally-attending tokens on a per-task basis, the authors follow their summarization setting throughout all tasks, which enables global attention only for the first token.

### Heuristic Baselines

[p. 7] Simple heuristics are used to find the lower bound of performance on each dataset. For most datasets, the fixed-length prefix heuristic is used, akin to the LEAD baseline in the summarization literature. Specifically, the average output-input length ratio *rho* is computed over the training set (in characters), and then the first *rho* * *n* characters from the given input are produced at inference time (where *n* is the input's length). For QuALITY, the majority class is used (which is just above one quarter). For ContractNLI, the per-hypothesis majority class is used, as the same 17 hypotheses are shared across all documents.

## 5.2 Results

[p. 7-8] Table 2 shows the baselines' performance on SCROLLS.

**Table 2** (p. 8): "Baseline results on SCROLLS, using naive heuristics, BART, and Longformer Encoder-Decoder (LED), and various input length limits. The final SCROLLS score (Avg) is computed by averaging over each dataset's overall performance score. For QuALITY (QALT), we use the EM score calculated over the full test set (EM-T), without up-weighting the performance on the hard subset (EM-H). For datasets evaluated with ROUGE, we aggregate the different ROUGE scores via geometric mean to produce a single score per dataset, which is then used when calculating the final average SCROLLS score."

| Model | Input | GovRep ROUGE-1/2/L | SumScr ROUGE-1/2/L | QMSum ROUGE-1/2/L | Qspr F1 | Nrtv F1 | QALT EM-T/H | CNLI EM | Avg |
|---|---|---|---|---|---|---|---|---|---|
| Naive | - | 45.3 / 17.9 / 20.8 | 19.6 / 1.8 / 11.0 | 14.2 / 2.0 / 9.3 | 3.4 | 1.5 | 25.2 / 26.1 | 66.0 | *19.35* |
| BART | 256 | 41.9 / 14.2 / 20.3 | 24.5 / 3.8 / 15.3 | 29.9 / 8.3 / 20.4 | 23.3 | 14.0 | 26.0 / 25.8 | 69.8 | *26.35* |
| BART | 512 | 45.6 / 16.9 / 21.8 | 26.3 / **5.1** / 16.2 | 29.5 / 8.2 / 20.1 | 24.7 | 14.5 | **26.8** / **27.4** | 71.6 | *27.58* |
| BART | 1024 | 47.9 / 18.6 / 22.7 | **27.2** / 4.9 / **16.7** | **30.2** / **8.7** / **20.7** | 26.3 | 15.4 | 26.0 / 25.9 | **77.4** | ***29.01*** |
| LED | 1024 | 40.9 / 16.1 / 23.1 | 22.7 / 3.6 / 15.1 | 24.6 / 6.5 / 19.0 | 24.4 | 15.2 | 26.6 / 27.2 | 73.4 | *27.06* |
| LED | 4096 | 52.5 / 23.3 / 26.8 | 23.0 / 4.1 / 15.1 | 26.6 / 6.9 / 19.9 | 25.0 | 16.3 | 26.6 / 27.3 | 71.5 | *28.30* |
| LED | 16384 | **56.2** / **26.6** / **28.8** | 24.2 / 4.5 / 15.4 | 25.1 / 6.7 / 18.8 | **26.6** | **18.5** | 25.8 / 25.4 | 71.5 | ***29.16*** |

Bold values indicate best performance in each column. Italic averages indicate overall SCROLLS scores.

### More Context Improves Performance

[p. 7] Experiments with three context lengths for each model show that as the model receives more context, its average SCROLLS score increases. For BART, increasing the input length from 256 tokens to 1,024 increases performance by 2.66 points, while LED grows by 2.1 points when enlarging its maximal sequence length from 1,024 tokens to 16,384. This trend is relatively consistent across datasets for BART, but less so for LED (e.g., QMSum and ContractNLI).

### BART versus LED

[p. 7-8] Although LED does achieve the highest SCROLLS score when given 16,384 tokens per sequence, BART arrives within 0.15 points of the top score *despite being limited to only 1,024 tokens*. This is surprising, given the substantial difference in input lengths. Moreover, when controlling for the number of input tokens, BART outperforms LED by almost two points, suggesting that LED might be under-optimized. Inspecting the dataset-level results reveals that LED (16k) significantly outperforms BART (1k) in two datasets, GovReport and NarrativeQA, which are coincidentally the largest datasets in SCROLLS by number of examples. Thus, it is possible that since LED is initialized with BART's parameters (without long-text pretraining), it requires a substantial amount of data and fine-tuning to adapt its parameters to sliding window attention and potentially longer inputs.

Overall, the experiments highlight the importance of measuring not only whether an architecture can efficiently process long sequences, but also whether it can effectively model their semantics -- precisely what SCROLLS is designed to do.

### How Far is SCROLLS from being Solved?

[p. 8] The heuristic baselines set a lower bound average score of 19.35, which the model baselines are able to improve upon by 7 to 10 points. While it is difficult to establish an accurate human performance ceiling on SCROLLS, especially when considering the summarization datasets, there are some indicators that it is probably much higher than the current baselines. Dasigi et al. (2021) study a subset of Qasper that has multiple annotated answers, and find their overlap to be 60.9% F1, more than double the best baseline. Likewise, human agreement on QuALITY was measured at 93.5% EM (Pang et al., 2021). The inter-annotator agreement (F1) on NarrativeQA's test set (where each question has two answers) is computed, arriving at around 58.7% F1, compared to the best baseline of 18.5% F1. Overall, it seems that contemporary off-the-shelf models struggle with these tasks, challenging future work to make progress on SCROLLS.
