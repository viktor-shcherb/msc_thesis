# 1 Introduction [p. 1-2]

[p. 1]

Deep learning has greatly advanced artificial intelligence, impacting scientific and industrial uses involving complex sequential data processing tasks such as natural language understanding, conversational AI, time-series analysis, and indirectly sequential formats like images and graphs (Brown et al., 2020; Ismail Fawaz et al., 2019; Wu et al., 2020; Albalak et al., 2022). Predominant techniques include RNNs and Transformers (Vaswani et al., 2017), each with specific benefits and drawbacks. RNNs require less memory, particularly for handling long sequences, but suffer from the vanishing gradient problem and non-parallelizability in the time dimension during training, limiting their scalability (Hochreiter, 1998; Le and Zuidema, 2016).

**Figure 1** (p. 1): "Average performance of RWKV models compared to transformers across twelve NLP tasks. For further details, see section 5."
- X-axis: Compute (exaFLOP), log scale from ~10^1 to ~10^3.
- Y-axis: Accuracy, ranging from ~37 to ~56.
- Four model families plotted: BLOOM, Pythia, OPT, RWKV.
- RWKV performance tracks closely with transformer baselines (BLOOM, Pythia, OPT) at similar compute budgets, performing on par or slightly below at most compute levels. All curves show increasing accuracy with increasing compute.

Transformers emerged as a powerful alternative, adept at managing local and long-range dependencies and supporting parallelized training (Tay et al., 2022). Models such as GPT-3 (Brown et al., 2020), ChatGPT (OpenAI, 2022; Kocon et al., 2023), LLaMA (Touvron et al., 2023), and Chinchilla (Hoffmann et al., 2022) showcase the potential of Transformers in NLP. However, the self-attention mechanism's quadratic complexity makes it computationally and memory intensive for tasks involving long sequences and constrained resources. This has stimulated research to enhance Transformers' scalability, sometimes sacrificing some of their effectiveness (Wang et al., 2020; Zaheer et al., 2020; Dao et al., 2022a).

[p. 2]

To tackle these challenges, the authors introduce the Receptance Weighted Key Value (RWKV) model, combining the strengths of RNNs and Transformers while circumventing key drawbacks. RWKV alleviates memory bottleneck and quadratic scaling associated with Transformers (Katharopoulos et al., 2020) with efficient linear scaling, while maintaining the expressive properties of the Transformer, such as parallelized training and robust scalability. RWKV reformulates the attention mechanism with a variant of linear attention, replacing traditional dot-product token interaction with more effective channel-directed attention. This implementation, *without approximation*, offers the lowest computational and memory complexity; see Table 1.

**Table 1** (p. 2): Inference complexity comparison with different Transformers. $T$ = sequence length, $d$ = feature dimension, $c$ = MEGA's chunk size of quadratic attention, $s$ = size of a local window for AFT.

| Model | Time | Space |
|---|---|---|
| Transformer | $O(T^2 d)$ | $O(T^2 + Td)$ |
| Reformer | $O(T \log T d)$ | $O(T \log T + Td)$ |
| Performer | $O(Td^2 \log d)$ | $O(Td \log d + d^2 \log d)$ |
| Linear Transformers | $O(Td^2)$ | $O(Td + d^2)$ |
| AFT-full | $O(T^2 d)$ | $O(Td)$ |
| AFT-local | $O(Tsd)$ | $O(Td)$ |
| MEGA | $O(cTd)$ | $O(cd)$ |
| **RWKV (ours)** | $O(\mathbf{T}\mathbf{d})$ | $O(\mathbf{d})$ |

The motivation behind RWKV is to balance computational efficiency with expressive capacity in neural networks. It offers a solution for handling large-scale models with billions of parameters, exhibiting competitive performance at a reduced computational cost. Experiments suggest RWKV addresses scaling and deployment challenges in AI, especially for sequential data processing, pointing towards more sustainable and efficient AI models.

Contributions listed in the paper:
- The introduction of RWKV, a novel architecture combining RNNs and Transformer advantages while mitigating their limitations.
- Detailed experiments demonstrating RWKV's performance and efficiency on benchmark datasets for large-scale models.
- The release of pretrained models, from 169 million to 14 billion parameters, trained on the Pile (Gao et al., 2020; Biderman et al., 2022). Code at: https://github.com/BlinkDL/RWKV-LM. Models at: https://huggingface.co/RWKV.
