# A Layer-wise Relevance Propagation [p. 10–12]

## A.1 General Idea [p. 10–11]

Layer-wise relevance propagation (LRP) was originally designed to compute the contributions of single pixels to predictions of image classifiers (Bach et al., 2015). LRP back-propagates relevance recursively from the output layer to the input layer. The authors adapt LRP to the Transformer model to calculate relevance that measures the association degree between two arbitrary neurons in neural networks. [p. 10]

LRP in its general form assumes that the model can be decomposed into several layers of computation. The first layer are the inputs (for example, the pixels of an image or tokens of a sentence), the last layer is the real-valued prediction output of the model $f$. The $l$-th layer is modeled as a vector $z = (z_d^{(l)})_{d=1}^{V(l)}$ with dimensionality $V(l)$. [p. 11]

LRP assumes that we have a Relevance score $R_d^{(l+1)}$ for each dimension $z_d^{(l+1)}$ of the vector $z$ at layer $l + 1$. The idea is to find a Relevance score $R_d^{(l)}$ for each dimension $z_d^{(l)}$ of the vector $z$ at the next layer $l$ which is closer to the input layer such that the following equation holds: [p. 11]

$$f = \ldots = \sum_{d \in l+1} R_d^{(l+1)} = \sum_{d \in l} R_d^{(l)} = \cdots = \sum_d R_d^{(1)}.$$

> "This equation represents a *conservation principle*, on which LRP relies to propagate the prediction back without using gradients." [p. 11]

Intuitively, this means that total contribution of neurons at each layer is constant. Since the authors are interested only in heads relevance, they do not propagate till input variables and stop at the neurons of the encoder layer of interest. [p. 11]

## A.2 Formal Rules [p. 11]

The approach of Ding et al. (2017) previously used for neural machine translation is followed. [p. 11]

Let $r_{u \leftarrow v}$ denote relevance of neuron $u$ for neuron $v$. [p. 11]

**Definition 1** Given a neuron $u$, its incoming neuron set $IN(u)$ comprises all its direct connected preceding neurons in the network. [p. 11]

**Definition 2** Given a neuron $u$, its outcoming neuron set $OUT(u)$ comprises all its direct connected descendant neurons in the network. [p. 11]

**Definition 3** Given a neuron $v$ and its incoming neurons $u \in IN(v)$, the *weight ratio* measures the contribution of $u$ to $v$. It is calculated as: [p. 11]

For matrix multiplication:

$$w_{u \to v} = \frac{W_{u,v} u}{\sum_{u' \in IN(v)} W_{u',v} u'}, \quad \text{if } v = \sum_{u' \in IN(v)} W_{u',v} u',$$

For element-wise multiplication:

$$w_{u \to v} = \frac{u}{\sum_{u' \in IN(v)} u'}, \quad \text{if } v = \prod_{u' \in IN(v)} u'.$$

**Redistribution rule for LRP** Relevance is propagated using the *local redistribution rule* as follows: [p. 11]

$$r_{u \leftarrow v} = \sum_{z \in OUT(u)} w_{u \to z} \, r_{z \leftarrow v}.$$

The provided equations for computing weights ratio and the redistribution rule allow to compute the relative contribution of neurons at one point in a network to neurons at another. The authors follow Ding et al. (2017) and ignore non-linear activation functions. [p. 11]

## A.3 Head Relevance [p. 12]

In the experiments, the relative contribution of each head to the network predictions is computed. The contribution of neurons in head$_i$ (see equation 1) to the top-1 logit predicted by the model is evaluated. [p. 12]

Head relevance for a given prediction is computed as the sum of relevances of its neurons, normalized over heads in a layer. The final relevance of a head is its average relevance, where average is taken over all generation steps for a development set. [p. 12]
