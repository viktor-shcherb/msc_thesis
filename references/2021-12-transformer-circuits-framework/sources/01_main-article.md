# A Mathematical Framework for Transformer Circuits [https://transformer-circuits.pub/2021/framework/index.html]

**Type:** blog-post
**Fetched:** 2026-02-07
**Priority:** primary

Note: The primary source at transformer-circuits.pub is a JavaScript-rendered interactive article that cannot be fetched as static HTML. The content below is reconstructed from comprehensive secondary sources that extensively quote and summarize the original article, including detailed technical notes by Logan Graves (logangraves.com), Oxen.ai Arxiv Dives (Parts 1 and 2), c7w.tech reading notes, and Pratik Doshi's review. All claims have been cross-checked across multiple sources for accuracy.

---

## Article Structure

The article is organized into the following major sections:

1. Summary of Results
2. Transformer Overview / Framework
   - Reframing transformers
   - The residual stream
   - Attention heads as independent operations
   - QK and OV circuits
   - Virtual weights
3. Zero-Layer Transformers
4. One-Layer Attention-Only Transformers
   - Skip-trigram analysis
   - Copying behavior and eigenvalue analysis
5. Two-Layer Attention-Only Transformers
   - Composition of attention heads (Q-composition, K-composition, V-composition)
   - Virtual attention heads
   - Induction heads
   - Ablation studies
6. Discussion and Motifs
   - Superposition and the residual stream
   - Path expansion and term dominance

---

## 1. Summary of Results

The article presents a mathematical framework for reverse-engineering transformer models by directly analyzing their weight matrices. The key findings, progressively building in complexity:

- **Zero-layer transformers** model bigram statistics. The bigram table can be accessed directly from the weights (the product W_U W_E).
- **One-layer attention-only transformers** are an ensemble of bigram and "skip-trigram" models. Both the bigram and skip-trigram tables can be accessed directly from the weights, without running the model.
- **Two-layer attention-only transformers** can implement much more complex algorithms using compositions of attention heads, and these compositional algorithms can be detected directly from weights. Notably, two-layer models use attention head composition to create "induction heads," a very general in-context learning algorithm.

> "Attention-only models can be written as a sum of interpretable end-to-end functions mapping tokens to changes in logits. These functions correspond to 'paths' through the model, and are linear if one freezes the attention patterns."

---

## 2. Transformer Framework

### 2.1 Reframing Transformers

The article reframes the standard transformer architecture in a mathematically equivalent but more interpretable way. The key insight is that transformers can be understood as a series of independent operations that read from and write to a shared "residual stream."

> "In many cases, it's helpful to reframe transformers in equivalent, but non-standard ways. Mechanistic interpretability requires breaking models down into human-interpretable pieces, and an important first step is finding the representation which makes it easiest to reason about the model."

The article focuses on simplified models:
- Decoder-only (autoregressive) architecture, like GPT
- Attention-only (no MLP layers)
- No bias terms or layer normalization (these can theoretically be folded into adjacent parameters)

### 2.2 The Residual Stream

The residual stream is the central conceptual contribution of the framework. All components of a transformer (the token embedding, attention heads, MLP layers, and unembedding) communicate with each other by reading from and writing to the residual stream.

> "The residual stream is a high-dimensional vector space, allowing layers to store data in different subspaces."

Key properties of the residual stream:
- It is a matrix of shape [seq_len, d_model]
- Once information is added, it persists unless another layer actively deletes it
- Dimensions of the residual stream function as "memory" or "bandwidth"
- The residual stream has no privileged basis -- features do not necessarily align with coordinate axes, which complicates interpretation
- MLPs can be understood as performing "memory management" by clearing unimportant information

> "Every attention head and MLP layer simply adds its information back to the residual stream."

### 2.3 Attention Heads as Independent Operations

> "Attention heads operate independently and add their output back into the residual stream."

The article emphasizes that although attention heads are often described using the "concatenate-multiply" formulation for computational efficiency, this is mathematically equivalent to treating each head as a completely independent operation. Each head reads from the residual stream, performs its computation, and writes its result back by addition.

> "Attention layers [operate as] completely independent heads, which process information in parallel, and add their output back into the residual stream."

Each attention head performs two largely independent computations:
1. **Where to move information** (which source token to attend to)
2. **What information to move** (how attending to a token affects the output)

### 2.4 QK and OV Circuits

This is one of the central technical contributions. Each attention head is decomposed into two independent circuits:

