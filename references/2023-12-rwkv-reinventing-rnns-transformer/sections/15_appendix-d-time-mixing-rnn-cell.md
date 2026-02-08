# D Time-Mixing Block as an RNN Cell [p. 17]

[p. 17]

As stated in 3.3, the RWKV time-mixing block can be formulated as an RNN, as the $WKV$ computation can be written in a recursive form:

$$a_0, b_0 = 0, \tag{19}$$

$$wkv_t = \frac{a_{t-1} + e^{u+k_t} \odot v_t}{b_{t-1} + e^{u+k_t}}, \tag{20}$$

$$a_t = e^{-w} \odot a_{t-1} + e^{k_t} \odot v_t, \tag{21}$$

$$b_t = e^{-w} \odot b_{t-1} + e^{k_t}. \tag{22}$$

The dataflow of the RNN-like time-mixing is shown in Figure 8, where the hidden states $h$ is the numerator-denominator tuple $(a, b)$.

**Figure 8** (p. 17): "RWKV time-mixing block formulated as an RNN cell. Color codes: yellow ($\mu$) denotes the token shift, red (1) denotes the denominator, blue (2) denotes the numerator, and pink (3) denotes the fraction computations in 16. $h$ denotes the numerator-denominator tuple."
- The figure shows a diagram with inputs $\mathbf{x}_{t-1}$ and $\mathbf{x}_t$ flowing through the time-mixing block. Token shift ($\mu$) is applied to produce $\mathbf{k}_t$, $\mathbf{v}_t$, $\mathbf{r}_t$. The hidden state $\mathbf{h}_{t-1}$ feeds into the numerator (blue, labeled 2) and denominator (red, labeled 1) computations. The $wkv_t$ value is computed and combined with $\sigma$ (sigmoid of $\mathbf{r}_t$) to produce output $\mathbf{o}_t$, which feeds into $\mathbf{h}_t$. The output is also gated to produce $\mathbf{h}_t$ (next hidden state).

## Numerical Stability Trick

To avoid overflow in calculating $e^{k_t}$, a numerical trick is used in the official implementation. Noticing that $a_1 = e^{k_1} \odot v_1$ and $b_1 = e^{k_1}$, we set $a'_1 = v_1, b'_1 = 1, p_1 = k_1$, where $p_t$ stores the shared exponents of $a_t$ and $b_t$. Now the above recursion can be converted into a numerical safe version, for each time step $t > 1$:

$$q := \max(p_{t-1}, u + k_t), \tag{23}$$

$$wkv_t = \frac{e^{p_{t-1}-q} \odot a'_{t-1} + e^{u+k_t-q} \odot v_t}{e^{p_{t-1}-q} \odot b'_{t-1} + e^{u+k_t-q}}. \tag{24}$$

The update to $a'_t$, $b'_t$, and their shared exponent is also carried out in a similar fashion:

$$q' := \max(p_{t-1} - w, k_t), \tag{25}$$

$$a'_t = e^{p_{t-1}-w-q'} \odot a'_{t-1} + e^{k_t-q'} \odot v_t, \tag{26}$$

$$b'_t = e^{p_{t-1}-w-q'} \odot b'_{t-1} + e^{k_t-q'}, \tag{27}$$

$$p_t = q'. \tag{28}$$

## Internal State

The RWKV model has an internal state that stores some previous information. In each layer, the internal state consists five parts, each of which is a vector with $D$ numbers, where $D$ is the model dimension. The five parts are:

- The current input of the Time-mix block $x_t$;
- The current input of the Channel-mix block $y_t$;
- The numerator of the $WKV$ value $a'_t$, as defined in equation (26);
- The denominator of the $WKV$ value $b'_t$, as defined in equation (27);
- An auxiliary state $p_t$ in (28), which is used for $WKV$ computation to maintain numerical precision.

This yields a total size of $5DL$ parameters. It is worth noting that in an algebraic context with infinite precision, the helper state $p_t$ can be ignored, and the $WKV$ numerator and denominator can be computed directly using equations (21) and (22), reducing the size of the internal state to $4DL$.
