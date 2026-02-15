# Appendix A: Details of Approaches [p. 15–16]

> "This section serves as a supplement to the Approaches section 3 in the main text, expanding relevant details about related methods to provide readers with a deeper understanding." [p. 15]

## A.1 Positional Encoding [p. 15]

### A.1.1 Variants of RoPE [p. 15]

Su et al. (2024) try to seek a positional encoding method that could encode relative position during the computing query and key similarity, and decompose this process into the representations of the query and key. They conduct theoretical analysis and propose a novel positional encoding, which transform this similarity into following formula:

$$\sin(q_m, k_n) = q_m^T R_{\Theta,m}^d k_n = (R_{\Theta,m}^d q_m)^T (R_{\Theta,n}^d k_n)$$ (3)

where $R_{\Theta,m}^d$ are a series of pre-defined orthogonal matrices, named as the rotation matrix, which is defined as follows:

$$R_{\Theta,m}^d = \begin{pmatrix}
\cos m\theta_1 & -\sin m\theta_1 & \cdots & 0 & 0 \\
\sin m\theta_1 & \cos m\theta_1 & \cdots & 0 & 0 \\
\vdots & \vdots & \ddots & \vdots & \vdots \\
0 & 0 & \cdots & \cos m\theta_{d/2} & -\sin m\theta_{d/2} \\
0 & 0 & \cdots & \sin m\theta_{d/2} & \cos m\theta_{d/2}
\end{pmatrix}$$

The function set $\Theta$ consists of a set of pre-defined function values $\Theta = \{\theta_i = 10000^{-2(i-1)/d}, i \in [1, 2, ..., d/2]\}$. $R_{\Theta}^d$ integrates positional information into the query and key vectors for multiplication. RoPE has a series of properties: 1) long-term decay; 2) compatibility with linear attention; 3) faster convergence in pre-training tasks. Besides, Liu et al. (2024b) conduct a detailed analysis of RoPE and provides the scaling laws for RoPE-based extrapolation.

**Position Index Adjustment** An et al. (2024) propose Dual Chunk Attention (DCA), which distributes the position indexes used during pre-training to each token based on the chunk to relate relationships between query and key without additional training. It is proposed from the perspective of allocation of position information.

And there are also some methods based on scaling position indexes. Chen et al. (2023b) propose Position Interpolation (PI) method based on the fact that position encoding can be applied to non-integer positions. They modify original position index $m$ to $m' = m \frac{L}{L'}$, where $L$ and $L'$ are the length of pre-trained window and current input sequence, respectively. This method insert additional positional encoding between adjacent integer positional encoding between adjacent integer position index in the original RoPE to handle longer sequences.

Combining above two methods, Su (2023) proposed ReRoPE, which combines direct extrapolation and position interpolation. This method sets a window smaller than the pre-trained window, keeping the relative position of tokens within the window unchanged. And scales the relative position of tokens outside the window.

**Base Frequency Adjustment** As described in the main text, this type of methods enhance the model extrapolation performance by modifying $\theta_i$ in the trigonometric function terms in the rotation matrix.

Peng and Quesnelle (2023); Roziere et al. (2023) choose to change the base $b$ of the exponential terms $\theta_i$ from the default value $b = 10000$ to other values which can improve the model extrapolation performance.

Different from them, some work directly scale $\theta_i$. NTK-by-parts (bloc97, 2023) interpolation chooses to scale the $\theta_i$ of different dimensions in the rotation matrix by a scale function of the dimension $i$ and the input sequence length $L'$. And YaRN (Peng et al., 2023) incorporates temperature $t$ related to the input sequence length $L'$ on the basis of NTK-by-parts interpolation to further improve the extrapolation performance of the model.

**Structure Modification** XPOS (Sun et al., 2022) adjusts the original RoPE structure and introduces a position-dependent exponential bias to enhance relative position information, particularly enhancing the decay effect on distant tokens.

### A.1.2 Attention Bias [p. 15]

Besides applying RoPE-based methods, a plenty of method add a bias related to the relative distance between tokens to introduce relative position information. The process can be expressed as follows:

$$\sin(q_m, k_n) = q_m^T k_n + f_{bias}(m, n)$$ (4)

where $f_{bias}(m, n)$ is a bias function that depends on the token position index corresponding to query and key. $f_{bias}(m, n)$ be divided into two categories: learnable and predefined.

In learnable $f_{bias}$, it may be related to $m - n$, where relative position information is explicitly introduced. For example, in T5 (Raffel et al., 2020), $f_{bias}$ is a learnable function with $m - n$ as input and varies with attention heads. Similarly, KERPLE (Chi et al., 2022a) sets $f_{bias}$ as a parameterized kernel function, requiring training to determine the parameter values.

