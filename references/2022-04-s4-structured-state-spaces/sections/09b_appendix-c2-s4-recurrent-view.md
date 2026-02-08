# C.2 Computing the S4 Recurrent View [p. 21]

[p. 21]

This subsection proves Theorem 2, showing the efficiency of the S4 parameterization for computing one step of the recurrent representation (Section 2.3).

Recall that without loss of generality, we can assume that the state matrix $\boldsymbol{A} = \boldsymbol{\Lambda} - \boldsymbol{P}\boldsymbol{Q}^*$ is diagonal plus low-rank (DPLR), potentially over $\mathbb{C}$. The goal in this section is to explicitly write out a closed form for the discretized matrix $\overline{\boldsymbol{A}}$.

Recall from equation (3) that:

$$\overline{\boldsymbol{A}} = (\boldsymbol{I} - \Delta/2 \cdot \boldsymbol{A})^{-1}(\boldsymbol{I} + \Delta/2 \cdot \boldsymbol{A})$$

$$\overline{\boldsymbol{B}} = (\boldsymbol{I} - \Delta/2 \cdot \boldsymbol{A})^{-1}\Delta\boldsymbol{B}.$$

The two terms in the definition of $\overline{\boldsymbol{A}}$ are simplified independently.

## Forward Discretization

The first term is essentially the Euler discretization motivated in Section 2.3:

$$\boldsymbol{I} + \frac{\Delta}{2}\boldsymbol{A} = \boldsymbol{I} + \frac{\Delta}{2}(\boldsymbol{\Lambda} - \boldsymbol{P}\boldsymbol{Q}^*)$$

$$= \frac{\Delta}{2}\left[\frac{2}{\Delta}\boldsymbol{I} + (\boldsymbol{\Lambda} - \boldsymbol{P}\boldsymbol{Q}^*)\right]$$

$$= \frac{\Delta}{2}\boldsymbol{A}_0$$

where $\boldsymbol{A}_0$ is defined as the term in the final brackets.

## Backward Discretization

The second term is known as the Backward Euler's method. Although this inverse term is normally difficult to deal with, in the DPLR case we can simplify it using Woodbury's Identity (Proposition 4).

$$\left(\boldsymbol{I} - \frac{\Delta}{2}\boldsymbol{A}\right)^{-1} = \left(\boldsymbol{I} - \frac{\Delta}{2}(\boldsymbol{\Lambda} - \boldsymbol{P}\boldsymbol{Q}^*)\right)^{-1}$$

$$= \frac{2}{\Delta}\left[\frac{2}{\Delta} - \boldsymbol{\Lambda} + \boldsymbol{P}\boldsymbol{Q}^*\right]^{-1}$$

$$= \frac{2}{\Delta}\left[\boldsymbol{D} - \boldsymbol{D}\boldsymbol{P}\left(\boldsymbol{I} + \boldsymbol{Q}^*\boldsymbol{D}\boldsymbol{P}\right)^{-1}\boldsymbol{Q}^*\boldsymbol{D}\right]$$

$$= \frac{2}{\Delta}\boldsymbol{A}_1$$

where $\boldsymbol{D} = \left(\frac{2}{\Delta} - \boldsymbol{\Lambda}\right)^{-1}$ and $\boldsymbol{A}_1$ is defined as the term in the final brackets. Note that $(1 + \boldsymbol{Q}^*\boldsymbol{D}\boldsymbol{P})$ is actually a scalar in the case when the low-rank term has rank 1.

## S4 Recurrence

Finally, the full bilinear discretization can be rewritten in terms of these matrices as:

$$\overline{\boldsymbol{A}} = \boldsymbol{A}_1\boldsymbol{A}_0$$

$$\overline{\boldsymbol{B}} = \frac{2}{\Delta}\boldsymbol{A}_1\Delta\boldsymbol{B} = 2\boldsymbol{A}_1\boldsymbol{B}.$$

The discrete-time SSM (3) becomes:

$$x_k = \overline{\boldsymbol{A}}x_{k-1} + \overline{\boldsymbol{B}}u_k$$

$$= \boldsymbol{A}_1\boldsymbol{A}_0 x_{k-1} + 2\boldsymbol{A}_1\boldsymbol{B}u_k$$

$$y_k = \boldsymbol{C}x_k.$$

Note that $\boldsymbol{A}_0$, $\boldsymbol{A}_1$ are accessed only through matrix-vector multiplications. Since they are both DPLR, they have $O(N)$ matrix-vector multiplication, showing Theorem 2.
