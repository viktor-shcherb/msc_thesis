# B Models and Implementation [p. 16]

[p. 16] This section describes the details of the authors' implementation. The code is primarily written in JAX and FLAX. Specific details about certain implementations of models are noted. The authors plan to release hyperparameters in a form of readme or script later.

## B.1 A Brief Overview of Model Implementations [p. 16]

[p. 16] While most of the fine-grained details is planned to be available in the released code, the authors provide a brief overview of some settings of the xformer models being evaluated:

- **Local Attention:** overlapping blocks are not used.
- **Sinkhorn Transformer:** local attention within Sinkhorn Transformer blocks does not use overlapping windows either.
- **Linformers:** the projections are shared between key and values but not across multiple layers.
- **Performer:** the implementation uses FAVOR+, the more recent version in the paper Choromanski et al. (2020b).

## B.2 Special Cases of our Implementation [p. 16]

[p. 16] This section describes several special cases in the implementation details. The diverse suite of Transformers come with a plethora of hardware constraints and implementation details. To succeed, a Transformer model needs to also 'win' the hardware lottery (Hooker, 2020), i.e., having readily supported ops, kernels or accelerator support to take advantage of its technical design. This section discusses some of the trade-offs and edge cases that make comparison of several models challenging. The authors argue that simplicity is a virtue and not requiring any special support is a positive thing for an efficient Transformer model.

**On CUDA kernels:** CUDA kernels are cumbersome and are specific to GPU hardware, making it difficult to implement or use on TPU pods. Generally, these are considered to be undesirable and inconvenient in practical applications. Hence, Sparse Transformer and Longformer are implemented with **equivalent** implementations to emulate for performance. This is done by applying an equivalent mask. For this reason, Sparse Transformer and Longformer are not benchmarked for speed.

**Reformer's Implementation:** Having optimized ops to support many of Reformer's functionality is crucial. Hence, Reformer is implemented slightly differently from other Transformer models. Instead of computing tensors with batch size dimensions B and head dimensions H, (i.e., B x H x N x d), the attention function is computed for tensors of N x d dimensions. After which, this function is parallelized via VMAP over the batch and head dimensions.
