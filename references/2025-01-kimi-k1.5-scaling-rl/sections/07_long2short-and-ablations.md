# 3.4 Long2short [p. 13]

The authors compared the proposed long2short RL algorithm with the DPO, shortest rejection sampling, and model merge methods introduced in the Section 2.4, focusing on the token efficiency for the long2short problem (X. Chen et al. 2024), specifically how the obtained long-cot model can benefit a short model [p. 13-14].

**Figure 7** (p. 14): "Long2Short Performance. All the k1.5 series demonstrate better token efficiency compared to other models."

Description: Two scatter plots comparing token efficiency on MATH500 and AIME2024 benchmarks
- Key elements: 
  - Left panel (MATH500): Accuracy (y-axis, 75-95%) vs. Token Length (x-axis, 400-1400 tokens)
  - Right panel (AIME2024): Accuracy (y-axis, 10-60%) vs. Token Length (x-axis, 1000-5000 tokens)
  - Orange markers represent k1.5 series models, blue markers represent baseline models
- Notable patterns: 
  - k1.5-long represents the long-cot model selected for long2short training
  - k1.5-short w/ rl refers to the short model obtained using long2short RL training
  - k1.5-short w/ dpo denotes the short model with improved token efficiency through DPO training
  - k1.5-short w/ merge represents the model after model merging
  - k1.5-short w/ merge + rs indicates the short model obtained by applying shortest rejection sampling to the merged model
  - k1.5-shortest represents the shortest model obtained during the long2short training
  - Baselines: Claude 3.5, deepseek-v3, gpt-4-0513, qwen25-72B-inst (all in blue)
- Supports claim: The proposed long2short RL algorithm demonstrates the highest token efficiency compared to other methods such as DPO and model merge [p. 13-14]

**Key findings** [p. 13-14]:

All models in the k1.5 series (marked in orange) demonstrate superior token efficiency compared to other models (marked in blue):

- **k1.5-short w/ rl** achieves a Pass@1 score of **60.8 on AIME2024** (averaged over 8 runs) while utilizing only **3,272 tokens on average** [p. 13]
- **k1.5-shortest** attains a Pass@1 score of **88.2 on MATH500** while consuming approximately the same number of tokens as other short models [p. 13]

The k1.5 series substantially outperforms baseline models (deepseek-v3, qwen25-72B-inst, Claude 3.5, gpt-4-0513) in token efficiency across both benchmarks [p. 14, Figure 7].

# 3.5 Ablation Studies [p. 14]

## Scaling of model size and context length [p. 14]

The main contribution is the application of RL to enhance the model's capacity for generating extended CoT, thereby improving its reasoning ability. A natural question arises: how does this compare to simply increasing the model size? [p. 14]

To demonstrate the effectiveness of the approach, the authors trained two models of different sizes using the same dataset and recorded the evaluation results and average inference lengths from all checkpoints during RL training. These results are shown in Figure 8 [p. 14].

**Figure 8** (p. 15): "Model Performance vs Response Length of Different Model Sizes"

Description: Four scatter plots comparing Small Size vs Large Size models across benchmarks
- Key elements: Each panel shows Accuracy (y-axis) vs. Mean Response Length in tokens (x-axis) with trend lines for both model sizes
  - OMNI-MATH500 (truncated at 60): Small Size slope = 3.33e-05, Large Size slope = 6.42e-05
  - AIME2024 (truncated at 60): Small Size slope = 5.90e-05, Large Size slope = 8.10e-05
  - MATH500 (truncated at 60): Small Size slope = 2.45e-05, Large Size slope = 2.00e-05
  - AIMO2024: Small Size slope = 3.25e-05, Large Size slope = 6.84e-05
- Notable patterns: The larger model generally has steeper slopes (better token efficiency) except on MATH500 where the smaller model has a slightly higher slope. Both models show positive correlation between response length and accuracy.
- Supports claim: Although the larger model initially outperforms the smaller one, the smaller model can achieve comparable performance by utilizing longer CoTs

**Key findings** [p. 14]:

- Although the larger model initially outperforms the smaller one, **the smaller model can achieve comparable performance by utilizing longer CoTs optimized through RL** [p. 14]
- However, **the larger model generally shows better token efficiency than the smaller model** [p. 14]
- This indicates that **if one targets the best possible performance, scaling the context length of a larger model has a higher upper bound and is more token efficient** [p. 14]
- However, **if test-time compute has a budget, training smaller models with a larger context length may be viable solutions** [p. 14]

## Sampling strategies [p. 15]

The authors further demonstrate the effectiveness of their curriculum sampling strategy, as introduced in Section 2.3.4 [p. 15].

