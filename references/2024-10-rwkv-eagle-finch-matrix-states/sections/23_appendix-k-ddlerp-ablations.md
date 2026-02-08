# Appendix K: DDLerp Ablations [p. 41]

[p. 41] In order to demonstrate the specific benefit of our new DDLerp token shift over the Eagle LERP-based token shift we ran an ablation on DDLerp to demonstrate its benefit to each component. We trained a small 6 layer, d_model = 768 Finch model on the 1.6B token minipile (Kaddour, 2023) dataset at context length 512 and obtained the final validation loss results shown in 19. Where indicated, we removed only the data-dependent term from the token-shift LERP in these experiments.

### Table 19: Ablation Results on DDLerp [p. 41]

| Model | Final Validation Loss |
|-------|----------------------|
| Finch | 2.91 |
| Finch with DDLerp only on decay | 2.923 |
| Finch with no DDLerp at all | 2.926 |

Caption: Ablation Results on DDLerp for 6 layer 768 dimension Finch model