The predefined $f_{bias}$ is typically ALiBi (Attention with Linear Biases) (Press et al., 2021). It uses a predefined function for $f_{bias}$ that depends on the number of attention heads $h$ and the current head number $h_i$, which is expressed as $f_{bias}(m, n) = 2^{-\frac{8}{H} \cdot (n - m)}$. Besides, in Sandwich method (Chi et al., 2022b), $f_{bias}$ is defined as $f_{bias} = \frac{8h}{H} \cdot (p_m p_n - \frac{s}{2})$, where $p_m$ and $p_n$ are the sinusoidal positional encoding used in the original Transformer model.

## A.2 Context Compression [p. 16]

### A.2.1 Soft Compression [p. 16]

This kind of methods achieve compression at the hidden states level.

Bulatov et al. (2022) introduced the Recurrent Memory Transformer (RMT), which compresses at segment level. It begins by dividing the input into a sequence of segments, with memory tokens appended to the start and end of each segment to serve as its summary token. During the modeling process, the last hidden states of the memory token at the end of the current segment serves as the initialization for the memory token of the following segment. Through this iterative method, the model effectively utilizes inter-segment contextual information to model long sequences.

Similarly, the Recurrent Attention Network (RAN, Li et al., 2023b) appends a Global Perception Cell (GPC) vector at the start of the hidden vector representation of each segment to achieve a compressed representation achieving the effect of concatenating summary tokens, and completing the information interaction between segments. This method simulates the human mechanism of memory enhancement through iteration, introduced a Memory Review scheme which performs cross-attention between last hidden states of the GPC from all segments and and the original input to update the representation of GPC. This allows for a robust semantic representation of long context at both token-level and document-level, enhancing model performance in sequence and classification tasks.

AutoCompressors (Chevalier et al., 2023) is built on the basis of RMT, compressing the content of the segment into summary vectors for representation. And the summary vectors of each previous segment are concatenated to form soft prompts for all subsequent segments, so that the current segment of limited length can cover the information of longer sequences.

In addition, In-context Autoencoder (ICAE, Ge et al., 2023) adds memory tokens at the end of the input sequence to compress context into short memory slots while training the model to generate outputs closely resembling the original context. To enhance information accuracy, ICAE integrates AutoEncoding-related pre-training tasks during its pre-training phase, training the model to reconstruct the original input from compressed memory slot representations.

Gisting (Mu et al., 2024b) similarly compresses the prompt part of the input token sequence into shorter gist tokens, improving inference speed.

### A.2.2 Hard Compression [p. 16]

Hard compression directly utilizes LLMs to compress original input text.

LLM-Lingua (Jiang et al., 2023) trains a small model to align with the output of LLM and uses the perplexity (PPL) of the small model as an evaluation for token importance. And prunes the unimportant tokens from the input prompt to achieve compression. Furthe, LongLLMLingua (Jiang et al., 2024a) has made improvements on this basis, compressing the input based on the content of the question, thus better preserving key information related to the question.

Differently, MEMWALKER (Chen et al., 2023a) employs a hierarchical summarization approach to compress long context sequences, iteratively summarizing the input to construct a tree-like structure of summarized content. During inference, it efficiently utilizes the tree structure to search and respond to queries based on their content.

## A.3 Retrieval Augmented [p. 16]

### A.3.1 Retrieval Granularity [p. 16]

The retrieval granularity in existing work can be divided into two categories: token-level retrieval and block-level retrieval.

Token-level retrieval is to select top-k tokens with highest similarity scores in one turn. This method is widely used in existing (Wu et al., 2022; Tworkowski et al., 2024; Bertsch et al., 2024a). It is simple to implement, but it has some limitations. Such as the potential for semantic discontinuities due to discrete token retrieval and the need to recalculate similarity for all tokens, which is computationally intensive and inefficient.

Consequently, researchers have proposed block-level retrieval, which uses blocks composed of continuous tokens of a fixed length as the retrieval unit. Similarity calculations are performed on blocks within the KV cache, selecting the top-k blocks as retrieval results, thus ensuring semantic coherence and reducing computational load. However, block-level retrieval faces a new challenge on how to effectively utilize the information of the tokens in the block and effectively represent the block to complete the similarity calculation. Long-MEM (Wang et al., 2024b) and RPT (Rubin and Berant, 2023) represent the corresponding block by calculating the mean pooling of token representations within the block. InFLLM (Xiao et al., 2024) calculates the representative score of each token within the block against other tokens, selecting a subset of high-scoring tokens to represent the block. Additionally, some methods introduce an extra token to represent blocks, such as the Landmark method (Mohtashami and Jaggi, 2024) introduces the Landmark token, a new token into the vocabulary, and place it at the end of each block. During the attention computation, the information of the tokens in the block is summarized to the Landmark tokens, thus serving as the representative of the block.

### A.3.2 Similarity Computation [p. 17]

After determining the retrieval granularity, we need to formulate an appropriate rule to compute similarity. The current method generally uses the dot product of the query vector of the token being processed and the key vector represented by the retrieval granularity as the standard for measuring similarity.

