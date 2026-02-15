# 2.4 Post-Training Stages [p. 6]

**Figure 5** (p. 6): "The post-training stages of Kimi-VL and Kimi-VL-Thinking, including two stages of joint SFT in 32K and 128K context, and further long-CoT SFT and RL stages to activate and enhance long thinking abilities."

Description: Flow diagram
- Key elements: Three blue boxes in sequence from left to right: (1) "Joint Supervised Fine-tuning: Text + Multimodal SFT Data, ↑ Fine-tuning ↑ Effective 128K" labeled as "Kimi-VL" (2) "Long-CoT Supervised Fine-tuning: Text + Multimodal Long-CoT Data, Planning, Evaluation, Reflection, Exploration" (3) "Reinforcement Learning (RL): Online RL on Answer-Only, Length penalty, Difficulty control" labeled as "Kimi-VL" on right side
- Notable patterns: Progressive enhancement from base SFT to long-CoT to RL, increasing complexity of reasoning capabilities
- Supports claim: Shows the post-training pipeline for developing thinking capabilities in Kimi-VL-Thinking

## Joint Supervised Fine-tuning (SFT) [p. 6]

In this phase, we fine-tune the base model of Kimi-VL with instruction-based fine-tuning to enhance its ability to follow instructions and engage in dialogue, culminating in the creation of the interactive Kimi-VL model. This is achieved by employing the ChatML format (Openai, 2024), which allows for targeted instruction optimization while maintaining architectural consistency with Kimi-VL. We optimize the language model, MLP projector, and vision encoder using a mixture of pure-text and vision-language SFT data, which will be described in Sec. 3.2. Supervision is applied to responses only, with system and user prompts being masked. The model is exposed to a curated set of multimodal instruction-response pairs, where explicit dialogue role tagging (e.g., "user:", "system:", structured injection of visual information, and preservation of the model's positional relationships are ensured through the format-aware packing. Additionally, to guarantee the model's comprehensive proficiency in dialogue, we incorporate a mix of multimodal data and pure text dialogue data used in Moonlight, ensuring its versatility across various dialogue scenarios.

We first train the model at the sequence length of 32k tokens for 1 epoch, followed by another epoch at the sequence length of 128k tokens. In the first stage (32K), the learning rate decays from 2 × 10^-5 to 2 × 10^-6, before it re-warmups to 1 × 10^-5 in the second stage (128K) and finally decays to 1 × 10^-6. To improve training efficiency, we pack multiple training examples into each single training sequence.

## Long-CoT Supervised Fine-Tuning [p. 6]

With the refined RL prompt set, we employ prompt engineering to construct a small yet high-quality long-CoT warmup dataset containing accurate and verified reasoning paths for both text and image inputs. This approach resembles rejection sampling (RS) but focuses on generating long-CoT reasoning paths through careful engineering. The resulting dataset encompasses key cognitive processes that are fundamental to human-like reasoning, such as **planning**, where the model systematically outlines steps before execution; **evaluation**, involving critical assessment of intermediate steps, reflecting during execution and refine its approach; and **exploration**, encouraging consideration of alternative solutions. By performing a lightweight SFT on this warm-up dataset, we effectively prime the model to internalize these multimodal reasoning strategies. As a result, the fine-tuned long-CoT model demonstrates improved capability in generating more detailed and logically coherent responses, which enhances its performance across diverse reasoning tasks.

## Reinforcement Learning [p. 6-7]

To further advance the model's reasoning abilities, we then train the model with reinforcement learning (RL), enabling the model to autonomously generate structured CoT rationales. Specifically, similar as Kimi k1.5 (K. Team et al. 2025), we adopt a variant of online policy mirror descent as our RL algorithm, which iteratively refines the policy model πθ to improve its problem-solving accuracy. During the i-th training iteration, we treat the current model as a reference policy model and optimize the following objective, regularized by relative entropy

---
[p. 7 continued]

to stabilize policy updates:

$$\max_{\theta} \mathbb{E}_{(x,y^*) \sim \mathcal{D}} \left[ \mathbb{E}_{y \sim \pi_{\theta}} \left[ r(x, y, y^*) \right] - \tau \text{KL}(\pi_{\theta}(x) || \pi_{\theta_i}(x)) \right]$$
(1)

where r is a reward model that justifies the correctness of the proposed answer y for the given problem x, by assigning a value r(x, y, y*) ∈ {0, 1} based on correctness, and τ > 0 is a parameter controlling the degree of regularization.

Each training iteration begins by sampling a problem batch from the dataset D, and the model parameters are updated to θ_{i+1} using the policy gradient derived from (1), with the optimized policy model subsequently assuming the role of reference policy for the subsequent iteration. To enhance RL training efficiency, we implement a length-based reward to penalize excessively long responses, mitigating the oververbalization problem where the model generates redundant reasoning chains. Besides, we employ two sampling strategies including curriculum sampling and prioritized sampling, which leverage difficulty labels and per-instance importance to focus training effort on the most pedagogically valuable examples, thereby optimizing the learning trajectory and improving training efficiency.

Through large-scale reinforcement learning training, we can derive a model that harnesses the strengths of both basic prompt-based CoT reasoning and sophisticated learning-enhanced CoT approaches. During inference, the model maintains standard autoregressive sequence generation, eliminating the deployment complexities associated with specialized planning algorithms that require external computation. Simultaneously, the model incorporates essential meta-reasoning abilities including error detection, backtracking, and iterative solution refinement by effectively utilizing the complete history of explored reasoning steps. With extended learning from its complete reasoning trace history, the model can effectively encode planned search procedures into its parametric knowledge.
