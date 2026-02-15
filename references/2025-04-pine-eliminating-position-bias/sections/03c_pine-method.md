# 3.3 PINE: Inter-Document Position-Invariant Inference via Bidirectional Attention [p. 4–6]

## Goal and Approach

The goal is to obtain an inter-document position-invariant hidden state **H_PINE**, which does not change regardless of document orders [p. 4]. The authors can mechanistically eliminate the position bias by equally attending to all documents [p. 4]. Therefore, they propose PINE, an approach that uses bidirectional inter-segment attention and re-assigning positions by importance scores (computed from attention score) to eliminate position bias (Figure 2) [p. 4].

The authors address that the "elimination" and "invariance" in the method are talked about from the input-output perspective, i.e., outputs remain unchanged regardless of the input-position orders [p. 4]. PINE still uses position encoding and does not eliminate position encoding itself [p. 5].

**Figure 2** (p. 4): "PINE: inter-document position-invariant inference via bidirectional attention."

Description: Diagram showing the PINE architecture with attention matrix visualization
- Key elements: Shows the attention matrix transformation from the running example in Section 3.1. The figure displays orange, blue, and green colors denoting system prompts (1 token), three different documents (2 tokens each), and decoded tokens (1 token), respectively. The figure shows p_i,j denotes the position of a token j when computing the attention from query q_i.
- Process flow: Shows three main stages: bidirectional attention → compute importance score → position re-assignment → sorting → decoded output
- Notable patterns: The importance score computation shows formulas like Importance(D₁, _) > Importance(D₂, _), Importance(Token 8, D₁) > Importance(Token 8, D₂), etc., indicating how documents are ranked and sorted
- Supports claim: Illustrates how PINE enables inter-document attention scores between documents to compute their importance, then documents are sorted by importances with more important documents placed in closer positions. The computation of "importance score" is introduced in Section 3.3.

## Bidirectional Attention

The authors first change the attention mask so that documents can attend to each other [p. 5]. Specifically, they make the inter-document attention **bidirectional** but keep the intra-document attention **causal** (Figure 2, middle) [p. 5]. The goal is to "eliminate" position bias among different documents rather than "intra" position bias within each document [p. 5]. The latter will lose the order information of tokens, and models can degenerate into bag-of-words models, which is not what the authors expect [p. 5].

## Re-assign Positions: Sorting By Importance Scores

Re-assigning positions must consider two folds: the position of queries and keys [p. 5]. Each token in conventional LMs has the same position when serving as both query and key [p. 5]. In the bidirectional attention used, this assignment has to be reconsidered [p. 5].

First, LMs are trained causally, meaning the position of the query must be larger than the keys in the attention computation [p. 5]. Therefore, it is necessary that positions so that each document is the **last** document when serving as queries (the diagonal of the rightmost figure in Figure 2) [p. 5]. For tokens before and after documents, their positions will not be affected as they are serving as queries [p. 5].

Re-assigning positions for keys must be redesigned to eliminate position bias [p. 5]. The authors determine the positions of documents based on importance scores when they serve as keys (numbers in the rightmost part of Figure 2) [p. 5]. Specifically, they first compute attentions without position embedding involved:

$$\text{Importance}_{\text{token}}(i, j) = \text{Softmax}(\mathbf{q}_i \mathbf{k}_j^T / \sqrt{d})$$

where d is the hidden state dimension [p. 5]. Then, they obtain the importance score between documents by aggregation, for example, Importance(D₁, D₂) = ∑_{i∈D₁,j∈D₂} Importance_token(i, j)/|D₂| [p. 5]. The length normalization is to prevent assigning higher importance scores to longer documents.³ The importance score could also be computed between individual tokens (e.g., Token 8) and documents [p. 5]. Lastly, they re-assign positions by importance scores as shown in the rightmost part of Figure 2: more important documents will have closer positions to the query [p. 5]. The rightmost part of Figure 2 shows the position re-assignment for keys (its diagonal also represents the position re-assignment for queries) [p. 5]. To avoid confusion, the authors address the fact that they do not actually sort and only re-assign them to different positions [p. 5]. In the position re-assignment, the position of keys may vary depending on the queries (numbers in column are different), which is the key difference between PINE and vanilla inference [p. 5]. Besides, the method is not limited to specific position embedding types [p. 5].

