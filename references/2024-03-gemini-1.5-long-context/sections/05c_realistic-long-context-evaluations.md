# 5.2.2. Realistic Long-Context Evaluations [p. 17–21]

[p. 17] Having investigated the model's multimodal abilities on handling long-context using a battery of diagnostic tests, the authors turn to a series of novel multimodal tasks designed to better reflect the potential uses of this model, thus stress-testing models in a more realistic way.

## 5.2.2.1 In-context language learning -- learning to translate a new language from one book

[p. 17] To test the in-context learning abilities enabled by very long context, the authors evaluate Gemini 1.5 Flash & 1.5 Pro on the Machine Translation from One Book (MTOB) benchmark (Tanzer et al., 2023). MTOB measures the ability to learn to perform sentence-level translation between English and Kalamang (ISO 639-3 language code: `kgv`) from instructional materials. Kalamang has fewer than 200 speakers and therefore virtually no presence on the web, which means that the model must rely on the data given in context (rather than knowledge stored in its weights at training time).^11

The available resources for Kalamang are:
- Field linguistics documentation^12 comprising a ~500 page reference grammar (Visser, 2020b)
- A ~2000-entry bilingual wordlist (Visser, 2020a)
- A set of ~400 additional parallel sentences (Visser, 2020a)

In total the available resources for Kalamang add up to around ~250k tokens. This task framing offers the promise of using extremely long-context models to support languages that are not sufficiently represented in pre-training corpora, with curated resources that can be created and deployed by independent parties. [p. 17]

### Experimental setup

[p. 17] To perform the task, Gemini 1.5 Flash & 1.5 Pro are provided with the full set of materials in their input context. To compare fairly against GPT-4 Turbo (version 2024-04-09) and Claude 3, since the full materials do not fit in their publicly released context windows (128K and 200K respectively), results are also reported using only half of the grammar book (~100k tokens). Moreover, to test to what extent the models are making use of information in the context rather than relying on knowledge found in their pre-training data, a 0-shot setup is also run. Finally, the authors compare to MTOB's reference for human performance, in which a human learned Kalamang from the exact same full set of materials.^13

### Evaluation metrics

[p. 17] Performance is assessed via a human evaluation where the same human language learner is given the input sentence and reference translation, and rates the quality of the predicted translation on a scale from 0 to 6, with 6 being an excellent translation. This rater is a non-native non-fluent speaker who can identify their own translations, so the scores should be interpreted in context. Automatic metrics are additionally reported: BLEURT (Sellam et al., 2020) for Kalamang to English (`kgv`->`eng`) and chrF (Popovic, 2015) for English to Kalamang (`eng`->`kgv`).

### 0-shot results

[p. 17] Gemini 1.5, GPT-4 Turbo, and Claude 3 all have essentially random performance in the 0-shot setting (i.e., no additional Kalamang information in context). The models sometimes successfully copy proper nouns, identify loanwords from higher resource languages like Malay, or narrow generation using style cues like question marks. Their generations for `eng`->`kgv` are identified by Google Translate as various other languages, often malformed. These results indicate that, as expected, no substantial Kalamang data, if any, was part of the models' training data. [p. 17]

### Results with context

[p. 18] Gemini 1.5 Pro in the half book setting outperforms GPT-4 Turbo and Claude 3 on the same setup by a wide margin; see Tables 4 and 5. In the best setting, Gemini 1.5 Pro attains a 4.14 human evaluation score on `kgv`->`eng` translation, compared to 5.52 of the "human language learner" score, and 5.46 on `eng`->`kgv` translation, compared to 5.58 by the "human language learner". There is still a substantial qualitative gap for `kgv`->`eng` translation, but `eng`->`kgv` translation is similar to the human language learner on average.^14 Gemini 1.5 Flash also performs admirably, falling short of Gemini 1.5 Pro as expected but handily outperforming GPT-4 Turbo and sitting somewhere between Claude 3 Haiku & Sonnet or Sonnet & Opus depending on the translation direction. See Appendix 12.17 for more details, experiments, and qualitative examples. [p. 18]

**Table 4** (p. 18): Quantitative results for Kalamang->English translation on MTOB (Tanzer et al., 2023). Human evaluation scores on a scale of 0 to 6 (6 = excellent). Automatic metrics (BLEURT) in parentheses.

