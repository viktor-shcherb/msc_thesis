# 5 Experiments [p. 6]

[p. 6] The authors evaluate the proposed modifications to self-attention on several language models (BERT, OPT) and the vision transformers (ViT). They first test the different hyperparameters for the methods and provide insight into how they work. Then they set out to test their method in terms of accuracy, and the difference in quantization improvement after training. All detailed hyperparameters of the experiments are in Appendix C.

## BERT

[p. 6] Experimental setup:
- **Model:** BERT-base-uncased (109M parameters)
- **Objective:** Masked language modeling (MLM)
- **Training data:** Concatenation of the training sets of BookCorpus [77] and English Wikipedia (footnote 7: Specifically, the English subset of Wiki-40b, https://huggingface.co/datasets/wiki40b, that contains cleaned-up text of English Wikipedia and training/validation splits). Following [14].
- **Implementation:** PyTorch [48], HuggingFace libraries [20, 34, 65]
- **Training procedure:** Following the pre-training procedure from [14]
- **Sequence length:** Maximum sequence length of 128 for the whole duration of the training (to speed up training and experimentation)
- **Evaluation:** Wikipedia validation set, reporting MLM perplexity

## OPT

[p. 6] Experimental setup:
- **Model:** 125M sized variant of OPT [74]
- **Objective:** Causal language modeling (CLM)
- **Training data:** Same dataset as BERT pre-training (BookCorpus + Wikipedia) with a maximum sequence length of 512
- **Batch size:** 192
- **Training and evaluation pipelines:** HuggingFace libraries
- **Evaluation:** Wikipedia validation set, reporting CLM perplexity

## ViT

[p. 7] Experimental setup:
- **Model:** Vision transformer [15] (ViT-S/16 configuration, 22M parameters)
- **Training data:** ImageNet-1K [11, 52]
- **Training and validation pipelines:** PyTorch Image models library [64]
- **Evaluation:** Top-1 accuracy on the validation set of ImageNet

## Quantization Setup

[p. 7] In all experiments, after the model is trained, 8-bit PTQ is applied. The quantization setup uses:
- **Scheme:** Uniform affine quantization -- symmetric weights, asymmetric activations -- with the static activation range setting, as discussed in Section 2
- **Scope:** All weights and activations (both input and output) are quantized, except the final linear layer for BERT and OPT models
- **Range estimation:** Several choices explored (see Appendix C.4); the best configuration for each experiment is reported based on model performance
- **Repetitions:** Each PTQ experiment repeated 3 times with different random seeds (footnote 8: Different random subsets of training data are used for quantizer range estimation); mean and standard deviation reported for accuracy/perplexity

Each network is trained two times with different random seeds and mean and standard deviation are reported.

**Outlier metrics:** To assess the amount of outliers in the trained model, two metrics are used:
- **Maximum $\|\mathbf{x}\|_\infty$:** averaged across the validation set
- **Kurtosis of $\mathbf{x}$:** averaged across all layers, where $\mathbf{x}$ is the output of an attention layer

These metrics have been shown to correlate well with model quantizability [4, 6].

## 5.1 The impact of clipped softmax hyperparameters ($\gamma$ and $\zeta$)

[p. 7] The effect of different values of the clipped softmax stretch parameters is investigated, with results presented in Table 1. Most of the improvement happens when $\gamma < 0$ (clipping at zero). For instance, using the value of $\gamma = -0.03$ leads to a significantly smaller infinity norm, kurtosis, and quantized model perplexity, compared to the baseline. In the limit $|\gamma| \to 0$ the approach converges to vanilla softmax attention. Using $\zeta > 1$ (clipping at one) yields similar results to the vanilla softmax. When combining both $\gamma < 0$ and $\zeta > 1$, the results seem similar to just clipping at 0. The authors therefore conclude that for dampening outliers, only the lower-range clipping that allows exact zeros matters. Going forward only $\gamma < 0$ is used, and in Appendix B.5 it is confirmed that $\zeta > 1$ is not required for ViT.

These observations are in line with the hypothesis that by giving the model the mechanism for representing exact zeros in the attention, the model does not need to learn the strong outliers.

**Table 1** (p. 7): "The impact of clipped softmax hyperparameters on BERT-base."

| $\gamma$ | $\zeta$ | FP16 ppl.$\downarrow$ | Max inf. norm | Avg. kurtosis | W8A8 ppl.$\downarrow$ |
|---|---|---|---|---|---|
| 0 (= Vanilla) | 1 | $4.49^{\pm 0.01}$ | $735^{\pm 55}$ | $3076^{\pm 262}$ | $1294^{\pm 1046}$ |
| 0 | 1.003 | $4.48^{\pm 0.01}$ | $715^{\pm 335}$ | $2159^{\pm 238}$ | $451^{\pm 57}$ |
| 0 | 1.03 | $4.49^{\pm 0.00}$ | $741^{\pm 66}$ | $1707^{\pm 1249}$ | $1469^{\pm 646}$ |
| $-0.003$ | 1 | $4.46^{\pm 0.00}$ | $688^{\pm 64}$ | $2149^{\pm 110}$ | $636^{\pm 566}$ |
| $-0.03$ | 1 | $\mathbf{4.41}^{\pm 0.01}$ | $\mathbf{20}^{\pm 1}$ | $\mathbf{80}^{\pm 6}$ | $\mathbf{4.55}^{\pm 0.01}$ |
| $-0.003$ | 1.003 | $4.47^{\pm 0.00}$ | $683^{\pm 23}$ | $2494^{\pm 1205}$ | $268^{\pm 120}$ |
| $-0.03$ | 1.03 | $\mathbf{4.43}^{\pm 0.03}$ | $\mathbf{22}^{\pm 3}$ | $\mathbf{73}^{\pm 8}$ | $\mathbf{4.56}^{\pm 0.05}$ |

## 5.2 Clipped softmax $\gamma$ vs. sequence length

[p. 7-8] Having an extra hyper-parameter that needs to be tuned per model or setup is generally not desirable. The sensitivity of the stretch factor $\gamma$ and its relation with the sequence length $T$ is studied. The matrix of attention probabilities $\mathbf{P}$ has dimensions $T \times T$ and each row sums up to one. Because of that, the average value in $\mathbf{P}$ is $1/T$. It is reasonable to assume that if we define $\gamma := -\alpha/T$, where $\alpha > 0$ is a new hyperparameter, there might be a set or a range of values of $\alpha$ that works well across different sequence lengths.

[p. 8] To study this, a 6-layer variant of BERT-base (BERT-6L) is trained for 500000 steps on WikiText-103 [42] with a batch size of 128 with several values of maximum sequence lengths $T \in \{32, 64, 128, 192, 256\}$ and values of $\alpha \in \{1/4, 1/2, 1, 2, 4, 8\}$. As shown in Figure 6, using a clipped softmax with $\alpha \in [2, 4]$ significantly dampens the magnitude of outliers while maintaining good FP16 perplexity across all explored sequence lengths.

**Figure 6** (p. 8): "The performance of clipped softmax using $\gamma = -\alpha/T$ parameterization on BERT-6L."
- **(a) Relative FP16 log-perplexity:** x-axis is $\alpha$ (log scale: 0.25 to 8.0), y-axis is Rel. FP16 log-perplexity. Shows lines for $T = 32, 64, 128, 192, 256$ plus a dashed vanilla baseline at 1.0. All sequence lengths show perplexity remains close to 1.0 (within 0.75-1.0 range) for $\alpha$ up to about 4, with slight degradation at $\alpha = 8$. Evaluated on WikiText validation set.
- **(b) Maximum infinity norm:** x-axis is $\alpha$ (log scale: 0.25 to 8.0), y-axis is Max inf. norm (log scale: 2 to 512). Shows lines for $T = 32, 64, 128, 192, 256$ plus vanilla baseline. All sequence lengths converge from high values (64-512 range) at low $\alpha$ down to very low values (2-8 range) at $\alpha \geq 2$, confirming that $\alpha \in [2, 4]$ effectively dampens outliers.

## 5.3 The impact of bias initialization in gated attention

[p. 8] In all gated attention experiments, the weights of $\mathbf{G}$ are randomly initialized following [22]. By initializing the *bias* to a specific value, the gates can be set to be more *open* or more *closed* initially. More open at the start means initializing closer to the original network, but given the exponential nature of the gate it might take many iterations for the gate to learn to close. Similarly, if the gates are all closed at the start, the deviation is too far from the original model training, causing a potential decrease in performance. Assuming Linear $\mathbf{G}_i$'s with small initial weights, if the bias is set to the value of $b_{\text{init}}$, then $\mathbf{G}_i(\cdot) \approx b_{\text{init}}$ and $\boldsymbol{\pi}_i(\cdot) = \text{sigmoid}(\mathbf{G}_i(\cdot)) \approx \text{sigmoid}(b_{\text{init}}) =: \pi_{\text{init}}$, at the start of training.

The effect of different values of $b_{\text{init}}$ for Linear gated attention on BERT-6L and ViT is studied. The bias for all $\mathbf{G}_i$'s is set to the same value of $b_{\text{init}}$. For BERT-6L, the same setup as in Section 5.2 is used, with a fixed sequence length of 128. For ViT, the main setup is used, except it is trained for 150 epochs instead of 300.

[p. 8] In Figure 7, in both BERT and ViT cases, using bias with very high $\pi_{\text{init}}$ generally performs similarly to the vanilla attention (comparable floating-point performance but strong outliers and poor quantized performance) while setting bias to have very low $\pi_{\text{init}}$ dampens outliers quite well but leads to strong degradation in the floating-point and quantized performance. The reasonable ranges of $\pi_{\text{init}}$ seem to be around $[0.25, 0.9]$ for BERT and $[0.1, 0.5]$ for ViT. The wide range indicates the relative robustness of the method to this hyperparameter.

**Figure 7** (p. 8): "The performance of Linear gated attention using different bias initialization settings."
- **(a) BERT-6L:** x-axis is $b_{\text{init}}$ (from -10.0 to 5.0), secondary x-axis at top shows $\pi_{\text{init}}$ values (1e-05 to 0.99). Left y-axis is Perplexity $\downarrow$ (range ~5.0 to 7.5), right y-axis is Max inf. norm (range 0 to 300). Four curves plotted: vanilla (dashed), FP16 ppl., W8A8 ppl., and Max inf. norm. FP16 ppl. remains stable (~5.0-5.5) for $b_{\text{init}} \gtrsim -5$, then degrades. W8A8 ppl. tracks FP16 ppl. for $b_{\text{init}} \in [-5, 0]$, then diverges upward for very high $b_{\text{init}}$. Max inf. norm is low (<50) for $b_{\text{init}} \lesssim 0$, then climbs rapidly.
- **(b) ViT:** x-axis is $b_{\text{init}}$ (from -10.0 to 5.0), secondary x-axis at top shows $\pi_{\text{init}}$ values. Left y-axis is Top-1 accuracy $\uparrow$ (range ~45 to 80), right y-axis is Max inf. norm (range ~100 to 700). Similar pattern: FP32 accuracy is stable (~75-80%) for $b_{\text{init}} \in [-2.5, 2.5]$, degrades outside that range. W8A8 accuracy is best for $b_{\text{init}} \in [-5, 0]$. Max inf. norm increases sharply for $b_{\text{init}} > 0$.

## 5.4 Main results

[p. 9] The main set of results is summarized in Table 2. In almost all cases, both proposed techniques dampen the outliers' magnitude to a great extent, reduce the kurtosis, and yield models with significantly higher quantized performance, which is close to the original FP16/32 performance. In addition, for each model, at least one of the methods also improves the floating-point task performance. The authors hypothesize this is because the network is helped by learning the "no-op" updates more easily. However, they are cautious about the improved performance as this is not consistent across all hyper-parameters and it is unclear if it generalizes to more architectures and larger models.

The only case where the method failed to perform well was the clipped softmax applied to OPT. No explanation is given and this is left for future work. Selected hyper-parameters and extended results are listed in Appendix B. Results of the proposed methods quantized to lower bitwidths are shown in Appendix B.7.

**Table 2** (p. 9): "A summary of results for our proposed methods applied on BERT, OPT-125m, and ViT."

| Model | Method | FP16/32 | Max inf. norm | Avg. kurtosis | W8A8 |
|---|---|---|---|---|---|
| BERT (ppl.$\downarrow$) | Vanilla | $4.49^{\pm 0.01}$ | $735^{\pm 55}$ | $3076^{\pm 262}$ | $1294^{\pm 1046}$ |
| BERT (ppl.$\downarrow$) | Clipped softmax | $\mathbf{4.39}^{\pm 0.00}$ | $\mathbf{21.5}^{\pm 1.5}$ | $\mathbf{80}^{\pm 6}$ | $\mathbf{4.52}^{\pm 0.01}$ |
| BERT (ppl.$\downarrow$) | Gated attention | $4.45^{\pm 0.03}$ | $39.2^{\pm 26.0}$ | $201^{\pm 181}$ | $4.65^{\pm 0.04}$ |
| OPT (ppl.$\downarrow$) | Vanilla | $15.84^{\pm 0.05}$ | $340^{\pm 47}$ | $1778^{\pm 444}$ | $21.18^{\pm 1.89}$ |
| OPT (ppl.$\downarrow$) | Clipped softmax | $16.29^{\pm 0.07}$ | $63.2^{\pm 8.8}$ | $19728^{\pm 7480}$ | $37.20^{\pm 2.40}$ |
| OPT (ppl.$\downarrow$) | Gated attention | $\mathbf{15.55}^{\pm 0.05}$ | $\mathbf{8.7}^{\pm 0.6}$ | $\mathbf{18.9}^{\pm 0.9}$ | $\mathbf{16.02}^{\pm 0.07}$ |
| ViT (acc.$\uparrow$) | Vanilla | $80.75^{\pm 0.10}$ | $359^{\pm 81}$ | $1018^{\pm 471}$ | $69.24^{\pm 6.93}$ |
| ViT (acc.$\uparrow$) | Clipped softmax | $80.89^{\pm 0.13}$ | $\mathbf{73.7}^{\pm 14.9}$ | $\mathbf{22.9}^{\pm 1.6}$ | $79.77^{\pm 0.25}$ |
| ViT (acc.$\uparrow$) | Gated attention | $\mathbf{81.01}^{\pm 0.06}$ | $79.8^{\pm 0.5}$ | $19.9^{\pm 0.3}$ | $\mathbf{79.82}^{\pm 0.11}$ |

### Results for bigger models

[p. 9] The question of scalability to larger models is studied. Table 3 shows the gated attention results for 350m and 1.3B variants of OPT. Due to compute constraints, the networks are trained for $10^5$ steps with batch size of 256 and the rest is the same as in the main pre-training setup. The proposed gated attention is also very effective at dampening the outliers and significantly improving the quantized model performance when applied to bigger models. Further study in Appendix B.6 shows how gated attention can decrease outliers when fine-tuning bigger pre-trained models with outliers.

**Table 3** (p. 9): "The performance of gated attention applied on bigger variants of OPT model."

| Model | Method | FP16 | Max inf. norm | Avg. kurtosis | W8A8 |
|---|---|---|---|---|---|
| OPT-350m (ppl.$\downarrow$) | Vanilla | 13.19 | 253 | 2689 | $37.52^{\pm 3.84}$ |
| OPT-350m (ppl.$\downarrow$) | Gated attention | 13.01 | 65.4 | 261 | $\mathbf{14.42}^{\pm 0.06}$ |
| OPT-1.3B (ppl.$\downarrow$) | Vanilla | 12.13 | 428 | 2756 | $989.6^{\pm 175}$ |
| OPT-1.3B (ppl.$\downarrow$) | Gated attention | 12.21 | 67.2 | 444 | $\mathbf{29.95}^{\pm 0.42}$ |

## 5.5 Qualitative results

[p. 9-10] In Figure 8, the learned attention patterns using vanilla softmax and the proposed methods are compared (more examples in Appendix A.1). Both methods can represent a partial/soft no-op behavior, but in case of the proposed methods this does not require strong outliers elsewhere in the network. Similar patterns were found in multiple attention heads, but the exact head indices where such patterns were observed depend on random initialization. In the case of clipped softmax, smaller attention weights are generally more diffused while higher weights are more saturated (which comes from the stretching and clipping). In the case of gated attention, the output of the softmax is significantly different since the update of the hidden representation is now further modulated by gating probabilities.

**Figure 8** (p. 10): "Visualization of the self-attention patterns for BERT-base trained using vanilla and our proposed techniques, computed on data sequence #5 from MNLI-m validation set."
- **(a) Vanilla softmax (Attention layer #11, head #3):** Shows three heatmaps -- attention probabilities, values, and their product. Attention matrix shows a pattern where certain token positions receive concentrated attention (sharp columns), consistent with the "no-op" behavior where attention is directed to specific tokens to achieve near-zero updates.
- **(b) Clipped softmax (Attention layer #11, head #8):** Shows three heatmaps -- attention probabilities, values, and their product. The attention probabilities show more diffused smaller weights with saturated (clipped) higher weights. The product shows a partial no-op pattern without requiring outliers.
- **(c) Gated attention (Attention layer #11, head #5):** Shows gating probabilities $\boldsymbol{\pi} = \text{sigmoid}(\mathbf{G}(\mathbf{x}))$, attention probabilities (output of softmax), values, and their combined product. The gating probabilities column shows which tokens have their updates suppressed (low gate values), allowing the no-op behavior to be achieved through the gate rather than through outliers in the attention matrix.
