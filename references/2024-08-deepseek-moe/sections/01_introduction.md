# 1. Introduction [p. 1-4]

## Motivation

[p. 1] Recent research has empirically demonstrated that, with sufficient training data, scaling language models with increased parameters and computational budgets can yield remarkably stronger models (Brown et al., 2020; Hoffmann et al., 2022; OpenAI, 2023; Touvron et al., 2023a). However, scaling models to an extremely large scale is associated with exceedingly high computational costs. The Mixture-of-Experts (MoE) architecture (Jacobs et al., 1991; Jordan and Jacobs, 1994; Shazeer et al., 2017) has emerged as a popular solution: it can enable parameter scaling while concurrently keeping computational costs at a modest level.

[p. 2] Recent applications of MoE architectures in Transformers (Vaswani et al., 2017) have yielded successful attempts at scaling language models to a substantial size (Du et al., 2022; Fedus et al., 2021; Lepikhin et al., 2021; Zoph, 2022), accompanied with remarkable performance.

## Problems with Existing MoE

[p. 2] Existing MoE architectures potentially suffer from issues of knowledge hybridity and knowledge redundancy, which limit expert specialization (i.e., each expert acquires non-overlapping and focused knowledge).

Conventional MoE architectures substitute the Feed-Forward Networks (FFNs) in a Transformer with MoE layers. Each MoE layer consists of multiple experts, with each structurally identical to a standard FFN, and each token is assigned to one (Fedus et al., 2021) or two (Lepikhin et al., 2021) experts. This architecture manifests two potential issues:

1. **Knowledge Hybridity:** existing MoE practices often employ a limited number of experts (e.g., 8 or 16), and thus tokens assigned to a specific expert will be likely to cover diverse knowledge. Consequently, the designated expert will intend to assemble vastly different types of knowledge in its parameters, which are hard to utilize simultaneously. [p. 2]

2. **Knowledge Redundancy:** tokens assigned to different experts may require common knowledge. As a result, multiple experts may converge in acquiring shared knowledge in their respective parameters, thereby leading to redundancy in expert parameters. [p. 2]

These issues collectively hinder expert specialization in existing MoE practices, preventing them from reaching the theoretical upper-bound performance of MoE models.

## DeepSeekMoE Proposal

[p. 2-3] In response, the authors introduce **DeepSeekMoE**, an innovative MoE architecture specifically designed towards ultimate expert specialization. It involves two principal strategies:

1. **Fine-Grained Expert Segmentation:** while maintaining the number of parameters constant, the experts are segmented into a finer grain by splitting the FFN intermediate hidden dimension. Keeping a constant computational cost, more fine-grained experts are activated to enable a more flexible and adaptable combination of activated experts. Fine-grained expert segmentation allows diverse knowledge to be decomposed more finely and be learned more precisely into different experts, where each expert will retain a higher level of specialization. [p. 2-3]

2. **Shared Expert Isolation:** certain experts are isolated to serve as shared experts that are always activated, aiming at capturing and consolidating common knowledge across varying contexts. Through compressing common knowledge into these shared experts, redundancy among other routed experts will be mitigated, enhancing parameter efficiency and ensuring that each routed expert retains specialized by focusing on distinctive aspects. [p. 3]

## Validation at 2B Scale

[p. 3] Starting from a modest scale with 2B parameters, the authors validate the advantages of the DeepSeekMoE architecture. They conduct evaluations on 12 zero-shot or few-shot benchmarks spanning diverse tasks. Empirical results indicate that:

- DeepSeekMoE 2B surpasses GShard 2B (Lepikhin et al., 2021) by a substantial margin.
- DeepSeekMoE 2B even matches GShard 2.9B, a larger MoE model with 1.5x expert parameters and computation.
- DeepSeekMoE 2B nearly approaches the performance of its dense counterpart with an equivalent number of parameters, which sets the strict upper bound of MoE language models.

Elaborate ablation studies and analysis on expert specialization validate the effectiveness of fine-grained expert segmentation and shared expert isolation.

## Scaling to 16B

