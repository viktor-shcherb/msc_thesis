---
title: "Ministral 3"
authors: "Liu, Khandelwal, Subramanian, Jouault, et al."
year: 2026
venue: "arXiv preprint 2601.08584"
paper_type: preprint
categories: ["model-release", "architecture", "pruning-and-sparsity"]
scope: ["dense open-weight LMs", "iterative distillation", "multi-size model family (3B/8B/14B)", "long-context extension to 256K"]
benchmarks_used: ["mmlu", "triviaqa", "math-hendrycks", "agi-eval", "arc", "race", "natural-questions", "gpqa", "mbpp", "mmmu", "arena-hard", "mt-bench", "livecodebench", "aime-2025", "hmmt-2025"]
models_introduced: ["ministral-3-3b", "ministral-3-8b", "ministral-3-14b"]
models_evaluated: ["qwen3-14b", "qwen3-8b", "qwen3-4b", "gemma-3-12b", "gemma-3-4b"]
key_claims:
  - id: C1
    claim: "Cascade Distillation produces competitive 3B/8B/14B base models with 1-3T token training budgets versus larger from-scratch budgets (e.g., 15T/36T)"
    evidence: "Section 1, Table 2"
    status: supported
    scope: "Base model pretraining comparisons against Qwen3 and Gemma3 families"
    magnitude: "Token budget 1-3T vs 15T (Llama3) and 36T (Qwen3), with competitive benchmark performance"
  - id: C2
    claim: "Ministral 3 14B Base retains a large fraction of Mistral Small 3.1 capability despite >40% parameter reduction"
    evidence: "Section 1, Table 3"
    status: supported
    scope: "Teacher-student comparison on general, math/code, multilingual, and multimodal evaluations"
    magnitude: "MMLU-Redux 82.0 vs 82.7; MMLU 79.4 vs 81.0; MBPP 71.6 vs 71.6"
  - id: C3
    claim: "For pretraining distillation, a stronger teacher (Mistral Medium 3) does not necessarily outperform a smaller teacher (Mistral Small 3.1)"
    evidence: "Section 5.1, Figure 3"
    status: supported
    scope: "14B pretraining ablations in this report"
    magnitude: "Figure 3 trend favors Mistral Small 3.1 distillation across multiple downstream benchmarks"
  - id: C4
    claim: "Distilling from a post-trained teacher (instruct/reasoning) during pretraining improves STEM-oriented outcomes over a base teacher"
    evidence: "Section 5.1, Figure 4"
    status: supported
    scope: "3B pretraining teacher-variant ablations"
    magnitude: "Figure 4 reports stronger gains on MATH/code with comparable knowledge and multimodal results"
  - id: C5
    claim: "Ministral 3 14B Reasoning outperforms size-matched Qwen 3 14B on AIME 2024/2025, HMMT 2025, GPQA, and LiveCodeBench"
    evidence: "Table 5"
    status: supported
    scope: "Reasoning evaluation at pass@16 (pass@5 for LiveCodeBench)"
    magnitude: "AIME 2024: 89.8 vs 83.7; AIME 2025: 85.0 vs 73.7; HMMT 2025: 67.5 vs 55.8; GPQA: 71.2 vs 66.3; LiveCodeBench: 64.6 vs 59.3"
  - id: C6
    claim: "Layer importance can be approximated using output/input activation norm ratios for pruning"
    evidence: "Section 3.1, Algorithm 2"
    status: supported
    scope: "Cascade Distillation pruning stage in this architecture/training setup"
    magnitude: "Heuristic replaces counterfactual-perplexity layer ranking while enabling iterative pruning across 24B->14B->8B->3B"
  - id: C7
    claim: "ODPO improves alignment quality and mitigates generation-pathology issues relative to SFT/offline preference optimization"
    evidence: "Section 3.2.2, Section 5.3, Figure 6"
    status: supported
    scope: "Instruction and reasoning post-training stages (especially 14B/8B)"
    magnitude: "Figure 6 reports substantial chat-benchmark gains for 14B/8B after ODPO; paper also reports mitigation of infinite-loop artifacts"
