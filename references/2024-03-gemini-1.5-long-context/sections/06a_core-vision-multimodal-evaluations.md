# 6.2. Core Vision Multimodal Evaluations [p. 38–41]

[p. 38] To assess performance on multimodal image tasks, the authors report results across a wide variety of 15 image understanding benchmarks (Table 18) and 6 video understanding benchmarks (Table 19), spanning multiple multimodal capabilities.

[p. 38] Gemini 1.5 Pro consistently and often substantially improves over Gemini 1.0 Pro on all image understanding benchmarks, even matching or exceeding Gemini 1.0 Ultra on all but one of them. A similar generational improvement is seen for Gemini 1.5 Flash which outperforms Gemini 1.0 Pro on all benchmarks. The core capability evaluation is discussed in four meta-categories: (1) Multimodal Reasoning (Section 6.2.1); (2) Chart, Diagram, and Document understanding (Section 6.2.2); (3) Natural Image Understanding (Section 6.2.3); and (4) Video understanding (Section 6.2.4).

## 6.2.1. Multimodal Reasoning

[p. 38–40] Gemini 1.5 Pro particularly excels at reasoning in multimodal contexts. MMMU (Yue et al., 2023) is a particularly difficult benchmark where models are judged on their ability to understand images, and use that information to solve college-level problems. Gemini 1.5 Pro scores 62.2% on MMMU, improving over Gemini 1.0 Ultra. A similar trend is seen on MathVista which requires mathematical reasoning in visual context. On MathVista, Gemini 1.5 Pro scores 63.9%, a new state-of-the-art result. [p. 38]

[p. 38, 40] As multimodal models become more capable, the authors want to understand their efficacy on specific scientific domains as well. Understanding structures of chemical diagrams is one such core-capability with a lot of downstream uses. The authors introduce **ChemicalDiagramQA**, an internal evaluation set to measure how well their models understand chemical structures in scientific figures. On this benchmark Gemini 1.5 models substantially outperform all 1.0 models, with 1.5 Pro scoring 69.7%: demonstrating that multimodal models are soon poised to help in scientific domains as well. See Appendix 12.14.6 for more details on this benchmark. [p. 38, 40]

[p. 40] The surprisingly strong performance of 1.5 Flash is also noted on these reasoning benchmarks, with 1.5 Flash outperforming even 1.0 Ultra on all of these except for MMMU. [p. 40]

## 6.2.2. Charts and Document Understanding

[p. 40] Chart and diagram understanding has been a particularly challenging domain for large multimodal models. Understanding complex charts/diagrams requires accurately parsing information from the image and also reasoning about them. Gemini 1.5 Pro sets new SOTA on popular external chart benchmarks like ChartQA (Masry et al., 2022). [p. 40]

[p. 40] The authors also construct an internal benchmark for chart and diagram understanding. They created **BetterChartQA** with 9 disjoint capability buckets (a comprehensive list of capabilities is shown in Appendix 12.18 together with by-capability performance of different Gemini models). The chart images are randomly sampled from the web (e.g., news articles, government reports, academic papers) and QA pairs are written by professional human annotators to reflect the wide distribution of chart styles and real-world cases. As indicated in Figure 32 and Table 18, overall Gemini 1.5 Pro outperforms the previous generation of Gemini 1.0 Pro by more than 20%. [p. 40]

[p. 41] To evaluate document understanding, in addition to the popular DocVQA (Mathew et al., 2021) and InfographicVQA (Mathew et al., 2022) benchmarks, the authors evaluate DUDE (Landeghem et al., 2023) and TAT-DQA (Zhu et al., 2022). **DUDE** is a document VQA benchmark based on multi-industry, multi-domain and multi-page documents with a combination of extractive, abstractive and unanswerable questions. **TAT-DQA** is a document VQA benchmark with a focus on financial documents with tables where questions often require strong spatial reasoning skills. These benchmarks are designed to gauge a multimodal model's ability to understand layout, tables and other visual elements found in visually rich documents. Gemini 1.5 Pro outperforms Gemini 1.0 Pro and Gemini 1.0 Ultra on both benchmarks, especially on TAT-DQA where it is more than 24% better than Gemini 1.0 Ultra. [p. 41]

