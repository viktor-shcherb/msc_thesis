# 8. Related Work [p. 22–24]

[p. 22–24] The Mixture of Experts (MoE) technique is first proposed by Jacobs et al. (1991); Jordan and Jacobs (1994) to deal with different samples with independent expert modules. Shazeer et al. (2017) introduce MoE into language model training and build a large-scale LSTM-based (Hochreiter and Schmidhuber, 1997) MoE models. As Transformer become the most popular architecture for NLP, many attempts extend FFNs in a Transformer as MoE layers to build MoE language models.

**Routing strategies:**
- GShard (Lepikhin et al., 2021) and Switch Transformer (Fedus et al., 2021) are pioneers which employ learnable top-2 or top-1 routing strategies to scale the MoE language models to an extremely large scale.
- Hash Layer (Roller et al., 2021) and StableMoE (Dai et al., 2022b) use fixed routing strategies for more stable routing and training.
- Zhou et al. (2022) propose an expert-choice routing strategy, where each token can be assigned to different numbers of experts.
- Zoph (2022) focus on the issues of training instability and fine-tuning difficulty in MoE models, and propose ST-MoE to overcome these challenges.

**Large-scale MoE models:**
- In addition to research on MoE architectures and training strategies, recent years have also witnessed the emergence of numerous large-scale language or multimodal models (Du et al., 2022; Lin et al., 2021; Ren et al., 2023; Xue et al., 2023) based on existing MoE architectures.

**Gap identified by this paper:**
- By and large, most of the previous MoE models are based on conventional top-1 or top-2 routing strategies, leaving large room for improving expert specialization. In response, the DeepSeekMoE architecture aims to improve the expert specialization to the utmost extent.
