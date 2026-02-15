# Gated Delta Networks [p. 3-6]

## 3.1 Formulation: Gated Delta Rule [p. 4]

As shown above, DeltaNet implements a first-order linear recurrence with generalized Householder transition matrices $(1 - \beta_t \boldsymbol{k}_t \boldsymbol{k}_t^{\top})$ [p. 4]. Despite demonstrating superior associative recall and language modeling performance (Schlag et al., 2021a), DeltaNet received limited attention due to computational inefficiency until Yang et al. (2024b) introduced a hardware-efficient chunkwise training algorithm, as detailed below [p. 4].

### Chunkwise parallel form [p. 4]

By partially expanding the recurrence, we have [p. 4]:

$$\mathbf{S}_{[t]}^r = \mathbf{S}_{[t]} \left(\prod_{i=1}^{r} \mathbf{I} - \beta_{[t]}^i \boldsymbol{k}_{[t]}^i \boldsymbol{k}_{[t]}^{i\top}\right) + \sum_{i=1}^{r} \left(\beta_{[t]}^i \boldsymbol{v}_{[t]}^i \boldsymbol{k}_{[t]}^{i\top} \prod_{j=i+1}^{r} \left(\mathbf{I} - \beta_{[t]}^j \boldsymbol{k}_{[t]}^j \boldsymbol{k}_{[t]}^{j\top}\right)\right) \quad (3)$$

$$= \underbrace{\mathbf{S}_{[t]} \mathbf{P}_{[t]}^r}_{\mathbf{P}_{[t]}^r} + \underbrace{\sum_{i=1}^{r} \beta_{[t]}^i \boldsymbol{v}_{[t]}^i \boldsymbol{k}_{[t]}^{i\top} \mathbf{H}_{[t]}^r}_{\mathbf{H}_{[t]}^r}$$

where $\mathbf{P}_{[t]}^r$ involves cumulative products of generalized Householder matrices, which could be optimized by the classical WY representation (Bischof & Loan, 1985) [p. 4]:

$$\mathbf{P}_{[t]}^r = \mathbf{I} - \sum_{i=1}^{r} \mathbf{w}_{[t]}^i \boldsymbol{k}_{[t]}^{i\top} \in \mathbb{R}^{d_k \times d_k}, \qquad \mathbf{w}_{[t]}^r = \beta_{[t]}^r \left(\boldsymbol{k}_{[t]}^r - \sum_{i=1}^{r-1} \left(\mathbf{w}_{[t]}^i (\boldsymbol{k}_{[t]}^{i\top} \boldsymbol{k}_{[t]}^r)\right)\right) \in \mathbb{R}^{d_k} \quad (4)$$

Likewise, $\mathbf{H}_{[t]}^r$ could be represented as [p. 4]:

$$\mathbf{H}_{[t]}^r = \sum_{i=1}^{r} \mathbf{u}_{[t]}^i \boldsymbol{k}_{[t]}^{i\top} \in \mathbb{R}^{d_v \times d_k}, \qquad \mathbf{u}_{[t]}^r = \beta_{[t]}^r \left(\boldsymbol{v}_{[t]}^r - \sum_{i=1}^{r-1} \left(\mathbf{u}_{[t]}^i (\boldsymbol{k}_{[t]}^{i\top} \boldsymbol{k}_{[t]}^r)\right)\right) \in \mathbb{R}^{d_v} \quad (5)$$

and in matrix form: $\mathbf{P}_{[t]} = \mathbf{I} - \mathbf{W}_{[t]}^{\top} \mathbf{K}_{[t]} \in \mathbb{R}^{d_k \times d_k}$, $\mathbf{H}_{[t]} = \mathbf{U}_{[t]}^{\top} \mathbf{K}_{[t]} \in \mathbb{R}^{d_v \times d_k}$ [p. 4]. By using the UT transform (Joffrain et al., 2006), we can further write $\mathbf{W}$ and $\mathbf{U}$ in matrix form [p. 4]:

$$\mathbf{T}_{[t]} = \left[\mathbf{I} + \text{strictLower}\left(\text{diag}(\beta_{[t]}) \mathbf{K}_{[t]} \mathbf{K}_{[t]}^{\top}\right)\right]^{-1} \text{diag}(\beta_{[t]}) \in \mathbb{R}^{C \times C} \quad (6)$$

