# D Compute and inference details [p. 13]

[p. 13] The authors use the Huggingface Transformers package with the two models: Tulu-2-7B and Vicuna-7B-v1.5-16k, both containing 7B parameters. They run the experiments with two NVIDIA A100 GPUs. The inference time is roughly 1 to 3 hours on both datasets. They run the experiments with all greedy decoding without any non-deterministic factor, so they only need to run the experiments for once. Their method is a pure inference method, so there is no need to do training or hyperparameter searching.
