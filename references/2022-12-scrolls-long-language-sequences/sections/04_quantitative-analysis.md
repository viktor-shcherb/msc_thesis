# Quantitative Analysis [p. 6]

[p. 6] Length alone is not enough to make SCROLLS a challenging benchmark. The authors provide a quantitative analysis that suggests producing the correct output for a SCROLLS task typically requires fusing different parts of the input that are often hundreds and even thousands of words apart. This analysis complements the qualitative inspection of examples from SCROLLS, as shown in Figure 2 and Figure 3, and further discussed in Appendix E.

## Methodology

Each example in SCROLLS consists of a textual input and output. Given a specific input-output pair, the example's *spread* is measured by computing the standard deviation between the locations of output bigrams in the input. Specifically, the output string is represented as a set of bigrams, and the *first occurrence* of each bigram in the input (if it exists) is located; the standard deviation between these locations (where a bigram is represented by the position of its first word in the input) is then computed. This produces an example-level measure of spread that can be plotted on a histogram for an entire dataset to compare different datasets.

Note: For ContractNLI, the output is considered to be the hypothesis, and the input to be the premise. For question answering datasets, the question is omitted. This metric is inspired by the analysis of Huang et al. (2021) for GovReport, which also used bigram statistics.

**Figure 4** (p. 7): "The spread of reference-text bigrams in the input texts, measured by the standard deviation of the position of each bigram's first occurrence in the input document. SCROLLS datasets (blue), other popular datasets (pink)."
- Two sub-panels with histograms (x-axis: Standard Deviation in Words on log scale from 10^0 to 10^5; y-axis: Density).
- **(a) Summarization datasets:** Shows CNN/DM (pink, peaked around 10^2), arXiv (pink, peaked around 10^2-10^3), GovReport (blue, peaked around 10^3), SummScreen (blue, peaked around 10^2-10^3), QMSum (blue, broad distribution peaked around 10^2-10^3). SCROLLS datasets are shifted right (higher spread) compared to CNN/DM and arXiv.
- **(b) QA and NLI datasets:** Shows SQuAD (pink, sharply peaked near 10^0), Natural Questions (pink, sharply peaked near 10^0-10^1), Qasper (blue, peaked around 10^2), NarrativeQA (blue, bimodal with peaks near 10^0-10^1 and 10^2-10^3), QuALITY (blue, peaked around 10^2-10^3), ContractNLI (blue, peaked around 10^2). SCROLLS datasets show much higher spread than SQuAD and Natural Questions.

## Summarization Datasets

Figure 4a compares the three summarization datasets in SCROLLS to the canonical CNN/DM summarization dataset (Hermann et al., 2015), as well as arXiv (Cohan et al., 2018), which has been used to evaluate long-sequence models. The reference bigrams are spread out across much larger distances in SCROLLS than in CNN/DM, and by a factor of 1.5 to 2 times more than arXiv on average.

## QA & NLI Datasets

Figure 4b compares the remaining four datasets in SCROLLS, which typically have shorter outputs, to the popular SQuAD (Rajpurkar et al., 2016) and Natural Questions (Kwiatkowski et al., 2019) datasets. While the answer bigrams in SQuAD and Natural Questions typically spread across distances of under 5 words, the output bigrams in SCROLLS datasets are usually separated by hundreds of words. NarrativeQA also seems to contain many examples where the answer bigrams cluster close together, but also a significant subset of examples where the answer's bigrams are dispersed across huge distances.
