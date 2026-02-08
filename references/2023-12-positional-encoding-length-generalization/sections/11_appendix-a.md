# Appendix A: Number of Instances Decreases Rapidly as Sequence Length Grows [p. 16]

[p. 16] The recent trend of SFT-RLHF pipeline (Ouyang et al., 2022) relies on finetuning LLMs on the instruction following tasks. However, the training data of these datasets is often skewed towards shorter sequences. Figure A.1 shows the distribution of instruction lengths in two instruction finetuning datasets: FLAN (CoT subset) (Longpre et al., 2023) and Super Natural Instructions (Wang et al., 2022). The median length of instructions in these datasets is quite short compared to the maximum length that exists. Such distribution shape highlights the importance of length generalization in these tasks. In fact, the models are supposed to learn from short instructions and generalize to ones during inference that might be much longer.

**Figure A.1** (p. 16): "Histogram of instruction lengths in two instruction finetuning datasets: FLAN (CoT subset) (Longpre et al., 2023) and Super Natural Instructions (Wang et al., 2022). The dotted line indicates the median of the length of the instructions in each dataset."

The figure contains two side-by-side histograms:
- **Left panel (FLAN (CoT)):** x-axis is Example Length (0 to ~4000), y-axis is Count (0 to ~60000). The distribution is heavily right-skewed, with the vast majority of examples having lengths below ~500 tokens. The median (dotted line) falls at a short length. A long tail extends to ~4000.
- **Right panel (Super-Natural Instructions):** x-axis is Example Length (0 to ~4000), y-axis is Count (0 to ~60000). Similarly right-skewed distribution with most examples concentrated at short lengths. The median (dotted line) falls at a very short length. A long tail extends to ~4000.

Both distributions demonstrate that the number of training instances decreases rapidly as sequence length grows, motivating the need for length generalization.
