# Introduction [p. 1-3]

## Motivation: Mechanistic interpretability and safety [p. 1]

As Transformer generative models continue to scale and gain increasing real world use [1, 2, 3, 4, 5], addressing their associated safety problems becomes increasingly important. *Mechanistic interpretability* -- attempting to reverse engineer the detailed computations performed by the model -- offers one possible avenue for addressing these safety issues. If we can understand the internal structures that cause Transformer models to produce the outputs they do, then we may be able to address current safety problems more systematically, as well as anticipating safety problems in future more powerful models.

In the past, mechanistic interpretability has largely focused on CNN vision models [6], but recently the authors presented [7] some very preliminary progress on mechanistic interpretability for Transformer language models. In that prior work, a mathematical framework for decomposing the operations of transformers was developed, which allowed making sense of small (1 and 2 layer attention-only) models and giving a near-complete account of how they function. [p. 1-2]

## Prior work on induction heads [p. 2]

The most interesting finding from the prior work [7] was the *induction head*, a circuit whose function is to look back over the sequence for previous instances of the current token (call it `A`), find the token that came after it last time (call it `B`), and then predict that the same completion will occur again (e.g. forming the sequence `[A][B] ... [A] -> [B]`). Induction heads "complete the pattern" by copying and completing sequences that have occurred before.

Mechanistically, induction heads in their models are implemented by a circuit of two attention heads: the first head is a "previous token head" which copies information from the previous token into the next token, while the second head (the actual "induction head") uses that information to find tokens preceded by the present token. For 2-layer attention-only models [7], the authors were able to show precisely that induction heads implement this pattern copying behavior and appear to be the primary source of in-context learning. [p. 2]

## The challenge of scaling to large models [p. 2]

The ultimate goal is to reverse-engineer frontier language models (which often contain hundreds of layers and billions or trillions of parameters), not merely 2-layer attention-only models. Both the presence of many layers, and the presence of MLPs, makes it much more difficult to mathematically pin down the precise circuitry of these models. However, a different approach is possible: by empirically observing, perturbing, and studying the learning process and the formation of various structures, one can try to assemble an *indirect* case for what might be happening mechanistically inside the network. This is compared to how a neuroscientist might gain understanding of how part of the brain functions by looking at neural development over time, studying patients with injuries, perturbing brain function in animals, or looking at a select small number of relevant neurons. [p. 2]

## Central hypothesis [p. 2]

The paper presents preliminary and indirect evidence for a tantalizing hypothesis:

> "*that induction heads might constitute the mechanism for the actual majority of all in-context learning in large transformer models*" [p. 2]

Specifically, the thesis is that there are circuits which have the same or similar mechanism to the 2-layer induction heads and which perform a "fuzzy" or "nearest neighbor" version of pattern completion, completing `[A*][B*] ... [A] -> [B]`, where `A* ~ A` and `B* ~ B` are similar in some space; and furthermore, that these circuits implement most in-context learning in large models. [p. 2]

## The phase change [p. 2]

The primary evidence comes via discovery and study of a *phase change* that occurs early in training for language models of every size (provided they have more than one layer), and which is visible as a bump in the training loss. During this phase change, the majority of in-context learning ability (as measured by difference in loss between tokens early and late in the sequence) is acquired, and simultaneously induction heads form within the model that are capable of implementing fairly abstract and fuzzy versions of pattern completion. The authors study this connection in detail to try to establish that it is causal, including showing that if the transformer architecture is perturbed in a way that causes the induction bump to occur in a different place in training, then the formation of induction heads *as well as* formation of in-context learning simultaneously move along with it. [p. 2]

## Six arguments [p. 3]

The paper presents six complementary lines of evidence arguing that induction heads may be the mechanistic source of general in-context learning in transformer models of any size:

- **Argument 1** (*Macroscopic co-occurrence*): Transformer language models undergo a "phase change" early in training, during which induction heads form and simultaneously in-context learning improves dramatically.

- **Argument 2** (*Macroscopic co-perturbation*): When the transformer architecture is changed in a way that shifts whether induction heads can form (and when), the dramatic improvement in in-context learning shifts in a precisely matching way.

- **Argument 3** (*Direct ablation*): When induction heads are directly "knocked out" at test-time in small models, the amount of in-context learning greatly decreases.

- **Argument 4** (*Specific examples of induction head generality*): Although induction heads are defined very narrowly in terms of copying literal sequences, the same heads also appear to implement more sophisticated types of in-context learning, including highly abstract behaviors, making it plausible they explain a large fraction of in-context learning.

- **Argument 5** (*Mechanistic plausibility of induction head generality*): For small models, the authors can explain mechanistically how induction heads work, and can show they contribute to in-context learning. Furthermore, the actual mechanism of operation suggests natural ways in which it could be re-purposed to perform more general in-context learning.

- **Argument 6** (*Continuity from small to large models*): In the previous 5 arguments, the case for induction heads explaining in-context learning is stronger for small models than for large ones. However, many behaviors and data related to both induction heads and in-context learning are smoothly continuous from small to large models, suggesting the simplest explanation is that mechanisms are the same.

Together the claims establish a circumstantial case that induction heads *might* be responsible for the majority of in-context learning in state-of-the-art transformer models. The authors emphasize that their results are only the beginnings of evidence, and that like any empirical or interventional study, a large number of subtle confounds or alternative hypotheses are possible. [p. 3]

## Safety relevance of the phase change [p. 3]

The phase change may have relevance to safety in its own right. Neural network capabilities -- such as multi-digit addition -- are known to sometimes abruptly form or change as models train or increase in scale [8, 1], and are of particular concern for safety as they mean that undesired or dangerous behavior could emerge abruptly. For example reward hacking, a type of safety problem, can emerge in such a phase change [9]. Studying a phase change "up close" and better understanding its internal mechanics could contain generalizable lessons for addressing safety problems in future systems. The phase change observed forms an interesting potential bridge between the microscopic domain of interpretability and the macroscopic domain of scaling laws and learning dynamics. [p. 3]

## Paper organization [p. 3]

The rest of the paper is organized as follows: clarifying key concepts and definitions (including in-context learning, induction heads, and a "per-token loss analysis" method), then presenting the 6 arguments one by one, drawing on evidence from analysis of 34 transformers over the course of training, including more than 50,000 attention head ablations (the data of which is shown in the Model Analysis Table). The paper then discusses unexplained "curiosities" in the findings, as well as reviewing related work. [p. 3]
