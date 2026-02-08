# Key Concepts [p. 4-6]

## In-context Learning [p. 4-5]

In modern language models, tokens later in the context are easier to predict than tokens earlier in the context. As the context gets longer, loss goes down. In some sense this is just what a sequence model is designed to do (use earlier elements in the sequence to predict later ones), but as the ability to predict later tokens from earlier ones gets better, it can increasingly be used in interesting ways (such as specifying tasks, giving instructions, or asking the model to match a pattern) that suggest it can usefully be thought of as a phenomenon of its own. This is usually referred to as **in-context learning**. [p. 4]

Emergent in-context learning was noted in GPT-2 [10] and gained significant attention in GPT-3 [1]. Simply by adjusting a "prompt", transformers can be adapted to do many useful things without re-training, such as translation, question-answering, arithmetic, and many other tasks. Using "prompt engineering" to leverage in-context learning became a popular topic of study and discussion [11, 12]. [p. 4]

### Two conceptions of in-context learning [p. 4]

At least two importantly different ways of conceptualizing and measuring in-context learning exist in the literature:

1. **Few-shot learning** (the Brown *et al.* conception [1]): focuses on few-shot learning of specific tasks. The model is prompted with several instances of some "task" framed in a next-token-prediction format (such as few-digit addition, or English-to-French translation).

2. **Decreasing loss at increasing token indices** (the Kaplan *et al.* conception [13]): focuses on observing the loss at different token indices, in order to measure how much better the model gets at prediction as it receives more context.

The first conception can be thought of as a micro perspective (focusing on specific tasks), where the second conception can be seen as a macro perspective (focusing on general loss, which on average correlates with these tasks). [p. 4]

The "few-shot learning" conception has tended to receive greater community attention. The ability to do many different tasks with one large model, even without further fine-tuning, is a notable change to the basic economics of model training. Moreover, it gives evidence of wide-ranging general capabilities and the ability to adapt on the fly, which nudges us to re-examine what it means for a model to "understand" or to "reason". [p. 4]

However, for the purposes of this work, the authors focus on the Kaplan *et al.* conception: *decreasing loss at increasing token indices*. They do so because it is a more general framing of the phenomenon than "few-shot learning". A drawback of this definition is it fails to isolate specific behaviors of interest. At the same time, it allows measuring models' overall ability to learn on-the-fly from the context, without depending on specific choices of "task". Starting from this definition, the authors are *also* able to study a couple classic few-shot learning examples (see Argument 4). [p. 4]

### In-context learning score [p. 4]

Throughout this work the authors compute a simple heuristic measure of in-context learning:

- **In-context learning score:** the loss of the 500th token in the context minus the average loss of the 50th token in the context, averaged over dataset examples.

The 500th and 50th token indices were chosen somewhat arbitrarily. The 500th token is near the end of a length-512 context, and the 50th token is far enough into the context that some basic properties of the text have been established (such as language and document type) while still being near the start. The authors also show that picking different numbers here does not change their conclusions. [p. 4]

### Safety relevance [p. 5]

In-context learning is of potentially special relevance to safety. In-context learning makes it harder to anticipate how a model might behave after a long context. In the longer run, concepts such as mesa-optimization or inner-alignment [14] postulate that meaningful learning or optimization could occur at test time (without changing the weights). In-context learning would be an obvious future mechanism for such hidden optimization to occur, whether or not it does so today. Thus, studying in-context learning seems valuable for the future. [p. 5]

## Induction Heads [p. 5-6]

In the authors' previous paper [7], they discovered a special kind of attention head -- which they named *induction heads* -- in two layer attention-only models. Induction heads are implemented by a circuit consisting of a pair of attention heads in different layers that work together to copy or complete patterns. The first attention head copies information from the previous token into each token. This makes it possible for the second attention head to attend to tokens based on what happened before them, rather than their own content. Specifically, the second head (which they call the "induction head") searches for a previous place in the sequence where the present token `A` occurred and attends to the next token (call it `B`), copying it and causing the model to be more likely to output `B` as the next token. That is, the two heads working together cause the sequence `...[A][B]...[A]` to be more likely to be completed with `[B]`. [p. 5]

Induction heads are named by analogy to inductive reasoning. In inductive reasoning, we might infer that if `A` is followed by `B` earlier in the context, `A` is more likely to be followed by `B` again later in the same context. Induction heads crystallize that inference. They search the context for previous instances of the present token, attend to the token which would come next if the pattern repeated, and increase its probability. Induction heads attend to tokens that would be predicted by basic induction (over the context, rather than over the training data). [p. 5]

