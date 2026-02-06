---
title: "Context-Extension Methods: Architectural Taxonomy, Effective Utilization, and the Perplexity--Performance Disconnect"
research_question: "To what extent do different context-extension methods improve effective (rather than claimed) context utilization, and which architectural components do they modify?"
date_produced: 2026-02-05
corpus:
  # Foundational architecture
  - 2017-12-attention-is-all-you-need
  # Position encoding methods
  - 2024-01-roformer-rope
  - 2022-04-alibi-train-short-test-long
  - 2023-06-pi-positional-interpolation
  - 2023-06-rope-ntk
  - 2024-05-yarn-context-extension
  - 2025-12-drope-dropping-positional-embeddings
  - 2022-12-nope-transformers-learn-positions
  - 2023-12-positional-encoding-length-generalization
  - 2025-04-round-and-round-rope
  # Position bias analysis
  - 2024-02-lost-in-the-middle
  - 2025-07-position-bias-transformers
  - 2025-07-position-bias-single-dimension-scaling
  - 2025-11-pos2distill-position-bias-distillation
  - 2024-08-found-in-the-middle
  - 2025-04-pine-eliminating-position-bias
  - 2024-12-lost-in-the-middle-in-between
  # Attention mechanisms and analysis
  - 2020-04-longformer-long-document-transformer
  - 2023-12-landmark-attention-infinite-context
  - 2024-05-attention-sinks-streaming
  - 2025-04-attention-sink-emerges
  - 2023-12-quantizable-transformers-attention-do-nothing
  - 2024-12-transformers-need-glasses-over-squashing
  - 2025-04-retrieval-head-long-context-factuality
  # Memory and compression
  - 2020-04-compressive-transformer-pg19
  - 2025-12-ttt-e2e-long-context
  # Context limitation mechanisms
  - 2021-11-long-range-models-use-context
  - 2018-06-prediction-short-memory
  - 2021-08-context-features-transformer-lm
  - 2025-11-context-length-hurts-performance
  - 2024-08-flenqa-input-length-reasoning
  # Effective context benchmarks
  - 2024-10-ruler-context-size
  - 2024-12-babilong-long-context-reasoning
  - 2025-07-nolima-long-context-evaluation
  - 2024-06-ada-leval-length-adaptable-benchmark
  - 2025-07-longbench-v2
  - 2024-08-infinitebench-long-context-evaluation
  - 2024-08-longbench-bilingual-benchmark
  - 2024-11-genuinely-difficult-long-context
  - 2025-03-longiclbench-long-in-context-learning
  - 2026-01-longbench-pro
  - 2023-11-needle-in-a-haystack
  - 2025-04-effective-context-length-falls-short
  # Model technical reports
  - 2023-02-llama-open-efficient-foundation
  - 2024-07-llama-3-herd-of-models
  - 2024-03-gemini-1.5-long-context
  - 2024-03-yi-open-foundation-models
  - 2024-07-qwen2-technical-report
  - 2025-05-qwen3-technical-report
  - 2024-05-deepseek-v2-moe
  - 2024-12-deepseek-v3-technical-report
  - 2025-03-gemma-3-technical-report
  - 2025-01-kimi-k1.5-scaling-rl
  - 2025-10-kimi-linear-attention
corpus_search_strategy: |
  category context-extension
  category position-encoding
  category attention-efficiency
  category position-bias
  category long-context-evaluation
  text "context extension"
  text "effective context"
  text "positional interpolation"
  text "RoPE"
  text "YaRN"
  text "ALiBi"
  text "STRING"
  text "NTK"
  text "attention sink"
  text "landmark"
  text "NoPE"
  text "over-squashing"
  text "retrieval head"
categories: ["context-extension", "position-encoding", "attention-efficiency", "position-bias", "long-context-evaluation"]
themes:
  - id: architectural-taxonomy
    label: "Taxonomy of architectural components modified by extension methods"
  - id: pe-scaling-effectiveness
    label: "PE scaling methods: perplexity improvement vs effective context gains"
  - id: position-removal
    label: "Position removal as a context extension strategy"
  - id: attention-modifications
    label: "Attention architecture modifications for long context"
  - id: over-squashing-mechanisms
    label: "Over-squashing and representational collapse as fundamental bottlenecks"
  - id: retrieval-heads
    label: "Retrieval heads and their role in long-context factuality"
  - id: training-time-extension
    label: "Training-time context extension and its effectiveness"
  - id: perplexity-effectiveness-disconnect
    label: "The perplexity--effectiveness disconnect"
consensus_claims:
  - claim: "PE scaling methods (PI, NTK, YaRN) reliably improve perplexity at extended context lengths but do not proportionally improve effective context on downstream tasks, especially reasoning"
    sources: ["2024-05-yarn-context-extension", "2024-12-babilong-long-context-reasoning", "2025-07-longbench-v2", "2024-06-ada-leval-length-adaptable-benchmark", "2024-08-infinitebench-long-context-evaluation"]
    strength: strong
  - claim: "All context-extension methods that modify only the positional encoding leave fundamental length-induced reasoning degradation unaddressed"
    sources: ["2025-11-context-length-hurts-performance", "2024-08-flenqa-input-length-reasoning", "2024-12-babilong-long-context-reasoning", "2024-12-transformers-need-glasses-over-squashing"]
    strength: strong
  - claim: "High-frequency RoPE dimensions encode positional patterns (diagonal and previous-token heads) while low-frequency dimensions carry semantic information"
    sources: ["2025-04-round-and-round-rope", "2023-06-rope-ntk", "2024-05-yarn-context-extension"]
    strength: moderate
  - claim: "Causal attention masking is an independent source of position bias beyond positional encodings, causing exponentially fewer information pathways for middle tokens"
    sources: ["2025-07-position-bias-transformers", "2025-04-pine-eliminating-position-bias", "2025-07-position-bias-single-dimension-scaling", "2024-12-transformers-need-glasses-over-squashing"]
    strength: strong
  - claim: "Training-time progressive context extension (Llama 3, Yi, Qwen2/3) produces more robust long-context utilization than post-hoc PE scaling, but effective context still falls substantially short of claimed context"
    sources: ["2024-07-llama-3-herd-of-models", "2024-03-yi-open-foundation-models", "2024-07-qwen2-technical-report", "2025-05-qwen3-technical-report", "2024-10-ruler-context-size", "2025-04-effective-context-length-falls-short", "2026-01-longbench-pro"]
    strength: strong
  - claim: "Position frequency distribution in pretraining data, not the positional encoding scheme itself, is a primary determinant of effective context length"
    sources: ["2025-04-effective-context-length-falls-short", "2024-10-ruler-context-size"]
    strength: moderate
  - claim: "No context-extension method achieves full effective utilization of the extended window on tasks harder than single-fact retrieval with high lexical overlap"
    sources: ["2024-10-ruler-context-size", "2024-12-babilong-long-context-reasoning", "2025-07-nolima-long-context-evaluation", "2025-04-effective-context-length-falls-short", "2026-01-longbench-pro", "2025-03-longiclbench-long-in-context-learning"]
    strength: strong
  - claim: "A sparse set (<5%) of attention heads implement retrieval, and their failure causes hallucination rather than graceful degradation"
    sources: ["2025-04-retrieval-head-long-context-factuality"]
    strength: moderate
  - claim: "Combining multiple context-extension methods (PE scaling + attention modification) produces substantially better results than any single method"
    sources: ["2024-07-qwen2-technical-report", "2025-05-qwen3-technical-report", "2025-03-gemma-3-technical-report"]
    strength: moderate
