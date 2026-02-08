# 4.1.3 Supervised Finetuning Data [p. 28–30]

[p. 28–29] The supervised finetuning employs a carefully curated mixture of instruction-following datasets, developed through eight iterations of empirical evaluation. The final mixture is made available on HuggingFace^37 and comprises approximately 3.8 million examples from diverse sources, balancing general instruction-following, mathematical reasoning, code generation, and multilingual capabilities. Table 12 summarizes the composition. Data is aggregated from six primary categories:

**Foundation Instruction Data** (529K examples): Leverages high-quality instruction datasets from OLMo2 (OLMo et al., 2025) and Tulu3 (Lambert et al., 2025), including WildChat (299K), scientific instructions from SciRiff (30K), and structured data from TableGPT (25K). Mathematical datasets undergo post-processing to remove `\boxed{}` formatting from assistant responses if present, enabling more natural response generation. Verifiable results are instead represented as a verifiable response. [p. 29]

**Mathematical and Reasoning** (771K examples): Incorporates filtered personas-based math problems from Tulu3 (125K), OpenMath GSM8K variants (50K), and Llama-Nemotron mathematical reasoning data (200K). Executable Python code from NuminaMath solutions is extracted into function calls and function outputs (63K), intending to enable tool-augmented problem solving. [p. 29]

**Code and Technical** (378K examples): Programming instruction data includes Llama-Nemotron code examples (200K), function-calling datasets from xlam (60K) and Glaive (113K), and APIGen examples (5K). This mixture supports both direct code generation and tool-use scenarios. [p. 29]

**Multilingual and Cultural** (1.4M examples): A significant portion targets multilingual capabilities through SmolTalk2 conversational data (1.3M examples across 8 languages), EuroBlocks synthetic multilingual instructions (157K), and language-specific datasets. Notably, 1,000 examples from the s1k_42_langs dataset are included, a version of the s1k dataset (Muennighoff et al., 2025) translated to 42 languages, specifically selecting unique samples with non-English prompts/responses but English reasoning chains to encourage cross-lingual transfer. [p. 29]

**Structured Knowledge** (545K examples): The Tome dataset provides financial and web-based instruction-following examples that enhance the model's ability to process structured information, handle specialized terminology, and maintain factual consistency in professional domains. [p. 29]

**Low-Resource and Regional Languages** (944K examples): To improve representation of underserved language communities, extensive multilingual Wikipedia Q&A (884K), Romansh language data (46K) covering six written varieties, Swiss-German dialect instructions (6K), and African language instructions (7K) are included. Additionally, 226 constitutional alignment examples following the principles outlined in the Swiss AI Charter are incorporated. This diverse linguistic data promotes better cross-lingual transfer and reduces the performance gap between high and low-resource languages. [p. 29]

**Romansh Language Support:** To provide comprehensive support for Romansh -- Switzerland's fourth national language with approximately 60,000 speakers -- a specialized post-training dataset covering the six main written varieties (Rumantsch Grischun, Sursilvan, Sutsilvan, Surmiran, Puter, and Vallader) was developed. The dataset comprises 46,923 instruction-following examples including bidirectional dictionary translations, sentence-level translations paired with German/French/Italian/English, and idiom identification tasks that teach the model to distinguish between regional varieties. To the authors' knowledge, this represents the most extensive Romansh language resource for LLM training to date, addressing a critical gap in language technology for this vulnerable language community. Full details on data collection, quality filtering, and linguistic considerations are provided in Appendix J. [p. 29]

**Quality Assurance:** Beyond the license filtering and decontamination procedures described above, datasets undergo additional processing: removal of formatting artifacts (*e.g.*, `\boxed{}` annotations), extraction of executable code from mathematical solutions into tool-calling formats, and prioritization of human-verified over model-judged examples. Through eight iterations of mixture refinement -- each evaluated on the benchmark suite -- the balance between language diversity, task coverage, and quality was optimized. [p. 29]

**Table 12: SFT data mixture composition by source and category.** All datasets are decontaminated against evaluation benchmarks. Numbers indicate example count after filtering. [p. 30]

| Category | Dataset Source | # Examples | Data Ratio |
|---|---|---|---|
| Foundation | OLMo2 WildChat | 298,556 | |
| | OLMo2 Personas | 29,356 | |
| | OLMo2 SciRiff | 29,809 | |
| | OLMo2 TableGPT | 24,803 | |
| | OLMo2 CoCoNot | 10,793 | |
| | OLMo2 OASST1 | 7,047 | |
| | *Subtotal* | 400,364 | 9.56% |
| Math & Reasoning | Llama-Nemotron Math | 200,000 | |
| | Tulu3 Personas Math (filtered) | 125,522 | |
| | NuminaMath (tool-extracted) | 63,248 | |
| | OLMo2 OpenMath GSM8K | 49,948 | |
| | Llama-Nemotron Chat/Safety | 46,808 | |
| | *Subtotal* | 485,526 | 11.60% |
| Code & Functions | Llama-Nemotron Code | 200,000 | |
| | Glaive Function Calling | 112,688 | |
| | XLam Function Calling | 60,000 | |
| | APIGen | 5,000 | |
| | *Subtotal* | 377,688 | 9.02% |
| Multilingual | SmolTalk2 (8 languages) | 1,273,789 | |
| | EuroBlocks Multilingual | 157,318 | |
| | s1k_42_langs (filtered) | 1,000 | |
| | *Subtotal* | 1,432,107 | 34.22% |
| Regional | WikiQA | 883,513 | |
| | Romansh | 46,170 | |
| | Swiss-German Dialects | 6,179 | |
| | African Languages | 7,339 | |
| | Swiss Charter Q&A | 226 | |
| | *Subtotal* | 943,427 | 22.54% |
| Domain-Specific | The-Tome (Financial/Web) | 544,975 | 13.02% |
| **Total** | | **4,184,087** | **100%** |

---

**Footnotes:**
- ^37: https://huggingface.co/datasets/swiss-ai/apertus-sft-mixture
