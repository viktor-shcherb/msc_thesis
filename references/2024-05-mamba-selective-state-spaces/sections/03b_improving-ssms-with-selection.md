# Improving SSMs with Selection [p. 5-6]

## Section 3.2

[p. 5]

One method of incorporating a selection mechanism into models is by letting their parameters that affect interactions along the sequence (e.g. the recurrent dynamics of an RNN or the convolution kernel of a CNN) be input-dependent.

Algorithms 1 and 2 illustrate the main selection mechanism. The main difference is simply making several parameters $\Delta, \boldsymbol{B}, \boldsymbol{C}$ functions of the input, along with the associated changes to tensor shapes throughout. In particular, these parameters now have a length dimension $L$, meaning that the model has changed from time-invariant to time-varying. (Note that shape annotations were described in Section 2.) This loses the equivalence to convolutions (3) with implications for its efficiency, discussed next. [p. 5]

The specific parameterization choices are: [p. 5]

- $s_B(x) = \text{Linear}_N(x)$
- $s_C(x) = \text{Linear}_N(x)$
- $s_\Delta(x) = \text{Broadcast}_D(\text{Linear}_1(x))$
- $\tau_\Delta = \text{softplus}$

where $\text{Linear}_d$ is a parameterized projection to dimension $d$. The choice of $s_\Delta$ and $\tau_\Delta$ is due to a connection to RNN gating mechanisms explained in Section 3.5.

## Algorithm 1: SSM (S4) vs. Algorithm 2: SSM + Selection (S6)

[p. 6]

**Algorithm 1** SSM (S4):

| Step | Operation |
|------|-----------|
| **Input:** | $x : (B, L, D)$ |
| **Output:** | $y : (B, L, D)$ |
| 1: | $\boldsymbol{A} : (D, N) \leftarrow \text{Parameter}$ |
| | (Represents structured $N \times N$ matrix) |
| 2: | $\boldsymbol{B} : (D, N) \leftarrow \text{Parameter}$ |
| 3: | $\boldsymbol{C} : (D, N) \leftarrow \text{Parameter}$ |
| 4: | $\Delta : (D) \leftarrow \tau_\Delta(\text{Parameter})$ |
| 5: | $\overline{\boldsymbol{A}}, \overline{\boldsymbol{B}} : (D, N) \leftarrow \text{discretize}(\Delta, \boldsymbol{A}, \boldsymbol{B})$ |
| 6: | $y \leftarrow \text{SSM}(\overline{\boldsymbol{A}}, \overline{\boldsymbol{B}}, \boldsymbol{C})(x)$ |
| | (Time-invariant: recurrence or convolution) |
| 7: | **return** $y$ |

**Algorithm 2** SSM + Selection (S6):

| Step | Operation |
|------|-----------|
| **Input:** | $x : (B, L, D)$ |
| **Output:** | $y : (B, L, D)$ |
| 1: | $\boldsymbol{A} : (D, N) \leftarrow \text{Parameter}$ |
| | (Represents structured $N \times N$ matrix) |
| 2: | $\boldsymbol{B} : (B, L, N) \leftarrow s_B(x)$ |
| 3: | $\boldsymbol{C} : (B, L, N) \leftarrow s_C(x)$ |
| 4: | $\Delta : (B, L, D) \leftarrow \tau_\Delta(\text{Parameter} + s_\Delta(x))$ |
| 5: | $\overline{\boldsymbol{A}}, \overline{\boldsymbol{B}} : (B, L, D, N) \leftarrow \text{discretize}(\Delta, \boldsymbol{A}, \boldsymbol{B})$ |
| 6: | $y \leftarrow \text{SSM}(\overline{\boldsymbol{A}}, \overline{\boldsymbol{B}}, \boldsymbol{C})(x)$ |
| | (Time-varying: recurrence (*scan*) only) |
| 7: | **return** $y$ |

Key differences between Algorithm 1 (S4) and Algorithm 2 (S6):
- In S4, $\boldsymbol{B}, \boldsymbol{C}, \Delta$ are learned parameters with shapes $(D, N)$, $(D, N)$, and $(D)$ respectively -- no dependence on input or sequence length.
- In S6, $\boldsymbol{B}, \boldsymbol{C}, \Delta$ are computed as functions of the input $x$, gaining shapes $(B, L, N)$, $(B, L, N)$, and $(B, L, D)$ -- they now vary across both batch and sequence length dimensions.
- The discretized $\overline{\boldsymbol{A}}, \overline{\boldsymbol{B}}$ expand from $(D, N)$ in S4 to $(B, L, D, N)$ in S6.
- S4 can use either recurrence or convolution (time-invariant); S6 can only use recurrence via scan (time-varying).
