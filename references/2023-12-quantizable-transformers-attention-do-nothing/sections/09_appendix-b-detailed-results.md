# B Detailed Results [p. 16–20]

[p. 16] This section provides extended results for each model, including the used hyperparameters and other design choices. Additional ablation studies are also presented.

**Table 4** (p. 17): "An overview of the gating function parameterizations explored in this paper and their memory overhead."

| Configuration | $G$ | Memory overhead (per attention layer): # extra parameters | Memory overhead (per attention layer): # extra tokens |
|---|---|---|---|
| Linear | $n_{\text{heads}} \times \text{Linear}(d_{\text{head}} \to 1)$ | $n_{\text{heads}}(d_{\text{head}} + 1)$ | $\sim 1$ |
| MLP | $n_{\text{heads}} \times \text{MLP}(d_{\text{head}} \to n_{\text{hid}} \to 1)$ | $n_{\text{heads}}(n_{\text{hid}}(d_{\text{head}} + 2) + 1)$ | $\sim n_{\text{hid}}$ |
| All-heads-linear | $\text{Linear}(d_{\text{model}} \to n_{\text{heads}})$ | $n_{\text{heads}}(d_{\text{model}} + 1)$ | $\sim n_{\text{heads}}$ |

## B.1 Gating Architectures

[p. 17] The authors investigate the choice of several gating functions, summarized in Table 4. The configuration "MLP" parameterizes each $G_i$ with a feed-forward net with one hidden layer of size $n_{\text{hid}}$ and a ReLU non-linearity [47]. They also explore what happens if they allow the mixing of the representation from different attention heads in the "All-heads-linear" setting, where a single linear layer is used to produce the gating probabilities for all attention heads at once. All three options are tested below.

> "Unless explicitly stated otherwise, we initialize the bias of the gating function to zero (i.e., $b_{\text{init}} = 0 \leftrightarrow \pi_{\text{init}} = 0.5$)." [p. 17]

## B.2 BERT

**Table 5** (p. 17): "Main results for our proposed clipped softmax (CS) and gated attention (GA) applied to BERT-base. We report the masked language modeling perplexity (ppl. for short) on the English Wikipedia validation set for both the floating-point baseline and W8A8 quantized model. We also report the maximum $\|\mathbf{x}\|_\infty$ averaged across the validation set, and kurtosis of $\mathbf{x}$ averaged across all layers, where $\mathbf{x}$ is the output of an attention layer."

