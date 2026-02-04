---
title: "Position Bias Mitigates Position Bias: Mitigate Position Bias Through Inter-Position Knowledge Distillation"
authors: "Wang, Xiong, Wang, Li, Chu, Zeng"
year: 2025
venue: "EMNLP 2025"
paper_type: conference-paper
categories: ["position-bias"]
scope: ["position bias mitigation", "knowledge distillation", "long-context retrieval", "long-context reasoning"]
benchmarks_used: ["natural-questions", "triviaqa", "hotpotqa", "webqa", "musique", "2wikimultihopqa"]
models_introduced: []
models_evaluated: ["mistral-7b", "qwen1.5-7b", "llama-3-8b", "llama-3.1-8b", "qwen2.5-7b", "qwen2.5-14b", "qwen2.5-32b"]
key_claims:
  - id: C1
    claim: "PB manifests as token-shifting in retrieval (errors concentrated at a few decisive tokens) and thought-shifting in reasoning (compound deviation in both retrieval and reasoning sub-processes)"
    evidence: "Section 3, Figure 3, Table 9, Figure 8"
    status: supported
  - id: C2
    claim: "Pos2Distill-R1 achieves near-uniform retrieval performance across all 20 positions, with Llama-3-8B averaging 56.7% on WebQ compared to 57.9% at the optimal sink position"
    evidence: "Table 1, Section 5.2"
    status: supported
  - id: C3
    claim: "KL divergence outperforms hard-label supervision (SeqKD) for correcting token-shifting, improving NQ average from 60.2% (SeqKD) to 65.1% (KL) on Qwen1.5-7B with identical training data"
    evidence: "Table 3, Section 5.2.1"
    status: supported
  - id: C4
    claim: "With only 250 training instances, Pos2Distill-R1 improves Mistral-7B NQ performance by 6.7%, achieving 70.2% accuracy"
    evidence: "Figure 5, Section 5.2.2, Abstract"
    status: supported
  - id: C5
    claim: "Pos2Distill-R1 generalizes from 20-document training to 50-document evaluation with narrowed position gaps (base 17.8% gap reduced to 3.0%)"
    evidence: "Table 2, Section 5.2"
    status: supported
  - id: C6
    claim: "Pos2Distill-R2 surpasses all baselines on multi-hop reasoning, achieving 42.8 EM on MusiQue (+2.9 over best baseline) and 58.3 on HotpotQA (+7.4) for Llama-3.1-8B"
    evidence: "Table 4, Section 5.3"
    status: supported
  - id: C7
    claim: "Both Pos2Distill systems exhibit cross-task generalization: R1 (retrieval-optimized) yields +3.3% on MusiQue reasoning, R2 (reasoning-optimized) yields +1.6% on NQ retrieval"
    evidence: "Table 6, Section 5.4"
    status: supported
  - id: C8
    claim: "PB persists at 14B and 32B model scales but Pos2Distill remains effective, reducing retrieval gaps from 7.0-8.1% to 3.4-3.8% and reasoning gaps from 9.0-10.0% to 4.9-6.7%"
    evidence: "Tables 7, 8, Section 5.4"
    status: supported
cross_references:
  - target: 2024-02-lost-in-the-middle
    type: extends
    detail: "Uses the lost-in-the-middle U-shaped performance curve as motivation and defines advantageous vs. trivial positions based on its positional performance disparity"
  - target: 2024-08-found-in-the-middle
    type: complementary
    detail: "Hsieh et al.'s attention calibration approach is a representative mechanistic baseline; Pos2Distill proposes a training-based alternative achieving larger and more uniform gains"
  - target: 2024-05-attention-sinks-streaming
    type: complementary
    detail: "Leverages the attention sink phenomenon to define the advantageous position (position 1) for retrieval distillation, where attention sink overlaps with the gold document"
  - target: 2024-01-roformer-rope
    type: complementary
    detail: "Identifies RoPE's long-range decay as one of three architectural causes of positional bias that Pos2Distill aims to mitigate"
  - target: 2022-04-alibi-train-short-test-long
    type: complementary
    detail: "ALiBi cited as another relative positional encoding contributing to recency bias via long-range decay"
  - target: 2022-12-chain-of-thought-prompting
    type: complementary
    detail: "Pos2Distill-R2 distills CoT reasoning trajectories from advantageous positions to mitigate thought-shifting in multi-hop reasoning"
  - target: 2025-07-position-bias-transformers
    type: complementary
    detail: "Wu et al. provide a theoretical framework for why positional biases emerge; Pos2Distill offers training-based mitigation for the biases that theory predicts"
