# 3 Pre-Training [p. 4-6]

[p. 4] Language model pre-training involves: **(1)** the curation and filtering of a large-scale training corpus, **(2)** the development of a model architecture and corresponding scaling laws for determining model size, **(3)** the development of techniques for efficient pre-training at large scale, and **(4)** the development of a pre-training recipe. Each component is presented separately below.

## 3.1 Pre-Training Data [p. 4-6]

[p. 4] The dataset for language model pre-training is created from a variety of data sources containing knowledge until the end of 2023. Several de-duplication methods and data cleaning mechanisms are applied on each data source to obtain high-quality tokens. Domains containing large amounts of personally identifiable information (PII) and domains with known adult content are removed.

### 3.1.1 Web Data Curation [p. 4-6]

[p. 4] Much of the data utilized is obtained from the web. The cleaning process is described below.

**PII and safety filtering.** Among other mitigations, filters are implemented to remove data from websites that are likely to contain unsafe content or high volumes of PII, domains that have been ranked as harmful according to a variety of Meta safety standards, and domains that are known to contain adult content. [p. 4]

[p. 5] **Text extraction and cleaning.** Raw HTML content from non-truncated web documents is processed to extract high-quality diverse text. A custom parser is built that extracts the HTML content and optimizes for precision in boilerplate removal and content recall. The parser's quality is evaluated in human evaluations, comparing it with popular third-party HTML parsers that optimize for article-like content, and found to perform favorably. HTML pages with mathematics and code content are carefully processed to preserve structure. Image alt attribute text is maintained since mathematical content is often represented as pre-rendered images with math in the alt attribute. Markdown is found experimentally to be harmful to the performance of a model primarily trained on web data compared to plain text, so all markdown markers are removed. [p. 5]

**De-duplication.** Several rounds of de-duplication are applied at the URL, document, and line level: [p. 5]

- **URL-level de-duplication.** URL-level de-duplication across the entire dataset. The most recent version for pages corresponding to each URL is kept.
- **Document-level de-duplication.** Global MinHash (Broder, 1997) de-duplication across the entire dataset to remove near duplicate documents.
- **Line-level de-duplication.** Aggressive line-level de-duplication similar to ccNet (Wenzek et al., 2019). Lines that appeared more than 6 times in each bucket of 30M documents are removed. Manual qualitative analysis showed that the line-level de-duplication removes not only leftover boilerplate from various websites such as navigation menus, cookie warnings, but also frequent high-quality text; however, empirical evaluations showed strong improvements. [p. 5]

**Heuristic filtering.** Heuristics are developed to remove additional low-quality documents, outliers, and documents with excessive repetitions. Examples include: [p. 5]

- Duplicated n-gram coverage ratio (Rae et al., 2021) to remove lines consisting of repeated content such as logging or error messages. Those lines could be very long and unique, hence cannot be filtered by line-dedup.
- "Dirty word" counting (Raffel et al., 2020) to filter out adult websites not covered by domain block lists.
- Token-distribution Kullback-Leibler divergence to filter out documents containing excessive numbers of outlier tokens compared to the training corpus distribution. [p. 5]

**Model-based quality filtering.** Various model-based quality classifiers are applied to sub-select high-quality tokens. These include: [p. 5]

- Fast classifiers such as fasttext (Joulin et al., 2017) trained to recognize if a given text would be referenced by Wikipedia (Touvron et al., 2023a).
- More compute-intensive Roberta-based classifiers (Liu et al., 2019a) trained on Llama 2 predictions.
- A quality classifier based on Llama 2: a training set of cleaned web documents is created, quality requirements are described, and Llama 2's chat model is instructed to determine if documents meet these requirements.
- DistilRoberta (Sanh et al., 2019) is used to generate quality scores for each document for efficiency reasons. Various quality filtering configurations are experimentally evaluated. [p. 5]

**Code and reasoning data.** Similar to DeepSeek-AI et al. (2024), domain-specific pipelines are built to extract code and math-relevant web pages. Both the code and reasoning classifiers are DistilRoberta models trained on web data annotated by Llama 2. Unlike the general quality classifier, prompt tuning is used to target web pages containing math deduction, reasoning in STEM areas, and code interleaved with natural language. Since the token distribution of code and math is substantially different from natural language, these pipelines implement domain-specific HTML extraction, customized text features, and heuristics for filtering. [p. 5]

**Multilingual data.** Similar processing pipelines for English are applied, with filters to remove data from websites likely to contain PII or unsafe content. The multilingual text processing pipeline has several unique features: [p. 5-6]

- A fasttext-based language identification model to categorize documents into 176 languages.
- Document-level and line-level de-duplication within data for each language.
- Language-specific heuristics and model-based filters to remove low-quality documents. [p. 5-6]

[p. 6] Quality ranking of multilingual documents is performed using a multilingual Llama 2-based classifier to ensure high-quality content is prioritized. The amount of multilingual tokens used in pre-training is determined experimentally, balancing model performance on English and multilingual benchmarks. [p. 6]

### 3.1.2 Determining the Data Mix [p. 6]

