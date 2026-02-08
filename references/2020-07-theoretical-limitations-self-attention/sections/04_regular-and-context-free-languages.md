# 4 Regular and Context-Free Languages [p. 4]

[p. 4] The paper analyzes the ability of transformers to recognize regular and context-free languages, using two prominent representatives.

## PARITY

PARITY is the set of bit strings such that the number of 1s is even. This is a very simple regular language, recognized by a finite-state automaton with two states. The regular languages form the lowest layer of the Chomsky hierarchy, and even simple RNNs can compute all regular languages. Within the regular languages, a particularly basic class is formed by the *counter-free* or *star-free* languages (McNaughton and Papert, 1971), which can be expressed by regular expressions using only union, complementation, and concatenation. In some sense, PARITY is the simplest non-counter-free, or *periodic*, regular language. This means, if transformers cannot compute PARITY, they cannot recognize (almost)^2 any regular language that is not counter-free.

Footnote 2: Inability to compute PARITY entails that they cannot recognize any regular language whose syntactic morphism is not quasi-aperiodic (Barrington et al., 1992, p. 488). [p. 4]

In the context of natural language, PARITY naturally arises in the context of evaluating logical formulas: evaluating iterated negations is tantamount to counting whether the number of nested negations is even or odd. If transformers cannot compute parity, they also cannot evaluate logical formulas accurately.

## 2DYCK

2DYCK is the language of correctly bracketed words consisting of two types of brackets ('(', ')' and '[', ']'). This language is a very simple model of hierarchical structure. The Chomsky-Schutzenberger theorem (Chomsky and Schutzenberger, 1963) states that any context-free language arises from a variant of 2DYCK with multiple types of parentheses through intersection with a regular language and homomorphisms. Consequently, the ability of LSTMs to model languages such as 2DYCK has been an object of experimental study (Sennhauser and Berwick, 2018; Skachkova et al., 2018; Bernardy, 2018). The theoretical results will show that transformers are strongly limited in their ability to model 2DYCK, including variants with fewer or more types of parentheses.
