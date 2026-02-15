# Appendix E: Experimental study of algorithm design [p. 20-23]

[p. 20-23] This appendix re-runs evaluations under design variations:
- Optimize task-specific metrics vs KL.
- Zero activation patching vs corrupted activation patching.
- Node-level ROC vs edge-level ROC.

## Quantitative summary tables

### Table 2: Random/Corrupted ablation (AUC)

| Metric | Task | ACDC(E) | HISP(E) | SP(E) |
|---|---|---:|---:|---:|
| KL | Docstring | 0.982 | 0.805 | 0.937 |
| KL | Greater-Than | 0.853 | 0.693 | 0.806 |
| KL | IOI | 0.869 | 0.789 | 0.823 |
| Loss | Tracr-Proportion | 0.679 | 0.679 | 0.525 |
| Loss | Tracr-Reverse | 0.200 | 0.577 | 0.193 |

### Table 3: Zero ablation (AUC)

| Metric | Task | ACDC(E) | HISP(E) | SP(E) |
|---|---|---:|---:|---:|
| KL | Docstring | 0.906 | 0.805 | 0.428 |
| KL | Greater-Than | 0.701 | 0.693 | 0.163 |
| KL | IOI | 0.539 | 0.792 | 0.486 |
| Loss | Tracr-Proportion | 1.000 | 0.679 | 0.829 |
| Loss | Tracr-Reverse | 1.000 | 0.577 | 0.801 |

[p. 21-23] Reported qualitative pattern:
- KL is generally more stable than task-specific objectives.
- Zero ablation unexpectedly helps some toy settings (notably tracr), but harms some language-model settings.
