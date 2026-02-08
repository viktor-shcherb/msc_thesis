# Appendix C. Training Benchmark Curves of DeepSeekMoE 16B [p. 32-33]

[p. 32-33] Benchmark curves during training of DeepSeekMoE 16B and DeepSeek 7B (Dense) are presented in Figure 7 for reference.

**Figure 7** (p. 33): "Benchmark curves during training of DeepSeekMoE 16B and DeepSeek 7B (Dense)."

- The figure contains 18 subplots (arranged in a 6x3 grid), each showing a different benchmark metric plotted against the number of training tokens (in billions, x-axis range 0 to 2000B).
- Two lines are plotted in each subplot:
  - DeepSeekMoE 16B (blue)
  - DeepSeek 7B (Dense) (orange/yellow)
- Benchmarks shown (all with y-axis = Performance):
  1. **HellaSwag (Acc.)**: DeepSeekMoE 16B consistently above DeepSeek 7B from early training; both rise from ~0.3-0.4 to ~0.7-0.77.
  2. **PIQA (Acc.)**: Both models converge to similar performance (~0.78-0.80); DeepSeekMoE 16B slightly higher.
  3. **ARC-easy (Acc.)**: Both models converge to ~0.65-0.68; comparable performance throughout training.
  4. **ARC-challenge (Acc.)**: Both converge to ~0.45-0.50; fluctuating curves, roughly comparable.
  5. **RACE-middle (Acc.)**: Both converge to ~0.55-0.63; DeepSeek 7B slightly higher later.
  6. **RACE-high (Acc.)**: Both converge to ~0.40-0.46; roughly comparable with some fluctuation.
  7. **DROP (EM)**: Both rise from ~0.05 to ~0.3; DeepSeek 7B slightly higher in later stages.
  8. **GSM8K (EM)**: Both rise from ~0 to ~0.15-0.19; DeepSeekMoE 16B slightly higher at end.
  9. **HumanEval (Pass@1)**: Both rise from ~0 to ~0.2-0.27; DeepSeekMoE 16B notably higher at end.
  10. **MBPP (Pass@1)**: Both rise from ~0.05 to ~0.35-0.39; DeepSeekMoE 16B slightly higher at end.
  11. **TriviaQA (EM)**: DeepSeekMoE 16B consistently above; both rise to ~0.55-0.65.
  12. **NaturalQuestions (EM)**: Both converge to ~0.20-0.25; DeepSeekMoE 16B slightly higher.
  13. **MMLU (Acc.)**: Both rise from ~0.25 to ~0.45-0.48; DeepSeek 7B slightly higher at end.
  14. **WinoGrande (Acc.)**: Both fluctuate around ~0.55-0.70; roughly comparable.
  15. **CLUEWSC (EM)**: Both show noisy curves rising from ~0.2 to ~0.5-0.6; similar performance.
  16. **CEval (Acc.)**: Both converge to ~0.35-0.45; DeepSeek 7B slightly higher at end.
  17. **CMMLU (Acc.)**: Both converge to ~0.35-0.47; DeepSeek 7B slightly higher at end.
  18. **CHID (Acc.)**: DeepSeekMoE 16B rises faster; both converge to ~0.85-0.90; DeepSeekMoE 16B higher.

- General trend: DeepSeekMoE 16B matches or exceeds DeepSeek 7B (Dense) on most benchmarks throughout training, despite using only about 40% of the computation. Notable advantages for DeepSeekMoE 16B are visible on knowledge-intensive tasks (HellaSwag, TriviaQA, CHID), while DeepSeek 7B shows slight advantages on multiple-choice tasks (MMLU, CEval, CMMLU).