[p. 6] To obtain a high-quality language model, it is essential to carefully determine the proportion of different data sources in the pre-training data mix. The main tools for determining the data mix are knowledge classification and scaling law experiments.

**Knowledge classification.** A classifier is developed to categorize the types of information in web data to more effectively determine a data mix. This classifier is used to downsample data categories that are over-represented on the web, for example, arts and entertainment. [p. 6]

**Scaling laws for data mix.** Scaling law experiments are performed in which several small models are trained on a data mix and used to predict the performance of a large model on that mix (see Section 3.2.1). This process is repeated multiple times for different data mixes to select a new data mix candidate. Subsequently, a larger model is trained on this candidate data mix and performance is evaluated on several key benchmarks. [p. 6]

**Data mix summary.** The final data mix contains roughly 50% of tokens corresponding to general knowledge, 25% of mathematical and reasoning tokens, 17% code tokens, and 8% multilingual tokens. [p. 6]

### 3.1.3 Annealing Data [p. 6]

[p. 6] Empirically, annealing (see Section 3.4.3) on small amounts of high-quality code and mathematical data can boost the performance of pre-trained models on key benchmarks. Akin to Li et al. (2024b), annealing is performed with a data mix that upsamples high-quality data in select domains. Training sets from commonly used benchmarks are not included in the annealing data, to assess the true few-shot learning capabilities and out-of-domain generalization of Llama 3. [p. 6]

Following OpenAI (2023a), the efficacy of annealing is evaluated on the GSM8k (Cobbe et al., 2021) and MATH (Hendrycks et al., 2021b) training sets in annealing. Annealing improved the performance of a pre-trained Llama 3 8B model on the GSM8k and MATH validation sets by 24.0% and 6.4%, respectively. However, the improvements on the 405B model are negligible, suggesting that the flagship model has strong in-context learning and reasoning capabilities and does not require specific in-domain training samples to obtain strong performance. [p. 6]

**Using annealing to assess data quality.** Similar to Blakeney et al. (2024), annealing enables judging the value of small domain-specific datasets. The value of such datasets is measured by annealing the learning rate of a 50% trained Llama 3 8B model linearly to 0 on 40B tokens. In those experiments, 30% weight is assigned to the new dataset and the remaining 70% weight to the default data mix. Using annealing to evaluate new data sources is more efficient than performing scaling law experiments for every small dataset. [p. 6]

## 3.2 Model Architecture [p. 6]

[p. 6] Llama 3 uses a standard, dense Transformer architecture (Vaswani et al., 2017). It does not deviate significantly from Llama and Llama 2 (Touvron et al., 2023a,b) in terms of model architecture; performance gains are primarily driven by improvements in data quality and diversity as well as by increased training scale.

A few small modifications compared to Llama 2: [p. 6]

- Grouped query attention (GQA; Ainslie et al. (2023)) with 8 key-value heads is used to improve inference speed and reduce the size of key-value caches during decoding.
- An attention mask is used that prevents self-attention between different documents within the same sequence. This change had limited impact during standard pre-training, but is found to be important in continued pre-training on very long sequences.

---
[p. 7 continued]

- A vocabulary with 128K tokens is used. The token vocabulary combines 100K tokens from the tiktoken^3 tokenizer with 28K additional tokens to better support non-English languages. Compared to the Llama 2 tokenizer, the new tokenizer improves compression rates on a sample of English data from 3.17 to 3.94 characters per token. This enables the model to "read" more text for the same amount of training compute. Adding 28K tokens from select non-English languages improved both compression ratios and downstream performance, with no impact on English tokenization. [p. 7]

  ^3 https://github.com/openai/tiktoken/tree/main

- The RoPE base frequency hyperparameter is increased to 500,000. This enables better support for longer contexts; Xiong et al. (2023) showed this value to be effective for context lengths up to 32,768. [p. 7]

[p. 7] Llama 3 405B uses an architecture with 126 layers, a token representation dimension of 16,384, and 128 attention heads; see Table 3 for details. This leads to a model size that is approximately compute-optimal according to scaling laws on the data for the training budget of 3.8 x 10^25 FLOPs.

### Table 3 [p. 7]

**Table 3: Overview of the key hyperparameters of Llama 3.** Settings for 8B, 70B, and 405B language models.

|                       | 8B             | 70B            | 405B           |
|-----------------------|----------------|----------------|----------------|
| Layers                | 32             | 80             | 126            |
| Model Dimension       | 4,096          | 8,192          | 16,384         |
| FFN Dimension         | 14,336         | 28,672         | 53,248         |
| Attention Heads       | 32             | 64             | 128            |
| Key/Value Heads       | 8              | 8              | 8              |
| Peak Learning Rate    | 3 x 10^-4     | 1.5 x 10^-4   | 8 x 10^-5     |
| Activation Function   | SwiGLU         | SwiGLU         | SwiGLU         |
| Vocabulary Size       | 128,000        | 128,000        | 128,000        |
| Positional Embeddings | RoPE (theta = 500,000) | RoPE (theta = 500,000) | RoPE (theta = 500,000) |

