# 5 Results for Hard Attention [p. 4--6]

[p. 4] The analysis starts with hard attention (Perez et al., 2019). Hard attention transformers cannot represent PARITY or 2DYCK. To keep the results maximally general, the analysis uses combinatorial arguments and makes no assumption about activation functions, the norms of parameter matrices, or even that the internal position-wise representations y_j^{(k)} in each layer are vector-valued (as opposed to, say, discrete structures).

The aim is to prove that no hard-attention transformer is capable of representing PARITY or 2DYCK, by constructing -- for any given candidate transformer model -- a set of input words that this model will have to misclassify.

## Input Restrictions

[p. 5] The basic idea (see Figure 1) behind the proof is that, by fixing a small fraction of the input symbols in a particular way, the "attention" of the transformer can be captured so that it ends up ignoring almost all remaining input symbols. This shows the transformer could not have solved a problem such as PARITY, where every single input bit matters.

An **input restriction** (short: **restriction**) rho is a family of maps rho_n : {1, ..., n} -> {*, 0, 1} for n in N. An input restriction rho is applied to a transformer by fixing, when the input length is n, the input symbol x_i to the value rho_n(i) in {0, 1} whenever rho_n(i) != *. The output value of the resulting transformer only depends on those inputs x_i such that rho_n(i) = *.

The idea of using such input restrictions has been successful in the theory of Boolean circuits (Furst et al., 1984; Hastad et al., 1994). In particular, Furst et al. (1984) famously used it to prove that polynomial-size bounded-depth Boolean circuits with AND, OR, and NOT gates cannot compute PARITY. The paper describes a new method to prove existence of suitable restrictions appropriate to transformers, as the proof approaches from the Boolean circuit literature do not seem to generalize to networks with real-valued activations.

## Theorem 1 (Main Result for Hard Attention)

**Theorem 1.** *Let any hard attention transformer be given, and let C in (0, 1). Then there is a restriction rho and an integer c > 0 such that*

|{i <= n : rho_n(i) = *}| >= Cn

*(for all sufficiently large n) and such that the function computed by the transformer on the restricted input depends on <= c inputs, independent of input length n.* [p. 5]

## Corollary 2

**Corollary 2.** *Transformers with hard attention cannot model PARITY or 2DYCK.* [p. 5]

**Proof.** For PARITY, after applying a restriction, the transformer's output depends on c inputs. An input of sufficiently large size n thus has unrestricted inputs that do not influence the output. But flipping a single input bit changes the value, so the transformer's output cannot match membership in PARITY beyond chance for such n.

For 2DYCK, hard attention transformers cannot even solve the simpler variant 1DYCK with a single bracket type ('(', ')'). First restrict the first 0.2n input positions to '(' and the last 0.2n positions to ')'. After then applying the restriction provided by the theorem with C = 0.9, the resulting restricted input will still be compatible with both well-bracketed and non-well-bracketed inputs, but the prediction will depend only on a bounded number of positions. As the prediction depends on only a bounded number of positions, this shows the transformer could not recognize 1DYCK, and thus also not 2DYCK. [p. 5]

## Discussion: Languages That Can Be Modeled

[p. 5--6] It may be instructive to compare to similar languages that *can* be modeled by hard-attention transformers:

1. **1*** (over the alphabet {0, 1}) -- the regular language of words with only ones and no zeroes; its minimal automaton has two states, like PARITY. A transformer can recognize this by having an attention head that attends to a position with zero input if it exists, and rejects if the head found such a position.
2. **a^n b^n** -- a very basic context-free language. It can be recognized using suitable positional embeddings by (1) having one head attend to the largest position n, (2) using this information to attend to any b at position < n/2 or any a at position >= n/2. If such a symbol is found, the model rejects, else it accepts.

A crucial difference between these languages and PARITY / 2DYCK is that fixing a few inputs in any part of an input string can easily force nonmembership, e.g., a single 0 for 1*, and an a in the second half for a^n b^n. Therefore, such simple languages are immune to the depth reduction method, and indeed *can* be modeled perfectly with self-attention.

