# 6 Limitations [p. 9-10]

[p. 9-10] Despite LongBench offering a more comprehensive testbed for long context understanding, the authors acknowledge the following shortcomings:

1. **Potentially unreliable automatic metrics:** As previous studies suggest (Bai et al., 2023), the automatic evaluation metrics (ROUGE-L, F1) may not accurately reflect the quality of the response. Particularly, results on these metrics may be underestimated for models that are used to generating longer responses. Although using LLM as an examiner may reduce this problem (Bai et al., 2023; An et al., 2023), the runtime overhead for evaluation may be high, and LLM also has bias when used as an evaluation metric (Zheng et al., 2023a).

2. **Coupling with instruction-following capabilities:** The primary objective is to assess the models' proficiency in long-context modeling regardless of their instruction-following capabilities. However, as the tasks in LongBench are closer to real-world applications, mastering them inevitably demands a certain level of instruction-following capability. Consequently, the performance on LongBench is coupled with the models' instruction-following capabilities.
