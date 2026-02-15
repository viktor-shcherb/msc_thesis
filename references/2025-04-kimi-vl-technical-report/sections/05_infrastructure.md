# 2.5 Infrastructure [p. 7]

## Storage [p. 7]

We utilize S3 (Amazon Web Services, 2023) compatible object storage from cloud service vendors to store our visual text data. To minimize the time between data preparation and model training, we store visual data in its original format and have developed an efficient data loading system. This system provides several key benefits:

- Supports on-the-fly data shuffling, mixing, tokenization, loss masking and packing during training, allowing us to adjust data proportions as needed;
- Enables random augmentation of both visual and text data, while preserving the correctness of 2D coordinate and orientation information during transformations;
- Ensures reproducibility by strictly controlling random states and other states across different data loader workers, guaranteeing that any interrupted training can be resumed seamlessly—the data sequence after resumption remains identical to an uninterrupted run;
- Delivers high-performance data loading: through multiple caching strategies, our system reliably supports training on large-scale clusters while maintaining controlled request rate and throughput to the object storage.

Additionally, to ensure consistent dataset quality control, we developed a centralized platform for data registration, visualization, compiling statistics, synchronizing data across cloud storage systems, and managing dataset lifecycles.

## Parallelism [p. 7]

We employ a hybrid of 4D parallelism strategies—Data Parallelism (J. Li et al. 2020), Expert Parallelism (Fedus et al. 2022), Pipeline Parallelism (Y. Huang et al. 2019; Narayanan et al. 2021), and Context Parallelism (Jacobs et al. 2023; H. Liu et al. 2023)—to accelerate the speed of Kimi-VL. After optimizing parallel strategies, the resulting training throughput of our model is around 60% higher than a 7B dense VLM (e.g. VLMs based on Qwen2.5-7B).

- **Data Parallelism (DP).** DP replicates the model across multiple devices, each processing different micro-batches. This setup allows larger effective batch sizes by simply increasing the number of devices.
- **Expert Parallelism (EP).** EP distributes the MoE layer across multiple devices. When combined with DP, experts on a given device can handle tokens from different DP groups, enhancing computational efficiency.
- **Pipeline Parallelism (PP).** PP splits the model into multiple layer-based stages. To minimize pipeline bubbles, we allocate the Vision Tower (VT) and additional decoder layers to the first stage, place the output layer and additional decoder layers in the last stage, and distribute the remaining decoder layers evenly across intermediate stages based on their time overhead.
- **Context Parallelism (CP).** CP addresses long-sequence training by splitting sequences across different CP ranks in conjunction with flash attention (Dao et al. 2022). This substantially reduces peak memory usage and relieves the memory pressure from attention computations.

Beyond these four parallel strategies, we incorporate ZeRO1 (Rajbhandari et al. 2020) and Selective Checkpointing Activation (T. Chen et al. 2016; Korthikanti et al. 2022) to further optimize memory usage. ZeRO1 reduces optimizer state overhead by using a distributed optimizer while avoiding extra communication costs. Selective Checkpointing Activation trades time for space by recomputing only those layers that have low time overhead but high memory consumption, striking a balance between computation efficiency and memory demands. For extremely long sequences, we expand recomputation to a broader set of layers to prevent out-of-memory errors.
