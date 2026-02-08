# Introduction [p. 1-2]

## Two existing strategies for applying pre-trained representations

[p. 1] Two existing strategies for applying pre-trained language representations to downstream tasks: *feature-based* and *fine-tuning*.

- **Feature-based** (e.g., ELMo, Peters et al., 2018a): uses task-specific architectures that include the pre-trained representations as additional features.
- **Fine-tuning** (e.g., OpenAI GPT, Radford et al., 2018): introduces minimal task-specific parameters; is trained on downstream tasks by fine-tuning *all* pre-trained parameters. Both approaches share the same objective function during pre-training and use unidirectional language models to learn general language representations.

## Core argument

[p. 1] The authors argue that current techniques restrict the power of pre-trained representations, especially for fine-tuning approaches. The major limitation is that standard language models are unidirectional, which limits the choice of architectures for pre-training. In OpenAI GPT, the authors use a left-to-right architecture where every token can only attend to previous tokens in the self-attention layers of the Transformer (Vaswani et al., 2017). Such restrictions are sub-optimal for sentence-level tasks and could be very harmful for token-level tasks such as question answering, where it is crucial to incorporate context from both directions.

## BERT proposal

[p. 1-2] The paper improves fine-tuning-based approaches by proposing BERT: **B**idirectional **E**ncoder **R**epresentations from **T**ransformers. BERT alleviates the unidirectionality constraint by using a "masked language model" (MLM) pre-training objective, inspired by the Cloze task (Taylor, 1953). The masked language model randomly masks some tokens from the input, and the objective is to predict the original vocabulary id of the masked word based only on its context. Unlike left-to-right language model pre-training, the MLM objective enables the representation to fuse left and right context, allowing pre-training of a deep bidirectional Transformer. In addition to MLM, a "next sentence prediction" (NSP) task is used that jointly pre-trains text-pair representations.

## Stated contributions

[p. 2] The contributions are:

1. Demonstrating the importance of bidirectional pre-training for language representations. Unlike Radford et al. (2018), which uses unidirectional LMs, BERT uses masked language models to enable pre-trained deep bidirectional representations. This is also in contrast to Peters et al. (2018a), which uses a shallow concatenation of independently trained left-to-right and right-to-left LMs.
2. Showing that pre-trained representations reduce the need for many heavily-engineered task-specific architectures. BERT is the first fine-tuning based representation model that achieves state-of-the-art performance on a large suite of sentence-level *and* token-level tasks, outperforming many task-specific architectures.
3. BERT advances the state of the art for eleven NLP tasks. Code and pre-trained models available at https://github.com/google-research/bert.

## Key results (from abstract/introduction)

- GLUE score: 80.5% (7.7 point absolute improvement)
- MultiNLI accuracy: 86.7% (4.6% absolute improvement)
- SQuAD v1.1 question answering Test F1: 93.2 (1.5 point absolute improvement)
- SQuAD v2.0 Test F1: 83.1 (5.1 point absolute improvement)

## In-text citations

- Dai and Le, 2015: language model pre-training for NLP tasks
- Peters et al., 2018a: ELMo, feature-based approach
- Radford et al., 2018: OpenAI GPT, fine-tuning approach
- Howard and Ruder, 2018: language model pre-training for NLP tasks
- Bowman et al., 2015; Williams et al., 2018: natural language inference tasks
- Dolan and Brockett, 2005: paraphrasing task
- Tjong Kim Sang and De Meulder, 2003: named entity recognition
- Rajpurkar et al., 2016: question answering task
- Vaswani et al., 2017: Transformer architecture, self-attention
- Taylor, 1953: Cloze task, inspiration for MLM