open_questions:
  - question: "Can adaptive strategies that adjust the distillation process based on reasoning chain complexity or document configuration further improve Pos2Distill-R2?"
    addressed_by: null
  - question: "Does the self-distillation paradigm generalize to other bias types beyond positional bias (e.g., format bias, length bias in LLM-as-judge settings)?"
    addressed_by: null
  - question: "How does Pos2Distill interact with architectural PB mitigations (e.g., DroPE, bidirectional attention) — are the gains complementary or redundant?"
    addressed_by: null
---
# Position Bias Mitigates Position Bias: Mitigate Position Bias Through Inter-Position Knowledge Distillation

**Authors:** Yifei Wang, Feng Xiong, Yong Wang, Linjing Li, Xiangxiang Chu, Daniel Dajun Zeng (Chinese Academy of Sciences, University of Chinese Academy of Sciences, Alibaba Group)
**Date:** November 2025, EMNLP 2025, pages 1495--1512, DOI:10.18653/v1/2025.emnlp-main.78 (arXiv:2508.15709)

---

## Core Research Problem

Large language models exhibit **positional bias (PB)** -- non-uniform sensitivity across different contextual locations -- which significantly impairs long-context comprehension. This manifests as the "lost in the middle" phenomenon (Liu et al., 2024), where models favor information at the beginning and end of the context while neglecting middle positions. PB stems from the interplay of three architectural factors: (1) **long-range decay** from relative positional encodings such as RoPE (Su et al., 2024) and ALiBi (Press et al., 2021), which bias attention toward recent tokens; (2) **attention sinks** (Xiao et al., 2024; Gu et al., 2025), where disproportionate attention is allocated to initial tokens regardless of semantic relevance; and (3) **causal masking**, which enforces unidirectional information flow and implicitly encodes positional information (Haviv et al., 2022).

Prior work has addressed PB through two strategies. **Mechanistic approaches** modify architectural components -- position encodings (Zhang et al., 2024c; Chen et al., 2024), causal masks (Wang et al., 2025b), attention reweighting (Hsieh et al., 2024; Tan et al., 2025), or hidden state manipulation (Yu et al., 2024) -- but fail to eliminate the substantial performance disparity across positions. **Training approaches** (An et al., 2024; Zhang et al., 2024a,b) synthesize contextual awareness data but incur significant data and computational overhead. The core challenge is: **how to effectively and efficiently mitigate position bias without requiring expensive data synthesis or failing to close the performance gap across positions.**

---

## Problem Solutions

The paper proposes **Pos2Distill**, a position-to-position knowledge distillation framework that transfers knowledge from advantageous positions (where the model performs well due to PB) to disadvantaged positions (where PB degrades performance). The conceptual principle is to leverage the inherent performance disparity created by PB as a supervisory signal to counteract PB itself.

A key observation motivating the two-system design is that PB manifests differently depending on the task:

1. **Token-shifting in retrieval:** PB causes the model to produce erroneous tokens at a few decisive "turning" positions in the response, derailing subsequent generation. Manual correction of the shifted token enables the model to resume correct generation -- a **token recovery mechanism** that Pos2Distill-R1 exploits.
2. **Thought-shifting in reasoning:** In-context reasoning involves intertwined retrieval and reasoning sub-processes. PB affects both the retrieval of supporting facts and the reasoning trajectory itself, creating a compound effect that requires reshaping the entire Chain-of-Thought (CoT) response.
3. **Two specialized systems:** Pos2Distill-R1 for retrieval uses KL divergence to align token-level distributions from trivial positions with those from the advantageous sink position. Pos2Distill-R2 for reasoning distills high-quality CoT trajectories from advantageous positions and trains the model to reproduce them at arbitrary positions.

---

## Approach Details

### Method

**Task definition.** A long-context task is defined by instruction I, a set of n documents D := {d_i}_{i=1}^{n}, and a question Q. The prompt is P := {I | gamma(D) | Q}, where gamma determines document ordering. For retrieval, the gold document d_gold at index i yields prompt P^i. For reasoning (two-hop setting), first-hop document d_pre at index i and second-hop d_post at index j yield prompt P^{(i,j)}.

