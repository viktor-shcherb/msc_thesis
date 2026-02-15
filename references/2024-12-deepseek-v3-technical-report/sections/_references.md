# References Cited in Notes

This file contains only the references that were cited in the section notes.

## References from Introduction and Architecture sections

**Anthropic, 2024**
- Cited in 01_introduction.md as one of the closed-source model providers showing rapid LLM iteration and evolution

**Google, 2024**
- Cited in 01_introduction.md as one of the closed-source model providers showing rapid LLM iteration and evolution

**OpenAI, 2024a**
- Cited in 01_introduction.md as one of the closed-source model providers showing rapid LLM iteration and evolution

**DeepSeek-AI, 2024a,b**
- Cited in 01_introduction.md as part of the DeepSeek series of open-source models making strides toward AGI

**Guo et al., 2024**
- Cited in 01_introduction.md as part of the DeepSeek series

**AI@Meta, 2024a,b**
- Cited in 01_introduction.md as the LLaMA series of open-source models

**Touvron et al., 2023a,b**
- Cited in 01_introduction.md as the LLaMA series of open-source models

**Qwen, 2023, 2024a,b**
- Cited in 01_introduction.md as the Qwen series of open-source models

**Jiang et al., 2023**
- Cited in 01_introduction.md as the Mistral series of open-source models

**Mistral, 2024**
- Cited in 01_introduction.md as the Mistral series of open-source models

**DeepSeek-AI, 2024c**
- Cited in 01_introduction.md, 02_architecture.md, 04_pre-training.md, and 05_post-training.md as the source of Multi-head Latent Attention (MLA) for efficient inference, DeepSeek-V2, and long context extension approach

**Dai et al., 2024**
- Cited in 01_introduction.md and 02_architecture.md as the source of DeepSeekMoE for cost-effective training

**Wang et al., 2024a**
- Cited in 01_introduction.md as the source of the auxiliary-loss-free strategy for load balancing

**Dettmers et al., 2022**
- Cited in 01_introduction.md as work on low-precision training as a promising solution for efficient training

**Kalamkar et al., 2019**
- Cited in 01_introduction.md as work on low-precision training

**Narang et al., 2017**
- Cited in 01_introduction.md as work on low-precision training

**Peng et al., 2023b**
- Cited in 01_introduction.md as work on low-precision training

**Luo et al., 2024**
- Cited in 01_introduction.md as work on hardware capabilities tied to low-precision training evolution (HiFloat8 format for deep learning)

**Micikevicius et al., 2022**
- Cited in 01_introduction.md as work on hardware capabilities tied to low-precision training evolution

**Rouhani et al., 2023a**
- Cited in 01_introduction.md as work on hardware capabilities tied to low-precision training evolution

**Rouhani et al., 2023b**
- Cited in 03_infrastructures.md as source of microscaling data formats idea for fine-grained quantization

**Vaswani et al., 2017**
- Cited in 02_architecture.md as the Transformer framework and standard Multi-Head Attention (MHA)

**Su et al., 2024**
- Cited in 02_architecture.md as the source of Rotational Position Embedding (RoPE)

**Gloeckle et al., 2024**
- Cited in 02_architecture.md as inspiration for Multi-Token Prediction (MTP) objective

**Li et al., 2024b**
- Cited in 02_architecture.md as the source of EAGLE speculative decoding approach that maintains causal chain

**Leviathan et al., 2023**
- Cited in 02_architecture.md as work on speculative decoding

**Xia et al., 2023**
- Cited in 02_architecture.md as work on speculative decoding

**Shazeer et al., 2017**
- Cited in 02_architecture.md as describing routing collapse in MoE models

**Fedus et al., 2021**
- Cited in 02_architecture.md as using auxiliary loss for load balance in MoE

**Lepikhin et al., 2021**
- Cited in 02_architecture.md as traditional MoE architecture (GShard) and in 03_infrastructures.md as source of Expert Parallelism (EP)

## References from Infrastructures section

**Qi et al., 2023a**
- Cited in 03_infrastructures.md as source of Pipeline Parallelism (PP)

**Qi et al., 2023b**
- Cited in 03_infrastructures.md as source of ZeroBubble method for splitting backward into input and weights components

**Rajbhandari et al., 2020**
- Cited in 03_infrastructures.md as source of ZeRO-1 Data Parallelism (DP)

