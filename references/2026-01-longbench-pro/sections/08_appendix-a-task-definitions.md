# Appendix A. Task Definitions [p. 16-20]

[p. 16-20] Appendix A provides task-by-task I/O templates with required answer formatting (`[Answer]` marker, line-by-line output), context requirement (Full/Partial), and metric.

## T1 Retrieval & Ranking [p. 16]
- T1.1 Global Cohesive Retrieval (Full, NDCG@k): retrieve and reorder global content.
- T1.2 Key-Snippet Retrieval (Partial, NDCG@k): locate target fragment in specified paragraph.

## T2 Sequencing & Structure Reconstruction [p. 16]
- T2.1 Global Timeline Reconstruction (Full, Pairwise Accuracy): recover event order across full text.
- T2.2 Local Causal Chain Sorting (Partial, Pairwise Accuracy): reorder local paragraph content.

## T3 Evidence-Grounded QA [p. 16-17]
- T3.1 Multi-Doc Integration QA (Full, Accuracy): multi-hop evidence integration.
- T3.2 Single-Hop Fact QA (Partial, Accuracy): local evidence lookup.

## T4 Summarization & Synthesis [p. 17]
- T4.1 Global-Coverage Constrained Summary (Full, `0.5*max(SemSim)+0.5*max(ROUGE-L)`).
- T4.2 Query-Focused Summary (Partial, same metric).

## T5 Attribution & Citation Alignment [p. 17]
- T5.1 Full-Sentence Citation Alignment (Full, F1).
- T5.2 Key-Statement Citation Alignment (Partial, F1).

## T6 Aggregation & Clustering [p. 18]
- T6.1 Large-Scale Document Clustering (Full, SubEM).
- T6.2 Targeted Subset Cluster Identification (Partial, F1).
- T6.3 Global Frequency Analysis (Full, Pairwise Accuracy).

## T7 Consistency & Compliance Checking [p. 18]
- T7.1 Global Conflict & Inconsistency Localization (Full, F1).
- T7.2 Targeted Rule or Condition Violation Detection (Partial, F1).
- T7.3 Comprehensive Error & Anomaly Sweep (Full, F1).

## T8 Structured & Numeric Reasoning [p. 19]
- T8.1 Structured Multi-Source Consistency Verification (Full, SubEM).
- T8.2 Single-Source Targeted Aggregation (Partial, SubEM).
- T8.3 Long-Context Procedural State Tracking (Full, F1 in appendix examples).

## T9 Version & Code Diff Analysis [p. 19]
- T9.1 Dependency-Aware Multi-Version Impact Analysis (Full, F1).
- T9.2 Localized Interface Change Detection (Partial, F1).

## T10 Rule Induction & In-Context Learning [p. 20]
- T10.1 Large-Scale In-Context Rule Induction (Full, SubEM).
- T10.2 Targeted Example-Based Rule Induction (Partial, SubEM).

## T11 Dialogue Memory & Long-Horizon Tracking [p. 20-21]
- T11.1 Long-Range Entity & Commitment Tracking (Full, Accuracy).
- T11.2 Short-Range Reference Resolution & State Query (Partial, Accuracy).

[p. 16-20] Across all tasks, Appendix A enforces strict output-structure regularity to support automated evaluation and reduce parsing ambiguity.
