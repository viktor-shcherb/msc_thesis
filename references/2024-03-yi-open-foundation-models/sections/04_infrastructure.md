# 4 Infrastructure [p. 7–9]

The infrastructure supports the full-stack data processing, pretraining, finetuning, and serving. Infrastructure features: [p. 7]

1. Automated managing and monitoring the computing resource
2. Improved the training speed from optimized parallel strategies, kernel efficiency, and long-context support
3. Unified finetuning framework supporting heterogeneous distributed training backend, such as simultaneously using Megatron and DeepSpeed for multiple models in Direct Preference Optimization (DPO) [59]
4. Reducing the deployment cost by various LLM serving accelerations such as quantization, continuous batching, and paged attention

## Computing Resources Management

[p. 7–8]

To efficiently schedule large-scale language model development, particularly pretraining which may take months on thousands of GPUs, a highly efficient multi-cloud task scheduling algorithm is built to manage pre-training, SFT, and RLHF tasks of different priorities. A high-performance in-house training framework is also built that allows automatically elastic scaling of the pre-train jobs to different node sizes based on the GPU availability. All the training-related hyper-parameters are scaled at the same time seamlessly. [p. 7]

During the large language model training stage, a wide range of failures regularly occur, ranging from GPU crashes to communication fabric errors to loss spikes. The following strategies address these reliability challenges: [p. 8]

1. Automated inspection, prediction, and labeling of nodes for different kinds of software/hardware error categories. Nodes marked as tainted are temporarily removed from the resource pool until the errors are cleared.
2. A task queuing system with pre-checks and the capability for fast, automatic recovery in the event of failures during training tasks.
3. A user-friendly multi-task submission and management console, enabling developers to seamlessly manage and track their training tasks and hyper-parameters.

## Performance and Cost Efficiency

[p. 8]

*Memory* and *communication* restrictions are the two major technical challenges of large scale model training requiring integrated solutions beyond adding more GPUs. The following techniques are used to tackle the memory and communication restrictions:

1. ZeRO-1 [60] to remove the memory consumption by partitioning optimizer states cross data-parallel processes
2. Tensor parallel combined with pipeline parallel [70] within each compute node to avoid inter-node communication bottleneck, and the 3D parallel strategy is well designed and optimized to avoid using activation checkpointing and minimize the pipeline bubbles
3. Kernel fusion techniques like flash attention [15][14] and JIT kernels to reduce redundant global memory access and consumption
4. Topology-aware resource allocation (ranking strategy) to minimize the communication across different layers of switches, which is the limitation of a typical fat-tree-topology

## Finetuning Framework

[p. 8]

Different from pretraining, finetuning LLMs may require the orchestration of multiple models, as is the practice of DPO [59] and PPO [54]. In such training jobs, a typical process is to use reference/reward model to predict a batch of data (which also requires nontrivial time), then let the target model use this data to calculate loss and update parameters. A multi-model scheduling framework is built to support multiple backends for different LLMs in a single job. For example, when finetuning a language model with DPO, the intermediate results from the reference model can be cached and reused, improving the training speed and resource cost to be close to the supervised finetuning counterparts.

## Fast and Efficient Inference

[p. 8]

Primarily use quantization, dynamic batching, and Paged Attention for improving decoding speed and memory usage. Quantization is used to decrease both the memory footprint and computation demand. By 4-bit model quantization [81] and 8-bit KV cache quantization [18], significant GPU memory saving is achieved with near-zero performance degradation (e.g., less than 1% accuracy drop in MMLU/CMMLU benchmark). Dynamic batching [86] is used to minimize the response time and improve batching efficiency. PagedAttention [41] is used to improve memory utilization and improve decoding.

## Long-context Window Support

[p. 9]

Computation-communication overlapping, sequence parallelism, and communication compression are implemented and improved to support up to 200K context length for continued pretraining and finetuning. The method to scale the context length to 200K is *solely* based on engineering -- the model architecture is not modified (no sparse, local, or sliding window attention). The model remains using full attention even when the input is 200K.
