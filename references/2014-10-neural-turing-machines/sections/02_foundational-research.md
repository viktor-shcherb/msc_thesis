# 2 Foundational Research [p. 2-5]

## 2.1 Psychology and Neuroscience [p. 2-3]

[p. 2] The concept of working memory has been most heavily developed in psychology to explain short-term manipulation of information. The broad picture is that a "central executive" focuses attention and performs operations on data in a memory buffer (Baddeley et al., 2009). Psychologists have extensively studied capacity limitations of working memory, often quantified by the number of "chunks" of information that can be readily recalled (Miller, 1956). There remains vigorous debate about how best to characterise capacity limitations (Barrouillet et al., 2004).

In neuroscience, working memory is ascribed to the functioning of a system composed of the prefrontal cortex and basal ganglia (Goldman-Rakic, 1995). [p. 3] Typical experiments involve recording from neurons in prefrontal cortex while a monkey performs a task involving a transient cue, a delay period, and a cue-dependent response. Certain tasks elicit persistent firing from individual neurons during the delay period or more complicated neural dynamics. A recent study quantified delay period activity in prefrontal cortex for a complex, context-dependent task based on "dimensionality" of the population code and showed it predicted memory performance (Rigotti et al., 2013).

Modeling studies of working memory range from biophysical circuits implementing persistent neuronal firing (Wang, 1999) to those solving explicit tasks (Hazy et al., 2006) (Dayan, 2008) (Eliasmith, 2013). Of these, Hazy et al.'s model is the most relevant to this work, as it is itself analogous to the Long Short-Term Memory architecture, which the authors have modified. Hazy et al.'s mechanisms gate information into memory slots to solve a memory task constructed of nested rules. In contrast, the authors include sophisticated memory addressing, which allows storage and recall of relatively simple, atomic data. Gallistel and King (Gallistel and King, 2009) and Marcus (Marcus, 2003) have argued that addressing must be implicated in the operation of the brain.

## 2.2 Cognitive Science and Linguistics [p. 3-4]

[p. 3] Historically, cognitive science and linguistics emerged alongside AI, all influenced by the advent of the computer (Chomsky, 1956) (Miller, 2003). In the early 1980s, both fields considered recursive or procedural (rule-based) symbol-processing to be the highest mark of cognition. The Parallel Distributed Processing (PDP) or connectionist revolution cast aside the symbol-processing metaphor in favour of "sub-symbolic" description of thought processes (Rumelhart et al., 1986).

Fodor and Pylyshyn (Fodor and Pylyshyn, 1988) made two barbed claims about the limitations of neural networks for cognitive modeling:
1. Connectionist theories were incapable of *variable-binding*, i.e., the assignment of a particular datum to a particular slot in a data structure.
2. Neural networks with fixed-length input domains could not reproduce human capabilities in tasks involving processing *variable-length structures*.

In response, neural network researchers including Hinton (Hinton, 1986), Smolensky (Smolensky, 1990), Touretzky (Touretzky, 1990), Pollack (Pollack, 1990), Plate (Plate, 2003), and Kanerva (Kanerva, 2009) investigated specific mechanisms that could support both variable-binding and variable-length structure within a connectionist framework. The NTM architecture draws on and potentiates this work.

[p. 4] Recursive processing of variable-length structures continues to be regarded as a hallmark of human cognition. In the last decade, debate arose over whether recursive processing is the "uniquely human" evolutionary innovation enabling language (supported by Fitch, Hauser, and Chomsky (Fitch et al., 2005)) or whether multiple new adaptations are responsible for human language evolution and recursive processing predates language (Jackendoff and Pinker, 2005). All agreed it is essential to human cognitive flexibility.

## 2.3 Recurrent Neural Networks [p. 4-5]

[p. 4] RNNs are a broad class of machines with dynamic state whose evolution depends both on the input and on the current state. Compared to hidden Markov models (which also have dynamic state), RNNs have a distributed state and therefore significantly larger and richer memory and computational capacity. Dynamic state is crucial for context-dependent computation; a signal entering at a given moment can alter the behaviour of the network at a much later moment.

A crucial innovation was the Long Short-Term Memory (LSTM) (Hochreiter and Schmidhuber, 1997), developed to address the "vanishing and exploding gradient" problem (Hochreiter et al., 2001a), which the authors relabel as "vanishing and exploding sensitivity." LSTM ameliorates the problem by embedding perfect integrators (Seung, 1998) for memory storage. The simplest example of a perfect integrator is:

**x**(t + 1) = **x**(t) + **i**(t)

where **i**(t) is an input to the system. The implicit identity matrix *I***x**(t) means that signals do not dynamically vanish or explode. Adding a programmable gate depending on context gives:

**x**(t + 1) = **x**(t) + g(context)**i**(t)

which allows selective information storage for an indefinite length of time.

RNNs readily process variable-length structures without modification. They have recently been used in speech recognition (Graves et al., 2013; Graves and Jaitly, 2014), text generation (Sutskever et al., 2011), handwriting generation (Graves, 2013), and machine translation (Sutskever et al., 2014). The authors do not feel it is urgent or even necessarily valuable to build explicit parse trees to merge composite structures greedily (Pollack, 1990) (Socher et al., 2012) (Frasconi et al., 1998).

[p. 5] Other important precursors to this work include differentiable models of attention (Graves, 2013) (Bahdanau et al., 2014) and program search (Hochreiter et al., 2001b) (Das et al., 1992), constructed with recurrent neural networks.
