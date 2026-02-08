# 5.6 Qualitative Spot-Testing [p. 51]

[p. 51] Given the performance of the Apertus models on standard benchmarks was in-line with other open models, the authors also focused on spot-testing for test cases known to be difficult for LLMs. Specifically, they spot-test for inherently dangerous responses and common usage harms using relatively recently reported issues on state-of-the-art models in the wild.

Manual testing was conducted on the released Apertus-8B-Instruct and Apertus-70B-Instruct models, notably focusing on CBRNE, Dual Use, Medical Disinformation, Private Person Claims, and Suitability for Information Operations in Low-resource Languages. While potential for improvement in future model releases was found, no issue was found that would have warranted the delay of the model release. A detailed description of risk models and evaluation results is provided in Appendix M.1. To allow for further accumulation of such critical examples, a repository of critical examples and an Apertus-specific issues reporting system is deployed as part of the model release.^50

^50: https://github.com/swiss-ai/Apertus-Generation-Issues-Reports
