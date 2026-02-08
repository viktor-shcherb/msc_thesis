# Appendix B: Evaluation Setups [p. 11]

[p. 11]

**Evaluation Hyperparameters.** For open-source LLMs, their default hyperparameters are adopted during evaluation on Ada-LEval. For proprietary models including GPT-4-Turbo, GPT-3.5-Turbo-1106, the temperature is set to 0. [p. 11]

**Computational Budget.** Experiments for open-source LLMs are conducted on NVIDIA A100 80GB GPU. The entire evaluation consumes around 800 GPU-hours. [p. 11]

**Benchmark Instructions.** Instructions of both tasks are presented within Ada-LEval. To ensure that models know what to do, the sample input and output format that models need to follow in solving problems are contained. [p. 11]

**Validity of 200-testcase subset.** Experiments on long-context settings adopt 200-testcase subset for proprietary models and 1000-testcase subset for open-source LLMs. To ensure that evaluation results on 200-testcase subset is valid, Table 12 and Table 13 display results on 200-testcase subset. [p. 11]
