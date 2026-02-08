# 4 Results [p. 6]

[p. 6]

The authors first show that on WikiText-103, ALiBi is efficient and enables training models with short input subsequences that outperform strong baselines even when the ALiBi models extrapolate to more than six times the number of tokens that they were trained on. They then take the same hyperparameters for their method (the set of slopes) that worked on WikiText-103 and show that -- with no modification -- they provide strong results on a dataset in a very different domain: books. Finally, they show that a 1.3B parameter model trained with ALiBi on a much larger (461 GB) dataset with much more compute provides a superior alternative to the sinusoidal method since it achieves similar perplexity scores while running faster and using less memory (since it is trained on shorter inputs). [p. 6]

While multiple alternatives to the position methods presented in Vaswani et al. (2017) have been proposed, few have been adopted in large (1B or more parameter) LMs since that setting is much more challenging than the smaller scale experiments. GPT-3 and Jurassic-1 (Lieber et al., 2021) use the learned position embedding method from Vaswani et al., and GPT-J uses the rotary method. The results on the 1.3B parameter model show the method's ability to generalize to larger models, dataset sizes and training durations without retuning the hyperparameter. [p. 6]

## 4.1 Results on WikiText-103 and Toronto BookCorpus [p. 6]

## Figure 4

**Figure 4** (p. 6): "ALiBi models trained and evaluated on varying sequence lengths on the WikiText-103 validation set and the sinusoidal baseline (not evaluated on longer sequences). All of our models outperform the sinusoidal ones even when trained on fewer tokens. Appendix Table 5 has exact perplexities, more ALiBi models (trained on fewer tokens), and results for rotary and T5 bias models."

The figure shows a line plot titled "ALiBi Extrapolating on WikiText-103":
- x-axis: Validation Input Length ($L_{valid}$), values: 512, 1024, 1536, 2048, 3072
- y-axis: Perplexity (17.0 to 21.0)
- Lines shown for ALiBi at $L = 512, 1024, 1536, 2048, 3072$ (dashed lines with various markers, showing extrapolation to longer lengths)
- Square markers for Sinusoidal at $L = 512, 1024, 1536, 2048, 3072$ (each evaluated only at its own training length, no extrapolation)
- Key observation: All ALiBi models outperform the sinusoidal ones even when trained on fewer tokens. ALiBi $L = 512$ evaluated at $L_{valid} = 3072$ achieves lower perplexity than Sinusoidal $L = 512$ evaluated at $L_{valid} = 512$. Perplexity generally decreases (improves) as $L_{valid}$ increases for ALiBi models, with the curves flattening around $L_{valid} = 2048$-$3072$.

[p. 6]

The method is first developed on the WikiText-103 corpus (Merity et al., 2016), replacing the sinusoidal position embeddings in the language model of Baevski & Auli (2018) with ALiBi. [p. 6]

Figure 4 (and the corresponding Appendix Table 5) show results for models trained with varying numbers of input subsequence tokens ($L$), extrapolating to longer subsequence lengths on the validation dataset. The first observation is that, without extrapolation, for every $L$, the ALiBi models outperform those using the sinusoidal method, sometimes by a significant amount. For example, the Baevski & Auli model achieves $18.67 \pm 0.24$ (std. dev.) perplexity when trained with $L = 3072$ input tokens, but the ALiBi $L = 3072$ model achieves 17.60 perplexity (when both models evaluate with $L_{valid} = 3072$). [p. 6]

---
[p. 7 continued]

The second observation is that all ALiBi models can extrapolate, and they obtain improved perplexity scores when handling more tokens than they observed during training. For example, the model trained on 512 tokens (which achieves 19.73 perplexity when evaluating subsequences of length 512 in the development set) achieves a perplexity score of 18.40 on the development set when extrapolating to subsequences of length 3072. Surprisingly, this surpasses the score that the $L = 3072$ sinusoidal model obtains on the development set by a statistically significant margin. All ALiBi models trained on $L = 512$ to $L = 2048$ outperform the sinusoidal baseline trained on $L = 3072$ when extrapolating to $L_{valid} = 3072$ even though those models all take much less time to train since they train on shorter subsequences (Appendix Figure 8 compares training speed to perplexity for these models). The $L = 512$ model is 1.84 times faster to train and yet still outperforms the $L = 3072$ sinusoidal model when extrapolating to $L_{valid} = 3072$. In addition, training the $L = 3072$ sinusoidal model requires a GPU with more than 16 GB of memory to fit the large attention matrices, which the $L = 512$ ALiBi model outperforms even though it can be trained on a GPU with much less memory due to much smaller attention matrices. [p. 7]

