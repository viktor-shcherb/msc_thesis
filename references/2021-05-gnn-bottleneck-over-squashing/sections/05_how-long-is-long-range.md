# 5 How Long is Long-Range? [p. 8-9]

[p. 8] In this section, over-squashing is analyzed combinatorially in the TREE-NEIGHBORSMATCH problem. A combinatorial lower bound is provided for the minimal hidden size that a GNN requires to perfectly fit the data (learn to 100% training accuracy) given its problem radius $r$.

## Notation

[p. 8] The arity of a tree is denoted by $m$ (=2 in the experiments); the counting base as $b=2$; the number of bits in a floating-point variable as $f=32$; and the hidden dimension of the GNN, i.e., the size of a node vector $\mathbf{h}_v^{(k)}$, as $d$.

## Derivation

[p. 8] A full tree of arity $m$ and problem radius $r = depth$ has $m^r$ green label-nodes. All $(m^r)!$ possible permutations of the labels {A, B, C, ...} are valid, disregarding the order of sibling nodes. Thus, the number of label assignments of green nodes is $(m^r)! / (m!)^{m^r - 1}$ (there are $m^r - 1$ parent nodes, where the order of each of their $m$ siblings can be permutated).

Right before interacting with the target node and predicting the label, a single vector of size $d$ must encapsulate the information flowing from all green nodes (Equations (2) and (3)).$^1$ Such a vector contains $d$ floating-point elements, each of them is stored as $f$ bits. Overall, the number of possible cases that this vector *can* distinguish is $b^{f \cdot d}$. The number of possible cases that the vector can distinguish between must be greater than the number of different examples that this vector may encounter in the training data. This requirement is expressed in Equation (4).

$^1$ The analysis holds for GCN and GIN. Architectures that use the representation of the recipient node to aggregate messages, like GAT, need to compress the information from only *half* of the leaves in a single vector. This increases the final upper bounds on $r$ by up to 1 and demonstrated empirically in Section 4.1.

## Equation (4)

$$b^{f \cdot d} > \frac{(m^r)!}{(m!)^{m^r - 1}} \tag{4}$$

The number of distinguishable states in a $d$-dimensional floating-point vector must exceed the number of distinct label assignments of green nodes.

## Equation (5)

Considering binary trees ($m=2$), and floating-point values of $f=32$ binary ($b=2$) bits, Equation (4) yields:

$$2^{32 \cdot d} > \frac{(2^r)!}{2^{2^r - 1}} \tag{5}$$

## Implications

[p. 9] Since factorial grows faster than an exponent with a constant base, a small increase in $r$ requires a much larger increase in $d$. Specifically, for $d=32$ as in the experiments in Section 4.1, the maximal problem radius is as low as $r=7$. That is, a model with $d=32$ *cannot* obtain 100% accuracy for $r > 7$.

In practice, the problem is worse; i.e., the empirical minimal $d$ is higher than the combinatorial, because even if a solution to storing some information in a vector of a certain size exists, a gradient descent-based algorithm is not guaranteed to find it. Figure 4 shows the combinatorial lower bound of $d$ given $r$. The authors also repeated the experiments from Section 4.1 and report the minimal empirical $d$ for each value of $r$. As shown in Figure 4, the empirical and the theoretical minimal $d$ grow exponentially with $r$; for example, even $d=512$ can empirically fit $r=7$ at most.

## Figure 4

**Figure 4** (p. 8): "Combinatorial and empirical lower bounds of the model dimension given the problem radius."

The figure shows a plot with x-axis "The problem radius $r$" ranging from 2 to 11 and y-axis showing the model dimension $d$ from 0 to 600. Two curves are plotted:
- **Empirical min $d$** (red triangles, dashed line): shows the minimum hidden dimension that achieves 100% training accuracy for each $r$. Values are approximately: $r=2$: 4, $r=3$: 8, $r=4$: 16, $r=5$: 32, $r=6$: 128, $r=7$: 512, with no empirical solution found for $r \geq 8$.
- **Combinatorial min $d$** (blue circles, solid line): shows the theoretical lower bound from Equation (5). Values are approximately: $r=2$: 1, $r=3$: 3, $r=4$: 8, $r=5$: 19, $r=6$: 52, $r=7$: 106, $r=8$: 256, $r=9$: 243 [unclear: exact values are hard to read], $r=10$: 549, $r=11$: labeled but off chart.

Both curves grow exponentially, with the empirical values consistently higher than the combinatorial lower bound. The gap between empirical and combinatorial bounds demonstrates that gradient descent cannot find the theoretically optimal encoding.
