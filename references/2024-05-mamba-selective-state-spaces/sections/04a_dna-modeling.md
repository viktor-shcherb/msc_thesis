# 4.3 DNA Modeling [p. 12–14]

[p. 12]

Motivated by the success of large language models, there has been recent exploration into using the foundation model paradigm for genomics. DNA has been likened to language in that it consists of sequences of discrete tokens with a finite vocabulary. It is also known for requiring long-range dependencies to model (Avsec et al. 2021). The authors investigate Mamba as a FM backbone for pretraining and fine-tuning in the same setting as recent works on long-sequence models for DNA (Nguyen, Poli, et al. 2023). In particular, they focus on two explorations of scaling laws across model size and sequence length (Figure 5), and a difficult downstream synthetic classification task requiring long context (Figure 6). [p. 12]

For pretraining, the authors largely follow a standard causal language modeling (next token prediction) setup for the training and model details (see also Appendix E.2). For the dataset, they largely follow the setup of HyenaDNA (Nguyen, Poli, et al. 2023), which uses the HG38 dataset for pretraining consisting of a single human genome with about 4.5 billion tokens (DNA base pairs) in the training split. [p. 12]

## 4.3.1 Scaling: Model Size

[p. 13]

In this experiment, the authors investigate the scaling properties of genomics foundation models with various model backbones (Figure 5 *Left*). [p. 13]

**Training.** To advantage the baselines, they train on a short sequence length of 1024; as shown in Section 4.3.2, they expect results to favor Mamba even more at longer sequence lengths. They fix a global batch size of 1024, for a total of $2^{20} \approx 1M$ tokens per batch. Models were trained for $10K$ gradient steps for a total of $10B$ tokens. [p. 13]

**Results.** Figure 5 (*Left*) shows that Mamba's pretraining perplexity improves smoothly with model size, and that Mamba scales better than both HyenaDNA and Transformer++. For example, at the largest model size of $\approx 40M$ parameters, the curve shows that > "**Mamba can match the Transformer++ and HyenaDNA models with roughly 3x to 4x fewer parameters**." [p. 13]

## 4.3.2 Scaling: Context Length

[p. 13]

In the next DNA experiment, the authors investigate the scaling properties of models with respect to sequence length. They only compare the HyenaDNA and Mamba models, as quadratic attention becomes prohibitively expensive at longer sequence lengths. They pretrain models on sequence lengths $2^{10} = 1024$, $2^{12} = 4096$, $2^{14} = 16384$, $2^{16} = 65536$, $2^{18} = 262144$, $2^{20} = 1048576$. They fix a model size of 6 layers by width 128 (about 1.3M-1.4M parameters). Models were trained for $20K$ gradient steps for a total of $\approx 330B$ tokens. The longer sequence lengths used sequence length warmup similar to (Nguyen, Poli, et al. 2023). [p. 13]

**Results.** Figure 5 (*Right*) shows that > "**Mamba is able to make use of longer context even up to extremely long sequences of length 1M**", and its pretraining perplexity improves as the context increases. On the other hand, the HyenaDNA model gets worse with sequence length. This is intuitive from the discussion in Section 3.5 on properties of the selection mechanism. In particular, LTI models cannot selectively ignore information; from a convolutional perspective, a very long convolution kernel is aggregating all information across a long sequence which may be very noisy. Note that while HyenaDNA claims to improve with longer context, their results do not control for computation time. [p. 13]

## 4.3.3 Synthetic Species Classification

[p. 13–14]

The authors evaluate models on a downstream task of classifying between 5 different species by randomly sampling a contiguous segment of their DNA. This task is adapted from HyenaDNA, which used the species {human, lemur, mouse, pig, hippo}. They modify the task to be significantly more challenging by classifying between the five *great apes* species {human, chimpanzee, gorilla, orangutan, bonobo}, which are known to share 99% of their DNA. [p. 13]

## Figures

**Figure 5** (p. 13): "(**DNA Scaling Laws.**) Pretraining on the HG38 (human genome) dataset. (*Left*) Fixing short context length $2^{10} = 1024$ and increasing size from $\approx 200K$ to $\approx 40M$ parameters, Mamba scales better than baselines. (*Right*) Fixing model size and increasing sequence lengths while keeping tokens/batch and total training tokens fixed. Unlike baselines, the selection mechanism of Mamba facilitates better performance with increasing context length."

The figure contains two plots side by side:
- **Left plot** ("Scaling Laws on the Human Genome (HG38)"): x-axis is Parameters (log scale, from $10^5$ to $10^7$), y-axis is Perplexity (ranging roughly from 2.7 to 3.1). Three lines are shown: HyenaDNA (blue), Mamba (orange), Transformer++ (green). Mamba consistently achieves the lowest perplexity at each model size, with the gap widening at larger model sizes. At $\approx 40M$ parameters, Mamba achieves a perplexity that HyenaDNA and Transformer++ require 3-4x more parameters to match.
- **Right plot** ("Scaling Laws - Sequence Length (HG38)"): x-axis is Sequence Length (log scale, from $10^3$ to $10^6$), y-axis is Perplexity (ranging roughly from 2.75 to 3.00). Three lines: HyenaDNA 1.4M (blue), Mamba 1.4M (orange), Mamba 7M (green). Mamba 1.4M perplexity consistently decreases (improves) as sequence length increases. HyenaDNA 1.4M perplexity initially decreases but then increases at longer sequence lengths. Mamba 7M achieves the best perplexity across all sequence lengths.

**Figure 6** (p. 14): "(**Great Apes DNA Classification.**) Accuracy after fine-tuning on sequences of length $2^{10} = 1024$ up to $2^{20} = 1048576$ using pretrained models of the same context length. Numerical results in Table 13."

The figure shows:
- x-axis: Sequence Length (log scale, from $10^3$ to $10^6$)
- y-axis: Accuracy (ranging from 0.2 to 0.8)
- Models: HyenaDNA 1.4M (blue), Mamba 1.4M (orange), Mamba 7M (green), Random (dashed gray baseline at 0.2)
- Mamba 1.4M and Mamba 7M both show improving accuracy with sequence length, reaching over 0.7 at the longest sequences. HyenaDNA 1.4M also improves initially but plateaus or declines at the longest lengths. Mamba 7M achieves the highest accuracy overall. Random baseline stays flat at 0.2 (1/5 chance for 5 species).
