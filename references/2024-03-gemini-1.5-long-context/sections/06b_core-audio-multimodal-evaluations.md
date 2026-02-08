# 6.3. Core Audio Multimodal Evaluations [p. 42]

[p. 42] In addition to long-context evaluations on speech input, the authors also evaluate Gemini 1.5 Pro and Gemini 1.5 Flash on several Automatic Speech Recognition (ASR) and Automatic Speech Translation (AST) benchmarks. These include internal benchmarks derived from YouTube (both English and 52 other languages), as well as public benchmarks like Multilingual Librispeech (MLS) (Pratap et al., 2020), FLEURS (Conneau et al., 2023) and CoVoST-2 (Wang et al., 2020).^27

[p. 42] On FLEURS, a subset of 55 languages for which they have coverage in their training data is evaluated. On CoVoST-2, they evaluate on translating speech in 20 languages into English, reporting on the subset of languages that were seen by the model during pre-training. Word-Error-Rate (WER) is reported on all ASR tasks, where lower is better, except the four segmented languages on FLEURS where they aggregate Character-Error-Rates (Chinese, Japanese, Korean and Thai). On AST they report BLEU scores.

## Table 20

**Table 20** (p. 42): Comparison of Gemini 1.5 Pro with USM, Whisper, Gemini 1.0 Pro and Gemini 1.0 Ultra on audio understanding tasks.

| Category | Task | Metric | USM | Whisper | Gemini 1.0 Pro | Gemini 1.0 Ultra | Gemini 1.5 Flash | Gemini 1.5 Pro |
|---|---|---|---|---|---|---|---|---|
| Automatic Speech Recognition | YouTube (en-us) | WER (down) | 5.8% | 6.5% (v3) | 4.8% | **4.7%** | 4.9% | 4.8% |
| Automatic Speech Recognition | YouTube (52 lang) | WER (down) | 22.8% | 41.4% (v3) | 22.5% | **21.0%** | 23.8% | 22.6% |
| Automatic Speech Recognition | Multilingual LibriSpeech (en-us) (Pratap et al., 2020) | WER (down) | 7.0% | 6.2% (v2) | 4.8% | 4.4% | 5.2% | **4.2%** |
| Automatic Speech Recognition | FLEURS (55 lang) (Conneau et al., 2023) | WER (down) | 11.2% | 16.6% (v3) | 6.4% | **6.0%** | 9.8% | 6.5% |
| Automatic Speech Translation | CoVoST 2 (20 lang) (Wang et al., 2020) | BLEU (up) | 31.5 | 29.4 (v2) | 40.0 | **41.0** | 36.1 | 39.4 |

## Key Findings

[p. 42] Gemini 1.5 Pro, despite being a generalist model, significantly improves over specialist models like USM and Whisper that are trained exclusively for speech understanding on speech understanding benchmarks. Gemini 1.5 Pro performs similarly to Gemini 1.0 Pro on Speech Understanding, showing that performance on non long-context tasks is not compromised by the addition of long-context abilities. Gemini 1.0 Ultra does offer slight benefits over 1.5 Pro, but the former is a model requiring more training compute and serving resources. Finally, while Gemini 1.5 Flash ranks behind the more powerful generalist models in the Gemini 1.0 series and 1.5 Pro, it still outperforms specialist models.

> ^27 For these evaluations presented in this Section, we employ the model before the instruction-tuning phase for fair comparison with the other baselines. [p. 42]
