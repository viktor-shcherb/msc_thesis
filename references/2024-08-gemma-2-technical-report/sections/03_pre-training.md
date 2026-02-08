# 3. Pre-training [p. 3–4]

## 3.1. Training Data [p. 3]

Gemma 2 27B is trained on 13 trillion tokens of primarily-English data. The 9B model is trained on 8 trillion tokens, and the 2B model on 2 trillion tokens. These tokens come from a variety of data sources, including web documents, code, and science articles. The models are not multimodal and are not trained specifically for state-of-the-art multilingual capabilities. The final data mixture was determined through ablations similar to the approach in Gemini 1.0 (Gemini Team, 2023). [p. 3]

**Tokenizer.** The same tokenizer as Gemma 1 and Gemini is used: a SentencePiece tokenizer with split digits, preserved whitespace, and byte-level encodings (Kudo and Richardson, 2018). The resulting vocabulary has 256k entries. [p. 3]

**Filtering.** The same data filtering techniques as Gemma 1 are used. Specifically, the pre-training dataset is filtered to reduce the risk of unwanted or unsafe utterances, filter out certain personal information or other sensitive data, decontaminate evaluation sets from the pre-training data mixture, and reduce the risk of recitation by minimizing the proliferation of sensitive outputs. [p. 3]

## Table 3 | Training infrastructure with sharding [p. 3]

| Model | Type | #Chips | Data (Shards) | Model (Shards) |
|---|---|---|---|---|
| 2B | TPUv5e | 512 | 512 | 1 |
| 9B | TPUv4 | 4096 | 1024 | 4 |
| 27B | TPUv5p | 6144 | 768 | 8 |

## Table 4 | Relevant formatting control tokens used for Gemma models [p. 3]

| Context | Relevant Token |
|---|---|
| User turn | `user` |
| Model turn | `model` |
| Start of conversation turn | `<start_of_turn>` |
| End of conversation turn | `<end_of_turn>` |
| Beginning of sequence | `<bos>` |
| End of sequence | `<eos>` |

## 3.2. Knowledge Distillation [p. 3]

Given a large model used as a teacher, smaller models are learned by distilling from the probability given by the teacher of each token *x* given its context *x_c*, i.e., *P_T(x | x_c)*. More precisely, the negative log-likelihood between the probabilities from the teacher and the student is minimized: [p. 3]

$$\min_{P_S} \sum_x -P_T(x \mid x_c) \log P_S(x \mid x_c)$$

where *P_S* is the parameterized probability of the student. Knowledge distillation was also used in Gemini 1.5 (Gemini Team, 2024). [p. 3]

## 3.3. Compute Infrastructure [p. 3]

Models are trained with TPUv4, TPUv5e, and TPUv5p as outlined in Table 3. [p. 3]

- **2B model:** 2x16x16 configuration of TPUv5e, totaling 512 chips, with 512-way data replication and 1-way model sharding.
- **9B model:** 8x16x32 configuration of TPUv4, totaling 4096 chips, with 1024-way data replication and 4-way model sharding.
- **27B model:** 8x24x32 configuration of TPUv5p, totaling 6144 chips, with 768-way data replication and 8-way model sharding.

The optimizer state is further sharded using techniques similar to ZeRO-3 (Ren et al., 2021). For scales beyond a single pod, data-replica reduction is performed over the data center network, using the Pathways approach of Barham et al. (2022). The 'single controller' programming paradigm of Jax (Roberts et al., 2023) and Pathways (Barham et al., 2022) is also used. As in Gemma 1, the GSPMD partitioner (Xu et al., 2021) is used for training step computation and the MegaScale XLA compiler (XLA, 2019). [p. 3]

## 3.4. Carbon Footprint [p. 4]

The carbon emissions from pre-training the Gemma models are estimated to be 1247.61 tCO₂eq. As in Gemma 1 (Gemma Team, 2024), this value is calculated based on the hourly energy usage reported directly from the TPU data centers and scaled to account for the additional energy expended to create and maintain the data center. Google data centers are carbon neutral, achieved through a combination of energy efficiency, renewable energy purchases, and carbon offsets. This carbon neutrality applies to the experiments and the machines running them. [p. 4]
