# 4 Data Statistics and Validation of LongBench Pro [p. 6]

[p. 6] The benchmark is built with a balanced combinatorial design:
- 25 secondary tasks
- 2 languages (EN, ZH)
- 6 length buckets
- 5 samples per combination

Total sample count:
- `25 x 2 x 6 x 5 = 1,500`.

[p. 6] Validation audit procedure:
- 300 uniformly sampled items across tasks, languages, and lengths.
- Two audit axes:
  - attribute correctness (language, length, secondary task, context requirement)
  - answer correctness

[p. 6] Reported audit outcomes:
- Attribute correctness: **99.3%**
- Answer correctness: **97.3%**
- Problematic samples have minor aggregate effect (reported impact: **0.96** score points).

**Figure 4** (p. 6): "Overview of LongBench Pro sample distributions"
- Description: multiple distribution plots over text type, language, context requirement, length, difficulty, and per-task composition.
- Key elements: visibly balanced splits across intended benchmark dimensions.
- Supports claim: dataset construction follows the intended balanced design rather than opportunistic collection.
