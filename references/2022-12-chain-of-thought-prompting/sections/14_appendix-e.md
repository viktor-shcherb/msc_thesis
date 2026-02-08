# E Additional Details [p. 30–31]

## Version Control [p. 30]

[p. 30] The paper went through several revisions on arXiv:

- **V5 -> V6.** Fixed minor typo in Figure 3.
- **V4 -> V5.** Added Codex and UL2 results. Small changes to writing and style of paper.
- **V3 -> V4.** Fixed typo in Figure 3 and added a couple citations.
- **V2 -> V3.** Added GPT-3 results. Added SVAMP and AQuA eval datasets for math. Added SayCan eval for commonsense. Added Extended Related Work section (Appendix C). Added ablations for Commonsense and Symbolic Reasoning (Table 7). Added FAQ section (Appendix A). Added raw results in Appendix B.
- **V1 -> V2.** Added PaLM results (V1 only had LaMDA).

## E.1 Reproducibility Statement [p. 30]

[p. 30] As the results make use of two sets of large language models that is not publicly available, the authors take the following actions to facilitate reproducibility. First, they provide the exact input prompts for all tasks in Table 20 through Table 27 in Appendix G (and emphasize that they do not perform any finetuning and only apply prompting to off-the-shelf language models). Second, they conduct experiments using the publicly available GPT-3 API for four model scales: text-ada-001, text-babbage-001, text-curie-001, text-davinci-002. Finally, they make exact inputs, targets, and predictions for LaMDA 137B for each task available as a zip file in the supplementary material.

## E.2 Computational Resources [p. 30]

[p. 30] For all three language models evaluated, prompting-based inference only was performed. No finetuning was done for this paper. For inference on LaMDA 137B they used TPU v3 (8x8 configuration, 64 chips / 128 cores), and for inference on PaLM 540B they used TPU v4 (4x4x12 configuration, 192 chips / 384 cores). GPT-3 experiments were done using the public API.^5

^5 https://beta.openai.com/docs/api-reference/making-requests

## E.3 Dataset Details and Licenses [p. 30–31]

[p. 30] The details and licenses for all arithmetic and commonsense datasets used in the paper are listed below. The symbolic reasoning datasets were created synthetically, as described in Section 4.

### Arithmetic reasoning [p. 30]

- **Math Word Problem Repository** (Koncel-Kedziorski et al., 2016): AddSub (Hosseini et al., 2014): https://www.cs.washington.edu/nlp/arithmetic; MultiArith (Roy and Roth, 2015), license: CC BY 4.0.
- **ASDiv** (Miao et al., 2020): https://github.com/chaochun/nlu-asdiv-dataset.
- **AQuA** (Ling et al., 2017): https://github.com/deepmind/AQuA, license: https://github.com/deepmind/AQuA/blob/master/LICENSE.
- **GSM8K** (Cobbe et al., 2021): https://github.com/openai/grade-school-math, MIT license: https://github.com/openai/grade-school-math/blob/master/LICENSE.
- **SVAMP** (Patel et al., 2021): https://github.com/arkilpatel/SVAMP, MIT license: https://github.com/arkilpatel/SVAMP/blob/main/LICENSE.

### Commonsense reasoning [p. 30–31]

- **CSQA** (Talmor et al., 2019): https://www.tau-nlp.org/commonsenseqa, https://github.com/jonathanherzig/commonsenseqa.
- **StrategyQA** (Geva et al., 2021): the authors use the open-domain setting (question-only set) from BIG-bench collaboration (2021): https://github.com/google/BIG-bench/tree/main/bigbench/benchmark_tasks/strategyqa. The original dataset is from https://github.com/eladsegal/strategyqa, MIT license: https://github.com/eladsegal/strategyqa/blob/main/LICENSE.
- **Date understanding and sports understanding** from BIG-Bench (BIG-bench collaboration, 2021): Apache License v.2: https://github.com/google/BIG-bench/blob/main/LICENSE.
- **SayCan** (Ahn et al., 2022): SayCan dataset can be accessed at https://say-can.github.io/ under CC BY 4.0 license.