contested_claims:
  - claim: "Whether PE scaling methods provide genuine context extension or merely redistribute existing capacity"
    for: ["2024-05-yarn-context-extension", "2023-06-pi-positional-interpolation"]
    against: ["2025-12-drope-dropping-positional-embeddings", "2022-04-alibi-train-short-test-long"]
    resolution: "DroPE shows YaRN's zero-shot behavior is equivalent to context cropping (Figure 5). ALiBi's extrapolation gains are primarily from reduced early token curse (Appendix B). After fine-tuning, PI and YaRN do provide genuine extension on perplexity and passkey retrieval, but the extension does not transfer to reasoning tasks (C5 from 2024-12-babilong-long-context-reasoning)."
    resolved: true
  - claim: "Whether positional encodings are necessary for long-context utilization or serve only as a training scaffold"
    for: ["2025-12-drope-dropping-positional-embeddings", "2022-12-nope-transformers-learn-positions", "2025-10-kimi-linear-attention"]
    against: ["2025-04-round-and-round-rope", "2024-01-roformer-rope"]
    resolution: "Both positions have merit. NoPE achieves competitive perplexity, DroPE demonstrates zero-shot extension after PE removal, and Kimi Linear with NoPE+KDA outperforms RoPE variants (RULER 84.3 vs 78.8 at 128K). However, RoPE's high frequencies enable positional heads that NoPE must approximate through multi-head circuits. PEs accelerate training and enable specific head types but are not strictly necessary given sufficient capacity."
    resolved: true
  - claim: "Whether attention mechanism or PE modifications are more effective for context extension"
    for: ["2023-12-landmark-attention-infinite-context", "2025-04-pine-eliminating-position-bias", "2025-10-kimi-linear-attention"]
    against: ["2023-06-pi-positional-interpolation", "2024-05-yarn-context-extension"]
    resolution: "Qwen2/3 and Gemma 3 combine both (YARN+DCA, dual-frequency RoPE) and achieve substantially better results than either alone. Kimi Linear with learnable KDA outperforms both RoPE and NoPE variants. The approaches are complementary rather than competing, but controlled ablations isolating individual contributions are lacking."
    resolved: false
gaps:
  - description: "No study systematically compares all major context-extension methods (PI, NTK, YaRN, DroPE, STRING, Landmark, progressive training) on the same models using the same effective-context benchmarks (RULER, NoLiMa, BABILong)"
    severity: high
  - description: "The interaction between context-extension methods and post-training stages (SFT, RLHF) is minimally explored -- whether fine-tuning undoes or preserves the benefits of extension"
    severity: high
  - description: "No context-extension method has been evaluated on high-dispersion high-scope tasks (Goldman et al. taxonomy) where both information extraction AND integration are difficult"
    severity: high
  - description: "The mechanistic understanding of over-squashing (Barbero et al., 2024-12-transformers-need-glasses-over-squashing) has not been connected to practical mitigation strategies beyond delimiter insertion"
    severity: medium
  - description: "Retrieval head dynamics during context extension are unstudied -- whether extension methods affect retrieval head formation or effectiveness"
    severity: medium
  - description: "Cross-lingual effectiveness of context extension is poorly characterized; LongBench Pro shows systematic English-Chinese asymmetries but causes are unexplored"
    severity: medium
overall_confidence:
  - conclusion: "Context-extension methods improve perplexity and passkey retrieval but do not proportionally extend effective context for reasoning and synthesis"
    level: high
    basis: "12 papers across all major evaluation methodologies; consistent findings for PE-only methods; multi-method combinations partially close the gap"
    caveats: ["STRING and Kimi Linear show substantial RULER improvements but lack NoLiMa/BABILong evaluation", "Most evidence is from 7B-70B scale; frontier models may behave differently"]
  - conclusion: "The effective context bottleneck has multiple independent sources: undertrained positions, attention bias from causal masking, over-squashing, and length-induced reasoning degradation"
    level: high
    basis: "4 independent mechanistic analyses with formal proofs and empirical validation"
    caveats: ["The relative contribution of each source at different scales and architectures is unknown"]
  - conclusion: "Multi-method combinations (PE scaling + attention modification) represent the current best practice for context extension"
    level: moderate
    basis: "Qwen2/3, Gemma 3, and Kimi Linear all combine multiple methods and achieve SOTA results; but no controlled ablations isolate individual contributions"
    caveats: ["Training compute and data confound architecture effects"]
---

# Context-Extension Methods: Architectural Taxonomy, Effective Utilization, and the Perplexity--Performance Disconnect

**Research question:** To what extent do different context-extension methods improve effective (rather than claimed) context utilization, and which architectural components do they modify?
**Corpus:** 51 papers, 2017--2026.
**Categories:** context-extension, position-encoding, attention-efficiency, position-bias, long-context-evaluation.

---

## Executive Summary

- Context-extension methods fall into seven architectural categories: PE function scaling (PI, NTK, YaRN), PE removal (DroPE, NoPE), learnable position encoding (Kimi KDA), attention pattern modification (Longformer, Landmark, DCA), attention bias calibration (Found in the Middle, PINE, positional hidden state scaling), memory compression (Compressive Transformer, StreamingLLM), and training-time progressive extension (Llama 3, Qwen3). Each modifies a different Transformer component, and no single category addresses all sources of effective context limitation (`2024-12-transformers-need-glasses-over-squashing`, `2025-07-position-bias-transformers`, `2025-04-effective-context-length-falls-short`).
- PE scaling methods (PI, NTK, YaRN) reliably reduce perplexity at extended lengths -- YaRN achieves 2.37 perplexity at 128K (`2024-05-yarn-context-extension`) -- but these gains do not transfer proportionally to effective context. BABILong reports that YaRN "fails to extend effective context despite stable perplexity" on reasoning tasks (C5 from `2024-12-babilong-long-context-reasoning`). InfiniteBench shows YaRN-Mistral-7B-128K achieves only 19.96% average, with 0% on Retrieve.KV (`2024-08-infinitebench-long-context-evaluation`).
- Multi-method combinations (PE scaling + attention modification) represent the current best practice. Qwen3 achieves 90.6% RULER at 128K using RoPE ABF + YARN + DCA (`2025-05-qwen3-technical-report`). Qwen2's YARN+DCA improves NeedleBench from 17.13 to 85.21 at 256K for 72B (`2024-07-qwen2-technical-report`). Gemma 3 uses dual-frequency RoPE (10K local, 1M global) with RoPE rescaling factor 8, achieving 91.1% RULER at 32K but degrading to 66.0% at 128K (`2025-03-gemma-3-technical-report`).
- Kimi Linear with NoPE + learnable KDA achieves 84.3% RULER at 128K and 94.8% at 1M, outperforming both RoPE (78.8%) and MLA (81.3%) variants (`2025-10-kimi-linear-attention`). This represents the first evidence that learnable position encoding can outperform explicit PE methods for context extension.
- The position frequency distribution in pretraining data is a primary determinant of effective context. STRING, which replaces undertrained tail positions with well-trained ones, improves Llama 3.1 70B by 15.1 points on RULER at 128K without training (`2025-04-effective-context-length-falls-short`).
- Over-squashing provides a mechanistic explanation for the U-shaped retrieval curve: Barbero et al. prove that causal masking creates exponentially fewer information pathways for middle tokens (Theorem 5.1 from `2024-12-transformers-need-glasses-over-squashing`). Combined with representational collapse at 50--100 tokens in bf16 (Theorem 4.2), this explains why models fail on middle-position retrieval.
- Retrieval heads -- a sparse set of <5% of attention heads -- implement the conditional copy-paste algorithm that underlies NIAH success. Masking these heads causally degrades NIAH performance below 50% (`2025-04-retrieval-head-long-context-factuality`). When retrieval fails, these heads attend to attention sink tokens, producing hallucinations rather than graceful degradation.
- Context length alone degrades reasoning independent of all currently known mechanisms. Du et al. (`2025-11-context-length-hurts-performance`) show 7.9--50% performance drops at 30K tokens even with attention-masked distractors (C3). No context-extension method addresses this mechanism.
- LongBench Pro (`2026-01-longbench-pro`) demonstrates that context optimization outperforms parameter scaling: Qwen3-4B-256K (45.68) > Qwen3-8B (44.34); Qwen3-30B-256K (54.52) > Qwen3-32B (51.12). The benchmark also reveals that MiniMax-Text-01 (4M claimed) scores only 45.00 -- below most 128K models.
- In-context learning (ICL) effective context is even more limited: LongICLBench (`2025-03-longiclbench-long-in-context-learning`) shows open-source models plateau at 7K--14K tokens. On Discovery (174 classes, 50K tokens), all models achieve ~0% except Gemini-1.5-Pro at 14%.

