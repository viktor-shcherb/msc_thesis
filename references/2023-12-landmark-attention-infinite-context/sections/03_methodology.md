# 3 Methodology [p. 4-6]

[p. 4] The paper mainly focuses on the causal language modeling setting where each token can only attend to previous tokens in the input. The extension to the non-causal case is briefly discussed in Appendix F.

When using a Transformer to process a long input, the ideal case would be to allow each token to attend to all previous tokens. However, this becomes computationally infeasible as the input length increases. Nevertheless, since the attention scores always sum to one, the number of keys with a large attention weight is limited even for long contexts. Thus, by retrieving only those keys with large attention scores, it is possible to closely emulate the ideal case. The authors propose a method to find these keys by dividing a long input into blocks of consecutive tokens and using the attention to retrieve relevant blocks.

More particularly, a representative vector is assigned to each block such that a high attention score to any token inside a block would lead to a high attention score to the block's representative vector. Therefore, blocks can be directly retrieved based on the attention score of their representative vector.

To obtain the representative vector of a block, a new special token is introduced to the vocabulary, called the **landmark token**. A landmark token is inserted after the last token of each block, and the model is trained such that the key vector for this token becomes the representative vector sought. The process is illustrated in Figure 1.

An alternative for directly finding a candidate set of keys with high attention score is using a data structure that allows finding nearest neighbors of the query vectors efficiently such as FAISS [15]. In comparison, this method provides a retrieval method directly controlled by attention which can be more semantic-based. Furthermore, retrieving a block instead of a single token allows the attention to also access the local context around the token which may be more accommodating of observed classic attention patterns [20]. The aforementioned data structures can also be applied on top of this method to search for relevant blocks.

## 3.1 Training Landmark Tokens [p. 4-5]

[p. 4] To train the landmark tokens, the text corpus is first processed by adding a landmark token after every ℓ_block tokens. Training then proceeds using the standard batching method which feeds windows of ℓ_seq tokens to the model. In a list of ℓ_seq > ℓ_block tokens, the model is trained such that each landmark token represents the block consisting of all previous tokens until the previous landmark token (or the beginning of the input if no previous landmark token exists). The token is passed through the transformer as any other token while its representation is updated using the self-attention mechanism.

Let the index (token position) of the landmark corresponding to the i-th token's block be denoted by p_i. If the last block is incomplete and does not have a landmark token, p_i := ℓ_seq. If the i-th token is a landmark token, p_i := i.

To train the transformer to make use of landmark tokens, the standard attention mechanism is altered such that the attention weight for a token depends on the similarity of the query vector with both the token's key as well as with the key of its block's landmark token. A generalized softmax function called **Grouped Softmax** is defined.

[p. 5] Given a vector **v** in R^{ℓ_seq} and a group index **g** in N^{ℓ_seq}, Grouped Softmax applies softmax separately over elements belonging to the same group. (Using **g** = 1_{ℓ_seq} recovers the standard softmax function):

$$\sigma_G(\mathbf{v}, \mathbf{g})_x := \text{GroupedSoftmax}(\mathbf{v}, \mathbf{g})_x := \frac{e^{\mathbf{v}_x}}{\sum_{y: \mathbf{g}_y = \mathbf{g}_x} e^{\mathbf{v}_y}}.$$  (1)

Equation (1) defines GroupedSoftmax: each element is normalized only against elements in the same group, rather than against all elements.

The softmax function is replaced with Grouped Softmax after computing the attention scores. For each block, regular tokens are put in a separate group, ensuring that all regular tokens within the same block share the same group, while tokens outside the block are assigned to different groups. When computing the attention weights for the i-th token, landmark tokens for other blocks are placed in the same group as the i-th token. The landmark token for the i-token's block is **ignored** when computing the attention weights for the i-th token. In other words, the landmark token for each block is only used by tokens in other blocks. This is intuitive as the landmark token should only be accessed when tokens in other blocks require to retrieve information from the landmark's corresponding block.

