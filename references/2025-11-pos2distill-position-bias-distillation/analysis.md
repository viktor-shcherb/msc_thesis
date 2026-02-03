# Position Bias Mitigates Position Bias: Mitigate Position Bias Through Inter-Position Knowledge Distillation

**Authors:** Yifei Wang, Feng Xiong, Yong Wang, Linjing Li, Xiangxiang Chu, Daniel Dajun Zeng (Chinese Academy of Sciences, University of Chinese Academy of Sciences, Alibaba Group)
**Date:** November 2025, EMNLP 2025, pages 1495--1512, DOI:10.18653/v1/2025.emnlp-main.78 (arXiv:2508.15709)

---

## Core Research Problem

Large language models exhibit **positional bias (PB)** -- non-uniform sensitivity across different contextual locations -- which significantly impairs long-context comprehension. This manifests as the "lost in the middle" phenomenon (Liu et al., 2024), where models favor information at the beginning and end of the context while neglecting middle positions. PB stems from the interplay of three architectural factors: (1) **long-range decay** from relative positional encodings such as RoPE (Su et al., 2024), which bias attention toward recent tokens; (2) **attention sinks** (Xiao et al., 2024; Gu et al., 2025), where disproportionate attention is allocated to initial tokens regardless of semantic relevance; and (3) **causal masking**, which enforces unidirectional information flow and implicitly encodes positional information.

Prior work has addressed PB through two main strategies. **Mechanistic approaches** modify architectural components -- position encodings (Zhang et al., 2024c; Chen et al., 2024), causal masks (Wang et al., 2025b), attention reweighting (Hsieh et al., 2024; Tan et al., 2025), or hidden state manipulation (Yu et al., 2024) -- but fail to eliminate the substantial performance disparity across positions. **Training approaches** (An et al., 2024; Zhang et al., 2024a,b) synthesize contextual awareness data but incur significant data and computational overhead. The core challenge is: **how to effectively and efficiently mitigate position bias without requiring expensive data synthesis or failing to close the performance gap across positions.**

A further insight motivating this work is that PB manifests differently depending on the task. In retrieval tasks, PB causes **token-shifting**: the model produces erroneous tokens at a few decisive turning positions, derailing the response. In reasoning tasks, PB produces **thought-shifting**: because in-context reasoning involves intertwined retrieval and reasoning sub-processes, PB affects both the retrieval of supporting facts and the reasoning trajectory itself, creating a compound effect.

---

## Problem Solutions

The paper proposes **Pos2Distill**, a position-to-position knowledge distillation framework that transfers knowledge from advantageous positions (where the model performs well) to disadvantaged ones (where PB degrades performance). The conceptual principle is to leverage the inherent performance disparity created by PB as a supervisory signal to counteract PB itself. Two specialized systems are designed:

1. **Pos2Distill-R1 (Retrieval):** Directly calibrates token-shifting by using KL divergence to align the model's probability distributions at trivial positions with those at the advantageous sink position (position 1), combined with a position-aware weighting scheme and an anchoring loss to preserve sink-position performance.
2. **Pos2Distill-R2 (Reasoning):** Reshapes reasoning trajectories by distilling high-quality Chain-of-Thought (CoT) responses from advantageous positions (last two document positions) and training the model to reproduce them when gold documents appear at arbitrary positions.

---

## Approach Details

### Method

**Task definition.** A long-context task is defined by instruction I, a set of n documents D := {d_i}_{i=1}^{n}, and a question Q. The prompt is P := {I | gamma(D) | Q}, where gamma determines document ordering. For retrieval, the gold document d_gold at index i yields prompt P^i and response R* ~ M(P*). For reasoning (two-hop setting), first-hop document d_pre at index i and second-hop d_post at index j yield prompt P^{(i,j)} and CoT response C* ~ M(P*).

**Pos2Distill-R1 for Retrieval.** The framework has two modules:

*Activation of Trivial Positions.* The advantageous position is position 1 (the sink position), where the attention sink region overlaps with d_gold, producing high-quality outputs. Responses R^adv ~ M(P^adv) are sampled from the sink position. K prompts are constructed for distinct trivial positions {P^{n_k}}_{k=1}^{K} with n_i in {2, ..., n}. The activation loss aligns the student's distribution at each trivial position with the teacher's distribution at the sink:

> L^{P^{n_i}}_Act = E[KL(P_Theta(R^adv | P^adv) || P_{hat{Theta}}(R^adv | P^{n_i}))]

