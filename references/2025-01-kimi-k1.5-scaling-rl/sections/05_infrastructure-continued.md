# 2.6 Infrastructure (continued) [p. 11]

## 2.6.3 Checkpoint Transfer (continued) [p. 11]

It could be challenging to entirely release GPU memory by vLLM offloading primarily due to CUDA graphs, NCCL buffers and NVIDIA drivers. To minimize modifications to vLLM, the authors terminate and restart it when needed for better GPU utilization and fault tolerance.

The worker in Megatron converts the owned checkpoints into the Hugging Face format in shared memory. This conversion also takes Pipeline Parallelism and Expert Parallelism into account so that only Tensor Parallelism remains in these checkpoints. Checkpoints in shared memory are subsequently divided into shards and registered in the global metadata system. The authors employ Mooncake to transfer checkpoints between peer nodes over RDMA. Some modifications to vLLM are needed to load weight files and perform tensor parallelism conversion.

## 2.6.4 Code Sandbox [p. 11]

The authors developed the sandbox as a secure environment for executing user-submitted code, optimized for code execution and code benchmark evaluation. By dynamically switching container images, the sandbox supports different use cases through MultiPL-E (Cassano, Gouwar, D. Nguyen, S. Nguyen, et al. 2023), DMOJ Judge Server, Lean, Jupyter Notebook, and other images.

For RL in coding tasks, the sandbox ensures the reliability of training data judgment by providing consistent and repeatable evaluation mechanisms. Its feedback system supports multi-stage assessments, such as code execution feedback and repo-level editing, while maintaining a uniform context to ensure fair and equitable benchmark comparisons across programming languages.

The service is deployed on Kubernetes for scalability and resilience, exposing it through HTTP endpoints for external integration. Kubernetes features like automatic restarts and rolling updates ensure availability and fault tolerance.

### Performance Optimizations [p. 11]

To optimize performance and support RL environments, several techniques are incorporated into the code execution service to enhance efficiency, speed, and reliability:

- **Using Crun:** The authors utilize crun as the container runtime instead of Docker, significantly reducing container startup times.
- **Cgroup Reusing:** Pre-created cgroups for container use, which is crucial in scenarios with high concurrency where creating and destroying cgroups for each container can become a bottleneck.
- **Disk Usage Optimization:** An overlay filesystem with an upper layer mounted as tmpfs is used to control disk writes, providing a fixed-size, high-speed storage space. This approach is beneficial for ephemeral workloads.

**Performance comparison** [p. 11]:

| Method   | Container Startup Time (s) | Max Containers/sec (16-core machine) |
|----------|---------------------------|-------------------------------------|
| Docker   | 0.12                      | 27                                  |
| Sandbox  | 0.04                      | 120                                 |

The sandbox achieves 3× faster container startup times (0.04s vs 0.12s) and 4.4× higher throughput (120 vs 27 containers/second) compared to Docker [p. 11].

These optimizations improve RL efficiency in code execution, providing a consistent and reliable environment for evaluating RL-generated code, essential for iterative training and model improvement.
