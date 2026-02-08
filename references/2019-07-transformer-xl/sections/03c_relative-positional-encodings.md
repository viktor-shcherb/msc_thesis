# 3.3 Relative Positional Encodings [p. 4-5]

## The problem with absolute positional encodings

A crucial technical challenge with state reuse: how to keep the positional information coherent when reusing hidden states. In the standard Transformer, sequence order information is provided by positional encodings **U** in R^{L_max x d}, where the i-th row **U**_i corresponds to the i-th *absolute* position within a segment and L_max prescribes the maximum possible length to be modeled. The actual input is the element-wise addition of word embeddings and positional encodings. [p. 4]

If absolute positional encoding is simply adapted to the recurrence mechanism, the hidden state sequence would be computed schematically by: [p. 4]

**h**_{tau+1} = f(**h**_tau, **E**_{**s**_{tau+1}} + **U**_{1:L})

**h**_tau = f(**h**_{tau-1}, **E**_{**s**_tau} + **U**_{1:L})

where **E**_{**s**_tau} in R^{L x d} is the word embedding sequence of **s**_tau, and f represents a transformation function. Both **E**_{**s**_tau} and **E**_{**s**_{tau+1}} are associated with the same positional encoding **U**_{1:L}. As a result, the model has no information to distinguish the positional difference between x_{tau,j} and x_{tau+1,j} for any j = 1, ..., L, resulting in a sheer performance loss. [p. 4-5]

## Relative positional encoding idea

The fundamental idea is to only encode the *relative* positional information in the hidden states. The positional encoding gives the model a temporal clue or "bias" about how information should be gathered, i.e., where to attend. Instead of incorporating bias statically into the initial embedding, one can inject the same information into the attention score of each layer. [p. 5]

When a query vector q_{tau,i} attends on key vectors **k**_{tau, <=i}, it does not need to know the absolute position of each key vector. It suffices to know the relative distance between each key vector k_{tau,j} and itself q_{tau,i}, i.e. i - j. [p. 5]

A set of relative positional encodings **R** in R^{L_max x d} is created, where the i-th row **R**_i indicates a relative distance of i between two positions. By injecting the relative distance dynamically into the attention score, the query vector can easily distinguish representations of x_{tau,j} and x_{tau+1,j} from their different distances, making the state reuse mechanism feasible. The absolute position can be recovered recursively from relative distances. [p. 5]

## Prior work on relative positional encodings

The idea has been explored in the context of machine translation (Shaw et al., 2018) and music generation (Huang et al., 2018). The authors offer a different derivation, arriving at a new form of relative positional encodings, which has a one-to-one correspondence to its absolute counterpart and enjoys much better generalization empirically (see Section 4). [p. 5]

## Derivation from absolute attention

In the standard Transformer (Vaswani et al., 2017), the attention score between query q_i and key vector k_j within the same segment can be decomposed as: [p. 5]

**A**^{abs}_{i,j} = **E**^T_{x_i} **W**^T_q **W**_k **E**_{x_j} (term a) + **E**^T_{x_i} **W**^T_q **W**_k **U**_j (term b) + **U**^T_i **W**^T_q **W**_k **E**_{x_j} (term c) + **U**^T_i **W**^T_q **W**_k **U**_j (term d)

The authors re-parameterize the four terms relying only on relative positional information: [p. 5]

**A**^{rel}_{i,j} = **E**^T_{x_i} **W**^T_{q} **W**_{k,E} **E**_{x_j} (term a) + **E**^T_{x_i} **W**^T_{q} **W**_{k,R} **R**_{i-j} (term b) + *u*^T **W**_{k,E} **E**_{x_j} (term c) + *v*^T **W**_{k,R} **R**_{i-j} (term d)

## Three changes from absolute to relative

1. Replace all appearances of the absolute positional embedding **U**_j for computing key vectors in terms (b) and (d) with its relative counterpart **R**_{i-j}. This reflects the prior that only the relative distance matters for where to attend. Note that **R** is a sinusoid encoding matrix (Vaswani et al., 2017) without learnable parameters. [p. 5]

2. Introduce a trainable parameter *u* in R^d to replace **U**^T_i **W**^T_q in term (c). Since the query vector is the same for all query positions, it suggests the attentive bias towards different words should remain the same regardless of the query position. With similar reasoning, a trainable parameter *v* in R^d substitutes **U**^T_i **W**^T_q in term (d). [p. 5]

3. Deliberately separate the two weight matrices **W**_{k,E} and **W**_{k,R} for producing the content-based key vectors and location-based key vectors respectively. [p. 5]

## Intuitive meaning of each term

Under the new parameterization: [p. 5]
- Term (a): content-based addressing
- Term (b): content-dependent positional bias
- Term (c): global content bias
- Term (d): global positional bias

## Comparison with Shaw et al. (2018)

Shaw et al. (2018) only has terms (a) and (b), dropping the two bias terms (c) and (d). Moreover, Shaw et al. (2018) merge the multiplication **W**_k **R** into a single trainable matrix **R-hat**, which abandons the inductive bias built into the original sinusoid positional encoding (Vaswani et al., 2017). In contrast, the relative positional embedding **R** in Transformer-XL adapts the sinusoid formulation. As a benefit of the inductive bias, a model trained on a memory of some certain length can automatically generalize to a memory several times longer during evaluation. [p. 5]

## Complete Transformer-XL procedure

The computational procedure for a N-layer Transformer-XL with a single attention head, for n = 1, ..., N: [p. 5]

**h-tilde**^{n-1}_tau = [SG(**m**^{n-1}_tau) circ **h**^{n-1}_tau]

**q**^n_tau, **k**^n_tau, **v**^n_tau = **h**^{n-1}_tau **W**^{n,T}_q, **h-tilde**^{n-1}_tau **W**^{n,T}_{k,E}, **h-tilde**^{n-1}_tau **W**^{n,T}_v

**A**^n_{tau,i,j} = **q**^{n,T}_{tau,i} **k**^n_{tau,j} + **q**^{n,T}_{tau,i} **W**^n_{k,R} **R**_{i-j} + *u*^T **k**_{tau,j} + *v*^T **W**^n_{k,R} **R**_{i-j}

**a**^n_tau = Masked-Softmax(**A**^n_tau) **v**^n_tau

**o**^n_tau = LayerNorm(Linear(**a**^n_tau) + **h**^{n-1}_tau)

**h**^n_tau = Positionwise-Feed-Forward(**o**^n_tau)

with **h**^0_tau := **E**_{**s**_tau} defined as the word embedding sequence. [p. 5]

A naive way to compute **A** requires computing **W**^n_{k,R} **R**_{i-j} for all pairs (i, j), whose cost is quadratic w.r.t. the sequence length. However, since i - j only ranges from zero to the sequence length, the authors show a simple computation procedure in Appendix B which reduces the cost to be linear w.r.t. the sequence length. [p. 5]