| Context | GPT-4 Turbo | Haiku | Claude 3 Sonnet | Opus | Gemini 1.5 Flash | Gemini 1.5 Pro | Human language learner |
|---|---|---|---|---|---|---|---|
| 0-shot | 0.14 (30.0) | 0.24 (33.4) | 0.14 (30.0) | 0.18 (32.7) | 0.14 (31.5) | 0.18 (30.0) | - |
| half book | 2.04 (49.7) | 2.80 (53.5) | 3.40 (58.5) | 3.74 (58.3) | 3.00 (55.1) | **4.14** (63.9) | - |
| full book | - | - | - | - | 3.14 (57.4) | 4.00 (**64.6**) | 5.52 (70.3) |

**Table 5** (p. 18): Quantitative results for English->Kalamang translation on MTOB (Tanzer et al., 2023). Human evaluation scores on a scale of 0 to 6 (6 = excellent). Automatic metrics (chrF) in parentheses.

| Context | GPT-4 Turbo | Haiku | Claude 3 Sonnet | Opus | Gemini 1.5 Flash | Gemini 1.5 Pro | Human language learner |
|---|---|---|---|---|---|---|---|
| 0-shot | 0.08 (15.0) | 0.08 (15.3) | 0.08 (17.3) | 0.12 (18.7) | 0.08 (15.4) | 0.00 (12.0) | - |
| half book | 3.90 (45.4) | 4.46 (51.7) | 4.64 (49.2) | 5.18 (55.5) | 4.94 (54.6) | 5.38 (**59.1**) | - |
| full book | - | - | - | - | 4.66 (52.0) | **5.46** (59.0) | 5.60 (57.0) |

Note: Bold values in the tables indicate the best model score (excluding human). A dash (-) indicates the full book context does not fit in the model's context window.

### Discussion

[p. 18–19] The performance of Gemini 1.5 Pro highlights the importance of long-context understanding and providing sufficient context for learning new skills in-context. By leveraging the extensive field linguistics documentation provided in context, Gemini 1.5 Pro was able to achieve remarkable translation quality comparable to a human language learner, and was able to do so for a language for which it had essentially zero exposure to during the training of the model. This finding opens up exciting possibilities for leveraging LLMs with sufficiently long-context capabilities to support the preservation and revitalization of endangered languages, as well as to facilitate communication and understanding across different linguistic communities. As research continues in this area, it will be crucial to explore techniques for improving the quality of translation in both directions, e.g., Kalamang-to-English, and to address the challenges of evaluating the performance of LLMs on low-resource and under-represented languages, which the authors believe is also applicable to other areas of education and language learning. [p. 19]

### Footnotes

> ^11 "Of course, the models do have some relevant knowledge to transfer to the task, such as competence at translation in general, understanding of linguistics reference grammars, and knowledge of loanwords or other languages with areal influence on Kalamang (though Kalamang is not known to be genealogically related to any other languages) (Tanzer et al., 2023; Visser, 2020b)." [p. 17]

> ^12 "Machine learning for indigenous languages can be culturally sensitive (Bird, 2020). In the case of MTOB, the field linguist who documented Kalamang is an author on the MTOB project; in addition to getting consent for the original data collection for linguistic research, the field linguist got renewed permission from their main community consultant to use the data specifically for machine learning research (Tanzer et al., 2023)." [p. 17]

> ^13 "Note that this is different from the typical notion of human performance in machine translation, where native speakers rate the quality of the translations in absolute. MTOB is instead concerned with the ability to learn to translate from limited reference materials, and how to bridge the gap to useful applications is a separate research question." [p. 17]

> ^14 "This is not to say that the task is solved; both the human and Gemini 1.5 Pro make avoidable errors, though typically of different kinds. The human errors tend to be retrieval failures, where they pick a suboptimal phrase because they could not find the ideal reference (because rereading the entire set of materials for each sentence is infeasible for a human). The model failures tend to be inconsistent application of rules, like that the word 'se' is pronounced 'he' after a vowel (this alternation is described in the phonology section of the grammar and reflected in the additional parallel sentence data, but the model may be confused by the fact that the underlying 'se' form is used as the gloss throughout the examples within the grammar), or lack of reflection, like that the word 'kabor', although it is defined as 'to be full' in the dictionary, is only used for stomachs/hunger in all examples of its use." [p. 18]

## 5.2.2.2 In-context language learning -- learning to transcribe speech in a new language in context