The original model parameters Theta serve as the teacher throughout training; hat{Theta} denotes the updated parameters at the current step. This avoids loss of advantage at the sink position during updates.

*Position-Aware Alignment.* Since alignment difficulty varies across trivial positions, a dynamic weight alpha_{ij} for each instance combines inter-position and intra-position components:

> alpha_{ij} = [exp(mean_j L^{P^i_j}_Act) / sum_{i=2}^{n} exp(mean_j L^{P^i_j}_Act)] * [L^{P^i_j}_Act / max_k L^{P^i_k}_Act]

The first factor (inter-position) upweights positions with higher average alignment difficulty; the second factor (intra-position) upweights harder instances within each position bin. The overall activation loss is:

> L_Act = sum_i sum_j alpha_{ij} L^{P^i_j}_Act

*Anchoring of Advantageous Positions.* An anchoring loss prevents attention dilution at the sink position during distillation:

> L_Anc = E[KL(P_Theta(R^adv | P^adv) || P_{hat{Theta}}(R^adv | P^adv))]

*Training Objective:*

> L = L_Act + lambda * L_Anc

where lambda = 1.0 controls anchoring intensity.

**Pos2Distill-R2 for Reasoning.** The advantageous position for reasoning is defined as P^{(n-1, n)} (both gold documents at the last two positions). CoT trajectories C^adv ~ M(P^adv) are sampled. K distinct prompts are constructed for position pairs {(n^pre_k, n^post_k)}_{k=1}^{K} where n^pre_k != n^post_k, sampled from {1, ..., n}. The training loss uses cross-entropy:

> L = -sum_{k=1}^{K} log M(C^adv | P^{(n^pre_k, n^post_k)})

### Key Technical Components

- **Token-shifting and token recovery:** In retrieval, PB concentrates errors at a few decisive tokens. KL divergence at the token level shows spikes at these positions (e.g., 1.4e-01 at token 6 for Mistral+NQ, vs. typical values of 1e-03 to 1e-06). Manual correction of the shifted token enables the model to resume correct generation -- a **token recovery mechanism** that Pos2Distill-R1 exploits via soft KL alignment rather than hard-label supervision.
- **Compound PB in reasoning:** In multi-hop reasoning, PB is associated with absolute position, distance between relevant documents, and their relative order. This creates three failure modes: connected (adjacent hops), disconnected (separated hops), and reversed (logically inverted order). Pos2Distill-R2 addresses all three by training across diverse position pairs.
- **Teacher as frozen reference:** Throughout Pos2Distill-R1 training, the teacher distribution P_Theta(R^adv | P^adv) uses the original (unfrozen) model parameters Theta, not the updating hat{Theta}, preventing degradation of sink-position performance.
- **Optimal K (sampled positions):** Increasing K from 0 to 6 yields 4.6% improvement on NQ; further increases show diminishing returns. Optimal range is K = 4-6.

### Experimental Setup

**Models for Pos2Distill-R1:** Mistral-7B-Instruct-v0.3, Qwen1.5-7B-Chat, Llama-3-8B-Instruct.

**Models for Pos2Distill-R2:** Llama-3.1-8B-Instruct, Qwen2.5-7B-Instruct.

**Retrieval datasets:** NaturalQuestions (NQ), TriviaQA (TQA), WebQA (WebQ), KV Retrieval (140 KV pairs). All use 20 documents per query.

**Reasoning datasets:** HotpotQA, MusiQue, 2WikiMultiHopQA.

**Baselines (retrieval):** Base model, Ms-PoE (Zhang et al., 2024c), vanilla SFT, SeqKD (Kim and Rush, 2016). Additional comparison with Attention Buckets, MoICE, PEAR on Llama2-7B.

**Baselines (reasoning):** CoT, Chain-of-Citation (CoC), SeaLong (Li et al., 2024a), LongFaith-SFT (CoT and CoC variants), LongFaith-DPO (Yang et al., 2025a).

**Training details:** Learning rate 3e-6, batch size 32, 2 epochs. DeepSpeed ZeRO-3 + FlashAttention with bfloat16. Retrieval: 300 samples at K=4 random positions. Reasoning: 500 samples at K=4 random position pairs. Inference via vLLM. NVIDIA H20 GPUs.

**Evaluation metrics:** Sub_EM for retrieval, EM for reasoning.

### Key Results

**Pos2Distill-R1 on retrieval-augmented QA (20 documents):**