---

## Temporal Evolution

The development of context-extension methods progressed through five phases, each targeting a different architectural bottleneck.

| Date | Paper | Method / Finding | Architectural Component | Shift |
|------|-------|------------------|-------------------------|-------|
| 2017-06 | Vaswani et al. | Original Transformer | Full architecture | Established attention mechanism and sinusoidal PE |
| 2020-04 | Longformer | Sliding window + global attention | Attention pattern | Showed O(n) attention could match full attention on downstream tasks |
| 2020-04 | Compressive Transformer | Memory compression | Memory hierarchy | Demonstrated memory as alternative to attention span |
| 2022-01 | RoFormer | Rotary Position Embedding | PE function | Established RoPE as the dominant PE; enabled all subsequent RoPE-scaling methods |
| 2022-04 | ALiBi | Linear attention biases | PE function | Showed PE choice determines extrapolation; but gains from early-token-curse reduction |
| 2022-12 | NoPE | No positional encoding | PE removal | Showed causal LMs learn positions implicitly |
| 2023-06 | PI | Position index interpolation | PE function | First post-hoc RoPE extension; 16x extension with 1000 fine-tuning steps |
| 2023-06 | NTK-Aware RoPE | Base frequency scaling | PE function | Preserved high-frequency components; enabled zero-shot extension |
| 2023-11 | NIAH | Needle-in-a-haystack evaluation | Evaluation methodology | Revealed GPT-4-128K degrades above 73K despite 128K support |
| 2023-12 | Landmark Attention | Grouped softmax with retrieval tokens | Attention mechanism | Showed attention mechanism itself could perform random-access retrieval |
| 2024-01 | YaRN | NTK-by-parts + temperature scaling | PE function + attention | Unified PI and NTK; SOTA PE-scaling method |
| 2024-02 | Lost in the Middle | U-shaped position bias | Evaluation finding | Established U-shaped curve: 75.8% (1st) → 53.8% (middle) → 63.2% (end) |
| 2024-03 | Yi | RoPE ABF + continual pretraining | PE + training | Extended 4K to 200K with only 5B tokens continual pretraining |
| 2024-05 | StreamingLLM | Attention sink preservation | KV cache | Showed sinks necessary for stable inference, NOT for context extension |
| 2024-07 | Qwen2 | YARN + DCA + RoPE base 10K→1M | PE + attention + training | Combined PE scaling + attention modification; first multi-method combination |
| 2024-07 | Llama 3 | Progressive 8K→128K, theta=500K | Training data + PE | 800B token extension achieves 100% NIAH but limited effective context |
| 2024-10 | RULER | Multi-task synthetic benchmark | Evaluation methodology | Showed near-perfect NIAH hides large effective context gaps |
| 2024-11 | Goldman et al. | Task difficulty taxonomy | Evaluation methodology | Revealed most benchmarks miss high-dispersion high-scope tasks |
| 2024-12 | Transformers Need Glasses | Over-squashing formalization | Mechanistic understanding | Proved representational collapse + exponential path count explains U-shape |
| 2025-03 | Qwen3 | RoPE ABF + YARN + DCA | PE + attention + training | 32K training → 128K inference; RULER 90.6% at 128K |
| 2025-03 | Gemma 3 | Dual-frequency RoPE + rescaling | PE + attention interleaving | 10K local, 1M global; 5:1 local-to-global; RULER 91.1% at 32K, 66.0% at 128K |
| 2025-04 | STRING | Position index replacement | PE manipulation | Identified position frequency as root cause; +15.1 RULER without training |
| 2025-04 | PINE | Bidirectional inter-doc + importance PE | Attention mask + PE | Proved position-invariant inference-time intervention |
| 2025-04 | Retrieval Heads | Sparse retrieval mechanism analysis | Mechanistic understanding | Identified <5% heads responsible for retrieval; failure → hallucination |
| 2025-07 | Position bias emergence | Graph-theoretic analysis | Mechanistic understanding | Proved causal masking converges context to first token regardless of PE |
| 2025-10 | Kimi Linear | NoPE + KDA (learnable) | PE architecture | First learnable PE outperforming explicit PE on long context (RULER 84.3 vs 78.8) |
| 2025-12 | DroPE | Complete PE removal | PE removal + recalibration | Showed PEs are training scaffold; removal enables zero-shot extension |
| 2026-01 | LongBench Pro | Comprehensive bilingual benchmark | Evaluation methodology | Context optimization > parameter scaling; thinking training essential |

### Phase 1: Sparse attention and memory (2020)

The earliest context-extension approaches modified the attention mechanism directly. Longformer (`2020-04-longformer-long-document-transformer`) replaced O(n²) full attention with O(n) sliding window plus task-specific global attention tokens, achieving competitive performance on downstream tasks up to 16K tokens. Global attention is the single most important component -- removing it drops WikiHop by 8.3 points (C3). The Compressive Transformer (`2020-04-compressive-transformer-pg19`) added a secondary compressed memory extending temporal range without increasing attention cost. Neither method was designed for extending pretrained models -- both require training from scratch or continued pretraining.

### Phase 2: PE-centric extension (2022--2024)

The adoption of RoPE by LLaMA (`2023-02-llama-open-efficient-foundation`) made PE modification the dominant extension strategy. PI (`2023-06-pi-positional-interpolation`) demonstrated that rescaling position indices could extend LLaMA's 2048-token window to 32768 with only 1000 fine-tuning steps. NTK-Aware RoPE (`2023-06-rope-ntk`) identified that PI's uniform interpolation destroys high-frequency information, proposing base frequency scaling for zero-shot extension.