**Pos2Distill-R1 for Retrieval.** The framework has two core modules: Activation of Trivial Positions and Anchoring of Advantageous Positions.

*Advantageous vs. trivial positions.* The advantageous position is position 1 (the sink position), where the attention sink region overlaps with d_gold, producing high-quality outputs. Positions {2, ..., n} are designated as trivial.

*Activation of trivial positions.* Responses R^adv ~ M(P^adv) are sampled from the sink position. K prompts are constructed for distinct trivial positions {P^{n_k}}_{k=1}^{K} with n_i in {2, ..., n}. The activation loss aligns the student's distribution at each trivial position with the teacher's distribution at the sink:

> L^{P^{n_i}}_Act = E[KL(P_Theta(R^adv | P^adv) || P_{hat{Theta}}(R^adv | P^{n_i}))]

The original model parameters Theta serve as the teacher throughout training; hat{Theta} denotes the updated parameters at the current step. This frozen-teacher design avoids degradation of sink-position performance during updates.

*Position-aware alignment.* Since alignment difficulty varies across trivial positions, a dynamic weight alpha_{ij} for each instance combines inter-position and intra-position components:

> alpha_{ij} = [exp(mean_j L^{P^i_j}_Act) / sum_{i=2}^{n} exp(mean_j L^{P^i_j}_Act)] * [L^{P^i_j}_Act / max_k L^{P^i_k}_Act]

The first factor (inter-position) upweights positions with higher average alignment difficulty; the second factor (intra-position) upweights harder instances within each position bin. The overall activation loss is:

> L_Act = sum_i sum_j alpha_{ij} L^{P^i_j}_Act

*Anchoring of advantageous positions.* An anchoring loss prevents attention dilution at the sink position during distillation:

> L_Anc = E[KL(P_Theta(R^adv | P^adv) || P_{hat{Theta}}(R^adv | P^adv))]

*Training objective:*

> L = L_Act + lambda * L_Anc

where lambda = 1.0 controls anchoring intensity.

**Pos2Distill-R2 for Reasoning.** The advantageous position for reasoning is P^{(n-1, n)} (both gold documents at the last two positions, exploiting recency bias). CoT trajectories C^adv ~ M(P^adv) are sampled. K distinct prompts are constructed for position pairs {(n^pre_k, n^post_k)}_{k=1}^{K} where n^pre_k != n^post_k, sampled from {1, ..., n}. The training loss uses cross-entropy:

> L = -sum_{k=1}^{K} log M(C^adv | P^{(n^pre_k, n^post_k)})

### Key Technical Components

- **Token-shifting and token recovery:** In retrieval, PB concentrates errors at a few decisive tokens. Token-level KL divergence between responses from trivial and advantageous positions shows extreme spikes at these positions (e.g., 1.4e-01 at token 6 for Mistral+NQ, vs. typical values of 1e-03 to 1e-06; Table 9). Manual correction of the shifted token enables the model to resume correct generation. Pos2Distill-R1 exploits this via soft KL alignment rather than hard-label supervision.
- **Compound PB in reasoning:** In multi-hop reasoning, PB is associated with absolute position, distance between relevant documents, and their relative order. This creates three failure modes: connected (adjacent hops), disconnected (separated hops), and reversed (logically inverted order). Pos2Distill-R2 addresses all three by training across diverse position pairs.
- **Perplexity analysis of response distributions:** For retrieval, responses sampled from sink and recent positions, conditioned on trivial-position prompts, have much lower PPL than gold labels from SFT (Figure 9). This high distribution similarity enables rapid adaptation and explains Pos2Distill's data efficiency. For reasoning, PPL increases substantially, confirming that token-shifting is not an appropriate assumption for reasoning scenarios.
- **Optimal K (sampled positions):** Increasing K from 0 to 6 yields 4.6% improvement on NQ for retrieval (Figure 6, left); further increases show diminishing returns. For reasoning on MusiQue, improvement saturates around K = 4-6 (Figure 6, right).

### Experimental Setup

**Models for Pos2Distill-R1:** Mistral-7B-Instruct-v0.3, Qwen1.5-7B-Chat, Llama-3-8B-Instruct.

**Models for Pos2Distill-R2:** Llama-3.1-8B-Instruct, Qwen2.5-7B-Instruct.

**Retrieval datasets:** NaturalQuestions (NQ), TriviaQA (TQA), WebQA (WebQ), KV Retrieval (140 KV pairs, from Liu et al., 2024). All use 20 documents per query.