**Harlap et al., 2018**
- Cited in 03_infrastructures.md as source of 1F1B pipeline parallelism method

**Li and Hoefler, 2021**
- Cited in 03_infrastructures.md as source of Chimera pipeline parallelism approach

**Bauer et al., 2014**
- Cited in 03_infrastructures.md as source of warp specialization technique for communication optimization

**Noune et al., 2022**
- Cited in 03_infrastructures.md as work on low-precision training advances

**Fishman et al., 2024**
- Cited in 03_infrastructures.md as work on outliers limiting low-precision training and successful FP8 pre-training application

**He et al.**
- Cited in 03_infrastructures.md as work on outliers in low-precision training (no year provided in paper)

**Sun et al., 2024**
- Cited in 03_infrastructures.md as work on outliers in low-precision training

**Frantar et al., 2022**
- Cited in 03_infrastructures.md as work on inference quantization progress

**Xiao et al., 2023**
- Cited in 03_infrastructures.md as work on inference quantization progress

**Graham et al., 2016**
- Cited in 03_infrastructures.md as source of NVIDIA SHARP network co-processor

**Wortsman et al., 2023**
- Cited in 03_infrastructures.md as work showing that limited accumulation precision becomes more pronounced when the inner dimension K is large in GEMM operations

**Thakkar et al., 2023**
- Cited in 03_infrastructures.md as source of the strategy of promotion to CUDA Cores for higher precision in FP8 training

**Sun et al., 2019b**
- Cited in 03_infrastructures.md as prior work using hybrid FP8 format (E4M3 in Fprop, E5M2 in Dgrad/Wgrad)

**NVIDIA, 2022**
- Cited in 03_infrastructures.md as source of IBGDA (GPUDirect Async) technology for reducing latency and enhancing communication efficiency in decoding

**NVIDIA, 2024a**
- Cited in 03_infrastructures.md as announcement of Blackwell architecture support for microscaling formats with smaller quantization granularity

**NVIDIA, 2024b**
- Cited in 03_infrastructures.md as example of FP8 frameworks using limited accumulation precision as default option, and as prior work using hybrid FP8 format

## References from Pre-Training section

**Ding et al., 2024**
- Cited in 04_pre-training.md as inspiration for document packing method for data integrity

**DeepSeek-AI, 2024a**
- Cited in 04_pre-training.md as DeepSeekCoder-V2, where Fill-in-Middle (FIM) strategy was observed not to compromise next-token prediction

**Shibata et al., 1999**
- Cited in 04_pre-training.md as source of Byte-level BPE tokenization approach

**Lundberg, 2023**
- Cited in 04_pre-training.md as describing bias issues with combined punctuation and line break tokens in multi-line prompts

**Loshchilov and Hutter, 2017**
- Cited in 03_infrastructures.md and 04_pre-training.md as source of AdamW optimizer

**Peng et al., 2023a**
- Cited in 04_pre-training.md as source of YaRN (Yet another RoPE extensioN method) for long context extension

**Hendrycks et al., 2020**
- Cited in 04_pre-training.md as source of MMLU benchmark

**Gema et al., 2024**
- Cited in 04_pre-training.md as source of MMLU-Redux benchmark

**Wang et al., 2024b**
- Cited in 04_pre-training.md as source of MMLU-Pro benchmark

**OpenAI, 2024b**
- Cited in 04_pre-training.md as source of MMMLU benchmark

**Huang et al., 2023**
- Cited in 04_pre-training.md as source of C-Eval benchmark

**Li et al., 2023**
- Cited in 04_pre-training.md as source of CMMLU benchmark

**Zellers et al., 2019**
- Cited in 04_pre-training.md as source of HellaSwag benchmark

**Bisk et al., 2020**
- Cited in 04_pre-training.md as source of PIQA benchmark

**Clark et al., 2018**
- Cited in 04_pre-training.md as source of ARC benchmark

**Suzgun et al., 2022**
- Cited in 04_pre-training.md as source of BigBench Hard (BBH) benchmark

**Joshi et al., 2017**
- Cited in 04_pre-training.md as source of TriviaQA benchmark

**Kwiatkowski et al., 2019**
- Cited in 04_pre-training.md as source of NaturalQuestions benchmark

