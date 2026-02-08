# 6 Infrastructure, Scaling, and Efficiency [p. 52–56]

[p. 52] The training of the Apertus collection of models was enabled by Alps, a leading supercomputing infrastructure operated by the Swiss National Supercomputing Centre (CSCS). The paper details the architectural features of the Machine Learning Platform and the engineering contributions that facilitated this release.

## 6.1 Infrastructure

### 6.1.1 The Alps Research Infrastructure [p. 52]

[p. 52] The Alps Research Infrastructure at CSCS is an HPE Cray EX system with a measured HPL performance of 434 PFlops (fp64), placing it in the top 10 most powerful supercomputers globally.

Architecturally, Alps is designed so that resources operate as independent endpoints within a global high-speed network. This design addresses the limitations of traditional, vertically integrated HPC architectures by providing greater flexibility and composability.

Hardware infrastructure:
- 10,752 NVIDIA Grace-Hopper (GH200) GPUs (four per node)
- Interconnected by a Slingshot-11 network with 200 Gb/s injection bandwidth per GPU
- Storage: 100 PB ClusterStor HDD system and a 3 PB ClusterStor SSD system, both using the Lustre file system, plus a 1 PB VAST storage system

Additional details are outlined in Martinasso et al. (2025); Schuppli et al. (2025).

Alps uses a versatile software-defined cluster (vCluster) technology, which bridges cloud and HPC paradigms. This technology abstracts infrastructure, service management, and user environments into distinct layers, facilitating the deployment of independent, tenant-specific, and platform-specific services.

### 6.1.2 The Machine Learning Platform [p. 52]

[p. 52] The Machine Learning (ML) platform within the Alps Research Infrastructure is specifically designed to meet the evolving computational demands of AI and Machine Learning workloads, particularly for the Swiss AI Initiative. During the Apertus training runs, this platform leveraged a dedicated vCluster with approximately 1,500 NVIDIA Grace-Hopper (GH200) nodes (with 4 GPUs each) of the Alps system. This vCluster, named Clariden, ensures robust performance and scalability for training advanced AI models, including large language models (LLMs), and supports long-duration jobs. It is explicitly engineered to diverge from traditional HPC offerings, addressing specific challenges observed since its early access phase in 2023 (Schuppli et al., 2025).

A container-first approach is fundamental to the ML platform's design, streamlining the user experience and enhancing application portability. The platform provides an environment that closely mirrors existing setups for users familiar with container-based workflows and vendor-curated images (e.g., PyTorch, JAX), minimizing the need for extensive HPC-specific knowledge. This is facilitated by the Container Engine (CE) toolset, which runs Linux application containers on HPC resources in a seamless manner, incorporating Open Container Initiative (OCI) hooks and Container Device Interface (CDI) specifications for performance optimization. Users define their software environments concisely using TOML-based Environment Definition Files (EDF), promoting autonomy and rapid integration of custom dependencies (Cruz & Madonna, 2024).

[p. 52–53] To enhance the reliability and efficiency of large-scale ML training, the platform incorporates a node-vetting and early-abort system. This system dynamically verifies the readiness of allocated compute nodes through lightweight, rapid diagnostic tests just prior to job execution. These tests are designed to identify transient issues such as high GPU temperature, insufficient memory, "dirty" GPU states, or network congestion that could otherwise degrade performance or cause job failures. The results are centrally collected, providing shared operational intelligence to improve the overall reliability of the system.

[p. 53] The pretraining and finetuning workloads of the Apertus models represent the first and most significant computational workload executed so far on the Alps Research Infrastructure, running, for the 70B model, at scales from 2048 to 4096 GPUs over several months. The vCluster technology brought an operational flexibility unusual in HPC systems: critical updates could be applied selectively to vClusters serving other communities while being deferred on the nodes dedicated to this campaign, and the ML engineering team itself could roll out node-level changes without depending on system engineering colleagues. Crucially, this work demonstrated that even amid these technological advancements, Alps delivered stable, well-scaling performance for cutting-edge large models pretraining.

## 6.2 Full Training Run Performance [p. 53]

[p. 53] A detailed timeline showing token throughput performance over the pretraining runs of the 70B and 8B Apertus models is displayed in Figure 11. Training of the 70B model for 15T tokens took 6.74 x 10^24 FLOPs (details in Appendix E). In terms of usage, the main run consumed around 6 million GPU hours, though this is underestimated as it does not count loading weights or overhead due to initial performance shortcomings, failures, or downtime.

Once a production environment has been set up, the model can be realistically trained in approximately 90 days on 4096 GPUs, accounting for overheads. Assuming 560 W power usage per Grace-Hopper module in this period, below the set power limit of 660 W, an estimated 5 GWh power usage for the compute of the pretraining run is obtained. CSCS is almost carbon neutral, relying entirely on hydropower, and uses a sustainable cooling system that uses water from Lake Lugano in a closed cycle, with all the water returned to the lake and none consumed.^51

