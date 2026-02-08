# 7.7 Video Recognition Results [p. 61–62]

[p. 61] The video adapter for Llama 3 is evaluated on three benchmarks:

- **PerceptionTest** (Patraucean et al., 2023) evaluates the model's ability to answer temporal reasoning questions focusing on skills (memory, abstraction, physics, semantics) and different types of reasoning (descriptive, explanatory, predictive, counterfactual). It consists of 11.6K test QA pairs, each with an on-average 23s long video, filmed by 100 participants worldwide to show perceptually interesting tasks. The focus is on the multiple-choice question answering task, where each question is paired with [p. 62] three possible options. Performance is reported on the held-out test split which is accessed by submitting predictions to an online challenge server.^16

- **NExT-QA** (Xiao et al., 2021) is another temporal and causal reasoning benchmark, with a focus on open-ended question answering. It consists of 1K test videos each on-average 44s in length, paired with 9K questions. The evaluation is performed by comparing the model's responses with the ground truth answer using Wu-Palmer Similarity (WUPS) (Wu and Palmer, 1994).^17

- **TVQA** (Lei et al., 2018) evaluates the model's ability to perform compositional reasoning, requiring spatiotemporal localization of relevant moments, recognition of visual concepts, and joint reasoning with subtitle-based dialogue. This dataset, being derived from popular TV shows, additionally tests for the model's ability to leverage its outside-knowledge of those TV shows in answering the questions. It consists of over 15K validation QA pairs, with each corresponding video clip being on-average 76s in length. It also follows a multiple-choice format with five options for each question, and performance is reported on the validation set following prior work (OpenAI, 2023b). [p. 62]

- **ActivityNet-QA** (Yu et al., 2019) evaluates the model's ability to reason over long video clips to understand actions, spatial relations, temporal relations, counting, etc. It consists of 8K test QA pairs from 800 videos, each on-average 3 minutes long. For evaluation, the protocol from prior work (Google, 2023; Lin et al., 2023; Maaz et al., 2024) is followed, where the model generates short one-word or one-phrase answers, and the correctness of the output is evaluated using the GPT-3.5 API which compares it to the ground truth answer. The average accuracy as evaluated by the API is reported. [p. 62]

^16 See https://eval.ai/web/challenges/challenge-page/2091/overview.
^17 See https://github.com/doc-doc/NExT-OE.

## Inference Setup [p. 62]

[p. 62] When performing inference, frames are uniformly sampled from the full video clip and passed into the model with a short text prompt. Since most benchmarks involve answering multiple-choice questions, the following prompt is used: **Select the correct answer from the following options: {question}. Answer with the correct option letter and nothing else.** For benchmarks that require producing a short answer (e.g., ActivityNet-QA and NExT-QA), the following prompt is used: **Answer the question using a single word or phrase. {question}.** For NExT-QA, since the evaluation metric (WUPS) is sensitive to the length and the specific words used, the model is additionally prompted to be specific and respond with the most salient answer, for instance specifying "living room" instead of simply responding with "house" when asked a location question. For benchmarks that contain subtitles (i.e., TVQA), the subtitles corresponding to the clip are included in the prompt during inference. [p. 62]

## Results [p. 62]

**Table 30** (p. 62): "Video understanding performance of our vision module attached to Llama 3. We find that across range of tasks covering long-form and temporal video understanding, our vision adapters for Llama3 8B and 70B parameters are competitive and sometimes even outperform alternative models."

|                         | Llama 3-V 8B | Llama 3-V 70B | Gemini 1.0 Pro | Gemini 1.0 Ultra | Gemini 1.5 Pro | GPT-4V | GPT-4o |
|-------------------------|-------------|--------------|----------------|-----------------|----------------|--------|--------|
| PerceptionTest (test)   | 53.8        | **60.8**     | 51.1           | 54.7            | --             | --     | --     |
| TVQA (val)              | 82.5        | **87.9**     | --             | --              | --             | 87.3   | --     |
| NExT-QA (test)          | 27.3        | **30.3**     | 28.0           | 29.9            | --             | --     | --     |
| ActivityNet-QA (test)   | 52.7        | 56.3         | 49.8           | 52.2            | 57.5           | --     | **61.9** |

[p. 62] The performance of Llama 3 8B and 70B is presented in Table 30. Llama 3's performance is compared with that of two Gemini and two GPT-4 models. All results are zero-shot, as none of these benchmarks are included in the training or finetuning data. The Llama 3 models that train a small video adapter during post-training are found to be very competitive, and in some cases even better, than other models that potentially leverage native multimodal processing all the way from pre-training. Llama 3 performs particularly well on video recognition given that only the 8B and 70B parameter models are evaluated. Llama 3 achieves its best performance on PerceptionTest, suggesting the model has a strong ability to perform complex temporal reasoning. On long-form activity understanding tasks like ActivityNet-QA, Llama 3 is able to obtain strong results even though it is processing only up to 64 frames, which means that for a 3-minute long video the model only processes one frame every 3 seconds. [p. 62]