³ In pilot experiments, the authors find summation makes models convert from position bias to length bias. They also try maximum instead of averaging and find methods usually have noticeably worse performance than averaging possibly due to noises brought by unimportant tokens [p. 5].

## Inter-Document Position Invariant Inference

Once the authors have new attention mask and position re-assignment, they can place them into the model to obtain **H_PINE** [p. 5]. By applying **H_PINE** to every layer, attention heads, and tokens, they reach their method PINE. They prove that:

**Lemma 1.** *If the input* **Q, K, V** *are inter-document position-invariant representations, then* **H_PINE** *are also inter-document position-invariant representations.*

### Proof

To simplify the notation and without loss of generality (w.l.o.g), the authors still use examples in Section 3.1 [p. 5].

First, the SYS tokens already satisfy this lemma under the vanilla inference since they appear before documents, and PINE does not change their computation process [p. 5]. The authors only need to show PINE can make D₁ and Token 8 (i.e., tokens after documents) satisfy the lemma. W.l.o.g, they use D₁ as a running example [p. 5]:

• PINE first obtains importance score between documents: Sim(D₁, D_i) = ∑ Softmax(**Q₁ K_i^T** / √d)/|D_i|, where **Q₁** ∈ ℝ^{2×d}, **K_i** ∈ ℝ^{2×d}, 2 denotes the number of tokens in documents, and d denotes hidden states dimensions [p. 5]. Note that here the **Q, K** have not been applied to position embedding yet. Therefore, the importance score is not a function of input document positions [p. 5].

• W.l.o.g, let's assume Sim(D₁, D₃) > Sim(D₁, D₂), then they sort the document as follows [D₃|D₂|D₁] when they serve as keys and D₁ as query [p. 5]. Concretely, **Q_{PE,1}** = PE(**Q₁**, 3) (3 denotes it is treated as the last, i.e., third, document), **K_{PE,1}** = PE(**K₁**, 3), **K_{PE,2}** = PE(**K₂**, 2), **K_{PE,3}** = PE(**K₃**, 1) [p. 6]. Then they compute hidden states of D₁: **H₁** = Softmax(**Q_{PE,1}K_{PE}^T**/√d), where **K_{PE}** is the key values for the whole sequence [SYS|D₃|D₂|D₁] [p. 6]. It is noted that this process does not use any variables that are dependent on the input document positions, nor directly use the input document positions [p. 6]. Therefore, **H₁** obtained by PINE is not a function of input document positions [p. 6].

• Similarly, **H₂**, **H₃**, and Token 8's hidden states are not functions of input document positions. Their concatenation yields **H_PINE**, which is not a function of input document positions [p. 6].

**Proof ends.**

**Theorem 1.** *Given an input, if* **H_PINE** *is applied to every layer, attention head, and token to replace the conventional attention computation, then the model outputs are inter-document position-invariant representations.*

The theorem can be proved by mathematic induction by (1) lemma, (2) FFN, QKV projection, and layer norm yield representations that are not a function of document positions, and (3) the embedding representation is not a function of document positions [p. 6]. The authors put the complete proof in Appendix B [p. 6]. This lemma can also be understood in a simpler way: it is a corollary of the symmetry principle (Gross, 1996) [p. 6].

Some takeaways that are worth noting: (1) Both bidirectional attention mask and position re-assignment are needed to complete the proof. (2) PINE needs to be applied to every layer, attention heads, and tokens to complete the proof. (3) PINE is not limited to specific position embedding types [p. 6].
