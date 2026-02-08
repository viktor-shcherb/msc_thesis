# 1. Introduction [p. 6]

[p. 6]

An expansive open ecosystem for developing large language models (LLMs) has flourished since the release of GPT-J (Wang & Komatsuzaki, 2021), with the quality of released models improving and accelerating (Black et al., 2022; Zhang et al., 2022; Scao et al., 2022; Touvron et al., 2023a;b; Jiang et al., 2023; Bai et al., 2023; Mesnard et al., 2024; Grattafiori et al., 2024; Yang et al., 2024a; Riviere et al., 2024; Yang et al., 2024b; Kamath et al., 2025; Yang et al., 2025a). Despite this proliferation of new, powerful LLMs, many of their design decisions continue to overlook the needs of many prospective global users, including data compliance and multilinguality. At various points throughout the LLM development pipeline, these decisions introduce systemic limitations that hinder further downstream development for many users.

The authors release the Apertus suite of models to address several of these limitations -- in particular, data compliance and multilingual representation -- to help democratize LLMs for broader communities of global users.

## Data compliance

[p. 6]

The authors set new standards for data compliance. Most of today's open models are, in fact, not open-source or reproducible, but only open-weights (Jiang et al., 2023; Grattafiori et al., 2024; Kamath et al., 2025, *inter alia*), with offerings by a few organizations (e.g., EleutherAI, Allen AI, LLM360, BigScience, etc.) serving as notable exceptions (Black et al., 2022; Scao et al., 2022; Liu et al., 2023; Groeneveld et al., 2024, *inter alia*). Open-weight models do not release the data used for training the model and often reveal very little about it beyond the token count. Simultaneously, many of these open-weight models allegedly include large amounts of illegal material that do not consider the access rights granted by content owners.^1

By contrast, Apertus is pretrained solely on openly available data sources, with documents excluded whenever their owners have opted out of AI crawling through `robots.txt` (Fan et al., 2025). The authors also train Apertus using a variant of the Goldfish objective (Hans et al., 2024) to limit the memorization and reproduction of training data. Their evaluation, the first at this scale, demonstrates that this approach effectively prevents verbatim memorization of training data while preserving downstream task performance.

## Multilingual representation

[p. 6]

Most models today only focus on single languages (Touvron et al., 2023b; Mesnard et al., 2024; Liu et al., 2025b), or small subsets of high-resource languages (Yang et al., 2024b; Grattafiori et al., 2024; Kamath et al., 2025), limiting their extensions for lower-resource language environments.^2 For Apertus, the authors massively expand the number of languages represented in the pretraining data to over 1800 languages, and set aside a much larger proportion of the pretraining text data mixture (~40%) for non-English languages. They also include over 149 languages in the post-training mixture for adapting Apertus for user interaction.

## Technical report overview

[p. 6]

This technical report describes in comprehensive detail the Apertus models, a collection of pretrained and Instruct models whose design prioritizes core values. The Apertus models are 8B-scale and 70B-scale models (Section 2) pretrained on up to 15T tokens (Section 3) using up to 4096 GPUs (Section 6). The pretraining corpus, containing multilingual text from 1811 languages (Penedo et al., 2025), is extensively filtered for copyrighted materials, retroactive author opt-outs according to the Robots Exclusion Protocol (i.e., `robots.txt`), toxic content, and Personally Identifiable Information (PII), providing a compliant basis for downstream development. Furthermore, in line with prior work (Lambert et al., 2025; Martins et al., 2025), the authors post-train these pretrained models to yield Apertus-{8B,70B}-Instruct (Section 4). Following their data compliance standard, they also filter post-training data according to license terms of the data, and add several custom multilingual post-training corpora covering 149 languages to improve downstream interaction in a broader number of languages.

The results (Section 5) demonstrate that the Apertus models are the strongest pretrained open models on multilingual benchmarks with open state-of-the-art performance at equivalent scale, even outperforming solely open-weight counterparts in

---
[p. 7 continued]

several settings. The report describes how these design decisions were considered and tested, providing a valuable resource for the community for their own future development.

## Contributions

[p. 7]

The authors summarize five contributions:

- **Scale.** The Apertus-70B model is the first fully open model to be trained at this scale -- 70B parameters trained on 15T tokens. To achieve this scale via training on up to 4096 GPUs, they implement several architectural (e.g., xIELU) and training (e.g., AdEMAMix, QRPO) innovations to stabilize large-scale training.

- **Data Compliance.** The pretraining corpus was compiled solely from web data, respecting `robots.txt` not only at crawl time (January 2025), but also retroactively applying January 2025 opt-out preferences to web scrapes from previous crawls. All datasets used for post-training were similarly filtered for non-compliant data (e.g., data released under non-permissive licenses). These filtering choices are designed to yield Apertus LLMs that comply with data provisions of the EU AI Act and similar regulations.