YaRN (`2024-05-yarn-context-extension`) unified these approaches with NTK-by-parts interpolation plus attention temperature scaling, achieving SOTA perplexity with 10x fewer tokens than Code Llama. However, the evaluation methodology was limited to perplexity, passkey retrieval, and standard short-context benchmarks. The question of whether these methods improve *effective* context utilization remained unanswered.

### Phase 3: The evaluation reckoning (2024--2025)

NIAH (`2023-11-needle-in-a-haystack`) first revealed the gap between claimed and effective context: GPT-4-128K degrades above 73K tokens despite 128K support, with failure concentrated at 7--50% document depth. RULER (`2024-10-ruler-context-size`) showed that near-perfect NIAH scores masked large degradation on aggregation, variable tracking, and multi-value retrieval (C1). BABILong (`2024-12-babilong-long-context-reasoning`) directly tested YaRN-extended models and found that "context extension methods fail to extend effective context despite stable perplexity" (C5).

InfiniteBench (`2024-08-infinitebench-long-context-evaluation`) extended evaluation beyond 100K tokens, finding that all evaluated models show significant performance degradation. Critically, no consistent "lost-in-the-middle" effect appeared at 100K+ -- position effects became task- and model-specific, complicating the prior understanding. LongICLBench (`2025-03-longiclbench-long-in-context-learning`) showed that in-context learning effective context is even more limited: open-source models plateau at 7K--14K tokens, and grouping same-label demonstrations causes universal degradation (Mistral-7B: -46.5%).

Goldman et al. (`2024-11-genuinely-difficult-long-context`) provided a conceptual framework: most benchmarks target either dispersion (finding information) OR scope (integrating information), not both. The high-dispersion high-scope quadrant -- where genuine long-context capability is required -- is severely under-explored.

### Phase 4: Mechanistic understanding (2024--2025)

Barbero et al. (`2024-12-transformers-need-glasses-over-squashing`) formalized over-squashing for Transformers: Theorem 4.2 proves representational collapse for decoder-only Transformers with causal masking, and Theorem 5.1 shows that causal mask topology creates position-dependent gradient sensitivity bounds -- earlier tokens have exponentially more information pathways to the final token than later tokens. This directly explains the U-shaped retrieval curve.

Wu et al. (`2025-07-position-bias-transformers`) proved that causal masking alone causes cumulative context convergence to the first token regardless of PE type (C1). Liu et al. (`2024-02-lost-in-the-middle`) had earlier documented the U-shaped curve empirically: GPT-3.5-Turbo achieves 75.8% at position 1, 53.8% at position 10, 63.2% at position 20 on 20-document QA.

Wu et al. (`2025-04-retrieval-head-long-context-factuality`) discovered that <5% of attention heads implement a conditional copy-paste algorithm that underlies NIAH success. These retrieval heads are universal across model families and scales. Critically, when retrieval fails, these heads attend to attention sink tokens, producing fluent but unfactual output -- explaining why retrieval failure causes hallucination rather than graceful degradation.

### Phase 5: Multi-method combinations (2025--2026)

The most recent phase shifted from single-method evaluation to multi-method combinations. Qwen2 (`2024-07-qwen2-technical-report`) combined RoPE ABF (base 10K→1M) + YaRN + DCA, achieving dramatic improvements: NeedleBench at 256K improved from 17.13 to 85.21 for 72B. Qwen3 (`2025-05-qwen3-technical-report`) continued this approach with 32K training → 128K inference via YARN+DCA, achieving 90.6% RULER at 128K.

Gemma 3 (`2025-03-gemma-3-technical-report`) introduced dual-frequency RoPE (10K for local layers, 1M for global) with 5:1 local-to-global attention interleaving, reducing KV cache from ~60% to <15% overhead. However, performance degrades rapidly beyond 32K: RULER drops from 91.1% at 32K to 66.0% at 128K.

Kimi Linear (`2025-10-kimi-linear-attention`) represents a paradigm shift: replacing RoPE with NoPE + learnable KDA (Kimi Delta Attention). KDA interprets as a multiplicative positional encoding that relaxes RoPE's orthogonality constraint. Results: RULER 84.3% at 128K (vs 78.8% for RoPE variant, 81.3% for MLA) and 94.8% at 1M with extended training.

LongBench Pro (`2026-01-longbench-pro`) provides the most comprehensive evaluation to date: 46 models on 1,500 naturally occurring bilingual samples. Key finding: context optimization outperforms parameter scaling (Qwen3-4B-256K > Qwen3-8B), and native thinking training is essential for frontier performance.

---

## Thematic Synthesis

### Taxonomy of architectural components modified by extension methods

**Statement:** Context-extension methods modify seven distinct Transformer components, each addressing a different bottleneck.

**Heterogeneity check:** Methods vary in whether they require training (from-scratch, fine-tuning, recalibration, or none). Comparison across categories should account for training compute. Methods also vary in target architecture (encoder-only vs decoder-only, dense vs MoE).

**Evidence table:**

| Method | Paper | Component Modified | Modification Type | Training Required |
|--------|-------|--------------------|-------------------|-------------------|
| PI | `2023-06-pi-positional-interpolation` | RoPE position indices | g(m) = m*L/L' (compress indices) | Fine-tuning (1000 steps) |
| NTK-Aware | `2023-06-rope-ntk` | RoPE base frequency | b' = b * s^(d/(d-2)) | None (zero-shot) |
| YaRN | `2024-05-yarn-context-extension` | RoPE frequencies + attention temperature | NTK-by-parts + sqrt(1/t) scaling | Fine-tuning (400 steps) |
| ALiBi | `2022-04-alibi-train-short-test-long` | PE function | Linear attention biases m*[-(i-1),...,0] | From-scratch |
| DroPE | `2025-12-drope-dropping-positional-embeddings` | PE removal | Drop all RoPE, add QKNorm + temperature | Recalibration (0.5--12.5%) |
| STRING | `2025-04-effective-context-length-falls-short` | RoPE relative position matrix | Drop tail indices, shift, restore locality | None (inference-time) |
| NoPE + KDA | `2025-10-kimi-linear-attention` | PE architecture | Learnable multiplicative encoding | From-scratch (part of pretraining) |
| Longformer | `2020-04-longformer-long-document-transformer` | Attention pattern | Sliding window + global tokens | Continued pretraining |
| Landmark | `2023-12-landmark-attention-infinite-context` | Attention mechanism | Grouped softmax + retrieval tokens | Fine-tuning (15K steps) |
| DCA | `2024-07-qwen2-technical-report` | Attention mechanism | Chunk-based relative position | Inference-time |
| PINE | `2025-04-pine-eliminating-position-bias` | Attention mask + PE | Bidirectional inter-doc + importance sort | None (inference-time) |
| Compressive | `2020-04-compressive-transformer-pg19` | Memory | FIFO + compressed secondary memory | From-scratch |
| StreamingLLM | `2024-05-attention-sinks-streaming` | KV cache | Sink tokens + rolling cache | None (inference-time) |
| Found in Middle | `2024-08-found-in-the-middle` | Attention weights | Calibrate via dummy-document subtraction | None (inference-time) |
| Hidden state scaling | `2025-07-position-bias-single-dimension-scaling` | Hidden states | Scale single positional channel | None (inference-time) |
| Pos2Distill | `2025-11-pos2distill-position-bias-distillation` | Model weights | KL distillation from advantageous positions | Fine-tuning (2 epochs, 250 samples) |
| Progressive training | `2024-07-llama-3-herd-of-models` | Training data + PE | 6-stage 8K→128K + theta=500K | Training (~800B tokens) |
| YARN+DCA+ABF | `2024-07-qwen2-technical-report`, `2025-05-qwen3-technical-report` | PE + attention + training | RoPE base 10K→1M + YaRN + DCA | Pre-training + inference |
| Dual-frequency RoPE | `2025-03-gemma-3-technical-report` | PE + attention interleaving | 10K local, 1M global; 5:1 ratio | Pre-training |

