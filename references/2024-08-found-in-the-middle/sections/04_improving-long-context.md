# 4 Improving long-context utilization with found-in-the-middle [p. 6-8]

[p. 6] Having validated that calibrated attention through found-in-the-middle is effective in locating relevant information within a long input context, the authors are ultimately interested in leveraging it to tackle lost-in-the-middle and practically improve a model's RAG performance.

## 4.1 Attention calibration [p. 6]

[p. 6] To allow the model to attend to contexts without being dictated by positional bias, the authors propose to intervene the model's attention based on the proposed calibrated attention. Specifically, given an input $x^{\text{prompt}}$, instead of allocating $\text{rel}(x_k^{\text{doc}}) + \text{bias}(k)$ attention to the $k$-th document, their ideal model attention $\text{Attn}_{\text{calibrated}}(x_k^{\text{doc}})$ would reflect only the relevance of the context $\text{rel}(x_k^{\text{doc}})$.

To achieve this, they propose to redistribute the attention values assigned to $\{x_k^{\text{doc}}\}_{k=1}^K$ according to $\text{rel}(x_k^{\text{doc}})$. Specifically, for each document $x_k^{\text{doc}}$, they propose to rescale the attention values on the tokens within the document, $\{x_{k,i}^{\text{doc}}\}_{i=1}^{N_k}$, by:

$$\text{attn}_{\text{calibrated}}(x_{k,i}^{\text{doc}}) = \frac{\alpha_k}{\text{Attn}_{\text{original}}(x_k^{\text{doc}})} \cdot \text{attn}_{\text{original}}(x_{k,i}^{\text{doc}}) \cdot C, \quad (5)$$

where $\alpha_k = \text{Softmax}(\text{rel}(x_k^{\text{doc}}), t)$, $t$ is the temperature hyperparameter, and $C$ is a normalization constant to ensure the total attention $\sum_{k,i} x_{k,i}^{\text{doc}}$ remains unchanged. With the rescaling, they effectively make the final attention on $x_k^{\text{doc}}$:

$$\text{Attn}_{\text{calibrated}}(x_k^{\text{doc}}) \propto \text{Softmax}(\text{rel}(x_k^{\text{doc}}), t), \quad (6)$$

where higher attention is allocated to more relevant context, and $t$ controls the disparity level.

## 4.2 Calibrated v.s. uncalibrated attention [p. 6-7]

[p. 6] The authors evaluate the performance of the proposed attention calibration method. They conduct experiments on two multi-document question answering tasks (more details in Appendix A): NaturalQuestion (Kwiatkowski et al., 2019) and SynthWiki (Peysakhovich and Lerer, 2023), with two models supporting different context window length: Vicuna-7b-v1.5-16k (Vicuna) (Li et al., 2023a) and tulu-2-7b (Tulu) (Wang et al., 2023) with 16k and 8k context window respectively. For each dataset, they consider two settings with different number of retrieved documents, $K = \{10, 20\}$.

[p. 7] Further implementation details are left to Appendix B.

**Figure 5** (p. 7): "Attention calibration effectively improves models' context utilization ability, with its performance curves lying almost entirely above standard vanilla attention (on 22 out of 24 cases). On the most challenging settings where the gold documents are placed in the middle, attention calibration provides 6-15 points improvements. Top/Bottom row: 10/20-doc. Numbers shown in Table 5."

The figure shows 8 subplots arranged in 2 rows of 4. Each subplot compares "Vanilla Attention" (blue) against "Calibrated Attention" (orange) for accuracy (y-axis) vs. position of the gold document (x-axis). Top row ($K = 10$): NaturalQuestion-Vicuna, NaturalQuestion-Tulu, SynthWiki-Vicuna, SynthWiki-Tulu. Bottom row ($K = 20$): same four dataset-model combinations. In all subplots, vanilla attention shows a U-shaped curve while calibrated attention performance curves lie almost entirely above. The improvement is most pronounced when the gold document is placed mid-sequence (6-15 percentage points). Calibrated attention's performance curve is above vanilla in 22 out of 24 cases.

**Found-in-the-middle improves long-context utilization across various datasets and models.** [p. 7] The authors observe that found-in-the-middle attention calibration consistently outperforms the uncalibrated baseline by a large margin (up to 15 percentage point improvement) across different tasks and models. On the most challenging scenario when the gold document is placed mid-sequence, attention calibration consistently offers improvements from 6-15 pp. Notably, attention calibration's performance curve lies almost entirely above the vanilla baseline curve (except 2 out of 24 cases), validating the effectiveness of their method in improving models' long context utilization.

## 4.3 Attention calibration in practice [p. 7-8]

[p. 7] In practice, to avoid the lost-in-the-middle effect, one commonly adopted workaround is to reorder the document positions, where documents considered more relevant are placed towards the beginning (or end) of the input. While these methods have led to performance improvements over the baseline without reordering, without handling the model's intrinsic bias, reordering-based methods' performance relies heavily on the correct ranking of the documents. The authors are interested in validating whether attention calibration can be applied on top of re-ordering methods to provide another layer of improvements.

**Attention calibration improves existing RAG pipelines.** [p. 7-8] The authors continue using NaturalQuestion and SynthWiki for evaluation. They compare to existing reordering methods including:

- **Prompt reordering** (Sun et al., 2023; Liang et al., 2023): Reorder documents based on relevance score generated through prompting.
- **LongLLMLingua-$r_k$** (Jiang et al., 2023): Reorder documents using query generation as the reranking metric.
- **Attention sorting** (Peysakhovich and Lerer, 2023): Reorder documents using vanilla model attention assigned to the documents.

**Figure 6** (p. 8): "Attention calibration can be applied on top of reordering-based methods to provide further performance boost. This suggests that mitigating attention bias can more fundamentally improve models' context utilization, offering a complementary way to further improve existing RAG pipeline. Top/Bottom row: 10/20-doc. Numbers shown in Table 5."

The figure shows 8 subplots arranged in 2 rows of 4 (same layout as Figure 5), comparing five methods: Vanilla Attention, Attention Sorting, Prompt Reordering, LongLLMLingua, and LongLLMLingua Calibrated. Top row ($K = 10$) and bottom row ($K = 20$) across NaturalQuestion and SynthWiki with Vicuna and Tulu models. LongLLMLingua-$r_k$ and prompt reordering are invariant to the gold document's position since they compute relevance of each document independently. Reordering methods do alleviate lost-in-the-middle where models' performances increase when gold documents are placed mid-sequence. LongLLMLingua-$r_k$ with calibration consistently achieves the highest performance across datasets and models.

[p. 8] The authors note that LongLLMLingua-$r_k$ and prompt reordering are invariant to the gold document's position since they compute the relevance of each document independently. First, reordering methods do alleviate lost-in-the-middle where models' performances increase when gold documents are placed mid-sequence. More importantly, by applying attention calibration on top of a reordering mechanism (LongLLMLingua-$r_k$ in this case), LongLLMLingua-$r_k$ with calibration consistently achieves the highest performance across datasets and models. These results suggest that attention calibration can more fundamentally improve models' context utilization, providing a complementary way to re-ordering methods to further improve current RAG pipeline.
