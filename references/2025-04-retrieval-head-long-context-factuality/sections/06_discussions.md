# 5 Discussions [p. 7-8]

## General Functionalities of Attention Heads [p. 7]

For transformer language models, there is a tendency to view the functionality of FFNs layers to be the place for storing knowledge [8], and the attention layers to be the place for implementing algorithms [19]. The induction head discussed in Olsson et al. [19] typically searches repeated patterns of the input, which is at a certain level similar to the retrieval heads (as it also searches and repeats information). Different than the induction heads, the retrieval heads are typically responsible for redirecting the information according to the context, but do not for inferring programs. The authors tend to believe there exist more algorithm and functionalities implemented by other types of attention heads to be discovered by future research.

## Relationship to Local and Linear Attention and State Space Model [p. 8]

Although there exist numerous works about local [24] / linear [22] attention, state space models [9], and hybrid architectures [5] achieving inspiring efficiency in some context modeling, so far there is no linear attention / SSM architecture that passes the Needle-in-a-Haystack test to the best of the authors' knowledge, suggesting that the full attention might be a must for long-context information retrieval. One example is that the Mistral v0.1 [12] uses sliding window attention and cannot pass needle-in-a-haystack, and their authors changes the attention to full in v0.2 [18], then it can pass the needle test. The authors' results showing strong evidence why full attention is needed: it is crucial for the retrieval heads to work on the full KV cache.

## Applications to KV Cache Compression [p. 8-9]

The problem that the KV cache is too large and occupies a large chunk of the GPU memory severely hinders the deployment of long-context models. For example, for LLAMA 2 7B, the KV cache of 100K tokens requires more than 50GB memory, while 2K context requires less than 1GB memory. If the authors serve this model on one 80G A100, then the concurrency of 100K context can be 50 times less than 2K context queries, which is prohibitively expensive. The results from this work indicates that it might be possible to radically prune out the KV cache corresponding to the non-retrieval heads (recall in Fig. 3 shows only 5% of the heads are retrieval) and significantly reducing the deployment cost of long-context models. The authors leave this study to future research.