**QK Circuit (W_QK = W_Q^T W_K):**
- Determines the attention pattern
- Computes which source tokens each destination token attends to
- Produces scalar logits for pairs of tokens, which are passed through softmax
- Dimensions: [d_model, d_model]

> "The QK circuit determines the source (keys) and destination (query) of information by identifying the tokens with relevant information for each target token."

**OV Circuit (W_OV = W_O W_V):**
- Determines what information is moved when a token is attended to
- Computes how each source token affects the output logits if attended to
- Manages the content transferred between tokens
- Dimensions: [d_model, d_model]

> "The OV circuit manages the content to be moved between tokens."

Key insight: Q, K, V, and O are best understood not as four independent matrices, but as two pairs:
- W_Q and W_K operate together (query-key matching)
- W_O and W_V operate together (value transformation)

> "Key, query, and value vectors can be thought of as intermediate results in the computation of the low-rank matrices."

Each of these combined matrices (W_QK and W_OV) is a low-rank matrix (rank at most d_head, typically 64), even though its full dimensions are [d_model, d_model].

### 2.5 Virtual Weights

Virtual weights describe how non-adjacent layers communicate through the residual stream. Because all layers read from and write to the same residual stream, the effective weight matrix connecting any two layers is the product of the relevant projection matrices. These products create "virtual weights" that do not correspond to any single learned parameter matrix but describe the effective computation.

---

## 3. Zero-Layer Transformers

The simplest case: a model with only token embedding (W_E) and token unembedding (W_U), with no attention layers or MLPs.

The output logits are computed as:

    logits = W_U W_E x

where x is the one-hot token input. This is simply a lookup in the bigram table encoded by the matrix product W_U W_E. The model can only capture bigram statistics -- the probability that one token follows another, independent of any other context.

This serves as the baseline for understanding what additional capabilities each layer adds.

---

## 4. One-Layer Attention-Only Transformers

### 4.1 Mathematical Formulation

A one-layer attention-only transformer can be written as a sum of terms:

    T = Id tensor W_U W_E + sum_h (A^h tensor W_U W_OV^h W_E)

where:
- The first term is the "direct path" (bigram statistics, same as zero-layer)
- Each additional term corresponds to one attention head h
- A^h is the attention pattern matrix for head h
- W_OV^h = W_O^h W_V^h is the OV circuit for head h
- The tensor product separates "across-position" operations (attention patterns) from "per-position" operations (value transformations)

The full end-to-end matrix W_U W_OV^h W_E maps input tokens through the OV circuit directly to output logit effects.

### 4.2 Skip-Trigrams

One-layer models primarily learn skip-trigram patterns: structured as [source]...[destination] -> [output], where a source token at one position influences the prediction at a later position through attention.

The QK circuit determines which source tokens are attended to, and the OV circuit determines how that attention affects the output logits.

Examples of learned skip-trigrams:
- "keep ... in" -> "mind"
- "Back ... and" -> "forth"
- "perfect" -> "looks" -> "perfect"
- "large" -> "using"/"contains" -> "large"/"small"
- " Ralph" -> "R" -> "alph" (subword token completion)

**Python code patterns:**
- Indentation: `\n\t\t\t` ... `\n\t` -> `else` / `elif` / `except`
- Function arguments: `open` ... `,` -> `rb` / `wb` / `r` / `w`

**HTML patterns:**
- `tbody` ... `<` -> `<td`