### 3.2.1 Scaling Laws [p. 7-8]

[p. 7] Scaling laws are developed (Hoffmann et al., 2022; Kaplan et al., 2020) to determine the optimal model size for the flagship model given the pre-training compute budget. In addition to determining the optimal model size, a major challenge is to forecast the flagship model's performance on downstream benchmark tasks, due to a couple of issues: (1) Existing scaling laws typically predict only next-token prediction loss rather than specific benchmark performance. (2) Scaling laws can be noisy and unreliable because they are developed based on pre-training runs conducted with small compute budgets (Wei et al., 2022b).

To address these challenges, a two-stage methodology is implemented to develop scaling laws that accurately predict downstream benchmark performance: [p. 7]

1. First, a correlation is established between the compute-optimal model's negative log-likelihood on downstream tasks and the training FLOPs.
2. Next, the negative log-likelihood on downstream tasks is correlated with task accuracy, utilizing both the scaling law models and older models trained with higher compute FLOPs. In this step, the Llama 2 family of models is specifically leveraged.

This approach enables predicting downstream task performance given a specific number of training FLOPs for compute-optimal models. A similar method is used to select the pre-training data mix (see Section 3.4). [p. 7]

**Scaling law experiments.** [p. 7] The scaling laws are constructed by pre-training models using compute budgets between 6 x 10^18 FLOPs and 10^22 FLOPs. At each compute budget, models ranging in size between 40M and 16B parameters are pre-trained, using a subset of model sizes at each compute budget. In these training runs, a cosine learning rate schedule with a linear warmup for 2,000 training steps is used. The peak learning rate is set between 2 x 10^-4 and 4 x 10^-4 depending on the size of the model. The cosine decay is set to 0.1 of the peak value. The weight decay at each step is set to 0.1 times the learning rate at that step. A fixed batch size for each compute scale is used, ranging between 250K and 4M. [p. 7]

[p. 8] These experiments give rise to the IsoFLOPs curves in Figure 2. The loss in these curves is measured on a separate validation set. The measured loss values are fit using a second-degree polynomial and the minimums of each parabola are identified. The minimum of a parabola is referred to as the *compute-optimal* model at the corresponding pre-training compute budget.

The compute-optimal models identified this way are used to predict the optimal number of training tokens for a specific compute budget. A power-law relation between compute budget, *C*, and the optimal number of training tokens, *N*(C)*, is assumed:

$$N^*(C) = AC^\alpha$$

*A* and alpha are fit using the data from Figure 2. The result is (alpha, A) = (0.53, 0.29); the corresponding fit is shown in Figure 3. Extrapolation of the resulting scaling law to 3.8 x 10^25 FLOPs suggests training a 402B parameter model on 16.55T tokens. [p. 8]

An important observation is that IsoFLOPs curves become *flatter* around the minimum as the compute budget increases. This implies that performance of the flagship model is relatively robust to small changes in the trade-off between model size and training tokens. Based on this observation, the decision was ultimately made to train a flagship model with 405B parameters. [p. 8]

**Predicting performance on downstream tasks.** [p. 8] The resulting compute-optimal models are used to forecast the performance of the flagship Llama 3 model on benchmark data sets. First, the (normalized) negative log-likelihood of correct answer in the benchmark and the training FLOPs are linearly correlated. In this analysis, only the scaling law models trained up to 10^22 FLOPs on the data mix described above are used. Next, a sigmoidal relation between the log-likelihood and accuracy is established using both the scaling law models and Llama 2 models, which were trained using the Llama 2 data mix and tokenizer. The results of this experiment on the ARC Challenge benchmark are shown in Figure 4. This two-step scaling law prediction, which extrapolates over four orders of magnitude, is found to be quite accurate: it only slightly underestimates the final performance of the flagship Llama 3 model. [p. 8]

### Figure 2 [p. 8]

**Figure 2** (p. 8): "Scaling law IsoFLOPs curves between 6 x 10^18 and 10^22 FLOPs. The loss is the negative log-likelihood on a held-out validation set. We approximate measurements at each compute scale using a second degree polynomial."

The figure shows: Left plot with x-axis "Training Tokens" (log scale, 10^10 to 10^12), y-axis "Validation Loss" (0.70 to 0.95). Multiple IsoFLOPs curves are shown for compute budgets: 6e18, 1e19, 3e19, 6e19, 1e20, 3e20, 6e20, 1e21, 3e21, 1e22. Each curve is approximately parabolic, with the minimum shifting rightward (more tokens) as compute increases. The curves become flatter around their minimums at higher compute budgets.

### Figure 3 [p. 8]

**Figure 3** (p. 8): "Number of training tokens in identified compute-optimal models as a function of pre-training compute budget. We include the fitted scaling-law prediction as well. The compute-optimal models correspond to the parabola minimums in Figure 2."