Induction heads are implementing a simple algorithm, and are *not* memorizing a fixed table of n-gram statistics. The rule `[A][B] ... [A] -> [B]` applies regardless of what `A` and `B` are. This means that induction heads can in some sense work *out of distribution*, as long as local statistics early in the context are representative of statistics later. This hints that they may be capable of more general and abstract behavior. [p. 5]

### Formal definition [p. 6]

Formally, an **induction head** is defined as one which exhibits the following two properties on a repeated random sequence of tokens:

- **Prefix matching:** The head attends back to previous tokens that were followed by the current and/or recent tokens. That is, it attends to the token which induction would suggest comes next.
- **Copying:** The head's output increases the logit corresponding to the attended-to token.

In other words, induction heads are any heads that empirically increase the likelihood of `[B]` given `[A][B]...[A]` when shown a repeated sequence of completely random tokens. [p. 6]

**Figure 1** (p. 6): Illustration of induction head behavior. Shows two copies of a random token sequence ("Random Tokens" and "Repeat of Random Tokens"), each labeled "Category 40 ids node struction". An attention arrow connects the second occurrence of "node" back to the first occurrence of "struction" (which followed "node" in the first sequence). The prefix of the attended-to token equals the current token. The attended-to token is *copied*: the corresponding logit is increased for the next token. This illustrates how the induction head pattern-matches on `[A][B]...[A]` and promotes `[B]` as the completion. [p. 6]

As a consequence, induction heads will tend to be good at repeating sequences wholesale. For example, given "The cat sat on the mat. The cat ...", induction heads will promote the continuation "sat on the mat". This gives a first hint of how they might be connected to general in-context learning and even few-shot learning: they learn to repeat arbitrary sequences, which is a (simple) form of few-shot learning. [p. 6]

### Analogical sequence copying / in-context nearest neighbors [p. 6]

One of the things the authors are trying to establish is that when induction heads occur in sufficiently large models and operate on sufficiently abstract representations, the very same heads that do sequence copying *also* take on a more expanded role of *analogical sequence copying* or *in-context nearest neighbors*. By this they mean that they promote sequence completions like `[A*][B*] ... [A] -> [B]` where `A*` is not exactly the same token as `A` but similar in some embedding space, and also `B` is not exactly the same token as `B*`. For example, `A` and `A*` (as well as `B` and `B*`) might be the same word in different languages, and the induction head can then translate a sentence word by word by looking for "something like `A`", finding `A*` followed by `B*`, and then completing with "something like `B*`" (which is `B`). The authors are not yet able to prove mechanistically that induction heads do this in general, but in Argument 4 they show empirical examples of induction heads behaving in this way (including on translation), and in Argument 5 they point out that the known copying mechanism of induction heads in small models can be naturally adapted to function in this way. [p. 6]

## Per-Token Loss Analysis [p. 6-7]

To better understand how models evolve during training, the authors analyze what they call the "per-token loss vectors." The core idea traces back to a method used by Erhan *et al.* [15], and more generally to the idea of "function spaces" in mathematics. [p. 6]

---
[p. 7 continued]

The method starts with a collection of models. (In the authors' use, they train several different model architectures, saving dozens of "snapshots" of each over the course of training. This set of snapshots is used as the collection of models.) Next, the log-likelihoods each model assigns to a consistent set of 10,000 random tokens are collected, each taken from a different example sequence. These log-likelihoods are combined into a "per-token loss vector" and Principal Component Analysis (PCA) is applied. [p. 7]

The procedure has three steps:

1. **Step 1:** Run each model/snapshot over the same set of multiple dataset examples, collecting one token's loss per example.
2. **Step 2:** For each sample, extract the loss of a consistent token. Combine these to make a vector of losses per model/snapshot.
3. **Step 3:** The vectors are jointly reduced with principal component analysis to project them into a shared 2D space.

**Figure 2** (p. 7): Illustration of the per-token loss analysis method. Shows two models each processing the same set of examples (ex. 0, ex. 1, ex. 2, ...) with tokens highlighted. Step 1 collects one token's loss per example from each model. Step 2 extracts the loss of a consistent token and combines them into a vector (loss, loss, loss, ...) per model/snapshot. Step 3 applies PCA to project all loss vectors into a shared 2D space, shown as a small scatter plot. [p. 7]

A more detailed discussion of technical details can be found in the Appendix. [p. 7]

By applying this method to snapshots over training for multiple models, one can visualize and compare how different models' training trajectories evolve in terms of their outputs. Since PCA is used, each direction can be thought of as a vector of log-likelihoods that models are moving along. The authors particularly focus on the first two principal components, since those can be easily visualized. Models also move in directions not captured by the first two principal components, but it is a useful visualization for capturing the highest-level story of training. [p. 7]
