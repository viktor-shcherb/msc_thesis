# 5 Limitations and Future Directions [p. 10]

[p. 10]

## Compiling to CUDA

The current approach to building IO-aware implementations of attention requires writing a new CUDA kernel for each new attention implementation. This requires writing the attention algorithm in a considerably lower-level language than PyTorch, and requires significant engineering effort. Implementations may also not be transferrable across GPU architectures. These limitations suggest the need for a method that supports writing attention algorithms in a high-level language (e.g., PyTorch), and compiling to IO-aware implementations in CUDA -- similar to efforts such as Halide in image processing [70].

## IO-Aware Deep Learning

> "We believe that the IO-aware approach can extend beyond attention." [p. 10]

Attention is the most memory-intensive computation in Transformers, but every layer in a deep network touches GPU HBM. The authors hope their work inspires IO-aware implementations of additional modules. Potential extensions are discussed in Appendix D.

## Multi-GPU IO-Aware Methods

The IO-aware implementation of attention is optimal within constants for computing attention on a single GPU. However, the attention computation may be parallelizable across multiple GPUs [72]. Using multiple GPUs adds an additional layer to IO analysis -- accounting for data transfer between GPUs. The authors hope their work inspires future work in this direction.
