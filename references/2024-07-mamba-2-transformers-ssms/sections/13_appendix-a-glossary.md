# A Glossary [p. 42]

[p. 42] **Table 8**: Glossary of notation and terminology; mnemonics bolded. (*Top*) Frequently used tensor dimensions. (*Bottom*) Matrices and tensors used in state space models or structured masked attention.

| Notation | Description | Definition |
|---|---|---|
| T | **T**ime axis or **t**arget sequence axis | Definition 2.1 |
| S | **S**ource sequence axis (in attention) | Equation (9) |
| D | Model **d**imension or `d_model` | Definition 7.1 |
| N | State/feature dimension or `d_state` | Equations (2) and (9) |
| P | Head dimension or `d_head` | Definition 2.1 |
| H | Number of **h**eads or `n_head` | Definition 7.1 |
| $M$ | Sequence transformation **m**atrix | Definition 2.3 |
| $A$ | Discrete SSM recurrent (state) matrix | Equation (2) |
| $B$ | State space model input projection (expansion) matrix | Equation (2) |
| $C$ | State space model output projection (contraction) matrix | Equation (2) |
| $X$ | Input matrix (shape (T, P)) | Equations (2) and (9) |
| $Y$ | Output matrix (shape (T, P)) | Equations (2) and (9) |
| $Q$ | Attention **q**uery matrix | Equation (9) |
| $K$ | Attention **k**ey matrix | Equation (9) |
| $V$ | Attention **v**alue matrix | Equation (9) |
| $G$ | Attention **G**ram matrix | $QK^\top$ (or $CB^\top$) |
| $L$ | (Structured) mask matrix (**l**ower-triangular in the causal setting) | Definition 4.2 |