**Reasoning datasets:** HotpotQA, MusiQue, 2WikiMultiHopQA.

**Baselines for retrieval:** Base model, Ms-PoE (Zhang et al., 2024c), vanilla SFT, SeqKD (Kim and Rush, 2016). Additional comparison with Attention Buckets (Chen et al., 2024), MoICE (Lin et al., 2024), PEAR (Tan et al., 2025) on Llama-2-7B-chat-4k (Table 10).

**Baselines for reasoning:** CoT, Chain-of-Citation (CoC; Li et al., 2024b), SeaLong (Li et al., 2024a), LongFaith-SFT (CoT and CoC variants), LongFaith-DPO (Yang et al., 2025a).

**Training details:** Learning rate 3e-6, batch size 32, 2 epochs. DeepSpeed ZeRO-3 + FlashAttention with bfloat16. Retrieval: 300 samples at K=4 random positions. Reasoning: 500 samples at K=4 random position pairs. Inference via vLLM. NVIDIA H20 GPUs.

**Evaluation metrics:** Sub_EM for retrieval, EM for reasoning.

### Key Results

**Pos2Distill-R1 on retrieval-augmented QA (20 documents, Table 1):**

| Model + Method | NQ Avg. | KV Avg. | TQA Avg. | WebQ Avg. |
|---|---|---|---|---|
| Mistral-7B base | 64.8 | 74.6 | 82.7 | 68.4 |
| Mistral-7B + Ms-PoE | 60.9 | 89.3 | 80.0 | 65.2 |
| Mistral-7B + SFT | 65.7 | 87.1 | 77.3 | 52.1 |
| Mistral-7B + SeqKD | 59.9 | 91.8 | 77.0 | 57.0 |
| Mistral-7B + Pos2Distill | **71.1** | **94.8** | **83.5** | **68.9** |
| Qwen1.5-7B base | 61.2 | 55.2 | 76.6 | 54.4 |
| Qwen1.5-7B + Pos2Distill | **68.4** | **96.9** | **80.0** | **62.2** |
| Llama-3-8B base | 59.4 | 81.1 | 83.7 | 52.8 |
| Llama-3-8B + Pos2Distill | **67.0** | **97.6** | **84.3** | **56.7** |

- Pos2Distill-R1 achieves near-uniform performance across positions. On WebQ, Llama-3-8B averages 56.7% across all 20 positions, comparable to the 57.9% at the optimal sink position (Section 5.2).
- SFT and SeqKD improve uniformity but sacrifice sink-position performance and often degrade average accuracy on WebQ (SFT drops Mistral-7B from 68.4% to 52.1%).

**Ablation study (Qwen1.5-7B on NQ, Table 3):**

| Method | Pos 1 | Pos 5 | Pos 10 | Pos 15 | Pos 20 | Avg. |
|---|---|---|---|---|---|---|
| Base | 73.6 | 57.3 | 56.9 | 57.3 | 60.9 | 61.2 |
| SeqKD | 61.7 | 58.7 | 58.9 | 59.9 | 61.9 | 60.2 |
| KL | 61.7 | 64.3 | 65.6 | 66.4 | 67.6 | 65.1 |
| KL + Align | 64.5 | 66.5 | 67.8 | 67.3 | 67.4 | 66.7 |
| KL + Align + Anc. | 69.9 | 67.3 | 68.1 | 69.1 | 67.5 | 68.4 |

- KL divergence substantially outperforms hard-label SeqKD (65.1 vs. 60.2), confirming soft alignment is better suited for token-shifting correction.
- Position-aware alignment adds +1.6 average (66.7 vs. 65.1) by prioritizing harder positions.
- Anchoring adds +1.7 average (68.4 vs. 66.7) and critically recovers sink-position performance from 64.5 to 69.9.

**Comparison with mechanistic baselines (Llama-2-7B-chat-4k, Table 10):**

| Method | Avg. | GAP |
|---|---|---|
| Base | 65.05 | 4.86 |
| Ms-PoE | 64.34 | 3.84 |
| Attention Buckets | 65.18 | 3.16 |
| MoICE | 65.48 | 2.22 |
| PEAR | 66.81 | 6.86 |
| Pos2Distill-R1 | **68.18** | **1.79** |

- Pos2Distill-R1 achieves the highest average accuracy (68.18) and lowest position gap (1.79), outperforming all mechanistic approaches.

