# 4 Conclusion [p. 11]

Retentive networks (RetNet) are proposed for sequence modeling, which enables various representations, i.e., parallel, recurrent, and chunkwise recurrent. RetNet achieves significantly better inference efficiency (in terms of memory, speed, and latency), favorable training parallelization, and competitive performance compared with Transformers. The above advantages make RetNet an ideal successor to Transformers for large language models, especially considering the deployment benefits brought by the O(1) inference complexity. [p. 11]

Future directions: [p. 11]
- Scale up RetNet in terms of model size [CDH+22] and training steps.
- Retention can efficiently work with structured prompting [HSD+22b] by compressing long-term memory.
- Use RetNet as the backbone architecture to train multimodal large language models [HSD+22a, HDW+23, PWD+23].
- Deploy RetNet models on various edge devices, such as mobile phones.