$$\mathbf{W}_{[t]} = \mathbf{T}_{[t]} \mathbf{K}_{[t]} \in \mathbb{R}^{C \times d_k}, \qquad \mathbf{U}_{[t]} = \mathbf{T}_{[t]} \mathbf{V}_{[t]} \in \mathbb{R}^{C \times d_v} \quad (7)$$

Substituting these back into Eq. 3 yields a hardware-efficient chunkwise algorithm for DeltaNet that leverages matmuls, enabling tensor core based GPU optimization [p. 4]:

$$\mathbf{S}_{[t+1]} = \mathbf{S}_{[t]} \mathbf{P}_{[t]} + \mathbf{H}_{[t]} = \mathbf{S}_{[t]} + \left(\mathbf{U}_{[t]} - \mathbf{W}_{[t]} \mathbf{S}_{[t]}^{\top}\right)^{\top} \mathbf{K}_{[t]} \qquad \in \mathbb{R}^{d_v \times d_k} \quad (8)$$

$$\mathbf{O}_{[t]} = \mathbf{Q}_{[t]} \mathbf{S}_{[t]}^{\top} + (\mathbf{Q}_{[t]} \mathbf{K}_{[t]}^{\top} \odot \mathbf{M}) \left(\mathbf{U}_{[t]} - \mathbf{W}_{[t]} \mathbf{S}_{[t]}^{\top}\right) \qquad \in \mathbb{R}^{C \times d_v} \quad (9)$$

### Proposed gated delta rule [p. 4]

The proposed gated delta rule is simple yet effective [p. 4]:

$$\mathbf{S}_t = \mathbf{S}_{t-1} \left(\alpha_t (1 - \beta_t \boldsymbol{k}_t \boldsymbol{k}_t^{\top})\right) + \beta_t \boldsymbol{v}_t \boldsymbol{k}_t^{\top} \quad (10)$$

where the data-dependent gating term $\alpha_t \in (0, 1)$ controls state decay [p. 4]. This formulation unifies the advantages of both gating mechanisms and the delta rule: the gating term enables adaptive memory management, while the delta update facilitates effective key-value association learning [p. 4].

We present a formal analysis of the gated delta rule through the lens of the online learning framework introduced by Liu et al. (2024) [p. 4]. In this framework, recurrent state updates emerge as *closed-form* solutions to an online learning problem, as shown in Table 1 [p. 4].

**Table 1** (p. 5): Comparison of different linear RNN models and their corresponding online learning objectives using the framework from Liu et al. (2024). For convenience, we simplify Longhorn's vector-valued $\beta$ to scalar $\beta$.

| Method | Online Learning Objective | Online Update |
|--------|---------------------------|---------------|
| LA | $\|\|\mathbf{S}_t - \mathbf{S}_{t-1}\|\|_F^2 - 2\langle\mathbf{S}_t\boldsymbol{k}_t, \boldsymbol{v}_t\rangle$ | $\mathbf{S}_t = \mathbf{S}_{t-1} + \boldsymbol{v}_t\boldsymbol{k}_t^{\top}$ |
| Mamba2 | $\|\|\mathbf{S}_t - \alpha_t\mathbf{S}_{t-1}\|\|_F^2 - 2\langle\mathbf{S}_t\boldsymbol{k}_t, \boldsymbol{v}_t\rangle$ | $\mathbf{S}_t = \alpha_t\mathbf{S}_{t-1} + \boldsymbol{v}_t\boldsymbol{k}_t^{\top}$ |
| Longhorn | $\|\|\mathbf{S}_t - \mathbf{S}_{t-1}\|\|_F^2 - \beta_t\|\langle\mathbf{S}_t\boldsymbol{k}_t - \boldsymbol{v}_t\|\|^2$ | $\mathbf{S}_t = \mathbf{S}_{t-1} - (1 - \epsilon\boldsymbol{k}_t)\boldsymbol{k}_t^{\top} + \epsilon_t\boldsymbol{v}_t\boldsymbol{k}_t^{\top}, \epsilon_t = \frac{\beta_t}{1 + \beta_t\boldsymbol{k}_t^{\top}\boldsymbol{k}_t}$ |
| DeltaNet | $\|\|\mathbf{S}_t - \mathbf{S}_{t-1}\|\|_F^2 - 2\langle\mathbf{S}_t\boldsymbol{k}_t, \boldsymbol{v}_t\rangle + (\boldsymbol{v}_t - \mathbf{S}_{t-1}\boldsymbol{k}_t)^{\top}$ | $\mathbf{S}_t = \mathbf{S}_{t-1} - (1 - \beta_t\boldsymbol{k}_t)\boldsymbol{k}_t^{\top} + \beta_t\boldsymbol{v}_t\boldsymbol{k}_t^{\top}$ |
| Gated DeltaNet | $\|\|\mathbf{S}_t - \alpha_t\mathbf{S}_{t-1}\|\|_F^2 - 2\langle\mathbf{S}_t\boldsymbol{k}_t, \boldsymbol{v}_t\rangle + (\boldsymbol{v}_t - \alpha_t\mathbf{S}_{t-1}\boldsymbol{k}_t)^{\top}$ | $\mathbf{S}_t = \mathbf{S}_{t-1}\left(\alpha_t(1 - \beta_t\boldsymbol{k}_t\boldsymbol{k}_t^{\top})\right) + \beta_t\boldsymbol{v}_t\boldsymbol{k}_t^{\top}$ | Recent linear RNN architectures typically incorporate a regularization term in their online learning objective to prevent state divergence from previous values, thereby enabling better memory retention [p. 4]. However, this mechanism becomes problematic when the state becomes saturated with information. In such cases, each state would encode a superposition of multiple information pieces, making precise retrieval challenging [p. 4]. To address this limitation, Mamba2 and Gated DeltaNet introduce an adaptive scaling factor $\alpha_t$ that relaxes the regularization term, allowing controlled deviations between $\mathbf{S}_t$ and $\mathbf{S}_{t-1}$ [p. 4]. This modification enables dynamic memory management through selective forgetting, which could be useful in filtering out irrelevant information (see §3.2) [p. 4].

