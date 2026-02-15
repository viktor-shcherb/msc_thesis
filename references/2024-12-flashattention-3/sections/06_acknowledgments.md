# Acknowledgments [p. 12]

[p. 12] We are grateful to the NVIDIA CUTLASS team (especially Haicheng Wu, Aniket Shivam, and Cris Cecka) for helping us understand Hopper's programming model and for their library, which provides clean and powerful building blocks for the implementation of FLASHATTENTION-3.

[p. 12] We thank the cuDNN team for the idea of kernel transpose for FP8. The idea of overlapping GEMMs and softmax was inspired by insightful conversations with Christopher Re, Benjamin Spector, Aniket Shivam, and Markus Hoehnerbach.

[p. 12] The pingpong scheduling is adapted from the warp-specialized pingpong GEMM implementation in CUTLASS.

[p. 12] We appreciate Driss Guessous for integrating FLASHATTENTION to PyTorch.

[p. 12] FLASHATTENTION-3 has benefited from helpful discussions with Horace He on different attention variants, with Hao Liu and Phil Wang on distributed attention, and with Daniel Haziza and Chris De Sa on quantization.

[p. 12] We thank Meta, Together AI, and Princeton Language and Intelligence (PLI) for compute support.
