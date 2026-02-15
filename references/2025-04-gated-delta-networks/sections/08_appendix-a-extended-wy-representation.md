# Appendix A: Extended WY Representation for Gated Delta Rule [p. 21]

To reduce notation clutter, we only consider the first chunk here [p. 21].

For $\mathbf{S}_t$, the extended WY representation is [p. 21]:

$$\mathbf{S}_t = \sum_{i=1}^t \frac{\gamma_t}{\gamma_i} \mathbf{u}_i \boldsymbol{k}_i^\top, \quad \mathbf{u}_t = \beta_t \left( \boldsymbol{v}_t - \sum_{i=1}^{t-1} \frac{\gamma_t}{\gamma_i} \mathbf{u}_i \boldsymbol{k}_i^\top \boldsymbol{k}_t \right)$$

We proof this by mathematical induction [p. 21].

## Proof [p. 21]

$$\mathbf{S}_{t+1} = \mathbf{S}_t \left( \alpha_{t+1} (1 - \beta_{t+1} \boldsymbol{k}_{t+1} \boldsymbol{k}_{t+1}^\top) \right) + \beta_{t+1} \boldsymbol{v}_{t+1} \boldsymbol{k}_{t+1}^\top$$

$$= \alpha_{t+1} (\sum_{i=1}^t \frac{\gamma_t}{\gamma_i} \mathbf{u}_i \boldsymbol{k}_i^\top) - \alpha_{t+1} \beta_{t+1} (\sum_{i=1}^t \frac{\gamma_t}{\gamma_i} \mathbf{u}_i \boldsymbol{k}_i^\top \boldsymbol{k}_{t+1} \boldsymbol{k}_{t+1}^\top) + \beta_{t+1} \boldsymbol{v}_{t+1} \boldsymbol{k}_{t+1}^\top$$

$$= \sum_{i=1}^t \frac{\gamma_{t+1}}{\gamma_i} \mathbf{u}_i \boldsymbol{k}_i^\top + \beta_{t+1} \left( \boldsymbol{v}_{t+1} - \sum_{i=1}^t \frac{\gamma_{t+1}}{\gamma_i} \mathbf{u}_i \boldsymbol{k}_i^\top \boldsymbol{k}_{t+1} \right) \boldsymbol{k}_{t+1}^\top$$

$$= \sum_{i=1}^t \frac{\gamma_{t+1}}{\gamma_i} \mathbf{u}_i \boldsymbol{k}_i^\top + \frac{\gamma_{t+1}}{\gamma_{t+1}} \underbrace{\mathbf{u}_{t+1}}_{\text{=1}} \boldsymbol{k}_{t+1}^\top$$

$$= \sum_{i=1}^{t+1} \frac{\gamma_{t+1}}{\gamma_i} \mathbf{u}_i \boldsymbol{k}_i^\top$$

∎
