# Preliminary [p. 2-4]

## 2.1 Mamba2: Linear Attention with Decay [p. 2-3]

It is known that the linear transformer (Katharopoulos et al., 2020b) can be formulated as the following linear recurrence when excluding normalization and query/key activations [p. 2]:

$$\mathbf{S}_t = \mathbf{S}_{t-1} + \boldsymbol{v}_t \boldsymbol{k}_t^{\top} \in \mathbb{R}^{d_v \times d_k}, \qquad \boldsymbol{o}_t = \mathbf{S}_t \boldsymbol{q}_t \in \mathbb{R}^{d_v}$$

where $d_k$ and $d_v$ represent the (head) dimensions for query/key and value, respectively [p. 2]. By expanding the recurrence, we can express it in both vector form (left) and matrix form (right) as follows [p. 2]:

$$\boldsymbol{o}_t = \sum_{i=1}^{t} (\boldsymbol{v}_i \boldsymbol{k}_i^{\top}) \boldsymbol{q}_t = \sum_{i=1}^{t} \boldsymbol{v}_i (\boldsymbol{k}_i^{\top} \boldsymbol{q}_t) \in \mathbb{R}^{d_v}, \qquad \mathbf{O} = (\mathbf{Q} \mathbf{K}^{\top} \odot \mathbf{M}) \mathbf{V} \in \mathbb{R}^{L \times d_v}$$

where $L$ is the sequence length, and $\mathbf{M} \in \mathbb{R}^{L \times L}$ is the causal mask defined by $\mathbf{M}_{ij} = 0$ when $i < j$, and 1 otherwise [p. 2].

However, this vanilla linear attention underperforms Transformers in language modeling by a large margin [p. 2]. To address this, it is common to incorporate a scalar decay term to forget historical information. Here we take Mamba2 (Dao & Gu, 2024a) as an example, which can be represented by the following linear recurrence (up to specific parameterization) [p. 2]:

$$\mathbf{S}_t = \alpha_t \mathbf{S}_{t-1} + \boldsymbol{v}_t \boldsymbol{k}_t^{\top}, \qquad \boldsymbol{o}_t = \mathbf{S}_t \boldsymbol{q}_t$$

where $\alpha_t \in (0, 1)$ is a data-dependent scalar-valued decay term that varies with $t$ [p. 2]. Define the cumulative decay product $\gamma_j = \prod_{i=j}^{t} \alpha_i$, and by expanding the recurrence, we can express the result in both a vector form (left) and a matrix parallel form (right) [p. 2]:

$$\boldsymbol{o}_t = \sum_{i=1}^{t} \left(\frac{\gamma_i}{\gamma_1} \boldsymbol{v}_i \boldsymbol{k}_i^{\top}\right) \boldsymbol{q}_t = \sum_{i=1}^{t} \boldsymbol{v}_i \left(\frac{\gamma_i}{\gamma_1} \boldsymbol{k}_i^{\top} \boldsymbol{q}_t\right), \qquad \mathbf{O} = ((\mathbf{Q} \mathbf{K}^{\top}) \odot \Gamma) \mathbf{V}$$

Here, $\Gamma \in \mathbb{R}^{L \times L}$ is a decay-aware causal mask where $\Gamma_{ij} = \frac{\gamma_i}{\gamma_j}$ if $i \geq j$ and $\Gamma_{ij} = 0$ otherwise [p. 3]. The equivalence between these parallel and recurrent forms is also referred to as the state space duality (SSD) described in Dao & Gu (2024a). This recurrence structure appears in several other architectures including Gated RFA (Peng et al., 2021), xLSTM (Beck et al., 2024), and Gated RetNet (Sun et al., 2024b) [p. 3]. When $\gamma_t$ is data-dependent, this formulation reduces to RetNet (Sun et al., 2023a) and Lightning-Attention (Qin et al., 2024a) [p. 3]. Furthermore, if $\gamma_t$ is extended to matrix-valued rather than scalar-valued, efficient linear-time computation remains possible but parameterized with an outer-product structure, as demonstrated by Yang et al. (2024a) and used by Yang et al. (2024a); Peng et al. (2024b); Qin et al. (2024b); Zhang et al. (2024); Chou et al. (2024); He et al. (2025); Lu et al. (2025) [p. 3].

### Chunkwise training [p. 3]

However, both the recurrent and parallel forms are not ideal for efficient training (Hua et al., 2022b; Yang et al., 2024a), which motivates the use of the chunkwise parallel form (Hua et al., 2022b; Sun et al., 2023a,b) to enable hardware-efficient, linear-time training, as introduced below [p. 3]. To summarize, the chunkwise parallel form splits inputs and outputs into several chunks of size $C$, and computes outputs for each chunk based on the accumulated chunk state and the query/key/value blocks of the current chunk [p. 3]. Following the notation of Sun et al. (2023b); Yang et al. (2024a,b), we take the query block, denoted as an example, and denote the $r$-th query within chunk $t$ as $\boldsymbol{q}_{[t]}^r := \boldsymbol{q}_{C_{t-1}+r}$ [p. 3]. The initial state of chunk $t$ is defined as $\mathbf{S}_{[t]} := \mathbf{S}_{[t]}^0 = \mathbf{S}_{[t-1]}^C$ [p. 3]. By partially expanding the recurrence, we have [p. 3]:

