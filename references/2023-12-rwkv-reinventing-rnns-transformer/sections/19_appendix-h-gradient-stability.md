# H Gradient Stability in RWKV [p. 19-20]

[p. 19-20]

This section presents a mathematical description of the gradient stability property in RWKV, focusing specifically on the time-mixing block. By gradient stability, the authors mean that if the inputs $x_t$ are bounded and the model parameters are fixed, then the gradients with respect to $W_k$ and $W_v$ are uniformly bounded for all $T$ (thus not exploding). Consequently, the amount each $x_t$ contributes to the gradient at $T$ can be controlled in a naturally decaying fashion by the weight decay mechanism $w$ (thus not vanishing unless desired).

The authors make the simplification that there are no token shifts; this will not affect the final conclusion. In this scenario, $wkv_T$ can be written as

$$wkv_T = \frac{\sum_{t=1}^T K_t^e \odot v_t}{\sum_{t=1}^T K_t^e} = \mathrm{E}(v_t) = \frac{\mathrm{S}(v_t)}{\mathrm{S}(1)}, \tag{29}$$

where

$$v_t = W_v x_t, \quad \frac{\partial(v_t)_i}{\partial(W_v)_{i,j}} = (x_t)_j,$$

$$K_t^e = e^{W_k x_t + w_{T,t}}, \quad \frac{\partial(K_t^e)_i}{\partial(W_k)_{i,j}} = (x_t)_j (K_t^e)_i,$$

and $\mathrm{S}(\cdot)$ and $\mathrm{E}(\cdot)$ are shorthand for denoting sums and averages over weights $K_t^e$.

The loss function at position $T$ can be written as

$$L_T = l(f(wkv_T), y_T). \tag{30}$$

Because $wkv_T$ relates to $(W_k)_{i,j}$ and $(W_v)_{i,j}$ only through the $i$-th channel $(wkv_T)_i$, we have

$$\frac{\partial L_T}{\partial (W_v)_{i,j}} = \frac{\partial L_T}{\partial (wkv_T)_i} \frac{\partial (wkv_T)_i}{\partial (W_v)_{i,j}} \tag{31}$$

The first part of the above equation contains trivial operations like output layers, and other layers of time-mixing, which can be proven inductively. The second part of the above equation can be bounded as

$$\left|\frac{\partial(wkv_T)_i}{\partial(W_v)_{i,j}}\right| = \left|\frac{\partial \mathrm{E}_i[(v_t)_i]}{\partial(W_v)_{i,j}}\right| = |\mathrm{E}_i[(x_t)_j]| \leq \max_t |(x_t)_j|, \tag{32}$$

which is irrelevant to $T$. Similarly,

$$\frac{\partial(wkv_T)_i}{\partial(W_k)_{i,j}} = \partial \frac{\mathrm{S}_i[(v_t)_i]}{\mathrm{S}_i(1)} / \partial(W_k)_{i,j}$$
$$= \frac{\mathrm{S}_i[(x_t)_j(v_t)_i]}{\mathrm{S}_i(1)} - \frac{\mathrm{S}_i[(x_t)_j]\mathrm{S}_i[(v_t)_i]}{\mathrm{S}_i(1)^2}$$
$$= \mathrm{E}_i[(x_t)_j(v_t)_i] - \mathrm{E}_i[(x_t)_j]\mathrm{E}_i[(v_t)_i]$$
$$= \mathrm{cov}_i((x_t)_j, (v_t)_i) \tag{33}$$

can also be bounded. Note that $wkv$'s softmax operation contains at least two non-zero terms ($u$ and $w$), so the above "covariance" will not degenerate into 0.
