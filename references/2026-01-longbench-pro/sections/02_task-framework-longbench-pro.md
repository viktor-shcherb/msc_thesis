# 2 Task Framework of LongBench Pro [p. 3-4]

[p. 3] The benchmark organizes long-context evaluation with a two-level taxonomy:
- 11 primary task families.
- 25 secondary tasks formed by combining task family with context requirement (Full vs Partial).

[p. 3] Context-requirement definition:
- **Full**: solving requires integration across multiple distant spans.
- **Partial**: solving mainly uses localized spans.

[p. 3] The paper states that this taxonomy covers capability dimensions represented across existing benchmarks (Figure 2) and adds explicit multi-dimensional categorization.

## Table 1: Comparison of long-context benchmarks [p. 3]

| Benchmark | Text Type | #Task | Metric | Language | Ctx-Req | Length | Difficulty |
|---|---|---:|---|---|---|---|---|
| RULER (Hsieh et al., 2024) | Fully Synthetic | 4 | Single | EN | absent | absent | absent |
| InfinityBench (Zhang et al., 2024) | Synthetic, Natural | 6 | Diverse | EN, ZH | absent | absent | absent |
| CLongEval (Qiu et al., 2024) | Synthetic, Natural | 7 | Diverse | ZH | absent | absent | absent |
| HELMET (Yen et al., 2024) | Synthetic, Natural | 7 | Diverse | EN | absent | absent | absent |
| LongBench v2 (Bai et al., 2025) | Fully Natural | 6 | Single | EN | coarse | coarse | coarse |
| **LongBench Pro (Ours)** | **Fully Natural** | **11** | **Diverse** | **EN, ZH** | **detailed** | **detailed** | **detailed** |

[p. 4] Full task list (Table 2) with metric assignment:

| Primary Task | Representative Secondary Tasks | Context Split | Metric(s) |
|---|---|---|---|
| T1 Retrieval & Ranking | T1.1 Global cohesive retrieval; T1.2 key-snippet retrieval | Full + Partial | NDCG@k |
| T2 Sequencing & Structure Reconstruction | T2.1 global timeline; T2.2 local causal-chain sorting | Full + Partial | Pairwise Accuracy |
| T3 Evidence-Grounded QA | T3.1 multi-doc integration QA; T3.2 single-hop fact QA | Full + Partial | Accuracy |
| T4 Summarization & Synthesis | T4.1 global constrained summary; T4.2 query-focused summary | Full + Partial | SemSim, ROUGE-L |
| T5 Attribution & Citation Alignment | T5.1 full-sentence alignment; T5.2 key-statement alignment | Full + Partial | F1 |
| T6 Aggregation & Clustering | T6.1 large-scale clustering; T6.2 targeted subset; T6.3 global frequency | Mixed | SubEM, F1, Pairwise Accuracy |
| T7 Consistency & Compliance Checking | T7.1 global conflicts; T7.2 targeted rule violation; T7.3 anomaly sweep | Mixed | F1 |
| T8 Structured & Numeric Reasoning | T8.1 multi-source verification; T8.2 targeted aggregation; T8.3 procedural state tracking | Mixed | SubEM |
| T9 Version & Code Diff Analysis | T9.1 dependency-aware impact; T9.2 localized interface changes | Full + Partial | F1 |
| T10 Rule Induction & In-Context Learning | T10.1 large-scale rule induction; T10.2 targeted rule induction | Full + Partial | SubEM |
| T11 Dialogue Memory & Long-Horizon Tracking | T11.1 long-range entity/commitment; T11.2 short-range reference/state query | Full + Partial | Accuracy |

**Figure 2** (p. 3): "Task mapping between LongBench Pro and existing benchmarks"
- Description: mapping diagram from prior benchmark task spaces into the LongBench Pro taxonomy.
- Key elements: cross-benchmark capability alignment, showing LongBench Pro as superset coverage.
- Supports claim: LongBench Pro spans the core capability dimensions present in prior long-context benchmarks.
