# 3.3 Retrieval Augmented [p. 4–5]

Some existing work propose retrieval-augmented methods to enhance model performance on long context tasks by selectively incorporating crucial tokens from history context into attention [p. 4].

With reference to related work, we summarize a processing paradigm for this type of method [p. 4].

Initially, the (key, value) pairs from history are stored in the KV cache. Then the model retrieves the corresponding token representations from the KV cache at different retrieval granularity levels. This process is based on the similarity between current token and history tokens from KV cache. The top-k relevant tokens are selected as the retrieved context, which is then concatenated with the context within the current window to form a new input. Finally, the model applies appropriate positional encoding to this concatenated context for attention calculation [p. 4].

Below, we summarize the different methods according to each step of the above process [p. 4].

## 3.3.1 Retrieval Granularity [p. 4–5]

In the process of long context retrieval, we focus on the most relevant subset of tokens from KV cache related to the current processing step [p. 4].

Different methods use different retrieval granularity with the basic being token-level retrieval. Specifically, it involves calculating the similarity of each history token in the KV cache with the current token, and selecting the top-k history tokens' key and value vectors as the retrieval result [p. 5].

Methods applying this strategy include MemTRM (Wu et al., 2022), FoT (Tworkowski et al., 2024), Unlimiformer (Bertsch et al., 2024a), etc. [p. 5].

Besides, some work focus on block-level retrieval, which retrieve top-k set of tokens in one step (Wang et al., 2024b; Rubin and Berant, 2023; Xiao et al., 2024; Mohtashami and Jaggi, 2024) [p. 5].

## 3.3.2 Similarity Computation [p. 5]

Almost all existing works compute the inner product of query and key as similarity. This strategy draws from the standard attention mechanism, which calculates the dot product between query and key to allocate corresponding weights to the value (Vaswani et al., 2023). It is simple to implement and can effectively capture and utilize the similarity information between queries and keys [p. 5].

## 3.3.3 Positional Encoding [p. 5]

After computing the similarity, we select the top-k relative tokens as the results, and call them retrieved context tokens. Correspondingly, tokens within the current window are called as local context tokens [p. 5].

These two types of context tokens are concatenated to form a new set of context tokens. Before these new context tokens are fed into the model for attention computation, it is necessary to consider suitable positional encoding to distinguish the information of tokens at different positions [p. 5].

Some work choose to assign the same position vector to the retrieved context tokens (Wu et al., 2022; Tworkowski et al., 2024; Xiao et al., 2024), while Mohtashami and Jaggi (2023) choose reallocation strategies [p. 5].

## 3.3.4 Attention Calculation [p. 5]

Next, when performing attention calculation, we need to consider how to make full use of retrieved context tokens and local context tokens. Different approaches use different attention strategies [p. 5].

Simply, Tworkowski et al. (2024); Xiao et al. (2024) choose standard attention, while Bertsch et al. (2024a) chooses cross attention. Besides, Wu et al. (2022); Wang et al. (2024b) adopt a Joint Attention method. Landmark employs the Grouped Soft-max method, a fine-grained approach for calculation (Mohtashami and Jaggi, 2023) [p. 5].