**Pos2Distill-R2 on multi-hop reasoning (EM, trained on MusiQue, Table 4):**

| Model + Method | MusiQue Overall | 2WikiMHQA Overall | HotpotQA Overall |
|---|---|---|---|
| Llama-3.1-8B + CoT | 11.8 | 27.4 | 19.4 |
| Llama-3.1-8B + SeaLong | 25.5 | 52.6 | 49.6 |
| Llama-3.1-8B + LongFaith-SFT (best) | 39.9 | 56.6 | 50.9 |
| Llama-3.1-8B + Pos2Distill | **42.8** (+2.9) | **61.8** (+5.2) | **58.3** (+7.4) |
| Qwen2.5-7B + LongFaith-SFT (best) | 43.3 | 51.1 | 53.6 |
| Qwen2.5-7B + LongFaith-DPO | 38.4 | 59.6 | 56.5 |
| Qwen2.5-7B + Pos2Distill | **46.2** (+2.9) | **63.4** (+3.8) | **58.7** (+5.5) |

- Pos2Distill-R2 surpasses all self-training baselines in both in-domain (MusiQue) and out-of-domain (2WikiMHQA, HotpotQA) evaluation, suggesting that training across diverse position pairs is more effective than conventional instance-by-instance self-training.

**Position gap reduction on MusiQue two-hop (Qwen2.5-7B, Table 5):**

| Method | Connected Avg. | Disconnected Avg. | Reversed Avg. | GAP |
|---|---|---|---|---|
| Base | 35.5 | 29.4 | 30.7 | 11.6 |
| LongFaith-SFT | 48.6 | 44.9 | 43.2 | 9.3 |
| LongFaith-DPO | 36.5 | 33.0 | 36.5 | 10.1 |
| Pos2Distill | **50.3** | **47.4** | **47.2** | **4.8** |

- Pos2Distill reduces the cross-mode position gap from 11.6% to 4.8%, while conventional self-training methods struggle to reduce it (LongFaith-DPO even slightly increases the gap for Llama-3.1-8B from 4.4 to 6.5; Table 5).

### Data Efficiency

With only 250 training instances, Mistral-7B achieves 70.2% average accuracy on NQ -- an improvement of 6.7% over the base model (Figure 5, Abstract). This already surpasses SFT and SeqKD at any data scale. The efficiency stems from the high distribution similarity between responses at advantageous and trivial positions (low PPL gap; Figure 9), enabling rapid in-domain adaptation without relying on out-of-domain labels.

### Generalization to Longer Contexts

Mistral-7B trained on 20-document contexts and evaluated on 20--50 documents maintains high accuracy with narrowed position gaps (Table 2):

| Num. Documents | Base Avg. | Base GAP | Pos2Distill Avg. | Pos2Distill GAP |
|---|---|---|---|---|
| 20 | 65.1 | 11.1 | 69.5 | 4.8 |
| 30 | 63.8 | 14.2 | 69.1 | 3.6 |
| 40 | 64.3 | 12.6 | 67.4 | 1.8 |
| 50 | 63.1 | 17.8 | 67.2 | 3.0 |

Extended evaluation on 50-document training shows further improvements, with models trained on 50 docs maintaining 70% accuracy on 80 docs (Table 13).

### Generalization to Larger Models

PB persists at larger scales but Pos2Distill remains effective (Tables 7, 8; 30 documents):

| Model | NQ GAP (base -> Pos2Distill) | WebQ GAP (base -> Pos2Distill) |
|---|---|---|
| Qwen2.5-14B | 8.1 -> 3.4 | 7.2 -> 2.4 |
| Qwen2.5-32B | 7.0 -> 3.8 | 7.2 -> 2.6 |

| Model | MusiQue Reasoning GAP (base -> Pos2Distill) |
|---|---|
| Qwen2.5-14B | 10.0 -> 6.7 |
| Qwen2.5-32B | 9.0 -> 4.9 |

### Cross-Task Generalization

Both systems generalize to each other's domain (Qwen1.5-7B, Table 6):

| Task | Base | Pos2Distill-R1 | Pos2Distill-R2 |
|---|---|---|---|
| NQ (retrieval) | 62.5 | **74.3** (+11.8) | 64.1 (+1.6) |
| WebQ (retrieval) | 63.9 | **68.1** (+4.2) | 66.7 (+2.8) |
| MusiQue (reasoning) | 41.8 | 45.1 (+3.3) | **48.9** (+7.1) |
| HotpotQA (reasoning) | 66.7 | 69.2 (+2.5) | **72.3** (+5.6) |

