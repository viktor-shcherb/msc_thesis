# Methodology [p. 3-5]

## 3.1 Preliminaries

[p. 3] RoPE formulation is introduced for hidden vector `h = [h0, h1, ..., h_{d-1}]` at position `m`.

Equation (1):

`f(h, m) = [h_even] ⊗ [cos(m theta_j)] + [h_odd_rot] ⊗ [sin(m theta_j)]`, where `theta_j = 10000^(-2j/d)`.

The paper writes this explicitly as paired 2D rotations across dimensions.

[p. 3] Attention score with RoPE is written as:

Equation (2):

`a(q, k) = <f(q, m), f(k, n)>`

`= sum_{j=0}^{d/2-1} [(q_{2j}k_{2j} + q_{2j+1}k_{2j+1}) cos((m-n)theta_j) + (q_{2j}k_{2j+1} - q_{2j+1}k_{2j}) sin((m-n)theta_j)]`

`:= g(q, k, theta, m-n)`

[p. 4] Problem setup: extend model context from original `Lc` to target `Lt`.

[p. 4] Position interpolation variants summarized:
- Linear interpolation: scale indices by `1/alpha`, `alpha = Lt/Lc`.
- NTK interpolation: modify RoPE base `10000 -> 10000*lambda`, `lambda = alpha^(d/(d-2))`.
- YaRN interpolation: dimension-wise mix of Linear and NTK plus temperature adjustment.

## 3.2 PoSE: Positional Skip-wise Training

[p. 4] PoSE design goals:
- Cover full target relative-position range `{1, ..., Lt-1}`.
- Preserve pre-training-like positional structure to avoid hurting original capabilities.

[p. 4] Chunking setup: split original window into `N` chunks `c0...c_{N-1}` with lengths `l0...l_{N-1}` and `sum l_i = Lc`.

Equation (3):

`Pos(c_i) = {st_i, st_i + 1, ..., st_i + l_i - 1},   st_i = sum_{j=0}^{i-1} l_j`

[p. 4] Sample skipping bias `u_i ~ U({u_{i-1}, ..., Lt-Lc})` and shift chunk positions:

Equation (4):

`PoSE(c_i) = {u_i + st_i, u_i + st_i + 1, ..., u_i + st_i + l_i - 1}`

Constraint: `u_i >= u_{i-1}` to avoid overlap across chunks.

[p. 5] Chunk content sampling from text `x = {x0, ..., x_{Lx}}`:

Equation (5):

`c_i = x[v_i + st_i : v_i + st_i + l_i]`

with `v_i ~ U({v_{i-1}, ..., Lx-Lc})` in the main method. Ablations also test `v_i = 0` and `v_i = u_i`.

[p. 5] Implementation choices:
- Initial biases: `u0 = 0`, `v0 = 0`.
- Default chunk number: `N = 2` (trade-off between coverage and preserving pre-training positional structure).
