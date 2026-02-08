# 3. Scaling Properties [p. 11-14]

[p. 11]

The authors present a study of the *scaling properties* of the Switch Transformer architecture during pre-training. Per Kaplan et al. (2020), they consider a regime where the model is not bottlenecked by either the computational budget or amount of data. To avoid the data bottleneck, they use the large C4 corpus with over 180B target tokens (Raffel et al., 2019) and train until diminishing returns are observed.

The number of experts is the most efficient dimension for scaling the model. Increasing the experts keeps the computational cost approximately fixed since the model only selects one expert per token, regardless of the number of experts to choose from. The router must compute a probability distribution over more experts, however, this is a lightweight computation of cost O(d_model x num experts) where d_model is the embedding dimension of tokens passed between the layers. In this section, the scaling properties are considered on a step-basis and a time-basis with a fixed computational budget.

## 3.1 Scaling Results on a Step-Basis [p. 12]

[p. 12]

Figure 4 demonstrates consistent scaling benefits with the number of experts when training all models for a fixed number of steps. A clear trend is observed: when keeping the FLOPS per token fixed, having more parameters (experts) speeds up training. The left figure demonstrates consistent scaling properties (with fixed FLOPS per token) between sparse model parameters and test loss. This reveals the advantage of scaling along this additional axis of sparse model parameters. The right figure measures sample efficiency of a dense model variant and four FLOP-matched sparse variants. Increasing the number of experts leads to more sample efficient models. The Switch-Base 64 expert model achieves the same performance of the T5-Base model at step 60k at step 450k, which is a ~7.5x speedup in terms of step time. In addition, consistent with the findings of Kaplan et al. (2020), larger models are also more *sample efficient* -- learning more quickly for a fixed number of observed tokens.

**Figure 4** (p. 12): "Scaling properties of the Switch Transformer. Left Plot: We measure the quality improvement, as measured by perplexity, as the parameters increase by scaling the number of experts. The top-left point corresponds to the T5-Base model with 223M parameters. Moving from top-left to bottom-right, we double the number of experts from 2, 4, 8 and so on until the bottom-right point of a 256 expert model with 14.7B parameters. Despite all models using an equal computational budget, we observe consistent improvements scaling the number of experts. Right Plot: Negative log perplexity per step sweeping over the number of experts. The dense baseline is shown with the purple line and we note improved sample efficiency of our Switch-Base models."

- Left plot: x-axis is "Sparse Model Parameters" (log scale, from ~10^9 to ~10^10), y-axis is "Test Loss" (ranging from ~4.8 to ~6.2). Data points labeled 1e, 2e, 4e, 8e, 16e, 32e, 64e, 128e, 256e show a smooth decrease in test loss as the number of experts (and thus sparse parameters) increases. The top-left point (1e) corresponds to the T5-Base model with 223M parameters; the bottom-right point (256e) is a 14.7B parameter model.
- Right plot: x-axis is "Training Step" (0 to 5 x 10^5), y-axis is "Neg Log Perplexity" (from -2.0 to -1.2). Lines for Switch-Base: 128e, 64e, 32e, 16e, and T5-Base are shown. All Switch-Base models achieve better (more negative) log perplexity than the T5-Base, with more experts yielding better performance and improved sample efficiency. Switch-Base: 128e reaches roughly -2.0 while T5-Base reaches roughly -1.5.

## 3.2 Scaling Results on a Time-Basis [p. 13]

[p. 13]

Figure 4 demonstrates that on a step basis, as the number of experts increases, performance consistently improves. While the models have roughly the same amount of FLOPS per token as the baseline, the Switch Transformers incur additional communication costs across devices as well as the extra computation of the routing mechanism. Therefore, the increased sample efficiency observed on a step-basis does not necessarily translate to a better model quality as measured by wall-clock. This raises the question:

> "*For a fixed training duration and computational budget, should one train a dense or a sparse model?*" [p. 13]

Figures 5 and 6 address this question. Figure 5 measures the pre-training model quality as a function of time. For a fixed training duration and computational budget, Switch Transformers yield a substantial speed-up. In this setting, the Switch-Base 64 expert model trains in *one-seventh* the time that it would take the T5-Base to get similar perplexity.

**Figure 5** (p. 13): "Speed advantage of Switch Transformer. All models trained on 32 TPUv3 cores with equal FLOPs per example. For a fixed amount of computation and training time, Switch Transformers significantly outperform the dense Transformer baseline. Our 64 expert Switch-Base model achieves the same quality in *one-seventh* the time of the T5-Base and continues to improve."

- x-axis is "Training Time" (from ~25 to ~350 hours), y-axis is "Neg Log Perplexity" (from -2.0 to -1.2). Lines for Switch-Base: 128e, 64e, 32e, and T5-Base are shown. A double-headed arrow labeled "7x Speedup" spans the horizontal gap between the T5-Base curve and the Switch-Base: 64e curve at approximately -1.6 perplexity. All Switch models significantly outperform T5-Base at every point in training time.

## 3.3 Scaling Versus a Larger Dense Model [p. 13-14]

[p. 13-14]

The above analysis shows that a computationally-matched dense model is outpaced by its Switch counterpart. Figure 6 considers a different scenario: what if the resources were instead allocated to a larger dense model? The authors measure Switch-Base against the next strong baseline, *T5-Large*. But despite T5-Large applying 3.5x more FLOPs per token, Switch-Base is still more sample efficient and yields a 2.5x speedup. Furthermore, more gains can be had simply by designing a new, larger sparse version, Switch-Large, which is FLOP-matched to T5-Large. The authors demonstrate superior scaling and fine-tuning in the following section.

**Figure 6** (p. 14): "Scaling Transformer models with Switch layers or with standard dense model scaling. Left Plot: Switch-Base is more sample efficient than both the T5-Base, and T5-Large variant, which applies 3.5x more FLOPS per token. Right Plot: As before, on a wall-clock basis, we find that Switch-Base is still faster, and yields a 2.5x speedup over T5-Large."

- Left plot: x-axis is "Training Step" (0 to 5 x 10^5), y-axis is "Neg Log Perplexity" (from -2.0 to -1.2). Lines for Switch-Base: 64e, T5-Large, and T5-Base are shown. Switch-Base: 64e is consistently below (better than) both T5-Large and T5-Base throughout training, demonstrating superior sample efficiency.
- Right plot: x-axis is "Training Time" (from ~50 to ~350 hours), y-axis is "Neg Log Perplexity" (from -2.0 to -1.2). Lines for Switch-Base: 64e, T5-Large, and T5-Base are shown. Double-headed arrows indicate "2.5x Speedup" (Switch-Base: 64e vs. T5-Large) and "7.0x Speedup" (Switch-Base: 64e vs. T5-Base). Switch-Base: 64e is faster than both dense baselines on a wall-clock basis.
