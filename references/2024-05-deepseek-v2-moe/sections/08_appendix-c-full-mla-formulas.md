# Appendix C. Full Formulas of MLA [p. 31]

[p. 31] In order to demonstrate the complete computation process of MLA, its full formulas are provided:

$$\mathbf{c}_t^Q = W^{DQ} \mathbf{h}_t, \tag{37}$$

where Eq. (37) compresses the input hidden state into a latent vector for queries.

$$[\mathbf{q}_{t,1}^C; \mathbf{q}_{t,2}^C; ...; \mathbf{q}_{t,n_h}^C] = \mathbf{q}_t^C = W^{UQ} \mathbf{c}_t^Q, \tag{38}$$

where Eq. (38) up-projects the query latent vector and slices into per-head compressed query components.

$$[\mathbf{q}_{t,1}^R; \mathbf{q}_{t,2}^R; ...; \mathbf{q}_{t,n_h}^R] = \mathbf{q}_t^R = \text{RoPE}(W^{QR} \mathbf{c}_t^Q), \tag{39}$$

where Eq. (39) produces the decoupled multi-head RoPE queries from the compressed query latent.

$$\mathbf{q}_{t,i} = [\mathbf{q}_{t,i}^C; \mathbf{q}_{t,i}^R], \tag{40}$$

where Eq. (40) concatenates the compressed and RoPE query components for each head.

$$\boxed{\mathbf{c}_t^{KV}} = W^{DKV} \mathbf{h}_t, \tag{41}$$

where Eq. (41) compresses the input hidden state into a latent vector for keys and values. The boxed vector $\mathbf{c}_t^{KV}$ needs to be cached for generation.

$$[\mathbf{k}_{t,1}^C; \mathbf{k}_{t,2}^C; ...; \mathbf{k}_{t,n_h}^C] = \mathbf{k}_t^C = W^{UK} \mathbf{c}_t^{KV}, \tag{42}$$

where Eq. (42) up-projects the KV latent vector to produce per-head compressed key components.

$$\boxed{\mathbf{k}_t^R} = \text{RoPE}(W^{KR} \mathbf{h}_t), \tag{43}$$

where Eq. (43) produces the shared decoupled RoPE key. The boxed vector $\mathbf{k}_t^R$ also needs to be cached for generation.

$$\mathbf{k}_{t,i} = [\mathbf{k}_{t,i}^C; \mathbf{k}_t^R], \tag{44}$$

where Eq. (44) concatenates the compressed key and shared RoPE key for each head.

$$[\mathbf{v}_{t,1}^C; \mathbf{v}_{t,2}^C; ...; \mathbf{v}_{t,n_h}^C] = \mathbf{v}_t^C = W^{UV} \mathbf{c}_t^{KV}, \tag{45}$$

where Eq. (45) up-projects the KV latent vector to produce per-head value components.

$$\mathbf{o}_{t,i} = \sum_{j=1}^{t} \text{Softmax}_j\left(\frac{\mathbf{q}_{t,i}^T \mathbf{k}_{j,i}}{\sqrt{d_h + d_h^R}}\right) \mathbf{v}_{j,i}^C, \tag{46}$$

where Eq. (46) computes the scaled dot-product attention output for each head.

$$\mathbf{u}_t = W^O [\mathbf{o}_{t,1}; \mathbf{o}_{t,2}; ...; \mathbf{o}_{t,n_h}], \tag{47}$$

where Eq. (47) applies the output projection to the concatenated per-head outputs.

## Inference Optimization

[p. 31] The boxed vectors in blue ($\mathbf{c}_t^{KV}$ and $\mathbf{k}_t^R$) need to be cached for generation. During inference, the naive formula needs to recover $\mathbf{k}_t^C$ and $\mathbf{v}_t^C$ from $\mathbf{c}_t^{KV}$ for attention. Fortunately, due to the associative law of matrix multiplication, $W^{UK}$ can be absorbed into $W^{UQ}$, and $W^{UV}$ can be absorbed into $W^O$. Therefore, there is no need to compute keys and values out for each query. Through this optimization, the computational overhead for recomputing $\mathbf{k}_t^C$ and $\mathbf{v}_t^C$ during inference is avoided. [p. 31]