**LaTeX patterns:**
- `\left` ... `\` -> `\right`

### 4.3 Copying Behavior and Eigenvalue Analysis

Many attention heads dedicate substantial capacity to "copying" -- preserving the identity of attended tokens in the output.

> "A lot of attention heads in 'one layer' models dedicate a lot of their capacity to copying."

The copying behavior is detected by analyzing the eigenvalues of the OV circuit matrix (W_U W_OV W_E):

> "If a matrix has positive eigenvalues, it suggests that a linear combination of tokens increases the logits of those same tokens, indicating copying behavior."

> "The eigenvalues of the OV and QK circuits are extremely positive, validating the idea that they are probably doing a kind of copying behavior."

This copying represents "a very simple form of in-context learning" -- if a token has appeared before, the model boosts the probability of that same token appearing again.

### 4.4 Attention Head Specialization

Analysis of a model with 12 heads (d_head = 64) reveals functional differentiation:
- Head 0:0 attends predominantly to conjunctions ("and," "or") and punctuation
- Head 0:4 focuses on verbs and prepositions ("be," "to," "in")
- Head 0:5 specializes in capitalization and numerical patterns

Some heads exhibit strong positional preferences, consistently attending to specific relative positions (e.g., always attending to the immediately preceding token).

---

## 5. Two-Layer Attention-Only Transformers

### 5.1 Composition of Attention Heads

The key capability that emerges with two layers is composition: second-layer attention heads can use the outputs of first-layer heads (which have been written to the residual stream) as inputs. This greatly increases expressivity.

There are three types of composition, corresponding to how the first-layer output enters the second-layer computation:

**Q-Composition:** The second layer's W_Q reads from residual stream positions modified by first-layer heads. This changes what the second-layer head is "looking for."

**K-Composition:** The second layer's W_K reads from residual stream positions modified by first-layer heads. This changes what information is "advertised" at each position for the second layer to find.

**V-Composition:** The second layer's W_V reads from residual stream positions modified by first-layer heads. This changes what information is actually moved when attention occurs, but does not affect the attention pattern itself.

### 5.2 Measuring Composition

The strength of composition between two heads is measured using the Frobenius norm ratio:

    composition_score = ||W_1 W_2||_F / (||W_1||_F * ||W_2||_F)

This normalized score indicates how much the product of two weight matrices deviates from what would be expected by chance, revealing which pairs of heads have significant compositional interactions.

### 5.3 Two-Layer Mathematical Formulation

The full two-layer transformer can be decomposed as:

    T = Id tensor W_U W_E
        + sum_{h in H1 union H2} A^h tensor (W_U W_OV^h W_E)
        + sum_{h2 in H2} sum_{h1 in H1} (A^{h2} A^{h1}) tensor (W_U W_OV^{h2} W_OV^{h1} W_E)

The three lines correspond to:
1. **Order 0 (direct path):** Bigram statistics via W_U W_E
2. **Order 1 (single head paths):** Skip-trigram statistics, each head independently
3. **Order 2 (composed paths):** Two heads composing, creating new attention patterns and value transformations

### 5.4 Attention Pattern Decomposition

The attention pattern for a second-layer head can itself be decomposed into terms reflecting the different composition types:

    C_QK^h = Id tensor Id tensor (W_E^T W_QK^h W_E)
             + sum_{h_q in H1} A^{h_q} tensor Id tensor (W_E^T W_OV^{h_q T} W_QK^h W_E)
             + sum_{h_k in H1} Id tensor A^{h_k} tensor (W_E^T W_QK^h W_OV^{h_k} W_E)
             + sum_{h_q in H1} sum_{h_k in H1} A^{h_q} tensor A^{h_k} tensor (W_E^T W_OV^{h_q T} W_QK^h W_OV^{h_k} W_E)

These four terms correspond to:
1. Pure token-token attention (no composition)
2. Q-composition (query modified by first-layer head)
3. K-composition (key modified by first-layer head)
4. Both Q- and K-composition simultaneously

### 5.5 Virtual Attention Heads

V-composition creates "virtual attention heads" -- effective attention heads that do not correspond to any single physical head in the network. Mathematically, a virtual attention head from V-composition has:

- Attention pattern: A^{h2} A^{h1} (product of two attention patterns)
- Value transformation: W_U W_OV^{h2} W_OV^{h1} W_E (composed OV circuits)

Because the OV circuit is linear after the softmax, the composition of two sequential value transformations can theoretically be collapsed into a single virtual attention head.

### 5.6 Induction Heads

Induction heads are the primary compositional mechanism discovered in two-layer models. They implement a general in-context learning algorithm:

**Mechanism:** Given a sequence where token A is followed by token B at some earlier point, when token A appears again later, the induction head predicts that B will follow.

**Two-head circuit:**

1. **First layer -- "previous token head":** Attends to the immediately preceding token and copies information about it into the residual stream at each position. After this head operates, each position's residual stream contains information about what token preceded it.

2. **Second layer -- "induction head":** Uses K-composition to match the current token against the "previous token" information written by the first-layer head. This effectively searches for previous occurrences of the current token and attends to whatever followed those occurrences.

Example with tokenization: "Potter" -> `Pot` + `ter`
- First layer: marks positions where `Pot` precedes `ter`
- Second layer: when seeing `Pot` again, attends to previous `ter` tokens, predicts `ter`

> "The query searches for 'similar' key vectors, but keys are shifted" by the prior layer's embeddings.

Because the mechanism operates in embedding space, "similar tokens" can provide information even without exact matches -- enabling approximate pattern matching.

**Validation:** The mechanism is tested on "totally random repeated patterns" requiring no training data statistics. Example: attending to arbitrary token `<7192>` successfully retrieves its previous occurrence, demonstrating the mechanism's robustness and generality.

### 5.7 Ablation Studies

The article validates the mathematical framework using order-by-order ablation analysis:

**Method:**
1. Record all attention patterns during a normal forward pass
2. Re-run with specific attention head outputs zeroed out or restricted
3. Measure the marginal loss reduction at each order of composition

**Ablation procedure (order-by-order):**
- Step 0: Normal forward pass, freeze attention patterns
- Step k: Allow only attention outputs from order <= k-1 to contribute to the residual stream
- Measure marginal loss reduction at each order

**Results (loss reduction in nats):**
- **Order 0** (direct path, W_U W_E): 1.8 nats reduction vs. uniform distribution
- **Order 1** (single attention heads): 5.2 nats additional reduction
  - Layer 1, Order 1: 0.05 nats vs. direct + layer 2; 1.3 nats vs. direct path alone
  - Layer 2, Order 1: 4.0 nats vs. direct + layer 1; 5.2 nats vs. direct path alone
- **Order 2** (V-composition): 0.3 nats additional reduction

**Conclusion:** Order 0 and Order 1 terms dominate model performance. V-composition (Order 2) contributes only a small additional improvement in this model, suggesting that K-composition and Q-composition (which affect attention patterns, not the value computation) are the primary drivers of compositional behavior.

---

## 6. Discussion and Motifs

### 6.1 Superposition and the Residual Stream

The residual stream lacks a privileged basis -- features do not necessarily align with coordinate axes. This creates a challenge for interpretation.

> "The residual stream often encodes more features than there are dimensions, so these features are approximately orthogonal (dot products close to zero)."

Sparse activation during training mitigates interference problems. MLP neurons tend to be polysemantic (responding to multiple unrelated features), and features may exist in "superposition" -- encoded as nearly-orthogonal directions in a space with fewer dimensions than features.

### 6.2 Architectural Scope and Limitations

The analysis focuses on attention-only models and explicitly excludes MLPs:

> "MLPs comprise 2/3 of a standard transformer's parameters."

> "More complete understanding will require progress on MLP layers."

The mathematical framework provides exact decompositions for attention-only models, but the combinatorial expansion of composition terms grows exponentially with depth, making direct mathematical analysis impractical for deeper models. The ablation methodology provides an empirical alternative.

### 6.3 Key Mathematical Tools

**Tensor product notation:** The article uses the tensor product (Kronecker product) to cleanly separate per-position and across-position operations:
- (A tensor B) * (C tensor D) = (AC) tensor (BD) (mixed-product property)
- (A tensor W) X = A X W^T (left-right multiplication interpretation)
- vec(A X W^T) = (W tensor A) vec(X) (vectorization)

**Attention head output:**
    h(x) = (A tensor W_OV) X
where A = softmax(X^T W_Q^T W_K X) and W_OV = W_O W_V

### 6.4 Interactive Visualizations

The original article contains extensive interactive visualizations (not reproducible in text) including:
- Attention pattern heatmaps for individual heads
- Eigenvalue spectra of OV circuits showing copying behavior
- Skip-trigram tables showing source-destination-output relationships
- Composition score matrices between first-layer and second-layer heads
- Induction head attention patterns on repeated random sequences
- Ablation study loss curves

[not accessible: Interactive JavaScript visualizations cannot be captured in text format. Readers should consult the original article for these visualizations.]

---

## 7. References Cited in the Article

The article references and builds upon several prior works, including:

- Vaswani et al. (2017) -- "Attention Is All You Need" (original transformer architecture)
- Radford et al. (2019) -- GPT-2 (decoder-only transformer language model)
- Elhage et al. (2021) -- Related Anthropic work on transformer interpretability
- Olah et al. (2020) -- "Zoom In: An Introduction to Circuits" (circuits framework for neural networks, originally developed for vision models)
- Olah et al. (2018) -- "The Building Blocks of Interpretability"
- Black et al. -- Work on polysemantic neurons and superposition
- Von Oswald et al. -- In-context learning via simulated gradient descent through composed induction heads (follow-up work)
