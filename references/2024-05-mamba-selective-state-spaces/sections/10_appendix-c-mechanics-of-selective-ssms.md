# Appendix C: Mechanics of Selective SSMs [p. 27–28]

[p. 27]

*Proof of Theorem 1.* Consider a selective SSM (Algorithm 2) with $N = 1$, $\boldsymbol{A} = -1$, $\boldsymbol{B} = 1$, $s_\Delta = \text{Linear}(x)$, $\tau_\Delta = \text{softplus}$. The corresponding continuous-time SSM (1) is

$$\dot{h}(t) = -h(t) + x(t)$$

which is also called a *leaky integrator*.

The discretization step size is

$$\Delta_t = \tau_\Delta(\text{Parameter} + s_\Delta(x_t))$$
$$= \text{softplus}(\text{Parameter} + \text{Linear}(x_t))$$
$$= \text{softplus}(\text{Linear}(x_t))$$

where the authors observe that the parameter can be viewed as a learnable bias and folded into the linear projection.

Now applying the zero-order hold (ZOH) discretization formulas:

$$\overline{A}_t = \exp(\Delta A) = \frac{1}{1 + \exp(\text{Linear}(x_t))} = \sigma(-\text{Linear}(x_t))$$
$$= 1 - \sigma(\text{Linear}(x_t))$$

$$\overline{B}_t = (\Delta A)^{-1}(\exp(\Delta A) - I) \cdot \Delta B = -(\exp(\Delta A) - I) = 1 - \overline{A}$$
$$= \sigma(\text{Linear}(x_t)).$$

[p. 28]

Thus the final discrete recurrence (2a) is

$$g_t = \sigma(\text{Linear}(x_t))$$
$$h_t = (1 - g_t) h_{t-1} + g_t x_t$$

as desired. $\square$
