# Language Modeling Experiments [p. 9–14]

## 8.1 LM Evaluation Harness Benchmarks

[p. 9] To assess the performance of Eagle and Finch models, we evaluate on a series of common multilingual and English-focused benchmarks using evaluation_harness (Gao et al., 2023) as shown in Tables 3 and 4. We find that Eagle and Finch demonstrate exceptionally high capabilities on multi-lingual benchmarks, with nearly all results significantly outperforming the other similarly sized models we tested.

[p. 9] In figures 2 and 3 we plot the accuracy versus FLOPs used to train various open models across a similar set of common benchmarks. For multilingual benchmarks, Eagle and Finch represent a substantial improvement to the Pareto frontier, achieving far higher scores than other models trained for a similar number of FLOPs. The two models additionally obtain competitive performance across these English benchmarks.

### Figure 2: Multilingual Benchmarks [p. 10]

**Figure 2:** Multilingual average benchmark accuracy versus training FLOPs. Average of LAMBADA Multilingual, xStoryCloze, xWinoGrande, and xCOPA

The figure shows a scatter plot with Training FLOPs on x-axis (around 10^22) and Accuracy on y-axis (ranging from ~0.47 to 0.62). Models plotted include:
- finch (red circles)
- eagle (blue squares)
- pythia (orange diamonds)
- mamba (black triangles)
- stablelm (brown stars)
- btlm-3b-8k-base (cyan inverted triangles)
- falcon-7b (green right-pointing triangles)
- Llama-2-7b (yellow hexagons)

The Finch and Eagle models appear at the top of the plot, showing the highest accuracy scores around 0.58-0.62.

### Figure 3: English Benchmarks [p. 10]

**Figure 3:** English average benchmark accuracy versus training FLOPs. Average of LAMBADA (OpenAI), PIQA, StoryCloze16, HellaSwag, WinoGrande, Arc (challenge), Arc (easy), HeadQA (English), OpenBookQA, SciQ, ReCoRD and COPA

The figure shows a similar scatter plot with Training FLOPs on x-axis (around 10^22) and Accuracy on y-axis (ranging from ~0.58 to 0.72). The same models are plotted with the same color/marker scheme. Finch and Eagle models show competitive performance, appearing in the upper portion of the plot around 0.66-0.71 accuracy.

### Table 3: Multilingual Benchmarks [p. 11]

| Model | lmb.m ppl↓ | lmb.m acc↑ | pawsx acc↑ | xcopa acc↑ | xnli acc↑ | xsClz acc↑ | xwin acc↑ | avg acc↑ |
|-------|------------|------------|------------|------------|-----------|------------|-----------|----------|
| Pythia-1.4b | 115.9 | 35.5 | 50.9 | 52.7 | 38.9 | 51.8 | 68.3 | 49.7 |
| Mamba-1.4b | 73.1 | 40.4 | 48.0 | 54.4 | 41.6 | 54.2 | 72.4 | 51.8 |
| RWKV-4-1.5b | 72.5 | 38.5 | 53.7 | 55.4 | 39.3 | 56.0 | 67.7 | 51.8 |
| Eagle-1.5b | 43.2 | 44.8 | 51.9 | 57.9 | 40.4 | 57.9 | 73.0 | 54.3 |
| Finch-1.6b | 37.5 | 46.9 | 50.9 | 58.0 | 41.4 | 57.9 | 74.9 | 55.0 |
| Pythia-2.8b | 81.3 | 38.8 | 49.4 | 53.7 | 40.0 | 53.5 | 71.5 | 51.1 |
| Mamba-2.8b | 53.7 | 43.5 | 43.6 | 55.3 | 42.1 | 56.3 | 75.6 | 52.7 |
| RWKV-4-3b | 40.1 | 43.4 | 50.9 | 55.5 | 40.9 | 58.1 | 72.3 | 53.9 |
| Eagle-3b | 38.8 | 49.1 | 51.6 | 59.0 | 42.2 | 60.7 | 77.8 | 56.5 |
| Finch-3b | 29.1 | 50.5 | 48.6 | 56.8 | 44.9 | 59.8 | 76.9 | 57.1 |
| Pythia-6.9b | 85.6 | 36.7 | 48.4 | 54.1 | 40.0 | 54.2 | 70.9 | 50.7 |
| MPT-7b | 49.8 | 44.4 | 43.5 | 53.6 | 39.8 | 56.3 | 76.9 | 52.4 |
| Llama-2-7b | 30.4 | 50.8 | 41.2 | 56.7 | 39.9 | 57.5 | 79.5 | 54.3 |
| Falcon-7b | 28.7 | 51.3 | 48.2 | 58.0 | 39.0 | 59.0 | 77.7 | 55.7 |
| Mistral-7b-v0.1 | 27.1 | 51.9 | 41.5 | 55.9 | 43.1 | 59.2 | 81.2 | 54.5 |
| RWKV-4-7b | 33.1 | 47.4 | 52.1 | 60.1 | 41.2 | 60.9 | 76.5 | 56.4 |
| Eagle-7B | 21.0 | 53.7 | 45.6 | 62.2 | 44.0 | 63.3 | 80.4 | 58.2 |

