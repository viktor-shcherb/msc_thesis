# 1 Introduction [p. 1--2]

[p. 1] Transformers are emerging as the new workhorse of NLP, achieving state-of-the-art in language modeling, machine translation, and pretrained contextualized word embeddings. They eschew recurrent computations, relying entirely on self-attention and performing computations largely in parallel, which enables scaling to very long sequences (Vaswani et al., 2017; Dai et al., 2019; Child et al., 2019).

It has been suggested that this limits their expressiveness, as they cannot process input sequentially (Tran et al., 2018; Dehghani et al., 2019; Shen et al., 2018a; Chen et al., 2018; Hao et al., 2019).

One aspect thought to be challenging for sequence models is hierarchical structure and recursion, widely thought essential to modeling natural language syntax (Everaert et al., 2015). Many researchers have studied the capability of recurrent neural network models to capture context-free languages (e.g., Kalinke and Lehmann, 1998; Gers and Schmidhuber, 2001; Gruning, 2006; Weiss et al., 2018; Sennhauser and Berwick, 2018; Korsky and Berwick, 2019) and linguistic phenomena involving hierarchical structure (e.g., Linzen et al., 2016; Gulordava et al., 2018). Some experimental evidence suggests transformers might not be as strong as LSTMs at modeling hierarchical structure (Tran et al., 2018), though analysis studies have shown transformer-based models encode a good amount of syntactic knowledge (e.g., Clark et al., 2019; Lin et al., 2019; Tenney et al., 2019).

The paper examines these questions from a theoretical perspective, asking whether models entirely based on self-attention are theoretically capable of modeling hierarchical structures involving unbounded recursion. Two computations thought essential to hierarchical structure are studied:

1. **Close brackets** -- the ability to correctly close brackets, a basic problem underlying all nonregular context-free languages, formalized by the Dyck language (Chomsky and Schutzenberger, 1963).
2. **Evaluate iterated negation** -- a basic component of evaluating logical formulas, amounting to evaluating the PARITY of bitstrings.

[p. 2] The paper shows that neither of these problems can be solved by transformers and similar models relying entirely on self-attention, unless the number or size of parameters increases with the input length. Besides representing basic building blocks of hierarchical structure, these languages also represent large classes of regular and context-free languages, so the results carry over to classes of other formal languages. The results yield more general limitations on the ability of self-attention to model finite-state languages and context-free languages.

Although theoretical work has investigated the power of recurrent neural networks in depth (e.g., Siegelman and Sontag, 1995; Bengio et al., 1994; Weiss et al., 2018; Miller and Hardt, 2019; Merrill, 2019), the theoretical study of self-attention has begun only recently (Perez et al., 2019; Hsieh et al., 2019). This study provides the first theoretical results on limitations in the power of self-attention.

Results are provided for both hard and soft attention settings, using different proof methods:
- Results are strongest in the hard attention setting, holding without further assumptions on activation functions and parameter norms.
- In the soft attention setting, results are obtained assuming smoothness of activation functions as used in practical implementations.

Paper structure: Related work (Section 2), self-attention definition (Section 3), two fundamental formal languages representing regular and context-free languages (Section 4), proof that self-attention cannot model these languages using hard (Section 5) or soft (Section 6) attention, discussion (Section 7).
