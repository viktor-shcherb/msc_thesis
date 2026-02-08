# 2 Pretraining [p. 4–6]

The approach to pretraining is to train a standard dense transformer architecture on a heavily engineered large pretraining corpora. The underlying assumption is that when trained on extensive data of high-enough quality, a standard architecture can exhibit advanced capability -- architectural modification may not be needed, although the authors conducted extensive preliminary architectural experiments. [p. 4]

## 2.1 Data Processing [p. 4–5]

The Yi data mixture is shown in Figure 2. To produce high-quality bilingual pretraining data, a cascaded data-processing pipeline was designed, as illustrated in Figure 1. The pipeline features a series of data-cleaning strategies targeting quality and diversity. Starting with web documents from Common Crawl, the CCNet pipeline [79] is used for language identification and perplexity scoring, followed by a combination of filtering and deduplication. [p. 4]

### Heuristic Rule Filters

[p. 5]

Filters for removing low-quality text based on:
1. URL, domain, word blocklists and garbled text filters
2. Document length, the ratio of special symbols, and the ratio of short, consecutive, or incomplete lines
3. Repeated words, n-grams, or paragraphs [58]; filtering thresholds based on statistical analysis of large document samples, as described in Nguyen et al. [52]
4. Identify and anonymize Personal Identifiable Information (PII), such as email addresses and phone numbers

### Learned Filters

[p. 5]

Learned filters address nuanced cases that exceed standard heuristic rules. Notably, Chinese content from Common Crawl presents unique challenges, particularly with a higher ratio of inappropriate content like pornography and gambling. Four learned scorers are integrated:

1. **Perplexity Scorer:** Uses the KenLM library as per CCNet [80], evaluates web documents, discarding those with perplexity scores largely above average.
2. **Quality Scorer:** A classifier trained to recognize and favor pages similar to Wikipedia in quality and assign scores accordingly. Documents failing to meet the quality standard are subsequently removed.
3. **Document Coherence Scorer:** Identifies low-quality web documents consisting of disparate sentences or paragraphs (being incoherent). Such documents are either segmented for further analysis or removed entirely.
4. **Safety Scorer:** Identifies and removes web documents containing toxic content, such as violence, pornography, and political propaganda.

### Cluster-based Filters

[p. 5]

Unsupervised semantic clustering is used to group web documents. The clustered data are subsequently annotated with quality labels, providing essential references for the optimization of Yi's data mixture strategy. Documents identified as low-quality through automatic and manual verification are excluded from the dataset.

### Deduplication

[p. 5]

A comprehensive deduplication pipeline following the procedure in Penedo et al. (2023) [56]. This pipeline integrates document-level MinHash deduplication and sub-document exact-match deduplication, effectively identifying and removing duplicate content within and across documents. Web documents are further categorized into specific themes using a topic model predicting labels like news, ads, and knowledge-based content. In the final pretraining dataset, less helpful content (mostly advertisements) is down-sampled to ensure information density. The final composition of Yi's pretraining data is shown in Figure 2.

**Figure 1** (p. 4): "Yi's pretraining data cleaning pipeline."
The figure shows a flowchart of the data cleaning pipeline. Starting from "Data Collection" and "Raw Web Data" on the left, the pipeline proceeds through: Language Filtering -> Text Metric Filtering -> Repetitive Document Removal -> Rule Based Correction -> Perplexity Filtering -> Document Quality Filtering -> Paragraph Deduplication -> MinHash Deduplication -> Exact Deduplication -> Safety Filtering -> Topic Filtering -> Semantic Filtering. The stages are arranged in a multi-row flow from left to right.

**Figure 2** (p. 5): "Yi's pre-training data mixture. Overall our data consist of 3.1T high-quality tokens in both English and Chinese, and come from various sources. Our major differences from existing known mixtures like LLaMA [76] and Falcon [56] are that we are bilingual, and of higher quality due to our more rigorous cleaning pipeline."
The figure shows a donut/pie chart with data source composition. Visible categories and token counts (in billions): Webpage: 25239 (84.89%), Code: 2569 (8.63%), Paper: 1526 (5.13%), Book: 949 (2.69% [unclear: exact percentage partially obscured]), Encyclopedia: 349 (1.05% [unclear: exact percentage partially obscured]), Other: 615 (1.92% [unclear: exact percentage partially obscured]). The chart distinguishes English and Chinese portions within each category. Numbers sum to approximately 31,247B (~3.1T tokens).

## 2.2 Tokenization [p. 5]

- Uses byte-pair encoding (BPE) [69] implemented in the SentencePiece framework [40]
- Vocabulary size: 64,000 to balance computational efficiency and word comprehension
- Numbers are split into individual digits to facilitate better understanding of numeric data
- Rare characters fall back to unicode-byte encoding for fault tolerance
- Identity tokenizer employed to avoid transferring all punctuations to half-width format
- Does NOT use the dummy prefix (whitespace at beginning of text) approach common in English LLMs, because the assumption does not always hold in English context (especially sentences beginning with quotation marks) and does not show positive effect in Chinese context

## 2.3 Model Architecture [p. 6]

Yi uses a modified version of the classical decoder-only Transformer architecture [78] where the code is based on LLaMA's [77] implementation. The main parameter settings are summarized in Table 1.

**Table 1** (p. 6): "Model configs of Yi-6B and Yi-34B. LR stands for learning rate."

| Models | Hidden Size | Q-heads | KV-heads | Layers | Pretrain Seq. Len | Max LR |
|--------|-------------|---------|----------|--------|-------------------|--------|
| 6B     | 4096        | 32      | 4        | 32     | 4096              | 3 x 10^-4 |
| 34B    | 7168        | 56      | 8        | 60     | 4096              | 1.5 x 10^-4 |

Modifications from LLaMA to Yi:

### Attention Mechanism

[p. 6]

LLaMA 2 uses Grouped-Query Attention (GQA) [1] only on its largest 70B model, and its 7B and 13B uses full attention. Yi incorporates GQA in both Yi-6B and Yi-34B. GQA splits query-heads into G groups, sharing a single key and value head within each group of query [1]. This offers substantial reductions of training and inference costs, compared to the original Multi-Head Attention (MHA) [16, 57, 67]. No performance degradation is observed after applying GQA to the 6B smaller model.

### Activation Function

[p. 6]

SwiGLU [68] is used as Yi's post-attention layer, reducing its activation size from 4h to 8/3h (h denotes hidden size) to be consistent with the normal post-attention layer. This adjustment also compensates for the reduction in parameters resulted from GQA, making the overall parameter count comparable of existing 7B and 34B models.

### Positional Embedding and Long Context

[p. 6]

Rotary Position Embedding (RoPE) [73] is used following the standard implementation. The base frequency is adjusted (RoPE ABF), introduced in Xiong et al. [82], to support long context windows up to 200K where the base model itself is trained on 4K context length.

To adapt the base model to longer context, continue pretraining on 10B tokens from the pretraining data mixture with slightly upsampled long sequences, mostly from book. Only 1-2B tokens is enough for the model to converge to low loss on 4K-200K length, and a lightweight finetuning further induces near-perfect long-context retrieval performance.

> Based on this observation, the authors "tend to view that the capability of modeling longer dependency than the pretrained length (4K) is a intrinsic capability (rather than an being injected by post-train). This is to say, the base model already has the capability to model longer than 4K dependency even the model is trained shorter, and the post-train / finetuning procedure simply release this capability." [p. 6]
