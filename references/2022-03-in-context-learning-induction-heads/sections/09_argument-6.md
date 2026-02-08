# Argument 6: Extrapolation from small models suggests induction heads are responsible for the majority of in-context learning in large models [p. 28-29]

## Strength of argument for sub-claims [p. 28]

|                      | Small Attention-Only | Small with MLPs | Large Models |
|----------------------|----------------------|-----------------|--------------|
| Contributes Some     |                      |                 | Analogy      |
| Contributes Majority |                      |                 | Analogy      |

Note: The Small Attention-Only and Small with MLPs columns are left blank (grayed out in the original). This argument applies specifically to large models via analogy. [p. 28]

## Extended inference from prior arguments [p. 28]

This argument is really an extended inference from all the above arguments. Arguments 1-5 present fairly strong evidence that in small transformers (especially small attention-only models), induction heads are responsible for the majority of in-context learning, while for large transformers, the evidence is not as strong. To what extent can one reasonably infer from small models that the same thing is happening in larger models? The authors note this is obviously a matter of judgment. [p. 28]

## Analogous measurements across model scales [p. 28]

The measurements in the model analysis table look fully analogous between the small attention-only, small models with MLPs, and full-scale model cases. Provided there is more than one layer, all of them go through a phase change. All of them have the same sharp increase in in-context learning, with the same rough amounts before and after the transition. All of them trace similar paths in PCA space. All of them form induction heads. [p. 28]

If things change from the small model case to the large model case, where do they change? And why is there no visible sign of the change in all the measurements? [p. 28]

## Caveats [p. 28]

On the flip side, there are many cases where large models behave very differently than small models (see discussion of phase changes with respect to model size in Related Work). Extrapolating from small models to models many orders of magnitude larger is something one should do with caution. [p. 28]

## Alternative possibilities [p. 28]

The most compelling alternative possibility the authors see is that other composition mechanisms may also form during the phase change. Larger models have more heads, which gives them more capacity for other interesting Q-composition and K-composition mechanisms that small models cannot afford to express. If all "composition heads" form simultaneously during the phase change, then it is possible that above some size, non-induction composition heads could together account for more of the phase change and in-context learning improvement than induction heads do. [p. 28]
