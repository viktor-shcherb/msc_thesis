# 2.2 DeepSeekMoE: Training Strong Models at Economical Costs [p. 9-11]

## 2.2.1 Basic Architecture

[p. 9] For FFNs, the DeepSeekMoE architecture (Dai et al., 2024) is employed. DeepSeekMoE has two key ideas: segmenting experts into finer granularity for higher expert specialization and more accurate knowledge acquisition, and isolating some shared experts for mitigating knowledge redundancy among routed experts. With the same number of activated and total expert parameters, DeepSeekMoE can outperform conventional MoE architectures like GShard (Lepikhin et al., 2021) by a large margin. [p. 9]

Let $\mathbf{u}_t$ be the FFN input of the $t$-th token, we compute the FFN output $\mathbf{h}_t'$ as follows:

$$\mathbf{h}_t' = \mathbf{u}_t + \sum_{i=1}^{N_s} \text{FFN}_i^{(s)}(\mathbf{u}_t) + \sum_{i=1}^{N_r} g_{i,t}\, \text{FFN}_i^{(r)}(\mathbf{u}_t), \tag{20}$$

where Eq. (20) computes the FFN output as the sum of the input (residual), all shared expert outputs, and the gated routed expert outputs.

$$g_{i,t} = \begin{cases} s_{i,t}, & s_{i,t} \in \text{Topk}(\{s_{j,t} | 1 \leqslant j \leqslant N_r\}, K_r), \\ 0, & \text{otherwise}, \end{cases} \tag{21}$$

where Eq. (21) defines the gate value: equal to the affinity score if the expert is among the top-$K_r$ selected, zero otherwise.

$$s_{i,t} = \text{Softmax}_i\left(\mathbf{u}_t^T \mathbf{e}_i\right), \tag{22}$$

where Eq. (22) computes the token-to-expert affinity score as the softmax over inner products of the token representation and expert centroids.

Here $N_s$ and $N_r$ denote the numbers of shared and routed experts, respectively; $\text{FFN}_i^{(s)}(\cdot)$ and $\text{FFN}_i^{(r)}(\cdot)$ denote the $i$-th shared expert and the $i$-th routed expert, respectively; $K_r$ denotes the number of activated routed experts; $g_{i,t}$ is the gate value for the $i$-th expert; $s_{i,t}$ is the token-to-expert affinity; $\mathbf{e}_i$ is the centroid of the $i$-th routed expert in this layer; and $\text{Topk}(\cdot, K)$ denotes the set comprising $K$ highest scores among the affinity scores calculated for the $t$-th token and all routed experts. [p. 9]

## 2.2.2 Device-Limited Routing

[p. 9-10] For DeepSeek-V2, beyond the naive top-K selection of routed experts, it is additionally ensured that the target experts of each token will be distributed on at most $M$ devices. To be specific, for each token, the $M$ devices that have experts with the highest affinity scores are first selected. Then, top-K selection among experts is performed on these $M$ devices. In practice, when $M \geqslant 3$, the device-limited routing can achieve a good performance roughly aligned with the unrestricted top-K routing. [p. 10]

This mechanism is designed to bound MoE-related communication costs. When expert parallelism is employed, the routed experts will be distributed across multiple devices. For each token, its MoE-related communication frequency is proportional to the number of devices covered by its target experts. Due to the fine-grained expert segmentation in DeepSeekMoE, the number of activated experts can be large, so the MoE-related communication will be more costly if expert parallelism is applied. [p. 9]

## 2.2.3 Auxiliary Loss for Load Balance

[p. 10] The load balance is taken into consideration for automatically learned routing strategies. Unbalanced load will raise the risk of routing collapse (Shazeer et al., 2017), preventing some experts being fully trained and utilized. When expert parallelism is employed, unbalanced load will diminish computation efficiency. During the training of DeepSeek-V2, three kinds of auxiliary losses are designed for controlling expert-level load balance ($\mathcal{L}_{\text{ExpBal}}$), device-level load balance ($\mathcal{L}_{\text{DevBal}}$), and communication balance ($\mathcal{L}_{\text{CommBal}}$), respectively. [p. 10]

### Expert-Level Balance Loss

An expert-level balance loss (Fedus et al., 2021; Lepikhin et al., 2021) is used to mitigate the risk of routing collapse:

