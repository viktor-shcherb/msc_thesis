# 8. Future Work [p. 26-27]

[p. 26]

This paper lays out a simplified architecture, improved training procedures, and a study of how sparse models scale. However, there remain many open future directions which the authors briefly describe:

1. **Training stability for the largest models.** A significant challenge is further improving training stability for the largest models. While the stability techniques were effective for Switch-Base, Switch-Large and Switch-C models (no observed instability), they were not sufficient for Switch-XXL. Early steps towards stabilizing these models have been taken, which the authors think may be generally useful for large models, including using regularizers for improving stability and adapted forms of gradient clipping, but this remains unsolved.

2. **Upstream to downstream transfer.** Generally, improved pre-training quality leads to better downstream results (Appendix E), though striking anomalies are sometimes encountered. For instance, despite similar perplexities modeling the C4 data set, the 1.6T parameter Switch-C achieves only an 87.7 exact match score in SQuAD, which compares unfavorably to 89.6 for the smaller Switch-XXL model. One notable difference is that the Switch-XXL model applies approximately 10x the FLOPS per token than the Switch-C model, even though it has approximately 4x less unique parameters (395B vs 1.6T). This suggests a poorly understood dependence between fine-tuning quality, *FLOPS per token* and *number of parameters*.

3. **Scaling relationships.** Perform a comprehensive study of scaling relationships to guide the design of architectures blending data, model and expert-parallelism. Ideally, given the specs of a hardware configuration (computation, memory, communication) one could more rapidly design an optimal model. And, vice versa, this may also help in the design of future hardware.

4. **Heterogeneous experts.** The authors' approach always used identical, homogeneous experts, but future designs (facilitated by more flexible infrastructure) could support *heterogeneous* experts. This would enable more flexible adaptation by routing to larger experts when more computation is desired -- perhaps for harder examples.

5. **Expert layers outside the FFN.** Investigating expert layers outside the FFN layer of the Transformer. Preliminary evidence is found that this similarly can improve model quality. In Appendix A, quality improvement is reported when adding expert layers inside Self-Attention layers, where the layer replaces the weight matrices which produce Q, K, V. However, due to training instabilities with the bfloat16 format, this is instead left as an area for future work. [p. 26-27]

6. **New and different modalities.** Examining Switch Transformer in new and across different modalities. The authors have thus far only considered language, but believe that model sparsity can similarly provide advantages in new modalities, as well as multi-modal networks. [p. 27]

The authors note this list could easily be extended, but hope it gives a flavor for the types of challenges they are thinking about and what they suspect are promising future directions. [p. 27]
