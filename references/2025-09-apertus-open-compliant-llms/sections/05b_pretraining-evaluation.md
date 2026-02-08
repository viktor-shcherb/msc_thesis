# 5.1 Pretraining Evaluation [p. 37–39]

## Scope [p. 37]

[p. 37] The model's capabilities acquired during pretraining are evaluated, focusing on two key areas: *"general language understanding"* and *"factual knowledge acquisition."* Given the interest in multilingual performance across both dimensions, the aim is to capture the nuances between language-agnostic factual knowledge, information that holds across languages, and region-specific factual knowledge, which reflects culturally or geographically grounded information tied to particular linguistic or cultural groups.

## Benchmarks [p. 37–38]

[p. 37–38] To evaluate language and general knowledge understanding, the following benchmarks are used: HellaSwag (Zellers et al., 2019), ARC (Clark et al., 2018), WinoGrande (Sakaguchi et al., 2019), XNLI (Conneau et al., 2018), PIQA (Bisk et al., 2020), and COPA (Roemmele et al., 2011) along with their multilingual variants. To assess language-agnostic factual recall and reasoning, MMLU (Hendrycks et al., 2021a) and Global-MMLU (Singh et al., 2025) are used. For region-specific factual knowledge, INCLUDE (Romanou et al., 2025), BLEnD (Myung et al., 2025), and CulturalBench (Chiu et al., 2025) are used. In addition, a custom benchmark *SwitzerlandQA* targeting Swiss regional knowledge is introduced, presented in English, Italian, French, German, and Romansh (Section K).

## Baseline Models [p. 38]

[p. 38] Apertus is compared against a set of pretrained fully open and open-weight models within the same scale class. The baseline models range in size from 1.7B to 72B parameters, and include both dense architectures and Mixture-of-Experts (MoE) variants.

The fully open models considered are:
- OLMo2 (OLMo et al., 2025)
- EuroLLM (Martins et al., 2025)
- SmoLM2 (Allal et al., 2025)
- SmolLLM3 (Bakouch et al., 2025)
- Poro (Luukkonen et al., 2024)

The open-weight pretrained models include:
- Llama3 (Grattafiori et al., 2024)
- Llama 4
- Qwen2.5 (Qwen et al., 2024)
- Qwen3 (Yang et al., 2025b)
- GPT-OSS (OpenAI et al., 2025)

## Evaluation Setup [p. 38]

[p. 38] For benchmark evaluation, EleutherAI's *lm-evaluation-harness*^45 framework (Gao et al., 2024) is used with probabilistic scoring. This approach is adopted during pretraining to provide a more sensitive measure of model progress than generation accuracy alone, which may remain low or change only gradually in early stages. By constraining answer options to the probability distribution over answer choices, the evaluation captures subtle improvements in the model's internal representations and reasoning, offering a finer-grained view of learning dynamics. All reported pretraining benchmarks follow the default configuration specified in *lm-evaluation-harness*.

^45: https://github.com/swiss-ai/lm-evaluation-harness

## Pretraining Evaluation Results [p. 38–39]

[p. 38–39] The Apertus family achieves state-of-the-art predictive quality across model sizes. Tables 14 and 15 present downstream evaluation results for the pretrained models. The models demonstrate strong performance on both general language understanding tasks and multilingual benchmarks. For example, Apertus-70B achieves the highest score among all evaluated models on the multilingual XCOPA benchmark, while both the 70B and 8B variants surpass all other fully open models on INCLUDE V1 (covering 44 languages) and INCLUDE V2 (covering 45 languages). This shows the strong multilingual capability of Apertus models.

Furthermore, Figure 7 illustrates the evolution of macro-averaged accuracy during training. The Apertus family shows consistently strong multilingual capabilities (Global, EU, Swiss Evaluation Macro) while maintaining highly competitive results in English.

---

**Table 14: Pretraining Evaluation** [p. 38]

Performance (%) of Apertus models on *general language understanding* tasks compared to other pretrained models. The arrows (up/down) show the desired direction for each benchmark.

