# Appendix C: Task Correlation Analysis [p. 19]

## Validity of Task Categories

RULER is designed under the assumption that tasks across different categories are able to reveal distinct model behaviors [p. 19]. The authors conduct a preliminary correlational study to confirm the validity of task categories and guide the selection of representative tasks [p. 19].

## Methodology

The authors evaluate eight open-sourced models at various context sizes across 18 task configurations [p. 19]. Each task can then be represented with a vector of model performance at various context sizes [p. 19]. The 18 task vectors are then clustered via agglomerative clustering algorithm, using correlation coefficient as the distance metric [p. 19].

## Results

As shown in Figure 5, tasks exhibit moderate correlations with others, tasks in each of the four categories (NIAH, VT, AG, QA) form cohesive clusters of their own without redundancy [p. 19]. The authors further eliminate a few tasks that correlate highly with other tasks within the same cluster, and finalize 13 tasks for later large scale evaluation [p. 19].

**Figure 5** (p. 19): Correlation heatmap among 18 tasks with diverse task configurations

Description: Heatmap showing correlation coefficients between different task configurations
- Key elements: 18x18 correlation matrix with color coding from dark blue (low correlation) to yellow (high correlation)
- Axes: Both x and y axes list the 18 task configurations including:
  - a=2.0 (FWE) and a=3.5 (FWE)
  - squad (QA) and hotpotqa (QA)
  - CWE
  - chain=2, hop=2 (VT) and chain=1, hop=4 (VT)
  - #q=4 (MQ-NIAH)
  - #v=4 (MV-NIAH)
  - #v=2 (MV-NIAH)
  - #q=2 (MQ-NIAH)
  - k=W, v=U, h=essay (S-NIAH)
  - k=W, v=W, h=essay (S-NIAH)
  - #k=4 (MK-NIAH)
  - k=W, v=N, h=essay (S-NIAH)
  - k=W, v=N, h=repeat (S-NIAH)
  - #k=full (MK-NIAH)
  - #k=full, k=U, v=U (MK-NIAH)
- Notable patterns: Tasks within each category (NIAH, VT, AG, QA) show higher correlations (brighter yellow/green) forming diagonal blocks, while cross-category correlations are lower (darker blue)
- Supports claim: Tasks in red text were eliminated as redundant and only 13 representative tasks (in black) were preserved for RULER [p. 19]
- Legend note: W: words; N: numbers; U: UUIDs; Full: entire haystack

The figure demonstrates that the four task categories successfully capture distinct aspects of long-context understanding, validating the benchmark design.
