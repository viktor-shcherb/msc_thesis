# 3 Pretraining Data [p. 17]

This section describes the diverse datasets and pre-processing steps used for pretraining Apertus. The primary goal is to establish an open, reproducible, and high-quality foundation for model training, focusing on general language modelling, multilingual breadth, mathematical and coding capabilities, and limiting to permissively-licensed data. [p. 17]

Multiple source datasets are aggregated and mixed, processed through a carefully designed pipeline guided by three key principles:

**Reproducibility.** All pre-processing steps are documented to ensure full transparency and facilitate replication of results. The pipeline code^9 is released to recreate all of the data used for training the models. [p. 17]

**Multilinguality.** The data contains 1811 languages (1868 language-script pairs), increasing the applicability of the model to broad languages and cultures. [p. 17]

**Compliance.** The model is trained only on permissive content. All data from websites that have opted out of crawling by popular AI crawlers as of January 2025 is removed. Only code data available under permissive licenses is used. Personally identifiable information (PII) is removed and toxic content is filtered. [p. 17]

## 3.1 Data Compliance [p. 17]

This section covers data compliance considerations for the pretraining data. Each of the following subsections describes a component in the document filtering and formatting pipeline to address compliance. A comprehensive legal assessment of data usage in large language model training under Swiss law is provided in Rosenthal & Veraldi (2025). [p. 17]

### 3.1.1 Consent: robots.txt with Hindsight [p. 17]

[p. 17] Pretraining datasets based on web data are typically constructed by aggregating multiple snapshots taken from web crawls at different points in time (Penedo et al., 2024a; 2025). Content owners may apply restrictions on web crawlers by updating their `robots.txt` files (Longpre et al., 2024; Fan et al., 2025). However, pretraining datasets, when they account for these restrictions at all, typically enforce them only at the moment of crawling. This practice raises concerns about data usage, as subsequent changes to access policies are not retroactively applied to previously collected web snapshots, potentially leading to the continued use of data that is no longer permitted under the updated restrictions. [p. 17]

To respect the consent of data owners and mitigate potential legal violations, the authors retroactively apply the most recent crawling permissions specified by data owners. This filter is applied to *all* datasets. [p. 17]

**Implementation:** URL domains are ranked by the volume of texts they contribute to the FineWeb (Penedo et al., 2024a) and FineWeb-2 (Penedo et al., 2025) corpus, as an approximation of web-level English and multilingual data. The top one million English domains and the top one million non-English domains are selected. Due to domain overlap and the fact that some sites are now offline, the total number of accessible `robots.txt` files is smaller than two million. For each domain that remains reachable, the `robots.txt` file as of January 2025 is retrieved and the directives targeting AI-specific user agents listed in Appendix B are examined. Any contents blocked by the current `robots.txt` is removed retroactively from the entire 2013-2024 range of the training dataset. An opt-out policy is followed: if the corresponding `robots.txt` files are not available, the data is considered usable for training. [p. 17]

The filtering process results in an estimated token loss of approximately 8% in English data and 4% in multilingual data.^10 [p. 17]

### 3.1.2 Personally Identifiable Information (PII) [p. 18]

[p. 18] To protect against potential memorization of PII in the model, pretraining data is anonymized using best-effort practices to process data on the scale of hundreds of terabytes of data (Penedo et al., 2024a; 2025). Regular expressions are applied to detect email addresses, IP addresses, and IBAN bank account numbers, and replace them with anonymous markers, such as `<email-pii>`. [p. 18]

### 3.1.3 Toxicity Filtering [p. 18]

[p. 18] Multilingual toxicity filtering is implemented across nine languages (English, Chinese, French, German, Italian, Dutch, Polish, Spanish, and Portuguese) on FineWeb-2 (Penedo et al., 2025) and FineWeb (Penedo et al., 2024a). Language-specific binary classifiers are trained using annotated datasets from PleIAs (Arnett et al., 2024)^11 and SWSR (Jiang et al., 2021).^12 [p. 18]

The PleIAs corpus provides five-dimensional toxicity annotations covering: (1) *Race and origin-based bias*, (2) *Gender and sexuality-based bias*, (3) *Religious bias*, (4) *Ability bias*, and (5) *Violence and abuse*. Due to the scarcity of positive labels, all samples with a total toxicity score greater than 0 are classified as positive labels, indicating harmfulness in at least one evaluated dimension. For Chinese texts, the *SexComments* subset from the SWSR corpus is additionally used, which provides binary labels for sexuality-related toxicity. [p. 18]

To address class imbalance between positive and negative samples, non-toxic examples are subsampled to create balanced 50%-50% training sets for each language. 10% is separated from the balanced dataset as the validation set. The trained classifiers are open-sourced on HuggingFace.^13 [p. 18]

The toxicity classifier is trained using a two-stage approach: first the multilingual document embeddings are extracted using `XLM-RoBERTa`,^14 then a language-specific 2-layer MLP is trained for binary toxicity classification on top of these embeddings for 6 epochs. The classifier checkpoints with the best accuracy on the held-out validation set are further employed to annotate toxicity scores for FineWeb-2 and FineWeb documents.^15 [p. 18]

> **"We filter the 5% of documents per language with the highest predicted toxicity scores from the pretraining corpus."** [p. 18]

**Figure 4** (p. 19): **"Distributions of Toxicity Scores in 9 Languages,** when applying our classifiers to the Chinese, French, German, Italian, Dutch, Polish, Spanish, and Portuguese datasets from FineWeb-2 (Penedo et al., 2025) and English from FineWeb (Penedo et al., 2024a). The 95% threshold is highlighted as High-Risk."

The figure shows a 3x3 grid of density plots, one per language, with x-axis "Toxicity Score" and y-axis "Density". Each subplot includes a vertical dashed red line marking the 95th percentile ("High Risk (95%)"). All distributions are heavily right-skewed, with the majority of documents concentrated at low toxicity scores. Summary statistics per language:

| Language   | Mean  | Median | Std   |
|------------|-------|--------|-------|
| German     | 0.199 | 0.003  | 0.353 |
| French     | 0.216 | 0.002  | 0.372 |
| Italian    | 0.269 | 0.010  | 0.391 |
| Spanish    | 0.266 | 0.023  | 0.375 |
| Polish     | 0.159 | 0.002  | 0.318 |
| Portuguese | 0.399 | 0.330  | 0.308 |
| Dutch      | 0.222 | 0.024  | 0.341 |
| Chinese    | 0.241 | 0.193  | 0.173 |
| English    | 0.245 | 0.011  | 0.377 |

---

**Footnotes visible on pages 17-18:**
- ^9: github.com/swiss-ai/pretrain-data
- ^10: A convenient set of filtering tools is available at data-compliance.github.io/tools
- ^11: huggingface.co/datasets/PleIAs/ToxicCommons
- ^12: zenodo.org/records/4773875
- ^13: huggingface.co/swiss-ai/apertus-pretrain-toxicity
- ^14: huggingface.co/FacebookAI/xlm-roberta-base
- ^15: The toxicity filter is not applied on code and math datasets, FineWeb-Edu and DCLM-Edu, as those subsets are considered filtered already by a restrictive subtopic or a selective education-related prompt, respectively.