The figure shows: Plot with x-axis "Compute (FLOPs)" (log scale, 10^18 to 10^22), y-axis "Training Tokens" (log scale, ~10^9 to 10^11). Data points (pink/red diamonds) show the compute-optimal token count at each compute budget. A fitted line (labeled "Fitted Line, alpha = 0.537, A = 0.299") runs through the data, showing a power-law relationship between compute and optimal training tokens.

### Figure 4 [p. 9]

**Figure 4** (p. 9): "Scaling law forecast for ARC Challenge. *Left:* Normalized negative log-likelihood of the correct answer on the ARC Challenge benchmark as a function of pre-training FLOPs. *Right:* ARC Challenge benchmark accuracy as a function of the normalized negative log-likelihood of the correct answer. This analysis enables us to predict model performance on the ARC Challenge benchmark before pre-training commences. See text for details."

The figure shows two plots:
- Left plot: x-axis "Compute (FLOPs)" (log scale, 10^20 to 10^25), y-axis "Normalized NLL per Char." (1.200 to 1.400). Pink diamonds (Scaling Law Models) show decreasing NLL as compute increases, with a fitted curve.
- Right plot: x-axis "Normalized NLL per Char." (1.40 to 1.20, reversed), y-axis "Accuracy" (0.3 to 1.0). Three series are shown: Scaling Law Models (pink diamonds), Llama 2 Models (orange circles), and Scaling Law Prediction (blue triangles, fitted sigmoidal curve). The Llama 3 405B point (blue square) falls near the prediction at ~0.93 accuracy with NLL ~1.20, confirming the scaling law prediction is slightly below the actual performance.

## 3.3 Infrastructure, Scaling, and Efficiency [p. 8-11]

[p. 8] The hardware and infrastructure that powered Llama 3 405B pre-training at scale is described, along with several optimizations that lead to improvements in training efficiency.

### 3.3.1 Training Infrastructure [p. 8-9]

[p. 8] The Llama 1 and 2 models were trained on Meta's AI Research SuperCluster (Lee and Sengupta, 2022). As further scaling was needed, the training for Llama 3 was migrated to Meta's production clusters (Lee et al., 2024). This setup optimizes for production-grade reliability, which is essential as training is scaled up. [p. 8-9]

**Compute.** [p. 9] Llama 3 405B is trained on up to 16K H100 GPUs, each running at 700W TDP with 80GB HBM3, using Meta's Grand Teton AI server platform (Matt Bowman, 2022). Each server is equipped with eight GPUs and two CPUs. Within a server, the eight GPUs are connected via NVLink. Training jobs are scheduled using MAST (Choudhury et al., 2024), Meta's global-scale training scheduler. [p. 9]

**Storage.** [p. 9] Tectonic (Pan et al., 2021), Meta's general-purpose distributed file system, is used to build a storage fabric (Battey and Gupta, 2024) for Llama 3 pre-training. It offers 240 PB of storage out of 7,500 servers equipped with SSDs, and supports a sustainable throughput of 2 TB/s and a peak throughput of 7 TB/s. A major challenge is supporting the highly bursty checkpoint writes that saturate the storage fabric for short durations. Checkpointing saves each GPU's model state, ranging from 1 MB to 4 GB per GPU, for recovery and debugging. The aim is to minimize GPU pause time during checkpointing and increase checkpoint frequency to reduce the amount of lost work after a recovery. [p. 9]

**Network.** [p. 9] Llama 3 405B used RDMA over Converged Ethernet (RoCE) fabric based on the Arista 7800 and Minipack2 Open Compute Project^4 OCP rack switches. Smaller models in the Llama 3 family were trained using Nvidia Quantum2 Infiniband fabric. Both RoCE and Infiniband clusters leverage 400 Gbps interconnects between GPUs. Despite the underlying network technology differences between these clusters, both are tuned to provide equivalent performance for the large training workloads. Further elaboration is on the RoCE network since it is fully owned. [p. 9]

^4 Open Compute Project: https://www.opencompute.org/

- **Network topology.** [p. 9] The RoCE-based AI cluster comprises 24K GPUs^5 connected by a three-layer Clos network (Lee et al., 2024). At the bottom layer, each rack hosts 16 GPUs split between two servers and connected by a single Minipack2 top-of-the-rack (ToR) switch. In the middle layer, 192 such racks are connected by Cluster Switches to form a pod of 3,072 GPUs with full bisection bandwidth, ensuring no oversubscription. At the top layer, eight such pods within the same datacenter building are connected via Aggregation Switches to form a cluster of 24K GPUs. However, network connectivity at the aggregation layer does not maintain full bisection bandwidth and instead has an oversubscription ratio of 1:7. The model parallelism methods (see Section 3.3.2) and training job scheduler (Choudhury et al., 2024) are all optimized to be aware of network topology, aiming to minimize network communication across pods. [p. 9]

  ^5 Note that only up to 16K of these 24K GPUs are used for Llama 3 pre-training.

- **Load balancing.** [p. 9-10] LLM training produces fat network flows that are hard to load balance across all available network paths using traditional methods such as Equal-Cost Multi-Path (ECMP) routing. Two techniques are employed: First, the collective library creates 16 network flows between two GPUs, instead of just one, thereby reducing the traffic per flow and providing more flows for load balancing. Second, the Enhanced-ECMP (E-ECMP) protocol effectively balances these 16 flows across different network paths by hashing on additional fields in the RoCE header of packets. [p. 10]

