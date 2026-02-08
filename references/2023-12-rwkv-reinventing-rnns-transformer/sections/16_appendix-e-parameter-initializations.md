# E Parameter Initializations [p. 17-18]

[p. 17-18]

The specific parameter initializations are described below, motivating the design choices. Parameters belonging to residual blocks are often adjusted by layer depth and total number of layers. Let $\#$ denote the vocabulary size, $s$ denote the embedding dimension, $d$ denote the hidden size (we use $d = 4s$), $L$ the number of layers, $l$ the layer index (from 0 to $L - 1$), we use the following initializations:

- Embeddings are initialized to $\mathcal{U}\ (\pm 1 \times 10^{-4})$ as explained in 3.4.

- For the time-mixing blocks (11, 12, 13), initializations are $\mu_{k_i} = \left(\frac{i}{s}\right)^{1-\frac{l}{L}}$, $\mu_{v_i} = \left(\frac{i}{s}\right)^{1-\frac{l}{L}} + \frac{0.3l}{L-1}$ and $\mu_{r_i} = \frac{1}{2} \cdot \left(\frac{i}{s}\right)^{1-\frac{l}{L}}$

- For the channel-mixing blocks (14, 15), $\mu_{k_i}$ and $\mu_{r_i}$ are initialized to $\left(\frac{i}{s}\right)^{1-\frac{l}{L}}$

- $w_i$ (16), also known as "time decay", is initialized to $-5 + 8 \cdot \left(\frac{i}{d-1}\right)^{0.7+\frac{1.3l}{L-1}}$. Intuitively, it is the discount factor applied to previous tokens over time.

- $u_i$ (16), also known as "bonus", is set to $0.5 \cdot (((i+1) \mod 3) - 1) + \log 0.3$. It is the special weighting applied to the current token in equation 16. The alternating zigzag pattern initially creates subtle variations in the tensor elements, which are intended to help the model treat different dimensions of the embedding distinctively.

- $W_o$ (17) (time-mixing) and $W_v$ (channel-mixing) are initialized to $\mathcal{N}(0, \sqrt{\frac{d}{s}} = 2)$

- All other $W_r, W_k, W_v$ weights are initialized to 0 so the model can start learning from the beginning without noisy signals.

- All LayerNorm weights start from 1 and biases from 0.