**Cross-paper analysis.** The methods divide into two orthogonal dimensions: (1) which component they modify (PE, attention mechanism, memory, training pipeline, or architecture) and (2) whether they require training. PE-modification methods (PI, NTK, YaRN, STRING) share a common assumption: the bottleneck is in how position indices map to the RoPE frequency space. The attention-modification methods (Longformer, Landmark, PINE, DCA) assume the bottleneck is in how attention distributes over context.

The theoretical analyses from Wu et al. (`2025-07-position-bias-transformers`) and Barbero et al. (`2024-12-transformers-need-glasses-over-squashing`) show both assumptions have merit -- causal masking creates position bias independent of PE (proven in `2025-07-position-bias-transformers` C1), while PE choice determines the rate and form of decay. Additionally, over-squashing creates representational collapse independent of both (`2024-12-transformers-need-glasses-over-squashing` Theorem 4.2).

**Synthesis inference.** [Derived from `2024-12-transformers-need-glasses-over-squashing`, `2025-07-position-bias-transformers`, `2025-04-effective-context-length-falls-short`, `2025-11-context-length-hurts-performance`, `2025-04-retrieval-head-long-context-factuality`.] The effective context bottleneck has at least four independent sources: (1) PE-related undertrained positions, addressable by PE methods; (2) attention-related positional bias from causal masking, addressable by attention methods; (3) over-squashing causing representational collapse, partially addressable by delimiter insertion; and (4) length-induced reasoning degradation from positional distance, not addressed by any current method. Multi-method combinations partially address (1) and (2) simultaneously.

### PE scaling methods: perplexity improvement vs effective context gains

**Statement:** PE scaling methods (PI, NTK, YaRN) reliably improve perplexity and passkey retrieval at extended lengths but their impact on effective context utilization on downstream tasks is substantially smaller and task-dependent.

**Heterogeneity check:** Evaluation metrics vary: perplexity (PG-19, Proof-pile, WikiText), passkey retrieval (exact match), RULER (multi-task average), LongBench (task-weighted average), BABILong (reasoning accuracy). These metrics are not directly comparable -- perplexity measures next-token prediction, RULER measures diverse retrieval/aggregation, BABILong measures multi-hop reasoning.

**Evidence table:**

| Paper | Method | Perplexity Result | Passkey Result | Effective Context Result |
|-------|--------|-------------------|----------------|--------------------------|
| `2023-06-pi-positional-interpolation` | PI (s=16, 7B) | 6.77 at 32K | 100% at L' after 200 steps | Not evaluated |
| `2023-06-rope-ntk` | NTK-Aware (zero-shot) | Near-normal within pretrained range | Not evaluated | Not evaluated |
| `2024-05-yarn-context-extension` | YaRN (s=32, 7B) | 2.37 at 128K Proof-pile | 99.4% at 128K | ARC-c 52.3, MMLU 42.5 (slight drops) |
| `2024-12-babilong-long-context-reasoning` | YaRN (evaluated) | Stable perplexity | Not reported | "Fails to extend effective context" (C5) |
| `2024-08-infinitebench-long-context-evaluation` | YaRN-Mistral-7B-128K | Not reported | 100% PassKey | 19.96% average, 0% Retrieve.KV |
| `2025-07-longbench-v2` | YaRN (s=4, Qwen2.5) | Not reported | Not reported | +4.7 overall (retrieval-concentrated) |
| `2024-06-ada-leval-length-adaptable-benchmark` | NTK-Aware / ReRoPE | Not reported | Not reported | Collapse to 0% at 64K+ on BestAnswer |
| `2025-04-effective-context-length-falls-short` | STRING | Not primary | NIAH 85.7% vs 67.8% RoPE | RULER 128K: +15.1 (Llama 3.1 70B) |

**Cross-paper analysis.** The disconnect between perplexity and downstream performance is the most consistent finding. YaRN achieves 2.37 perplexity at 128K on Proof-pile (`2024-05-yarn-context-extension` C4), suggesting near-perfect language modeling. Yet BABILong (`2024-12-babilong-long-context-reasoning`) reports that YaRN-extended models show no improvement on multi-fact reasoning (C5). InfiniteBench (`2024-08-infinitebench-long-context-evaluation`) provides the most damning evidence: YaRN-Mistral-7B-128K achieves 100% on PassKey but 0% on Retrieve.KV and only 19.96% average.

STRING (`2025-04-effective-context-length-falls-short`) achieves the largest effective context improvement among PE-manipulation methods: +15.1 points on RULER for Llama 3.1 70B. STRING differs from PI/NTK/YaRN in that it does not interpolate or scale frequencies but instead replaces undertrained position indices with well-trained ones. This suggests that the position frequency problem is more important than the frequency interpolation problem. However, STRING's largest gain is on NIAH-like retrieval (78.9 to 92.7, +13.8) compared to aggregation (39.8 to 50.0, +10.2).

The mechanistic explanation from Barbero et al. (`2025-04-round-and-round-rope`) clarifies why PE scaling has limited downstream impact: RoPE does not decay attention with distance as commonly assumed (C1, C2) -- the decay is a property of trained weights, not the encoding itself.

**Current state.** PE scaling methods provide genuine extension for perplexity and passkey retrieval but their impact on effective context for reasoning and aggregation is limited. STRING's approach of targeting undertrained positions is more effective but still insufficient for reasoning tasks. As of 2026, no PE-only method closes the effective context gap on tasks requiring information integration.

### Position removal as a context extension strategy

**Statement:** Removing positional encodings entirely after pretraining is a viable context extension strategy, and learnable position encodings can outperform explicit PE methods.

**Evidence table:**

| Paper | Method | Key Finding | Scope |
|-------|--------|-------------|-------|
| `2022-12-nope-transformers-learn-positions` | NoPE (from scratch) | Competitive perplexity (gap 0.05 at 1.3B); implicit positional information from causal mask | 125M--1.3B |
| `2023-12-positional-encoding-length-generalization` | NoPE (from scratch) | NoPE outperforms all explicit PEs on length generalization (MRR 0.69 vs 0.55 next-best) | 107M on synthetic; 1.3B perplexity |
| `2025-12-drope-dropping-positional-embeddings` | DroPE | Outperforms PI, NTK, YaRN on zero-shot (LongBench 30.52 vs 19.94 YaRN) | 360M--7B |
| `2025-04-round-and-round-rope` | Mechanistic analysis | NoPE cannot learn single-head positional patterns; multi-head workaround required | Gemma 7B, 2B |
| `2025-10-kimi-linear-attention` | NoPE + KDA (learnable) | RULER 84.3% at 128K (vs RoPE 78.8%, MLA 81.3%); 94.8% at 1M | 48B-A3B MoE |