[p. 41] The surprisingly strong performance of 1.5 Flash is again noted here, with 1.5 Flash outperforming 1.0 Ultra on 4 out of the 6 Charts and Documents understanding benchmarks tested on. [p. 41]

## 6.2.3. Natural Image Understanding

[p. 41] The authors evaluate the performance of Gemini 1.0 and 1.5 models on five benchmarks designed to assess real-world multimodal capabilities: VQAv2 (Goyal et al., 2017), TextVQA (Singh et al., 2019), RealWorldQA (x.ai), BLINK (Fu et al., 2024), and V* Benchmark (Wu and Xie, 2023). These benchmarks are designed to evaluate the performance of AI models on tasks such as spatial reasoning and detailed natural image understanding. [p. 41]

[p. 41] Gemini 1.5 models maintain competitive performance to 1.0 models on the popular TextVQA and VQAv2 benchmarks (focusing on OCR in natural images and generic QA in natural images). **RealWorldQA** assesses a model's understanding of the physical world by testing its ability to answer questions about images depicting real-world scenarios, focusing on capabilities such as basic spatial reasoning. **BLINK** is a benchmark consisting of 14 visual perception tasks that humans can solve quickly but pose challenges for current LLMs (including multi-view reasoning, depth estimation, etc.). On both benchmarks, Gemini 1.5 Pro performs favorably against previous state-of-the-art results reported in papers proposing those benchmarks. Despite the impressive performance of Gemini 1.5 Pro and Gemini 1.5 Flash, there still exists a notable gap compared to human-level understanding. [p. 41]

[p. 41] A core capability improved by both Gemini 1.5 models is understanding and answering questions about high resolution images. On the **V* Benchmark** (Wu and Xie, 2023) where the task is to answer questions about the attributes and spatial relations of very small objects on high resolution images (average resolution 2246 x 1582) from SA-1B dataset (Kirillov et al., 2023), Gemini 1.5 Pro surpasses Gemini 1.0 Pro and Gemini 1.0 Ultra by a large margin, even obtaining performance within a few points of the expensive and specialized visual search guided technique (SEAL) proposed by (Wu and Xie, 2023). [p. 41]

## 6.2.4. Video Understanding

[p. 41] In addition to the video needle-in-a-haystack results presented in Section 5.2.1.1 and the hour-long video question answering results presented in Section 5.2.2, the authors present core video understanding results in Table 19. Gemini 1.5 Pro outperforms 1.0 Ultra on question-answering datasets on all several-minutes long videos tested (i.e., ActivityNet-QA and EgoSchema). As for video captioning, Gemini 1.5 Pro underperforms 1.0 Ultra on YouCook2 which is focused on cooking videos but outperforms 1.0 Ultra on VATEX and Chinese variant VATEX ZH which contain more diverse videos. Finally, on OpenEQA (Majumdar et al., 2024), which is an open-vocabulary benchmark dataset for embodied question answering, Gemini 1.5 Flash outperforms 1.0 Ultra. Gemini 1.5 Pro is slightly behind on this benchmark, and upon inspection it is caused by refusal to answer the questions. [p. 41]

## Tables

**Table 18** (p. 39): Comparison of Gemini 1.5 models to Gemini 1.0 models on image understanding benchmarks. For DocVQA, InfographicVQA and DUDE, Average Normalized Levenshtein Similarity (ANLS) is reported (Biten et al., 2019). For other datasets, accuracy is reported. For AI2D, following the evaluation protocol used by x.ai, scores are reported using a transparent bounding box. Only for DocVQA, the model is additionally provided with annotations from Google Cloud OCR engine. For MMMU, MathVista, and ChartQA the models produce a chain of thought rationale before giving a final answer.