[p. 19] Gemini 1.5 has demonstrated exceptional performance at extremely long in-context learning for translation, both with Kalamang (on MTOB) and other low-resource languages (on standard benchmarks below). Kalamang, like many other endangered languages, is primarily oral; applications must therefore support speech in order to be socially useful. The authors take the next step towards these applications -- and at the same time stress test Gemini 1.5's **mixed-modal in-context learning capabilities** -- by evaluating how well it can learn to transcribe Kalamang speech from text and audio documentation in context. This task framing is possible in LLMs for the first time due to Gemini 1.5's native audio support.

[p. 19] The authors present a preview of results on a new benchmark, ASROB (Automatic Speech Recognition from One Book). ASROB extends MTOB with 104 speech recordings (15 total hours) of transcribed and translated Kalamang speech from The Kalamang Collection (Visser, 2020c).^15 Experiments are reported on a subset of 6 recordings (45 minutes) with manually realigned phrase-level captions; 5 of the recordings (~800 phrases) are used as the in-context train set and 1 (~100 phrases) as the test set. The same speaker from the test recording is present in 3 of the train recordings.

[p. 19] Character Error Rate (CER) is reported across various combinations of text context (the ~2000-entry bilingual wordlist and ~400 parallel sentences from MTOB) and audio context (up to 800 Kalamang speech/text pairs). The authors cannot compare directly to GPT-4 or Claude 3 because they do not provide access to audio input at the time of writing.^16

**Table 6** (p. 19): Character Error Rate (CER, lower is better) for Gemini 1.5 Pro learning Kalamang ASR in context.

| Gemini 1.5 Pro | | audio context | | |
|---|---|---|---|---|
| text context | 0-audioshot | 5-audioshot | 50-audioshot | 800-audioshot |
| none | 35.0% | 30.2% | 27.5% | 23.1% |
| wordlist | 29.7% | 27.7% | 24.8% | 23.2% |
| sentences | 31.4% | 27.2% | 25.7% | **22.9%** |
| both | 32.5% | 26.5% | 25.8% | 23.0% |

**Table 7** (p. 20): Character Error Rate (CER, lower is better) for Gemini 1.5 Flash learning Kalamang ASR in context.

| Gemini 1.5 Flash | | audio context | | |
|---|---|---|---|---|
| text context | 0-audioshot | 5-audioshot | 50-audioshot | 800-audioshot |
| none | 73.3% | 32.0% | 32.3% | 26.0% |
| wordlist | 45.4% | 31.3% | 31.3% | 26.1% |
| sentences | 37.9% | 33.2% | 33.1% | 25.3% |
| both | 37.5% | 33.0% | 33.4% | **25.2%** |

### ASR results discussion

[p. 20] Gemini 1.5 Pro performs remarkably well without any in-context examples (where the prompt instructs the model to transcribe Kalamang speech with Indonesian orthography), achieving 35.0% CER. Judging from the outputs, the model clearly hears the sounds of the language but does not know how to segment or spell words in it, especially affixes. As text and audio context are added for many-shot learning (Agarwal et al., 2024a), ASR quality improves relatively gracefully, reaching 22.9% CER in the best setting. These outputs are segmented and spelled much better, with some examples transcribed perfectly, but there is still significant room for improvement -- in particular ensuring that all outputs are grammatically correct Kalamang. Gemini 1.5 Flash (Table 7) follows a similar trajectory to Pro, but with worse scores across the board. [p. 20]

### Footnotes

> ^15 "When the linguist author of Visser (2020b) got the blessing of a community member to use the Kalamang data for machine learning for MTOB, she included speech data/tasks in the discussion." [p. 19]

> ^16 "We tried to compare to GPT-4 by cascading the speech input through Whisper, but we were unable to get Whisper to consistently produce transcriptions of the kind that Gemini 1.5 produces zero-shot. We tried using a) default settings, b) the language code for Indonesian, and c) prompts in English & Indonesian introducing 'an audio sample in Kalamang, which is written with Indonesian orthography.'" [p. 19]

## 5.2.2.3 Scaling In-Context learning for low-resource machine translation

