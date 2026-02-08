# Discussion [p. 43]

## Safety Implications [p. 43]

The ultimate motivation of the research is the theory that reverse engineering neural networks might help us be confident in their safety. The authors state their work is only a very preliminary step towards that goal, but it does begin to approach several safety-relevant issues: [p. 43]

**Phase changes:** If neural network behavior discontinuously changes from one scale to the next, this makes it more challenging for researchers and society to prepare for future problems. [p. 43]

**In-Context Learning:** In-context learning has been a topic of concerned speculation in the safety community. With less-capable neural networks, one might be tempted to treat their behavior as relatively fixed after training. (That said, demonstrations of adversarial reprogramming [21] shed some doubt on this assumption.) In-context learning highlights that model behavior can in some sense "change" during inference, without further training. Even if we think of in-context learning as "locating" an already-learned behavior [22], rather than learning something new, the behavior could be a surprising and unwanted off-distribution generalization. [p. 43]

**Mesa-Optimization:** There have been some concerns that the underlying mechanism of in-context learning might be mesa-optimization [14], a hypothesized situation where models develop an internal optimization algorithm. The authors' work suggests that the primary mechanism of in-context learning, at least in small models, is induction heads. They did not observe any evidence of mesa-optimizers. [p. 43]

## Linking Learning Dynamics, Scaling Laws, and Mechanistic Interpretability [p. 43]

The in-context-learning phase change may be a useful "Rosetta stone" linking mechanistic interpretability, learning dynamics [23], and statistical physics-like empirical properties of neural networks (e.g. scaling laws or phase changes). If one wants to investigate the intersections of these lines of work, the phase change seems like an ideal starting point: a concrete example where these lines of inquiry are intertwined, which can be explored in small models, bounded in a small sliver of the training process, and is linked to a capability (in-context learning) the community is excited about. [p. 43]