In general, the depth reduction method applies to languages that are sufficiently *sensitive*: If, for some C in (0, 1), fixing Cn input symbols cannot force a word to be inside or outside of the language, then hard-attention transformers cannot recognize this language. Sensitivity of functions has been studied in computational complexity (Boppana, 1997; Gopalan et al., 2016) and more recently linked to generalization in feedforward networks (De Palma et al., 2018). The authors intend to investigate these connections in future work.

## Proof Idea of Theorem 1

[p. 6] The approach is to construct input restrictions in a layerwise manner, starting from layer 1. For each layer, a suitable restriction is constructed that should only affect a few input bits (about (1 - C^{1/L})n many input bits), while forcing every attention head in the first layer to ignore all but c input bits. Perhaps surprisingly, this is possible: the idea is to fix input bits that achieve high attention scores for several heads, so that input bits that cannot achieve such high attention scores will be ignored.

Once such a restriction always exists, the technique can be used to iteratively remove layers, as illustrated in Figure 1: After applying the first such restriction, each of the heads in the first layer will only depend on a bounded number c of input positions. In the second step, the same argument is applied to the heads in the second layer, so that each head in the second layer only depends on a bounded number c' of heads in the first layer. After this step, the first layer can be collapsed into a collection of feedforward networks that transform a bounded number <= cc' of input positions into an activation y_i^{(0)} of the lowest layer. After this step, the first layer has been entirely removed. Iterating this argument, all layers are removed until the prediction output only depends on a bounded number of input positions, bounded independently of input length.

## Figure 1

**Figure 1** (p. 5): "Iteratively reducing the layers of a transformer by fixing a few input symbols."

Four panels (a)--(d) show the iterative layer reduction process:
- **(a)** By applying a suitable input restriction, attention is "attracted" from the first layer to a few inputs.
- **(b)** After this step, Lemma 4 ensures that each activation in the first layer only depends on a small number of input symbols that it can attend to (solid connections), plus the input that feeds into it via a skip connection (dashed connections).
- **(c)** A few more input symbols are fixed to "attract" attention of layer-2 heads to some layer-1 activations, again by Lemma 4. Each layer-2 activation only depends on a small number of layer-1 activations.
- **(d)** After this step, each layer-1 activation only depends on a few inputs, and layer 1 can be removed.

## Figure 2

**Figure 2** (p. 6): "Finding a good input restriction."

Two panels (a)--(b):
- **(a)** Every attention head in the first layer could potentially attend to any input bit.
- **(b)** Perhaps surprisingly, one can fix a small number of input bits in such a way that each layer-1 attention head can only possibly attend to c (here, c = 1) inputs, and ignores all other inputs. Each activation vector y_j^{(1)} in the first layer then only depends on the H * c inputs that its H (here, H = 1) attention heads can attend to, plus the input x_j that feeds into it via a skip-connection.

## Definition 3 (c-Transformer)

[p. 6] After the removal of the first layer of a transformer, the resulting structure is not a transformer any more, as each head in the lowest layer now depends on a *combination* of input positions. A technical definition is introduced:

**Definition 3.** *(c-Transformer). Let c be a positive integer. A c-transformer with L layers is one in which the layer-0 activations y_j^{(0)} depend on the embeddings not just at one position j, but are a function of the embeddings at <= c input positions:*

$$y_j^{(0)} = f_{n,j}^{inp}((v_{i_1^{j,n}}, p_{i_1^{j,n}}), ..., (v_{i_c^{j,n}}, p_{i_c^{j,n}}))$$  (4)

*for some indices i_s^{j,n} in {1, ..., n} (s = 1, ..., c).*

## Lemma 4 (Depth Reduction Lemma)

**Lemma 4.** *(Depth Reduction Lemma). Given a c-transformer with L layers, and some restriction rho such that*

$$|{i <= n : \rho_n(i) = *}| >= Cn$$  (5)

