# Appendix C: Details on RMT, ARMT, and Mamba fine-tuning and evaluation on BABILong [p. 17-18]

## GPT-2 based RMT and ARMT models [p. 17]

We used the GPT-2 (Radford et al., 2019) (137M) model (https://huggingface.co/GPT-2) as the backbone for RMT and ARMT. The sequence length was fixed at 512 tokens, and the model was augmented with 16 memory tokens for RMT and 10 memory tokens for ARMT. Finetuning was conducted on BABILong using a curriculum approach with progressively increasing sequence lengths: 1, 2, 4, 6, 8, 16 and 32 segments. ARMT used 2-3-5-8-16-32. For each curriculum step n we chose the number of segments randomly from 1 to n within a certain context size. We maintained a fixed batch size of 64 and the AdamW (Loshchilov & Hutter, 2019) optimizer with learning rate in range (5e-05, 3e-05), on linear schedule with 1000 warmup steps. In ARMT experiments, the learning rate was set to 1e-04. We also consider the memory-dimension parameter for ARMT to be 64 and we use non-linearity DPP-3 (Schlag et al., 2021). Each curriculum stage had a maximum of 10,000 steps with early stopping if metrics stop increasing. The weight decay value was set to 0.01, and no gradient stopping was used. Training was performed on 1-4 Nvidia A100 or H100 GPUs with the duration of each curriculum stage ranging from 40 minutes to 20 hours. [p. 17]

**Figure 5** (p. 18): "RMT performance on five BABILong tasks varies between training seeds. The plot represents average performance and standard deviation across three training runs."

Description: Line plot showing accuracy vs context size (1k to 10M tokens)
- Key elements: 5 colored lines with shaded regions representing different BABILong tasks (qa1-single-supporting-fact, qa2-two-supporting-facts, qa3-three-supporting-facts, qa4-two-arg-relations, qa5-three-arg-relations)
- Notable patterns: Performance generally decreases as context size increases; qa1 (single fact) maintains highest accuracy across all lengths; tasks with more supporting facts show steeper decline; all tasks show variation (standard deviation bands) across training runs
- Supports claim: RMT performance varies between training seeds and degrades with increasing context length [p. 18]

For each experiment we conducted three runs with different memory initializations and dataset shuffles. As shown in Figure 5, performance on context lengths, exceeding ones seen during training, may vary across different runs. This suggests that the early stopping criterion based on short-context accuracy may not be optimal. To reduce deviations between runs and enhance overall performance, techniques such as improving early stopping, gradient truncation and training on longer sequences can be employed. [p. 18]

To fine-tune mamba-130m, we used the exact same curriculum approach, with a randomly selected number of segments that gradually increases. Throughout every curriculum step, the batch size remained constant at 128. We employed the AdamW optimizer with a linear schedule, weight decay of 2.0, gradient clipping of 1.0, learning rate of 4e-4, and a warmup step count of 10% of the total training steps. The model was trained for 10,000 steps in each curriculum stage except for the last one, which had 32 segments, where it was trained for 15,000 steps. GPUs were used for the training, and the overall training process for every task from BABILong took 2 to 3 days to complete. [p. 18]

To evaluate recurrent models on the BABILong benchmark we use the full test set for sequences up to 1M tokens, for 10M tokens we only provide results on averaged over 100 samples. As shown in Table 3, evaluation time grows linearly with context length. We fix a random seed used to sample background texts from PG19 for the test set. However, the seed was not fixed to avoid overfitting to specific sampled texts during training. [p. 18]

**Table 3** (p. 18): "Time required for processing 1000 BABILong samples with RMT using a single A100 80Gb GPU, including input data processing."

| Context size | 4k | 32k | 128k | 1M |
|--------------|-----|-----|------|-----|
| Processing time, minutes | 4 | 30 | 80 | 315 |