- **Congestion control.** [p. 10] Deep-buffer switches are used in the spine (Gangidi et al., 2024) to accommodate transient congestion and buffering caused by collective communication patterns. This setup helps limit the impact of persistent congestion and network back pressure caused by slow servers, which is common in training. Better load balancing through E-ECMP significantly reduces the chance of congestion. With these optimizations, a 24K GPU cluster is successfully run without traditional congestion control methods such as Data Center Quantized Congestion Notification (DCQCN). [p. 10]

### 3.3.2 Parallelism for Model Scaling [p. 10-11]

[p. 10] To scale training for the largest models, 4D parallelism is used — a combination of four different types of parallelism methods — to shard the model. This approach efficiently distributes computation across many GPUs and ensures each GPU's model parameters, optimizer states, gradients, and activations fit in its HBM. The implementation of 4D parallelism is illustrated in Figure 5. It combines tensor parallelism (TP; Krizhevsky et al. (2012); Shoeybi et al. (2019); Korthikanti et al. (2023)), pipeline parallelism (PP; Huang et al. (2019); Narayanan et al. (2021); Lamy-Poirier (2023)), context parallelism (CP; Liu et al. (2023a)), and data parallelism (DP; Rajbhandari et al. (2020); Ren et al. (2021); Zhao et al. (2023b)). [p. 10]

Tensor parallelism splits individual weight tensors into multiple chunks on different devices. Pipeline parallelism partitions the model vertically into stages by layers, so that different devices can process in parallel different stages of the full model pipeline. Context parallelism divides the input context into segments, reducing memory bottleneck for very long sequence length inputs. Fully sharded data parallelism (FSDP; Rajbhandari et al., 2020; Ren et al., 2021; Zhao et al., 2023b) is used, which shards the model, optimizer, and gradients while implementing data parallelism which processes data in parallel on multiple GPUs and synchronizes after each training step. The use of FSDP for Llama 3 shards optimizer states and gradients, but for model shards they do not reshard after forward computation to avoid an extra **all-gather** communication during backward passes. [p. 10]

**GPU utilization.** [p. 10] Through careful tuning of the parallelism configuration, hardware, and software, an overall BF16 Model FLOPs Utilization (MFU; Chowdhery et al. (2023)) of 38-43% is achieved for the configurations shown in Table 4. The slight drop in MFU to 41% on 16K GPUs with DP=128 compared to 43% on 8K GPUs with DP=64 is due to the lower batch size per DP group needed to keep the global tokens per batch constant during training. [p. 10]

### Table 4 [p. 10]

**Table 4: Scaling configurations and MFU for each stage of Llama 3 405B pre-training.** See text and Figure 5 for descriptions of each type of parallelism.

| GPUs   | TP | CP | PP | DP     | Seq. Len. | Batch size/DP | Tokens/Batch | TFLOPs/GPU | BF16 MFU |
|--------|----|----|----|---------| ----------|---------------|--------------|------------|----------|
| 8,192  | 8  | 1  | 16 | 64     | 8,192     | 32            | 16M          | 430        | 43%      |
| 16,384 | 8  | 1  | 16 | 128    | 8,192     | 16            | 16M          | 400        | 41%      |
| 16,384 | 8  | 16 | 16 | 8      | 131,072   | 16            | 16M          | 380        | 38%      |

**Pipeline parallelism improvements.** [p. 10] Several challenges with existing pipeline parallelism implementations are encountered:

- **Batch size constraint.** Current implementations have constraints on supported batch size per GPU, requiring it to be divisible by the number of pipeline stages. For the example in Figure 6, the depth-first schedule (DFS) of pipeline parallelism (Narayanan et al., 2021) requires *N* = PP = 4, while the breadth-first schedule (BFS; Lamy-Poirier (2023)) requires *N* = *M*, where *M* is the total number of micro-batches and *N* is the number of contiguous micro-batches for the same stage's forward or backward. However, pre-training often needs flexibility to adjust batch size. [p. 10]

- **Memory imbalance.** Existing pipeline parallelism implementations lead to imbalanced resource consumption. The first stage consumes more memory due to the embedding and the warm-up micro-batches. [p. 10]

- **Computation imbalance.** After the last layer of the model, output and loss need to be calculated, making this stage the execution latency bottleneck. [p. 10]

