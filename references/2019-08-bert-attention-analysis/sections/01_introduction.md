# 1 Introduction [p. 1]

Large pre-trained language models achieve very high accuracy when fine-tuned on supervised tasks (Dai and Le, 2015; Peters et al., 2018; Radford et al., 2018), but it is not fully understood why. The strong results suggest pre-training teaches models about the structure of language, but the specific linguistic features learned remain unclear. [p. 1]

Recent work has investigated this question by examining the *outputs* of language models on carefully chosen input sentences (Linzen et al., 2016) or examining the internal *vector representations* of the model through probing classifiers (Adi et al., 2017; Belinkov et al., 2017). Complementary to these approaches, the authors study the *attention maps* of a pre-trained model. Attention (Bahdanau et al., 2015) is naturally interpretable because an attention weight has a clear meaning: how much a particular word will be weighted when computing the next representation for the current word. [p. 1]

The analysis focuses on the 144 attention heads in BERT-base (Devlin et al., 2019), a large pre-trained Transformer (Vaswani et al., 2017) network. [p. 1]

## Key findings summarized in introduction

[p. 1]

- BERT's attention heads exhibit common patterns: attending to fixed positional offsets, attending broadly over the whole sentence, and focusing heavily on the delimiter token [SEP].
- The authors argue attention to [SEP] is used by the model as a sort of no-op.
- Attention heads in the same layer tend to behave similarly.

[p. 1-2]

- Individual attention heads correspond remarkably well to particular syntactic relations. Heads are found that identify direct objects of verbs, determiners of nouns, objects of prepositions, and objects of possessive pronouns with >75% accuracy.
- A similar analysis for coreference resolution finds a BERT head that performs quite well.
- These behaviors emerge purely from self-supervised training on unlabeled data, without explicit supervision for syntax or coreference.

[p. 2]

- The authors propose an attention-based probing classifier that takes attention maps as input. It achieves 77 UAS at dependency parsing, showing BERT's attention captures substantial syntactic information.
- Several recent works have proposed incorporating syntactic information to improve attention (Eriguchi et al., 2016; Chen et al., 2018; Strubell et al., 2018). The authors' work suggests that syntax-aware attention already exists in BERT to an extent, which may contribute to its success.
