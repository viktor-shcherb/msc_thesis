# B Turing Completeness [p. 22-27]

[p. 22] This section extends the results to the setting of Perez et al. [72]. The exposition largely uses their proof structure with a few changes. Some of the lemmas are repeated with amendments to make the exposition self-contained.

## B.1 Notation [p. 22]

### Transformer Decoder

[p. 22] Both an encoder and a decoder are needed in the transformer for simulating a Turing machine. The notation from App. A.1 for encoders is reused. The decoder is similar to an encoder but with additional attention to an external pair of key-value vectors (**K**^e in R^{n x m}, **V**^e in R^{n x d}), which usually come from the encoder stack. A single layer of Transformer decoder is a parametric function Dec receiving a sequence **Y**_j = (**y**_1, ..., **y**_j) of vectors in R^d plus the external (**K**^e, **V**^e) and returning a sequence of vectors **Z**_j = (**z**_1, ..., **z**_j) of the same length. Each **z**_i is a d dimensional vector as well. Dec has three components, one more than Enc:

1. An attention mechanism ATTN that takes in the sequence **Y**_j and returns sequence (**p**_1, ..., **p**_j) of the same length and dimensionality;
2. A cross-attention mechanism CROSSATTN that takes in the sequence (**p**_1, ..., **p**_j) plus the external (**K**^e, **V**^e) and returns sequence (**a**_1, ..., **a**_j), with each **a**_i in R^d; and
3. A two layer fully connected network O that takes in a vector in R^d and returns a vector in R^d.

Then the i-th output vector of Dec(**Y**_j; **K**^e, **V**^e) is computed as follows:

**Equation (3):**

z_i = O(**a**_i) + **a**_i

**Equation (4):**

**a**_i = CROSSATTN(**p**_i, **K**^e, **V**^e) + **p**_i

**Equation (5):**

**p**_i = ATTN_D(**Y**_j)_i + **y**_i

[p. 22] ATTN_D and O are as defined in App. A.1 and it remains to define CROSSATTN. The i^th output vector of multi-head cross-attention attention is given by:

**Equation (6):**

CROSSATTN(**Y**_j)_i = sum_{h=1}^{H} sigma( (**y**_i W_Q^h)(**K**^{(e)} W_K^h)^T ) . (**V**^{(e)} W_V^h)

where W_Q^h, W_K^h, W_V^h in R^{d x m}, W_V^h in R^{d x d}, for all h = 1, ..., H heads.

### Turing Machine

[p. 22] The same setup of Turing Machine as used by Perez et al. [72] is employed (see section B.4). Given a Turing Machine M = (Q, Sigma, delta, q_init, F), the following notation is used:

- q^{(j)}: state of Turing machine M at time j.
- s^{(j)}: symbol under the head of M at time j.
- v^{(j)}: symbol written by M at time j.
- m^{(j)}: head direction in the transition of M at time j.

### Vector representations

[p. 22] For a symbol s in Sigma, [[s]] denotes its one-hot vector representation in Q^{|Sigma|}. All the transformer intermediate vectors used in the simulations have dimension d = 2|Q| + 4|Sigma| + 16. Note that five extra dimensions are used as compared to Perez et al. [72]. They follow the convention used in Perez et al. [72] and write a vector **v** in Q^d arranged in four groups of values as follows:

**v** = [ **q**_1, **s**_1, x_1,
         **q**_2, **s**_2, x_2, x_3, x_4, x_5, x_6,
         **s**_3, x_7, **s**_4,
         x_8, x_9, x_10, x_11, x_12, x_13, x_14, x_15, x_16 ]

where **q**_i in Q^{|Q|}, **s**_i in Q^{|Sigma|}, and x_i in Q.

## B.2 Details of the Simulation [p. 22-26]

[p. 22] This section gives more details on the architecture of the encoder and decoder needed to implement the simulation strategy.

### High Level Overview

