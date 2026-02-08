# Method [p. 6–8]

[p. 6] In this section, we use D to denote the model dimension, and unless explicitly stated, all vectors appearing in this section are dimension D/h, where h denotes the number of heads, belonging to R^{D/h}. For compactness and simplicity we show calculations per-head, eliding the head index. We use the convention that all vectors appearing in the section are explicitly transposed, so all matrices operate on the right side. We use the square subscript to denote a variable.

## 4.1 Eagle

### 4.1.1 Eagle Token Shift

[p. 6] We adopt the Token Shift technique from the previous RWKV, similar to a 1D causal convolution of size 2, as can be seen in Figure 1, center-bottom. To better introduce the Token Shift technique, we define some notation. The linear interpolation (lerp) between x_i and x_{i-1} used in RWKV-4 and Eagle Token Shift is defined as:

$$\text{lerp}_{\square}(a, b) = a + (b - a) \odot \mu_{\square}$$ (3)

where each μ_□ ∈ R^D is a learnable vector.

[p. 6] Token Shift allows the model to learn how much new versus old information should be allocated per time step to each channel of receptance, key, value, and gate vectors (r, k, v, and g respectively) independently and uniquely for each head. This makes it possible to form induction heads (Elhage et al., 2021) within a single layer since even a single head can directly accumulate both past and current token data into separate subspaces within these vectors.

### 4.1.2 Eagle Time Mixing

[p. 7] The formula of Eagle Time Mixing can be written as follows:

$$\square_i = \text{lerp}_{\square}(x_i, x_{i-1})W_{\square}, \quad \square \in \{r, k, v, g\}$$ (4)

$$w = \exp(-\exp(\omega))$$ (5)

$$wkv_i = \text{diag}(w) \cdot k_i^T \cdot v_i + \sum_{j=1}^{i-1} \text{diag}(w)^{i-1-j} \cdot k_j^T \cdot v_j \in \mathbb{R}^{(D/h) \times (D/h)}$$ (6)

$$o_i = \text{concat}(\text{SiLU}(g_i) \odot \text{LayerNorm}(r_i \cdot wkv_i)) W_o \in \mathbb{R}^D$$ (7)

Where LayerNorm operates on each of h heads separately, which is also equivalent to the Group-Norm (Wu & He (2018)) operation on h groups. It is also worth noting that w is obtained from w = exp(−exp(ω)), where ω ∈ R^{D/h} are the actual headwise trainable parameters. This ensures that w falls within the interval (0, 1), guaranteeing that diag(w) is a contraction matrix.

[p. 7] The wkv_i attention calculation can alternatively be written in a recurrent form:

$$wkv' = s + \text{diag}(w) \cdot k^T \cdot v$$ (8)

$$s' = \text{diag}(w) \cdot s + k^T \cdot v$$ (9)

[p. 7] RWKV's wkv term can be considered a decay-based equivalent to the normalised k^T v term in Linear Attention. It is instructive to note the way for each head j the recurrent state s is a sum of k^T v where each channel of s individually decays by the corresponding channel of w at each time step. Prior to the application of the value vector receptance, and output weights, a per-channel learned boost α is multiplied with the current token's k^T v and summed with the state, as can be seen in Figure 1, top-right. This gives the current token special treatment relative to the sum of past tokens contained within the decaying state history. The receptance is multiplied by this sum, acting like the query term in Linear Attention.

### 4.1.3 Channel Mixing

[p. 7] In both Eagle and Finch, the Channel Mixing module is identical to the previous RWKV-4 architecture, except for a slightly reduced hidden dimension from 4D to 3.5D. This reduction accounts for new gating weights in Eagle Time Mixing to ensure an equi-parameter relation with the prior model at the same number of layers and embedding dimension. We do not reduce the hidden dimension in Finch despite adding a small number of new parameters for LoRA weights. The formulas for Channel Mixing are the same as RWKV-4, but we restate them here to ensure notational consistency, using linear interpolation from Equation 3:

$$r'_i = \text{lerp}_{r'}(x'_i, x'_{i-1})W_{r'} \in \mathbb{R}^D$$ (10)

$$k'_i = \text{lerp}_{k'}(x'_i, x'_{i-1})W_{k'} \in \mathbb{R}^{3.5D}$$ (11)

$$v'_i = \text{ReLU}(k'_i)^2 W_{v'} \in \mathbb{R}^D$$ (12)

$$o'_i = \sigma(r'_i) \odot v'_i \in \mathbb{R}^D$$ (13)

## 4.2 Finch

### 4.2.1 Finch Token Shift

[p. 7] The data-dependent linear interpolation (ddlerp) between x_i and x_{i-1} used in Finch Token Shift is defined as:

$$\text{lora}_{\square}(x) = \lambda_{\square} + \tanh(xA_{\square})B_{\square}$$ (14)

$$\text{ddlerp}_{\square}(a, b) = a + (b - a) \odot \text{lora}_{\square}(a + (b - a) \odot \mu_{\square})$$ (15)
