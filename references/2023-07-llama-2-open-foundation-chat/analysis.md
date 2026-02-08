---
title: "Llama 2: Open Foundation and Fine-Tuned Chat Models"
authors: "Touvron, Martin, Stone, Albert, Almahairi, Babaei, Bashlykov, Batra, Bhargava, Bhosale, et al."
year: 2023
venue: "arXiv preprint 2307.09288"
paper_type: preprint
categories: ["model-release", "architecture"]
scope: ["open foundation models", "RLHF alignment", "grouped-query attention", "context length extension"]
benchmarks_used: ["mmlu", "arc", "hellaswag", "winogrande", "boolq", "piqa", "siqa", "openbookqa", "csqa", "humaneval", "mbpp", "gsm8k", "math-hendrycks", "triviaqa", "natural-questions", "squad", "bbh", "agi-eval", "truthfulqa", "toxigen", "bold", "asdiv", "svamp", "mawps"]
models_introduced: ["llama-2-7b", "llama-2-13b", "llama-2-70b"]
models_evaluated: ["llama-7b", "llama-13b", "llama-33b", "llama-65b", "falcon-7b", "mpt-7b", "gpt-4", "gpt-3.5-turbo", "palm-540b"]
key_claims:
  - id: C1
    claim: "Llama 2 70B outperforms all open-source models at time of release, exceeding LLaMA 65B by +5.5 on MMLU (68.9 vs 63.4) and +7.7 on BBH (51.2 vs 43.5)"
    evidence: "Table 3, Section 2.3"
    status: supported
    scope: "7B-70B scale, standard English academic benchmarks, 0-shot to 8-shot evaluation"
    magnitude: "MMLU 68.9 vs 63.4 (+5.5); BBH 51.2 vs 43.5 (+7.7); GSM8K 56.8 vs 50.9 (+5.9) over LLaMA 65B"
  - id: C2
    claim: "Doubling context length from 2048 to 4096 tokens yields large gains on long-context tasks with no degradation on standard benchmarks"
    evidence: "Table 16, Table 17, Appendix A.2.1"
    status: supported
    scope: "30B model scale, 150B training tokens, SCROLLS long-context tasks with ~3.5K average input length"
    magnitude: "NarrativeQA F1: 0.21 to 17.26; Qasper F1: 0.71 to 18.52; QuALITY acc: 26.1 to 29.6; HellaSwag change -0.3 (within noise)"
  - id: C3
    claim: "GQA with 8 KV heads achieves comparable quality to full MHA while enabling significantly higher inference throughput"
    evidence: "Table 18, Figure 24, Appendix A.2.1"
    status: supported
    scope: "30B model scale, 150B training tokens, 8xA100 80GB tensor parallelism, batch sizes up to 1024"
    magnitude: "GQA averages comparable to MHA across 11 benchmarks; MHA triggers OOM at batch size 1024 for 256-token context where GQA succeeds"
  - id: C4
    claim: "Llama 2-Chat 70B achieves 36% win rate against ChatGPT (gpt-3.5-turbo-0301) on human evaluations of helpfulness"
    evidence: "Figure 1, Figure 12, Section 3.4.2"
    status: supported
    scope: "~4,000 single and multi-turn prompts, 3 raters per prompt, 7-point Likert scale, English only, no coding/reasoning prompts"
    magnitude: "Win 35.9%, Tie 31.5%, Loss 32.5%; without system prompt for ChatGPT, win rate increases to 44%"
  - id: C5
    claim: "Safety fine-tuning reduces toxic generations to effectively 0% on ToxiGen across all model sizes without degrading helpfulness"
    evidence: "Table 14, Table 45, Figure 14, Section 4.2.3"
    status: supported
    scope: "7B-70B Llama 2-Chat, ToxiGen benchmark with 13 demographic groups, ~0.9M helpfulness + ~0.1M safety training samples"
    magnitude: "ToxiGen toxicity: 24.60% (pretrained 70B) to 0.01% (Chat 70B); helpfulness RM score distribution preserved (Figure 14 right)"
  - id: C6
    claim: "Ghost Attention maintains system prompt adherence at 100% accuracy for 20+ turns, compared to 0% at turn 6 without GAtt"
    evidence: "Table 30, Section 3.3, Appendix A.3.5"
    status: supported
    scope: "Llama 2-Chat, public figure and hobby constraints, total dialogue <4048 tokens, applied after RLHF-V3"
    magnitude: "100% attribute retention through 20+ turns (GAtt) vs 0% at turn 6 (baseline); generalizes to unseen constraint types"
  - id: C7
    claim: "Llama 2 70B approaches GPT-3.5 on MMLU and GSM8K but lags significantly on code generation"
    evidence: "Table 4, Section 2.3"
    status: supported
    scope: "70B model only, comparison to GPT-3.5/GPT-4/PaLM/PaLM-2-L on 6 benchmarks"
    magnitude: "MMLU: 68.9 vs 70.0 (-1.1); GSM8K: 56.8 vs 57.1 (-0.3); HumanEval: 29.9 vs 48.1 (-18.2)"
  - id: C8
    claim: "27,540 high-quality SFT annotations outperform millions of third-party examples for instruction tuning"
    evidence: "Section 3.1"
    status: supported
    scope: "Llama 2-Chat SFT stage, Meta vendor annotations vs third-party datasets"
    magnitude: "qualitative"
  - id: C9
    claim: "Llama 2-Chat demonstrates zero-shot tool use capability despite never being trained with tools, dramatically outperforming Toolformer on math datasets"
    evidence: "Table 15, Figure 23, Section 5.1"
    status: supported
    scope: "Calculator tool on ASDiv, SVAMP, MAWPS math datasets, zero-shot"
    magnitude: "ASDiv 67.1 vs 40.4 (Toolformer); SVAMP 69.2 vs 29.4; MAWPS 82.4 vs 44.0"
  - id: C10
    claim: "Only HellaSwag and MMLU-Humanities show evidence of contamination boost in Llama 2, with 70B benefiting more than 7B"
    evidence: "Table 51, Appendix A.6"
    status: supported
    scope: "Llama 2 7B and 70B pretrained models, tokenized contamination detection with skipgram budget"
    magnitude: "HellaSwag (L=40): 70B clean 80.0 vs dirty 92.2 (Z_n=7.42); 7B clean 70.5 vs dirty 83.7 (Z_n=6.84)"
