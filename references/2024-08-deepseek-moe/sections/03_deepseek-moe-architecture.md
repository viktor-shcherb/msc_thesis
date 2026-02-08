# 3. DeepSeekMoE Architecture [p. 5-6]

[p. 5] On top of the generic MoE architecture outlined in Section 2, DeepSeekMoE is specifically designed to exploit the potential of expert specialization. As illustrated in Figure 2, the architecture incorporates two principal strategies: fine-grained expert segmentation and shared expert isolation. Both strategies are designed to elevate the level of expert specialization.

## 3.1. Fine-Grained Expert Segmentation

[p. 5] In scenarios where the number of experts is limited, tokens assigned to a particular expert will be more likely to cover diverse types of knowledge. The designated expert will intend to learn vastly different types of knowledge in its parameters, and they are hard to be simultaneously utilized. However, if each token can be routed to more experts, diverse knowledge will gain the potential to be decomposed and learned in different experts respectively. In this context, each expert can still retain a high level of expert specialization, contributing to a more focused knowledge distribution across experts.

[p. 5] While maintaining a consistent number of expert parameters and computational cost, the experts are segmented with a finer grain. To be specific, on top of a typical MoE architecture shown in Figure 2(a), each expert FFN is segmented into $m$ smaller experts by reducing the FFN intermediate hidden dimension to $\frac{1}{m}$ times its original size. Since each expert becomes smaller, the number of activated experts is increased to $m$ times to keep the same computation cost, as illustrated in Figure 2(b).

[p. 6] With the fine-grained expert segmentation, the output of an MoE layer can be expressed as:

$$\mathbf{h}_t^l = \sum_{i=1}^{mN} \left(g_{i,t} \, \text{FFN}_i\left(\mathbf{u}_t^l\right)\right) + \mathbf{u}_t^l, \tag{6}$$

Weighted sum over $mN$ fine-grained experts plus residual connection.

$$g_{i,t} = \begin{cases} s_{i,t}, & s_{i,t} \in \text{Topk}(\{s_{j,t} | 1 \leqslant j \leqslant mN\}, mK), \\ 0, & \text{otherwise}, \end{cases} \tag{7}$$

Gate value: retains affinity score if among top-$mK$ of $mN$ fine-grained experts.

$$s_{i,t} = \text{Softmax}_i\left(\mathbf{u}_t^{l^T} \mathbf{e}_i^l\right), \tag{8}$$

Token-to-expert affinity, same form as Eq. 5 but over fine-grained experts.

[p. 6] Where the total number of expert parameters is equal to $N$ times the number of parameters in a standard FFN, and $mN$ denotes the total number of fine-grained experts. With the fine-grained expert segmentation strategy, the number of nonzero gates will also increase to $mK$.

### Combinatorial Flexibility

[p. 6] From a combinatorial perspective, the fine-grained expert segmentation strategy substantially enhances the combinatorial flexibility of activated experts. As an illustrative example, consider the case where $N = 16$. A typical top-2 routing strategy can yield $\binom{16}{2} = 120$ possible combinations. By contrast, if each expert is split into 4 smaller experts, the fine-grained routing strategy can yield $\binom{64}{8} = 4,426,165,368$ potential combinations. The surge in combinatorial flexibility enhances the potential for achieving more accurate and targeted knowledge acquisition.

## 3.2. Shared Expert Isolation

[p. 6] With a conventional routing strategy, tokens assigned to different experts may necessitate some common knowledge or information. As a result, multiple experts may converge in acquiring shared knowledge in their respective parameters, thereby resulting in redundancy in expert parameters. However, if there are shared experts dedicated to capturing and consolidating common knowledge across varying contexts, the parameter redundancy among other routed experts will be alleviated. This alleviation of redundancy will contribute to a more parameter-efficient model with more specialized experts.

[p. 6] Towards this objective, in addition to the fine-grained expert segmentation strategy, $K_s$ experts are further isolated to serve as shared experts. Regardless of the router module, each token will be deterministically assigned to these shared experts. In order to maintain a constant computational cost, the number of activated experts among the other routed experts will be decreased by $K_s$, as depicted in Figure 2(c).

With the shared expert isolation strategy integrated, an MoE layer in the complete DeepSeekMoE architecture is formulated as follows:

$$\mathbf{h}_t^l = \sum_{i=1}^{K_s} \text{FFN}_i\left(\mathbf{u}_t^l\right) + \sum_{i=K_s+1}^{mN} \left(g_{i,t} \, \text{FFN}_i\left(\mathbf{u}_t^l\right)\right) + \mathbf{u}_t^l, \tag{9}$$

Sum of shared expert outputs (always active) plus weighted sum of routed expert outputs plus residual.

$$g_{i,t} = \begin{cases} s_{i,t}, & s_{i,t} \in \text{Topk}(\{s_{j,t} | K_s + 1 \leqslant j \leqslant mN\}, mK - K_s), \\ 0, & \text{otherwise}, \end{cases} \tag{10}$$

Gate value for routed experts: top-$(mK - K_s)$ selected from the $mN - K_s$ routed experts.

$$s_{i,t} = \text{Softmax}_i\left(\mathbf{u}_t^{l^T} \mathbf{e}_i^l\right). \tag{11}$$

Token-to-expert affinity for routed experts.

[p. 6] In DeepSeekMoE, with $K_s$ shared experts:
- The total number of routed experts is $mN - K_s$.
- The number of nonzero gates is $mK - K_s$.

[p. 6] The prototype of shared expert isolation can be credited to Rajbhandari et al. (2022). The key distinction lies in the fact that they derive this strategy from an engineering perspective, while the DeepSeekMoE authors approach it from an algorithmic standpoint.

## Figures

**Figure 2** (p. 5): "Illustration of DeepSeekMoE. Subfigure (a) showcases an MoE layer with the conventional top-2 routing strategy. Subfigure (b) illustrates the fine-grained expert segmentation strategy. Subsequently, subfigure (c) demonstrates the integration of the shared expert isolation strategy, constituting the complete DeepSeekMoE architecture. It is noteworthy that across these three architectures, the number of expert parameters and computational costs remain constant."

- Subfigure (a) — **Conventional Top-2 Routing**: Shows Input Hidden flowing through a Router with $K = 2$ to $N$ experts (labeled 1, 2, ..., $N$), with outputs combined to produce Output Hidden. Two experts are selected and activated.
- Subfigure (b) — **Fine-Grained Expert Segmentation**: Shows Input Hidden flowing through a Router with $K = 4$ to $2N$ experts (labeled 1, 2, 3, 4, ..., $2N-1$, $2N$), with outputs combined to produce Output Hidden. Four smaller experts are selected (same total computation as (a)).
- Subfigure (c) — **Shared Expert Isolation (DeepSeekMoE)**: Shows Input Hidden flowing to both shared experts (green, always active; experts 1, 2) and through a Router with $K = 3$ to the remaining routed experts (labeled 3, 4, ..., $2N-1$, $2N$). Three routed experts are selected in addition to the shared experts. Across all three subfigures, the number of expert parameters and computational costs remain constant.
