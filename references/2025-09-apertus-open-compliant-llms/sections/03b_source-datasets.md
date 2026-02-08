# 3.2 Source Datasets [p. 18–21]

The following original source datasets were used for pretraining, before additionally going through consent, PII and toxicity filtering as described in Section 3.1. [p. 18]

## 3.2.1 English-only Data [p. 18–19]

[p. 18] Across the training stages, several English web-crawl pretraining datasets are used.

**FineWeb-HQ.** High-quality dataset obtained by filtering FineWeb web-crawl data using XLM-RoBERTa-based classifiers with a focus on structured and knowledge-rich content (Messmer et al., 2025). [p. 18]

**FineWeb-Edu.**^16 High-quality dataset obtained by filtering FineWeb web-crawl data using a classifier focusing on educational content (Penedo et al., 2024a). Both the larger score-2 (roughly 33%) and the regular, smaller, higher-quality score-1 (roughly 10%) versions are used. [p. 18]

**Figure 5** (p. 19): **"Relationships of our English pretraining datasets,** which are all based on CommonCrawl dumps. Not true to scale in terms of token count."

The figure is a Venn diagram showing the overlapping relationships among the English pretraining datasets. All are subsets of CommonCrawl-English (outermost oval). Inside: DCLM and FineWeb overlap partially; DCLM-edu is a subset of DCLM; FW-edu-score2 and FW-HQ are subsets of FineWeb; FW-edu-score1 is a subset of FW-edu-score2. The edu subsets of DCLM and FineWeb overlap because the same edu classifier is used for both. The base sets (DCLM and FineWeb) have non-overlapping parts.

**DCLM-Edu.**^17 High-quality dataset obtained by applying the FineWeb-Edu educational classifier on the DCLM dataset (Li et al., 2025). [p. 19]

To understand the composition of the English datasets, refer to Figure 5. All of the datasets can be seen as different, partially overlapping subsets from English CommonCrawl data. The same edu classifier is used for both DCLM and FineWeb, so the edu subsets overlap, but the base sets have non-overlapping parts (note that the figure is not true to scale in terms of token count). [p. 19]

## 3.2.2 Multilingual Data [p. 20]

**FineWeb-2.**^18 The base multilingual dataset, which is the largest openly available multilingual web-crawl dataset containing 1,811 languages (Penedo et al., 2025). All languages present in the dataset are preserved in their natural frequency. Appendix G provides an overview of the dataset's document distribution across the top 40 languages. [p. 20]

**FineWeb-2-HQ.**^19 High-quality dataset for 20 high-resource languages obtained by filtering FineWeb-2 web-crawl data using XLM-RoBERTa-based classifiers to identify structured and knowledge-rich content (Messmer et al., 2025), with removal of toxic content. [p. 20]

Since the available multilingual web-crawl data quickly drops off in volume, quality and toxicity filtering beyond the 20 most high-resource languages is not applied, and the data as it is in FineWeb-2 is used. However, the FineWeb-2 data from these languages is downsampled to maintain the relative proportion of the quality-filtered FineWeb-2-HQ data as found on the web. [p. 20]

**Translation Parallel Data.** For parallel data, EuroParl^20 (Koehn, 2005) and ParaDocs^21 (Wicks et al., 2024) are used. Both datasets provide sentence-level parallel data (source-target sentence pairs). While EuroParl contains single sentence pairs, ParaDocs includes document structure that allows reconstruction of context. For ParaDocs, consecutive sentences from the same document are concatenated to form longer translation pairs, up to the initial context limit of 4,096 tokens. [p. 20]

**Clean Wikipedia.**^22 A multilingual Wikipedia corpus is also included in the dataset. This is the same corpus that was used to compute the stop words for FineWeb-2's stop word filter (Penedo et al., 2024b). [p. 20]

## 3.2.3 Code, Mathematical, and Structured Data [p. 20–21]

[p. 20] To enable mathematical, coding, and task-solving abilities, the following datasets are used:

**StarCoderData.**^23 A large-scale code dataset derived from the permissively licensed GitHub collection *The Stack (v1.2)* (Kocetkov et al., 2022), which applies deduplication and filtering of opted-out files. In addition to source code, the dataset includes supplementary resources such as GitHub Issues and Jupyter Notebooks (Li et al., 2023). [p. 20]

**StarCoder Edu.** An annotated set of *StarCoderData*. Each programming language was partially annotated using `Qwen-Coder2.5`, capturing metrics such as code quality and educational usefulness. These annotations were used to finetune `CodeBERT` (Feng et al., 2020), resulting in models capable of generating annotations across all programming languages. This dataset serves as a permissively licensed complement to the existing *Stack v2 Edu* dataset (Allal et al., 2025). The final quality score is computed as a combination of all metrics, normalized to a range between 0 and 5. [p. 20]

**CommonPile/Stack v2 Edu.**^24 A curated dataset derived from CommonPile (Kandpal et al., 2025), in which *The Stack v2 Edu* (Allal et al., 2025) was filtered to retain only permissively licensed code. The dataset provides educational annotations with values ranging from 0 to 5. [p. 20]

