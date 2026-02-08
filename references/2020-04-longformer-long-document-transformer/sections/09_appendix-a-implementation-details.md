# A Implementation Details [p. 13]

[p. 13] Implementing Longformer's dilated sliding window attention requires a form of banded matrix multiplication (matrix multiplication where the output is all zero except certain diagonals) that is not directly supported in existing deep learning libraries like PyTorch/TensorFlow. Fig. 1 compares the runtime and memory of three different ways of implementing it.

## Longformer-loop

[p. 13] `Longformer-loop` is a naive implementation that computes each diagonal separately in a loop. It is memory efficient because it only computes the non-zero values, but it is unusably slow. Only used for testing because it is easy to implement but not used to run experiments.

## Longformer-chunks

[p. 13] `Longformer-chunks` only supports the non-dilated case. It chunks Q and K into overlapping blocks of size w and overlap of size 1/2 * w, multiplies the blocks, then masks out the diagonals. This is very compute efficient because it uses a single matrix multiplication operation from PyTorch, but it consumes 2x the memory a perfectly optimized implementation should consume because it computes some of the zero values. Because of the compute efficiency, this implementation is most suitable for the pretrain/finetune case. The authors did not find the increase in memory to be a problem for this setting.

## Longformer-cuda

[p. 13] `Longformer-cuda` is a custom CUDA kernel implemented using TVM (Chen et al., 2018). It is a fully functioning implementation of the attention (not limited as `Longformer-chunks`), it is the most memory efficient, and it is as fast as the highly optimized full self-attention.^10 Mainly used for the autoregressive language modeling experiments because of the memory efficiency (allows the longest sequences) and the support of dilation (needed for character-LM experiments).

^10 It is worth noting that theoretically, a perfectly optimized `Longformer-cuda` should be faster than the n^2 computation. However, achieving this level of performance requires special knowledge of low-level GPU programming, similar to implementing a highly optimized matrix multiplication. The current implementation is sufficiently fast and practical to use. [p. 13, footnote 10]

## Tensor Virtual Machine (TVM)

[p. 13] The custom CUDA kernel is built using TVM (Chen et al., 2018), a deep learning compiler stack that compiles high level description of a function into optimized device-specific code. Using TVM, the banded matrix multiplication is described in high-level python constructs, then TVM generates the corresponding CUDA code and compiles it for GPUs.

## CUDA Kernel Features

[p. 13] The CUDA kernel supports the autoregressive mode where each token attends to a window of previous tokens only. The implementation also includes a version of the relative position embedding that is compatible with the dilated sliding window attention.