- **Memorization Prevention.** The Apertus models are pretrained using the Goldfish objective (Hans et al., 2024), constraining the model's ability to regenerate text. The authors demonstrate that this approach effectively suppresses verbatim recall even at a large model scale and after 128 exposures during training.

- **Multilinguality.** They train on 15T tokens from 1811 languages during pretraining, taken from the FineWeb-2 web crawl dataset.^3 They operationalize these learned general abilities with data from 149 languages in post-training. They test the models on cultural, knowledge, and instruction-following benchmarks covering a further 94 languages (including many African languages that, to their knowledge, have never previously been considered in open LLM training).

- **Transparency.** Apertus is a fully open model. The authors pair the release of the weights of the Apertus model suite with a full set of reproduction artifacts, including source code, final and intermediate model checkpoints, reproducibility scripts for training data, evaluation suites, and this technical report. This complete transparency enables audits at every step of model development, including changes in pretraining data mixtures, long context extension, instruction-tuning, and alignment.

> "This commitment to transparency grounds our model's name 'Apertus', Latin for 'open'." [p. 7]

The authors state that Apertus is the leading fully open LLM today. They provide materials under permissive-use licenses for future development, engagement, and extension.

## Released artifacts

[p. 7-8]

**Models:**
- `swiss-ai/Apertus-8B-2509`
- `swiss-ai/Apertus-70B-2509`
- `swiss-ai/Apertus-8B-Instruct-2509`
- `swiss-ai/Apertus-70B-Instruct-2509`

**Code:**
- `swiss-ai/Megatron-LM`
- `swiss-ai/pretrain-data`
- `swiss-ai/pretrain-code`
- `swiss-ai/posttraining`
- `swiss-ai/posttraining-data`
- `swiss-ai/evals`
- `swiss-ai/lm-evaluation-harness`
- `swiss-ai/apertus-format`
- `swiss-ai/hfconverter`

**Datasets & Auxiliary Tools:**
- `swiss-ai/apertus-finetuning-recipes`
- `swiss-ai/apertus-memorization`
- `swiss-ai/apertus-pretrain-toxicity`
- `swiss-ai/apertus-pretrain-gutenberg`
- `swiss-ai/apertus-pretrain-poisonandcanaries`
- `swiss-ai/apertus-posttrain-romansh`
- `swiss-ai/africa-preferences`
- `swiss-ai/africa-sft`
- `swiss-ai/switzerland_qa`

## Separately released related scientific publications

[p. 8]

- Data compliance gap when respecting training data opt-out (Fan et al., 2025)
- FineWeb-2 dataset (Penedo et al., 2025)
- FineWeb-2-HQ dataset (Messmer et al., 2025)
- Memorization dynamics (Xu et al., 2025)
- Multilingual evaluation (Romanou et al., 2025; Singh et al., 2025)
- xIELU activation function (Huang & Schlag, 2025)
- FP8 (Hernández-Cano et al., 2025) and outlier protected block (He et al., 2024)
- Warmup-Stable-Decay Learning Rates (Hägele et al., 2024; Dremov et al., 2025)
- AdEMAMix optimizer (Pagliardini et al., 2025)
- Optimizer benchmarking (Semenov et al., 2025)
- QRPO post-training (Matrenok et al., 2025)
- Contrastive language identification (Foroutan et al., 2025b)
- Parity-aware tokenization (Foroutan et al., 2025a)
- Training data indexing (Marinas et al., 2025)
- Training data attribution (Wuhrmann et al., 2025)
- Data mixtures during pretraining (Böther et al., 2025)
- Multilingual Data Mixture (Foroutan et al., 2025c)

## Safety advisory statement

[p. 8]

The Apertus models, while trained at large scale and demonstrating general purpose capabilities, have limitations that must be considered before deploying for real-world use. First, while tested on a variety of safety benchmarks and environments, they may still produce hallucinations, degenerate as they produce text, generate toxic outputs, and manifest other unsafe behaviors. Second, these models are language-only, only capable of processing text, and cannot process other modalities (such as images). Apertus should only be deployed after extensive use-case alignment and additional testing.

**Footnotes:**
- ^1: www.theatlantic.com/technology/archive/2025/03/libgen-meta-openai/682093
- ^2: The BLOOM (Scao et al., 2022), Aya (Üstün et al., 2024), and Qwen3 (Yang et al., 2025a) models are exemplary exceptions to this practice. They train on more languages, but still ~10x fewer than in our work.
- ^3: https://github.com/huggingface/fineweb-2/blob/main/fineweb2-language-distribution.csv