| Method | FP16 ppl.$\downarrow$ | Max inf norm | Avg. Kurtosis | W8A8 ppl.$\downarrow$ |
|---|---|---|---|---|
| Vanilla | $4.49^{\pm 0.01}$ | $735.0^{\pm 54.9}$ | $3076^{\pm 262}$ | $1294^{\pm 1046}$ |
| CS ($\gamma = -0.005$) | $4.44^{\pm 0.02}$ | $406.6^{\pm 35.2}$ | $1963^{\pm 753}$ | $75.27^{\pm 39.57}$ |
| CS ($\gamma = -0.01$) | $4.35^{\pm 0.01}$ | $198.3^{\pm 78.7}$ | $1581^{\pm 839}$ | $7.06^{\pm 2.37}$ |
| CS ($\gamma = -0.015$) | $4.37^{\pm 0.01}$ | $38.9^{\pm 7.9}$ | $165^{\pm 34}$ | $4.54^{\pm 0.01}$ |
| CS ($\gamma = -0.02$) | $4.39^{\pm 0.02}$ | $31.7^{\pm 6.3}$ | $90^{\pm 20}$ | $4.56^{\pm 0.02}$ |
| CS ($\gamma = -0.025$) | $\mathbf{4.39}^{\pm 0.00}$ | $\mathbf{21.5}^{\pm 1.5}$ | $\mathbf{80}^{\pm 6}$ | $\mathbf{4.52}^{\pm 0.01}$ |
| CS ($\gamma = -0.03$) | $4.41^{\pm 0.01}$ | $20.4^{\pm 0.2}$ | $79^{\pm 6}$ | $4.55^{\pm 0.01}$ |
| CS ($\gamma = -0.04$) | $4.51^{\pm 0.05}$ | $19.8^{\pm 9.0}$ | $85^{\pm 7}$ | $4.65^{\pm 0.06}$ |
| GA, Linear ($\pi_{\text{init}} = 0.25$) | $4.49^{\pm 0.00}$ | $139.8^{\pm 62.3}$ | $739^{\pm 412}$ | $5.05^{\pm 0.27}$ |
| GA, Linear ($\pi_{\text{init}} = 0.5$) | $4.48^{\pm 0.00}$ | $177.3^{\pm 33.2}$ | $652^{\pm 81}$ | $5.13^{\pm 0.15}$ |
| GA, Linear ($\pi_{\text{init}} = 0.75$) | $4.49^{\pm 0.00}$ | $71.4^{\pm 49.9}$ | $262^{\pm 147}$ | $4.88^{\pm 0.22}$ |
| GA, Linear ($\pi_{\text{init}} = 0.9$) | $4.49^{\pm 0.00}$ | $171.5^{\pm 8.8}$ | $559^{\pm 141}$ | $5.15^{\pm 0.03}$ |
| GA, MLP ($n_{\text{hid}} = 4$) | $\mathbf{4.45}^{\pm 0.03}$ | $\mathbf{39.2}^{\pm 26.0}$ | $\mathbf{201}^{\pm 181}$ | $\mathbf{4.65}^{\pm 0.04}$ |
| GA, MLP ($n_{\text{hid}} = 64$) | $4.49^{\pm 0.01}$ | $117.0^{\pm 48.3}$ | $507^{\pm 167}$ | $4.77^{\pm 0.01}$ |
| GA, All-heads-linear | $4.49^{\pm 0.01}$ | $58.3^{\pm 41.2}$ | $334^{\pm 321}$ | $4.67^{\pm 0.03}$ |

[p. 17] Detailed results for BERT-base are summarized in Table 5. Across most of the settings, both methods significantly dampen the outliers' magnitude, reduce the kurtosis, drastically improve the quantized performance, while maintaining and sometimes even improving the FP16 perplexity.

## B.3 OPT

[p. 17–18] Detailed results for OPT-125m are summarized in Table 6.

In early experiments on a smaller OPT model, the authors found that applying the weight decay on LayerNorm weights $\gamma$ (which is not the case by default) has a strong effect on reducing the outliers' magnitude while yielding the comparable FP16 performance. Therefore, results are presented for applying the gated attention approach in both cases, with and without applying weight decay on LN $\gamma$.

**Table 6** (p. 18): "Main results for our proposed clipped softmax (CS) and gated attention (GA) applied to OPT-125m. We report the causal language modeling perplexity (ppl. for short) on the English Wikipedia validation set for both the floating-point baseline and W8A8 quantized model. We also report the maximum $\|\mathbf{x}\|_\infty$ averaged across the validation set, and kurtosis of $\mathbf{x}$ averaged across all layers, where $\mathbf{x}$ is the output of an attention layer."

