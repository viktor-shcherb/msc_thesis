# 3.3. Load Balance Consideration [p. 7]

[p. 7] Automatically learned routing strategies may encounter the issue of load imbalance, which manifests two notable defects. Firstly, there is a risk of routing collapse (Shazeer et al., 2017), i.e., the model always selects only a few experts, preventing other experts from sufficient training. Secondly, if experts are distributed across multiple devices, load imbalance can exacerbate computation bottlenecks.

## Expert-Level Balance Loss

[p. 7] In order to mitigate the risk of routing collapse, an expert-level balance loss is employed. The computation of the balance loss is as follows:

$$\mathcal{L}_{\text{ExpBal}} = \alpha_1 \sum_{i=1}^{N'} f_i P_i, \tag{12}$$

Expert-level balance loss: product of expert frequency $f_i$ and average routing probability $P_i$, summed over all $N'$ routed experts, scaled by $\alpha_1$.

$$f_i = \frac{N'}{K'T} \sum_{t=1}^{T} \mathbb{1}(\text{Token } t \text{ selects Expert } i), \tag{13}$$

Fraction of tokens routed to expert $i$, normalized so that a uniform distribution gives $f_i = 1$ for all experts.

$$P_i = \frac{1}{T} \sum_{t=1}^{T} s_{i,t}, \tag{14}$$

Average routing probability (affinity score) for expert $i$ across all $T$ tokens in the batch.

[p. 7] Where $\alpha_1$ is a hyper-parameter called expert-level balance factor, $N'$ is equal to $(mN - K_s)$ and $K'$ is equal to $(mK - K_s)$ for brevity. $\mathbb{1}(\cdot)$ denotes the indicator function.

## Device-Level Balance Loss

[p. 7] In addition to the expert-level balance loss, a device-level balance loss is introduced. When aiming to alleviate computation bottlenecks, it becomes unnecessary to enforce strict balance constraints at the expert level, because excessive constraints on load balance will compromise model performance. Instead, the primary objective is to ensure balanced computation across the devices. If all routed experts are partitioned into $D$ groups $\{\mathcal{E}_1, \mathcal{E}_2, ..., \mathcal{E}_D\}$, and each group is deployed on a single device, the device-level balance loss is computed as follows:

$$\mathcal{L}_{\text{DevBal}} = \alpha_2 \sum_{i=1}^{D} f'_i P'_i, \tag{15}$$

Device-level balance loss: product of device-level frequency and probability, summed over $D$ device groups, scaled by $\alpha_2$.

$$f'_i = \frac{1}{|\mathcal{E}_i|} \sum_{j \in \mathcal{E}_i} f_j, \tag{16}$$

Average expert frequency within device group $\mathcal{E}_i$.

$$P'_i = \sum_{j \in \mathcal{E}_i} P_j, \tag{17}$$

Sum of average routing probabilities for all experts in device group $\mathcal{E}_i$.

[p. 7] Where $\alpha_2$ is a hyper-parameter called device-level balance factor. In practice, a small expert-level balance factor is set to mitigate the risk of routing collapse, and meanwhile a larger device-level balance factor is set to promote balanced computation across the devices.