[p. 20–21] The impressive in-context language learning capability of Gemini 1.5 inspires the authors to revisit traditional in-context learning (ICL) at scale. ICL allows LLMs to learn new tasks from input-output examples provided at inference time. While it has been widely observed across tasks and models, the number of in-context examples explored is often limited, ranging from a handful to a few dozen, because of context length limitations and/or suboptimal long-context capabilities (Brown et al., 2020; Min et al., 2022; Zhang et al., 2023a). By contrast, Gemini 1.5's millions of tokens of context open new opportunities for scaling ICL to thousands of examples, also known as the many-shot ICL regime (Agarwal et al., 2024a; Bertsch et al., 2024). [p. 20–21]

In this section, the authors explore to what extent Gemini 1.5 can leverage an increased number of in-context examples (or shots) to improve machine translation for low-resource languages, extending the prior work exploring the limits of few-shot learning for machine translation (Garcia et al., 2023). [p. 21]

### Languages evaluated

[p. 21] Translation from English to 6 diverse low-resource languages:
- **Acholi** (ISO 639-3: ach; Africa)
- **Abkhaz** (ISO 639-3: abk; Asia)
- **Navajo** (ISO 639-3: nav; Americas)
- **Bemba** (ISO 639-3: bem; Africa)
- **Ewe** (ISO 639-3: ewe; Africa)
- **Kurdish** (ISO 639-3: kur; Asia)

These languages each have between a few hundred thousand to a few million speakers, with relatively low exposure on the Internet. Due to such low-resource nature, it requires the model to understand and learn from the given in-context examples rather than from the pretraining data and to acquire new knowledge about the language when appropriate. [p. 21]

### Evaluation setup

[p. 21] Two evaluation setups are created: public and in-house, depending on the accessibility of the test data to the general public.

**Public setup:** Following Agarwal et al. (2024a), covers Bemba, Ewe, and Kurdish using the dev set of Flores-200 (Team et al., 2022) (up to 997 examples and 90K tokens) as the in-context example set and the first 200 examples from its devtest set as the test set.

**In-house setup:** Covers Acholi, Abkhaz, and Navajo using Gatitos (Jones et al., 2023) (including up to 4K examples and 30K tokens) as the in-context example set and 200 held-out sentence pairs annotated by professional translators as the test set.

The translation prompt is presented in Appendix 12.16.15. Averaged performance over three runs is reported, each with freshly sampled in-context examples, using chrF (Popovic, 2015) as the evaluation metric. [p. 21]

### Scaling results

[p. 21] Figure 13 shows the ICL scaling performance. While previous ICL studies often see performance saturate after dozens of examples, Gemini 1.5 delivers almost consistent improvements as the number of shots is scaled. The quality gain over zero-shot translation can be quite substantial, e.g. +11.1/+21.4 chrF on Bemba and +9.5/+15.9 chrF on Navajo for 1.5 Pro/Flash, although it varies greatly across languages. Gemini 1.5 Flash degrades from few-shot ICL on Acholi, but further scaling ICL significantly improves the translation. Overall, Gemini 1.5 Flash presents more pronounced many-shot scaling compared to 1.5 Pro which may be related to its smaller model size: it relies more on in-context examples to perform the translation rather than its implicit knowledge. [p. 21]

While GPT-4 Turbo also shows some positive trend as the number of shots is scaled, Gemini 1.5 Pro often outperforms GPT-4 Turbo across languages and numbers of shots by a wide margin. One interesting exception is the translation for Abkhaz, where Gemini 1.5 Pro lags behind GPT-4 Turbo with few prompts but significantly surpasses it as ICL scales. This pattern also occurs with Gemini 1.5 Flash across languages: scaling up to 1K/4K examples improves Flash, enabling it to achieve superior performance to GPT-4 Turbo, e.g. +9.6/+6.4 chrF on Ewe/Acholi. In short, the Gemini 1.5 models excel at translating low-resource languages and gracefully improve with in-context examples. [p. 21]