| Method | LN $\gamma$ wd | FP16 ppl.$\downarrow$ | Max inf norm | Avg. Kurtosis | W8A8 ppl.$\downarrow$ |
|---|---|---|---|---|---|
| Vanilla | $\times$ | $15.84^{\pm 0.05}$ | $339.6^{\pm 47.2}$ | $1777^{\pm 444}$ | $21.18^{\pm 1.89}$ |
| GA, Linear ($\pi_{\text{init}} = 0.1$) | $\times$ | $15.61^{\pm 0.05}$ | $35.6^{\pm 4.5}$ | $42.4^{\pm 22.9}$ | $16.41^{\pm 0.18}$ |
| GA, Linear ($\pi_{\text{init}} = 0.25$) | $\times$ | $\mathbf{15.50}^{\pm 0.04}$ | $\mathbf{35.8}^{\pm 0.5}$ | $\mathbf{59.0}^{\pm 48.3}$ | $\mathbf{16.25}^{\pm 0.08}$ |
| GA, Linear ($\pi_{\text{init}} = 0.5$) | $\times$ | $15.54^{\pm 0.01}$ | $46.5^{\pm 5.0}$ | $40.6^{\pm 8.9}$ | $16.30^{\pm 0.01}$ |
| GA, All-heads-linear | $\times$ | $15.43^{\pm 0.01}$ | $32.8^{\pm 1.7}$ | $24.2^{\pm 3}$ | $16.30^{\pm 0.12}$ |
| Vanilla | $\checkmark$ | $15.96^{\pm 0.03}$ | $87.7^{\pm 31.9}$ | $2080^{\pm 1460}$ | $39.46^{\pm 16.59}$ |
| CS ($\gamma = -1/512$) | $\checkmark$ | $15.99^{\pm 0.02}$ | $106.4^{\pm 7.0}$ | $5764^{\pm 2150}$ | $185.23^{\pm 220.00}$ |
| CS ($\gamma = -2/512$) | $\checkmark$ | $15.90^{\pm 0.02}$ | $102.0^{\pm 27.0}$ | $11290^{\pm 4372}$ | $60.90^{\pm 52.70}$ |
| CS ($\gamma = -4/512$) | $\checkmark$ | $15.86^{\pm 0.01}$ | $83.1^{\pm 20.6}$ | $17174^{\pm 7791}$ | $84.64^{\pm 10.55}$ |
| CS ($\gamma = -8/512$) | $\checkmark$ | $16.13^{\pm 0.09}$ | $61.5^{\pm 9.9}$ | $19204^{\pm 4284}$ | $42.62^{\pm 3.64}$ |
| CS ($\gamma = -12/512$) | $\checkmark$ | $16.29^{\pm 0.07}$ | $63.2^{\pm 8.8}$ | $19727^{\pm 7479}$ | $37.22^{\pm 2.39}$ |
| GA, Linear ($\pi_{\text{init}} = 0.1$) | $\checkmark$ | $15.69^{\pm 0.05}$ | $7.3^{\pm 0.4}$ | $25.4^{\pm 10}$ | $16.23^{\pm 0.08}$ |
| GA, Linear ($\pi_{\text{init}} = 0.25$) | $\checkmark$ | $\mathbf{15.55}^{\pm 0.05}$ | $\mathbf{8.7}^{\pm 0.6}$ | $\mathbf{18.9}^{\pm 1}$ | $\mathbf{16.02}^{\pm 0.07}$ |
| GA, Linear ($\pi_{\text{init}} = 0.5$) | $\checkmark$ | $15.63^{\pm 0.00}$ | $10.8^{\pm 0.7}$ | $42.0^{\pm 19}$ | $16.20^{\pm 0.01}$ |
| GA, All-heads-linear | $\checkmark$ | $15.53^{\pm 0.01}$ | $7.9^{\pm 0.3}$ | $13.8^{\pm 1}$ | $16.09^{\pm 0.08}$ |

[p. 18] In both cases (with and without LN $\gamma$ weight decay), gated attention further dampens the outliers' magnitude to a great extent, reduces the kurtosis, and yields models with significantly higher quantized performance, which is close to the original FP16 performance.

## B.4 ViT

[p. 18–19] Detailed results for ViT-S/16 are summarized in Table 7.

After preliminary experiments on ViT, the authors noticed that distinct outliers already originate after the patch embeddings (which was absent in the model definition, by default). They experimented with adding the LayerNorm after the patch embeddings. Together with this change, both proposed methods greatly dampen the outliers' magnitude, reduce the kurtosis, and yield models with significantly higher quantized performance, which is within 1% of the original FP32 accuracy.

**Table 7** (p. 18): "Main results for our proposed clipped softmax (CS) and gated attention (GA) applied to ViT-S/16. We report the top-1 accuracy on ImageNet-1K validation set for floating-point baseline and W8A8 quantized model. We also report the maximum $\|\mathbf{x}\|_\infty$ averaged across the validation set, and kurtosis of $\mathbf{x}$ averaged across all layers, where $\mathbf{x}$ is the output of the attention layer."

