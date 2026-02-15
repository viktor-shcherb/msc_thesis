# 3.2 Scalability Compared with Transformer [p. 5]

The authors compare the scaling properties of DIFF Transformer and Transformer on language modeling [p. 5]. They scale up the model size, and the number of training tokens, respectively [p. 5]. They follow the augmented Transformer architecture as in LLaMA (Touvron et al., 2023) and use the same setting to ensure fair comparison [p. 5]. Specifically, the "Transformer" models include improvements in RMSNorm (Zhang & Sennrich, 2019), SwiGLU (Shazeer, 2020; Ramachandran et al., 2017) as well as the absence of bias [p. 5].

## Scaling Model Size [p. 5]

As shown in Figure 3a, the authors train language models with 830M, 1.4B, 2.8B, 6.8B, and 12.4B parameters [p. 5]. The models are trained with a sequence length of 2048, and a batch size of 0.25M tokens [p. 5]. They train models for 40K steps [p. 5]. Detailed hyperparameters are described in Appendix E [p. 5]. The scaling law (Kaplan et al., 2020) empirically fits well in this configuration [p. 5].

Figure 3a shows that DIFF Transformer outperforms Transformer in various model sizes [p. 5]. The fitted curves indicate that DIFF Transformer is scalable in terms of parameter count [p. 5]. According to the fitted curves, 6.8B-size DIFF Transformer achieves a validation loss comparable to 11B-size Transformer, requiring only 62.2% of parameters [p. 5]. Similarly, 7.8B-size DIFF Transformer matches the performance of 13.1B-size Transformer, requiring only 59.5% of parameters [p. 5].

## Scaling Training Tokens [p. 5]

As shown in Figure 3b, the authors evaluate the 3B language models (as presented in Appendix B) every 40B tokens (i.e., 10K steps) up to a total of 360B tokens (i.e., 90K steps) [p. 5]. The fitted curves indicate that DIFF Transformer trained with 160B tokens achieves comparable performance as Transformer trained with 251B tokens, consuming only 63.7% of the training tokens [p. 5].

**Figure 3** (p. 5): "Language modeling loss of scaling up parameter count and training tokens. DIFF Transformer requires only about 65% of model size or training tokens to match Transformer's performance."

Description: Two line plots showing scaling curves
- **(a) Scaling model size ranging from 830M to 13B:**
  - X-axis: #Parameters (B) on log scale from 10⁰ to 10¹
  - Y-axis: Loss from 2.90 to 3.15
  - Two curves: Transformer (black) and Diff (Ours) (orange)
  - Annotation: "38% Fewer Params" at the convergence point
  - Both curves decrease as parameters increase, with Diff consistently lower
- **(b) Scaling number of training tokens for 3B models:**
  - X-axis: #Tokens (B) on log scale from 2⁶ to 2⁹
  - Y-axis: Loss from 2.5 to 2.9
  - Two curves: Transformer (black) and Diff (Ours) (orange)
  - Annotation: "36% Fewer Tokens" at the convergence point
  - Both curves decrease as tokens increase, with Diff consistently lower
- Supports claim: DIFF Transformer achieves comparable performance with significantly fewer parameters (62.2%) and training tokens (63.7%) [p. 5]
