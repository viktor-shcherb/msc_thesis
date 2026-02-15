# 1. Introduction [p. 1-3]

## Motivation

[p. 1] Humans tend to think for longer on difficult problems to reliably improve their decisions [9, 17, 18]. The paper asks: given a challenging input query, can we enable language models to most effectively make use of additional computation at test time so as to improve the accuracy of their response?

Key motivations for test-time compute:
- An LLM should be able to do better than what it was trained to do by applying additional computation at test time
- Test-time capability has the potential to unlock new avenues in agentic and reasoning tasks [28, 34, 47]
- If pre-trained model size can be traded off for additional computation during inference, smaller on-device models could replace datacenter scale LLMs
- Automating improved model outputs via additional inference-time computation provides a path towards a general self-improvement algorithm with reduced human supervision

## Prior Work: Mixed Results

[p. 1] Prior work studying inference-time computation provides mixed results:
- Some works show that current LLMs can use test-time computation to improve their outputs [4, 8, 23, 30, 48]
- Other work shows that the effectiveness of these methods on more complex tasks such as math reasoning remains highly limited [15, 37, 43], even though reasoning problems often require drawing inferences about existing knowledge as opposed to new knowledge
- These conflicting findings motivate the need for a systematic analysis of different approaches for scaling test-time compute

## Two Mechanisms Studied

[p. 2] The paper studies two primary approaches:

1. **Best-of-N sampling** (and variants): sampling N outputs in "parallel" from a base LLM and selecting the one that scores highest per a learned verifier or reward model [7, 22]. This is the simplest and most well-studied approach.

2. **Modifying the proposal distribution and/or the verifier:**
   - Modifying the *proposal distribution* from which responses are obtained (e.g., asking the base model to revise its original responses "sequentially" [28])
   - Altering how the *verifier* is used (e.g., by training a process-based dense verifier [22, 45] and searching against this verifier)

## Experimental Setting

[p. 2-3] Experiments are carried out on the challenging MATH [13] benchmark using PaLM-2 [3] models specifically fine-tuned to either revise incorrect answers [28] (improving the proposal distribution; Section 6) or verify the correctness of individual steps in an answer using a process-based reward model (PRM) [22, 45] (Section 5).

Footnote 1 [p. 2-3]: Capability-specific finetuning is necessary to induce revision and verification capabilities into the base model on MATH since these capabilities are absent even in strong proprietary LLMs [15, 33]. The authors expect future LLMs will be more effective at verification and revision due to both increased scale and additional data targeted specifically towards these capabilities [5, 24, 36].

## Key Findings

[p. 3] The efficacy of a particular test-time compute strategy depends critically on both the nature of the specific problem at hand and the base LLM used:

- **Easier problems:** The base LLM can already readily produce reasonable responses. Iteratively refining its initial answer by predicting a sequence of N revisions (i.e., modifying the proposal distribution) may be a more effective use of test-time compute than sampling N independent responses in parallel.
- **More difficult problems:** May require searching over many different high-level approaches to solving the problem. Re-sampling new responses independently in parallel or deploying tree-search against a process-based reward model is likely a more effective way to use test-time computation.

This finding illustrates:
> "**the need to deploy an adaptive 'compute-optimal' strategy for scaling test-time compute**, wherein the specific approach for utilizing test-time compute is selected depending on the prompt, so as to make the best use of additional computation." [p. 3]

The paper shows that a notion of *question difficulty* (Section 4) from the perspective of the base LLM can be used to predict the efficacy of test-time computation, enabling practical instantiation of this "compute-optimal" strategy. By appropriately allocating test-time compute this way, they surpass the performance of a best-of-N baseline while only using about **4x less computation** with both revisions and search (Sections 5 and 6). [p. 3]

## FLOPs-Matched Comparison

[p. 3] Using the improved test-time compute scaling strategy, the authors conduct a FLOPs-matched comparison between a smaller model with additional test-time compute and pretraining a **14x larger model**:
- On easy and intermediate questions, and even hard questions (depending on specific conditions on the pretraining and inference workload), additional test-time compute is often preferable to scaling pretraining
- This finding suggests that: > "**in some settings it is be more effective to pretrain smaller models with less compute, and then apply test-time compute to improve model outputs**" [p. 3]
- On the most challenging questions, very little benefit is observed from scaling up test-time compute; instead, it is more effective to make progress by applying additional pretraining compute
- This demonstrates that current approaches to scaling test-time compute may not be 1-to-1 exchangeable with scaling pretraining
- Overall, even with a fairly naive methodology, scaling up test-time computation can already serve to be more preferable to scaling up pretraining, with only more improvements to be attained as test-time strategies mature
- Longer term, this hints at a future where fewer FLOPs are spent during pretraining and more FLOPs are spent at inference