| Method | Patch. Embd. LN | FP32 acc. | Max inf norm | Avg. Kurtosis | W8A8 acc. |
|---|---|---|---|---|---|
| Vanilla | $\times$ | $80.75^{\pm 0.10}$ | $358.5^{\pm 81.2}$ | $1018.3^{\pm 471.5}$ | $69.24^{\pm 6.93}$ |
| CS ($\gamma = -0.003$) | $\times$ | $80.24^{\pm 0.05}$ | $69.3^{\pm 20.7}$ | $25.6^{\pm 8.6}$ | $78.71^{\pm 0.33}$ |
| CS ($\gamma = -0.004$) | $\times$ | $80.38^{\pm 0.01}$ | $74.9^{\pm 10.6}$ | $30.6^{\pm 4.9}$ | $78.66^{\pm 0.49}$ |
| GA, Linear ($\pi_{\text{init}} = 0.25$) | $\times$ | $80.62^{\pm 0.01}$ | $86.0^{\pm 8.0}$ | $23.4^{\pm 2.7}$ | $79.16^{\pm 0.05}$ |
| GA, Linear ($\pi_{\text{init}} = 0.5$) | $\times$ | $80.32^{\pm 0.02}$ | $88.4^{\pm 17.9}$ | $27.9^{\pm 14.0}$ | $78.90^{\pm 0.25}$ |
| GA, MLP ($n_{\text{hid}} = 4$) | $\times$ | $80.62^{\pm 0.05}$ | $118.2^{\pm 40.5}$ | $47.8^{\pm 29.8}$ | $78.79^{\pm 0.29}$ |
| Vanilla | $\checkmark$ | $80.98^{\pm 0.08}$ | $81.1^{\pm 2.5}$ | $24.5^{\pm 1.8}$ | $79.62^{\pm 0.06}$ |
| CS ($\gamma = -0.0001$) | $\checkmark$ | $\mathbf{80.89}^{\pm 0.13}$ | $\mathbf{73.7}^{\pm 14.9}$ | $\mathbf{22.9}^{\pm 1.6}$ | $\mathbf{79.77}^{\pm 0.25}$ |
| CS ($\gamma = -0.0003$) | $\checkmark$ | $80.92^{\pm 0.07}$ | $78.9^{\pm 5.5}$ | $23.8^{\pm 0.5}$ | $79.63^{\pm 0.05}$ |
| CS ($\gamma = -0.0005$) | $\checkmark$ | $80.95^{\pm 0.08}$ | $72.9^{\pm 11.8}$ | $24.4^{\pm 0.7}$ | $79.73^{\pm 0.08}$ |
| CS ($\gamma = -0.001$) | $\checkmark$ | $80.95^{\pm 0.16}$ | $80.8^{\pm 2.1}$ | $24.1^{\pm 0.7}$ | $79.69^{\pm 0.03}$ |
| CS ($\gamma = -0.002$) | $\checkmark$ | $80.80^{\pm 0.07}$ | $78.0^{\pm 0.5}$ | $25.8^{\pm 0.7}$ | $79.32^{\pm 0.07}$ |
| CS ($\gamma = -0.003$) | $\checkmark$ | $80.79^{\pm 0.02}$ | $75.6^{\pm 7.9}$ | $28.1^{\pm 4.0}$ | $79.00^{\pm 0.10}$ |
| GA, Linear ($\pi_{\text{init}} = 0.5$) | $\checkmark$ | $\mathbf{81.01}^{\pm 0.06}$ | $\mathbf{79.8}^{\pm 0.5}$ | $\mathbf{19.9}^{\pm 0.3}$ | $\mathbf{79.82}^{\pm 0.11}$ |
| GA, Linear ($\pi_{\text{init}} = 0.75$) | $\checkmark$ | $81.01^{\pm 0.05}$ | $77.8^{\pm 0.3}$ | $21.8^{\pm 1.9}$ | $79.80^{\pm 0.08}$ |
| GA, Linear ($\pi_{\text{init}} = 0.9$) | $\checkmark$ | $80.92^{\pm 0.11}$ | $70.6^{\pm 8.0}$ | $23.2^{\pm 3.7}$ | $79.64^{\pm 0.09}$ |

