# 1 Introduction [p. 1]

[p. 1] Attention (Bahdanau et al., 2015; Vaswani et al., 2017) has become the key building block of neural sequence processing models. Visualizing attention weights is the easiest and most popular approach to interpret a model's decisions and gain insights about its internals (Vaswani et al., 2017; Xu et al., 2015; Wang et al., 2016; Lee et al., 2017; Dehghani et al., 2019; Rocktäschel et al., 2016; Chen and Ji, 2019; Coenen et al., 2019; Clark et al., 2019).

Although equating attention with explanation is wrong (Pruthi et al., 2019; Jain and Wallace, 2019), attention can offer plausible and meaningful interpretations (Wiegreffe and Pinter, 2019; Vashishth et al., 2019; Vig, 2019).

The paper focuses on problems arising when moving to higher layers of a model, due to lack of token identifiability of the embeddings in higher layers (Brunner et al., 2020).

[p. 1] The authors propose two methods to compute *token attention* (attention scores to input tokens) at each layer, by taking raw attentions (i.e., *embedding attention*) of that layer as well as those from the precedent layers. These methods model the information flow in the network with a *DAG* (Directed Acyclic Graph), where:
- Nodes are input tokens and hidden embeddings
- Edges are the attentions from nodes in each layer to those in the previous layer
- Edge weights are the attention weights

The first method, **attention rollout**, assumes that the identities of input tokens are linearly combined through the layers based on the attention weights. It rolls out the weights to capture the propagation of information from input tokens to intermediate hidden embeddings.

The second method, **attention flow**, considers the attention graph as a flow network. Using a maximum flow algorithm, it computes maximum flow values from hidden embeddings (sources) to input tokens (sinks).

Both methods take the residual connection in the network into account to better model the connections between input tokens and hidden embeddings.

**Key claim (contribution):** Compared to raw attention, the token attentions from attention rollout and attention flow have higher correlations with importance scores obtained from input gradients as well as *blank-out*, an input ablation based attribution method. [p. 1]

**Scope clarification:** The techniques proposed are not toward making hidden embeddings more identifiable, or providing better attention weights for better performance, but rather a new set of attention weights that take token identity problem into consideration and can serve as a better diagnostic tool for visualization and debugging. [p. 1]
