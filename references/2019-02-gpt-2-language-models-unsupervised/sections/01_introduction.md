# 1. Introduction [p. 1-2]

## Current state of ML systems

[p. 1] ML systems excel at tasks they are trained for using large datasets, high-capacity models, and supervised learning (Krizhevsky et al., 2012) (Sutskever et al., 2014) (Amodei et al., 2016). However, these systems are brittle and sensitive to slight changes in data distribution (Recht et al., 2018) and task specification (Kirkpatrick et al., 2017). Current systems are better characterized as narrow experts rather than competent generalists. [p. 1]

The dominant approach -- collecting task-specific training data, training on IID examples, testing on held-out IID data -- has shortcomings highlighted by erratic behavior in captioning models (Lake et al., 2017), reading comprehension systems (Jia & Liang, 2017), and image classifiers (Alcorn et al., 2018). [p. 1]

## Core hypothesis

[p. 1] The authors suspect that the prevalence of single task training on single domain datasets is a major contributor to the lack of generalization. Progress toward robust systems is likely to require training and measuring performance on a wide range of domains and tasks. Benchmarks such as GLUE (Wang et al., 2018) and decaNLP (McCann et al., 2018) have been proposed to study this. [p. 1]

## Multitask learning

[p. 1] Multitask learning (Caruana, 1997) is a promising framework for improving general performance. However, multitask training in NLP is still nascent. Recent work reports modest improvements (Yogatama et al., 2019) and the two most ambitious efforts to date trained on a total of 10 and 17 (dataset, objective) pairs respectively (McCann et al., 2018) (Bowman et al., 2018). From a meta-learning perspective, each (dataset, objective) pair is a single training example sampled from the distribution of datasets and objectives. Current ML systems need hundreds to thousands of examples to generalize, suggesting multitask training may need just as many effective training pairs. This motivates exploring additional setups for performing multitask learning. [p. 1]

## Pre-training and transfer

[p. 2] The current best performing systems use a combination of pre-training and supervised fine-tuning. The history of transfer in NLP:
1. Word vectors as inputs to task-specific architectures (Mikolov et al., 2013) (Collobert et al., 2011)
2. Contextual representations of recurrent networks transferred (Dai & Le, 2015) (Peters et al., 2018)
3. Recent work: task-specific architectures no longer necessary; transferring self-attention blocks is sufficient (Radford et al., 2018) (Devlin et al., 2018)

These methods still require supervised training for each task. Another line of work demonstrates language models performing specific tasks without supervised training, such as commonsense reasoning (Schwartz et al., 2017) and sentiment analysis (Radford et al., 2017). [p. 2]

## This paper's contribution

[p. 2] The authors connect these two lines of work and demonstrate language models can perform downstream tasks in a zero-shot setting -- without any parameter or architecture modification. They highlight the ability of language models to perform a wide range of tasks in a zero-shot setting, achieving promising, competitive, and state of the art results depending on the task. [p. 2]
