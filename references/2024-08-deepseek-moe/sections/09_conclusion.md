# 9. Conclusion [p. 24]

[p. 24] In this paper, the authors introduce the DeepSeekMoE architecture for MoE language models, with the objective of achieving ultimate expert specialization. Through fine-grained expert segmentation and shared expert isolation, DeepSeekMoE achieves significantly higher expert specialization and performance compared with prevailing MoE architectures.

**Validation at 2B scale:** Starting with a modest scale of 2B parameters, the authors validate the advantages of DeepSeekMoE, demonstrating its capability to approach the upper bound performance for MoE models. Furthermore, they provide empirical evidence to show that DeepSeekMoE has a higher level of expert specialization than GShard.

**Scaling to 16B:** Scaling up to a larger scale of 16B total parameters, DeepSeekMoE 16B is trained on 2T tokens and demonstrates its outstanding performance comparable with DeepSeek 7B and LLaMA2 7B, with only about 40% of computations. Additionally, supervised fine-tuning for alignment is conducted to construct an MoE chat model based on DeepSeekMoE 16B, further showing its adaptability and versatility.

**Preliminary 145B exploration:** Further, a preliminary exploration to scale DeepSeekMoE to 145B parameters is performed. DeepSeekMoE 145B still keeps substantial advantages over the GShard architecture, and demonstrates comparable performance with DeepSeek 67B, using only 28.5% (maybe even 18.2%) of computations.

**Model release:** For research purposes, the authors release the model checkpoint of DeepSeekMoE 16B to the public, which can be deployed on a single GPU with 40GB of memory. They aspire for this work to provide valuable insights for both academia and industry, and contribute to the accelerated advancement of large-scale language models.