[p. 3] The authors subsequently scale up DeepSeekMoE to 16B and train it on a large-scale corpus with 2T tokens. Evaluation results reveal that with only about 40% of computations, DeepSeekMoE 16B achieves comparable performance with DeepSeek 7B (DeepSeek-AI, 2024), a dense model trained on the same 2T corpus. DeepSeekMoE 16B consistently outperforms models with a similar number of activated parameters by a large margin, and achieves comparable performance with LLaMA2 7B (Touvron et al., 2023b), which has approximately 2.5 times the activated parameters. Figure 1 demonstrates the evaluation results on the Open LLM Leaderboard.^1

^1 https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard

Additionally, the authors conduct supervised fine-tuning (SFT) for alignment, transforming the model into a chat model. DeepSeekMoE Chat 16B achieves comparable performance with DeepSeek Chat 7B and LLaMA2 SFT 7B in the chat setting.

## Scaling to 145B

[p. 3] The authors further undertake a preliminary endeavor to scale up DeepSeekMoE to 145B. The experimental results still validate its substantial advantages over the GShard architecture consistently. In addition, it shows performance comparable with DeepSeek 67B, using only 28.5% (maybe even 18.2%) of computations.

## Contributions

[p. 3-4] The contributions are summarized as follows:

- **Architectural Innovation.** Introduction of DeepSeekMoE, an innovative MoE architecture aiming at achieving ultimate expert specialization, which employs two principal strategies of fine-grained expert segmentation and shared expert isolation.
- **Empirical Validation.** Extensive experiments to empirically validate the effectiveness of the DeepSeekMoE architecture. Experimental results validate the high level of expert specialization in DeepSeekMoE 2B, and indicate that DeepSeekMoE 2B can nearly approach the upper bound performance for MoE models.
- **Scalability.** DeepSeekMoE scaled to 16B, achieving comparable performance with DeepSeek 7B and LLaMA2 7B with only about 40% of computations. Preliminary endeavor to scale to 145B, highlighting consistent advantages over GShard architecture and showing comparable performance with DeepSeek 67B.
- **Alignment for MoE.** Successfully perform supervised fine-tuning on DeepSeekMoE 16B to create an aligned chat model, showcasing the adaptability and versatility of DeepSeekMoE 16B.
- **Public Release.** Release of the model checkpoint of DeepSeekMoE 16B to the public. The model can be deployed on a single GPU with 40GB of memory without the need for quantization.

## Figures

**Figure 1** (p. 2): "Comparison between DeepSeekMoE 16B and open source models on the Open LLM Leaderboard. The red dashed line is linearly fitted from data points of all models except DeepSeekMoE 16B. DeepSeekMoE 16B consistently outperforms models with a similar number of activated parameters by a large margin, and achieves comparable performance with LLaMA2 7B, which has approximately 2.5 times the activated parameters."

- X-axis: Number of Activated Parameters (Billions), range ~2 to ~7.
- Y-axis: Average Performance, range ~35 to ~52.
- Data points visible:
  - GPT-neo 2.7B: ~2.7B activated params, ~36 avg performance
  - OPT 2.7B: ~2.7B activated params, ~37 avg performance
  - Pythia 2.8B: ~2.8B activated params, ~37.5 avg performance
  - BLOOM 3B: ~3B activated params, ~37 avg performance
  - RedPajama-INCITE 3B: ~3B activated params, ~39 avg performance
  - Open LLaMA 3B: ~3B activated params, ~39.5 avg performance
  - **DeepSeekMoE 16B**: ~2.8B activated params, ~51 avg performance (red star, well above the red dashed line)
  - GPT-J 6B: ~6B activated params, ~42 avg performance
  - RedPajama-INCITE 7B: ~7B activated params, ~43 avg performance
  - Open LLaMA 7B: ~7B activated params, ~44 avg performance
  - Falcon 7B: ~7B activated params, ~46 avg performance
  - LLaMA 7B: ~7B activated params, ~47 avg performance
  - LLaMA2 7B: ~7B activated params, ~50.5 avg performance
- Red dashed line is linearly fitted from all models except DeepSeekMoE 16B, showing the general trend.
- DeepSeekMoE 16B dramatically outperforms the trend line, achieving ~51 avg performance with only ~2.8B activated parameters.