Caption: Multilingual Benchmarks, including LAMBADA Multilingual **(lmb.m)** (Gao et al., 2023), XCOPA (Ponti et al., 2020), XNLI (Conneau et al., 2018), PAWS-X (Yang et al., 2019), XStoryCloze **(xsClz)** (Lin et al., 2022), xWinogrande **(xwin)** (Tikhonov & Ryabinin, 2021).

### Table 4: English Focused Benchmarks [p. 11]

| Model | lmb.o acc↑ | hella acc_n↑ | piqa acc↑ | arcE acc↑ | arcC acc↑ | glue acc↑ | winG acc↑ | sciq acc↑ | copa acc↑ | avg acc↑ |
|-------|------------|--------------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|----------|
| Pythia-1.4b | 61.0 | 52.0 | 70.8 | 54.4 | 26.2 | 47.1 | 57.3 | 86.5 | 74.0 | 59.9 |
| RWKV-4-1.5b | 60.1 | 51.6 | 71.5 | 58.4 | 27.1 | 46.1 | 55.2 | 84.7 | 78.0 | 59.2 |
| Eagle-1.5b | 65.7 | 55.0 | 71.1 | 62.2 | 28.7 | 54.1 | 59.1 | 89.7 | 76.0 | 62.4 |
| Finch-1.6b | 66.8 | 57.3 | 72.6 | 62.7 | 29.8 | 49.8 | 59.4 | 89.6 | 78.0 | 62.9 |
| Mamba-1.4b | 64.5 | 59.0 | 74.2 | 65.0 | 30.1 | 47.0 | 61.3 | 87.1 | 80.0 | 63.1 |
| Pythia-2.8b | 63.8 | 59.1 | 73.9 | 63.8 | 29.0 | 47.3 | 58.2 | 88.6 | 79.0 | 62.5 |
| RWKV-4-3b | 65.7 | 58.8 | 72.4 | 62.9 | 29.4 | 53.6 | 57.5 | 87.6 | 86.0 | 64.1 |
| Eagle-3b | 68.7 | 62.6 | 74.3 | 68.6 | 33.8 | 46.3 | 62.0 | 92.6 | 85.0 | 66.0 |
| Mamba-2.8b | 68.1 | 65.9 | 75.2 | 69.7 | 33.8 | 46.3 | 63.0 | 90.2 | 84.0 | 66.2 |
| Finch-3b | 70.8 | 64.8 | 74.2 | 66.5 | 34.6 | 58.2 | 63.6 | 92.5 | 82.0 | 67.5 |
| Pythia-6.9b | 60.9 | 63.2 | 74.8 | 66.5 | 32.0 | 47.7 | 61.5 | 88.9 | 79.0 | 63.8 |
| RWKV-4-7b | 69.8 | 65.3 | 75.0 | 67.4 | 34.0 | 56.4 | 62.4 | 90.8 | 85.0 | 67.3 |
| MPT-7b | 66.6 | 76.4 | 79.1 | 76.5 | 42.4 | 59.3 | 68.1 | 93.0 | 86.0 | 71.9 |
| Llama-2-7b | 73.5 | 76.0 | 78.1 | 76.4 | 43.1 | 42.9 | 69.1 | 93.9 | 87.0 | 71.1 |
| Falcon-7b | 74.6 | 76.4 | 79.5 | 74.8 | 40.3 | 45.8 | 67.1 | 94.4 | 88.0 | 71.2 |
| Eagle-7B | 74.2 | 70.9 | 77.0 | 73.8 | 39.5 | 57.5 | 67.4 | 95.5 | 88.0 | 71.5 |
| Mistral 7B-v0.1 | 75.5 | 81.0 | 80.5 | 80.8 | 60.1 | 51.5 | 73.6 | 95.9 | 93.0 | 75.8 |

Caption: English Focused Benchmarks, including LAMBADA **(lmb.o)** (Paperno et al., 2016), Hellswag **(hella)** (Hampel, 1974), PIQA (Bisk et al., 2020), AI2 ARC **(arcE, arcC)** (Bhakthavatsalam et al., 2021), GLUE (Wang et al., 2018), Winogrande **(winG)** (Sakaguchi et al., 2021), SciQ (Welbl et al., 2017), COPA (Roemmele et al., 2011).

## 8.2 Associative Recall

[p. 11] Associative recall (AR) is a synthetic task designed to mimic the way that humans associate and retrieve information. It measures a model's proficiency in recalling information that was previously mentioned in context. Prior research suggests that a model's ability to perform AR is indicative of its effectiveness in in-context learning (Elhage et al., 2021; Olsson et al., 2022). As a result, AR has been adopted as a benchmark in developing new language model architectural designs. (Fu et al., 2023; Poli et al., 2023; Lutati et al., 2023). Arora et al. (2023) benchmarked a range of models for multi-query associative recall (MQAR) and identified a performance gap between various linear transformer architectures and the transformer with attention. In MQAR tasks, prior RWKV models demonstrated a correlation between model dimension and sequence length. To compare architectures, we trained models using RWKV-4, Eagle and Finch on MQAR,