Building on the fact that p_j = j only holds when the j-th token is a landmark token, the grouping used for the i-th token is defined more formally as:

$$\mathbf{G}_{i,j} := \begin{cases} p_j & p_j \neq j & \triangleright \text{ placing normal tokens in their own blocks.} \\ -1 & p_i = j & \triangleright \text{ ignoring current block's landmark token.} \\ p_i & p_i \neq j \wedge p_j = j & \triangleright \text{ placing other landmarks in the } i\text{-th token's group.} \end{cases}$$  (2)

Equation (2) defines the group assignment matrix G: normal tokens are assigned to their block's group (indexed by their landmark position p_j); the current block's own landmark is masked out (group -1); and landmarks from other blocks are placed into the same group as the i-th token's block.

Finally, to obtain the final weights after applying GroupedSoftmax, each token's softmax output is multiplied with the softmax output for its block's landmark token. For tokens in the same group as the i-th token, the softmax output is used directly as its attention weight. The weight for landmark tokens is always zero. In more formal terms:

$$\mathbf{S}_{i,j} := \text{SoftmaxScore}(\mathbf{Q}, \mathbf{K})_i := \text{GroupedSoftmax}\left(\frac{\mathbf{Q}_i^\top \times \mathbf{K}}{\sqrt{d_{\text{head}}}}, \mathbf{G}_i\right)$$  (3)

Equation (3): S_{i,j} computes per-group softmax scores using the scaled dot-product of the i-th query with all keys, grouped according to G_i.

$$\text{AttWeight}(\mathbf{Q}, \mathbf{K})_{i,j} := \begin{cases} 0 & p_j = j \\ \mathbf{S}_{i,j} & \mathbf{G}_{i,j} = \mathbf{G}_{i,i} \wedge p_j \neq j \\ \mathbf{S}_{i,j} \cdot \mathbf{S}_{i,p_j} & \mathbf{G}_{i,j} \neq \mathbf{G}_{i,i} \wedge p_j \neq j \end{cases}.$$  (4)

Equation (4) defines the final attention weight: landmark tokens always get zero weight; tokens in the same group as token i keep their GroupedSoftmax score directly; tokens in other blocks have their score multiplied by the score of their block's landmark token (the gating mechanism).

[p. 5] Under this scheme, the attention weights sum to one as is the case for the standard softmax function. More importantly, attending to tokens in other blocks is gated by the attention score to the landmark token as expected. Since tokens in the same block and the landmark tokens share the softmax group, the model has to choose between attending to other blocks and current tokens. The intuition behind the grouping is to force the model to only attend to relevant blocks due to this trade-off.

Attention masks can be applied normally by ignoring the masked elements in the softmax (e.g. by setting A_{i,j} to -infinity on the masked elements in practice). The focus is on experiments on the causal language modeling. The grouping scheme can be further extended to introduce additional hierarchy for retrieval. For example, the interested reader is referred to Appendix D, where a different grouping scheme is briefly discussed which also trains a global retrieval gate token that controls whether retrieval from an earlier block needs to be performed. At inference, this gate can be used to decide whether a memory call is needed or the model already has the information it needs in the context. Further investigations of this setting are left for future work.

## 3.2 Inference [p. 5-6]

[p. 5] Similar to training, the input gets augmented by a landmark token after every ℓ_block tokens. Then, the input is broken into chunks of ℓ_local length and iteratively fed from the beginning to the end. To retrieve relevant blocks, each attention layer has access to a cache of previous blocks. The cache stores the key-value vectors for all tokens of those blocks, including the landmark token. Since the retrieval only requires access to the landmarks, memory usage can be reduced significantly by swapping out (for example to CPU memory or even to disk) all regular tokens' cached key-value vectors, and then swapping them back in only if their corresponding block is retrieved by the attention.