Each system excels in its primary domain, but both provide gains on the other's tasks. This suggests shared underlying dynamics for PB mitigation, potentially influenced by whether CoT reasoning is involved. The development of two specialized systems is therefore both necessary and effective.

### Mechanistic Insights

Attention distribution analysis (Figure 7) shows that after Pos2Distill-R1 training, the model dynamically shifts its attention focus to consistently align with the relevant document as d_gold moves from position 1 to 20. The base model's attention remains anchored to the sink and recent positions regardless of where d_gold is placed.

---

## Limitations and Failure Modes

- **Pos2Distill-R2 lacks granularity.** The authors acknowledge that Pos2Distill-R2 could benefit from more granular mechanisms to calibrate PB mitigation, such as adaptive strategies that adjust based on the complexity of the reasoning chain or the specific configuration of supporting documents (Limitations section).
- **Fixed advantageous positions.** The advantageous position is defined as position 1 for retrieval (sink) and positions (n-1, n) for reasoning (recent). These definitions assume standard PB patterns and may not hold for models with atypical attention distributions.
- **Retrieval-specific evaluation.** Retrieval experiments use a fixed 20-document setup with single gold documents. Performance on tasks with multiple relevant documents distributed across positions is not evaluated.
- **Reasoning limited to two-hop.** Pos2Distill-R2 focuses on two-hop reasoning for formulation brevity. Generalization to more complex multi-hop chains (3-hop, 4-hop) is evaluated at test time (Table 4) but not explicitly targeted during training.
- **SFT degradation on some tasks.** Standard SFT and SeqKD baselines degrade WebQ performance for Mistral-7B (from 68.4% to 52.1% and 57.0% respectively; Table 1), indicating that naive training approaches can harm retrieval quality on some datasets. Pos2Distill avoids this degradation.

---

## Conclusions

### Contributions

1. **Distinct manifestations of position bias.** Established that PB manifests as token-shifting in retrieval (errors concentrated at a few decisive tokens) and thought-shifting in reasoning (compound deviation in both retrieval and reasoning sub-processes). These distinct behaviors necessitate separate mitigation strategies (Section 3, Figure 3).

2. **Self-corrective distillation paradigm.** Proposed Pos2Distill, a framework that exploits the performance disparity created by PB as a supervisory signal -- responses from advantageous positions serve as natural teachers for disadvantaged positions, enabling effective mitigation without external data synthesis or architectural modifications (Section 4).

3. **KL divergence over hard-label supervision for token-shifting.** Demonstrated that soft KL alignment at the token level provides fine-grained corrective signals that hard-label approaches (SFT, SeqKD) cannot match, improving average NQ accuracy from 60.2% (SeqKD) to 65.1% (KL) on Qwen1.5-7B (Table 3).

4. **High data efficiency.** With only 250 training instances, Pos2Distill-R1 achieves a 6.7% improvement on NQ for Mistral-7B, surpassing SFT and SeqKD at any data scale. The efficiency stems from exploiting in-domain distribution similarity rather than learning from markedly different distributions (Figure 5, Section 5.2.2).

5. **Generalization across context lengths and model scales.** Models trained on 20-document contexts generalize to 50+ documents with narrowed position gaps (17.8% -> 3.0% on 50 docs; Table 2). PB mitigation remains effective at 14B and 32B scales, reducing gaps from 7-10% to 2.4-4.9% (Tables 7, 8).

6. **Cross-task generalization.** Pos2Distill-R1 (retrieval-optimized) yields +3.3% on MusiQue reasoning, and Pos2Distill-R2 (reasoning-optimized) yields +1.6% on NQ retrieval, suggesting shared underlying mechanisms for position bias despite distinct surface manifestations (Table 6).

### Implications

1. **PB as a resource rather than an obstacle.** The paper reframes positional bias from a pure liability to a dual-natured phenomenon -- the same disparity that degrades performance also provides the supervisory signal for its own mitigation. [Inference: this conceptual shift may apply to other forms of model bias.]

2. **Superiority of self-distillation over external supervision.** The high data efficiency and strong performance suggest that self-distillation from within-model distributional differences may be a generally powerful paradigm for addressing systematic biases, beyond just positional bias. [Speculative: not tested beyond positional bias in this paper.]