$$\mathbf{S}_{[t]}^r = \mathbf{S}_{[t]} + \sum_{i=1}^{r} \boldsymbol{v}_{[t]}^i \boldsymbol{k}_{[t]}^{i\top} \in \mathbb{R}^{d_v \times d_k}, \qquad \boldsymbol{o}_{[t]}^r = \mathbf{S}_{[t]}^r \boldsymbol{q}_{[t]}^r = \mathbf{S}_{[t]} \boldsymbol{q}_{[t]}^r + \sum_{i=1}^{r} \boldsymbol{v}_{[t]}^i \left(\boldsymbol{k}_{[t]}^{i\top} \boldsymbol{q}_{[t]}^r\right) \in \mathbb{R}^{d_v}$$

Equivalently, in matrix form [p. 3]:

$$\mathbf{S}_{[t+1]} = \mathbf{S}_{[t]} + \mathbf{V}_{[t]} \mathbf{K}_{[t]}^{\top} \in \mathbb{R}^{d_v \times d_k}, \qquad \mathbf{O}_{[t]} = \mathbf{Q}_{[t]} \mathbf{S}_{[t]}^{\top} + \left(\mathbf{Q}_{[t]} \mathbf{K}_{[t]}^{\top} \odot \mathbf{M}\right) \mathbf{V}_{[t]} \in \mathbb{R}^{C \times d_v}$$

where $\mathbf{M} \in \mathbb{R}^{C \times C}$ is the causal mask [p. 3]. The above equations are rich in matrix multiplications (matmuls), allowing for tensor-core-based hardware optimization. This chunkwise algorithm could be easily extended to linear attention with decay [p. 3]:

$$\mathbf{S}_{[t+1]} = \overrightarrow{\mathbf{S}}_{[t]}^{\leftarrow} + \mathbf{V}_{[t]}^{\leftarrow} \mathbf{K}_{[t]}^{\leftarrow\top} \in \mathbb{R}^{d_v \times d_k}, \qquad \mathbf{O}_{[t]} = \overrightarrow{\mathbf{Q}}_{[t]} \overrightarrow{\mathbf{S}}_{[t]}^{\top} + \left(\mathbf{Q}_{[t]} \mathbf{K}_{[t]}^{\top} \odot \Gamma_{[t]}\right) \mathbf{V}_{[t]} \in \mathbb{R}^{C \times d_v} \quad (1)$$

where $(\Gamma_{[t]})_{ij} = \frac{\gamma_{[t]}^i}{\gamma_{[t]}^j}$, $\gamma_{[t]}^r = \prod_{j=C(t-1)+1}^{C(t-1)+r} \alpha_j$ [p. 3]. Here we use the left arrow ($\leftarrow$) or the right arrow ($\rightarrow$) to denote a variable decaying to the first position and the last position of each chunk, respectively [p. 3]:

$$\overrightarrow{\boldsymbol{q}}_{[t]}^r = \gamma_{[t]}^C \boldsymbol{q}_{[t]}^r \qquad \text{decaying each vector to the first position of chunk } t$$

$$\overleftarrow{\boldsymbol{k}}_{[t]}^r = \frac{\gamma_{[t]}^C}{\gamma_{[t]}^r} \boldsymbol{k}_{[t]}^r \qquad \text{decaying each vector to the last position of chunk } t$$

$$\overrightarrow{\mathbf{S}}_{[t]}^{\leftarrow} = \gamma_{[t]}^C \mathbf{S}_{[t]} \qquad \text{decaying the state matrix over the entire chunk } t \quad (2)$$

and likewise for other variables (e.g., $\overrightarrow{\boldsymbol{v}}$) [p. 3]. The SSD decomposition algorithm introduced in Mamba2 is largely equivalent to this chunkwise algorithm [p. 3]. For a more generalized approach, Yang et al. (2024a) proposed an extended chunkwise form of linear attention that incorporates time-grained decay mechanisms [p. 3].

## 2.2 Delta Networks: Linear Attention with Delta Rule [p. 3-4]

The delta update rule (Widrow et al., 1960; Schlag et al., 2021b) *dynamically* erases the value ($\boldsymbol{v}_t^{\text{old}}$) associated with the current input key ($\boldsymbol{k}_t$) and writes a new value ($\boldsymbol{v}_t^{\text{new}}$), which is a linear combination of the current input value and the old value based on the "writing strength" $\beta_t \in (0, 1)$:[^1] [p. 3]

$$\mathbf{S}_t = \mathbf{S}_{t-1} - (\mathbf{S}_{t-1} \boldsymbol{k}_t) \boldsymbol{k}_t^{\top} + (\beta_t \boldsymbol{v}_t + (1 - \beta_t) \mathbf{S}_{t-1} \boldsymbol{k}_t) \boldsymbol{k}_t^{\top} = \mathbf{S}_{t-1} + \beta_t \boldsymbol{v}_t \boldsymbol{k}_t^{\top}$$

$$= \underbrace{\mathbf{S}_{t-1} - (\mathbf{S}_{t-1} \boldsymbol{k}_t) \boldsymbol{k}_t^{\top}}_{\text{erase } \boldsymbol{v}_t^{\text{old}}} + \underbrace{\boldsymbol{v}_t^{\text{new}}}_{\boldsymbol{v}_t^{\text{new}}}$$

[^1]: Here we slightly abuse the notation of $\gamma$ to denote the cumulative product for each chunk (starting with the first position of each chunk separately) instead of the entire sequence.

[p. 3, footnote continues]: It is possible to set $\beta_t \in (0, 2)$ to allow negative eigenvalue to unlock the state tracking abilities of DeltaNet (Grazzi et al., 2024; Siems et al., 2025).