**Cross-paper analysis.** DroPE (`2025-12-drope-dropping-positional-embeddings`) provides strong practical evidence that PEs are a training scaffold: by removing all RoPE after pretraining and recalibrating for 0.5--12.5% of pretraining budget, DroPE substantially outperforms PE-scaling baselines on zero-shot extension (LongBench 30.52 vs 19.94 for YaRN, C4). The key finding is that YaRN's zero-shot behavior is equivalent to context cropping (C3).

Kimi Linear (`2025-10-kimi-linear-attention`) advances beyond PE removal to learnable position encoding. KDA (Kimi Delta Attention) interprets as a multiplicative positional encoding with data-dependent, learnable transition matrices that relax RoPE's orthogonality constraint. Results show NoPE + KDA outperforms both RoPE variants and full MLA attention on RULER at 128K (84.3% vs 78.8% vs 81.3%) and achieves 94.8% at 1M with extended training.

However, Barbero et al. (`2025-04-round-and-round-rope`) prove that NoPE cannot learn diagonal or off-diagonal attention patterns in a single head (Proposition 5.2, C5). RoPE's high-frequency dimensions enable positional heads that NoPE must approximate through multi-head circuits.

**Current state.** Position removal is effective for zero-shot extension up to 7B. Learnable position encoding (Kimi KDA) achieves SOTA effective context at 128K+ and represents a promising direction. The key question is whether learnable PEs scale to larger dense models and whether they can be retrofitted to existing RoPE models.

### Over-squashing and representational collapse as fundamental bottlenecks

**Statement:** Over-squashing and representational collapse impose fundamental limits on context extension that are independent of positional encoding choice.

**Evidence table:**

| Paper | Finding | Evidence |
|-------|---------|----------|
| `2024-12-transformers-need-glasses-over-squashing` | Representational collapse: distinct inputs produce arbitrarily close final-token representations as sequence grows | Theorem 4.2; collapse at 50--100 tokens in bf16 |
| `2024-12-transformers-need-glasses-over-squashing` | Causal mask creates position-dependent gradient sensitivity: earlier tokens have exponentially more information pathways | Theorem 5.1; path counting explains U-shape |
| `2024-02-lost-in-the-middle` | U-shaped retrieval: 75.8% (position 1) → 53.8% (position 10) → 63.2% (position 20) | GPT-3.5-Turbo 20-doc QA |
| `2025-07-position-bias-transformers` | Causal masking alone causes context convergence to first token regardless of PE | C1, formal proof |
| `2023-12-quantizable-transformers-attention-do-nothing` | Softmax cannot produce exact zeros; no-op heads concentrate on low-information tokens | >97% BERT outliers at delimiters |

**Cross-paper analysis.** Barbero et al. (`2024-12-transformers-need-glasses-over-squashing`) provide the most complete mechanistic explanation for the U-shaped retrieval curve. Theorem 5.1 shows that the gradient bound from token i to final token n is proportional to the path count from i to n through the causal mask graph. Early tokens benefit from exponentially more pathways (primacy bias); late tokens benefit from recency during autoregressive training; middle tokens suffer both moderate path count and lack of recency bias.

The practical implication is that delimiter insertion -- which maintains representational separation -- is the only mitigation strategy demonstrated in the corpus. Gemini 1.5 fails at last-element copying beyond ~300 tokens (`2024-12-transformers-need-glasses-over-squashing`), showing that even frontier models are affected.

The connection to softmax limitations (`2023-12-quantizable-transformers-attention-do-nothing`) reveals that attention heads attempting to not update the residual concentrate on low-information tokens (delimiters, punctuation), creating outliers. Gated attention with per-head sigmoid gates provides a potential solution that works across architectures.

**Current state.** Over-squashing is a fundamental architectural limitation that no current context-extension method directly addresses. Delimiter insertion is the only demonstrated mitigation but has not been systematically evaluated as a context-extension strategy.

### Retrieval heads and their role in long-context factuality

**Statement:** A sparse set of <5% of attention heads implement the retrieval mechanism that underlies NIAH success, and their failure causes hallucination rather than graceful degradation.

**Evidence table:**

| Paper | Finding | Evidence |
|-------|---------|----------|
| `2025-04-retrieval-head-long-context-factuality` | <5% of heads implement conditional copy-paste algorithm for retrieval | Retrieval score metric; universal across 4 families, 6 scales |
| `2025-04-retrieval-head-long-context-factuality` | Masking retrieval heads causally degrades NIAH below 50% | All models at K=50 heads masked |
| `2025-04-retrieval-head-long-context-factuality` | Failed retrieval → heads attend to attention sinks → hallucination | GSM8K accuracy drops 45.1% → 2.0% |
| `2024-05-attention-sinks-streaming` | Attention sinks are necessary for stable inference, not information | C2, C7: accuracy drops to zero beyond cache size |

**Cross-paper analysis.** Wu et al. (`2025-04-retrieval-head-long-context-factuality`) identify retrieval heads through a retrieval score metric measuring the fraction of needle tokens a head copy-pastes during decoding. These heads are intrinsic to base models (Pearson r > 0.8 within families across fine-tuning) and universal across Llama, Yi, Qwen, and Mistral families from 6B to 34B.

The connection to attention sinks (`2024-05-attention-sinks-streaming`) is critical: when retrieval fails, retrieval heads attend to initial position sink tokens, producing fluent but unfactual output. This explains why retrieval failure causes hallucination (the model generates plausible-sounding but incorrect answers) rather than abstention or error signals.

**Current state.** Retrieval heads provide a mechanistic target for context-extension research. No paper has evaluated whether context-extension methods affect retrieval head formation, effectiveness, or failure modes. This represents a significant gap.

### Training-time context extension and its effectiveness

**Statement:** Training-time approaches produce more robust long-context models than inference-time PE modification, but effective context still falls substantially short of claimed context.

**Evidence table:**

| Paper | Method | Training Cost | Claimed | Effective (benchmark, result) |
|-------|--------|---------------|---------|-------------------------------|
| `2024-07-llama-3-herd-of-models` | Progressive 8K→128K, theta=500K | ~800B tokens | 128K | NIAH: 100%. RULER (via `2024-10-ruler-context-size`): 64K effective for 70B |
| `2024-03-gemini-1.5-long-context` | Undisclosed architecture | Undisclosed | 10M | NIAH: >99% at 10M. NoLiMa: effective 2K |
| `2024-03-yi-open-foundation-models` | RoPE ABF + 5B continual pretraining | 5B tokens | 200K | NIAH: near-perfect. No RULER/NoLiMa evaluation |
| `2024-07-qwen2-technical-report` | YARN+DCA+ABF | Pre-training phase | 131K | NeedleBench 256K: 85.21 (72B). No RULER |
| `2025-05-qwen3-technical-report` | RoPE ABF + YARN+DCA | 30T+ tokens | 128K | RULER: 90.6% at 128K (non-thinking) |
| `2025-03-gemma-3-technical-report` | Dual-frequency RoPE + rescaling | Pre-training | 128K | RULER: 91.1% at 32K, 66.0% at 128K |
| `2024-05-deepseek-v2-moe` | Decoupled RoPE + YaRN | 8.1T tokens | 128K | No RULER/NIAH evaluation |
| `2024-12-deepseek-v3-technical-report` | YaRN on decoupled key | 14.8T tokens + 2000 steps | 128K | NIAH: perfect |
| `2025-10-kimi-linear-attention` | NoPE + KDA | 5.7T tokens | 1M | RULER 128K: 84.3%; RULER 1M: 94.8% |