**Figure 9** (p. 15): "Analysis of curriculum learning approaches on model performance."

Description: Single line chart comparing two sampling strategies over training iterations
- Key elements: 
  - x-axis: Iteration (0-40+)
  - y-axis: Accuracy (0.30-0.65)
  - Two lines: Baseline (Uniform Sampling) in one color and Curriculum Learning in another
  - A vertical dashed "Curriculum Transition" line at approximately iteration 24
- Notable patterns: 
  - Baseline uses uniform sampling of mixed easy/hard problems throughout
  - Curriculum method uses uniform problems first, then switches to hard problems only at the transition point (iter 24)
  - After the transition, Curriculum Learning shows significantly higher accuracy improvement compared to the Baseline
- Supports claim: The proposed curriculum sampling method significantly enhances performance by progressively challenging the model

The training dataset $\mathcal{D}$ comprises a diverse mix of problems with varying levels of difficulty [p. 15]. With the curriculum sampling method, training initially uses $\mathcal{D}$ for a warm-up phase and then focuses solely on hard questions to train the model. This is compared to a baseline method that employs a uniform sampling strategy without any curriculum adjustments [p. 15]. The curriculum sampling method significantly enhances performance, attributed to its ability to progressively challenge the model, allowing it to develop a more robust understanding and competency in handling complex problems [p. 15].

## Effects of using negative gradients [p. 14-15]

The authors investigate the effectiveness of using ReST (Gulcehre et al. 2023) as the policy optimization algorithm in their setting [p. 14-15]. The primary distinction between ReST and other RL-based methods including the authors' approach is that ReST iteratively refines the model by fitting the best response sampled from the current model, without applying negative gradients to penalize incorrect responses [p. 14-15].

**Figure 10** (p. 16): "Comparison with using ReST for policy optimization."

Description: Multi-panel line chart comparing two methods (ReST vs. Ours) across 12 benchmarks
- Key elements: Each panel shows Accuracy (y-axis) vs. Step (x-axis, 0-50 steps) for two methods (ReST in one color, Ours in another)
- Benchmarks shown (12 panels): OMNI-MATH500, MATH500, AIMO2024, AIME2024, ChatGLMMath, GAOKAO_bmk, GPQA, k12-biology, k12-chemistry, k12-physics, KAOYAN, Total
- Notable patterns: The authors' method (with negative gradients) consistently outperforms ReST across all 12 benchmarks, showing higher accuracy at the same training step and faster convergence
- Supports claim: The method exhibits superior sample complexity compared to ReST, indicating that the incorporation of negative gradients markedly enhances the model's efficiency in generating long CoT [p. 15]

**Key findings** [p. 14-15]:

- The authors' method **exhibits superior sample complexity compared to ReST**, indicating that the incorporation of negative gradients markedly enhances the model's efficiency in generating long CoT [p. 15]
- The method **not only elevates the quality of reasoning but also optimizes the training process, achieving robust performance with fewer training samples** [p. 15]
- This finding suggests that **the choice of policy optimization algorithm is crucial in this setting**, as the performance gap between ReST and other RL-based methods is not as pronounced in other domains (Gulcehre et al. 2023) [p. 15]
- The results **highlight the importance of selecting an appropriate optimization strategy to maximize effectiveness in generating long CoT** [p. 15]

# 4 Conclusions [p. 15-16]

We present the training recipe and system design of k1.5, our latest multi-modal LLM trained with RL. One of the key insights we extract from our practice is that **the scaling of context length is crucial to the continued improvement of LLMs** [p. 15]. We employ optimized learning algorithms and infrastructure optimization such as partial rollouts to achieve efficient long-context RL training. How to further improve the efficiency and scalability of long-context RL training remains an important question moving forward [p. 15].

Another contribution is a combination of techniques that enable improved policy optimization. Specifically, the authors formulate long-CoT RL with LLMs and derive a variant of online mirror descent for robust optimization [p. 16]. They also experiment with sampling strategies, length penalty, and optimizing the data recipe to achieve strong RL performance [p. 16].

The authors show that **strong performance can be achieved by long context scaling and improved policy optimization, even without using more complex techniques such as Monte Carlo tree search, value functions, and process reward models** [p. 16].

In the future, it will be intriguing to study:
- Improving credit assignments
- Reducing overthinking without hurting the model's exploration abilities [p. 16]

The authors have also observed the potential of long2short methods. These methods **largely improve performance of short CoT models** [p. 16]. Moreover, **it is possible to combine long2short methods with long-CoT RL in an iterative way to further increase token efficiency and extract the best performance out of a given context length budget** [p. 16].