[p. 11] To address these issues, the pipeline schedule is modified as shown in Figure 6, which allows setting *N* flexibly — in this case *N* = 5, which can run an arbitrary number of micro-batches in each batch. This allows running: (1) fewer micro-batches than the number of stages when there is a batch size limit at large scale; or (2) more micro-batches to hide point-to-point communication, finding a sweet spot between DFS and breadth first schedule (BFS) for the best communication and memory efficiency. To balance the pipeline, one Transformer layer is reduced each from the first and the last stages, respectively. This means that the first model chunk on the first stage has only the embedding, and the last model chunk on the last stage has only output projection and loss calculation. To reduce pipeline bubbles, an interleaved schedule (Narayanan et al., 2021) with *V* pipeline stages on one pipeline rank is used. Overall pipeline bubble ratio is (PP - 1) / (V * M). Further, asynchronous point-to-point communication in PP is adopted, which considerably speeds up training, especially in cases when the document mask introduces extra computation imbalance. `TORCH_NCCL_AVOID_RECORD_STREAMS` is enabled to reduce memory usage from asynchronous point-to-point communication. Finally, to reduce memory cost, based on detailed memory allocation profiling, tensors that will not be used for future computation are proactively deallocated, including the input and output tensors of each pipeline stage, that will not be used for future computation. With these optimizations, Llama 3 could be pre-trained on sequences of 8K tokens without activation checkpointing. [p. 11]

### Figure 5 [p. 11]

**Figure 5** (p. 11): "Illustration of 4D parallelism. GPUs are divided into parallelism groups in the order of [TP, CP, PP, DP], where DP stands for FSDP. In this example, 16 GPUs are configured with a group size of |TP|=2, |CP|=2, |PP|=2, and |DP|=2. A GPU's position in 4D parallelism is represented as a vector, [D_1, D_2, D_3, D_4], where D_i is the index on the i-th parallelism dimension."

The figure shows a diagram of 16 GPUs (GPU 0 through GPU 15) organized into a 4D parallelism grid. Each GPU is labeled with its TP, CP, PP, and DP indices (e.g., GPU 0 is TP0 CP0 PP0 DP0). The layout illustrates how GPUs sharing the same TP index are in the same TP group, same CP index in the same CP group, etc. Arrows indicate the TP, CP, PP, and DP dimensions. Examples from the caption: GPU0[TP0, CP0, PP0, DP0] and GPU1[TP1, CP0, PP0, DP0] are in the same TP group; GPU0 and GPU2 are in the same CP group; GPU0 and GPU4 are in the same PP group; GPU0 and GPU8 are in the same DP group.

**Context parallelism for long sequences.** [p. 11] Context parallelism (CP) is utilized to improve memory efficiency when scaling the context length of Llama 3 and enable training on extremely long sequences up to 128K in length. In CP, the partition is across the sequence dimension, and specifically the input sequence is partitioned into 2 x CP chunks so each CP rank receives two chunks for better load balancing. The *i*-th CP rank received both the *i*-th and the (2 x CP - 1 - *i*)-th chunks. [p. 11]

Different from existing CP implementations that overlap communication and computation in a ring-like structure (Liu et al., 2023a), the CP implementation adopts an **all-gather** based method where the key (K) and value (V) tensors are first all-gathered, and then attention output is computed for the local query (Q) tensor chunk. Although the **all-gather** communication latency is exposed in the critical path, this approach is still adopted for two main reasons: (1) it is easier and more flexible to support different types of attention masks in **all-gather** based CP attention, such as the document mask; and (2) the exposed **all-gather** latency is small as the communicated K and V tensors are much smaller than Q tensor due to the use of GQA (Ainslie et al., 2023). Hence, the time complexity of attention computation is an order of magnitude larger than **all-gather** (*O(S^2)* versus *O(S)*, where *S* represents the sequence length in the full causal mask), making the **all-gather** overhead negligible. [p. 12]

**Network-aware parallelism configuration.** [p. 12] The order of parallelism dimensions, [TP, CP, PP, DP], is optimized for network communication. The innermost parallelism requires the highest network bandwidth and lowest latency, and hence is usually constrained to within the same server. The outermost parallelism may spread across a multi-hop network and should tolerate higher network latency. Therefore, based on the requirements for network bandwidth and latency, parallelism dimensions are placed in the order of [TP, CP, PP, DP]. DP (i.e., FSDP) is the outermost parallelism because it can tolerate longer network latency by asynchronously prefetching sharded model weights and reducing gradients. Identifying the optimal parallelism configuration with minimal communication overhead while avoiding GPU memory overflow is challenging. A memory consumption estimator and a performance-projection tool are developed which helped explore various parallelism configurations and project overall training performance and identify memory gaps effectively. [p. 12]

**Numerical stability.** [p. 12] By comparing training loss between different parallelism setups, several numerical issues that impact training stability were fixed. To ensure training convergence, FP32 gradient accumulation during backward computation over multiple micro-batches is used and also **reduce-scatter** gradients in FP32 across data parallel workers in FSDP. For intermediate tensors, e.g., vision encoder outputs, that are used multiple times in the forward computation, the backward gradients are also accumulated in FP32. [p. 12]

### 3.3.3 Collective Communication [p. 12]