**Cross-paper analysis.** Llama 3's progressive extension (`2024-07-llama-3-herd-of-models`) represents the most thorough training-time approach: 6 stages from 8K to 128K over ~800B tokens. The result is 100% NIAH but RULER evaluation (`2024-10-ruler-context-size`) shows only 64K effective context for 70B -- 50% of claimed.

Gemini 1.5 Pro (`2024-03-gemini-1.5-long-context`) achieves >99% NIAH at 10M tokens but NoLiMa (`2025-07-nolima-long-context-evaluation`) reveals effective length of only 2K on latent-association tasks -- a 0.02% effective-to-claimed ratio.

Qwen3 (`2025-05-qwen3-technical-report`) achieves the best RULER results: 90.6% at 128K in non-thinking mode. Notably, thinking mode degrades RULER performance (92.2% vs 95.0% average), suggesting that extended reasoning tokens may compete with context for effective window.

Gemma 3 (`2025-03-gemma-3-technical-report`) shows rapid degradation beyond 32K: RULER drops from 91.1% at 32K to 66.0% at 128K. The dual-frequency approach (10K local, 1M global) with 5:1 interleaving reduces KV cache overhead but does not prevent degradation.

LongBench Pro (`2026-01-longbench-pro`) provides the most comprehensive evaluation: context optimization outperforms parameter scaling. Qwen3-4B-256K (45.68) > Qwen3-8B (44.34); Qwen3-30B-256K (54.52) > Qwen3-32B (51.12). Native thinking training is essential: Claude-4-Sonnet gains +13.80 with thinking, while Llama-3.1-405B gains only +0.59.

**Current state.** Training-time extension with multi-method combinations (PE scaling + attention modification) produces the most capable long-context models. Qwen3 achieves 90.6% RULER at 128K; Kimi Linear achieves 94.8% at 1M. However, effective context still falls short of claimed for all models, and the gap widens for tasks requiring synthesis rather than retrieval.

### The perplexity--effectiveness disconnect

**Statement:** Perplexity improvement at extended context lengths is a necessary but not sufficient condition for effective context utilization.

**Evidence table:**

| Paper | Finding | Evidence |
|-------|---------|----------|
| `2024-05-yarn-context-extension` | YaRN achieves 2.37 perplexity at 128K | Table 2, C4 |
| `2024-12-babilong-long-context-reasoning` | YaRN "fails to extend effective context despite stable perplexity" | C5 |
| `2024-08-flenqa-input-length-reasoning` | Next-word prediction correlates negatively with reasoning (rho = -0.95, p = 0.01) | C5 |
| `2024-08-infinitebench-long-context-evaluation` | YaRN-Mistral: 100% PassKey, 0% Retrieve.KV, 19.96% average | Table 2 |
| `2025-12-drope-dropping-positional-embeddings` | YaRN's zero-shot extension is equivalent to context cropping | C3 |
| `2024-06-ada-leval-length-adaptable-benchmark` | Models distinguish orderings via perplexity (89.2%) but fail generatively (5.4%) | C3 |
| `2018-06-prediction-short-memory` | Bounded mutual information implies short-window Markov models match optimal prediction | Proposition 1, Corollary 1 |
| `2021-11-long-range-models-use-context` | Long-range context provides negligible aggregate perplexity benefit beyond token copying | Main finding |

**Cross-paper analysis.** The perplexity--effectiveness disconnect is supported by 8 independent papers. InfiniteBench (`2024-08-infinitebench-long-context-evaluation`) provides the starkest evidence: YaRN-Mistral-7B-128K achieves 100% on PassKey (synthetic retrieval) but 0% on Retrieve.KV (key-value lookup) and only 19.96% overall average.

The theoretical foundation comes from Khandelwal et al. (`2018-06-prediction-short-memory`): bounded mutual information between past and future implies short-window Markov models can match optimal prediction. This explains why perplexity plateaus despite increasing context -- average prediction error is insensitive to the time scale of dependencies.

Sun et al. (`2021-11-long-range-models-use-context`) confirm empirically that long-range context provides negligible aggregate perplexity benefit beyond token copying. O'Connor and Andreas (`2021-08-context-features-transformer-lm`) show that content words carry most usable information, and complete word shuffling removes only 41% (mid-range) to 84% (long-range) of usable information -- suggesting models rely primarily on local co-occurrence.

**Current state.** Perplexity is an unreliable proxy for effective context and should not be the primary metric for context-extension evaluation. The field has adopted multi-task benchmarks (RULER, LongBench, BABILong) as standard, but even these may miss high-dispersion high-scope tasks per Goldman et al.'s taxonomy (`2024-11-genuinely-difficult-long-context`).

---

## Consensus and Disagreements

### Consensus

**Claim:** PE scaling methods reliably improve perplexity at extended lengths but do not proportionally improve effective context utilization on downstream tasks.
**Supporting papers:** `2024-05-yarn-context-extension`, `2024-12-babilong-long-context-reasoning`, `2025-07-longbench-v2`, `2024-06-ada-leval-length-adaptable-benchmark`, `2025-04-effective-context-length-falls-short`, `2024-08-infinitebench-long-context-evaluation`.
**Evidence strength:** strong (6 papers, 4 independent evaluation methodologies).
**Qualification:** STRING achieves substantial RULER improvements by targeting position frequency rather than PE interpolation. Multi-method combinations (Qwen2/3, Gemma 3) partially close the gap.

**Claim:** Causal attention masking is an independent source of position bias beyond PEs, causing exponentially fewer information pathways for middle tokens.
**Supporting papers:** `2025-07-position-bias-transformers`, `2025-04-pine-eliminating-position-bias`, `2025-07-position-bias-single-dimension-scaling`, `2024-12-transformers-need-glasses-over-squashing`.
**Evidence strength:** strong (4 papers; Wu et al. and Barbero et al. provide formal proofs).
**Qualification:** The relative magnitude of causal-mask bias vs PE bias depends on model depth and architecture.

**Claim:** Context length alone degrades reasoning independent of retrieval quality.
**Supporting papers:** `2025-11-context-length-hurts-performance`, `2024-12-babilong-long-context-reasoning`, `2024-08-flenqa-input-length-reasoning`.
**Evidence strength:** strong (3 papers with systematic controls; Du et al. isolate the effect with attention-masked distractors).
**Qualification:** Closed-source models are more robust (GPT-4o shows 0% degradation with whitespace padding), suggesting trainable mitigation.

**Claim:** No context-extension method achieves full effective utilization on tasks harder than single-fact retrieval with high lexical overlap.
**Supporting papers:** `2024-10-ruler-context-size`, `2024-12-babilong-long-context-reasoning`, `2025-07-nolima-long-context-evaluation`, `2025-04-effective-context-length-falls-short`, `2026-01-longbench-pro`, `2025-03-longiclbench-long-in-context-learning`.
**Evidence strength:** strong (6 papers across all major benchmark methodologies).
**Qualification:** Kimi Linear achieves 94.8% RULER at 1M, but RULER is retrieval-focused; NoLiMa and BABILong evaluation is lacking.

