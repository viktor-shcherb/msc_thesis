# Appendix D: Details of Subnetwork Probing and HISP [p. 19]

## D.1 Subnetwork Probing modifications

[p. 19] Three modifications relative to Cao et al. (2021):
1. Remove linear probe training.
2. Optimize same metric as ACDC (KL or task-specific metric).
3. Replace zero-only masking with interpolation between clean and corrupted activations.

## D.2 HISP generalization

[p. 19] The original head-importance method is generalized beyond attention-head outputs to additional internal components.

Head/component importance formulation:

```text
I_C = (1/n) * sum_i (C(x_i)-C(x'_i))^T * (∂F(x_i)/∂C(x_i))
```

The paper notes this aligns with attribution-patching style first-order approximations (up to absolute-value conventions).
