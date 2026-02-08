# 5 Safety [p. 9]

To enhance the model's trustworthiness and safety, a full-stack Responsible AI Safety Engine (RAISE) is developed. RAISE ensures safe pretraining, alignment, and deployment. This section discusses safety measures in the pretraining and alignment stages.

## Safety in Pretraining

[p. 9]

Aligning with standard pretraining data safety practices [5, 58, 77], a set of filters is built based on heuristic rules, keyword matching, and learned classifiers to remove text containing personal identifiers and private data, and reduce sexual, violent, and extremist content.

## Safety in Alignment

[p. 9]

Informed by existing research in [24, 35], a comprehensive safety taxonomy is first built. This taxonomy covers a broad spectrum of potential concerns, including environmental disharmony, superstitious, religious sensitivities, discriminatory practices, substance abuse, violent behavior, illegal activities, hate speech, ethical violations, privacy breaches, self-harm, sexually explicit content, mental health issues, and cybersecurity threats.

Curated datasets reflecting these categories are created for a robust alignment, and mixed with dialog SFT data. A targeted set of prompts simulating attack scenarios is also included in the alignment phase, which effectively improved the model's resilience against malicious use.