**Claim:** Multi-method combinations (PE scaling + attention modification) produce substantially better results than single methods.
**Supporting papers:** `2024-07-qwen2-technical-report`, `2025-05-qwen3-technical-report`, `2025-03-gemma-3-technical-report`.
**Evidence strength:** moderate (3 papers; no controlled ablations isolating individual contributions).
**Qualification:** Training compute and data confound architecture effects.

### Active Disagreements

**Claim:** Whether attention mechanism or PE modifications are more effective for context extension.
**Position A (`2023-12-landmark-attention-infinite-context`, `2025-04-pine-eliminating-position-bias`, `2025-10-kimi-linear-attention`):** Attention modifications address the retrieval mechanism directly. Kimi Linear with learnable KDA outperforms RoPE variants.
**Position B (`2023-06-pi-positional-interpolation`, `2024-05-yarn-context-extension`, `2025-04-effective-context-length-falls-short`):** PE modifications are simpler and more general. STRING achieves +15.1 RULER with no training.
**Methodological differences:** Different evaluation metrics (perplexity vs RULER vs multi-doc QA), different model scales, different training compute.
**Assessment:** Unresolved. The methods target different bottlenecks and are likely complementary rather than competing. Qwen2/3 and Gemma 3 combine both approaches.
**Resolution path:** Controlled ablation study comparing PE-only, attention-only, and combined modifications on identical base models across RULER, NoLiMa, and BABILong.

---

## Methodological Patterns

### Common experimental setups

PE-scaling methods are evaluated primarily on LLaMA/Llama families at 7B--13B scale using perplexity and passkey retrieval. Effective-context evaluation (RULER, BABILong, NoLiMa) is used by benchmark papers but not by most method papers. The most commonly tested model is Llama 2/3 7B/8B (appears in 25+ papers).

### Methodological strengths

An et al. (`2025-04-effective-context-length-falls-short`) set the gold standard: causal analysis (controlled pretraining with position frequency measurement) + multi-benchmark evaluation (NIAH, RULER, InfiniteBench) + training-free intervention (STRING). Barbero et al. (`2024-12-transformers-need-glasses-over-squashing`) provide formal proofs for all main claims with empirical verification. LongBench Pro (`2026-01-longbench-pro`) evaluates 46 models on 1,500 naturally occurring samples with difficulty calibration.

### Methodological weaknesses

1. **Method papers do not evaluate effective context.** Of the method papers proposing context extension (PI, NTK, YaRN, DroPE, Landmark), none evaluates on RULER, NoLiMa, or BABILong.
2. **No controlled cross-method comparisons.** No paper compares all major methods on the same models with the same benchmarks.
3. **Scale limitations.** DroPE evaluated to 7B, PINE to 70B, sigmoid attention to 1B. Kimi Linear is 48B-A3B MoE; dense model scaling unclear.
4. **High-dispersion high-scope tasks under-explored.** Per Goldman et al. (`2024-11-genuinely-difficult-long-context`), most benchmarks test either retrieval (dispersion) or integration (scope), not both.
5. **No variance estimates.** Most papers report single-run results without confidence intervals.

### Benchmark coverage matrix

| Paper | Perplexity | Passkey | NIAH | RULER | BABILong | NoLiMa | LongBench | InfiniteBench | LongBench Pro |
|-------|-----------|---------|------|-------|----------|--------|-----------|---------------|---------------|
| `2023-06-pi-positional-interpolation` | x | x | | | | | | | |
| `2024-05-yarn-context-extension` | x | x | | | | | | | |
| `2025-12-drope-dropping-positional-embeddings` | | | x | | | | x | | |
| `2025-04-effective-context-length-falls-short` | | x | x | x | | | | x | |
| `2024-07-llama-3-herd-of-models` | | x | x | | | | | x | |
| `2024-03-gemini-1.5-long-context` | | x | x | | | | | | |
| `2025-05-qwen3-technical-report` | | | x | x | | | | | |
| `2025-03-gemma-3-technical-report` | | | | x | | | | | |
| `2025-10-kimi-linear-attention` | | | | x | | | | | |
| `2024-10-ruler-context-size` | | | | x | | | | | |
| `2024-12-babilong-long-context-reasoning` | | | | | x | | | | |
| `2025-07-nolima-long-context-evaluation` | | | | | | x | | | |
| `2026-01-longbench-pro` | | | | | | | | | x |
| `2024-08-infinitebench-long-context-evaluation` | | x | | | | | | x | |
| `2024-08-longbench-bilingual-benchmark` | | | | | | | x | | |

---

## Gaps and Open Questions

1. **No unified evaluation of context-extension methods on effective-context benchmarks.**
   **Description:** Of the 15+ methods surveyed, none has been evaluated on the full suite of RULER, NoLiMa, and BABILong. STRING has RULER and InfiniteBench; Kimi Linear has RULER; no method has NoLiMa or BABILong.
   **Severity:** high.
   **Potential approach:** Standardized evaluation protocol applying all major methods to identical base models across RULER, NoLiMa, and BABILong.

2. **High-dispersion high-scope tasks are under-explored.**
   **Description:** Per Goldman et al.'s taxonomy (`2024-11-genuinely-difficult-long-context`), most benchmarks miss the quadrant requiring both difficult information extraction AND integration. Book summarization and complex reasoning represent this quadrant but are rarely used.
   **Severity:** high.
   **Potential approach:** Develop benchmarks explicitly targeting high-dispersion high-scope tasks, building on LongBench Pro's difficulty calibration methodology.

3. **Over-squashing mitigation beyond delimiter insertion is unexplored.**
   **Description:** Barbero et al. (`2024-12-transformers-need-glasses-over-squashing`) prove over-squashing causes representational collapse, with delimiter insertion as the only demonstrated mitigation. Systematic evaluation of delimiter strategies as context-extension methods is lacking.
   **Severity:** medium.
   **Potential approach:** Evaluate delimiter insertion variants (frequency, type, position) on RULER and reasoning benchmarks.

4. **Retrieval head dynamics during context extension are unstudied.**
   **Description:** Wu et al. (`2025-04-retrieval-head-long-context-factuality`) identify retrieval heads as critical for NIAH success, but no paper evaluates whether context-extension methods affect retrieval head formation, count, or effectiveness.
   **Severity:** medium.
   **Potential approach:** Apply retrieval score metric to models before and after PE scaling, training-time extension, and attention modification.

5. **Post-training interaction with context extension is minimally explored.**
   **Description:** SFT and RLHF use predominantly short-context data. Whether fine-tuning preserves or undoes extension benefits is unknown. Llama 3 uses 0.1% synthetic long-context SFT data; Kimi K1.5 (`2025-01-kimi-k1.5-scaling-rl`) shows RL benefits from 128K context, but systematic study is lacking.
   **Severity:** high.
   **Potential approach:** Controlled experiments applying SFT/RLHF with varying proportions of long-context data to extended models.

6. **Learnable position encoding scaling is unknown.**
   **Description:** Kimi Linear (`2025-10-kimi-linear-attention`) shows learnable KDA outperforms RoPE at 48B-A3B MoE scale. Whether this generalizes to large dense models and whether KDA can be retrofitted to existing RoPE models is untested.
   **Severity:** medium.
   **Potential approach:** Apply KDA or similar learnable PE to dense models at 7B--70B scale; evaluate retrofit strategies.