cross_references:
  - target: 2017-12-attention-is-all-you-need
    type: extends
    detail: "Ministral 3 uses a decoder-only Transformer backbone with modern attention/norm variants"
  - target: 2024-05-yarn-context-extension
    type: extends
    detail: "Uses YaRN-based context extension and position-aware scaling for long-context training"
  - target: 2025-05-qwen3-technical-report
    type: evaluates
    detail: "Primary same-era baseline family in tables for both base and reasoning variants"
  - target: 2025-03-gemma-3-technical-report
    type: evaluates
    detail: "Primary instruct/base comparison family in reported benchmark tables"
  - target: 2023-10-mistral-7b
    type: complementary
    detail: "Shares architectural lineage; Ministral 3 extends Mistral-family work with multi-size cascade distillation"
  - target: 2025-07-smollm3-long-context-reasoner
    type: concurrent
    detail: "Both are 3B-scale open model releases targeting efficient deployment with strong capabilities; SmolLM3 uses 11.2T token training vs Ministral 3's cascade distillation approach"
open_questions:
  - question: "How far can Cascade Distillation be pushed below 3B before quality collapse dominates compute savings?"
    addressed_by: null
  - question: "What teacher-student capacity ratio best balances pretraining and post-training distillation quality?"
    addressed_by: null
  - question: "How robust are the teacher-selection findings across architectures and data mixtures outside this report?"
    addressed_by: null
  - question: "How well do 256K-context Ministral models perform on hard long-context reasoning tasks beyond retrieval-style probes?"
    addressed_by: null
  - question: "Can verbosity-control methods preserve STEM gains while removing reflection/backtracking artifacts in smaller reasoning models?"
    addressed_by: null
---

# Ministral 3

**Authors:** Alexander H. Liu, Kartik Khandelwal, Sandeep Subramanian, Victor Jouault, et al. (Mistral AI)
**Date:** January 2026, arXiv:2601.08584

---

## 1. Core Research Problem

Recent open model families have improved quality partly by very large pretraining budgets. The paper frames this as a practical bottleneck: training from scratch at competitive quality can require tens of trillions of tokens.

The concrete question addressed here is:

**How can a single strong parent model be transformed into multiple smaller competitive dense models (14B, 8B, 3B) with substantially lower total pretraining cost, while still supporting modern capabilities (instruction-following, reasoning, vision, long context)?**

The paper argues this requires solving two coupled problems:

1. Efficiently transferring capability from a larger parent without retraining every child from scratch.
2. Preserving (or recovering) downstream quality after aggressive size reduction and post-training specialization.

---

## 2. Problem Solutions

The solution is a staged recipe named **Cascade Distillation** plus task-specific post-training:

1. Iterative prune-distill-repeat from a 24B parent (Mistral Small 3.1) to 14B -> 8B -> 3B.
2. Two-stage pretraining distillation per child (short context then long context).
3. Separate post-training pipelines for:
   - instruct models (SFT + ODPO)
   - reasoning models (SFT + GRPO + ODPO)
4. Shared multimodal support through a frozen ViT encoder and retrained projection heads.

This is designed to amortize parent capability across a full model family instead of paying separate full pretraining costs for each size.

---

## 3. Approach Details

### Method

The pretraining algorithm is explicitly iterative:

> Start from a parent model, prune to target size, distill on short context, distill on long context, then prune that child checkpoint to initialize the next smaller model.

Core pruning components:

- Layer pruning via activation norm ratio proxy:
  > `score = mean(output_norm / input_norm)`
- Hidden-dimension pruning with PCA-based projection.
- Feedforward-dimension pruning in SwiGLU blocks:
  > `W2(SiLU(W1 x) * W3 x)`

### Key Technical Components

- Decoder-only Transformer, GQA (32/8), RoPE, SwiGLU, RMSNorm.
- Vocabulary size: 131K.
- Context target: 256K for base/instruct (reasoning variant described at 128K in intro).
- Vision: frozen 410M ViT copied from Mistral Small 3.1; per-size projection retraining.
- Distillation setup:
  - forward-KL-only objective favored by ablations described in text.
