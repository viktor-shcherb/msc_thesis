# 5 Conclusion [p. 5]

Language models are expensive for inference primarily due to the memory bandwidth overhead from loading keys and values. Multi-query attention reduces this overhead at the cost of decreased model capacity and quality. The authors propose to convert multi-head attention models to multi-query models with a small fraction of original pre-training compute. Moreover, they introduce grouped-query attention, an interpolation of multi-query and multi-head attention that achieves quality close to multi-head at comparable speed to multi-query attention. [p. 5]

## Limitations [p. 5]

- This paper focuses on ameliorating the memory bandwidth overhead from loading keys and values. This overhead is most important when generating longer sequences, for which quality is inherently difficult to evaluate. [p. 5]
- For summarization, Rouge score is employed, which the authors acknowledge is a flawed evaluation that does not tell the whole story; for that reason, it is difficult to be certain the trade-offs are correct. [p. 5]
- Due to limited computation, the XXL GQA model is not compared to a comparative model trained from scratch, so the relative performance of uptraining vs training from scratch is not known. [p. 5]
- The impact of uptraining and GQA is evaluated only on encoder-decoder models. Recently, decoder-only models are extremely popular, and since these models do not have separate self-attention and cross-attention, the authors expect GQA to have a stronger advantage over MQA. [p. 5]
