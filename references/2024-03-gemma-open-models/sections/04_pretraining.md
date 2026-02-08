# Pretraining [p. 3-4]

## Training Data

Gemma 2B and 7B are trained on 3T and 6T tokens respectively of primarily-English data from web documents, mathematics, and code. Unlike Gemini, these models are not multimodal, nor are they trained for state-of-the-art performance on multilingual tasks. [p. 3]

A subset of the SentencePiece tokenizer (Kudo and Richardson, 2018) of Gemini is used for compatibility. It splits digits, does not remove extra whitespace, and relies on byte-level encodings for unknown tokens, following the techniques used for both (Chowdhery et al., 2022) and (Gemini Team, 2023). The vocabulary size is 256k tokens. [p. 3]

## Filtering

The pre-training dataset is filtered to reduce the risk of unwanted or unsafe utterances, and to filter out certain personal information or other sensitive data. This includes both heuristics and model-based classifiers to remove harmful or low-quality content. Further, all evaluation sets are filtered from the pre-training data mixture, targeted contamination analyses are run to check against evaluation set leakage, and the risk of recitation is reduced by minimizing proliferation of sensitive outputs. [p. 3]

The final data mixture was determined through a series of ablations on both the 2B and 7B models. Similar to the approach advocated in (Gemini Team, 2023), training is staged to alter the corpus mixture throughout training to increase the weight of relevant, high-quality data towards the end of training. [p. 3-4]