Additionally, Table 5 (in the appendix) also shows that, for $L$s of 1024 and 3072, the ALiBi method performs better than the rotary and T5 bias models even when $L_{valid} = L$ (i.e., no extrapolation is occurring). Figure 1 (and the corresponding Appendix Tables 2 and 3) more broadly explore the ALiBi method vs. the other position methods. They show that the T5 bias (the best of the baselines) improves perplexity until $L_{valid}$ is around $2L$, but on the WikiText-103 dataset the ALiBi method continually improves perplexity until at least around $3L$, with the $L = 512$ model improving perplexity even when $L_{valid}$ exceeds 12k tokens. Even when unable to improve perplexity given longer sequences, ALiBi always maintains strong performance as more tokens are added. [p. 7]

Appendix Table 6 shows that the results on the validation set also transfer to the test set of WikiText-103. Currently, almost all models that present results on WikiText-103 use sliding window evaluation (defined in Section B) to compute perplexities. The authors apply that method to their (and to the sinusoidal, rotary and T5 bias) models in Appendix Table 7. They find that their $L = 3072$ model surpasses the performance of Transformer-XL (Dai et al., 2019), the Sandwich (Press et al., 2020), and Shortformer (Press et al., 2021) models. The results are similar to the ones obtained with staged training (Press et al., 2021) but fall short of results obtained by Routing Transformer (Roy et al., 2020) and kNN-LM (Khandelwal et al., 2020). The methods used in those models are orthogonal to ALiBi, and the authors hypothesize that combining them with theirs might lead to even larger performance increases. [p. 7]

After developing their method on WikiText-103, in Appendix Section A.3, they run one set of experiments on a different domain (books) using a similar model architecture and without modifying any of the ALiBi hyperparameters (the slopes) and show that the results fully transfer to this new domain. The ALiBi models are able to both surpass the sinusoidal baseline when not extrapolating while also outperforming it when extrapolating to longer sequences. [p. 7]

## 4.2 Results on the CC100+RoBERTa Corpus [p. 7-9]

[p. 7]

The final set of experiments investigates whether ALiBi transfers to a larger model trained with a larger computational budget on a larger dataset than the ones previously used. The authors show that ALiBi achieves strong results in this more challenging setting, obtaining similar performance to the sinusoidal baseline while using significantly less memory, since they train on shorter subsequences. [p. 7]

The dataset chosen is a combination of the datasets used to train the RoBERTa (Liu et al., 2019) implementation of BERT (Devlin et al., 2019) and the English part of the CC-100 corpus introduced in Conneau et al. (2020), for a total of 461 GB. The RoBERTa training corpus -- i.e., the Toronto Book Corpus (Zhu et al., 2015), English Wikipedia, CC-News (Nagel, 2016), OpenWebText (Gokaslan & Cohen, 2019) and Stories (Trinh & Le, 2018) -- is 161 gigabytes, and the English part of the CC-100 corpus is 300 gigabytes. The validation set contains 649K tokens. [p. 7]

Model details for this dataset:
- 25 transformer layers
- 16 heads
- Dimension of 2048
- 8192 hidden dimension of the feedforward sublayers
- 1.3B parameters
- Trained for one epoch, which is 50k updates
- 128 V100 GPUs [p. 7]

## Figure 5

**Figure 5** (p. 8): "On the left (right), a 1.3B-parameter ALiBi model trained on 512 (1024) tokens during training, compared to the sinusoidal baseline trained on 1024 (2048) tokens. The ALiBi models obtain strong results even though they use 6%-11% less memory since they train on shorter sequences. Appendix Table 11 shows memory use and end-of-training perplexities."

Two side-by-side plots:
- **Left panel:** "Validation Perplexity Through Training with $L_{valid}$ = 1024." x-axis: Training Time (GPU Hours), 0 to 6000; y-axis: Perplexity (8.5 to 11.0). Two curves: Sinusoidal $L = 1024$ (orange squares) and ALiBi $L = 512$ (blue dots). Both start high (~11.0) and decrease. The ALiBi $L = 512$ curve tracks close to the Sinusoidal $L = 1024$ curve throughout training, despite training on shorter sequences.
- **Right panel:** "Validation Perplexity Through Training with $L_{valid}$ = 2048." x-axis: Training Time (GPU Hours), 0 to 6000; y-axis: Perplexity (8.5 to 11.0). Two curves: Sinusoidal $L = 2048$ (orange squares) and ALiBi $L = 1024$ (blue dots). Similar pattern: the ALiBi model with half the training length tracks close to the sinusoidal model, using less memory.