## Figure 1

**Figure 1** (p. 2): *"Summary of our main results. Left: Compute-optimal scaling for iterative self-refinement (i.e., revisions) and search. On the left, we compare the compute-optimal scaling policy for our PaLM 2-S* revision model against baselines in the revision setting (top) and the PRM search setting (bottom). We see that in the revisions case, the gap between standard best-of-N (e.g. "parallel") and compute-optimal scaling gradually widens, enabling compute-optimal test-time scaling to outperform best-of-N with 4x less compute. Similarly, in the PRM search setting, we observe significant early improvements over best-of-N from compute-optimal scaling, nearly outperforming best-of-N with 4x less compute. We compare the performance of compute-optimal test-time scaling with PaLM 2-S* against the performance of the much larger pretrained model without test-time compute (e.g. greedy sampling). We compare where we expect to fall in one of three regimes of pretraining and inference allocation schemes. The three bars in each difficulty bin for each regime correspond to tests for three systems of pretraining to inference token allocation (left to right, increasing inference-to-pretraining token ratio from Y << X to Y ≈ X to Y >> X). The annotations denote the percent change in accuracy by using additional test-time compute with the smaller model, so as to match this larger model's FLOPs requirement. How would it compare in terms of accuracy? We can see that for the revisions (top) when Y << X, test-time compute is more effective than additional pretraining. However, as the inference to pretraining token ratio increases, test-time compute remains preferable on easy questions. Whereas on harder questions, pretraining is preferable in these settings. We also see a similar trend with PRM search (bottom). See Section 7 for more details."*

The figure has four panels:

**Top-left: "Iteratively Revising Answers at Test-time — Compute Optimal Revisions"**
- X-axis: Generation Budget (from 2^1 to 2^7)
- Y-axis: MATH Accuracy (%)
- Four lines: Majority, Best-of-N Weighted, Compute Optimal, Parallel
- Shows that compute-optimal scaling gradually widens its gap over standard best-of-N (e.g., "parallel") and compute-optimal scaling outperforms best-of-N with 4x less test-time compute
- Accuracy ranges from roughly 20% to above 45%

**Top-right: "Comparing Test-time and Pretraining Compute in a FLOPs Matched Evaluation" (Revisions)**
- X-axis: Ratio of Inference Tokens to Pretraining Tokens (<<1, ~=1, >>1)
- Y-axis: Relative Improvement in Accuracy From Test-time Compute (%)
- Three bar groups: Easy Questions (green), Medium Questions (orange), Hard Questions (blue)
- Values shown: For <<1 ratio: +27.6% (easy), +21.6% (medium); for ~=1 ratio: +16.7% (easy), +11.8% (medium), -11.9% (hard); for >>1 ratio: +5.4% (easy), +3.5% (medium), -37.2% (hard)
- When Y << X (inference tokens << pretraining tokens), test-time compute is often preferable to additional pretraining. As the ratio increases, test-time compute remains preferable on easy questions. On harder questions, pretraining is preferable.

**Bottom-left: "Test-time Search Against a PRM Verifier — Compute Optimal Search"**
- X-axis: Generation Budget (from 2^1 to 2^7)
- Y-axis: MATH Accuracy (%)
- Four lines: Majority, ORM Best-of-N Weighted, PRM Best-of-N Weighted, PRM Compute Optimal
- PRM Compute Optimal nearly outperforms best-of-N with 4x less compute at some points
- Accuracy ranges from roughly 10% to above 45%

**Bottom-right: "Comparing Test-time and Pretraining Compute in a FLOPs Matched Evaluation" (PRM Search)**
- X-axis: Ratio of Inference Tokens to Pretraining Tokens (<<1, ~=1, >>1)
- Y-axis: Relative Improvement in Accuracy From Test-time Compute (%)
- Three bar groups: Easy Questions (green), Medium Questions (orange), Hard Questions (blue)
- Values shown: For <<1 ratio: +19.1% (easy), +2.2% (medium), +2.0% (hard); for ~=1 ratio: -5.6% (easy), -35.6% (medium), -30.6% (hard); for >>1 ratio: +0.0% (easy), -35.3% (medium), -52.9% (hard)
- Shows a similar trend to the revisions panels with test-time compute being preferable at low inference-to-pretraining token ratios, but the benefits are smaller overall compared to the revision setting