**FineMath.**^25 Mathematical data obtained by filtering CommonCrawl web-crawl data and InfiMM-WebMath data using a classifier focusing on mathematical educational content (Allal et al., 2025). Subsets *FineMath-3+* and *InfiMM-WebMath-3+* are used. [p. 20]

**MegaMath.**^26 An open math pretraining dataset curated from diverse sources available in different quality versions (Zhou et al., 2025b). The subsets *megamath-web* and *megamath-web-pro* are used. [p. 21]

For all mathematical datasets, data from websites which have opted out of web-crawling is filtered using the same approach as for English and multilingual data. PII is not removed from math and code data due to the common occurrence of false positive heuristics in these types of data. [p. 21]

**Instruction and Task Data.** For task data, EuroBlocks-SFT-Synthetic-1124^27 (Martins et al., 2025) is used for multilingual instruction and task data, as well as Flan filtered for licenses allowing commercial use^28 (Longpre et al., 2023). [p. 21]

## 3.2.4 Data for Downstream Analysis [p. 21]

[p. 21] Several datasets are included to study memorization and data poisoning effects on the pretrained models.

**Memorization Analysis Data.** Texts from the permissively licensed Project Gutenberg^29 are adopted to simulate scenarios where models might inadvertently memorize and reproduce protected content. This corpus consists of long-form literary texts that structurally resemble high-risk copyrighted material, such as books, providing a realistic proxy for studying copyright issues. [p. 21]

The Frequency-Varied Memorization Probe Buckets (FM-Probes) framework from prior work (Xu et al., 2025) is employed to inject distinct sets of unique Gutenberg sequences into the training corpus at precisely controlled frequencies (1-128 repetitions), serving as a relevant analogue to the "canaries" used in prior memorization studies (Carlini et al., 2019). Two distinct Gutenberg probe sets are constructed: [p. 21]
1. Gutenberg-V1 comprising buckets of 500 sequences (1.78B tokens total)
2. Gutenberg-V2, which consists of 167 entirely new sequences (583M tokens total)

Both are publicly available for reproducibility.^30 [p. 21]

**Data Poisoning Synthetic Data.** A small amount of synthetically generated examples is included into the corpus to conduct scientific research in pretraining data poisoning (Zhang et al., 2025). The dataset is made available,^31 and more details on the design choices are provided in Appendix H. [p. 21]

## 3.2.5 Data Filtering [p. 21–22]

[p. 21] All filtering pipelines are implemented using the `datatrove` (Penedo et al., 2024b) Python library, which enables efficient parallelization of computation across multiple compute nodes and CPUs. Figure 6 shows an overview of the data compliance filters discussed in Section 3.1 for some of the pretraining dataset resources. [p. 21]

**Figure 6** (p. 22): **"Document filtering pipeline** for selected resource datasets used during pretraining. This pipeline encompasses all filtering stages, including consent and toxicity filters (described in Section 3.1) and quality filters from Messmer et al. (2025), described in Sec 3.2."

The figure is a horizontal stacked bar chart showing the percentage of initial documents retained/removed at each pipeline stage for three datasets. Pipeline stages (color-coded): Robots.txt Filter, High-Quality Text Selection, Toxicity Filter, Random Subsampler, Final Dataset. Key data points:

| Dataset | Robots.txt | High-Quality Text Selection | Toxicity | Random Subsampler | Final Dataset |
|---|---|---|---|---|---|
| DCLM-Edu | 10.2% | 83.8% | — | — | ~6% |
| FineWeb-2-HQ and FineWeb-2 | 0.9% | 73.7% | 12.8% | 8.5% | ~4% |
| MegaMath-Web | 13.5% | 86.5% | — | — | ~0% |

The chart shows that High-Quality Text Selection removes the largest fraction of documents across all datasets. For FineWeb-2-HQ/FineWeb-2, additional Toxicity Filter and Random Subsampler stages further reduce the data. DCLM-Edu and MegaMath-Web do not show separate toxicity or subsampling bars.

---

**Footnotes visible on pages 18-21:**
- ^16: HuggingFaceFW/fineweb-edu-score-2 (v1.0.0) and HuggingFaceFW/fineweb-edu (v1.0.0)
- ^17: HuggingFaceTB/dclm-edu
- ^18: HuggingFaceFW/fineweb-2 (v2.0.1)
- ^19: epfml/FineWeb-2-HQ
- ^20: Helsinki-NLP/europarl
- ^21: jhu-clsp/paradocs
- ^22: HuggingFaceFW/clean-wikipedia
- ^23: bigcode/starcoderdata
- ^24: common-pile/stackv2-edu-filtered
- ^25: HuggingFaceTB/finemath
- ^26: LLM360/MegaMath
- ^27: utter-project/EuroBlocks-SFT-Synthetic-1124
- ^28: DataProvenanceInitiative/Commercial-Flan-Collection-(SNI, Flan 2021, Chain of Thought, P3)
- ^29: huggingface.co/datasets/manu/project_gutenberg
- ^30: huggingface.co/datasets/swiss-ai/apertus-pretrain-gutenberg
- ^31: swiss-ai/apertus-pretrain-poisonandcanaries