[p. 8]

In Figure 5 (left), the validation perplexity for $L_{valid} = 1024$ is compared throughout the training process for an ALiBi model trained with $L = 512$ compared to the sinusoidal model trained with $L = 1024$. Since the ALiBi model is trained on shorter sequences, it is 7% faster and uses 1.6 GB less memory. The authors halt training of the sinusoidal baseline when the ALiBi model reaches the end of its training (one epoch). At that time, the ALiBi model is just 0.06 perplexity away from the baseline even though it was trained on sequences that are half the length of those the baseline used and requires less memory. [p. 8]

In Figure 5 (right), results become even more impressive, showing that the ALiBi model trained on $L = 1024$ outperforms by 0.09 perplexity the sinusoidal model trained on $L = 2048$ (when evaluating with $L_{valid} = 2048$) even though the ALiBi model uses 3.1 GB less memory. The ALiBi model maintains a lead in perplexity over the sinusoidal model during the entire training process. By sampling five evenly distributed points across the training process, the authors compute that the $L = 1024$ ALiBi model reaches a given perplexity value, on average, 11% faster than the sinusoidal model does. [p. 8]

Since the ALiBi models in these comparisons use much less memory, they allow for stacking more layers, which would further improve performance (with negligible, if any, runtime cost). To keep the experiments as straightforward as possible, however, the authors do not add layers to their models. [p. 8]

Appendix Table 12 presents additional results comparing the ALiBi models to the sinusoidal baseline when both are trained on the same $L$, showing that ALiBi performs similarly to the sinusoidal baseline when not extrapolating. This contrasts with the results presented on the smaller datasets, where ALiBi consistently outperforms other position methods even when not extrapolating, suggesting that ALiBi's inductive bias provides additional benefits for lower-resource language modeling. [p. 8]

## Figure 6

**Figure 6** (p. 8): "The ALiBi and sinusoidal models (with both $L = 512$ and 1024) trained for 50k updates (1 epoch) on the CC100+RoBERTa corpus, extrapolating on the validation set. ALiBi achieves the best results at around $2L$ but maintains strong performance even up to 10000 tokens in these experiments."

Two side-by-side plots:
- **Left panel:** "Extrapolation, $L = 512$ on CC100+RoBERTa." x-axis: Validation Input Length ($L_{valid}$), 512 to 10000; y-axis: Perplexity (8.6 to 10.2). Two curves: Sinusoidal (green/yellow circles) and ALiBi (blue triangles). The Sinusoidal curve rises sharply immediately past 512. The ALiBi curve decreases from ~9.8 at 512 to a minimum of ~9.3 around 1012 tokens, then gradually rises but stays below ~9.5 even at 10000.
- **Right panel:** "Extrapolation, $L = 1024$ on CC100+RoBERTa." x-axis: Validation Input Length ($L_{valid}$), 1024 to 10000; y-axis: Perplexity (8.6 to 10.2). Two curves: Sinusoidal (green/yellow circles) and ALiBi (blue triangles). Similar pattern: Sinusoidal degrades immediately past 1024. ALiBi achieves its best around 2024 tokens (~8.9) then gradually rises.

[p. 8-9]

Figure 6 shows that the ALiBi models trained on $L = 512$ and $L = 1024$ achieve the best results when extrapolating to about double the tokens that they were trained on. Specifically, the $L = 512$ model (that obtains 9.79 perplexity when $L_{valid} = 512$) achieves its best score (9.3) when extrapolating to 1012 tokens, and the $L = 1024$ model (that obtains 9.16 perplexity when $L_{valid} = 1024$) achieves its best score (8.9) when extrapolating to 2024 tokens. [p. 8-9]

One possible explanation is that the subsequences the model observes during training are up to $L$ tokens long. When performing inference on subsequences of length $2L$, half of the subsequences the model consumes are as long as the examples seen during training. When inference is performed on subsequences of length $2L + 1$ or longer, less than half of the predictions the model makes are on subsequences of lengths seen during training, and that might degrade performance. [p. 9]

The sinusoidal model cannot extrapolate at all in this setting, with its performance degrading for both the $L = 512$ and 1024 models as soon as one token more than $L$ is added during evaluation. [p. 9]

In Appendix B, the authors find that ALiBi's edge over sinusoidal embeddings is largely explained by its improved avoidance of the early token curse. They posit that future work building on ALiBi might achieve further gains by more efficiently exploiting longer histories. [p. 9]