3. **Limitations of mechanistic approaches.** The consistent superiority of Pos2Distill over mechanistic baselines (Ms-PoE, Attention Buckets, MoICE, PEAR) suggests that inference-time interventions are insufficient -- PB mitigation requires updating model parameters. [Inference: this conclusion is supported by the data but limited to the models and tasks tested.]

---

## Key Claims

1. **Token-shifting in retrieval.** PB causes errors at a few decisive tokens in retrieval responses. Token-level KL divergence between responses from trivial and advantageous positions shows extreme spikes (e.g., 1.4e-01 at token 6 for Mistral+NQ vs. typical 1e-03 to 1e-06; Table 9). Manual correction of the shifted token enables the model to resume correct generation (Section 3, Appendix B). Status: **supported**.

2. **Near-uniform retrieval performance.** Pos2Distill-R1 achieves near-uniform performance across all 20 positions: Llama-3-8B averages 56.7% on WebQ across all positions vs. 57.9% at the optimal sink position (Table 1, Section 5.2). Status: **supported**.

3. **KL outperforms hard-label supervision.** On identical training data, KL divergence achieves 65.1% average NQ accuracy for Qwen1.5-7B vs. 60.2% for SeqKD (Table 3, Section 5.2.1). Status: **supported**.

4. **Data efficiency.** With 250 training instances, Pos2Distill-R1 achieves 70.2% accuracy on NQ for Mistral-7B, improving over the base model by 6.7% and surpassing SFT and SeqKD at any data scale (Figure 5, Section 5.2.2, Abstract). Status: **supported**.

5. **Context length generalization.** Mistral-7B trained on 20-document contexts maintains high accuracy and narrowed position gaps when evaluated on 50 documents (base gap 17.8% reduced to 3.0%; Table 2). Status: **supported**.

6. **Reasoning improvement.** Pos2Distill-R2 achieves 42.8 EM on MusiQue and 58.3 on HotpotQA for Llama-3.1-8B, surpassing the strongest baseline (LongFaith-SFT) by 2.9 and 7.4 points respectively (Table 4, Section 5.3). Status: **supported**.

7. **Cross-task generalization.** Pos2Distill-R1 yields +3.3% on MusiQue reasoning and Pos2Distill-R2 yields +1.6% on NQ retrieval (Table 6, Section 5.4). Status: **supported**.

8. **Scale generalization.** PB persists at 14B and 32B model scales; Pos2Distill reduces retrieval gaps from 7.0-8.1% to 3.4-3.8% and reasoning gaps from 9.0-10.0% to 4.9-6.7% (Tables 7, 8). Status: **supported**.

---

## Open Questions

1. **Adaptive distillation for complex reasoning.** Can strategies that adjust the distillation process based on reasoning chain complexity or document configuration further improve Pos2Distill-R2? The authors explicitly identify this as a limitation (Limitations section). Not yet addressed.

2. **Generalization beyond positional bias.** Does the self-distillation paradigm generalize to other bias types (e.g., format bias, length bias in LLM-as-judge settings, or distractor sensitivity)? The paper only tests positional bias. Not yet addressed.

3. **Complementarity with architectural approaches.** How does Pos2Distill interact with architectural PB mitigations such as DroPE (position-embedding dropping) or bidirectional attention modifications? Are the gains complementary or redundant? Not yet addressed.

4. **Scaling to very long contexts.** The paper evaluates up to 80 documents (~14K tokens) in supplementary experiments. How does Pos2Distill perform at 32K, 64K, or 128K token contexts? Not yet addressed.

---

## Core References and Why They Are Referenced

### Position Bias Characterization

- **Liu et al. (2024)** -- *Lost in the Middle: How Language Models Use Long Contexts.* Established the U-shaped positional performance curve that defines the "lost in the middle" problem. Pos2Distill directly addresses and mitigates the performance disparities this paper characterizes, using the U-shaped curve to define advantageous and trivial positions.

- **Xiao et al. (2024)** -- *Efficient Streaming Language Models with Attention Sinks.* Identified the attention sink phenomenon. Pos2Distill leverages the sink position (position 1) as the advantageous position for retrieval precisely because the attention sink overlaps with d_gold, producing high-quality outputs there.

- **Gu et al. (2025)** -- *When Attention Sink Emerges in Language Models: An Empirical View.* Traces the emergence of attention sinks to pre-training dynamics (optimization, data distribution, loss function), providing mechanistic grounding for why the sink position yields high-quality outputs.

