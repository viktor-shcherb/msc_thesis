# Appendix A: Solving for Lambda Algebraically [p. 14]

[p. 14] Appendix A derives the ROME rank-one update from constrained least squares.

Key progression:

1. Start from normal equations for baseline memory fit: `W K K^T = V K^T` (Eq. 6).
2. Add equality constraint `W_hat k* = v*` (Eq. 7).
3. Form Lagrangian with multiplier `Lambda` and set gradient to zero (Eqs. 8-11).
4. Obtain rank-one form: `W_hat = W + Lambda (C^-1 k*)^T` with `C = K K^T` (Eq. 13).
5. Solve `Lambda` from constraint substitution:

`Lambda = (v* - W k*) / ((C^-1 k*)^T k*)` (Eq. 17).

[p. 14] Appendix states this is standard equality-constrained least squares specialized to the MLP-memory setting.