| Model | Avg | ARC (up) | HellaSwag (up) | WinoGrande (up) | XNLI (up) | XCOPA (up) | PIQA (up) |
|---|---|---|---|---|---|---|---|
| **Fully Open Models** | | | | | | | |
| **Apertus-8B** | **65.8** | **72.7** | **59.8** | **70.6** | **45.2** | **66.5** | **79.8** |
| **Apertus-70B** | **67.5** | **70.6** | **64.0** | **73.3** | **45.3** | **69.8** | **81.9** |
| OLMo2-7B | 64.0 | 72.9 | 60.4 | 74.5 | 40.4 | 55.2 | 80.9 |
| OLMo2-32B | 67.7 | 76.2 | 66.7 | 78.6 | 42.9 | 60.1 | 82.1 |
| EuroLLM-1.7B | 54.8 | 57.2 | 44.9 | 58.1 | 40.7 | 55.7 | 72.4 |
| EuroLLM-9B | 62.8 | 67.9 | 57.9 | 68.8 | 41.5 | 61.1 | 79.6 |
| SmolLM2-1.7B | 58.5 | 66.1 | 52.4 | 65.6 | 37.6 | 52.3 | 77.0 |
| SmolLM3-3B | 61.6 | 68.6 | 56.4 | 68.1 | 40.5 | 58.2 | 77.7 |
| Poro-34B | 61.7 | 65.7 | 57.9 | 70.6 | 41.6 | 56.0 | 78.5 |
| **Open-Weight Models** | | | | | | | |
| Llama3.1-8B | 65.4 | 71.6 | 60.0 | 73.4 | 45.3 | 61.8 | 80.1 |
| Llama3.1-70B | 67.3 | 74.4 | 56.5 | 79.4 | 44.3 | 66.7 | 82.3 |
| Qwen2.5-7B | 64.4 | 69.6 | 60.1 | 72.8 | 43.3 | 61.7 | 78.7 |
| Qwen2.5-72B | 69.8 | 76.2 | 67.5 | 78.0 | 46.9 | 68.2 | 82.0 |
| Qwen3-32B | 67.8 | 75.6 | 64.0 | 73.8 | 44.4 | 67.9 | 80.9 |
| Llama4-Scout-16x17B | 67.9 | 74.7 | 66.8 | 73.2 | 43.5 | 67.7 | 81.2 |
| GPT-OSS-20B | 58.1 | 67.0 | 41.5 | 66.5 | 37.4 | 60.4 | 75.6 |

---

**Table 15: Pretraining Evaluation** [p. 39]

Performance (%) of Apertus models on *factual knowledge acquisition* tasks compared to other pretrained models. The arrows (up/down) show the desired direction for each benchmark.

| Model | Avg | MMLU (up) | Global-MMLU (up) | INCLUDE V1 (up) | INCLUDE V2 (up) | CulturalBench (up) | BLEND (up) | SwitzerlandQA (up) |
|---|---|---|---|---|---|---|---|---|
| **Fully Open Models** | | | | | | | | |
| **Apertus-8B** | **56.9** | **61.6** | **55.3** | **54.8** | **37.3** | **55.2** | **72.2** | **62.1** |
| **Apertus-70B** | **58.9** | **65.2** | **58.2** | **57.0** | **38.5** | **58.1** | **75.0** | **60.2** |
| OLMo2-7B | 51.6 | 60.5 | 41.1 | 33.8 | 30.6 | 69.5 | 73.2 | 52.5 |
| OLMo2-32B | 62.0 | 71.9 | 57.4 | 50.6 | 37.5 | 74.8 | 79.4 | 62.4 |
| EuroLLM-1.7B | 26.3 | 25.4 | 26.2 | 24.5 | 26.2 | 31.5 | 24.4 | 25.9 |
| EuroLLM-9B | 47.7 | 55.0 | 46.6 | 43.0 | 32.7 | 47.0 | 51.7 | 58.1 |
| SmolLM2-1.7B | 35.3 | 47.2 | 31.6 | 27.6 | 28.4 | 65.7 | 24.4 | 22.4 |
| SmolLM3-3B | 49.7 | 59.7 | 48.5 | 39.0 | 31.5 | 56.5 | 57.5 | 55.2 |
| Poro-34B | 37.5 | 44.3 | 34.8 | 31.0 | 26.8 | 40.2 | 43.4 | 42.1 |
| **Open-Weight Models** | | | | | | | | |
| Llama3.1-8B | 53.2 | 63.4 | 52.1 | 48.8 | 37.4 | 43.1 | 68.9 | 58.5 |
| Llama3.1-70B | 66.7 | 75.9 | 69.8 | 64.1 | 43.7 | 62.3 | 82.4 | 68.6 |
| Llama4-Scout-16x17B | 67.0 | 75.4 | 70.2 | 67.3 | 46.3 | 56.4 | 81.1 | 72.0 |
| Qwen2.5-7B | 58.6 | 71.9 | 60.3 | 53.9 | 37.8 | 47.3 | 75.2 | 63.9 |
| Qwen2.5-72B | 72.5 | 83.3 | 77.1 | 69.7 | 44.5 | 76.8 | 83.4 | 72.7 |
| Qwen3-32B | 69.1 | 80.7 | 71.1 | 67.7 | 41.8 | 74.9 | 81.0 | 66.5 |
| GPT-OSS-20B | 58.1 | 56.6 | 57.7 | 43.5 | 40.2 | 66.2 | 77.0 | 65.3 |
