# 7. Discussion [p. 25-26]

[p. 25]

The authors pose and discuss questions about the Switch Transformer, and sparse expert models generally, where sparsity refers to weights, not attention patterns.

**Isn't Switch Transformer better due to sheer parameter count?** Yes, and by design. Parameters, independent of the total FLOPs used, are a useful axis to scale neural language models. Large models have been exhaustively shown to perform better (Kaplan et al., 2020). But in this case, the model is more sample efficient and faster while using the same computational resources.

**I don't have access to a supercomputer -- is this still useful for me?** Though this work has focused on extremely large models, the authors also find that models with as few as two experts improves performance while easily fitting within memory constraints of commonly available GPUs or TPUs (details in Appendix D). They therefore believe their techniques are useful in small-scale settings.

**Do sparse models outperform dense models on the speed-accuracy Pareto curve?** Yes. Across a wide variety of different model sizes, sparse models outperform dense models per step and on wall clock time. Controlled experiments show that for a fixed amount of computation and time, sparse models outperform dense models.

**I can't deploy a trillion parameter model -- can we shrink these models?** The model quality cannot be fully preserved, but compression rates of 10 to 100x are achievable by distilling sparse models into dense models while achieving approximately 30% of the quality gain of the expert model.

**Why use Switch Transformer instead of a model-parallel dense model?** On a time basis, Switch Transformers can be far more efficient than dense-models with sharded parameters (Figure 6). Also, this decision is *not* mutually exclusive -- one can, and does, use model-parallelism in Switch Transformers, increasing the FLOPs per token, but incurring the slowdown of conventional model-parallelism.

[p. 26]

**Why aren't sparse models widely used already?** The motivation to try sparse models has been stymied by the massive success of scaling dense models (the success of which is partially driven by co-adaptation with deep learning hardware as argued in Hooker (2020)). Further, sparse models have been subject to issues including (1) model complexity, (2) training difficulties, and (3) communication costs. Switch Transformer makes strides to alleviate these issues.