### Positional Encoding and Architecture

- **Su et al. (2024)** -- *RoFormer: Enhanced Transformer with Rotary Position Embedding.* RoPE induces the long-range decay effect that is one of the root causes of positional bias. The paper's analysis of RoPE's contribution to PB is central to understanding why positions closer to the query receive more attention.

- **Press et al. (2021)** -- *ALiBi: Train Short, Test Long.* ALiBi is another relative positional encoding integrating token distances into attention computation, contributing to recency bias.

- **Haviv et al. (2022)** -- *Transformer Language Models Without Positional Encodings Still Learn Positional Information.* Shows that causal masking alone implicitly encodes positional information, identified as one of the three contributing factors to PB.

### Mechanistic PB Mitigation (Baselines)

- **Zhang et al. (2024c)** -- *Found in the Middle: How Language Models Use Long Contexts Better via Plug-and-Play Positional Encoding (Ms-PoE).* Assigns distinct rescaling factors to each attention head to compress relative distances. Primary mechanistic baseline; Pos2Distill substantially outperforms it across all benchmarks (Table 1, Table 10).

- **Hsieh et al. (2024)** -- *Found in the Middle: Calibrating Positional Attention Bias Improves Long Context Utilization.* Proposes attention reweighting to calibrate positional bias. Representative mechanistic approach that narrows but does not close the performance gap.

- **Chen et al. (2024)** -- *Fortify the Shortest Stave in Attention (Attention Buckets).* Exploits approximate periodicity in attention waveforms at distal positions to shift key information away from trough regions. Mechanistic baseline in Table 10.

- **Yu et al. (2024)** -- *Mitigate Position Bias in Large Language Models via Scaling a Single Dimension.* Reveals that PB is reflected in positional hidden states and mitigates it by scaling certain dimensions.

### Training-Based PB Mitigation (Baselines)

- **An et al. (2024)** -- *Make Your LLM Fully Utilize the Context (FILM).* Synthesizes long-context QA datasets for fine-grained information awareness. Referenced as representative of the data-intensive training approach that Pos2Distill supersedes with higher data efficiency.

- **Yang et al. (2025a)** -- *LongFaith: Enhancing Long-Context Reasoning in LLMs with Faithful Synthetic Data.* Provides LongFaith-SFT and LongFaith-DPO baselines for reasoning. Pos2Distill-R2 outperforms both across all reasoning benchmarks (Table 4).

- **Li et al. (2024a)** -- *Large Language Models Can Self-Improve in Long-Context Reasoning (SeaLong).* Self-training baseline for reasoning; Pos2Distill-R2 substantially outperforms it (e.g., 42.8 vs. 25.5 on MusiQue for Llama-3.1-8B; Table 4).

### Knowledge Distillation

- **Kim and Rush (2016)** -- *Sequence-Level Knowledge Distillation (SeqKD).* The sequence-level KD baseline. Pos2Distill's word-level KL approach outperforms SeqKD because soft token-level alignment is more effective for correcting token-shifting than hard-label sequence supervision (Table 3).

### Reasoning and Chain-of-Thought

- **Wei et al. (2022)** -- *Chain-of-Thought Prompting Elicits Reasoning in Large Language Models.* Foundational CoT paper. Pos2Distill-R2 distills CoT trajectories from advantageous positions, making the quality and structure of CoT central to the reasoning mitigation strategy.

- **Baker et al. (2024b)** -- *Lost in the Middle, and In-Between.* Provides insights on how PB in multi-hop reasoning depends on absolute position, inter-document distance, and relative order -- patterns that Pos2Distill-R2 directly addresses via diverse position-pair sampling.

### Evaluation Data

- **Kwiatkowski et al. (2019)** -- *Natural Questions.* Primary retrieval evaluation dataset.
- **Joshi et al. (2017)** -- *TriviaQA.* Retrieval evaluation dataset.
- **Berant et al. (2013)** -- *WebQA.* Retrieval evaluation dataset.
- **Yang et al. (2018)** -- *HotpotQA.* Multi-hop reasoning evaluation dataset.
- **Trivedi et al. (2022)** -- *MuSiQue.* Primary training and evaluation dataset for Pos2Distill-R2.
- **Ho et al. (2020)** -- *2WikiMultiHopQA.* Multi-hop reasoning evaluation dataset.