[p. 23] Given the Turing machine M, the aim is to show that a transformer with an appropriate encoder and decoder T_D can simulate each step of M's execution. The simulation strategy mostly follows Perez et al. [72], except a sparse attention mechanism is used. The main idea is to maintain the current Turing machine state q^{(j)} and symbol under the head s^{(j)} as part of the decoder sequence **Y** for all time step j so that we can always simulate the corresponding Turing machine transition delta(q^{(j)}, s^{(j)}) = (q^{(j)}, v^{(j)}, m^{(j)}). The key difference will rise in Lemma B.4 of Perez et al. [72], where full attention is used to select the appropriate symbol from tape history in one step. To accomplish the same task with sparse attention, the associative property of max is exploited and the symbol selection is broken down over multiple steps. Thus, unlike Perez et al. [72], one decoding step of the sparse transformer T_D does not correspond to one step of the Turing machine M. In particular, there will be two types of steps: compute steps corresponding to update of M's state and intermediate steps corresponding to aggregating the max (which in turn is used for symbol selection). Let i denote the step of T_D and g(i) denote the step of M being simulated at step i of the decoder. At each decoding step the aim is to maintain the current Turing machine state q^{g(i)} and symbol under the s^{g(i)} in **y**_i. For roughly O(sqrt(i)) intermediate steps the state will remain the same, while information about relevant past output symbols is aggregated through sparse attention. To maintain the same state for intermediate steps, an extra switching layer (App. B.2.3) is introduced. Finally, at the next compute step the transition is made to new state q^{g(i)+1}, new head movement m^{g(i)}, and new output symbol v^{g(i)} to be written. Thereby they are able to completely simulate the given Turing machine M. As a result, the following main theorem is proved:

**Theorem 3.** *There exists a sparse attention mechanism using O(n) inner products such that the resulting class of Transformer Networks using this sparse attention mechanism is Turing Complete.* [p. 23]

### Encoder

[p. 23] As [72], the same trivial single layer encoder is used where resulting **K**^{(e)} contains position embedding and **V**^{(e)} contains one-hot symbol representation.

### Decoder

#### Sparse Self-Attention mechanism for Decoder

[p. 23] A particular instance of the sparse graph D at decoder is considered. Its edges are defined by the following relations: for all j in N_+, 1 <= k <= j + 1,

( j(j+1)/2 + k, k(k+1)/2 )

and

( j(j+1)/2 + k, j(j+1)/2 + k ) if k > 1 else ( j(j+1)/2 + 1, j(j+1)/2 ).

This graph can be seen as a special case of BIGBIRD where the first type of edges are realizations of random and the second type of edges correspond to locality. Also note that this graph satisfies the left-to-right constraint of decoder, i.e. no node attends to a node in the future. [p. 23]

**Figure 2** (p. 23): "Mapping between transformer step and original Turing machine step."

The figure shows a table with three rows:
- Transform i: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15
- TM Step j: 0, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4
- Offset k: 1, 1, 2, 1, 2, 3, 1, 2, 3, 4, 1, 2, 3, 4, 5

With curved arrows above showing connections between transformer steps. Boxed entries at positions i = 3, 6, 10, 15 (corresponding to k = j+1, i.e. the "compute" steps). This illustrates how one Turing machine step is spread across multiple transformer steps.

#### Embeddings and positional encodings

[p. 24] The construction needs a different positional encoding pos_Dec : N -> Q^d for the decoder:

pos_Dec(i) = [ 0, ..., 0,
               0, ..., 0,
               0, ..., 0,
               1, g(i) + 1, 1/(g(i)+1), 1/(g(i)+1)^2, h(i), 0, 0, 0, 0 ]

where g(i) = floor((-1 + sqrt(1 + 8i)) / 2) and h(i) = g(i + 1) - g(i). Note that h(i) reduces to a binary indicator variable **1**{(-1 + sqrt(1 + 8i)) / 2 = floor((-1 + sqrt(1 + 8i)) / 2)}.

### Induction Setup

[p. 24] Next, the construction of the decoder layers to produce the sequence of outputs **y**_1, **y**_2, ... is shown, where **y**_i is given by:

