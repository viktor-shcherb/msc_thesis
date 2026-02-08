# 5.2 Evaluation [p. 20]

[p. 20] Models are evaluated on the test sets of GSM8K (Grade school math) (Cobbe et al., 2021), MATH (Challenging competition math problems) (Hendrycks et al., 2021), Math401 (Arithmetic ability) (Yuan et al., 2023b), and Math23K (Chinese grade school math) (Wang et al., 2017). MATH-QWEN-CHAT is compared with proprietary models ChatGPT and Minerva (Lewkowycz et al., 2022) and open-sourced math-specialized model RFT (Yuan et al., 2023a), WizardMath (Luo et al., 2023a), and GAIRMath-Abel (Chern et al., 2023a) in Table 12. MATH-QWEN-CHAT models show better math reasoning and arithmetic abilities compared to open-sourced models and QWEN-CHAT models of similar sizes.

[p. 20] Compared to proprietary models, MATH-QWEN-7B-CHAT outperforms Minerva-8B in MATH. MATH-QWEN-14B-CHAT is chasing Minerva-62B and GPT-3.5 in GSM8K and MATH and delivers better performance on arithmetic ability and Chinese math problems.

## Table 12: Results of models on mathematical reasoning [p. 19]

The accuracy of QWEN is reported for all benchmarks using greedy decoding. For MATH, QWEN's performances on the test set from Lightman et al. (2023) are reported.

| Model | Params | GSM8K | MATH | Math401 | Math23K |
|---|---|---|---|---|---|
| *Proprietary models* | | | | | |
| GPT-4 | - | **92.0** | **42.5** | 83.5 | 74.0 |
| GPT-3.5 | - | 80.8 | 34.1 | 75.1 | 60.0 |
| Minerva | 8B | 16.2 | 14.1 | - | - |
| | 62B | 52.4 | 27.6 | - | - |
| | 540B | 58.8 | 33.6 | - | - |
| *Open-source models* | | | | | |
| LLaMA-1 RFT | 7B | 46.5 | 5.2 | - | - |
| | 13B | 52.1 | 5.1 | - | - |
| WizardMath | 7B | 54.9 | 10.7 | - | - |
| | 13B | 63.9 | 14.0 | - | - |
| | 70B | 81.6 | 22.7 | - | - |
| GAIRMath-Abel | 7B | 59.7 | 13.0 | - | - |
| | 13B | 66.4 | 17.3 | - | - |
| | 70B | 83.6 | 28.3 | - | - |
| QWEN-CHAT | 7B | 50.3 | 6.8 | 57.4 | 51.2 |
| | 14B | 60.1 | 18.4 | 70.1 | 67.0 |
| MATH-QWEN-CHAT | 7B | 62.5 | 17.2 | 80.8 | 75.4 |
| | 14B | 69.8 | 24.2 | **85.0** | **78.4** |