On the other hand, Linear Attention (LA) and Mamba2 use a simple negative inner-product loss $-\langle\mathbf{S}_t\boldsymbol{k}_t, \boldsymbol{v}_t\rangle$, while Longhorn (Liu et al., 2024) uses a more expressive online regression objective $\|\mathbf{S}_t\boldsymbol{k}_t - \boldsymbol{v}_t\|^2$ for better modeling of key-value associations [p. 5]. The resulting Longhorn's update rule closely resembles the delta update rule,[^3] suggesting the superiority of the (gated) delta rule over Mamba2 in in-context associative recall [p. 5].

[^3]: The theoretical distinction lies in the optimization approach: Longhorn uses implicit online learning (Kulis & Bartlett, 2010) to derive closed-form globally optimal updates, while DeltaNet optimizes the same objective through one-step explicit gradient descent, as noted by Liu et al. (2024). [p. 5, footnote 3]

### Fast weight programming and SGD perspective [p. 5]

From the perspective of fast weight programming (Irie et al., 2022a) and test-time training (Sun et al., 2024a) and regression (Wang et al., 2025), the hidden state $\mathbf{S}$ can be interpreted as a (fast) weight matrix, with the delta rule optimizing the online regression objective $\mathcal{L}(\mathbf{S}_t) = \frac{1}{2}\|\mathbf{S}_t\boldsymbol{k}_t - \boldsymbol{v}_t\|^2$ via *test-time* stochastic gradient descent (SGD) [p. 5]:

$$\mathbf{S}_{t+1} = \mathbf{S}_t - \beta_t \nabla \mathcal{L}(\mathbf{S}_t) = \mathbf{S}_t - \beta_t (\mathbf{S}_t \boldsymbol{k}_t - \boldsymbol{v}_t) \boldsymbol{k}_t^{\top} = \mathbf{S}_t (\mathbf{I} - \beta_t \boldsymbol{k}_t \boldsymbol{k}_t^{\top}) + \beta_t \boldsymbol{v}_t \boldsymbol{k}_t^{\top}$$

where $\beta_t$ represents the (adaptive) learning rate [p. 5]. From this perspective, the gated delta rule can be viewed as incorporating an adaptive weight decay term $\alpha_t$ into the SGD update, a technique widely used in deep learning (Krogh & Hertz, 1991; Andriushchenko et al., 2023) [p. 5]. Concurrently, Titans (Behrouz et al., 2024) demonstrated the effectiveness of incorporating weight decay mechanisms in RNN test-time SGD updates [p. 5].

## 3.2 Case Study: Single Needle in a Haystack (S-NIAH) [p. 5]

To better understand the complementary strength between the delta rule and the gated rule, we present a case study on the Single Needle in a Haystack (S-NIAH) benchmark suite from RULER (Hsieh et al., 2024), where a key-value pair acts as a needle in the haystack (context) and the model must recall the value when given the key [p. 5]. Table 2 presents the results and we draw three main observations [p. 5]:

**Table 2** (p. 5): Zero-shot performance comparison on S-NIAH benchmark suite for 1.3B models (see §4 for setups)

|  | S-NIAH-1<br>(pass-key retrieval) | S-NIAH-2<br>(number in haystack) | S-NIAH-3<br>(uuid in haystack) |
|--|--------------------------------|----------------------------------|-------------------------------|
| Model | 1K | 2K | 4K | 8K | 1K | 2K | 4K | 8K | 1K | 2K | 4K |
| DeltaNet | 97.4 | 96.8 | 99.0 | 98.8 | 93.4 | 45.6 | 18.6 | 14.4 | 85.2 | 47.0 | 22.4 |
| Mamba2 | 99.2 | 98.8 | 65.4 | 30.4 | 99.4 | 98.8 | 58.2 | 17.0 | 64.4 | 47.6 | 4.6 |
| Gated DeltaNet | 98.4 | 88.4 | 91.4 | 91.8 | 100.0 | 99.8 | 92.2 | 29.6 | 86.6 | 84.2 | 27.6 |

**Decay hurts memory retention.** In the simplest S-NIAH-1 setting with repeated synthetic context, models memorize minimal information, testing long-term retention [p. 5]. DeltaNet achieves near-perfect performance across all sequence lengths. Mamba2 degrades significantly beyond 2K sequences since it decays historical information too quickly, while Gated DeltaNet's degradation is less severe thanks to the use of gating [p. 5].

**Gating facilitates filtering.** In S-NIAH-2/3 with real-world-essay context, models store all potentially relevant information, testing efficient memory management [p. 5]. With fixed state size, lack of clearance causes memory collision—information becomes superimposed and indistinguishable. DeltaNet's performance drops significantly at longer sequences due to poor memory clearance. Mamba2 and Gated DeltaNet maintain better performance through gating mechanisms that filter irrelevant information [p. 5].

**Delta rule helps memorization.** In S-NIAH-3, values change from numbers to UUIDs, testing complex pattern memorization [p. 5]. Mamba2's performance drops quickly, while Gated DeltaNet performs better, verifying that the delta rule helps with better memorization ability [p. 5-6].

## 3.3 Algorithm: Hardware-efficient Chunkwise Training [p. 6]

In this subsection, we derive a hardware-efficient chunkwise algorithm for training Gated DeltaNet [p. 6]. By partially expanding the recurrence in Eq. 10, we have [p. 6]:

$$\mathbf{S}_{[t]}^r = \mathbf{S}_{[t]} \left(\prod_{i=1}^{r} \alpha_{[t]}^i \left(\mathbf{I} - \beta_{[t]}^i \boldsymbol{k}_{[t]}^i \boldsymbol{k}_{[t]}^{i\top}\right)\right) + \sum_{i=1}^{r} \left(\beta_{[t]}^i \mathbf{v}_{[t]}^i \boldsymbol{k}_{[t]}^{i\top} \prod_{j=i+1}^{r} \alpha_{[t]}^j \left(\mathbf{I} - \beta_{[t]}^j \boldsymbol{k}_{[t]}^j \boldsymbol{k}_{[t]}^{j\top}\right)\right)$$

$$= \underbrace{\mathbf{S}_{[t]} \overrightarrow{\mathbf{P}}_{[t]}^r}_{\overrightarrow{\mathbf{P}}_{[t]}^r} + \underbrace{\sum_{i=1}^{r} \beta_{[t]}^i \mathbf{v}_{[t]}^i \boldsymbol{k}_{[t]}^{i\top} \overrightarrow{\mathbf{G}}_{[t]}^r}_{\overrightarrow{\mathbf{G}}_{[t]}^r}$$

It is easy to see that $\overrightarrow{\mathbf{P}}_{[t]}^r = \gamma_{[t]}^C \mathbf{P}_{[t]}^r = \overleftarrow{\mathbf{P}}_{[t]}^r$ [p. 6]. As for $\overrightarrow{\mathbf{G}}_{[t]}^r$, we adapt Eq. 5 as follows [p. 6]:

