# 9 Limitations [p. 9]

[p. 9]

Several limitations are acknowledged:

1. **Linear attention limits recall over long contexts:** The linear attention of RWKV leads to significant efficiency gains but still, it may also limit the model's performance on tasks that require recalling minutiae information over very long contexts. This is due to the funneling of information through a single vector representation over many time steps, compared with the full information maintained by the quadratic attention of standard Transformers. The model's recurrent architecture inherently limits its ability to "look back" at previous tokens, as opposed to traditional self-attention mechanisms. While learned time decay helps prevent the loss of information, it is mechanistically limited compared to full self-attention.

2. **Increased importance of prompt engineering:** Another limitation is the increased importance of prompt engineering in comparison to standard Transformer models. The linear attention mechanism used in RWKV limits the information from the prompt that will be carried over to the model's continuation. As a result, carefully designed prompts may be even more crucial for the model to perform well on tasks. This was confirmed by studies on prompt engineering presented in Appendix L. By changing the order of the information pieces, the authors were even able to almost double the RWKV performance for some tasks.
