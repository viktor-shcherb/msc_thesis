# Introduction [p. 1-2]

## Transformer limitations and linear alternatives

The Transformer architecture has significantly advanced Large Language Models (LLMs), showcasing exceptional performance across a wide range of tasks due to its effective attention mechanism [p. 1]. This mechanism excels in precise sequence modeling and leverages parallel processing capabilities of modern GPUs during training. However, the self-attention component scales quadratically with sequence length, leading to substantial computational demands that pose challenges for both training and inference [p. 1].

To mitigate these issues, researchers have explored alternatives such as linear Transformers (Katharopoulos et al., 2020a), which replace traditional softmax-based attention with kernelized dot-product-based linear attention, substantially reducing memory requirements during inference by reframing as a linear RNN with matrix-valued states [p. 1-2]. While early versions of linear Transformers underperformed in language modeling tasks compared to standard Transformers, recent enhancements—such as incorporating data-dependent gating mechanisms akin to those in LSTMs, exemplified by models like GLA (Yang et al., 2024a) and Mamba2 (Dao & Gu, 2024a)—have shown promising improvements [p. 2]. However, challenges persist in managing information over long sequences, particularly for in-context retrieval tasks where traditional Transformers maintain their advantage (Arora et al., 2023a; 2024a; Jelassi et al., 2024; Wen et al., 2024; Akyurek et al., 2024) [p. 1-2].

## Linear Transformers as associative memory

This phenomenon is not surprising: linear Transformers can be interpreted as implementing an outer-product-based key-value association memory, reminiscent of tensor product representation (Smolensky, 1990) [p. 2]. However, the number of orthogonal key-value pairs they can store is bounded by the model's dimensionality. When the sequence length exceeds this dimension, "memory collisions" become inevitable, hindering exact retrieval (Schlag et al., 2021a) [p. 2].

## Mamba2 and its limitations

Mamba2 addresses this limitation by introducing a simple gated update rule, $\mathbf{S}_t = \alpha_t \mathbf{S}_{t-1} + \boldsymbol{v}_t \boldsymbol{k}_t^{\top}$, which uniformly decays all key-value associations at each time step by a dynamic ratio, $\alpha_t \in (0, 1)$ [p. 1-2]. However, this approach does not account for the varying importance of different key-value associations, potentially leading to inefficient memory utilization. If the model needs to forget a specific key-value association, all key-value pairs are equally forgotten, making the process less targeted and efficient [p. 2].

## DeltaNet and its limitations

In contrast, the linear Transformer with the delta rule (Widrow et al., 1960), known as DeltaNet (Schlag et al., 2021a; Yang et al., 2024b), selectively updates memory by (softly) replacing an old key-value pair with the incoming one in a sequential manner [p. 2]. This method has demonstrated impressive performance in synthetic benchmarks for in-context retrieval. However, since this process only modifies a single key-value pair at a time, the model lacks the ability to rapidly clear outdated or irrelevant information, especially when there is more information than slots to be erased [p. 2]. Consequently, DeltaNet has been found to perform moderately on real-world tasks (Yang et al., 2024b), likely due to the absence of a robust memory-clearing mechanism [p. 2].

## Proposed gated delta rule

Recognizing the complementary advantages of the gated update rule and the delta rule in memory management, we propose the *gated delta rule*, a simple and intuitive mechanism that combines both approaches [p. 2]. This unified rule enables adaptive memory control: it can promptly clear memory by setting $\alpha_t \to 0$, while selectively updating specific content without affecting other information by setting $\alpha_t \to 1$ (effectively switching to the pure delta rule) [p. 2].

## Implementation and architecture

The remaining challenge lies in implementing the gated delta rule in a hardware-efficient manner [p. 2]. Building upon Yang et al. (2024b)'s efficient algorithm that parallelizes the delta rule computation using the WY representation (Bischof & Loan, 1987; Sun et al., 2023a; Yang et al., 2024a,b), we carefully extend their approach to incorporate the gating terms [p. 2]. Our extension preserves the benefits of chunkwise parallelism (Hua et al., 2022b; Sun et al., 2023a; Yang et al., 2024a,b) and enables hardware-efficient computation [p. 2].

## Results and contributions

Our resulting architecture, Gated DeltaNet, consistently outperforms both Mamba2 and DeltaNet across a comprehensive suite of benchmarks, including language modeling, commonsense reasoning, in-context retrieval, length extrapolation, and long-context understanding [p. 2]. Building on these results, we also develop hybrid architectures that strategically combine Gated DeltaNet layers with sliding window attention or Mamba2 layers, further enhancing both training efficiency and model performance [p. 2].