### A.3.3 Positional Encoding [p. 17]

Since the positions of the retrieved context tokens are not fixed, and recording each token's specific position in the KV cache is costly, it is challenging to provide accurate position information.

Based on experiments of Dai et al. (2019), which show that the relative position information of distant tokens does not seem to be important, some methods like MemTRM, FoT, and InFLLM choose to uniformly set the position encoding of the retrieved context token part to the same position vector, ignoring the position information between the retrieved context tokens themselves.

Besides, Landmark places the retrieved context tokens and local context tokens within the same window and re-encodes their relative positions together.

### A.3.4 Attention Calculation [p. 17]

When it comes to attention calculation, it's important to find a suitable method to make full use of retrieved context tokens and local context tokens.

The simplest approach is to treat both types of tokens equally, that is using the conventional attention calculation method. For example, FoT and InFLLM use standard attention for calculation, while Unlimformer (Bertsch et al., 2024a) employs cross attention.

However, the importance of the information contained within these two types of context tokens is not the same for the query currently being processed. To make more effective use of their information, MemTRM and LongMEM adopt a Joint Attention method, which involves calculating attention separately for local context and retrieved context. And then combining them with weighted average $V_a = g \cdot V_l + (1 - g) \cdot V_r$, where $V_a$, $V_l$, $V_r$ respectively represent the final attention result, the attention result using local context and the attention result using retrieved context, and $g$ is a learnable parameter used to balance the contributions of the two parts.

Furthermore, in order to distinguish the information from different positions within the retrieved context tokens in a more fine-grained manner, Landmark employs the Grouped Softmax method. Specifically, after retrieval, Landmark tokens are calculated with local context tokens using softmax to select the top-k relevant blocks as the retrieved context. Attention is then calculated separately within these blocks. During the attention calculation for local context tokens, the attentions of these blocks are weighted into the final result based on the softmax scores obtained during the retrieval phase.

## A.4 Attention Pattern [p. 17]

### A.4.1 Sliding Window [p. 17]

This type of method transform information between segments. Transformer-XL (Dai et al., 2019) uses sliding window method to process long context, where the hidden state from the previous segment is concatenated to the front of the current segment. It not only utilizes the key and value information from the current segment but also reuses those from the previous segment. This approach iteratively expands the receptive field, enabling inter-segment information transfer and enhancing the model's ability to process long context.

Besides, Han et al. (2024) identify that starting tokens occupy a distinct feature space, and these tokens act as a factor causing model generalization failures. They further propose LM-Infinite as a solution, utilizing a λ-shaped attention mask strategy during attention calculation. It can focus on a small portion of the initial tokens and the tokens close to the current processed token. Similarly, StreamingLLM (Xiao et al., 2023) also finds that the initial tokens in a sequence significantly influence the attention calculation of subsequent tokens and cannot be ignored. Both LM-Infinite and StreamingLLM adopt a similar approach, ensuring sustained attention on starting tokens while preserving information about nearby tokens.

### A.4.2 Parallel Context [p. 18]

Parallel Context Windows (PCW, Ratner et al., 2022) is one of the representative works. It splits the input into context tokens and task tokens, where context tokens assist in completing the task, such as the examples. And task tokens are the input of the test example, such as the questions. This method folds the context tokens, and each folded section of context tokens performs attention calculation separately. Finally, during the decoding phase of the task tokens, all these tokens, are concatenated in front of the task token, sharing the same set of position index.

Besides, Structured prompting (Hao et al., 2022) also adopts a similar approach by folding demonstration tokens in the input and concatenating them in front of the test input tokens. But unlike PCW, structured prompting employs Rescaled Attention, which reduces the weight of demonstration tokens in the attention calculation of the test tokens by a certain ratio. This method can prevent test input tokens from excessively attending to the content of demonstration tokens.

### A.4.3 Sparse Attention [p. 18]

This method can reduce the complexity of attention calculation. So that can improve efficiency when processing long context.

LongNet (Ding et al., 2023) introduces dilated attention, a mechanism that exponentially increases the attentive field as the distance between tokens increases. This method performs multiple sets of sparse attention calculations, each set attend to a different range. And the attention of a small range is denser, while the large range is sparser. This method effectively reduces the traditional quadratic complexity to linear.

MEGABYTE (Yu et al., 2023) performs hierarchical attention calculation on the input. Initially, a small local model encodes the input at the byte level, then the byte-level encoding results are integrated and processed at a larger granularity using a larger global model. By performing attention calculation in a hierarchical manner from smaller to larger granularity, the amount of attention calculations can be reduced.

In LongLoRA (Chen et al., 2023c), the proposed $S^2$-Attention groups attention heads and adjusts each group to attend to different but overlapping local windows, then leverages the characteristics of multihead attention to integrate various local information. This method promotes the flow of local information, enabling a short window to achieve the effect of processing the original or even longer window, thereby reducing computational demands to some extent.