| Model + Method | NQ Avg. | KV Avg. | TQA Avg. | WebQ Avg. |
|---|---|---|---|---|
| Mistral-7B base | 64.8 | 74.6 | 82.7 | 68.4 |
| Mistral-7B + Pos2Distill | **71.1** | **94.8** | **83.5** | **68.9** |
| Qwen1.5-7B base | 61.2 | 55.2 | 76.6 | 54.4 |
| Qwen1.5-7B + Pos2Distill | **68.4** | **96.9** | **80.0** | **62.2** |
| Llama-3-8B base | 59.4 | 81.1 | 83.7 | 52.8 |
| Llama-3-8B + Pos2Distill | **67.0** | **97.6** | **84.3** | **56.7** |

- Pos2Distill-R1 achieves near-uniform performance across positions. On WebQ, Llama-3-8B averages 56.7% across all 20 positions, comparable to the 57.9% at the optimal sink position.
- Outperforms SFT, SeqKD, and Ms-PoE consistently across all models and datasets.

**Ablation study (Qwen1.5-7B on NQ):**

| Method | Pos 1 | Pos 5 | Pos 10 | Pos 15 | Pos 20 | Avg. |
|---|---|---|---|---|---|---|
| Base | 73.6 | 57.3 | 56.9 | 57.3 | 60.9 | 61.2 |
| + KL | 61.7 | 64.3 | 65.6 | 66.4 | 67.6 | 65.1 |
| + KL + Align | 64.5 | 66.5 | 67.8 | 67.3 | 67.4 | 66.7 |
| + KL + Align + Anc. | 69.9 | 67.3 | 68.1 | 69.1 | 67.5 | 68.4 |

**Pos2Distill-R2 on multi-hop reasoning (EM, trained on MusiQue):**

| Model + Method | MusiQue Overall | 2WikiMHQA Overall | HotpotQA Overall |
|---|---|---|---|
| Llama-3.1-8B + LongFaith-SFT (best) | 39.9 | 56.6 | 50.9 |
| Llama-3.1-8B + Pos2Distill | **42.8** (+2.9) | **61.8** (+5.2) | **58.3** (+7.4) |
| Qwen2.5-7B + LongFaith-SFT (best) | 43.3 | 51.1 | 53.6 |
| Qwen2.5-7B + Pos2Distill | **46.2** (+2.9) | **63.4** (+3.8) | **58.7** (+5.5) |

**Position gap reduction on MusiQue two-hop (Qwen2.5-7B):**

| Method | Connected Avg. | Disconnected Avg. | Reversed Avg. | GAP |
|---|---|---|---|---|
| Base | 35.5 | 29.4 | 30.7 | 11.6 |
| + LongFaith-SFT | 48.6 | 44.9 | 43.2 | 9.3 |
| + Pos2Distill | **50.3** | **47.4** | **47.2** | **4.8** |

### Data Efficiency

With only 250 training examples, Mistral-7B achieves 70.2% average accuracy on NQ -- a 6.7% improvement over the base model (64.8%) and already surpassing SFT and SeqKD at any data scale. This efficiency stems from the high similarity between response distributions at advantageous and trivial positions, enabling rapid in-domain adaptation.

### Generalization to Longer Contexts

Mistral-7B trained on 20-document contexts and evaluated on 20--50 documents maintains high accuracy with narrowed position gaps:

| Num. Documents | Base Avg. | Base GAP | Pos2Distill Avg. | Pos2Distill GAP |
|---|---|---|---|---|
| 20 | 65.1 | 11.1 | 69.5 | 4.8 |
| 30 | 63.8 | 14.2 | 69.1 | 3.6 |
| 40 | 64.3 | 12.6 | 67.4 | 1.8 |
| 50 | 63.1 | 17.8 | 67.2 | 3.0 |

### Generalization to Larger Models

PB persists at larger scales but Pos2Distill remains effective:

| Model | NQ GAP (base -> Pos2Distill) | WebQ GAP (base -> Pos2Distill) |
|---|---|---|
| Qwen2.5-14B | 8.1 -> 3.4 | 7.2 -> 2.4 |
| Qwen2.5-32B | 7.0 -> 3.8 | 7.2 -> 2.6 |

### Cross-Task Generalization

Both systems generalize to each other's domain (Qwen1.5-7B):

| Task | Base | Pos2Distill-R1 | Pos2Distill-R2 |
|---|---|---|---|
| NQ (retrieval) | 62.5 | **74.3** (+11.8) | 64.1 (+1.6) |
| WebQ (retrieval) | 63.9 | **68.1** (+4.2) | 66.7 (+2.8) |
| MusiQue (reasoning) | 41.8 | 45.1 (+3.3) | **48.9** (+7.1) |
| HotpotQA (reasoning) | 66.7 | 69.2 (+2.5) | **72.3** (+5.6) |