[p. 12] The collective communication library for Llama 3 is based on a fork of Nvidia's NCCL library, called NCCLX. NCCLX significantly improves the performance of NCCL, especially for higher latency networks. Recall that the order of parallelism dimensions is [TP, CP, PP, DP], where DP corresponds to FSDP. The outermost parallelism dimensions, PP and DP, may communicate through a multi-hop network, with latency up to tens of microseconds. The original NCCL collectives — **all-gather** and **reduce-scatter** in FSDP, and **point-to-point** in PP — require data chunking and staged data copy. This approach incurs several inefficiencies, including (1) requiring a large number of small control messages to be exchanged over the network to facilitate data transfer, (2) extra memory-copy operations, and (3) using extra GPU cycles for communication. For Llama 3 training, a subset of these inefficiencies are addressed by tuning chunking and data transfer to fit network latencies, which can be as high as tens of microseconds for a large cluster. Small control messages are also allowed to traverse the network at a higher priority, especially avoiding being head-of-line blocked in deep-buffer core switches. Ongoing work for future Llama versions involves making deeper changes in NCCLX to holistically address all the aforementioned problems. [p. 12]

### Figure 6 [p. 12]

**Figure 6** (p. 12): "Illustration of pipeline parallelism in Llama 3. Pipeline parallelism partitions eight pipeline stages (0 to 7) across four pipeline ranks (PP ranks 0 to 3), where the GPUs with rank 0 run stages 0 and 4, the GPUs with P rank 1 run stages 1 and 5, etc. The colored blocks (0 to 9) represent a sequence of micro-batches, where M is the total number of micro-batches and N is the number of continuous micro-batches for the same stage's forward or backward. Our key insight is to make N tunable."

The figure shows a Gantt-chart-style timeline for four pipeline ranks (PP rank0 through PP rank3). Each rank processes blocks labeled 0-9 representing micro-batches. Color coding distinguishes Stage 0-3 forward (white), Stage 4-7 forward (blue), Stage 0-3 backward (gray), and Stage 4-7 backward (red/pink). The interleaved schedule shows how forward and backward passes of different stages overlap across ranks. N=5 continuous micro-batches of the same stage are scheduled before switching, demonstrating the flexible scheduling approach.

### 3.3.4 Reliability and Operational Challenges [p. 13-14]

[p. 13] The complexity and potential failure scenarios of 16K GPU training surpass those of much larger CPU clusters that have been operated. Moreover, the synchronous nature of training makes it less fault-tolerant — a single GPU failure may require a restart of the entire job. Despite these challenges, for Llama 3, higher than 90% effective training time was achieved while supporting automated cluster maintenance, such as firmware and Linux kernel upgrades (Vigraham and Leonhardi, 2024), which resulted in at least one training interruption daily. The effective training time measures the time spent on useful training over the elapsed time. [p. 13]

[p. 13] During a 54-day snapshot period of pre-training, a total of 466 job interruptions were experienced. Of these, 47 were planned interruptions due to automated maintenance operations such as firmware upgrades or operator-initiated operations like configuration or dataset updates. The remaining 419 were unexpected interruptions, which are classified in Table 5. Approximately 78% of the unexpected interruptions are attributed to confirmed hardware issues, such as GPU or host component failures, or suspected hardware-related issues like silent data corruption and unplanned individual host maintenance events. GPU issues are the largest category, accounting for 58.7% of all unexpected issues. Despite the large number of failures, significant manual intervention was required only three times during this period, with the rest of issues handled by automation. [p. 13]

### Table 5 [p. 13]

**Table 5: Root-cause categorization of unexpected interruptions during a 54-day period of Llama 3 405B pre-training.** About 78% of unexpected interruptions were attributed to confirmed or suspected hardware issues.

| Component                      | Category                | Interruption Count | % of Interruptions |
|--------------------------------|-------------------------|-------------------:|-------------------:|
| Faulty GPU                     | GPU                     | 148                | 30.1%              |
| GPU HBM3 Memory                | GPU                     | 72                 | 17.2%              |
| Software Bug                   | Dependency              | 54                 | 12.9%              |
| Network Switch/Cable           | Network                 | 35                 | 8.4%               |
| Host Maintenance               | Unplanned Maintenance   | 32                 | 7.6%               |
| GPU SRAM Memory                | GPU                     | 19                 | 4.5%               |
| GPU System Processor           | GPU                     | 17                 | 4.1%               |
| NIC                            | Host                    | 7                  | 1.7%               |
| NCCL Watchdog Timeouts         | Unknown                 | 7                  | 1.7%               |
| Silent Data Corruption         | GPU                     | 6                  | 1.4%               |
| GPU Thermal Interface + Sensor | GPU                     | 6                  | 1.4%               |
| SSD                            | Host                    | 3                  | 0.7%               |
| Power Supply                   | Host                    | 3                  | 0.7%               |
| Server Chassis                 | Host                    | 2                  | 0.5%               |
| IO Expansion Board             | Host                    | 2                  | 0.5%               |
| Dependency                     | Dependency              | 2                  | 0.5%               |
| CPU                            | Host                    | 2                  | 0.5%               |
| System Memory                  | Host                    | 2                  | 0.5%               |

