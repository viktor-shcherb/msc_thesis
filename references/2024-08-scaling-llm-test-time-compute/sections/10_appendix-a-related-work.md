# Appendix A. Related Work [p. 21]

## Language model reasoning

[p. 21] Language model performance on challenging mathematical reasoning tasks has rapidly improved in recent years [20, 22, 25, 32, 39]. These improvements can be attributed to four primary factors:

1. **Tuning continued pretraining on better corpora of math focused data** [20, 22, 32, 39].
2. **Improving the LLM proposal distribution** by either applying targeted optimization on specific reasoning tasks by finetuning with RL [32, 35, 49, 50] enabling models to critique and revise their answers iteratively [8, 23, 30];
3. **Enabling LLMs to benefit from additional test-time computation** by finetuning verifiers [6, 7, 10, 22, 40, 42, 45, 48].

The authors' work builds on these second and third lines of research by analyzing the extent to which test-time compute scaling can be improved by 1) refining an LLM's proposal distribution and 2) conducting search against verifiers. [p. 21]

## Analyzing test-time compute scaling

[p. 21] The tradeoff between train-time and test-time compute using Monte-Carlo tree search applied to the board game Hex was previously studied by Jones [16]. The authors instead focus their analysis on full-scale language model math reasoning problems. A survey work by Villalobos and Atkinson [44] analyzed the tradeoff between training and inference across a number of domains. However, much of their language-model analysis focused on test-time compute scaling in settings where the ground-truth answer is known. In contrast, the authors' analysis focuses on the setting when the ground-truth answer is not known. Additionally, a number of works in the RL literature have proposed methods, such as MCTS [19], which aim to navigate the tradeoff between test-time and training-time compute so as to enable a form of iterative self-play. The findings in the authors' work can be used to help develop similar algorithms that can operate on open-ended natural language. [p. 21]

## Augmenting LLMs with test-time compute

[p. 21] Beyond verifiers and revisions, a number of additional works have proposed alternative methods for enabling LMs to use test-time compute for reasoning. Namely, Wang et al. [46] conducts a hierarchical hypothesis search to enable inductive reasoning capabilities. A number of related works have proposed augmenting LMs with reasoning tools at test-time, which can greatly improve their performance on downstream tasks [11, 26, 27]. Finally, several works have proposed methods for learning thought tokens in an unsupervised manner [12, 51], enabling models to more effectively utilize the additional test-time compute that comes with sampling longer sequences. While the authors focus their analysis on two primary mechanisms by which test-time compute can be scaled in this work (e.g. verifiers and revisions), many of the methods by which they conduct their analysis (e.g. compute optimal scaling according to question difficulty) could, in principle, also be applied to any of these other methods of scaling test-time compute, and the authors believe that this is an interesting direction for future research. [p. 21]