**Figure 13** (p. 20): "In-context learning scaling results (chrF, higher is better) on low-resource translation. Top: results on Flores test sets. We use Flores dev sets for prompting and scale the number of shots to ~1K (including about 90K tokens). Bottom: results on in-house evaluation sets. We use Gatitos for prompting and scale the number of shots to ~4K (including about 30K tokens). Gemini 1.5 yields increasingly better translation performance as the number of shots grows, surpassing GPT-4 Turbo significantly."
- 6 panels arranged in a 2x3 grid. Top row: Flores test sets; Bottom row: in-house evaluation sets.
- Three models plotted: Gemini 1.5 Pro (blue solid line), Gemini 1.5 Flash (green solid line), GPT-4 Turbo (yellow/olive solid line).
- X-axis: "Number of Shots (K)" ranging from 2^0 to 2^10 (top) or 2^12 (bottom), log scale.
- Y-axis: "Test chrF (Flores)" (top row) or "Test chrF (In-house)" (bottom row).
- **Top left (English -> Bemba):** Y-axis ~20 to 50. Gemini 1.5 Pro reaches ~48 chrF at ~1K shots; Flash reaches ~45; GPT-4 Turbo ~35. Both Gemini models show steady improvement with more shots.
- **Top center (English -> Kurdish):** Y-axis ~30 to 45. Gemini 1.5 Pro reaches ~44; Flash ~43; GPT-4 Turbo ~37. All models show upward trend.
- **Top right (English -> Ewe):** Y-axis ~20 to 40. Gemini 1.5 Pro reaches ~35; Flash ~33; GPT-4 Turbo ~25. Gemini models clearly ahead.
- **Bottom left (English -> Acholi):** Y-axis ~10 to 35. Gemini 1.5 Pro reaches ~33; Flash ~30 (after initial dip at few-shot); GPT-4 Turbo ~25.
- **Bottom center (English -> Abkhaz):** Y-axis ~10 to 30. GPT-4 Turbo initially leads (~25 at low shots) but Gemini 1.5 Pro surpasses it at higher shot counts (~30). Flash starts low but catches up.
- **Bottom right (English -> Navajo):** Y-axis ~10 to 35. Gemini 1.5 Pro reaches ~32; Flash ~28; GPT-4 Turbo ~18. Large gap between Gemini models and GPT-4 Turbo.

## 5.2.2.4 Long-document QA

[p. 21–23] After testing Gemini 1.5 models' in-context language learning capabilities up to 250k tokens, the authors proceed into another realistic evaluation setup. Experiments on question answering are presented using the book "Les Miserables" (by Victor Hugo) and the model's ability to answer them correctly when the entire 1,462 page book (i.e., 710K tokens) is provided as input. Evaluating a model's ability to answer questions about long documents (or collections of documents) presents a unique challenge. Unlike tasks that focus on specific facts or details that measure the retrieval capability of the models, such questions often require understanding relationships between pieces of information spanning large portions of text. For example, a question like "How is the concept of duality portrayed through the character who embodies both respect for authority and hatred of rebellion?" necessitates comprehending the overall narrative and character dynamics within the above book. [p. 21–22]

### Comparison setup

[p. 22] Gemini 1.5 Pro is compared against Gemini 1.0 Pro. Due to the limited context window of the latter, Gemini 1.0 Pro requires retrieval-augmented generation to access useful passages from the book. This method indexes passages using TF-IDF and stores the results in an external database. The question is then used as a query to re-rank passages by cosine similarity, and the most relevant passages are retrieved, up to a maximum of 4k tokens (roughly 41 passages). The retrieved passages are then put into context following a temporal ordering. In contrast, Gemini 1.5 Pro, due to its larger context window capable of accommodating much longer material, eliminates any need for additional data post-processing, indexing and retrieval pipelines.^17

To evaluate the models' response, 100 questions are created. [p. 22]

> ^17 "See Appendix 12.3 on details of the automatic question generation pipeline." [p. 22]

### Evaluation methodology

[p. 22] Generally, LLMs today can achieve high factual accuracy in the zero-shot setting for well-known works such as "Les Miserables". This makes it challenging to distinguish between models when using absolute performance measures. The authors therefore use side-by-side comparisons to assess the answer quality between models with varying context sizes. For a more detailed discussion on this methodology and its implications, see Bohnet et al. (2024). The side-by-side comparison allows rating whether models provide enough details to answer a question sufficiently. An auto-rater is used that takes a question and answers from two different systems and compares them against each other. The auto-rater response is either *system-A is better*, *system-B is better* or *None* if both answers are non-factual, in which case they are both excluded. [p. 22]

### Bradley-Terry model analysis

[p. 23] Using these side-by-side comparison results, an analysis of model strength is provided using the Bradley-Terry model (Bradley and Terry, 1952). Such ranking models are used in many applications and are best known for their use in Chess or Go to rate player strength. The Bradley-Terry model assigns scores to a fixed set of models based on pairwise comparisons, where the log-odds of model *i* outperforming model *j* is given by the difference of their scores. The fitting of the parameters for *n* models, (beta_1, ..., beta_n) is performed via maximum likelihood estimation. The model strength has a direct mapping to the probability that an answer from Model M_A is better than an answer from M_B:

$$P(M_A \text{ answers better than } M_B) = \frac{e^{\beta_A}}{e^{\beta_A} + e^{\beta_B}} \quad (1)$$

**Figure 14** (p. 22): "Answer quality based on side-by-side auto-rater (Gemini 1.5 Pro), rankings and scores (e^beta) computed via the Bradley-Terry Model."
- Bar chart with y-axis "Strength" (0 to 7) and x-axis showing 7 configurations.
- Bars (left to right):
  - 0k_context Gemini 1.0 Pro: 0.1041 (blue)
  - RAG 4k_context Gemini 1.0 Pro: 0.2971 (blue)
  - RAG 4k_context GPT-4 Turbo: 1.2994 (gray)
  - 0k_context GPT-4 Turbo: 1.6424 (gray)
  - 0k_context Gemini 1.5 Pro: 1.3746 (gray)
  - RAG 4k_context Gemini 1.5 Pro: 1.7656 (gray)
  - full 710k_context Gemini 1.5 Pro: 6.2417 (orange, far tallest bar)
- Note: The rightmost bar (6.2417) represents full-context Gemini 1.5 Pro with the complete book, dramatically outperforming all other configurations.

### Results

[p. 23] Figure 14 summarizes the results for this evaluation. When using the entire book "Les Miserables" as context, Gemini 1.5 Pro outperforms all other systems by large margin. For example, full-context Gemini 1.5 Pro provides better answers than retrieval-augmented generation with 4k tokens using Gemini 1.5 Pro with probability P = 6.2417 / (6.2417 + 1.7656) = 0.7795, or in 78% of cases. Using the full book as context with Gemini 1.5 Pro provides a better answer compared to retrieval-augmented GPT-4 Turbo with 4k tokens in 83% of cases. [p. 23]

## 5.2.2.5 Long-context Audio

[p. 23] Next, the authors evaluate Gemini 1.5's long context understanding capabilities on audio inputs. To evaluate long-context automatic speech recognition (ASR) performance, Gemini 1.5 models are tested on an internal benchmark derived from 15 minute segments of YouTube videos. Results are reported against the 1.0 Pro model, which is trained on audio segments much shorter in length. Performance is also reported with the Universal Speech Model (USM) (Zhang et al., 2023b) and Whisper (OpenAI, 2023). Note that ASR tasks report a word error rate (WER) metric, where a lower number is better. [p. 23]

### Results

[p. 23] Table 8 shows that the 1.0 Pro model, when evaluated on transcribing 15-minute videos without segmentation, has a WER of 100% due to a mismatch between training and testing audio lengths. When the videos are segmented every 30 seconds and the textual content of the language model is passed across each segment boundary, the 1.0 Pro model can achieve a WER of 7.8%. The USM model with a CTC decoder, while robust to long segments, achieves a WER of 8.8%. As indicated in the table, Whisper is not robust to long segments and hence requires audio to be segmented every 30 seconds to achieve a WER of 7.3%. In comparison, Gemini 1.5 Pro is much more robust on these longer-context tasks. Specifically, thanks to its long-context capabilities and without the added complexity of extra input segmentation and pre-processing, Gemini 1.5 Pro can transcribe 15-minute videos more accurately than other models, achieving a WER of 5.5%, while Gemini 1.5 Flash trailing behind 1.0 Pro with a WER of 8.8%, a remarkable level of quality considering its smaller size and superior efficiency. [p. 23]

**Table 8** (p. 23): Word error rate (WER) for various models on 15-minute videos.

| | USM | Whisper (no seg) | Whisper (30s seg) | Gemini 1.0 Pro (no seg) | Gemini 1.0 Pro (30s seg) | Gemini 1.5 Pro | Gemini 1.5 Flash |
|---|---|---|---|---|---|---|---|
| Segmentation | -- | -- | 30s | -- | 30s | -- | -- |
| WER | 8.8% | 12.5% | 7.3% | 100% | 7.8% | **5.5%** | 8.8% |

Note: Bold value (5.5%) indicates the best WER. A dash (--) in Segmentation means no segmentation applied. USM is robust to long segments; Whisper and Gemini 1.0 Pro require 30s segmentation for good performance. Gemini 1.5 Pro and 1.5 Flash operate on unsegmented 15-minute audio.