- Instruct ODPO:
  - online pair sampling at temperature 0.7
  - pairwise reward model with probabilistic preference weighting
  - stability tweaks (temperature calibration + beta-rescaling)
  - explicit handling of infinite-generation artifacts
- Reasoning pipeline:
  - SFT with short/long CoT
  - two-stage GRPO (STEM then general)
  - max generation length raised from 32K to 80K
  - ODPO with reasoning-chunk stripping before reward scoring

### Experimental Setup

The report evaluates across general knowledge, reasoning, code, multilingual, multimodal, and post-training alignment benchmarks. External baselines (Qwen/Gemma families) are re-run using the same internal evaluation harness/configuration.

### Key Results (from reported tables)

| Highlight | Reported result |
|---|---|
| 14B base vs Qwen3 14B | Better on TriviaQA (74.9 vs 70.3) and MATH (67.6 vs 62.0) |
| 14B reasoning vs Qwen3 14B | Better on AIME 2024/2025, HMMT 2025, GPQA, LiveCodeBench |
| 14B vs teacher (24B) | Small drop on many tasks, parity on MBPP (71.6 vs 71.6), stronger MATH (67.6 vs 55.8) |
| 8B base vs Gemma 12B | Paper reports strong parameter efficiency; 8B often competitive or better in listed tasks |

---

## 4. Results and Evidence

### Base-model comparisons (Table 2)

- 14B: strong math/QA profile against Qwen3 and Gemma3 peers.
- 8B: broad competitiveness with larger Gemma baseline in several metrics.
- 3B: weaker absolute scores than larger peers but remains competitive on selected tasks, notably MATH.

### Teacher-retention view (Table 3)

- Capability decays with model size as expected.
- 14B retains much of teacher performance on several benchmarks.
- Some tasks improve versus teacher (e.g., reported MATH score in table).

### Post-training view (Tables 4-5)

- Instruct: 14B achieves strong Arena Hard/WildBench/MM-MTBench profile.
- Reasoning: 14B and 8B show clear gains relative to Qwen counterparts on multiple listed benchmarks.

### Discussion figures (3-6)

- Figure 3: stronger teacher does not always help pretraining distillation.
- Figure 4: post-trained teacher variant can improve student outcomes, especially STEM.
- Figure 5: verbosity-performance tradeoff appears in instruction models.
- Figure 6: ODPO provides substantial post-RL chat-quality gains for larger reasoning variants.

---

## 5. Limitations and Failure Modes

### Author-acknowledged limitations

1. **Teacher-selection behavior is non-trivial.** Stronger teacher quality does not monotonically map to stronger pretraining students.
2. **Verbosity tradeoff.** More long-CoT data can raise STEM scores but can degrade chat naturalness.
3. **3B instability/sensitivity.** 3B requires extra stabilization (distillation in SFT; sensitivity to tuning choices).
4. **Reasoning-chat tension.** Reasoning specialization can hurt conversational quality, requiring additional alignment stages.

### Inferred limitations (explicit inference)

- **[Inferred]** Results are heavily table-driven and mostly relative to selected open families; external generalization beyond those baselines is not fully characterized in this report.
- **[Inferred]** Some comparisons pool models with different modality/tooling/post-training recipes, which may confound pure architecture/training-budget attribution.

### Scope and Comparability

- **What was not tested:** The report does not provide exhaustive cross-family ablations for teacher choice, does not fully characterize behavior beyond listed benchmark suites, and does not isolate architecture/data/post-training effects with controlled matched runs.
- **Comparability notes:** External baselines differ in modality stack, post-training recipes, and potentially data curation. Cross-family score gaps should be interpreted as end-to-end system comparisons, not pure architecture-only deltas.

---

## 6. Conclusions

### Contributions

1. **Compute-efficient family construction.** Cascade Distillation establishes a practical prune-distill-repeat recipe to derive 14B, 8B, and 3B models from a single stronger parent while retaining strong reported benchmark quality.
2. **Actionable distillation design findings.** The paper documents that teacher strength and teacher variant interact with stage: smaller teacher can win in pretraining, while stronger/post-trained teachers can help in later alignment stages.
3. **Integrated post-training pipelines.** It operationalizes two multi-stage release tracks (instruct and reasoning) with ODPO/GRPO adaptations and explicit mitigation for pathological generation behavior.

