# Conclusions [p. 17]

[p. 17] In this work, we introduced Eagle (RWKV-5) and Finch (RWKV-6), marking substantial progress in RNN-based language models by integrating multiheaded matrix-valued states and dynamic data-driven recurrence mechanisms. These models demonstrate exceptional performance on MQAR and diverse linguistic benchmarks, challenging the dominance of traditional transformer architectures while retaining key RNN advantages. With models publicly available under the Apache 2.0 license and trained on an extensive multilingual corpus, our work not only advances the capabilities of language models but also emphasizes community accessibility and applicability across various domains. While acknowledging the computational and ethical challenges ahead, we hope that Eagle and Finch's efficient new architecture and wide availability will help push the boundaries of language modeling and pave the way for future innovations.

## Limitations

[p. 17] The Eagle and Finch models fall short on certain aspects that can be mitigated and addressed in future work.

[p. 17] We experimented with using Eagle as an embedding model on the Massive Text Embedding Benchmark (MTEB) (Muennighoff et al., 2023) and were not able to get strong embedding performance. We believe that its state is a very high-quality embedding of the context but an appropriate method is required to aggregate the information from this to fit future work.

[p. 17] Because our training corpus contains some synthetic data from GPT-3.5 and ChatGPT, our released models exhibit behaviors similar to ChatGPT and will mimic ChatGPT's conversation style and tone. For instance, the model might respond with phrases like that it is trained by OpenAI. However, this is not a general property of the RWKV architecture but rather a specific outcome of the data and training process.

## Future Work

[p. 17] Our 1.12 trillion token multilingual training corpus is much smaller than the training data sizes for contemporary models such as LLaMA2 (Touvron et al., 2023), and expanding our training corpus to be more diverse and expansive is a key priority to improving model performance (Albalak et al., 2024). We also plan to train and release larger versions of Finch such as 7B and 14B parameters, and further extend its performance with reduced inference and training costs via Mixture of Experts (Shazeer et al., 2017).

## Acknowledgments

[p. 17] We thank Stability AI for the compute used to train our models and for technical support in the development of RWKV. We also thank the members of the RWKV and EleutherAI Discord servers for their help and work on further extending the applicability of RWKV to different domains. We also thank Shenzhen Yuanshi Intelligence Co., Ltd. for its contribution to the promotion and commercialization of RWKV. We thank Songlin Yang for assistance with the code and ideas for our time-parallel implementations.