[p. 13] To increase the effective training time, job startup and checkpointing time were reduced, and tools were developed for fast diagnosis and problem resolution. PyTorch's built-in NCCL flight recorder (Ansel et al., 2024) is extensively used, a feature that captures collective metadata and stack traces into a ring buffer, and hence allowing diagnosis of hangs and performance issues quickly at scale, particularly with regard to NCCLX. Using this, every communication event and the duration of each collective operation are efficiently recorded, and also tracing data is automatically dumped on NCCLX watchdog or heartbeat timeout. More computationally intensive tracing operations and metadata collection are enabled selectively as needed live in production through online configuration changes (Tang et al., 2015) without needing a code release or job restart. [p. 13]

[p. 13-14] Debugging issues in large-scale training is complicated by the mixed use of NVLink and RoCE in the network. Data transfer over NVLink typically occurs through load/store operations issued by CUDA kernels, and failures in either the remote GPU or NVLink connectivity often manifest as stalled load/store operations within CUDA kernels without returning a clear error code. NCCLX enhances the speed and accuracy of failure detection and localization through a tight co-design with PyTorch, allowing PyTorch to access NCCLX's internal state and track relevant information. While stalls due to NVLink failures cannot be completely prevented, the system monitors the state of the communication library and automatically times out when such a stall is detected. Additionally, NCCLX traces the kernel and network activities of each NCCLX communication and provides a snapshot of the failing NCCLX collective's internal state, including finished and pending data transfers between all ranks. This data is analyzed to debug NCCLX scaling issues. [p. 14]

[p. 14] Sometimes, hardware issues may cause still-functioning but slow stragglers that are hard to detect. Even a single straggler can slow down thousands of other GPUs, often appearing as functioning but slow communications. Tools were developed to prioritize potentially problematic communications from selected process groups. By investigating just a few top suspects, the stragglers were usually able to be effectively identified. [p. 14]

[p. 14] One interesting observation is the impact of environmental factors on training performance at scale. For Llama 3 405B, a diurnal 1-2% throughput variation based on time-of-day was noted. This fluctuation is the result of higher mid-day temperatures impacting GPU dynamic voltage and frequency scaling. [p. 14]

[p. 14] During training, tens of thousands of GPUs may increase or decrease power consumption at the same time, for example, due to all GPUs waiting for checkpointing or collective communications to finish, or the startup or shutdown of the entire training job. When this happens, it can result in instant fluctuations of power consumption across the data center on the order of tens of megawatts, stretching the limits of the power grid. This is an ongoing challenge as training is scaled for future, even larger Llama models. [p. 14]

## 3.4 Training Recipe [p. 14]

[p. 14] The recipe used to pre-train Llama 3 405B consists of three main stages: **(1)** initial pre-training, **(2)** long-context pre-training, and **(3)** annealing. The three stages are described separately below. Similar recipes are used to pre-train the 8B and 70B models. [p. 14]

### 3.4.1 Initial Pre-Training [p. 14]

[p. 14] Llama 3 405B is pre-trained using AdamW with a peak learning rate of 8 x 10^-5, a linear warm up of 8,000 steps, and a cosine learning rate schedule decaying to 8 x 10^-7 over 1,200,000 steps. A lower batch size is used early in training to improve training stability, and increased subsequently to improve efficiency. Specifically, an initial batch size of 4M tokens and sequences of length 4,096 is used, and these values are doubled to a batch size of 8M sequences of 8,192 tokens after pre-training 252M tokens. The batch size is doubled again to 16M after pre-training on 2.87T tokens. This training recipe was found to be very stable: few loss spikes were observed and no interventions were required to correct for model training divergence. [p. 14]

**Adjusting the data mix.** [p. 14] Several adjustments were made to the pre-training data mix during training to improve model performance on particular downstream tasks. In particular, the percentage of non-English data during pre-training was increased to improve the multilingual performance of Llama 3. Mathematical reasoning data was also upsampled to improve the model's mathematical reasoning performance, more recent web data was added in the later stages of pre-training to advance the model's knowledge cut-off, and subsets of the pre-training data that were later identified as being lower quality were downsampled. [p. 14]

### 3.4.2 Long Context Pre-Training [p. 14]

[p. 14] In the final stages of pre-training, training is performed on long sequences to support context windows of up to 128K tokens. Training on long sequences is not done earlier because the compute in self-attention layers grows quadratically in the sequence length. The supported context length is increased in increments, pre-training until the model has successfully adapted to the increased context length. Successful adaptation is assessed by measuring whether **(1)** model performance on short-context evaluations has recovered completely and **(2)** the model perfectly solves "needle in a haystack" tasks up to that length. In Llama 3 405B pre-training, context length was increased gradually in six stages, starting from the original 8K context window and ending in the final 128K context window. This long-context pre-training stage was performed using approximately 800B training tokens. [p. 14]

### 3.4.3 Annealing [p. 15]

[p. 15] During pre-training on the final 40M tokens, the learning rate is linearly annealed to 0, maintaining a context length of 128K tokens. During this annealing phase, the data mix is also adjusted to upsample data sources of very high quality; see Section 3.1.3. Finally, the average of model checkpoints (Polyak (1991) averaging) is computed during annealing to produce the final pre-trained model. [p. 15]