Each system excels in its primary domain, but both provide gains on the other's tasks, suggesting shared underlying dynamics for PB mitigation.

### Limitations

Pos2Distill-R2 could benefit from more granular mechanisms to calibrate PB mitigation -- e.g., adaptive strategies that adjust the distillation process based on the complexity of the reasoning chain or the specific configuration of supporting documents.

---

## Conclusions

1. **Distinct manifestations of position bias:** PB manifests as token-shifting in retrieval (errors concentrated at a few decisive tokens) and thought-shifting in reasoning (compound deviation in both retrieval and reasoning sub-processes). These distinct behaviors necessitate separate mitigation strategies.

2. **Self-corrective distillation paradigm:** The performance disparity created by PB can be exploited as a supervisory signal -- responses from advantageous positions serve as natural teachers for disadvantaged positions, enabling effective mitigation without external data synthesis or architectural modifications.

3. **KL divergence outperforms hard-label supervision for token-shifting:** Soft KL alignment at the token level provides fine-grained corrective signals that hard-label approaches (SFT, SeqKD) cannot match, improving average NQ accuracy from 60.2 (SeqKD) to 65.1 (KL) on Qwen1.5-7B.

4. **High data efficiency:** With only 250 training examples, Pos2Distill-R1 achieves a 6.7% improvement on NQ for Mistral-7B, surpassing SFT and SeqKD baselines at any data scale. The efficiency stems from exploiting in-domain distribution similarity rather than learning from out-of-domain labels.

5. **Strong generalization across context lengths and model scales:** Models trained on 20-document contexts generalize to 50+ documents with narrowed position gaps (17.8% -> 3.0% on 50 docs). PB mitigation remains effective at 14B and 32B parameter scales, confirming the universal applicability of the framework.

6. **Cross-task generalization between retrieval and reasoning:** Pos2Distill-R1 (optimized for retrieval) yields +3.3% on MusiQue reasoning, and Pos2Distill-R2 (optimized for reasoning) yields +1.6% on NQ retrieval, suggesting shared underlying mechanisms for position bias despite distinct surface manifestations.

---

## Core References and Why They Are Referenced

### Position Bias Characterization

- **Liu et al. (2024)** -- *Lost in the Middle: How Language Models Use Long Contexts.* Established the U-shaped positional performance curve that defines the "lost in the middle" problem. Pos2Distill directly addresses and mitigates the performance disparities this paper characterizes.
- **Xiao et al. (2024)** -- *Efficient Streaming Language Models with Attention Sinks.* Identified the attention sink phenomenon whereby disproportionate attention is allocated to initial tokens. Pos2Distill leverages the sink position (position 1) as the advantageous position for retrieval precisely because the attention sink overlaps with d_gold there.
- **Gu et al. (2025)** -- *When Attention Sink Emerges in Language Models: An Empirical View.* Traces the emergence of attention sinks to pre-training dynamics (optimization, data distribution, loss function), providing mechanistic grounding for why the sink position yields high-quality outputs.

### Positional Encoding and Architecture

- **Su et al. (2024)** -- *RoFormer: Enhanced Transformer with Rotary Position Embedding.* RoPE induces the long-range decay effect that is one of the root causes of positional bias. The paper's analysis of RoPE's role in PB is central to understanding why positions closer to the query receive more attention.
- **Press et al. (2021)** -- *ALiBi: Train Short, Test Long.* ALiBi is another relative positional encoding that integrates token distances into attention computation, contributing to recency bias.
- **Haviv et al. (2022)** -- *Transformer Language Models Without Positional Encodings Still Learn Positional Information.* Shows that causal masking alone implicitly encodes positional information, identified as one of the three contributing factors to PB.

### Mechanistic PB Mitigation (Baselines)

- **Zhang et al. (2024c)** -- *Found in the Middle: How Language Models Use Long Contexts Better via Plug-and-Play Positional Encoding (Ms-PoE).* Assigns distinct rescaling factors to each attention head to compress relative distances. Primary mechanistic baseline; Pos2Distill substantially outperforms it across all benchmarks.
- **Hsieh et al. (2024)** -- *Found in the Middle: Calibrating Positional Attention Bias Improves Long Context Utilization.* Proposes attention reweighting to calibrate positional bias. Referenced as a representative mechanistic approach that narrows but does not close the performance gap.
- **Chen et al. (2024)** -- *Fortify the Shortest Stave in Attention (Attention Buckets).* Exploits approximate periodicity in attention waveforms to shift key information away from trough regions. Another mechanistic baseline.
- **Yu et al. (2024)** -- *Mitigate Position Bias in Large Language Models via Scaling a Single Dimension.* Reveals that PB is reflected in positional hidden states and mitigates it by scaling certain dimensions.