$$\overrightarrow{\mathbf{G}}_{[t]}^r = \sum_{i=1}^{r} \frac{\gamma_{[t]}^C}{\gamma_{[t]}^i} \overrightarrow{\mathbf{u}}_{[t]}^i \boldsymbol{k}_{[t]}^{i\top} \in \mathbb{R}^{d_v \times d_k}, \qquad \overrightarrow{\mathbf{u}}_{[t]}^r = \beta_{[t]}^r \left(\boldsymbol{v}_{[t]}^r - \sum_{i=1}^{r-1} \left(\overrightarrow{\mathbf{u}}_{[t]}^i (\frac{\gamma_{[t]}^r}{\gamma_{[t]}^i} \boldsymbol{k}_{[t]}^{i\top} \boldsymbol{k}_{[t]}^r)\right)\right) \in \mathbb{R}^{d_v}$$

(see §A for a proof) [p. 6]. By UT transform, we have the matrix form [p. 6]:

$$\overrightarrow{\mathbf{U}}_{[t]} = \left[\mathbf{I} + \text{strictLower}\left(\text{diag}(\beta_{[t]}) (\Gamma_{[t]} \odot \mathbf{K}_{[t]} \mathbf{K}_{[t]}^{\top})\right)\right]^{-1} \text{diag}(\beta_{[t]}) \mathbf{V}_{[t]} \qquad \in \mathbb{R}^{C \times d_v}$$

Similar to how Mamba2 extends linear attention (Eq. 1), we can adapt DeltaNet's chunkwise algorithm (Eq. 8-9) for Gated DeltaNet to enable hardware-efficient training as follows [p. 6]:

$$\mathbf{S}_{[t+1]} = \overrightarrow{\mathbf{S}}_{[t]}^{\leftarrow} + \left(\overrightarrow{\mathbf{U}}_{[t]} - \overrightarrow{\mathbf{W}}_{[t]} \overrightarrow{\mathbf{S}}_{[t]}^{\leftarrow\top}\right)^{\top} \overleftarrow{\mathbf{K}}_{[t]}^{\leftarrow} \qquad \in \mathbb{R}^{d_v \times d_k}$$

$$\mathbf{O}_{[t]} = \overrightarrow{\mathbf{Q}}_{[t]} \overrightarrow{\mathbf{S}}_{[t]}^{\top} + (\mathbf{Q}_{[t]} \mathbf{K}_{[t]}^{\top} \odot \mathbf{M}) \left(\overrightarrow{\mathbf{U}}_{[t]} - \overrightarrow{\mathbf{W}}_{[t]} \overrightarrow{\mathbf{S}}_{[t]}^{\leftarrow\top}\right) \qquad \in \mathbb{R}^{C \times d_v}$$

where $\overrightarrow{\boldsymbol{q}}_{[t]}^r = \gamma_{[t]}^C \boldsymbol{q}_{[t]}^r$, $\overrightarrow{\mathbf{w}}_{[t]}^r = \gamma_{[t]}^C \mathbf{w}_{[t]}^r$, $\overleftarrow{\boldsymbol{k}}_{[t]}^r = \frac{\gamma_{[t]}^C}{\gamma_{[t]}^r} \boldsymbol{k}_{[t]}^r$, and $\overrightarrow{\mathbf{S}}_{[t]}^{\leftarrow} = \gamma_{[t]}^C \mathbf{S}_{[t]}$ like we defined in Eq. 2 [p. 6].

## 3.4 Gated Delta Networks and Hybrid Models [p. 6]

### Token mixer block [p. 6]

The basic Gated DeltaNet follows Llama's macro architecture, stacking token mixer layers with SwiGLU MLP layers, but replaces self-attention with gated delta rule token mixing [p. 6]. Fig. 1 (right) shows its block design. For the gated delta rule design (Eq. 10), queries, keys and values $\{\boldsymbol{q}, \boldsymbol{k}, \boldsymbol{v}\}$ are generated through linear projection, short convolution and SiLU, with L2 normalization applied to $\boldsymbol{q}, \boldsymbol{k}$ for training stability [p. 6]. Following Sun et al. (2023a), the output is processed through normalization and gating before applying output projection [p. 6].

### Hybrid models [p. 6]

Linear transformers have limitations in modeling local shifts and comparisons, and their fixed state size makes it hard for retrieval tasks (Arora et al., 2024a) [p. 6]. Following recent hybrid architectures like Griffin (De et al., 2024) and Samba (Ren et al., 2024), we combine linear recurrent layers with sliding window attention (SWA), resulting in GatedDeltaNet-H1 [p. 6]. We also stack Mamba2, GatedDeltaNet and SWA, resulting in GatedDeltaNet-H2 [p. 6].