## B.5 The Impact of Clipped Softmax Hyperparameters ($\gamma$ and $\zeta$) on ViT

[p. 19] The authors investigate the effect of different values of the clipped softmax stretch parameters applied to the vision transformer.

**Table 8** (p. 19): "The impact of clipped softmax hyperparameters on ViT-S/16."

Training was sped up: 150 epochs instead of the usual 300 epochs. LayerNorm was not applied after the patch embeddings for this experiment.

| $\gamma$ | $\zeta$ | FP32 acc. | Max inf norm | W8A8 acc. |
|---|---|---|---|---|
| 0 (= Vanilla) | 1 | $78.80^{\pm 0.42}$ | $426^{\pm 69}$ | $71.27^{\pm 0.88}$ |
| 0 | 1.001 | $78.78^{\pm 0.29}$ | $411^{\pm 88}$ | $71.24^{\pm 0.59}$ |
| 0 | 1.002 | $78.90^{\pm 0.17}$ | $420^{\pm 47}$ | $70.74^{\pm 0.34}$ |
| 0 | 1.004 | $78.80^{\pm 0.45}$ | $377^{\pm 67}$ | $72.31^{\pm 0.06}$ |
| 0 | 1.01 | $78.81^{\pm 0.30}$ | $419^{\pm 77}$ | $71.35^{\pm 0.26}$ |
| $-0.00001$ | 1 | $78.81^{\pm 0.21}$ | $432^{\pm 76}$ | $69.02^{\pm 0.19}$ |
| $-0.0001$ | 1 | $78.81^{\pm 0.36}$ | $380^{\pm 64}$ | $64.04^{\pm 10.8}$ |
| $-0.001$ | 1 | $78.42^{\pm 0.63}$ | $282^{\pm 105}$ | $68.43^{\pm 6.50}$ |
| $-0.003$ | 1 | $\mathbf{78.26}^{\pm 0.06}$ | $\mathbf{99}^{\pm 36}$ | $\mathbf{76.49}^{\pm 0.48}$ |
| $-0.01$ | 1 | $78.10^{\pm 0.14}$ | $391^{\pm 21}$ | $75.83^{\pm 1.12}$ |
| $-0.03$ | 1 | $70.26^{\pm 1.46}$ | $197^{\pm 2}$ | $65.80^{\pm 1.41}$ |
| $-0.001$ | 1.001 | $78.45^{\pm 0.53}$ | $283^{\pm 82}$ | $65.03^{\pm 8.54}$ |
| $-0.003$ | 1.003 | $\mathbf{78.25}^{\pm 0.14}$ | $\mathbf{119}^{\pm 17}$ | $\mathbf{76.37}^{\pm 0.45}$ |

[p. 19] The authors found similar observations compared to BERT. Specifically, most of the improvement happens when using $\gamma < 0$ (clipping at zero), whereas using $\zeta > 1$ (clipping at one) yields similar results to the vanilla softmax. Combining both $\gamma < 0$ and $\zeta > 1$ yields similar results compared to just clipping at zero.

## B.6 Fine-tuning Experiment

**Table 9** (p. 19): "OPT-1.3B fine-tuning results with vanilla softmax and gated attention. We report the causal language modeling perplexity (ppl. for short) on the English Wikipedia validation set. We also report the maximum $\|\mathbf{x}\|_\infty$ averaged across the validation set, and kurtosis of $\mathbf{x}$ averaged across all layers, where $\mathbf{x}$ is the output of an attention layer."

| Method | FP16 ppl.$\downarrow$ | Max inf norm | Avg. Kurtosis |
|---|---|---|---|
| Vanilla fine-tuning | 29.46 | 79.3 | 2086 |
| Fine-tuning w/ Gated attention | 29.18 | 50.9 | 665 |