### Training-Based PB Mitigation (Baselines)

- **An et al. (2024)** -- *Make Your LLM Fully Utilize the Context (FILM).* Synthesizes long-context QA datasets for fine-grained information awareness. Referenced as representative of the data-intensive training approach that Pos2Distill aims to supersede with higher data efficiency.
- **Yang et al. (2025a)** -- *LongFaith: Enhancing Long-Context Reasoning in LLMs with Faithful Synthetic Data.* Provides LongFaith-SFT and LongFaith-DPO baselines for reasoning. Pos2Distill-R2 outperforms both across all reasoning benchmarks.
- **Li et al. (2024a)** -- *Large Language Models Can Self-Improve in Long-Context Reasoning (SeaLong).* Self-training baseline for reasoning; Pos2Distill-R2 substantially outperforms it (e.g., 42.8 vs. 25.5 on MusiQue for Llama-3.1-8B).

### Knowledge Distillation

- **Kim and Rush (2016)** -- *Sequence-Level Knowledge Distillation (SeqKD).* The sequence-level KD baseline. Pos2Distill's word-level KL approach outperforms SeqKD because soft token-level alignment is more effective for correcting token-shifting than hard-label sequence supervision.
- **Kullback and Leibler (1951)** -- *On Information and Sufficiency.* Foundational reference for the KL divergence loss used in Pos2Distill-R1.

### Reasoning and Chain-of-Thought

- **Wei et al. (2022)** -- *Chain-of-Thought Prompting Elicits Reasoning in Large Language Models.* Foundational CoT paper. Pos2Distill-R2 distills CoT trajectories from advantageous positions, making the quality and structure of CoT central to the reasoning mitigation strategy.
- **Baker et al. (2024b)** -- *Lost in the Middle, and In-Between.* Provides insights on how PB in multi-hop reasoning depends on absolute position, inter-document distance, and relative order -- patterns that Pos2Distill-R2 directly addresses.

### Evaluation Data

- **Kwiatkowski et al. (2019)** -- *Natural Questions.* Primary retrieval evaluation dataset.
- **Joshi et al. (2017)** -- *TriviaQA.* Retrieval evaluation dataset.
- **Yang et al. (2018)** -- *HotpotQA.* Multi-hop reasoning evaluation dataset; used for cross-domain generalization evaluation of Pos2Distill-R2.
- **Trivedi et al. (2022)** -- *MuSiQue.* Multi-hop reasoning dataset; primary training and evaluation dataset for Pos2Distill-R2.
- **Ho et al. (2020)** -- *2WikiMultiHopQA.* Multi-hop reasoning evaluation dataset.

#### Cross-References in Available Papers

- **Lost in the Middle (`2024-02-lost-in-the-middle`):** Liu et al. (2024) is the foundational reference for this paper. The "lost in the middle" phenomenon defines the problem that Pos2Distill addresses. Where Liu et al. characterized the U-shaped performance curve as an empirical observation, this paper provides a training-based mitigation that reduces the performance gap (e.g., from 11.1% to 4.8% on 20-document NQ for Mistral-7B) rather than simply documenting it or proposing reranking heuristics.
- **Attention Sinks (`2024-05-attention-sinks-streaming`):** Xiao et al. (2024) identified the attention sink phenomenon that Pos2Distill directly exploits. Pos2Distill-R1 designates the sink position (position 1) as the advantageous teacher position precisely because the overlap between the attention sink and d_gold produces high-quality outputs there.
- **Found in the Middle (`2024-08-found-in-the-middle`):** Hsieh et al. (2024) proposes attention reweighting to calibrate positional bias. This paper cites it as a representative mechanistic approach and positions Pos2Distill as a training-based alternative that more effectively closes the performance gap.
- **BABILong (`2024-12-babilong-long-context-reasoning`):** Kuratov et al. (2024) is referenced as a long-context reasoning benchmark that highlights the challenges PB poses for reasoning-in-a-haystack tasks, motivating Pos2Distill-R2's focus on reasoning.