### Implications

1. **Broader model-family efficiency (speculative).** If replicated broadly, cascade recipes could lower barrier-to-entry for multi-size open model families by reusing a single high-quality parent.
2. **Stage-specific distillation strategy (moderately supported).** Distillation may need different teacher-selection policies for pretraining versus post-training rather than a one-size-fits-all \"strongest teacher\" heuristic.
3. **Alignment-stack modularity (speculative).** The reported gains from ODPO after RL suggest a compositional approach where reasoning and conversational quality can be tuned in separate stages.

---

## 7. Key Claims

1. **C1:** Cascade Distillation enables competitive family-level pretraining efficiency versus larger from-scratch token budgets (Table 2, Section 1; supported). Scope: base-model comparisons against Qwen3/Gemma3 families. Magnitude: reported 1-3T token budgets vs cited 15T/36T scales.
2. **C2:** 14B retains much teacher capability despite substantial size reduction (Table 3; supported). Scope: teacher-student evaluation on general, math/code, multilingual, multimodal suites. Magnitude: e.g., MMLU-Redux 82.0 vs 82.7, MBPP 71.6 vs 71.6.
3. **C3:** Stronger teacher can underperform smaller teacher for pretraining distillation (Figure 3, Section 5.1; supported). Scope: 14B pretraining ablations in this report. Magnitude: figure trend favors Mistral Small 3.1 teacher.
4. **C4:** Post-trained teacher variants improve student pretraining outcomes on STEM-heavy metrics (Figure 4, Section 5.1; supported). Scope: 3B teacher-variant pretraining ablations. Magnitude: stronger gains reported on math/code, smaller effects on knowledge.
5. **C5:** 14B reasoning outperforms Qwen3 14B on multiple reasoning benchmarks in reported evaluations (Table 5; supported). Scope: pass@16 (pass@5 for LiveCodeBench). Magnitude: AIME 2024 89.8 vs 83.7; AIME 2025 85.0 vs 73.7; GPQA 71.2 vs 66.3.
6. **C6:** Activation-norm-ratio layer scoring is a practical pruning proxy within this cascade setup (Algorithm 2, Section 3.1; supported). Scope: this architecture/training recipe. Magnitude: replaces counterfactual-perplexity ranking in iterative 24B->14B->8B->3B pruning.
7. **C7:** ODPO improves alignment quality and helps mitigate generation artifacts for released models (Section 3.2.2 and Figure 6; supported). Scope: instruction and reasoning post-training stages, especially 14B/8B. Magnitude: figure reports substantial post-ODPO gains on chat benchmarks.

---

## 8. Open Questions

1. How does cascade quality/computation trade off when extending below 3B?
2. Which teacher-student capacity regimes optimize distillation quality at each stage (pretraining vs post-training)?
3. Are the teacher-selection findings stable across other architectures and data distributions?
4. What is effective long-context quality at 256K for complex reasoning, not just benchmark slices?
5. Can verbosity controls preserve reasoning gains while improving conversational naturalness in smaller models?

---

## 9. Core References and Why They Are Referenced

- **Vaswani et al. (2017)**: Transformer backbone used by Ministral 3.
- **Ainslie et al. (2023), Su et al. (2021), Shazeer (2020), Zhang & Sennrich (2019)**: Core architectural blocks (GQA, RoPE, SwiGLU, RMSNorm).
- **Peng et al. (2023), Nakanishi (2025)**: Long-context extension and attention-temperature scaling context.
- **Sun et al. (2023), Sreenivas et al. (2024), Muralidharan et al. (2024)**: Pruning/distillation baselines that motivate cascade choices.
- **Rafailov et al. (2023), Guo et al. (2024), DeepSeek-AI et al. (2025)**: Preference optimization and RL methods used in post-training.
- **Yang et al. (2025), Kamath et al. (2025), Bai et al. (2025)**: Main baseline families for empirical comparison.