[p. 19–20] One drawback of the proposed framework is that it requires training from scratch, which could be expensive when applied to very large models. To address this, the authors explored whether *fine-tuning* using gated attention can still lead to improved performance and decreased outliers for larger models.

They used OPT-1.3B pre-trained checkpoint from HuggingFace and fine-tuned it on Bookcorpus + Wikipedia for 4000 steps with batch size 256, maximum sequence length 512, maximum learning rate $10^{-5}$, and linear LR schedule with 400 warmup steps. The same LR is used for both model parameters and gating module parameters. The rest of the hyper-parameters are the same as for the pre-training setup.

The gating approach was adapted as follows: bias initialized as $b_{\text{init}} = 0$, which corresponds to the expected initial gating probability output of $\pi_{\text{init}} = 0.5$. The gating probability is multiplied by 2 so that the expected gate output is 1 and the vanilla softmax attention output is approximated at the start of fine-tuning. A small activation regularization term is added at the output of each FFN to further encourage the reduction in the magnitude of activations, as unlike when training from scratch, outliers are already present in the pre-trained model and need to be suppressed.

Fine-tuning with gated attention results in a better perplexity and also reduced maximum infinity norm and the average kurtosis compared to fine-tuning with vanilla softmax.

## B.7 Low-bit Quantization Results

**Table 10** (p. 20): "A summary of results for our proposed methods applied to BERT-base and quantized to different bitwidths for weights and activations (using the same PTQ setup as in all previous experiments). We report the masked language modeling perplexity on the English Wikipedia validation set."

| Bitwidths | Weight range estimation | Vanilla | Clipped softmax | Gated attention |
|---|---|---|---|---|
| FP16 | -- | $4.49^{\pm 0.01}$ | $4.39^{\pm 0.00}$ | $4.45^{\pm 0.03}$ |
| W8A8 | min-max | $1294^{\pm 1046}$ | $4.52^{\pm 0.01}$ | $4.65^{\pm 0.04}$ |
| W6A8 | min-max | $598^{\pm 254}$ | $4.64^{\pm 0.01}$ | $4.79^{\pm 0.03}$ |
| W6A8 | MSE | $6.49^{\pm 0.38}$ | $4.56^{\pm 0.01}$ | $4.71^{\pm 0.03}$ |
| W4A8 | MSE | $6.52^{\pm 0.02}$ | $4.90^{\pm 0.02}$ | $5.02^{\pm 0.03}$ |
| W6A6 | MSE | $42.8^{\pm 11.7}$ | $6.64^{\pm 0.14}$ | $5.90^{\pm 0.11}$ |

[p. 20] The proposed methods are not limited to 8-bit quantization and can in general be combined with other more advanced quantization and weight compression methods, including [18, 35, 36, 45, 63, 67]. Unless stated otherwise, for low-bit (<8-bit) weights and activations the MSE range estimator is used as recommended by [2, 7] since it gives better results.

Both methods significantly improve the perplexity compared to the vanilla softmax pre-training across all bitwidths. Performance progressively degrades as the bitwidths decrease, which is to be expected. Achieving good results with low-bit activation quantization in general is a challenging problem.

The perplexity of the vanilla model significantly improves whenever a low-bit weight quantization with MSE ranges is considered compared to the INT8 case. This can be explained by the fact that using MSE range estimation for weights leads to an implicit clipping of activations (in the same and all subsequent layers in the network), which happen to be of the right amount so that it does not hurt the perplexity.

The authors found that by going from W8A8 to W6A8 the average kurtosis is reduced from $3406^{\pm 547}$ to $631^{\pm 94}$ and the maximum infinity norm is reduced from $577^{\pm 80}$ to $158^{\pm 40}$. However, in all cases the resulting model still has significantly larger outliers and a worse performance than both of the proposed methods.

> "if achieving good low-bit quantization performance is the goal, it is recommended to combine our methods with more advanced quantization techniques." [p. 20]
