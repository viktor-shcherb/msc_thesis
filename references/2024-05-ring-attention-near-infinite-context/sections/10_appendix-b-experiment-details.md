# B Experiment Details [p. 14]

## B.1 Evaluation of context length

[p. 14] In the experimental results presented in Section 5.1, the authors used fully sharded tensor parallelism (FSDP) to partition the model across GPUs or TPU devices. The evaluation focused on determining the maximum achievable sequence length in commonly used FSDP training scenarios. For TPUs, they utilized the default training configuration, which involved performing matmul operations in `bfloat16` format with weight accumulation in `float32`. On the other hand, for GPUs, they adopted the default setup, where all operations were performed in `float32`.

## B.2 Evaluation of MFU

[p. 14] In the evaluation presented in Section 5.2, the batch size in tokens is 2 million per batch on GPU and 4 million per batch on TPU. The training was conducted using FSDP [11] with Jax SPMD. For gradient checkpointing [5], they used `nothing_saveable` as checkpointing policies for attention and feedforward network (FFN).

## B.3 Evaluation on line retrieval

[p. 14] In the evaluation presented in Section 5.4, the authors finetuned the LLaMA-13B model [36], limiting context length to 512K tokens due to constraints on cloud compute budget. The training was conducted on 32x A100 80GB Cloud GPUs. They use user-shared conversations gathered from ShareGPT.com with its public APIs for finetuning, following methodologies as outlined in prior works [6, 13]. ShareGPT is a website where users can share their ChatGPT conversations. To ensure data quality, they convert the HTML back to markdown and filter out some inappropriate or low-quality samples, which results in 125K conversations after data cleaning.
