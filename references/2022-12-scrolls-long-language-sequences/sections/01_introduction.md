# Introduction [p. 1-2]

[p. 1] Standard benchmarks such as GLUE (Wang et al., 2018, 2019), WMT (Barrault et al., 2019, 2020), and SQuAD (Rajpurkar et al., 2016, 2018) have driven progress in NLP of *short* utterances. However, a large portion of natural language is produced in the context of *longer* discourses, such as books, articles, meeting transcripts, etc.

To tackle the computational challenges of processing long sequences, many new model architectures have recently emerged (Tay et al., 2020b; Fournier et al., 2021), *without* establishing a standard scheme for evaluating them on long natural language problems. Some long-context models are evaluated via language modeling perplexity, but this metric mostly captures model sensitivity to local, short-range patterns (Khandelwal et al., 2018; Sun et al., 2021).

Other studies rely on Long Range Arena (Tay et al., 2021), which is limited from a natural-language perspective, since only two of its datasets involve natural language, and those are artificially elongated through byte tokenization.

[p. 2] To enable the research community to go beyond sentences and paragraphs, the authors present SCROLLS: **S**tandardized **C**ompa**R**ison **O**ver **L**ong **L**anguage **S**equences.

SCROLLS incorporates multiple tasks (summarization, question answering, and natural language inference) over various domains (literature, meeting transcripts, TV shows, scientific articles, and more), where each example's input typically contains thousands of words. The authors review existing literature on long-text tasks and manually curate a subset of 7 datasets, prioritizing those that require contextualizing and abstracting information across multiple parts of the text. The data is cleaned and converted to a unified text-to-text format to enable evaluation of a single model over all datasets.

**Figure 1** (p. 1): "The distribution of words per input in SCROLLS datasets (blue), alongside frequently-used NLP datasets (pink). Dashed vertical lines indicate the maximal sequence length (in tokens) of BERT (Devlin et al., 2019) and GPT3 (Brown et al., 2020)."
- X-axis: Words per Input (Log Scale), ranging from 10^1 to 10^5.
- Y-axis: Dataset names. SCROLLS datasets shown in blue: NarrativeQA, QMSum, GovReport, SummScreenFD, QuALITY, Qasper, ContractNLI. Popular datasets shown in pink: CNN/DM, SQuAD, MultiNLI.
- Key observation: SCROLLS datasets are substantially longer than commonly-used NLP benchmarks. BERT's max sequence length (~512 tokens) and GPT-3's max sequence length (~2048 tokens) are marked as dashed vertical lines; most SCROLLS datasets extend well beyond these limits.
- The analysis also reveals that in SCROLLS, critical information is spread out across longer distances within the input documents.

SCROLLS is available via the Datasets library (Lhoest et al., 2021) or direct download on its website, which hosts a live leaderboard that accepts submissions and automatically evaluates them against private test sets. By producing a single aggregate score, in addition to individual dataset scores, SCROLLS can serve as an evaluation platform for future approaches to processing long text, whether by new pretraining schemes, novel transformer architectures and alternatives, or even retrieval-based methods.

Initial baselines are provided using two transformer models: BART (Lewis et al., 2020) and its length-efficient variant, Longformer Encoder-Decoder (Beltagy et al., 2020). Experiments indicate that SCROLLS poses a formidable challenge for these models, leaving much room for improvement.