| Capability | Benchmark | 1.0 Pro | 1.0 Ultra | 1.5 Flash | 1.5 Pro |
|---|---|---|---|---|---|
| Multimodal Reasoning | **MMMU (val)** Multi-discipline college-level problems, 0-shot (Yue et al., 2023) | 47.9% | 59.4% | 56.1% | **62.2%** |
| Multimodal Reasoning | **MathViSTA (testmini)** Math reasoning in visual contexts, 0-shot (Lu et al., 2023) | 46.6% | 53.0% | 58.4% | **63.9%** |
| Multimodal Reasoning | **Ai2D (test)** Grade School Science diagrams, 0-shot (Kembhavi et al., 2016) | 81.9% | 87.7% | 91.7% | **94.4%** |
| Multimodal Reasoning | **ChemicalDiagramQA** Chemical structure diagram understanding, 0-shot, internal | 50.0% | 55.2% | 56.6% | **69.7%** |
| Charts & Documents | **ChartQA (test)** Chart understanding, 0-shot (Masry et al., 2022) | 74.1% | 80.8% | 85.4% | **87.2%** |
| Charts & Documents | **BetterChartQA** Chart understanding, 0-shot, internal | 43.0% | 47.9% | 59.0% | **65.8%** |
| Charts & Documents | **DocVQA (test)** Document understanding, 0-shot (Mathew et al., 2021) | 88.3% | 92.4% | 89.9% | **93.1%** |
| Charts & Documents | **DUDE (test)** Multi-page Document understanding, 0-shot (Landeghem et al., 2023) | 39% | 44% | **48%** | 46% |
| Charts & Documents | **TAT-DQA (test)** Document and table understanding, 0-shot (Zhu et al., 2022) | 9.9% | 13.2% | 23.6% | **37.8%** |
| Charts & Documents | **InfographicVQA (test)** Infographics understanding, 0-shot (Mathew et al., 2022) | 75.2% | 80.3% | 75.3% | **81.0%** |
| Natural images | **TextVQA (val)** Text reading on natural images, 0-shot (Singh et al., 2019) | 74.6% | **82.3%** | 78.7% | 78.7% |
| Natural images | **VQAv2 (test-dev)** Natural image understanding, 0-shot (Goyal et al., 2017) | 71.2% | 77.8% | 80.1% | **80.2%** |
| Natural images | **V* bench (test)** High-res image understanding, 0-shot (Wu and Xie, 2023) | 51.3% | 62.8% | **72.8%** | 71.7% |
| Natural images | **Blink (val)** Visual perception, 0-shot (Fu et al., 2024) | 45.1% | 51.7% | 56.5% | **61.4%** |
| Natural images | **Realworld QA (test)** Visual perception, 0-shot (x.ai) | 61.6% | 64.7% | 67.5% | **70.4%** |

**Table 19** (p. 40): Comparison of Gemini 1.5 Pro with Gemini 1.0 Pro and Ultra on video understanding benchmarks. For VATEX, VATEX ZH and YouCook2, CIDER is reported (Vedantam et al., 2015). For ActivityNet-QA and EgoSchema, accuracy is reported. For OpenEQA, language model evaluation scores suggested in the original paper (Majumdar et al., 2024) are reported. For EgoSchema the models produce a chain of thought rationale before giving a final answer.

| Capability | Benchmark | 1.0 Pro | 1.0 Ultra | 1.5 Flash | 1.5 Pro |
|---|---|---|---|---|---|
| Video understanding | **VATEX (test)** English video captioning, 4-shot (Wang et al., 2019a) | 57.4 | 62.7 | 57.1 | **64.6** |
| Video understanding | **VATEX ZH (val)** Chinese video captioning, 4-shot (Wang et al., 2019a) | 39.7 | 50.8 | 48.1 | **55.3** |
| Video understanding | **YouCook2 (val)** English video captioning, 4-shot (Zhou et al., 2018) | 123.2 | **135.4** | 80.9 | 106.5 |
| Video understanding | **ActivityNet-QA (test)** Video question answering, 0-shot (Yu et al., 2019) | 49.8% | 52.2% | 55.3% | **57.5%** |
| Video understanding | **EgoSchema (test)** Video question answering, 0-shot (Mangalam et al., 2023) | 55.7% | 61.5% | 65.7% | **72.2%** |
| Video understanding | **OpenEQA (val)** Embodied reasoning, 0-shot (Majumdar et al., 2024) | 44.9 | 61.3 | **63.1** | 57.9 |