$$\mathcal{L}_{\text{ExpBal}} = \alpha_1 \sum_{i=1}^{N_r} f_i P_i, \tag{23}$$

where Eq. (23) computes the expert-level balance loss as the scaled dot product of expert load fractions and routing probabilities.

$$f_i = \frac{N_r}{K_r T} \sum_{t=1}^{T} \mathbb{1}(\text{Token } t \text{ selects Expert } i), \tag{24}$$

where Eq. (24) computes the fraction of tokens routed to expert $i$, normalized so that a uniform distribution gives $f_i = 1$.

$$P_i = \frac{1}{T} \sum_{t=1}^{T} s_{i,t}, \tag{25}$$

where Eq. (25) computes the average routing probability for expert $i$ across all tokens.

Here $\alpha_1$ is a hyper-parameter called expert-level balance factor; $\mathbb{1}(\cdot)$ denotes the indicator function; and $T$ denotes the number of tokens in a sequence. [p. 10]

### Device-Level Balance Loss

In addition to the expert-level balance loss, a device-level balance loss is designed to ensure balanced computation across different devices. In the training process of DeepSeek-V2, all routed experts are partitioned into $D$ groups $\{\mathcal{E}_1, \mathcal{E}_2, ..., \mathcal{E}_D\}$, and each group is deployed on a single device. The device-level balance loss is computed as follows:

$$\mathcal{L}_{\text{DevBal}} = \alpha_2 \sum_{i=1}^{D} f_i' P_i', \tag{26}$$

where Eq. (26) computes the device-level balance loss analogously to the expert-level loss but aggregated per device.

$$f_i' = \frac{1}{|\mathcal{E}_i|} \sum_{j \in \mathcal{E}_i} f_j, \tag{27}$$

where Eq. (27) computes the average expert load fraction across all experts on device $i$.

$$P_i' = \sum_{j \in \mathcal{E}_i} P_j, \tag{28}$$

where Eq. (28) sums the routing probabilities of all experts on device $i$.

Here $\alpha_2$ is a hyper-parameter called device-level balance factor. [p. 10]

### Communication Balance Loss

[p. 10-11] A communication balance loss is introduced to ensure that the communication of each device is balanced. Although the device-limited routing mechanism guarantees that the sending communication of each device is bounded, if a certain device receives more tokens than other devices, the practical communication efficiency will also be affected. The communication balance loss is designed as follows:

$$\mathcal{L}_{\text{CommBal}} = \alpha_3 \sum_{i=1}^{D} f_i'' P_i'', \tag{29}$$

where Eq. (29) computes the communication balance loss.

$$f_i'' = \frac{D}{MT} \sum_{t=1}^{T} \mathbb{1}(\text{Token } t \text{ is sent to Device } i), \tag{30}$$

where Eq. (30) computes the fraction of tokens sent to device $i$, normalized so that a uniform distribution gives $f_i'' = 1$.

$$P_i'' = \sum_{j \in \mathcal{E}_i} P_j, \tag{31}$$

where Eq. (31) sums the routing probabilities of all experts on device $i$ (same as $P_i'$ in Eq. 28).

Here $\alpha_3$ is a hyper-parameter called communication balance factor. The device-limited routing mechanism operates on the principle of ensuring that each device transmits at most $MT$ hidden states to other devices. Simultaneously, the communication balance loss is employed to encourage each device to receive around $MT$ hidden states from other devices. The communication balance loss guarantees a balanced exchange of information among devices, promoting efficient communications. [p. 11]

## 2.2.4 Token-Dropping Strategy

[p. 11] While balance losses aim to encourage a balanced load, it is important to acknowledge that they cannot guarantee a strict load balance. In order to further mitigate the computation wastage caused by unbalanced load, a device-level token-dropping strategy is introduced during training. This approach first computes the average computational budget for each device, which means that the capacity factor for each device is equivalent to 1.0. Then, inspired by Riquelme et al. (2021), tokens with the lowest affinity scores on each device are dropped until reaching the computational budget. In addition, it is ensured that the tokens belonging to approximately 10% of the training sequences will never be dropped. In this way, the decision of whether to drop tokens during inference can be made flexibly according to the efficiency requirements, and consistency between training and inference is always ensured. [p. 11]