The most permissive retrieval scheme is described first. When processing each chunk at each layer, the attention score of each token with the landmark tokens currently in the cache is computed. For each token, the attention score for all the tokens in **the k highest scoring blocks** is computed, and the obtained attention matrix is prepended to the local attention matrix. This is finished by applying GroupedSoftmax to the attention matrix and computing the weighted average of the value vectors to obtain the token's representation.

[p. 6] Under the above scheme, each token and each head can retrieve different blocks from the cache. It is possible to limit the retrieval flexibility to improve efficiency. For example, it is possible to merge the scores across heads by taking a maximum over the landmark attention scores (after applying softmax) of each head. Under this scheme, the same set of blocks is retrieved for all heads. It is also possible to take the maximum over different tokens, retrieving only k blocks per head for all the tokens in the current window combined. The effect of these limitations is studied at the end of Section 4.1. Unless otherwise stated, experiments use the permissive scheme described above.

## 3.2.1 Positional Encoding [p. 6]

[p. 6] When computing the attention scores to cache elements (both landmark and normal tokens), it is important to correctly incorporate positional information. The transformer model is sensitive to positional information. For example, tokens right after the last memory block do not have access to any context and are unable to select memory blocks based on semantics. Instead, they need to rely on positional information to select the last memory block.

Optimally, the tokens are encoded with their actual position index. However, a known flaw of Transformers is their inability to extrapolate to lengths not observed during training. Various methods proposed to alleviate this condition also do not fully resolve the problem unless they are combined with block attention which only allows attending to a window of tokens. The authors decide against using block attention since the main goal is to facilitate attending to large contexts. In Appendix E an alteration of the training method which allows using the actual position index is proposed. However, to avoid overlapping changes, the following approximation is used for most experiments.

A segment with length (k+1) * (ℓ_block + 1) is allocated at the beginning of the context. The current chunk is indexed starting after this segment. For the retrieved blocks, the index for any of the latest k blocks is mapped to the corresponding place within the last k blocks in the allocated prefix segment. Other blocks in the cache have their position mapped to the first block in the allocated prefix segment. Once it is decided which blocks to retrieve, those among the latest k blocks are mapped to the right of the pre-allocated segment and the rest of the blocks are mapped to the left of the pre-allocated segment, while respecting the order of the blocks. This scheme is called **stingy position mapping** and is further illustrated in Figure 2.

When k = 1, mapping memory blocks to a segment of at least 2 blocks is crucial. Using only a single block, all memory blocks are mapped to the same index. However, as discussed at the beginning, it is essential to at least retrieve the last memory block solely based on position information which is impossible unless this block is mapped to a different index. While it is possible that the importance of pre-allocating the additional block decreases as k grows, this scheme is adapted so that the attention would be at least as flexible as simply keeping the last k blocks.

The above approximation relies on the ability to add position information when performing the retrieval. In experiments, Transformer models with Rotary positional encoding [33] are used, which adds the position information to the key and query vectors just before computing the attention. [p. 7] Thus, the key vectors can be stored without position information in the cache and the position information is added when performing the retrieval according to the following scheme.

**Figure 2** (p. 6): "Stingy position mapping: Retrieving top k = 2 blocks from a memory of 5 blocks. Retrieval landmarks for the last 2 blocks are accurately mapped to sequence index positions, while previous blocks are mapped to the position of the (k+1)-th last block. Blocks are then distributed across the prefix based on their position, with an empty block separating the last k blocks from older ones."

The figure shows: on the left, a "Memory" column with blocks labeled [a,b], [c,d], [e,f], [g,h], [i,j] each with their landmark tokens, plus a "New Input" [p,q,r,s]. The "Retrieval Position Mapping" shows how landmarks are mapped to positions: the last 2 blocks' landmarks are mapped to their actual positions, while earlier blocks are mapped to the (k+1)-th last block's position. The "Final Attention Position Mapping" shows three examples of how different retrieved blocks are arranged in the pre-allocated prefix segment alongside the current input [p,q,r,s].
