# Appendix F: Multilingual MMLU [p. 29, 32-33]

[p. 29] All questions and answers from MMLU [49] were translated using Azure Translate. An external model was used to perform the translation, instead of relying on GPT-4 itself, in case the model had unrepresentative performance for its own translations. A range of languages was selected that cover different geographic regions and scripts. An example question taken from the *astronomy* category translated into Marathi, Latvian and Welsh is shown in Table 13. The translations are not perfect, in some cases losing subtle information which may hurt performance. Furthermore some translations preserve proper nouns in English, as per translation conventions, which may aid performance. [p. 29]

The same MMLU prompt as [4] was incorporated: the model is instructed that it is an intelligent agent, supplied with the questions and a list of four answer options labelled 'A-D', followed by 'Answer:'. The model instruction, question and answers are translated, however the 'Answer' token is preserved along with the 'A-D' options in English. An example prompt is shown in Table 12. The prompts are composed three-shot, with the three examples picked from the development set. Three-shot evaluation is used over the regular five-shot because some languages map to much longer token sequences. The correct answer is classified by picking the A-D token continuation with the highest probability from the model. [p. 29]

## Table 12

**Table 12.** MMLU Example prompt, presented in two different languages. Note: the choice (A-D) or 'Answer' tokens are not translated for prompt format consistency. [p. 32]

| English | Swahili |
|---|---|
| A highly knowledgeable and intelligent artificial intelligence model answers multiple-choice questions about machine learning | Muundo wa akili bandia wenye ujuzi wa hali ya juu na akili hujibu maswali ya chaguo-nyingi kuhusu ujifunzaji wa mashine. |
| As the number of training examples goes to infinity, your model trained on that data will have: | Kadiri idadi ya mifano ya mafunzo inavyoenda kwa infinity, mfano wako uliofunzwa kwenye data hiyo utakuwa na: |
| A) Lower variance | A) Tofauti ya chini |
| B) Higher variance | B) Tofauti ya juu |
| C) Same variance | C) Tofauti sawa |
| D) None of the above | D) Hakuna kati ya zilizo hapo juu |
| Answer: | Answer: |

## Table 13

**Table 13.** An example MMLU question translated into Marathi, Latvian, and Welsh. [p. 33]

| Language | Example |
|---|---|
| English (>1B speakers) | Why is the sky blue? A) Because the molecules that compose the Earth's atmosphere have a blue-ish color. B) Because the sky reflects the color of the Earth's oceans. C) Because the atmosphere preferentially scatters short wavelengths. D) Because the Earth's atmosphere preferentially absorbs all other colors. |
| Marathi (90M speakers) | (Translated into Marathi script with Devanagari characters) A-D options translated. |
| Latvian (2M speakers) | (Translated into Latvian) A-D options translated. |
| Welsh (600k speakers) | (Translated into Welsh) A-D options translated. |
