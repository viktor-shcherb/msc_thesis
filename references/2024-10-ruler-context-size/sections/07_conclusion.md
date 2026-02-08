# Conclusion [p. 10]

[p. 10] The authors present RULER, a synthetic benchmark for evaluating long-context language models. RULER contains diverse task categories: *retrieval*, *multi-hop tracing*, *aggregation*, and *question answering*, providing a flexible and comprehensive evaluation of LLM's long-context capabilities. The authors benchmark 17 long-context LMs using RULER with context sizes ranging from 4K to 128K.

Key conclusions:
- Despite achieving perfect results in the widely used needle-in-a-haystack test, almost all models fail to maintain their performance in other tasks of RULER as input length increases.
- Common failure modes are observed at large context sizes, including the failure to ignore distractors and ineffective utilization of long context (e.g., simply copy from context or use parametric knowledge instead).
- RULER is challenging for even the top-ranked open-source models as task complexity increases.
- The analysis further reveals the large potential for improvement on RULER and the benefit of scaling model sizes in achieving better long context capabilities.