cross_references:
  - target: 2023-02-llama-open-efficient-foundation
    type: extends
    detail: "Direct successor to LLaMA with doubled context length (4096 tokens), 40% more training data (2T tokens), and GQA for 70B model"
  - target: 2023-12-gqa-grouped-query-attention
    type: extends
    detail: "Llama 2 70B adopts GQA with 8 KV heads serving 64 query heads, reducing KV cache by 8x while matching MHA quality"
  - target: 2017-12-attention-is-all-you-need
    type: extends
    detail: "Retains decoder-only Transformer with modifications (RMSNorm, SwiGLU, RoPE) inherited from LLaMA"
  - target: 2024-01-roformer-rope
    type: extends
    detail: "Uses RoPE positional encoding with base frequency b=10000, extended from 2048 to 4096 context length"
  - target: 2024-05-yarn-context-extension
    type: extended-by
    detail: "YaRN extends Llama 2's context window from 4K to 64K/128K tokens"
  - target: 2023-06-pi-positional-interpolation
    type: extended-by
    detail: "Position Interpolation extends Llama 2's RoPE context window through frequency rescaling"
  - target: 2024-06-effective-long-context-scaling
    type: extended-by
    detail: "Llama 2 Long extends Llama 2 to 32K context via continual pretraining with RoPE base frequency adjustment (b=500K), trained with 400B additional tokens"
  - target: 2024-05-attention-sinks-streaming
    type: extended-by
    detail: "StreamingLLM identifies attention sinks in Llama 2 enabling infinite-length streaming inference"
  - target: 2025-12-drope-dropping-positional-embeddings
    type: extended-by
    detail: "DroPE evaluates context extension on Llama 2 7B by dropping positional embeddings"
  - target: 2025-07-position-bias-transformers
    type: extended-by
    detail: "Position bias analysis conducted on Llama 2 models"
  - target: 2025-04-effective-context-length-falls-short
    type: extended-by
    detail: "Evaluates effective context length of Llama 2 models"
  - target: 2024-02-lost-in-the-middle
    type: extended-by
    detail: "Lost in the Middle evaluates positional bias in Llama 2 on multi-document QA"
  - target: 2025-04-retrieval-head-long-context-factuality
    type: extended-by
    detail: "Wu et al. use Llama-2-7B and Llama-2-13B (including 80K and 64K context-extended variants) to discover retrieval heads and show they are intrinsic to the base model"
  - target: 2023-10-mistral-7b
    type: extended-by
    detail: "Mistral 7B outperforms Llama 2 13B on all benchmarks at 7B parameters using sliding window attention and GQA"
  - target: 2024-07-llama-3-herd-of-models
    type: extended-by
    detail: "Llama 3 extends Llama 2 with 8x more training data (15.6T vs 2T tokens), 128K context (vs 4K), and 405B flagship model"
  - target: 2024-03-gemma-open-models
    type: extended-by
    detail: "Gemma 7B outperforms Llama 2 13B on MMLU (64.3 vs 54.8) and most benchmarks despite having fewer parameters"
open_questions:
  - question: "Would training beyond 2T tokens continue to improve performance, given that training loss showed no saturation?"
    addressed_by: null
  - question: "Can the safety-helpfulness tradeoff be resolved without over-cautious refusals on benign prompts containing sensitive keywords?"
    addressed_by: null
  - question: "How does Llama 2's context length (4096 tokens) compare to longer-context models on tasks requiring >4K context?"
    addressed_by: 2024-05-yarn-context-extension
  - question: "Does the contamination boost observed for HellaSwag and MMLU-Humanities generalize to other benchmarks at larger training scales?"
    addressed_by: null
  - question: "How does safety fine-tuning generalize to non-English languages where adversarial prompts are known attack vectors?"
    addressed_by: null
---

# Llama 2: Open Foundation and Fine-Tuned Chat Models

**Authors:** Hugo Touvron, Louis Martin, Kevin Stone, Peter Albert, Amjad Almahairi, Yasmine Babaei, Nikolay Bashlykov, ..., Thomas Scialom (GenAI, Meta)
**Date:** July 2023, arXiv:2307.09288

---

## Core Research Problem

Despite growing interest in open-weight language models following LLaMA (Touvron et al., 2023a), no open-weight model family combined competitive base model performance with a fully documented alignment pipeline (SFT + RLHF) and a permissive commercial license. Existing open models were either base-only without alignment (LLaMA, OPT, Falcon), closed-weight with alignment (GPT-4, PaLM 2, Claude), or aligned via distillation from proprietary models without documented methodology (Vicuna, Alpaca). Furthermore, LLaMA's 2048-token context window was a practical limitation for many applications, and its release license restricted commercial use. The core challenge was: **how to produce an open-weight model family with extended context length, documented alignment methodology, safety evaluations, and a commercial license, while matching or exceeding existing open-source models and approaching closed-source chat assistants.**

---

## Problem Solutions

Llama 2 addresses the problem through three contributions:

1. **Stronger pretrained base models.** Train 7B, 13B, 34B, and 70B parameter models on 2T tokens (40% more data than LLaMA) with an extended 4096-token context window. Adopt Grouped-Query Attention (GQA) for the 34B and 70B models to improve inference efficiency.

2. **Documented alignment pipeline (Llama 2-Chat).** Apply supervised fine-tuning (SFT) followed by iterative Reinforcement Learning from Human Feedback (RLHF) using both Rejection Sampling and Proximal Policy Optimization (PPO). Introduce Ghost Attention (GAtt) for multi-turn system prompt adherence.

