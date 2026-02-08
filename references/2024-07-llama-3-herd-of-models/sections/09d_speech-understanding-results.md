# 8.4 Speech Understanding Results [p. 66]

[p. 66] The speech understanding capabilities of the speech interface for Llama 3 are evaluated on three tasks: **(1)** automatic speech recognition, **(2)** speech translation, and **(3)** spoken question answering. The performance of the speech interface for Llama 3 is compared with three state-of-the-art models for speech understanding: Whisper (Radford et al., 2023), SeamlessM4T (Barrault et al., 2023), and Gemini.^19 In all the evaluations, greedy search for Llama 3 token prediction is used. [p. 66]

^19 Due to technical limitations, the comparison is with the performance of Gemini on MLS reported in the original paper.

**Speech recognition.** [p. 66–67] The ASR performance is evaluated on the English datasets of Multilingual LibriSpeech (MLS; Pratap et al. (2020)), LibriSpeech (Panayotov et al., 2015), VoxPopuli (Wang et al., 2021a), and a subset of the multilingual FLEURS dataset (Conneau et al., 2023). In evaluation, the decoding results are post-processed using the Whisper text normalizer to ensure consistency in comparing with the reported results of other models. On all benchmarks, the word error rate of the speech interface for Llama 3 is measured on the standard test set of those benchmarks, except for Chinese, Japanese, Korean and Thai, where the character error rate is reported. [p. 67]

**Table 31** Word error rate of our speech interface for Llama 3 on speech recognition tasks. We report the performance of Whisper, SeamlessM4T, and Gemini for reference. [p. 67]

| | Llama 3 8B | Llama 3 70B | Whisper | SeamlessM4T v2 | Gemini 1.0 Ultra | Gemini 1.5 Pro |
|---|---|---|---|---|---|---|
| MLS (English) | 4.9 | 4.4 | 6.2 (v2) | 6.5 | 4.4 | **4.2** |
| LibriSpeech (test-other) | 3.4 | **3.1** | 4.9 (v2) | 6.2 | – | – |
| VoxPopuli (English) | 6.2 | **5.7** | 7.0 (v2) | 7.0 | – | – |
| FLEURS (34 languages) | 9.6 | **8.2** | 14.4 (v3) | 11.7 | – | – |

Table 31 demonstrates the strong performance of Llama 3 (and multi-modal foundation models more generally) on speech recognition tasks: the model outperforms models that are tailored to speech like Whisper^20 and SeamlessM4T on all benchmarks. On MLS English, Llama 3 performs similarly to Gemini. [p. 67]

^20 On FLEURS ASR, Malayalam is not officially reported for Whisper v3, so the average of 33 languages is used.

**Speech translation.** [p. 67] The models are also evaluated on speech translation tasks in which the model is asked to translate non-English speech into English text. The FLEURS and Covost 2 (Wang et al., 2021b) datasets are used in these evaluations, measuring BLEU scores of the translated English. Table 32 presents the results of these experiments.^21 The performance of the models in speech translation highlights the advantages of multimodal foundation models for tasks such as speech translation. [p. 67]

^21 On Covost 2, evaluation is only on 15 (out of 21) languages.

**Table 32** BLEU score of our speech interface for Llama 3 on speech translation tasks. We report the performance of Whisper and SeamlessM4T for reference. [p. 67]

| | Llama 3 8B | Llama 3 70B | Whisper v2 | SeamlessM4T v2 |
|---|---|---|---|---|
| FLEURS (33 lang. -> English) | 29.5 | **33.7** | 21.9 | 28.6 |
| Covost 2 (15 lang. -> English) | 34.4 | **38.8** | 33.8 | 37.9 |

**Spoken question answering.** [p. 67] The speech interface of Llama 3 demonstrates remarkable question answering capabilities. The model can effortlessly comprehend code-switched speech without any prior exposure to such data. Notably, although the model was trained only on single-turn dialogue, it is capable of engaging in extended, coherent multi-turn dialogue sessions. Figure 30 presents a few examples that highlight these multilingual and multi-turn capabilities. [p. 67]

**Figure 30** (p. 68): "Transcribed dialogue examples using the speech interface for Llama 3. The examples illustrate zero-shot multi-turn and code-switching capabilities."
The figure shows three side-by-side transcribed audio conversations: (1) English/Italian/German code-switching about the movie "A Fish Called Wanda" and a cathedral in Milan; (2) English/Vietnamese code-switching about coffee and food in Vietnam; (3) Chinese/English code-switching about travel from San Francisco to Changchun and finding tofu pudding. Each conversation demonstrates multi-turn dialogue and switching between languages. [p. 68]

**Safety.** [p. 67] The safety of the speech model is evaluated on MuTox (Costa-jussa et al., 2023), a multilingual audio-based dataset of 20,000 utterances for English and Spanish and 4,000 for 19 other languages, each with toxicity labels attached. The audio is passed as input to the model and the output is evaluated for toxicity, after cleaning some special characters. The MuTox classifier (Costa-jussa et al., 2023) is applied and the results are compared with Gemini 1.5 Pro. The percentage of added toxicity (AT) is evaluated — when the input prompt is safe and the output is toxic — and the percentage of lost toxicity (LT) — when the input prompt is toxic and the answer is safe. Table 33 shows the results for English and an average across all 21 languages that were evaluated on.^22 The percentage of added toxicity is very low: the speech models have the lowest percentage of added toxicity for English, with less than 1%. It removes significantly more toxicity than it adds. [p. 67]

^22 Note that for Gemini, a significant number of responses were empty, which could be due to safety filters on their side (though some empty responses were for non-toxic input) or to rate limits. To conduct the analysis, it was assumed that all the empty responses are safe. This is the most conservative approach for results and the upper bound of what Gemini results would look like.

**Table 33** Speech toxicity of our speech interface to Llama 3 on the MuTox dataset. AT refers to added toxicity (%) and LT refers to lost toxicity (%). [p. 68]

| | Llama 3 8B | | Llama 3 70B | | Gemini 1.5 Pro | |
|---|---|---|---|---|---|---|
| Language | AT (down) | LT (up) | AT (down) | LT (up) | AT (down) | LT (up) |
| English | 0.84 | 15.09 | **0.68** | **15.46** | 1.44 | 13.42 |
| Overall | 2.31 | 9.89 | **2.00** | 10.29 | 2.06 | **10.94** |