^51: https://www.cscs.ch/science/computer-science-hpc/2022/at-cscs-energy-efficiency-is-a-key-priority-even-at-high-performance

**Figure 11** (p. 53): "Token Throughput During Training. Left panel: 70B parameter model, Right panel: 8B model"
- Left panel (70B): X-axis is Consumed Tokens (0.0T to 15.0T), Y-axis is Tokens Per Second Per GPU (ranging ~500–800). Throughput is variable, mostly in the 600–750 range, with several annotated dashed vertical lines marking data phase transitions. Notable dips occur early and around mid-training.
- Right panel (8B): X-axis is Consumed Tokens (0.0T to 15.0T), Y-axis is Tokens Per Second Per GPU (ranging ~4000–7000). Throughput is more stable, generally around 6000–7000, with similar annotated data phase transitions. A significant drop occurs around 10T–12.5T tokens consumed.

## 6.3 Engineering Challenges and Solutions [p. 53–56]

[p. 53] Training the Apertus model required careful, coordinated engineering across the entire software stack at CSCS and close collaboration with the SwissAI researchers. CSCS engineers systematically tuned software, hardware, and operational layers to optimize a stable and highly-performant training pipeline capable of sustaining large-scale LLM training on 1024 nodes (4096 GPUs) with predictable convergence behavior. The following sections describe the key areas where improvements were made and the impact is illustrated in Figure 12.

### 6.3.1 Systems-level Fixes [p. 54]

**Figure 12** (p. 54): "Throughput of the 70B Apertus Pretraining on 2048 GPUs Before and after Stability Improvements. Top: Runs prior to stability tuning show high variability, largely driven by poor filesystem I/O before migrating to full-flash storage, and an NVIDIA driver issue related to access counter-based memory page migration. Bottom: Performance after stability enhancements, exhibiting consistent throughput with predictable dips corresponding to Python garbage collection and checkpointing. Residual irregular fluctuations are attributable to minor filesystem interference."
- Top panel: X-axis is time (13 Apr 12:00 AM to 14 Apr 12:00 AM), Y-axis is Tokens/second/GPU (0–800). Throughput is highly variable, frequently dropping to near 0 with intermittent recovery to ~600.
- Bottom panel: X-axis is time (11 May 12:00 AM to 12 May 12:00 AM), Y-axis is Tokens/second/GPU (0–800). Throughput is much more stable around ~600, with only brief predictable dips.

[p. 54] The ALPS system relies on the HPE Slingshot 11 interconnect to provide the bandwidth required for large-scale distributed training. To enable efficient communication over this fabric, NCCL operates through the AWS OFI NCCL plugin in conjunction with libfabric. In the early stages, significant performance variability was observed caused by mismatched versions of these components. Aligning the plugin and libfabric versions resolved these inconsistencies, restoring stable communication and eliminating slowdowns during checkpoint restarts.

Several other critical issues were resolved in collaboration with industry partners:
- A GPU driver bug where an access-counter-based page migration caused interrupt storms on certain CPU cores, resulting in unpredictable performance when application threads were scheduled on those cores. As a workaround, the feature was disabled.
- A race condition in the Linux kernel that could be triggered by GPU driver calls, leading to kernel panics and node crashes. A targeted Linux kernel hot patch corrected this problem and substantially improved system stability.
- Transparent huge pages in the Linux kernel negatively affected performance for this workload. A Slurm option was introduced to allow users to disable transparent huge pages when necessary.

[p. 54–55] Another challenge was the GH200 system's unified memory architecture, which combines two different types of memory: LPDDR5 for the CPU and HBM for the GPU. The Linux kernel and various system processes were not designed for this level of heterogeneity and sometimes allocated GPU memory, causing issues for applications that expected exclusive control over it. This was mitigated by explicitly binding many system processes and adding extra parameters to kernel calls. For example, the memory implicitly allocated by the kernel in tmpfs filesystems, which are not directly constrained by user-space cgroups, was limited. These memory issues were compounded with another problem that resulted in OS file caches not migrating automatically back to CPU memory. This issue can only be fully addressed by a driver update; as an interim solution, the file caches are explicitly flushed and a Slurm prolog script verifies at least 90% of GPU memory can be allocated before a compute node is added to an allocation.

Together, these fixes removed major sources of instability and allowed large jobs to run for their full allocation without interruption.

### 6.3.2 Stability and Container Robustness [p. 55]

[p. 55] Ensuring the stability of the software environment was a major focus. One issue stemmed from Triton's JIT kernel caches, which were originally stored on the distributed filesystem. This design introduced contention and, in some cases, race conditions across nodes that led to software crashes. By moving these caches to in-memory storage on each node, race conditions were eliminated and overall stability improved.

