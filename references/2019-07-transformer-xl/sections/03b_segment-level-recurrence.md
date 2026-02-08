# 3.2 Segment-Level Recurrence with State Reuse [p. 3-4]

To address the limitations of a fixed-length context, the authors introduce a recurrence mechanism to the Transformer architecture. During training, the hidden state sequence computed for the previous segment is *fixed* and *cached* to be reused as an extended context when the model processes the next new segment, as shown in Fig. 2a. Although the gradient still remains within a segment, this additional input allows the network to exploit information in the history, leading to an ability of modeling longer-term dependency and avoiding context fragmentation. [p. 3]

**Figure 2** (p. 4): "Illustration of the Transformer-XL model with a segment length 4."
- (a) Training phase: shows "Fixed (No Grad)" cached hidden states from the previous segment concatenated with the "New Segment" hidden states. The dashed box around the cached states indicates they are fixed (no gradient). Green paths highlight the recurrent connections across segments.
- (b) Evaluation phase: shows "Extended Context" where previous segment representations are reused instead of recomputed. The shaded area visualizes how the dependency length grows linearly with the number of layers.

## Formal definition

Let the two consecutive segments of length L be **s**_tau = [x_{tau,1}, ..., x_{tau,L}] and **s**_{tau+1} = [x_{tau+1,1}, ..., x_{tau+1,L}] respectively. Denoting the n-th layer hidden state sequence produced for the tau-th segment **s**_tau by **h**^n_tau in R^{L x d}, where d is the hidden dimension. Then, the n-th layer hidden state for segment **s**_{tau+1} is produced (schematically) as follows: [p. 3-4]

**h-tilde**^{n-1}_{tau+1} = [SG(**h**^{n-1}_tau) circ **h**^{n-1}_{tau+1}]

**q**^n_{tau+1}, **k**^n_{tau+1}, **v**^n_{tau+1} = **h**^{n-1}_{tau+1} **W**^T_q, **h-tilde**^{n-1}_{tau+1} **W**^T_k, **h-tilde**^{n-1}_{tau+1} **W**^T_v

**h**^n_{tau+1} = Transformer-Layer(**q**^n_{tau+1}, **k**^n_{tau+1}, **v**^n_{tau+1})

where SG(.) stands for stop-gradient, [**h**_u circ **h**_v] indicates the concatenation of two hidden sequences along the length dimension, and **W** denotes model parameters. [p. 4]

The critical difference from the standard Transformer: the key **k**^n_{tau+1} and value **v**^n_{tau+1} are conditioned on the extended context **h-tilde**^{n-1}_{tau+1} and hence **h**^{n-1}_tau cached from the previous segment. [p. 4]

## Dependency length

The recurrent dependency between **h**^n_{tau+1} and **h**^{n-1}_tau shifts one layer downwards per-segment, which differs from the same-layer recurrence in conventional RNN-LMs. Consequently, the largest possible dependency length grows linearly w.r.t. the number of layers as well as the segment length, i.e., O(N x L), as visualized by the shaded area in Fig. 2b. This is analogous to truncated BPTT (Mikolov et al., 2010), a technique for training RNN-LMs. However, different from truncated BPTT, this method caches a sequence of hidden states instead of the last one, and should be applied together with relative positional encoding (Section 3.3). [p. 4]

## Faster evaluation

Besides achieving extra long context and resolving fragmentation, the recurrence scheme enables significantly faster evaluation. Specifically, during evaluation, the representations from the previous segments can be reused instead of being computed from scratch as in the vanilla model. In experiments on enwiki8, Transformer-XL is up to 1,800+ times faster than the vanilla model during evaluation (see Section 4). [p. 4]

## Memory mechanism

The recurrence scheme does not need to be restricted to only the previous segment. In theory, one can cache as many previous segments as the GPU memory allows. A predefined length-M old hidden states spanning (possibly) multiple segments are cached, referred to as the memory **m**^n_tau in R^{M x d}, due to a clear connection to the memory augmented neural networks (Graves et al., 2014; Weston et al., 2014). In experiments, M is set equal to the segment length during training, and increased by multiple times during evaluation. [p. 4]
