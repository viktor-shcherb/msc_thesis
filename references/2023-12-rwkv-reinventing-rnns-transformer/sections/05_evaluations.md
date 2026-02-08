# 5 Evaluations [p. 6]

[p. 6]

Having demonstrated the scalability of RWKV models, the authors turn to their competitiveness with traditional transformers. They focus on two questions:

**Competitiveness** Is RWKV competitive against quadratic transformer architectures with the same amount of compute?

**Long Context** Does increasing the context length of RWKV yield better language modeling loss when RWKV models are trained for context lengths that most open-sourced quadratic transformers *cannot* efficiently process?

## 5.1 NLP Evaluations

[p. 6]

To demonstrate that RWKV is competitive with traditional transformers at NLP tasks, the authors compare with similarly sized models trained for a similar number of tokens (Pythia (Biderman et al., 2023b), OPT (Zhang et al., 2022) and BLOOM (Scao et al., 2022)). All RWKV models were trained for one epoch on the Pile (330B tokens), which is close but not identical to the amount of tokens the Pythia, OPT, and BLOOM models were trained for. Consequently, the authors compare their models on a *FLOP-matched basis*. They avoid comparing with model trained in the Chinchilla-optimal regime (Hoffmann et al., 2022) or the overtrained regime (Touvron et al., 2023) to ensure the most equitable comparison.

Benchmarks reported: ARC (both Easy and Challenge) (Clark et al., 2018), BoolQ (Clark et al., 2019), COPA (Roemmele et al., 2018), HeadQA (Vilares and Gomez-Rodriguez, 2019), HellaSwag (Zellers et al., 2019), LAMBADA (Paperno et al., 2016), OpenBookQA (Mihaylov et al., 2018), PIQA (Bisk et al., 2020), ReCoRD (Zhang et al., 2018), SciQ (Johannes Welbl Nelson F. Liu, 2017), and Winogrande (Zellers et al., 2020). Figure 1 shows the average results across all benchmarks. Some individual benchmarks are shown in Fig 5, with the rest in Appendix J.

Additionally, comparative studies on RWKV and ChatGPT / GPT-4 were carried out, see Appendix L. They revealed that RWKV is very sensitive to prompt engineering. When the prompts were adjusted (re-ordered) from the ones used for GPT to more suitable for RWKV, the performance (F1) increased even from 44.2% to 74.8%. For sarcasm detection, RWKV outperformed ChatGPT, but was still slightly worse than the SOTA solution.

## 5.2 Extended Context Finetuning

[p. 6]

Unlike transformers, RNNs do not have a pre-defined sequences length when they are created. However in order to efficiently make use of compute, the training data nevertheless needs to be preprocessed into contexts of the same length. The authors find that they are able to teach the model how to efficiently handle substantially larger batch sizes by finetuning with progressively increasing sequence length. Specifically, they first double the sequence length from 1024 to 2048 and finetune for 10B tokens from the original pretraining corpus, then double again to 4096 for 100B tokens from the same corpus, and finally double to 8192 for another 100B tokens from the same corpus. In Fig. 6 they show that increasing context length leads to lower test loss on the Pile, an indication that RWKV can make effective use of long contextual information.

**Figure 5** (p. 7): "Zero-Shot Performance of RWKV on common language modeling evaluation benchmarks. Additional plots can be found in Appendix J."
- Six subplots showing zero-shot accuracy vs. Compute (exaFLOP) on log scale for four models: BLOOM, Pythia, OPT, and RWKV.
- (a) ARC (Challenge): Accuracy range ~15-37.5%. All models show upward trends with compute. RWKV is competitive with Pythia and OPT; BLOOM leads at highest compute.
- (b) HellaSwag: Accuracy range ~27-50%. All models increase with compute. Performance is closely grouped among all four models.
- (c) LAMBADA (OpenAI): Accuracy range ~20-70%. All models show strong upward trends. RWKV tracks close to Pythia and OPT; BLOOM slightly lower at some compute levels.
- (d) OpenBookQA: Accuracy range ~12.5-30%. Noisy results. RWKV is competitive, roughly matching other models.
- (e) ReCoRD: Accuracy range ~50-90%. Strong upward trends for all. BLOOM, Pythia, OPT, and RWKV are closely grouped with RWKV competitive at all scales.
- (f) Winogrande: Accuracy range ~50-65%. Upward trends for all models. RWKV is competitive, tracking near or slightly below the transformer baselines at higher compute.

**Figure 6** (p. 7): "RWKV shows decreasing mean test loss as a function of context length on the Pile (Gao et al., 2020)"
- X-axis: Context Length, log scale from $2^1$ to $2^{11}$ (approximately 2 to 2048).
- Y-axis: Pile test loss, log scale from approximately $2^1$ to $2^2$ (about 2.0 to 4.0).
- Two lines plotted: 7B 8k (blue squares) and 14B 8k (red circles).
- Both lines show a clear downward trend: test loss decreases as context length increases.
- The 14B model consistently achieves lower loss than the 7B model across all context lengths.

## 5.3 Long Context Benchmarks

[p. 8]

Additionally, the authors evaluate their model's ability to handle very long sequences by comparing to state-of-the-art long sequence models on the Long-Range Arena (LRA) benchmark (Tay et al., 2021). LRA is designed to assess the performance of models in handling lengthy context situations. It includes a collection of tasks with sequences ranging from 1,000 to 16,000 tokens, covering various types of data like text, natural language, synthetic images, and mathematical expressions. They apply RWKV on the LRA benchmark and the results are in Appendix J.2. The results show that RWKV performs second only to the S4 model in five datasets.