**Lai et al., 2017**
- Cited in 04_pre-training.md as source of RACE benchmark

**Dua et al., 2019**
- Cited in 04_pre-training.md as source of DROP benchmark

**Sun et al., 2019a**
- Cited in 04_pre-training.md as source of C3 benchmark

**Cui et al., 2019**
- Cited in 04_pre-training.md as source of CMRC benchmark

**Xu et al., 2020**
- Cited in 04_pre-training.md as source of CLUEWSC benchmark

**Sakaguchi et al., 2019**
- Cited in 04_pre-training.md as source of WinoGrande benchmark

**Gao et al., 2020**
- Cited in 04_pre-training.md as source of Pile language modeling benchmark

**Li et al., 2021**
- Cited in 04_pre-training.md as source of CCPM benchmark

**Cobbe et al., 2021**
- Cited in 04_pre-training.md as source of GSM8K math benchmark

**Hendrycks et al., 2021**
- Cited in 04_pre-training.md as source of MATH benchmark

**Shi et al., 2023**
- Cited in 04_pre-training.md as source of MGSM math benchmark

**Wei et al., 2023**
- Cited in 04_pre-training.md as source of CMath benchmark

**Chen et al., 2021**
- Cited in 04_pre-training.md as source of HumanEval code benchmark

**Jain et al., 2024**
- Cited in 04_pre-training.md and 05_post-training.md as source of LiveCodeBench code benchmark

**Austin et al., 2021**
- Cited in 04_pre-training.md as source of MBPP code benchmark

**Gu et al., 2024**
- Cited in 04_pre-training.md as source of CRUXEval code benchmark

**Zhong et al., 2023**
- Cited in 04_pre-training.md as source of AGIEval standardized exam benchmark

**DeepSeek-AI, 2024b;c**
- Cited in 04_pre-training.md as previous work using perplexity-based and generation-based evaluation approaches

**Qwen, 2024b**
- Cited in 04_pre-training.md as source of Qwen2.5 72B Base baseline model

**AI@Meta, 2024b**
- Cited in 04_pre-training.md as source of LLaMA-3.1 405B Base baseline model

## References from Post-Training section

**Shao et al., 2024**
- Cited in 05_post-training.md as source of Group Relative Policy Optimization (GRPO) for RL training

**Zhou et al., 2023**
- Cited in 05_post-training.md as source of IFEval benchmark

**Krishna et al., 2024**
- Cited in 05_post-training.md as source of FRAMES benchmark

**Bai et al., 2024**
- Cited in 05_post-training.md as source of LongBench v2 benchmark

**Rein et al., 2023**
- Cited in 05_post-training.md as source of GPQA benchmark

**OpenAI, 2024c**
- Cited in 05_post-training.md as source of SimpleQA benchmark

**He et al., 2024**
- Cited in 05_post-training.md as source of C-SimpleQA benchmark

**OpenAI, 2024d**
- Cited in 05_post-training.md as source of SWE-Bench benchmark

**MAA, 2024**
- Cited in 05_post-training.md as source of American Invitational Mathematics Examination 2024 (AIME 2024) benchmark

**Xia et al., 2024**
- Cited in 05_post-training.md as source of agentless framework used for SWE-Bench verified evaluation

**Lin, 2024**
- Cited in 05_post-training.md as source of Zero-Eval prompt format for MMLU-Redux

**Dubois et al., 2024**
- Cited in 05_post-training.md as source of AlpacaEval 2.0 benchmark for open-ended generation evaluation

**Li et al., 2024a**
- Cited in 05_post-training.md as source of Arena-Hard benchmark for open-ended generation evaluation

**Lambert et al., 2024**
- Cited in 05_post-training.md as source of RewardBench for judgment ability comparison

**Bai et al., 2022**
- Cited in 05_post-training.md as source of constitutional AI approach for self-rewarding

**Leviathan et al., 2023**
- Cited in 05_post-training.md as source of speculative decoding framework (also cited in 02_architecture.md)

**Xia et al., 2023**
- Cited in 05_post-training.md as source of speculative decoding framework (also cited in 02_architecture.md)

## References from Appendix B

**Xi et al., 2023**
- Cited in 08_appendix-b-low-precision-training.md in discussion of token-correlated outliers in activation gradients that cannot be effectively managed by block-wise quantization
