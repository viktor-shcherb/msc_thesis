# C Inference Requirement [p. 14, 16]

[p. 14] The authors provide the minimal sequence length required to overlap communication with computation during training in Table 2. Ring Attention enables effortless training of context size that scales linearly with the number of devices. While the paper focuses on introducing training as it is more memory demanding than autoregressive inference where the number of query tokens is one, Ring Attention is applicable to inference too.

For example, serving a LLaMA 7B on 32x TPUv5e, the conventional approach is to distribute the model along the attention heads dimension, with each device computing one attention head. Assuming a batch size of 1, this can serve up to a 256K context length due to key-value cache activation size. Ring Attention can allow 32 times larger context by circulating the key-value cache between a ring of devices.

To overlap the communication with computation, it needs:

$$d^2/F \geq 2 \cdot d^2/B$$

where $B/F \geq 2$. With a bandwidth of 186 GB/s and flops of 196 TFLOPs, and assuming an unreasonably high MFU of 40% for this large context, then $B/F = 2.4$, meaning that Ring Attention allows 32 times larger context for inference without adding overheads.