**y**_i = [ [[q^{g(i)}]], [[s^{g(i)}]], c^{g(i)},
           0, ..., 0,
           **0**_s, 0, [[w^{(i)}]],
           0, 0, 0, 0, 0, u_1^{(i)}, u_2^{(i)}, u_3^{(i)}, u_4^{(i)} ]

That is, at step i of the sparse decoder **y**_i, it will contain the information about the state of the Turing machine M at time g(i), the symbol under the head of M at time g(i), and the current location of head of M at time g(i). There is also a placeholder symbol w and placeholder scalars u_1, u_2, u_3, whose role will be clear from the construction. [p. 24]

The starting vector for the decoder is:

**y**_1 = [ [[q_init]], [[#]], 0,
           0, ..., 0,
           0, ..., 0,
           0, ..., 0 ]

The assumption is that the start head is at c^{(0)} = 0, the initial state is q^{(0)} = q_init, and s^{(0)} = #, initializing from clean tape. The correctness of the construction is shown by an inductive argument: the architecture is described piece by piece and at the same time it is shown that for every r >= 0, the architecture constructs **y**_{r+1} from the previous vectors (**y**_0, ..., **y**_r). [p. 24]

Thus, assume that **y**_1, ..., **y**_r satisfy the properties stated above. Since positional encodings are used, the actual input for the first layer of the decoder is the sequence:

**y**_1 + pos_Dec(1), **y**_2 + pos_Dec(2), ..., **y**_r + pos_Dec(r).

Denote by **y_bar**_i the vector **y**_i plus its positional encoding. Thus for all 1 <= i <= r:

**y_bar**_i = [ [[q^{g(i)}]], [[s^{g(i)}]], c^{g(i)},
               0, ..., 0,
               **0**_s, 0, [[w^{(i)}]],
               1, g(i) + 1, 1/(g(i)+1), 1/(g(i)+1)^2, h(i), u_1^{(i)}, u_2^{(i)}, u_3^{(i)}, u_4^{(i)} ]

## B.2.1 Layer 1: Simulate Transition Function [p. 24-25]

[p. 24] In this layer, the cross-attention between encoder and decoder is used to access the input string and a feed-forward network to simulate the transition function of M. The first self attention in Eq. (5) is not used in this layer and just produces the identity. This identity function is achieved by setting all queries, keys, values to be 0 everywhere plus the residual connection. Thus, **p**_i^1 = **y_bar**_i.

Since **p**_i^1 is of the form [_, ..., _, 1, g(i) + 1, _, ..., _], by Lemma B.1 of Perez et al. [72] attending over the encoder yields:

CROSSATTN(**p**_i^1, **K**^e, **V**^e) = [ 0, ..., 0,
                                         0, ..., 0,
                                         [[alpha^{g(i)+1}]], beta^{g(i)+1}, **0**_s,
                                         0, ..., 0 ]

where alpha and beta are as defined in Eq. (21) of [72]. [p. 25] Thus in Eq. (4) the vector **a**_i^1 is produced, given by:

**Equation (7):**

**a**_i^1 = CROSSATTN(**p**_i^1, **K**^e, **V**^e) + **p**_i^1
         = [ [[q^{g(i)}]], [[s^{g(i)}]], c^{g(i)},
             0, ..., 0,
             [[alpha^{g(i)+1}]], beta^{g(i)+1}, [[w^{(i)}]],
             1, g(i) + 1, 1/(g(i)+1), 1/(g(i)+1)^2, h(i), u_1^{(i)}, u_2^{(i)}, u_3^{(i)}, u_4^{(i)} ]

[p. 25] As the final piece of the first decoder layer, a function O_1(.) (Eq. (3)) is used that satisfies the following lemma:

**Lemma 6** (Lemma B.2 [72]). *There exists a two-layer feed-forward network O_1 : Q^d -> Q^d such that with input vector **a**_i^1 (Eq. (7)) produces as output*

O_1(**a**_i^1) = [ 0, ..., 0,
                   [[q^{g(i)+1}]], [[v^{g(i)}]], m^{g(i)}, 0, 0, 0, 0
                   0, ..., 0,
                   0, ..., 0 ]

That is, function O_1(.) simulates transition delta(q^{g(i)}, s^{g(i)}) to construct [[q^{g(i)+1}]], [[v^{g(i)}]], and m^{g(i)} besides some other linear transformations. [p. 25]

Thus, the output of the first decoder layer is:

**z**_i^1 = O_1(**a**_i^1) + **a**_i^1
         = [ [[q^{g(i)}]], [[s^{g(i)}]], c^{g(i)},
             [[q^{g(i)+1}]], [[v^{g(i)}]], m^{g(i)}, 0, 0, 0, 0,
             [[alpha^{g(i)+1}]], beta^{g(i)+1}, [[w^{(i)}]],
             1, g(i) + 1, 1/(g(i)+1), 1/(g(i)+1)^2, h(i), u_1^{(i)}, u_2^{(i)}, u_3^{(i)}, u_4^{(i)} ]

## B.2.2 Layer 2: Finding Head Node [p. 25]

[p. 25] In this layer, only the feed-forward network is used to evaluate the next location of the head. The self-attention and cross-attention are set to be the identity function, so **a**_2^i = **p**_i^2 = **z**_i^1. Recall that c^{g(i)} is the cell to which M is pointing to at time g(i), and that it satisfies the following recursion c^{g(i)+1} = c^{g(i)} + m^{g(i)}, which can be expanded to see that c^{g(i)+1} = m^{(0)} + m^{(1)} + ... + m^{g(i)}.

Its not difficult to see that a two layer network with non-linearity can compute c^{g(i)+1}/(g(i) + 1) and c^{g(i)}/(g(i) + 1) from c^{g(i)}, m^{g(i)}, and 1/(g(i) + 1) using the relation c^{g(i)+1} = c^{g(i)} + m^{g(i)}. At the end of layer 2, we obtain:

**z**_i^2 = O_2(**a**_i^2) + **a**_i^2
         = [ [[q^{g(i)}]], [[s^{g(i)}]], c^{g(i)},
             [[q^{g(i)+1}]], [[v^{g(i)}]], c^{g(i)+1}, 1/(g(i)+1), 1/(g(i)+1)^2, c^{g(i)+1}/(g(i)+1), c^{g(i)}/(g(i)+1),
             [[alpha^{g(i)+1}]], beta^{g(i)+1}, [[w^{(i)}]],
             1, g(i) + 1, 1/(g(i)+1), 1/(g(i)+1)^2, h(i), u_1^{(i)}, u_2^{(i)}, u_3^{(i)}, u_4^{(i)} ]

## B.2.3 Layer 3: Distinguishing Node Type [p. 25-26]

[p. 25] This is an additional layer (not present in the work of [72]), where computations are propagated in the sparse graph. In particular, this layer is used to "compute" or accumulate state in intermediate nodes. The self-attention and cross-attention are all set to be the identity function, so **a**_i^3 = **p**_i^3 = **z**_i^2. Only the dense attention layers are used to select the newly computed states or to continue with previous states. Using idea similar to Lemma B.6 of [72], a dense network can be constructed such that:

O([**x**, **y**, **z**, b]) = { [0, **0**, **0**, 0]        if b = 1,
                               [**0**, **z** - **y**, -**z**, 0]   if b = 0.

The negatives are generated to offset results from skip connection. This network is utilized to switch Turing machine state and position embedding for intermediate steps to the values received from [p. 26] previous time step and do nothing for compute nodes. h(i) is used as the flipping bit b. Thus, at end of layer 3, we obtain:

**z**_i^3 = O_3(**a**_i^3) + **a**_i^3
         = [ 0, ..., 0,
             [[q_hat^{(i)}]], [[v_hat^{(i)}]], c_hat^{(i)}, 1/(g(i)+1), 1/(g(i)+1)^2, c^{g(i)+1}/(g(i)+1), u_hat_4^{(i)},
             [[alpha_hat^{(i)}]], beta_hat^{(i)}, **0**_s,
             1, u_hat_1^{(i)}, u_hat_2^{(i)}, u_hat_3^{(i)}, h(i), 0, 0, 0, 0 ]

[p. 26] where h(i) is used for selecting old states. In particular:

- The input state and head position are copied as is for intermediate nodes. There is no need to transition to next Turing machine states in these nodes.

q_hat^{(i)} = { q^{g(i)+1}   if h(i) = 1,      v_hat^{(i)} = { v^{g(i)}   if h(i) = 1,      c_hat^{(i)} = { c^{g(i)+1}   if h(i) = 1,
                { q^{g(i)}     if h(i) = 0.                     { w^{(i)}    if h(i) = 0.                     { c^{g(i)}     if h(i) = 0.

- To preserve the symbol under the head for intermediate nodes, the previous symbol is copied to alpha location and set beta = g(i) + 1, as the symbol at alpha location will be copied as the symbol under head for next transformer step by the final transformation layer if beta = g(i) + 1. Thus, the previous symbol under head is correctly preserved as Turing machine does not transition these nodes. For compute nodes, things happen as usual.

alpha_hat^{(i)} = { alpha^{g(i)+1}   if h(i) = 1,      beta_hat^{(i)} = { beta^{g(i)+1}   if h(i) = 1,
                   { s^{g(i)}         if h(i) = 0.                       { g(i) + 1       if h(i) = 0.

- Finally, for the intermediate nodes, the position embedding corresponding to current best symbol w is copied, which is stored in u_1, u_2, u_3. For compute node, the position embedding corresponding to the current Turing machine step is kept.

u_hat_1^{(i)} = { g(i) + 1          if h(i) = 1,      u_hat_2^{(i)} = { 1/(g(i)+1)         if h(i) = 1,
                 { u_1^{(i)}         if h(i) = 0.                       { u_2^{(i)}          if h(i) = 0.

u_hat_3^{(i)} = { 1/(g(i)+1)^2      if h(i) = 1,      u_hat_4^{(i)} = { c^{g(i)}/(g(i)+1)  if h(i) = 1,
                 { u_3^{(i)}         if h(i) = 0.                       { u_4^{(i)}          if h(i) = 0.

[p. 26] For further simplification note that g(i + 1) = g(i) if h(i) = 0, else g(i) + 1 when h(i) = 1. With this fact, we can conclude that q_hat^{(i)} = q^{g(i+1)} and c_hat^{(i)} = c^{g(i+1)}. Thus, we can write:

**z**_i^3 = [ 0, ..., 0,
             [[q^{g(i+1)}]], [[v_hat^{(i)}]], c^{g(i+1)}, 1/(g(i)+1), 1/(g(i)+1)^2, c^{g(i)+1}/(g(i)+1), u_hat_4^{(i)},
             [[alpha_hat^{(i)}]], beta_hat^{(i)}, **0**_s,
             1, u_hat_1^{(i)}, u_hat_2^{(i)}, u_hat_3^{(i)}, h(i), 0, 0, 0, 0 ]

## B.2.4 Layer 4: Finding next symbol on tape [p. 26]

[p. 26] To find the symbol on tape under next head position c^{g(i)+1}, the aim is to find what was written last at the location c^{g(i)+1}. To facilitate this, following [72], ell(j) is defined to be the last time (previous to j) in which M was pointing to position c^{(j)}, or it is j - 1 if this is the first time that M is pointing to c^{(j)}. Recall j is the Turing machine step counter, which is different from sparse transformer step i. [72] could utilize full attention mechanism to find v^{ell(j+1)} at one go, but with sparse attention it has to be done over multiple steps.

Similar query, key, value functions as used for full attention by [72] are used. For all i:

Q_4(**z**_i^3) = [ 0, ..., 0,
                   0, ..., 0,
                   0, ..., 0,
                   0, c^{g(i)+1}/(g(i)+1), 1/(g(i)+1), 1/(3(g(i)+1)^2), 0, 0, 0, 0, 0 ]

---
[p. 26-27 continued]

K_4(**z**_i^3) = [ 0, ..., 0,
                   0, ..., 0,
                   0, ..., 0,
                   0, u_hat_2^{(i)}, u_hat_4^{(i)}, u_hat_3^{(i)}, 0, 0, 0, 0, 0 ]

V_4(**z**_i^3) = [ 0, ..., 0,
                   0, ..., 0,
                   **0**_s, 0, [[v_hat^{(i)}]],
                   0, 0, 0, 0, 0, u_1^{(i)}, u_2^{(i)}, u_3^{(i)}, u_4^{(i)} ]

[p. 27] It is clear that the three functions are linear transformations and thus they can be defined by feed-forward networks. The query vector is always formed using current time step position embedding, whereas key and value vectors are formed using copied over entries for intermediate nodes and using current entries only for compute node.

Perez et al. [72] find the desired v^{ell(j+1)} as v^{m(j)} using full attention, where

m(t) = arg min_{m in {0,...,t}} chi_t^j = arg min_{m in {0,...,t}} |<Q_4(**z**_j^3), K_4(**z**_m^3)>|

Note the minimization is only over Turing machine steps, i.e. over compute nodes in our case. The main idea is that m(j) can be estimated by parts using sparse attention mechanism. The minimization problem min_{m in {0,...,t}} chi_t^j can be expressed as min{...min{min{chi_0^j, chi_1^j}, chi_2^j}, ..., chi_t^j} by the associativity property.

By definition of graph D, at every intermediate node i of the form j(j+1)/2 + k, i.e. where k > 0, g(i) = j and h(i) = 0, we will attend over node k(k+1)/2 and best till now copied from i - 1. The node k(k+1)/2 is never an intermediate node as h(k(k+1)/2) = 1 for all k and in fact corresponds to Turing machine's step k. This will help us select the key and value corresponding to min between node k(k+1)/2 and i - 1. In other words, at node i of the form j(j+1)/2 + k we would have evaluated m(k) and corresponding value selected:

w^{j(j+1)/2+k+1} = v_hat^{m(k-1)}

and similarly for u's. So after going through all the intermediate nodes, finally at the next compute node, i.e. when k = j + 1, we will obtain the minimum value over all of 0, 1, ..., j. This implies at a compute node will be able to recover ell(g(i) + 1) and its corresponding value as shown in Lemma B.4 of [72]. Then we have that **p**_i^t is given by

**Equation (8):**

**p**_i^t = ATTN_D(**Z**_i^3) + **z**_i^3
         = [ 0, ..., 0,
             [[q^{g(i+1)}]], [[v_hat^{(i)}]], c^{g(i+1)}, 0, c^{g(i)+1}/(g(i)+1), u_hat_4^{(i)},
             [[alpha_hat^{(i)}]], beta_hat^{(i)}, [[w^{(i+1)}]],
             1, u_hat_1^{(i)}, u_hat_2^{(i)}, u_hat_3^{(i)}, h(i), u_1^{(i+1)}, u_2^{(i+1)}, u_3^{(i+1)}, u_4^{(i+1)} ]

The cross-attention and feed-forward network are set to be identity, so **z**_i^4 = **a**_i^4 = **p**_i^4.

## B.2.5 Final transformation [p. 27]

[p. 27] The construction is finished by using the final transformation function F(.) from the corresponding lemma from Perez et al. [72], with a slight modification.

**Lemma 7** (Lemma B.5 [72]). *There exists a function F : Q^d -> Q^d defined by a feed-forward network such that*

F(**z**_r^4) = [ [[q^{g(r+1)}]], [[s^{g(r+1)}]], c^{g(r+1)},
               0, ..., 0,
               **0**_s, 0, [[w^{(r+1)}]],
               0, 0, 0, 0, 0, 0, u_1^{(r+1)}, u_2^{(r+1)}, u_3^{(r+1)}, u_4^{(r+1)} ]
             = **y**_{r+1}

The modification is to let w, u_1, u_2, u_3 to pass through. This yields the desired input to transformer at next time step for both intermediate and compute node, thereby concluding the induction.