Container-level library compatibility posed another challenge. Early training runs were based on NGC 25.01, which contained a libnvrtc bug that caused sporadic crashes. The fix was present in later container releases, but dependencies on a specific PyTorch version in NGC 25.01 prevented an immediate upgrade. To address this, a custom container was built that included an updated version of libnvrtc, and once dependencies stabilized, it was possible to transition to NGC 25.03.

### 6.3.3 Checkpointing and Restart Strategies [p. 55]

[p. 55] Checkpointing is critical for fault tolerance, especially when operating at scale. Storage usage was optimized by placing datasets and caches on high-IOPS SSD storage, which accommodates small, random reads; checkpoint files, which involve large sequential writes, were stored on high-capacity HDDs. The frequency of checkpointing (every 250 iterations) was determined using the Young/Daly formula, balancing checkpoint overhead (a few seconds) against expected mean time between failures (MTBF, a few hours) to minimize lost work and downtime. These strategies reduced the cost of restarts and ensured that long training runs could progress reliably even in the event of node failures.

To ensure continuous execution of the training process, each job submitted the next job to the queue once a basic initialization check completed successfully, indicating that the job would proceed seamlessly. The Slurm sbatch configuration flag `--dependency=singleton` was leveraged, which enforces that only one job with the same name and user can run simultaneously. To avoid wasting compute resources, the `--signal` option was employed to send a SIGUSR2 signal a few minutes before the job's time limit, ensuring sufficient time to store a checkpoint and terminate gracefully.

### 6.3.4 Performance Optimizations at Scale [p. 55]

[p. 55] Beyond stability and resilience, targeted performance optimizations were introduced to maximize efficiency:

- **NVIDIA vBoost:** Enabled through a custom Slurm option. This adjustment trades off chip memory power to give it to the cores, thus increasing GPU clock frequencies while remaining within power budgets. LLM workloads benefit from this as they are typically compute-bound, not memory-bound.
- **NCCL collective consolidation:** Identified periods during training that involved numerous small collective operations. By adjusting Megatron's distributed data parallel bucket size, many small NCCL collectives were consolidated into fewer, larger messages. This significantly reduced communication latency and improved training performance during communication-heavy phases.
- **Scaling to 1024 nodes:** Made possible with two key modifications to the model parallelism: (1) removing delayed computation of the embedding gradients that caused spurious training metrics late in pretraining, assumed to be a Megatron issue, and (2) increasing virtual pipelining within model-parallel groups to optimize communication patterns.
- **Container loading:** To speed up loading the container image, nearly 20 GB in size, effectively at scale, Lustre striping had to be properly set for these files.

### 6.3.5 Operational Efficiency and Monitoring [p. 56]

[p. 56] Improving operational resilience was essential for reducing downtime and maximizing system utilization. A dedicated Slurm partition was created for large-scale jobs, ensuring resource availability for restarts and minimizing scheduling delays. Additional nodes were allocated to these partitions so that, in the event of hardware failure, spare capacity was immediately available. The queue time limits were extended to 48 hours to accommodate large jobs that required longer execution windows. Downtime was minimized with automated exit triggers, signal handling, and continuous monitoring tools to detect and respond to anomalies quickly.

### 6.3.6 Scaling and Parallel Efficiency [p. 56]

**Figure 13** (p. 56): "Scaling of the Apertus 70B model. Strong scaling parallel efficiency, with the global batch size held constant at 16.8 M tokens, is shown with blue circles. Weak scaling parallel efficiency is shown with green squares, where the global batch size varies from 0.13 M to 16.8 M tokens with increasing GPU count."
- X-axis: Number of GPUs (32 to 4096, log scale)
- Y-axis: Parallel Efficiency (0.0 to 1.4)
- Strong scaling (blue circles): Starts near 1.0 at 32 GPUs and remains relatively flat, declining to approximately 0.8 at 4096 GPUs.
- Weak scaling (green squares): Remains close to 1.0 across the range, with slight fluctuations, and shows approximately 0.85 at 4096 GPUs.

[p. 56] The parallel efficiency of the training was characterized with strong and weak scaling experiments. Both experiments used a global batch size (GBS) of 16.8 M tokens (sequence length 4096) at target scale of 4096 GPUs, and training runs ranged from 8 nodes (32 GPUs) to 1024 nodes (4096 GPUs).

- **Strong scaling:** GBS was constant at 16.8 M tokens across all GPU counts, with 8 nodes (32 GPUs) being the smallest resource with sufficient memory for this experiment.
- **Weak scaling:** GBS ranged from 0.13 M to 16.8 M tokens (32 to 4096 sequences, i.e. proportional to the number of GPUs used).

The result is shown in Figure 13, with ultimately 80% strong scaling parallel efficiency at 4096 GPUs. The performance at this scale is 723 tokens per second per GPU.