---
[p. 6--7 continued]

*(C in (0, 1]) for all sufficiently large n. Choose any C' < C. Then there is a restriction rho' such that*

$$|{i <= n : \rho'_n(i) = *}| >= C'n$$  (6)

*for all sufficiently large n, and such that the resulting function is computed by a (c * (2^c kH + 1))-transformer with L-1 layers, for some integer k (depending on C'), where H >= 1 is the number of attention heads at each layer and position.*

The lemma implies Theorem 1.

**Proof of Theorem 1.** The output of the transformer is determined by the last activation y_n^{(L)}. Apply the Depth Reduction Lemma iteratively, choosing the constants C' in the lemma appropriately, until only the zero-th layer remains. Then, after applying the resulting restriction, the final activation y_n^{(L)} is now computed by y_n^{(0)}, which is determined by a bounded number of input bits. QED.

## 5.1 Proving the Depth Reduction Lemma [p. 7--9]

[p. 7] The restrictions rho'_n are constructed separately for each n, on the basis of the given restriction rho_n. In this process, only additional bits are restricted, that is, the only case in which rho'_n(i) can be different from rho_n(i) is that rho'_n(i) may be 0 or 1 where rho_n(i) was *. The construction proceeds in three stages rho_n^{(1)}, rho_n^{(2)}, and rho_n^{(3)} = rho'_n, which all may restrict additional bits. At the end, the conclusion of the Depth Reduction Lemma is verified for the resulting restriction rho'_n.

Throughout the proof, a few parameters independent of n are needed: First, an integer k that has to be sufficiently large for the proof to succeed, and will be fixed later. Second, parameters eta in (0, 1/2), q in (0, 1), and delta > 0; specific values will be fixed later in the proof.

### Stage 1

[p. 7] Starting from rho_n, it is first modified into a restriction rho_n^{(1)} such that each input bit serves as an input to at most <= (1/eta) * c/C many different layer-0 heads, when applying rho_n^{(1)}. Assume the number of input bits feeding into more than (1/eta) * c/C different layer-0 activations is >= eta * C * n. Then the number of pairs of input bits and depending layer-0 activations is > eta * C * n * (1/eta) * c/C = nc. But there are at most nc such pairs, because there are n layer-0 activations, each of which depends on <= c inputs. So the number of input bits with > (1/eta) * c/C depending layer-0 heads is <= eta * C * n. The restriction rho_n^{(1)} is obtained from rho_n by restricting these input bits to some fixed value in {0, 1} (it doesn't matter which one), and the set {i <= n : rho_n^{(1)}(i) = *} still has at least (1 - eta) * C * n elements, for all sufficiently large n.

### Stage 2

[p. 7--8] The second stage is described. Write (h, i) for a layer-1 attention head h (h = 1, ..., H) at position i (i = 1, ..., n). Fix such a head (h, i). As y_i^{(0)} depends on <= c input bits, it can take on at most <= 2^c possible values. For each possible value z, and each position j in {1, ..., n}, the maximum possible attention value that can be achieved for this pair is computed:

$$\max_{x_1 ... x_n : y_i^{(0)} = z} f_{1,h}^{att}(z, y_j^{(0)})$$  (7)

considering only inputs x_1 ... x_n that are compatible with the restriction rho_n^{(1)} constructed at Stage 1. For each value z, the positions {1, ..., n} are ordered downwards by this value, obtaining a sequence j_1^{(z)}, ..., j_n^{(z)} for each layer-1 attention head h at a position i and each possible value z of y_i^{(0)} (in the case of ties, ordered by position, by Footnote 1). For each layer-1 attention head and each z, a sequence 1 <= i_1^{(z)} < i_2^{(z)} < ... < i_k^{(z)} <= n is selected such that (1) for each i_s^{(z)}, there is at least one input x_q that only feeds into the activation at position j_{i_s^{(z)}} and no j_{i_{s'}^{(z)}} (s != s'), and (2) i_k^{(z)} is minimal, i.e. there is no subsequence with smaller i_k^{(z)} that also satisfies (1). This construction is visualized in an example in Figure 3. Such a subsequence exists unless n <= ck, in which case the Depth Reduction Lemma is already satisfied for this input length n.

If z is a possible value of the activation y_i^{(0)}, then a pair ((h, i), z), of a head h at position i and a possible value z of y_i^{(0)}, is **satisfied** if one of the layer-0 activations y_{i_s^{(z)}}^{(0)} (s in {1, ..., k}) is fixed by rho_n^{(1)} to the value achieving the maximum attention value (7). Also, (h, i) is satisfied if each ((h, i), z) is satisfied. The idea behind this definition is: If ((h, i), z) is satisfied, then there are at most k different layer-0 heads that this head could attend to when applying rho'_n, assuming that y_i^{(0)} takes the value z. As a consequence, a satisfied head can only depend on c * (2^c k + 1) many input bits.

## Figure 3

**Figure 3** (p. 8): "Selecting the sequence i_1^{(z)} ... i_k^{(z)}: We have a c-transformer with c = 2, i.e., each Layer 0 activation only depends on at most two input bits. (a) We fix a head in Layer 1 at position i (here, i = 5), and some value z for y_i^{(0)} (blue activation). For each other Layer-0 activation y_j^{(0)}, we compute the maximal possible attention value between that activation and the Layer 1 head, assuming the fixed value z for y_i^{(0)} -- these maximum attention values are visualized by the thickness of the different lines. (b) We select k = 2 activations from Layer 0, marked in yellow and green. For each of these, there is at least one (in fact, two in the example) input bits (also marked in yellow and green) that feed into this one and no other selected activation."

Two panels:
- **(a)** Shows a c-transformer (c = 2) with input bits X_1 through X_7, Layer 0 activations, and a Layer 1 head at position i = 5, with one input fixed to 1. Lines of varying thickness connect Layer 0 activations to the Layer 1 head, representing maximal attention values for a fixed z.
- **(b)** Shows k = 2 selected activations (yellow and green) from Layer 0, with input bits that feed uniquely into each of these selected activations also marked in corresponding colors. One input is fixed to 1.

[p. 8] A layer-1 head k-**depends** on some input x_i if rho_n(i) = * and x_i appears as an input to some j_r^{(z)} for r <= i_k^{(z)}, for some z. Because i_k^{(z)} is minimal, a layer-1 head k-depends on an input if and only if that input appears as an input to some j_{i_s^{(z)}} (s <= k). In particular, a layer-1 head k-depends only on <= 2^c * c * k input variables. Two layer-1 heads are **k-neighbors** if some j_{i_s^{(z)}} for one and j_{i_{s'}^{(z')}} for the other both k-depend on some input bit x_l.

The restriction rho'_n is constructed using probabilistic arguments over randomly chosen restrictions. For this approach to succeed, a sufficient amount of independence between the activations of different heads in layer 1 is required. Thus the number of k-neighbors of each head must be bounded. Recall eta in (0, 1/2), and let H be the number of attention heads in each position of layer 1.

The restriction rho_n^{(1)} is modified into rho_n^{(2)} so that each layer-0 head has at most <= 2^c * k * H many k-depending unsatisfied layer-1 heads. Assume that indeed some layer-0 head has more than 2^c * k * H many k-depending unsatisfied layer-1 heads. By fixing <= c input bits and appealing to the Pigeonhole principle, this head can be fixed to a value that achieves the maximum attention value for at least > k * H many of these k-depending layer-1 heads. Let rho_n^{(2)} be the restriction resulting from adding this to rho_n^{(1)}. Once this is done, {i <= n : rho_n^{(2)}(i) = *} still has at least (1 - eta) * C * n - c elements, and more than kH many additional pairs ((h, i), z) are now also satisfied. The selection of the sequence j_1^{(z)}, ..., j_n^{(z)} is then repeated (substituting rho_n^{(2)} for rho_n^{(1)} in the definition), and the construction described is repeated to restrict additional input bits in rho_n^{(2)}. This procedure is iterated until no layer-0 head has > 2^c * k * H many k-depending unsatisfied layer-1 heads (h, i). This procedure can be iterated at most until each layer-1 head is satisfied, that is, at most (2^c * H * n) / (k * H) = (2^c * n) / k times. Let U be the number of times this procedure is iterated (U <= (2^c * n) / k). At the end, {i <= n : rho_n^{(2)}(i) = *} has at least (1 - eta) * C * n - cU >= ((1 - eta) * C - (2^c) / k) * n elements. By choosing k so large that (2^c) / k <= eta, {i <= n : rho_n^{(2)}(i) = *} still has at least (1 - 2*eta) * C * n many elements. Once this is completed, each layer-0 head has at most <= 2^c * k * H many k-depending unsatisfied layer-1 heads. Thus each input bit now has at most <= (2^c / eta) * k * c * H / C many k-depending unsatisfied layer-1 heads. Consequently, every unsatisfied layer-1 head has at most f <= (2^{2c} / eta) * c^2 * k^2 * H / C many unsatisfied k-neighbors.

### Stage 3

[p. 8--9] To construct the third and final restriction rho_n^{(3)}, the "probabilistic method" is applied: A probability distribution over restrictions rho_n^{(3)} is defined, and it is shown that the probability assigned to restrictions of the type required is strictly greater than zero, showing that such a restriction exists. For each input length n, the distribution over restrictions rho_n^{(3)} independently assigns to each input position i in {1, ..., n} the symbol 1 or 0 with probability q/2 each (q in (0, 1), chosen later), and * with probability 1 - q. On those input bits where rho_n^{(2)}(i) != *, the random restriction is restricted to agree with rho_n^{(2)}(i). For an attention head (h, i) and for each value z (there are at most 2^c such), define X_{i,h}^{(z)} to be the event that, for this head, none of y_{j_{i_1^{(z)}}}^{(0)}, ..., y_{j_{i_k^{(z)}}}^{(0)} are fixed to the value that produces the highest attention weight. Define X_0 to be the event that more than (1 + delta) * q of the input bits that rho_n^{(2)} maps to * are set to 0/1 by rho_n^{(3)} (where delta in (0, 1), to be fixed later).

The goal is to show that a nonzero amount of probability mass is assigned to restrictions rho'_n avoiding all events {X_0} union {X_{i,h}^{(z)} : i, h, z}.

First, a Chernoff bound gives (Mitzenmacher and Upfal, 2017, Theorem 4.4):

$$P(X_0) <= exp(-delta^2 * q * (1 - 2*eta) * C * n / 3)$$  (8)

since rho_n^{(2)} had >= (1 - 2*eta) * C * n unrestricted input bits after Stage 2.

[p. 9] Second, the probability of the event X_{i,h}^{(z)} (i = 1, 2, ..., n, h = 1, ..., H) decays exponentially in k. If ((h, i), z) is already satisfied after Stage 2, then P(X_{i,h}^{(z)}) = 0. Else, fixing z for ease of notation, let Y_{i,h}^t (t = 1, ..., k) be the event that the layer-0 activation y_{j_{i_t^{(z)}}}^{(0)} is not fixed to the value that produces the highest attention weight, for the given attention head (h, i). Note that X_{i,h}^{(z)} = intersection_t Y_{i,h}^t. P(Y_{i,h}^s) <= 1 - (q/2)^c in (0, 1). Any Y_{i,h}^s can be statistically dependent on at most c * (1/eta) * c/C = (1/eta) * c^2/C other events Y_{i,h}^{s'}, because each input bit has at most (1/eta) * c/C depending layer-0 heads. Therefore, there is a set of >= k / ((1/eta) * c^2/C) independent events among these. Call these Y_{i,h}^{t_1}, ..., Y_{i,h}^{t_{k/((1/eta)*c^2/C)}}. Then X_{i,h}^{(z)} is a subset of the intersection from s=1 to k/((1/eta)*c^2/C) of Y_{i,h}^{t_s}, and thus

$$P(X_{i,h}^{(z)}) <= product_{s=1}^{k/((1/eta)*c^2/C)} P(Y_{i,h}^{t_s}) <= (1 - (q/2)^c)^{k/((1/eta)*c^2/C)}$$  (9)

for each i = 1, 2, ..., n and h = 1, ..., H.

In order to conclude that there is a restriction rho_n^{(3)} avoiding all events {X_0} union {X_{i,h}^{(z)} : i, h, z}, the Lovasz Local Lemma is applied (Mitzenmacher and Upfal, 2017, Theorem 6.17). Each event X_{i,h}^{(z)} is statistically independent of the set {X_{(j,h')}^{(z')} : heads (j, h') and (i, h) are not k-neighbors}. The complement of this set has cardinality <= f = (2^{2c} / eta) * c^2 * k^2 * H / C, as concluded at the end of Stage 2. Set A := 1/k^2, B := 1/2. By the Lovasz Local Lemma, it is sufficient to show the following:

$$P(X_{i,h}^{(z)}) <= A(1 - B)(1 - A)^f$$  (10)

$$P(X_0) <= B(1 - A)^{2^c * H * n}$$  (11)

The Lovasz Local Lemma then guarantees that there is some input restriction rho_n^{(3)} that avoids all events {X_0} union {X_{i,h}^{(z)} : i, h, z}. For (10), it is needed that:

$$D <= A^{1/k}(1 - B)^{1/k}(1 - A)^{f/k}$$  (12)

where D = (1 - (q/2)^c)^{1/((1/eta)*c^2/C)} in (0, 1). For the first term on the right,

lim_{k -> infinity} A^{1/k} = lim_{k -> infinity} exp(-log(k^2)/k) = 1

Also, lim_{k -> infinity} (1 - A)^{f/k} equals

lim_{k -> infinity} (1 - 1/k^2)^{(2^{2c}/eta) * c^2 * k * H / C} = lim_{k -> infinity} (1 - E^2/k^2)^k = 1

for E := (2^{2c} / eta) * c^2 * H / C. So, if k is chosen large enough (independently of n), the RHS of (12) can be made arbitrarily close to 1, in particular, greater than D. In order to also satisfy (11), it is needed that:

exp(-delta^2 * q * (1 - 2*eta) * C / 3) <= B^{1/n} * (1 - A)^{2^c * H}

which holds for n, k large enough (again, choosing k independent of n). In conclusion, there exists, for each sufficiently-large n, a restriction rho_n^{(3)} that avoids all events {X_0} union {X_{i,h}^{(z)} : i, h, z}, for some k independent of n. For such a rho^{(3)}, we have:

|{i <= n : rho_n^{(3)}(i) = *}| >= (1 - 2*eta) * (1 - (1 + delta) * q) * C * n

for all sufficiently large n. Then choose eta in (0, 1/2), q in (0, 1), and delta > 0 (such that (1 + delta) * q in (0, 1)) in such a way as to achieve (1 - 2*eta) * (1 - (1 + delta) * q) = C'/C.

After applying rho_n^{(3)}, every layer-1 head b_{j,1,h} depends only on (1) the c input bits feeding into y_j^{(0)}, and (2) the <= c * 2^c * k input bits that the head k-depends on. Thus, each layer-1 activation y_j^{(1)} only depends on <= c * (2^c * k * H + 1) input bits: There are <= H * c * 2^c * k input bits that the H different attention heads k-depend on, plus a skip-connection from y_j^{(0)}, which itself depends on <= c input bits. The first layer can thus be removed: convert layer-1 activations y_j^{(1)} into layer-0 activations y_j^{(0)}, and obtain a (c * (2^c * kH + 1))-transformer performing the same computation as before when rho^{(3)} is applied. This concludes the proof of the Depth Reduction Lemma.
