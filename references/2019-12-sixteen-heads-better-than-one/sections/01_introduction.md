# 1 Introduction [p. 1-2]

[p. 1] Transformers (Vaswani et al., 2017) have shown state of the art performance across a variety of NLP tasks, including machine translation (Vaswani et al., 2017; Ott et al., 2018), question answering (Devlin et al., 2018), text classification (Radford et al., 2018), and semantic role labeling (Strubell et al., 2018). Central to the Transformer's architectural improvements is the extension of the standard attention mechanism (Bahdanau et al., 2015; Cho et al., 2014) via multi-headed attention (MHA), where attention is computed independently by $N_h$ parallel attention mechanisms (heads). It has been shown that beyond improving performance, MHA can help with subject-verb agreement (Tang et al., 2018) and that some heads are predictive of dependency structures (Raganato and Tiedemann, 2018). Several extensions to the general methodology have been proposed (Ahmed et al., 2017; Shen et al., 2018).

[p. 2] However, it is still not entirely clear what the multiple heads buy us. The paper makes the surprising observation that -- in both Transformer-based models for machine translation and BERT-based (Devlin et al., 2018) natural language inference -- most attention heads can be individually removed after training without any significant downside in terms of test performance (Section 3.2). Remarkably, many attention layers can even be individually reduced to a single attention head without impacting test performance (Section 3.3).

Based on this observation, the authors propose a simple algorithm that greedily and iteratively prunes away attention heads that seem to be contributing less to the model. By jointly removing attention heads from the entire network (not restricted to a single layer), they find that large parts of the network can be removed with little to no consequences, but that the majority of heads must remain to avoid catastrophic drops in performance (Section 4). This has significant benefits for inference-time efficiency, resulting in up to a **17.5% increase in inference speed** for a BERT-based model.

Further analysis reveals that encoder-decoder attention layers are particularly sensitive to pruning, much more than self-attention layers, suggesting that multi-headedness plays a critical role in this component (Section 5). The authors also provide evidence that the distinction between important and unimportant heads increases as training progresses, suggesting an interaction between multi-headedness and training dynamics (Section 6).

## Contributions (stated)

1. Observation that most attention heads can be individually removed at test time without significantly impacting performance.
2. Many layers can be individually reduced to a single attention head.
3. A greedy iterative pruning algorithm for jointly removing heads across the entire network.
4. Up to 17.5% inference speed increase for BERT-based model.
5. Analysis showing encoder-decoder attention is more sensitive to pruning than self-attention.
6. Precursory evidence that training dynamics play a role in the gains provided by multi-head attention.
