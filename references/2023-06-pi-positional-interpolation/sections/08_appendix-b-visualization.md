# Appendix B: Visualization of Quantities in Extrapolation Bound [p. 15–16]

[p. 15] As shown in Eqn. 8, the extrapolation bound contains the term $B(s) := \sum_{k=0}^{d/2-1} |A_{k+1}(s)|$ where $A_k(s) := \sum_{j=0}^{k-1} e^{\mathrm{i}s\theta_j}$. Here the authors check how large the bound is. They use $\theta_j = c^{-2j/d}$ with $c = 10000$ and $d = 4096/32 = 128$ (LLaMA-7B setting), and Fig. 5 shows that $B(s)/d$ almost always larger than 1 and in many places it is much larger than 1.

## Figure 5

**Figure 5** (p. 16): "The bound $B(s)/d$ decays with $s$. While the bounds goes down with large positional difference $s$, numerically $B(s)/d \geq 1$ and at many $s$ much larger than 1 (the dotted horizontal line). Please check Appendix C.2 for the source code used to draw the figure."

The figure plots $B(s)/d$ (y-axis, range approximately 0 to 16) versus Positional difference $s$ (x-axis, range 0 to approximately 4500). A dashed horizontal line at $B(s)/d = 1$ is shown. The curve shows high values near $s = 0$ (approximately 14-16), decaying rapidly, but with significant oscillations throughout. For most values of $s$, $B(s)/d$ remains above 1. Even at large $s$ values (around 3000-4500), the oscillations keep $B(s)/d$ mostly in the range of 2-5, well above the dashed line at 1. This confirms that the extrapolation bound from Eqn. 8 is numerically at least $d$ times $2 \max_j |h_j|$, making it at least ~600x larger than the interpolation bound. [p. 16]
