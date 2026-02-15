# 3.3 Long-Context Evaluation [p. 5]

The authors extend the 3B-size language models (described in Appendix B) to 64K context length [p. 5]. They continue training the 3B checkpoints for additional 1.5B tokens [p. 5]. Most hyperparameters are kept the same as in Section 3.1 [p. 5]. The learning rate is 8e-5 [p. 5]. The RoPE (Su et al., 2021) θ is increased to 640,000 [p. 5]. The training corpus is up-sampled according to sequence length (Fu et al., 2024) [p. 5].

## Results [p. 5]

Figure 4 presents cumulative average negative log-likelihood (NLL) of the tokens at varying positions (Reid et al., 2024), where lower NLL indicates better performance [p. 5]. The evaluation is conducted on book data within 64K length [p. 5]. The authors observe a consistent decrease in NLL as the context length increases [p. 5]. DIFF Transformer achieves lower NLL values than Transformer [p. 5]. The results demonstrate that DIFF Transformer can effectively leverage the increasing context [p. 5].

**Figure 4** (p. 5): "Cumulative average negative log-likelihood (lower is better) on book data. DIFF Transformer leverages long context more effectively."

Description: Line plot showing NLL over sequence positions
- X-axis: Sequence Position from 100 to 100K (log scale)
- Y-axis: Negative Log-Likelihood
- Two curves: Transformer (black) and Diff (Ours) (orange)
- Both curves show decreasing trend as sequence position increases
- Diff (Ours) consistently shows lower NLL values than Transformer across all positions
- Notable gap between the two models throughout the sequence
- Supports claim: DIFF Transformer effectively leverages increasing context, achieving lower NLL values consistently [p. 5]