3. **Open release with comprehensive safety evaluation.** Release model weights under a permissive commercial license, accompanied by detailed safety evaluations, red teaming with 350+ participants, and responsibility analysis.

---

## Approach Details

### Method

Llama 2 uses the same base architecture as LLaMA with two key changes:

1. **Extended context length:** 4096 tokens (doubled from LLaMA's 2048). RoPE positional encoding (Su et al., 2022) with base frequency b = 10000 is retained. Ablation experiments (Table 16, Appendix A.2.1) on models trained for 150B tokens show large gains on long-context tasks with no degradation on standard benchmarks (Table 17).

2. **Grouped-Query Attention (GQA):** The 34B and 70B models use GQA (Ainslie et al., 2023). The 70B model uses 8 key-value heads shared across 64 query heads. The 7B and 13B models retain standard multi-head attention.

All other architectural choices from LLaMA are retained: pre-normalization with RMSNorm (Zhang & Sennrich, 2019), SwiGLU activations (Shazeer, 2020), no bias terms, and the same SentencePiece BPE tokenizer with a 32,000-token vocabulary. All numbers are split into individual digits; unknown UTF-8 characters decomposed into bytes.

The alignment pipeline consists of four stages applied sequentially:
1. Supervised Fine-Tuning (SFT) on 27,540 high-quality annotations
2. Iterative RLHF (V1 through V5) with Rejection Sampling
3. PPO optimization (from RLHF-V4 onward)
4. Ghost Attention (GAtt) for multi-turn consistency (from RLHF-V3 onward)

### Key Technical Components

#### Model Configurations

| Model | Parameters | Context | GQA | Training Tokens | Learning Rate |
|---|---|---|---|---|---|
| Llama 2 7B | 7B | 4096 | No | 2.0T | 3.0e-4 |
| Llama 2 13B | 13B | 4096 | No | 2.0T | 3.0e-4 |
| Llama 2 34B | 34B | 4096 | Yes | 2.0T | 1.5e-4 |
| Llama 2 70B | 70B | 4096 | Yes | 2.0T | 1.5e-4 |

Global batch size for all models: 4M tokens. The 34B model was trained but not publicly released due to insufficient red-teaming time (Section 1, p. 4).

#### Grouped-Query Attention (GQA)

Standard multi-head attention (MHA) uses n_heads independent key-value heads. Multi-query attention (MQA, Shazeer 2019) uses a single KV head shared across all query heads. GQA is an intermediate: n_kv_heads KV heads serve n_heads query heads, with each KV head serving n_heads / n_kv_heads query heads.

For the 70B model, 8 KV heads serve 64 query heads, reducing the KV cache by 8x compared to MHA. Ablation at 30B scale for 150B tokens (Table 18, Appendix A.2.1) shows GQA achieves comparable quality to MHA across benchmarks while enabling significantly higher inference throughput (moderate evidence -- single model scale, single training budget). MHA triggers OOM at batch size 1024 for 256-token context on 8xA100 80GB; GQA and MQA succeed at those settings (Figure 24). To maintain comparable parameter count, FFN dimension was increased by 1.33x for MQA and 1.3x for GQA in the ablation.

#### Pretraining

- **Data:** 2T tokens from a new mix of publicly available data (no Meta user data). Factual sources upsampled to increase knowledge and reduce hallucinations. Exact composition not disclosed.
- **Optimizer:** AdamW (beta_1 = 0.9, beta_2 = 0.95, eps = 1e-5)
- **Learning rate:** Cosine schedule with 2000 warmup steps. Final learning rate decays to 10% of peak.
- **Weight decay:** 0.1; Gradient clipping: 1.0
- **Hardware:** Meta's Research Super Cluster (RSC, NVIDIA Quantum InfiniBand, 400W TDP) and internal production cluster (RoCE, 350W TDP). Both use A100-80GB GPUs with 200 Gbps interconnect.
- **Training cost:** Total 3,311,616 GPU-hours across all models: 7B = 184,320; 13B = 368,640; 34B = 1,038,336; 70B = 1,720,320 GPU-hours (Table 2).
- **Carbon emissions:** 539 tCO2eq total, 100% offset by Meta's sustainability program (Table 2).
- **Observation:** After pretraining on 2T tokens, models still showed no sign of saturation (Figure 5).

#### Supervised Fine-Tuning (SFT)

SFT uses publicly available instruction-tuning data plus vendor-collected annotations. Key finding: **27,540 high-quality, carefully curated annotations outperformed larger but noisier datasets** (millions of third-party examples; Section 3.1). Quality validated on 180 examples where SFT model outputs were competitive with human-written annotations.

- Learning rate: cosine schedule, peak 2e-5
- Weight decay: 0.1; Batch size: 64; Sequence length: 4096
- Loss zeroed on user prompt tokens (backpropagation only on answer tokens)
- Trained for 2 epochs

#### Reinforcement Learning from Human Feedback (RLHF)

RLHF proceeds through five iterative rounds (RLHF-V1 through V5):

**Human Preference Data:** Over 1,418,091 binary comparisons collected across 14 weekly batches from Meta annotators (Table 26). Additional open-source data used: Anthropic Helpful (122,387), Anthropic Harmless (43,966), OpenAI Summarize (176,625), OpenAI WebGPT (13,333), StackExchange (1,038,480), Stanford SHP (74,882), Synthetic GPT-J (33,139). Total: 2,919,326 comparisons (Table 6).

**Reward Modeling:** Two separate reward models trained -- one for helpfulness, one for safety -- both initialized from pretrained chat model checkpoints (to prevent information mismatch). Binary ranking loss with preference-rating margin:

> L_ranking = -log(sigma(r_theta(x, y_c) - r_theta(x, y_r) - m(r)))

where m(r) is a discrete function of the preference rating (large margin for clearly distinct pairs, small/zero for similar; Table 27). Trained for 1 epoch with max learning rate 5e-6 (70B) or 1e-5 (others), batch size 512 pairs, cosine schedule to 10% of max LR (Section 3.2.2).

Helpfulness RM achieves 70.6% average accuracy across test sets; Safety RM achieves 64.3% (Table 7). On Meta Safety data, Safety RM reaches 94.3% accuracy on "significantly better" pairs (Table 8). Both RMs outperform GPT-4 used as a zero-shot reward model (Table 7).

**Rejection Sampling (RS):** For each prompt, K outputs sampled from the current policy. Output with highest reward model score selected as training data. Performed only with the 70B model; smaller models fine-tuned on rejection-sampled data from 70B (distillation). Optimal sampling temperature: T in [1.2, 1.3] for 10-100 outputs (Figure 8). Later iterations incorporated top samples from ALL prior iterations (not just the preceding one) to prevent regression (Section 3.2.3).

**Proximal Policy Optimization (PPO):** Standard PPO applied after rejection sampling, starting from RLHF-V4 onward. The reward function combines helpfulness and safety rewards:

> R_c(g | p) = R_s(g | p) if IS_SAFETY(p) or R_s(g | p) < 0.15, else R_h(g | p)

Safety threshold 0.15 chosen with precision = 0.89, recall = 0.55 on Meta Safety test set (Section 3.2.3). Scores whitened via logit function, with KL penalty for diverging from original policy:

> R(g | p) = R_tilde_c(g | p) - beta * D_KL(pi_theta(g | p) || pi_0(g | p))

PPO hyperparameters: learning rate 1e-6 (constant), batch size 512, clip threshold 0.2, mini-batch size 64, one gradient step per mini-batch. KL penalty beta = 0.01 (7B, 13B) or 0.005 (34B, 70B). Trained for 200-400 iterations (70B: ~330 seconds per iteration). FSDP caused ~20x slowdown during generation; mitigated by consolidating model weights to each node before generation (Section 3.2.3).

#### Ghost Attention (GAtt)

Ghost Attention enforces system prompt adherence across multi-turn dialogues. In training, the system instruction is synthetically concatenated to all user messages. The model samples responses from this augmented data, then the instruction is dropped from all but the first turn. Loss is set to zero for all tokens from previous turns, focusing learning on following the system instruction in the current response (Section 3.3).

Training instructions constructed by randomly combining categories (hobbies, languages, public figures). Half the time, instructions are made less verbose (e.g., "Always act as Napoleon from now" becomes "Figure: Napoleon."). Applied after RLHF-V3. Maintains 100% attribute retention for 20+ turns (Table 30), compared to 100% at turn 2 dropping to 10% at turn 4 and 0% at turn 6 without GAtt (limited evidence -- evaluated on public figures and hobbies constraints only). Generalizes to constraints not present in training (e.g., "Always answer with Haiku"; Figure 28, Appendix A.3.5).

#### Safety Fine-Tuning

Safety alignment consists of three techniques (Section 4.2):

1. **Supervised Safety Fine-Tuning:** Adversarial prompts and safe demonstrations included in SFT.
2. **Safety RLHF:** Separate safety reward model plus adversarial prompts for rejection sampling and PPO.
3. **Safety Context Distillation:** Safer responses generated by prefixing a safety preprompt (e.g., "You are a safe and responsible assistant"), then fine-tuning without the preprompt. Applied only when the safety RM predicts improvement, to avoid degrading quality on already-safe responses (Figure 16b, Section 4.2.4).

Risk categories: illicit/criminal activities, hateful/harmful activities, unqualified advice (Section 4.2.1). Red teaming involved 350+ participants spanning cybersecurity, election fraud, social media misinformation, legal, policy, and other domains (Section 4.3). Robustness metric gamma (average violating prompts per person per hour) improved from 1.8 to 0.45 on the 7B model over iterations (Section 4.3).

### Experimental Setup

**Base model evaluation:** Standard benchmarks across 8 categories (Table 3):
- Code: HumanEval, MBPP (pass@1)
- Commonsense Reasoning: PIQA, SIQA, HellaSwag, WinoGrande, ARC-e/c, OpenBookQA, CommonsenseQA (7-shot for CSQA, 0-shot otherwise)
- World Knowledge: NaturalQuestions, TriviaQA (5-shot)
- Reading Comprehension: SQuAD, QuAC, BoolQ (0-shot)
- Math: GSM8K (8-shot), MATH (4-shot)
- MMLU (5-shot), BBH (3-shot), AGI Eval (3-5 shot, English only)

**Chat model evaluation:** Human evaluation comparing Llama 2-Chat against ChatGPT (gpt-3.5-turbo-0301), PaLM (chat-bison-001), Falcon-40B-Instruct, Vicuna-33B, MPT-7B-chat. Over 4,000 single and multi-turn prompts, 3 raters per prompt, 7-point Likert scale (Table 32, Section 3.4.2).

**Safety evaluation:** TruthfulQA (817 questions, 38 categories), ToxiGen (13 minority groups, revised version from Hosseini et al. 2023), BOLD (23,679 prompts, 43 subgroups across 5 domains). Safety human evaluation: ~2,000 adversarial prompts (1,351 single-turn + 623 multi-turn), 5-point Likert safety scale, 3 annotators per example (Section 4.4).

**Reproducibility:** Code released at https://github.com/facebookresearch/llama. Model weights available at https://huggingface.co/meta-llama. Pretraining data composition not disclosed (only stated as "publicly available data"). SFT data composition not fully disclosed. No random seeds reported. Single training run per model configuration.

### Key Results

**Base models vs. open-source (Table 3):**

| Model | Code | Commonsense | World Knowledge | Reading Comp. | Math | MMLU | BBH | AGI Eval |
|---|---|---|---|---|---|---|---|---|
| Llama 2 7B | 16.8 | 63.9 | 48.9 | 61.3 | 14.6 | 45.3 | 32.6 | 29.3 |
| Llama 2 13B | 24.5 | 66.9 | 55.4 | 65.8 | 28.7 | 54.8 | 39.4 | 39.1 |
| Llama 2 34B | 27.8 | 69.9 | 58.7 | 68.0 | 24.2 | 62.6 | 44.1 | 43.4 |
| Llama 2 70B | 37.5 | 71.9 | 63.6 | 69.4 | 35.2 | 68.9 | 51.2 | 54.2 |
| LLaMA 65B | 30.7 | 70.7 | 60.5 | 68.6 | 30.8 | 63.4 | 43.5 | 47.6 |
| Falcon 40B | 15.2 | 69.2 | 56.7 | 65.7 | 12.6 | 55.4 | 37.1 | 37.0 |

- Llama 2 70B improves over LLaMA 65B by ~5.5 points on MMLU and ~7.7 points on BBH (strong evidence -- tested across 8 benchmark categories spanning code, reasoning, knowledge, and math).

**Base models vs. closed-source (Table 4):**

| Benchmark (shots) | GPT-3.5 | GPT-4 | PaLM | PaLM-2-L | Llama 2 70B |
|---|---|---|---|---|---|
| MMLU (5-shot) | 70.0 | 86.4 | 69.3 | 78.3 | 68.9 |
| TriviaQA (1-shot) | -- | -- | 81.4 | 86.1 | 85.0 |
| Natural Questions (1-shot) | -- | -- | 29.3 | 37.5 | 33.0 |
| GSM8K (8-shot) | 57.1 | 92.0 | 56.5 | 80.7 | 56.8 |
| HumanEval (0-shot) | 48.1 | 67.0 | 26.2 | -- | 29.9 |
| BBH (3-shot) | -- | -- | 52.3 | 65.7 | 51.2 |

- Llama 2 70B approaches GPT-3.5 on MMLU (68.9 vs 70.0) and GSM8K (56.8 vs 57.1) but lags significantly on code (29.9 vs 48.1 HumanEval). Large gap remains vs. GPT-4 and PaLM-2-L (limited evidence -- closed-source results taken from published papers with potentially different evaluation setups).

**Chat models -- human evaluation (Figure 1):**

| Comparison | Win | Tie | Loss |
|---|---|---|---|
| Llama 2-Chat 70B vs. ChatGPT | 35.9% | 31.5% | 32.5% |
| Llama 2-Chat 70B vs. PaLM-bison | 53.0% | 24.6% | 22.4% |
| Llama 2-Chat 34B vs. Falcon-40B-Instruct | 76.3% | 14.6% | 9.1% |
| Llama 2-Chat 34B vs. Vicuna-33B | 37.2% | 31.6% | 31.2% |
| Llama 2-Chat 13B vs. Vicuna-13B | 45.4% | 29.8% | 24.9% |
| Llama 2-Chat 7B vs. MPT-7B-chat | 61.1% | 20.9% | 18.0% |

- Without system prompt for ChatGPT, Llama 2-Chat 70B win rate increases from 36% to 44% (Figure 30, Appendix A.3.7).
- Inter-rater reliability (Gwet's AC2): 0.37-0.55 for helpfulness (lower for similar models, higher for distinct), 0.70-0.95 for safety (average 0.92 for Llama 2-Chat; Section 3.4.2, Section 4.4).
- No coding or reasoning prompts in the evaluation set, which may favor Llama 2-Chat (scope limitation acknowledged in Section 3.4.2).

**Safety (Table 14):**

| Model | TruthfulQA (higher better) | ToxiGen (lower better) |
|---|---|---|
| ChatGPT | 78.46 | 0.20 |
| Llama 2-Chat 7B | 57.04 | 0.00 |
| Llama 2-Chat 13B | 62.18 | 0.00 |
| Llama 2-Chat 34B | 67.20 | 0.02 |
| Llama 2-Chat 70B | 64.14 | 0.01 |
| Falcon-instruct 7B | 28.03 | 7.89 |
| MPT-instruct 7B | 29.99 | 16.33 |

- Fine-tuning improves truthfulness from 50.18 to 64.14 and toxicity from 24.60 to 0.01 for the 70B model (Tables 11 and 14).
- Llama 2-Chat achieves effectively 0% toxic generations across all sizes (Table 45, strong evidence -- tested across 13 demographic groups).
- Anomaly: 70B Chat (64.14%) scores lower than 34B Chat (67.20%) on TruthfulQA (Table 14).

**Tool use emergence (Table 15):**

| Model | ASDiv | SVAMP | MAWPS |
|---|---|---|---|
| Toolformer | 40.4 | 29.4 | 44.0 |
| Llama 2-Chat | 67.1 | 69.2 | 82.4 |

- Zero-shot tool use without explicit tool training (preliminary observation, single evaluation, not systematically validated).

### Context Length Ablation

Both models trained at identical settings for 150B tokens, varying only context length (Table 16, Table 17, Appendix A.2.1):

| Task | 2k Context | 4k Context |
|---|---|---|
| NarrativeQA (F1) | 0.21 | 17.26 |
| Qasper (F1) | 0.71 | 18.52 |
| QuALITY (acc) | 26.1 | 29.6 |
| QMSum (Rouge-1/2/L) | 0.13/0.01/0.12 | 15.08/3.55/12.16 |
| ContractNLI (EM) | 11.76 | 16.33 |
| HellaSwag (0-shot) | 75.1 | 74.8 |
| HumanEval (0-shot) | 7.9 | 7.3 |
| GSM8K (8-shot) | 4.9 | 6.5 |

SCROLLS tasks have average input length of 3.5k tokens, explaining the large improvement. Standard benchmarks show negligible degradation (moderate evidence -- single model scale, 150B token ablation budget).

### GQA Ablation

30B model trained for 150B tokens with MHA, MQA, and GQA (Table 18, Appendix A.2.1):

| | BoolQ | PIQA | SIQA | HellaSwag | ARC-e | ARC-c | NQ | TQA | MMLU | GSM8K | HumanEval |
|---|---|---|---|---|---|---|---|---|---|---|---|
| MHA | 71.0 | 79.3 | 48.2 | 75.1 | 71.2 | 43.0 | 12.4 | 44.7 | 28.0 | 4.9 | 7.9 |
| MQA | 70.6 | 79.0 | 47.9 | 74.5 | 71.6 | 41.9 | 14.5 | 42.8 | 26.5 | 4.8 | 7.3 |
| GQA | 69.4 | 78.8 | 48.6 | 75.4 | 72.1 | 42.5 | 14.0 | 46.2 | 26.9 | 5.3 | 7.9 |

GQA performs comparably to MHA on most tasks and better than MQA on average, while enabling higher throughput at large batch sizes (moderate evidence -- single model scale).

### Dataset Contamination Analysis

Novel contamination detection method: matches on tokenized input with skipgram budget of 4 tokens and minimum match length L. Samples classified as "clean" (<20% contaminated tokens) or "dirty" (>=80%). Statistical significance tested via Z-scores requiring |Z_n| > 2 for all four subset types (Section A.6).

**Only HellaSwag and MMLU-Humanities show evidence of contamination boost** (Table 51). For HellaSwag at L=40: 70B clean subset scores 80.0 vs. dirty subset 92.2 (Z_n = 7.42 for dirty). 70B model benefits more from contamination than 7B. No other dataset showed contamination evidence at any L.

### RLHF Learnings

**In-Context Temperature Rescaling:** RLHF produces dynamic temperature rescaling contingent on context (Figure 21, Section 5.1). For creative prompts, increasing temperature continues to generate diversity. For factual prompts, Self-BLEU slope diminishes across RLHF iterations -- the model learns to consistently provide the same factual answer regardless of temperature.

**Temporal Perception:** With only 1,000 SFT time-focused examples, Llama 2-Chat generalizes the notion of time, adjusting responses based on stated dates (Figure 22, Section 5.1). This suggests LLMs have internalized temporal concepts to a greater extent than previously assumed.

---

## Limitations and Failure Modes

The paper explicitly acknowledges the following limitations (Section 5.2):

1. **Knowledge cutoff:** Training data ends September 2022; model cannot access post-cutoff information.
2. **Hallucinations:** Propensity toward non-factual generation and unqualified advice.
3. **English-centric:** 89.70% of pretraining data is English (Table 10). Performance in other languages is fragile.
4. **Harmful content generation:** Despite fine-tuning, harmful, offensive, or biased content may still be generated, particularly in non-English languages where safety data is scarce.
5. **Over-cautiousness:** Safety tuning sometimes produces excessive refusals. Examples include refusing to provide a recipe for "Christmas crack" (a toffee candy) or a "bomb drink" (a cocktail), interpreting keywords literally (Table 41). At 100% safety data, the model breaks character on benign pizza roleplay containing the word "abomination" (Table 37). False refusal rate on helpfulness data is ~0.05%; on a curated borderline set of 210 samples, it reaches ~27% at 100% safety data (Figure 33).
6. **Safety-helpfulness tradeoff:** As safety data increases from 0% to 100%, safety RM score rises (0.05 to 0.93) but helpfulness RM score declines (0.65 to 0.38) on adversarial prompts (Table 36, Section 4.2.3). Context distillation can degrade quality on samples that initially have high safety scores (Figure 16b).
7. **Code generation gap:** Llama 2 70B significantly lags GPT-3.5 on HumanEval (29.9 vs 48.1) and GPT-4 (67.0).
8. **Potential for misuse:** Base pretrained models (non-Chat) carry significant risk and require additional safety tuning before deployment.
9. **Pretrained model toxicity:** Most toxic demographic groups for pretrained Llama 2 70B are Mexicans (32.90%), Women (31.05%), and Latinos (30.42%) on ToxiGen (Table 45).

- **[Inferred]** No evaluation on tasks requiring >4096 tokens, so the practical benefit of the context extension is only demonstrated on tasks with average input length within the context window (~3.5K for SCROLLS).
- **[Inferred]** Human helpfulness evaluation excludes coding and reasoning prompts (acknowledged in Section 3.4.2), which likely inflates the apparent competitiveness with ChatGPT.
- **[Inferred]** Single training run per model size, no variance estimates reported, limiting claims about the reliability of specific performance deltas.

#### Scope and Comparability

- **What was not tested:** No evaluation on tasks requiring inputs >4096 tokens. No multilingual benchmarks. No evaluation of the 34B model on safety (not red-teamed sufficiently for release). No systematic evaluation of tool use beyond three math datasets. No evaluation on code generation with the Chat models (only base models evaluated on HumanEval/MBPP).
- **Comparability notes:** Closed-source results (GPT-3.5, GPT-4, PaLM, PaLM-2-L) are taken from their respective papers and may use different evaluation frameworks, decoding strategies, and few-shot templates. Human evaluation uses Meta-designed prompts and guidelines, which the authors acknowledge may be biased toward Llama 2-Chat (Section 4.4). Safety evaluations use Meta's content standards, creating a potential evaluation bias. The GQA ablation uses a single 30B model scale with 150B training tokens, which may not generalize to the full 2T token training budget. Falcon's low violation rate in safety evaluation is partly attributable to its concise (1-2 sentence) responses rather than genuine safety robustness (Section 4.4).

---

## Conclusions

### Contributions

1. **Extended context and increased data improve base performance.** Llama 2's 4096-token context and 2T training tokens yield consistent improvements over LLaMA across all benchmarks (MMLU: 68.9 vs 63.4; GSM8K: 56.8 vs 50.9 for the largest models; Table 3). Context ablation demonstrates dramatic gains on long-context tasks with no standard benchmark degradation (Tables 16-17).

2. **GQA enables efficient large-model inference with negligible quality loss.** The 70B model uses 8 KV heads (vs. 64 for MHA), reducing KV cache by 8x. Ablation at 30B scale confirms comparable accuracy to MHA while avoiding OOM at large batch sizes (Table 18, Figure 24). This established GQA as the standard for open models above 30B parameters.

3. **Iterative RLHF with rejection sampling improves progressively.** Five rounds of RLHF with increasing human preference data (1.4M+ comparisons across 14 batches) show consistent improvements (Figure 11). Rejection sampling from the 70B model provides effective distillation for smaller models. Incorporating top samples from all prior iterations prevents capability regression (Section 3.2.3).

4. **Ghost Attention enables multi-turn instruction following.** GAtt achieves 100% system prompt adherence for 20+ turns (vs. 0% at turn 6 without GAtt; Table 30), generalizing to constraint types not seen in training (Appendix A.3.5, Figure 28).

5. **Safety fine-tuning achieves near-zero toxicity without degrading helpfulness.** With sufficient helpfulness training data (~0.9M samples), adding safety data (~0.1M samples) reduces toxic generations to effectively 0% without decreasing helpfulness RM scores (Figure 14, Figure 15). Separate safety and helpfulness reward models enable targeted optimization.

6. **Comprehensive contamination analysis identifies limited benchmark leakage.** Novel tokenized contamination detection with skipgram matching identifies only HellaSwag and MMLU-Humanities as affected, with 70B models benefiting more than 7B (Table 51).

7. **Quality over quantity for SFT data.** 27,540 carefully curated annotations outperformed millions of third-party examples (Section 3.1), consistent with Zhou et al. (2023).

### Implications

1. **Open-source chat models approach closed-source quality.** Llama 2-Chat 70B achieves a 36% win rate against ChatGPT on helpfulness (Figure 1), demonstrating a narrowing gap. However, significant deficits remain on coding, mathematical reasoning, and knowledge tasks (Table 4).

2. **RLHF surpasses the ceiling of SFT annotation quality.** The paper argues RLHF enables models to explore writing trajectories beyond the best human annotators (Section 5.1), with reward models effectively removing the tail distribution of poor responses (Figure 20).

3. **Zero-shot tool use can emerge from alignment without explicit tool training.** The spontaneous emergence of calculator and search tool usage suggests RLHF may unlock latent capabilities from pretraining (Table 15, Figure 23). This observation is preliminary and not systematically validated.

4. **The safety-helpfulness tension requires targeted solutions.** Blanket safety data scaling causes over-cautiousness; targeted context distillation (applying safety augmentation only when the safety RM predicts improvement) is more effective than uniform application (Figure 16, Section 4.2.4).

---

## Key Claims

1. **Llama 2 70B outperforms all open-source models at the time of release.** It exceeds LLaMA 65B by +5.5 on MMLU (68.9 vs 63.4), +7.7 on BBH (51.2 vs 43.5), and +5.9 on GSM8K (56.8 vs 50.9). Exceeds Falcon 40B by +13.5 on MMLU. Evidence: Table 3, Section 2.3. Scope: 7B-70B scale, standard English academic benchmarks. Magnitude: see deltas above. Status: **supported** (strong evidence -- tested across 8 benchmark categories, multiple model sizes, consistent improvement pattern).

2. **Doubling context length from 2048 to 4096 yields large gains on long-context tasks without degrading standard benchmarks.** NarrativeQA F1 improves from 0.21 to 17.26; HellaSwag changes by -0.3 (within noise). Evidence: Tables 16-17, Appendix A.2.1. Scope: 30B model scale, 150B training tokens, SCROLLS tasks with ~3.5K average input length. Magnitude: 80x improvement on NarrativeQA, 26x on Qasper. Status: **supported** (moderate evidence -- single model scale ablation).

3. **GQA with 8 KV heads matches MHA quality while improving inference throughput.** Ablation at 30B scale shows GQA averages comparable to MHA across 11 benchmarks, while avoiding OOM at batch sizes where MHA fails. Evidence: Table 18, Figure 24. Scope: 30B model, 150B tokens, 8xA100 tensor parallelism. Magnitude: OOM avoidance at batch size 1024 for 256-token context. Status: **supported** (moderate evidence -- single scale point).

4. **Llama 2-Chat 70B wins 36% of comparisons against ChatGPT.** Based on ~4,000 prompts with 3 annotators each, win 35.9%, tie 31.5%, loss 32.5%. Evidence: Figure 1, Section 3.4.2. Scope: English only, no coding/reasoning prompts, gpt-3.5-turbo-0301. Magnitude: 35.9% win rate (increases to 44% without system prompt for ChatGPT). Status: **supported** (moderate evidence -- limited prompt diversity, no coding/reasoning prompts).

5. **Safety fine-tuning reduces toxicity to effectively 0% without harming helpfulness.** ToxiGen scores drop from 24.60 (pretrained) to 0.01 (Chat) for 70B; helpfulness RM distribution is preserved. Evidence: Tables 14, 45; Figure 14. Scope: 7B-70B, ToxiGen 13 demographic groups, ~0.9M helpfulness + ~0.1M safety data. Magnitude: 24.59 percentage point reduction in toxicity. Status: **supported** (strong evidence -- tested across all model sizes and 13 demographic groups).

6. **Ghost Attention maintains 100% system prompt adherence for 20+ turns.** Without GAtt, adherence drops to 0% by turn 6. With GAtt, 100% maintained through all tested turns. Evidence: Table 30, Appendix A.3.5. Scope: public figures and hobbies constraints, <4048 total tokens. Magnitude: 100% vs 0% adherence at turn 6+. Status: **supported** (limited evidence -- only two constraint types evaluated, human evaluation).

7. **Llama 2 approaches GPT-3.5 on MMLU and GSM8K but lags on code.** MMLU: 68.9 vs 70.0 (-1.1); GSM8K: 56.8 vs 57.1 (-0.3); HumanEval: 29.9 vs 48.1 (-18.2). Evidence: Table 4. Scope: 70B model only, 6 benchmarks. Magnitude: see deltas. Status: **supported**.

8. **27,540 high-quality SFT annotations outperform millions of third-party examples.** Evidence: Section 3.1. Scope: Meta vendor annotations vs third-party datasets. Magnitude: qualitative improvement noted, no quantitative comparison table provided. Status: **supported** (limited evidence -- qualitative observation, consistent with Zhou et al. 2023).

9. **Llama 2-Chat demonstrates zero-shot tool use, outperforming Toolformer on math datasets.** ASDiv 67.1 vs 40.4; SVAMP 69.2 vs 29.4; MAWPS 82.4 vs 44.0. Evidence: Table 15, Figure 23. Scope: calculator tool on 3 math datasets only. Magnitude: +26.7 to +39.8 point improvements. Status: **supported** (limited evidence -- three math benchmarks, zero-shot only, not systematically validated).

10. **Only HellaSwag and MMLU-Humanities show contamination boost.** HellaSwag (L=40): 70B clean 80.0 vs dirty 92.2 (Z_n = 7.42). Evidence: Table 51, Appendix A.6. Scope: 7B and 70B pretrained models, tokenized contamination detection. Magnitude: +12.2 points between clean and dirty subsets for 70B HellaSwag. Status: **supported** (strong evidence -- rigorous statistical methodology with Z-score testing).

---

## Open Questions

1. **Training data saturation.** Training loss showed no sign of saturation at 2T tokens (Figure 5). Would continued training or larger datasets yield further improvements? Not addressed within this paper; Llama 3 uses 15T tokens but is a different architecture.

2. **Safety-helpfulness Pareto frontier.** Can the over-cautiousness problem (false refusals on "Christmas crack," "bomb drink," pizza roleplay) be solved without reducing safety? The paper's targeted context distillation is partial; the borderline false refusal rate of ~27% remains high (Figure 33). Not directly addressed.

3. **Context length scaling.** How does the 4096-token context perform on tasks requiring >4K tokens? The paper does not evaluate on benchmarks with inputs exceeding the context window. Partially addressed by YaRN (2024-05-yarn-context-extension) and PI (2023-06-pi-positional-interpolation) which extend Llama 2's context.

4. **Contamination impact.** HellaSwag and MMLU-Humanities show contamination boosts (Table 51), with 70B benefiting more than 7B. Does contamination disproportionately benefit larger models? Not addressed.

5. **Non-English safety.** Safety tuning is English-only, and 89.70% of pretraining data is English (Table 10). How does safety generalize to other languages where adversarial prompts are known attack vectors? Red teaming included non-English prompts as attack vectors but all target model outputs were in English (Section 4.3). Not addressed.

---

## Core References and Why They Are Referenced

### Architecture Foundations

- **Vaswani et al. (2017)** -- *Attention Is All You Need.* The original Transformer architecture. Llama 2 retains the decoder-only autoregressive structure.
- **Su et al. (2022)** -- *RoFormer: Enhanced Transformer with Rotary Position Embedding.* Provides RoPE, retained with base frequency b = 10000 and extended to 4096-token context. The extended context became the primary target for context extension research.
- **Zhang & Sennrich (2019)** -- *Root Mean Square Layer Normalization.* RMSNorm used for pre-normalization, inherited from LLaMA.
- **Shazeer (2020)** -- *GLU Variants Improve Transformer.* SwiGLU activation, inherited from LLaMA.

### Direct Predecessor

- **Touvron et al. (2023a)** -- *LLaMA: Open and Efficient Foundation Language Models.* The base architecture and training methodology that Llama 2 extends with doubled context, 40% more data, and GQA.

### Grouped-Query Attention

- **Ainslie et al. (2023)** -- *GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints.* Introduces GQA and the method for converting MHA checkpoints to GQA via mean-pooling of KV heads. Llama 2 70B is the first widely adopted open model to use GQA.
- **Shazeer (2019)** -- *Fast Transformer Decoding: One Write-Head Is All You Need.* Introduces multi-query attention (MQA), the extreme case of GQA with a single KV head.

### Alignment and RLHF

- **Ouyang et al. (2022)** -- *Training Language Models to Follow Instructions with Human Feedback (InstructGPT).* Establishes the SFT + RLHF pipeline that Llama 2-Chat follows, including the binary ranking loss for reward modeling.
- **Schulman et al. (2017)** -- *Proximal Policy Optimization Algorithms.* PPO algorithm used in the RLHF stage.
- **Bai et al. (2022b)** -- *Constitutional AI: Harmlessness from AI Feedback.* Related alignment approach; Llama 2 uses a similar dual-reward (helpfulness + safety) framework and draws on context distillation ideas. Rejection sampling approach also adopted.
- **Stiennon et al. (2020)** -- *Learning to Summarize from Human Feedback.* First application of RLHF to text generation; PPO RL scheme and KL penalty adopted in Llama 2.
- **Bai et al. (2022a)** -- *Training a Helpful and Harmless Assistant with RLHF.* Anthropic Helpful/Harmless datasets used in reward model training; helpfulness-safety tradeoff observed.

### Safety Evaluation

- **Lin et al. (2021)** -- *TruthfulQA: Measuring How Models Mimic Human Falsehoods.* Used for evaluating truthfulness across 817 questions.
- **Hartvigsen et al. (2022)** -- *ToxiGen: A Large-Scale Machine-Generated Dataset for Adversarial and Implicit Hate Speech Detection.* Used for toxicity evaluation across 13 minority groups.
- **Dhamala et al. (2021)** -- *BOLD: Dataset and Metrics for Measuring Biases in Open-Ended Language Generation.* Used for bias evaluation across 43 demographic subgroups.

### Tool Use

- **Schick et al. (2023)** -- *Toolformer: Language Models Can Teach Themselves to Use Tools.* Primary baseline for tool use comparison (Table 15). Llama 2-Chat dramatically outperforms Toolformer in zero-shot setting without explicit tool training.

### Contamination Analysis

- **Lee et al. (2022)** -- Suffix array library adapted for tokenized contamination detection at scale (~7 hours on ~1,500 cores).
- **Chowdhery et al. (2022)** -- *PaLM: Scaling Language Modeling with Pathways.* Improved contamination methodology (8-gram, 70% threshold) that Llama 2's approach extends.

### Scaling and Efficiency

- **Hoffmann et al. (2022)** -- *Training Compute-Optimal Large Language Models (Chinchilla).* Redefined scaling laws toward token count; Llama 2 trains on 2T tokens, roughly following compute-optimal proportions.
