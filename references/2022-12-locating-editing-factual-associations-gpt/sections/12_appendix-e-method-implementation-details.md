# Appendix E: Method Implementation Details [p. 25-26]

## E.1 Fine-Tuning Baselines (FT, FT+L)

[p. 25] FT:

- Adam with early stopping,
- one-layer MLP intervention,
- GPT-2 XL best FT layer reported as layer 1 (from sweep),
- learning rate `5e-4`, early-stop loss `0.03`.

[p. 25] FT+L:

- L-infinity constrained fine-tuning (`||theta' - theta||_inf <= epsilon`),
- GPT-2 XL selected: layer 0, epsilon `5e-4`.

## E.2-E.4 KN / KE / MEND

[p. 25-26] KN uses gradient-attribution-selected neurons with scaled embedding updates.

[p. 26] KE/MEND: authors use reimplementations and additionally train task-specific versions (zsRE, COUNTERFACT) for fair comparison.

## E.5 ROME Implementation

[p. 26] Core settings:

- intervention at layer 18,
- second-moment statistics from 100,000 hidden-state samples over Wikipedia,
- key-selection prefix sampling includes multiple random-prefix lengths,
- value optimization with Adam (`lr=0.5`, weight decay `1.5e-3`, KL scale `1e2`), max 20 steps with early stop,
- reported edit runtime ~2s on NVIDIA A6000 for GPT-2 XL.
