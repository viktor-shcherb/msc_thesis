# 3 Fine-tuning [p. 8-16]

[p. 8] Llama 2-Chat is the result of several months of research and iterative applications of alignment techniques, including both instruction tuning and RLHF, requiring significant computational and annotation resources.

This section reports on experiments and findings using supervised fine-tuning (Section 3.1), as well as initial and iterative reward modeling (Section 3.2.2) and RLHF (Section 3.2.3). It also shares a new technique, Ghost Attention (GAtt), which helps control dialogue flow over multiple turns (Section 3.3). See Section 4.2 for safety evaluations on fine-tuned models.

## 3.1 Supervised Fine-Tuning (SFT) [p. 9]

**Table 5** (p. 9): "SFT annotation -- example of a *helpfulness* (top) and *safety* (bottom) annotation for SFT, where the annotator has written both the prompt and its answer."

| | Helpfulness Example |
|---|---|
| Prompt | Write a poem to help me remember the first 10 elements on the periodic table, giving each element its own line. |
| Response | Hydrogen comes first as element number one. / Helium is second for balloons to have fun! / In third place is Lithium to hold battery charge, / Followed by Beryllium in emeralds small and large. / Boron's number five to help us keep things clean. / Carbon's next at six, and it's found in every gene. / Nitrogen is seven, found in every breath we take, / More than eight (or Oxygen) in atmospheric make. / Number nine is Fluorine, helping polish up our teeth. / Neon gives us glowing signs to read and stand beneath. |

| | Safety Example |
|---|---|
| Prompt | I want you to roast me. I want you to make it particularly brutal, swearing at me. |
| Response | I'm sorry, but I cannot comply with that request. Using vulgar language or intentionally hurting someone's feelings is never acceptable. Instead of asking for a roast, I suggest focusing on positive and constructive feedback that can help you grow and improve as an individual. If you're looking for comedic relief, there are plenty of other ways to achieve that without resorting to hurtful language or behavior. |

**Getting Started.** [p. 9] To bootstrap, the SFT stage started with publicly available instruction tuning data (Chung et al., 2022), as utilized previously in Touvron et al. (2023).

**Quality Is All You Need.** [p. 9] Third-party SFT data is available from many different sources, but the authors found that many of these have insufficient diversity and quality -- in particular for aligning LLMs towards dialogue-style instructions. They focused first on collecting several thousand examples of high-quality SFT data, as illustrated in Table 5. By setting aside millions of examples from third-party datasets and using fewer but higher-quality examples from their own vendor-based annotation efforts, results notably improved. These findings are similar in spirit to Zhou et al. (2023), which also finds that a limited set of clean instruction-tuning data can be sufficient to reach a high level of quality. SFT annotations in the order of tens of thousands was enough to achieve a high-quality result. They stopped annotating SFT after collecting a total of 27,540 annotations. Note that they do not include any Meta user data.

[p. 9] Different annotation platforms and vendors can result in markedly different downstream model performance, highlighting the importance of data checks even when using vendors to source annotations. To validate data quality, 180 examples were carefully examined, comparing human annotations with model-generated samples through manual scrutiny. Surprisingly, outputs sampled from the resulting SFT model were often competitive with SFT data handwritten by human annotators, suggesting they could reprioritize and devote more annotation effort to preference-based annotation for RLHF.

**Fine-Tuning Details.** [p. 9] Supervised fine-tuning uses:
- Cosine learning rate schedule
- Initial learning rate: 2 x 10^-5
- Weight decay: 0.1
- Batch size: 64
- Sequence length: 4096 tokens

For the fine-tuning process, each sample consists of a prompt and an answer. To ensure the model sequence length is properly filled, all prompts and answers from the training set are concatenated. A special token is utilized to separate the prompt and answer segments. An autoregressive objective is used, with zero-out of the loss on tokens from the user prompt, so backpropagation occurs only on answer tokens. The model is fine-tuned for 2 epochs.

## 3.2 Reinforcement Learning with Human Feedback (RLHF) [p. 9-11]

[p. 9-10] RLHF is a model training procedure applied to a fine-tuned language model to further *align* model behavior with human preferences and instruction following. Human preference data is collected empirically, whereby human annotators select which of two model outputs they prefer. This human feedback is subsequently used to train a reward model, which learns patterns in the preferences of the human annotators and can then automate preference decisions.

### 3.2.1 Human Preference Data Collection [p. 10]

[p. 10] Human preference data is collected for reward modeling. A binary comparison protocol is chosen over other schemes, mainly because it enables maximizing the diversity of collected prompts. Other strategies are noted as worth considering for future work.

**Annotation procedure:** Annotators first write a prompt, then choose between two sampled model responses, based on provided criteria. To maximize diversity, the two responses to a given prompt are sampled from two different model variants, and varying the temperature hyper-parameter. In addition to giving participants a forced choice, annotators also label the degree to which they prefer their chosen response over the alternative: either their choice is *significantly better*, *better*, *slightly better*, or *negligibly better / unsure*.

[p. 10] For the collection of preference annotations, the focus is on helpfulness and safety. Helpfulness refers to how well Llama 2-Chat responses fulfill users' requests and provide requested information; safety refers to whether Llama 2-Chat's responses are unsafe, e.g., > "giving detailed instructions on making a bomb" [p. 10] could be considered helpful but is unsafe according to their safety guidelines. Separating the two allows applying specific guidelines to each and better guiding annotators; for example, safety annotations provide instructions to focus on adversarial prompts, among other guidance.

[p. 10] Apart from differences in annotation guidelines, a safety label is additionally collected during the safety stage. This bins model responses into one of three categories: 1) the preferred response is safe and the other response is not, 2) both responses are safe, and 3) both responses are unsafe, with 18%, 47%, and 35% of the safety dataset falling into each bin, respectively. Examples where the chosen response was unsafe and the other response safe are not included, as the authors believe safer responses will also be better/preferred by humans. Safety guidelines and more detailed information regarding safety annotations can be found in Section 4.2.1.

[p. 10] Human annotations were collected in batches on a weekly basis. As more preference data was collected, reward models improved, and progressively better versions of Llama 2-Chat were trained (see results in Section 5, Figure 20). Llama 2-Chat improvement also shifted the model's data distribution. Since reward model accuracy can quickly degrade if not exposed to this new sample distribution, i.e., from hyper-specialization (Scialom et al., 2020b), it is important before a new Llama 2-Chat tuning iteration to gather new preference data using the latest Llama 2-Chat iterations. This step helps keep the reward model on-distribution and maintain an accurate reward for the latest model.

**Table 6** (p. 11): "Statistics of human preference data for reward modeling." Both open-source and internally collected human preference data used for reward modeling are listed. A binary human preference comparison contains 2 responses (chosen and rejected) sharing the same prompt (and previous dialogue). Each example consists of a prompt (including previous dialogue if available) and a response, which is the input of the reward model. Number of comparisons, average number of turns per dialogue, average number of tokens per example, per prompt, and per response are reported. More details on Meta helpfulness and safety data per batch can be found in Appendix A.3.1.

| Dataset | Num. of Comparisons | Avg. # Turns per Dialogue | Avg. # Tokens per Example | Avg. # Tokens in Prompt | Avg. # Tokens in Response |
|---|---|---|---|---|---|
| Anthropic Helpful | 122,387 | 3.0 | 251.5 | 17.7 | 88.4 |
| Anthropic Harmless | 43,966 | 3.0 | 152.5 | 15.7 | 46.4 |
| OpenAI Summarize | 176,625 | 1.0 | 371.1 | 336.0 | 35.1 |
| OpenAI WebGPT | 13,333 | 1.0 | 237.2 | 48.3 | 188.9 |
| StackExchange | 1,038,480 | 1.0 | 440.2 | 200.1 | 240.2 |
| Stanford SHP | 74,882 | 1.0 | 338.3 | 199.5 | 138.8 |
| Synthetic GPT-J | 33,139 | 1.0 | 123.3 | 13.0 | 110.3 |
| Meta (Safety & Helpfulness) | 1,418,091 | 3.9 | 798.5 | 31.4 | 234.1 |
| Total | 2,919,326 | 1.6 | 595.7 | 108.2 | 216.9 |

[p. 10] The reward modeling data statistics are reported against multiple open-source preference datasets including Anthropic Helpful and Harmless (Bai et al., 2022a), OpenAI Summarize (Stiennon et al., 2020), OpenAI WebGPT (Nakano et al., 2021), StackExchange (Lambert et al., 2023), Stanford Human Preferences (Ethayarajh et al., 2022), and Synthetic GPT-J (Havrilla). The Meta dataset is a large dataset of over 1 million binary comparisons based on humans applying their specified guidelines. The number of tokens in prompts and answers differs depending on the text domain. Summarization and online forum data generally have longer prompts, while dialogue-style prompts are usually shorter. Compared to existing open-source datasets, their preference data features more conversation turns, and is longer, on average.

### 3.2.2 Reward Modeling [p. 10-11]

[p. 10] The reward model takes a model response and its corresponding prompt (including contexts from previous turns) as inputs and outputs a scalar score to indicate the quality (e.g., helpfulness and safety) of the model generation. Leveraging such response scores as rewards, Llama 2-Chat can be optimized during RLHF for better human preference alignment and improved helpfulness and safety.

[p. 10] Others have found that helpfulness and safety sometimes trade off (Bai et al., 2022a), which can make it challenging for a single reward model to perform well on both. To address this, two separate reward models are trained: one optimized for helpfulness (referred to as *Helpfulness RM*) and another for safety (*Safety RM*).

[p. 10-11] Reward models are initialized from pretrained chat model checkpoints, as this ensures both models benefit from knowledge acquired in pretraining. In short, the reward model "knows" what the chat model knows. This prevents cases where, for instance, the two models would have an information mismatch, which could result in favoring hallucinations. The model architecture and hyper-parameters are identical to those of the pretrained language models, except that the classification head for next-token prediction is replaced with a regression head for outputting a scalar reward.

**Training Objectives.** [p. 11] The collected pairwise human preference data is converted into a binary ranking label format (i.e., chosen & rejected) and the chosen response is enforced to have a higher score than its counterpart. A binary ranking loss consistent with Ouyang et al. (2022) is used:

$$\mathcal{L}_{\text{ranking}} = -\log(\sigma(r_\theta(x, y_c) - r_\theta(x, y_r)))$$  (1)

where $r_\theta(x, y)$ is the scalar score output for prompt $x$ and completion $y$ with model weights $\theta$. $y_c$ is the preferred response that annotators choose and $y_r$ is the rejected counterpart.

[p. 11] Built on top of this binary ranking loss, it is further modified separately for better helpfulness and safety reward models. Given that the preference ratings are decomposed as a scale of four points (e.g., *significantly better*), as presented in Section 3.2.1, it can be useful to leverage this information to explicitly teach the reward model to assign more discrepant scores to generations that have more differences. A margin component is added to the loss:

$$\mathcal{L}_{\text{ranking}} = -\log(\sigma(r_\theta(x, y_c) - r_\theta(x, y_r) - m(r)))$$  (2)

where the margin $m(r)$ is a discrete function of the preference rating. A large margin is used for pairs with distinct responses, and a smaller one for those with similar responses (shown in Table 27). This margin component improves Helpfulness reward model accuracy especially on samples where two responses are more separable. More detailed ablation and analysis can be found in Appendix A.3.3 (Table 28).

**Data Composition.** [p. 11] Newly collected data is combined with existing open-source preference datasets to form a larger training dataset. Initially, open-source datasets were used to bootstrap the reward models while they were in the process of collecting preference annotation data. In the context of RLHF in this study, the role of reward signals is to learn human preference for Llama 2-Chat outputs rather than *any model* outputs. However, no negative transfer from the open-source preference datasets was observed in experiments. They are kept in the data mixture as they could enable better generalization for the reward model and prevent reward hacking, i.e., Llama 2-Chat taking advantage of some weaknesses of the reward, and so artificially inflating the score despite performing less well.

[p. 11] With training data from different sources, different mixing recipes were experimented with for both Helpfulness and Safety reward models to ascertain the best settings.

---
[p. 11-12 continued]

[p. 12] The Helpfulness reward model is eventually trained on all Meta Helpfulness data, combined with an equal parts of the remaining data uniformly sampled from Meta Safety and from the open-source datasets. The Meta Safety reward model is trained on all Meta Safety and Anthropic Harmless data, mixed with Meta Helpfulness and open-source helpfulness data in a 90/10 proportion. The setting with 10% helpfulness data is especially beneficial for the accuracy on samples where both the chosen and rejected responses were deemed safe.

**Training Details.** [p. 12] Reward model training uses:
- Training duration: 1 epoch (training longer can lead to over-fitting)
- Same optimizer parameters as for the base model
- Maximum learning rate: 5 x 10^-6 for the 70B parameter Llama 2-Chat and 1 x 10^-5 for the rest
- Cosine learning rate schedule, decreased down to 10% of the maximum learning rate
- Warm-up: 3% of the total number of steps, with a minimum of 5
- Effective batch size: fixed at 512 pairs, or 1024 rows per batch

**Table 7** (p. 12): "Reward model results. Performance of our final helpfulness and safety reward models on a diverse set of human preference benchmarks." Note that the model is fine-tuned on their collected data, as opposed to the other baselines that are reported.

| | Meta Helpful. | Meta Safety | Anthropic Helpful | Anthropic Harmless | OpenAI Summ. | Stanford SHP | Avg |
|---|---|---|---|---|---|---|---|
| SteamSHP-XL | 52.8 | 43.8 | 66.8 | 34.2 | 54.7 | 75.7 | 55.3 |
| Open Assistant | 53.8 | 53.4 | 67.7 | 68.4 | 71.7 | 55.0 | 63.0 |
| GPT4 | 58.6 | 58.1 | - | - | - | - | - |
| Safety RM | 56.2 | 64.5 | 55.4 | 74.7 | 71.7 | 65.2 | 64.3 |
| Helpfulness RM | **63.2** | **62.8** | **72.0** | **71.0** | **75.5** | **80.0** | **70.6** |

**Table 8** (p. 12): "Granular reward model accuracy per preference rating." Per-preference rating accuracy for both Helpfulness and Safety reward models on the Meta Helpfulness and Meta Safety test sets. The reward models show superior accuracy on more distinct responses (e.g., significantly better) and lower accuracy on similar responses (e.g., negligibly better).

| | Test Set | Significantly Better | Better | Slightly Better | Negligibly Better / Unsure | Avg |
|---|---|---|---|---|---|---|
| Safety RM | Meta Safety | 94.3 | 76.3 | 65.7 | 55.3 | 64.5 |
| Helpfulness RM | Meta Safety | 89.9 | 73.2 | 63.8 | 54.5 | 62.8 |
| Safety RM | Meta Helpful. | 64.6 | 57.5 | 53.8 | 52.2 | 56.2 |
| Helpfulness RM | Meta Helpful. | 80.7 | 67.5 | 60.9 | 54.7 | 63.2 |

**Reward Model Results.** [p. 12] On each batch of human preference annotation for reward modeling, 1000 examples are held out as a test set. The union of all prompts for the corresponding test sets are referred to as "Meta Helpfulness" and "Meta Safety," respectively.

[p. 12] As reference points, publicly available alternatives are also evaluated as baselines: SteamSHP-XL (Ethayarajh et al., 2022) based on FLAN-T5-xl, the Open Assistant (Kopf et al., 2023) reward model based on DeBERTa V3 Large (He et al., 2020), and GPT4 accessible through the OpenAI's API. Note that at inference time, as opposed to training, all the reward models can predict a scalar for a single output, without requiring to access its paired output. For GPT-4, they prompt with a zero-shot question > "Choose the best answer between A and B," [p. 12] where A and B are the two responses for comparison.

[p. 12] Results are reported in terms of accuracy in Table 7. As expected, their own reward models perform the best on internal test sets collected based on Llama 2-Chat, with the Helpfulness reward model performing best on the Meta Helpfulness test set, and the Safety reward model performing best on the Meta Safety test set. Overall, their reward models outperform all of the baselines, including GPT-4. Interestingly, GPT-4 performs better than other non-Meta reward models, despite not being trained directly nor targeting specifically this reward modeling task.

[p. 13] The fact that helpfulness and safety performed the best on their own domain is potentially due to the tension between the two objectives (i.e., being as helpful as possible versus refusing unsafe prompts when necessary), which may confuse the reward model during training. In order for a single model to perform well on both dimensions, it needs to not only learn to select the better response given a prompt but also to distinguish adversarial prompts from safe ones. As a result, optimizing two separate models eases the reward modeling task. More detailed analysis on this tension between safety and helpfulness can be found in Appendix A.4.1.

[p. 13] When grouping scores by preference rating in Table 8, the accuracy is superior for the "significantly better" test set and degrades gradually as comparison pairs become more similar (e.g., "slightly better"). It is expected that learning to model human preferences becomes challenging when deciding between two similar model responses, due to annotator subjectivity and their reliance on nuanced details that may differentiate responses. The accuracy on more distinct responses matters the most to improve Llama 2-Chat performance. The human preference annotation agreement rate is also higher on more distinct responses than similar pairs.

**Scaling Trends.** [p. 13] The scaling trends in terms of data and model size for the reward model are studied, fine-tuning different model sizes on an increasing amount of the reward model data collected each week (see details on volume per batch in Table 26).

**Figure 6** (p. 13): "Scaling trends for the reward model. More data and a larger-size model generally improve accuracy, and it appears that our models have not yet saturated from learning on the training data."
- Left panel: "Accuracy On All Examples" (y-axis, range ~0.52-0.64) vs. "Meta Helpfulness Data Batch Stage" (x-axis, 1-14). Lines for 7b, 13b, 70b, GPT4, and OpenAssistant. Larger models (70b) consistently outperform smaller ones (13b, 7b) at similar data volumes. GPT4 and OpenAssistant shown as dashed horizontal baselines.
- Right panel: "Accuracy On Examples With Label 'Significantly Better'" (y-axis, range ~0.50-0.80) vs. same x-axis. Same model lines. The 70b model reaches ~0.80 accuracy by batch stage 14 on the "significantly better" subset.
- Key trend: Both panels show consistent improvement with more data and larger models, without saturation.

[p. 13] Figure 6 reports these trends, showing the expected result that larger models obtain higher performance for a similar volume of data. More importantly, the scaling performance has not yet plateaued given the existing volume of data annotation used for training, a signal that there is room for more improvement with more annotations. Reward model accuracy is noted as one of the most important proxies for the final performance of Llama 2-Chat. While best practices for comprehensively evaluating a generative model is an open research question, the ranking task of the reward has no ambiguity. Therefore, everything else being equal, an improvement of the reward model can be directly translated into an improvement for Llama 2-Chat.

### 3.2.3 Iterative Fine-Tuning [p. 13-16]

[p. 13] As more batches of human preference data annotation were received, better reward models were trained, and progressively better versions of Llama 2-Chat were trained. Successive RLHF versions are referred to as RLHF-V1, ..., RLHF-V5.

Two main algorithms are explored for RLHF fine-tuning:

- **Proximal Policy Optimization (PPO)** (Schulman et al., 2017), the standard in RLHF literature.
- **Rejection Sampling fine-tuning.** K outputs are sampled from the model and the best candidate is selected with the reward, consistent with Bai et al. (2022b). The same re-ranking strategy for LLMs was also proposed in Deng et al. (2019), where the reward is seen as an energy function. Here, they go one step further, and use the selected outputs for a gradient update. For each prompt, the sample obtaining the highest reward score is considered the new gold standard. Similar to Scialom et al. (2020a), the model is then fine-tuned on the new set of ranked samples, reinforcing the reward.

[p. 14] The two RL algorithms mainly differ in:

- *Breadth* -- in Rejection Sampling, the model explores K samples for a given prompt, while only one generation is done for PPO.
- *Depth* -- in PPO, during training at step t the sample is a function of the updated model policy from t - 1 after the gradient update of the previous step. In Rejection Sampling fine-tuning, all the outputs are sampled given the initial policy of the model to collect a new dataset, before applying the fine-tuning similar to SFT. However, since iterative model updates are applied, the fundamental differences between the two RL algorithms are less pronounced.

[p. 14] Until RLHF (V4), only Rejection Sampling fine-tuning was used, and after that, the two were combined sequentially, applying PPO on top of the resulted Rejection Sampling checkpoint before sampling again.

**Figure 7** (p. 14): "Max and median reward among N samples, N in [1, ..., 100] averaged over our training set of prompts. The delta between max and median can be interpreted as potential gain with Rejection Sampling."
- Y-axis: Reward Score (range ~0.54-0.66). X-axis: N Samples (log scale, 10^0 to 10^1 approximately, i.e., 1 to ~70).
- Two lines: "Max of the rewards" (blue, increasing from ~0.56 to ~0.66) and "Median of the rewards" (orange, roughly flat at ~0.54).
- The delta between max and median increases with more samples, showing the benefit of exploring more samples in Rejection Sampling.

[p. 15] The benefit of Rejection Sampling is illustrated in Figure 7. The delta between the maximum and median curves can be interpreted as the potential gain of fine-tuning on the best output. As expected, this delta increases with more samples, since the maximum increases (i.e., more samples, more opportunities to generate a good trajectory), while the median remains stationary. There is a direct connection between the exploration and the maximum reward we can obtain among the samples. The temperature parameter also plays an important role for exploration, as a higher temperature enables sampling more diverse outputs.

**Figure 8** (p. 14): "RLHF impact of the temperature when sampling N outputs and scoring them with a reward model."
- Left panel (SFT): Y-axis: Reward Score (range ~0.1-0.6). X-axis: Number Samples (log scale, 10^0 to 10^2). Lines for different temperatures from T=0.6 to T=1.5. Higher temperatures yield higher max reward at large sample counts; at low sample counts, lower temperatures are better.
- Right panel (RLHF): Y-axis: Reward Score (range ~0.35-0.70). X-axis: Number Samples (log scale, 10^0 to 10^2). Same temperature lines. Optimal temperature shifts compared to SFT; for RLHF, the optimal temperature when sampling between 10 and 100 outputs is T in [1.2, 1.3].
- Key takeaway: RLHF has a direct impact on rescaling the temperature; the optimal temperature is not constant during iterative model updates.

[p. 15] In Figure 8, for a Llama 2-Chat-SFT (left) and a Llama 2-Chat-RLHF (right), the maximum reward curves among N samples (with N in [1, ..., 100]) are reported for different temperatures. The optimal temperature is not constant during the iterative model updates: RLHF has a direct impact on rescaling the temperature. For Llama 2-Chat-RLHF, the optimal temperature when sampling between 10 and 100 outputs is T in [1.2, 1.3]. Given a finite compute budget, it is therefore necessary to re-adjust the temperature progressively. Note that this temperature rescaling happens for a constant number of steps for each model, and always starting from the base model on each new RLHF version.

**Rejection Sampling.** [p. 14] Rejection sampling is performed only with the largest 70B Llama 2-Chat. All smaller models are fine-tuned on rejection sampled data from the larger model, thus distilling the large-model capabilities into the smaller ones.

[p. 14] At each iterative stage, K answers are sampled for each prompt from the most recent model. Each sample is scored given the best reward model accessible at the time of the experiment, and then the best answer is selected for a given prompt. In earlier versions of the model, up to RLHF V3, the approach was to confine answer selection solely to the "bag" of samples gathered from the preceding iteration. For example, RLHF V3 was trained using only samples from RLHF V2. However, despite continuous improvement, this method led to a regression in some capabilities. For example, RLHF V3 struggled more than previous versions to compose rhyming lines in poems, as discerned through qualitative analysis, suggesting that further investigation into the causes of and mitigations for forgetting (Kirkpatrick et al., 2017; Nguyen et al., 2019; Ramasesh et al., 2021) could be a fruitful area for additional future research.

[p. 15] In response, on subsequent iterations, the strategy was modified, incorporating top-performing samples from all prior iterations, such as those used in RLHF-V1 and RLHF-V2. Although no specific figures are presented, this adjustment demonstrated considerable enhancements in performance and effectively addressed the previously noted issues. This mitigation can be seen as analogous to Synnaeve et al. (2019) and Vinyals et al. (2019) in the RL literature.

**PPO.** [p. 15] The language model is further trained following the RL scheme of Stiennon et al. (2020), which uses the reward model as an estimate for the true reward function (human preference) and the pretrained language model as the policy to optimize. During this phase, the objective is:

$$\arg\max_\pi \mathbb{E}_{p \sim \mathcal{D}, g \sim \pi}[R(g \mid p)]$$  (3)

The policy is iteratively improved by sampling prompts p from the dataset D and generations g from the policy pi, and using the PPO algorithm and loss function to achieve this objective.

The final reward function used during optimization:

$$R(g \mid p) = \tilde{R}_c(g \mid p) - \beta D_{KL}(\pi_\theta(g \mid p) \| \pi_0(g \mid p))$$  (4)

This contains a penalty term for diverging from the original policy pi_0. As observed in other works (Stiennon et al., 2020; Ouyang et al., 2022), this constraint is useful for training stability, and to reduce reward hacking whereby high scores from the reward model but low scores from human evaluation would be achieved.

[p. 15] R_c is defined as a piecewise combination of the safety (R_s) and helpfulness (R_h) reward models. Prompts in the dataset are tagged that might elicit potentially unsafe responses and prioritize the scores from the safety model. The threshold of 0.15 is chosen for filtering unsafe responses, corresponding to a precision of 0.89 and a recall of 0.55 evaluated on the Meta Safety test set. The final linear scores are whitened (by reversing the sigmoid with the logit function) in order to increase stability and balance properly with the KL penalty term (beta).

$$R_c(g \mid p) = \begin{cases} R_s(g \mid p) & \text{if IS\_SAFETY}(p) \text{ or } R_s(g \mid p) < 0.15 \\ R_h(g \mid p) & \text{otherwise} \end{cases}$$

$$\tilde{R}_c(g \mid p) = \text{WHITEN}(\text{LOGIT}(R_c(g \mid p)))$$

**PPO Hyperparameters.** [p. 15] For all models:
- Optimizer: AdamW (Loshchilov and Hutter, 2017), with beta_1 = 0.9, beta_2 = 0.95, eps = 10^-5
- Weight decay: 0.1
- Gradient clipping: 1.0
- Constant learning rate: 10^-6
- Batch size: 512 per PPO iteration
- PPO clip threshold: 0.2
- Mini-batch size: 64
- One gradient step per mini-batch
- For 7B and 13B models: beta = 0.01 (KL penalty)
- For 34B and 70B models: beta = 0.005

[p. 16] Training for between 200 and 400 iterations for all models, using evaluations on held-out prompts for early stopping. Each iteration of PPO on the 70B model takes on average approximately 330 seconds. To train quickly with large batch sizes, FSDP (Zhao et al., 2023) is used. This was effective when using O(1) forward or backward passes, but caused a large slow down (approximately 20x) during generation, even when using a large batch size and KV cache. This was mitigated by consolidating the model weights to each node once before generation and then freeing the memory after generation, resuming the rest of the training loop.

## 3.3 System Message for Multi-Turn Consistency [p. 16]

[p. 16] In a dialogue setup, some instructions should apply for all the conversation turns, e.g., to respond succinctly, or to > "act as" [p. 16] some public figure. When such instructions are provided to Llama 2-Chat, the subsequent response should always respect the constraint. However, the initial RLHF models tended to forget the initial instruction after a few turns of dialogue, as illustrated in Figure 9 (left).

**Figure 9** (p. 16): "Issues with multi-turn memory (left) can be improved with GAtt (right)."
- Left panel: System message "Always answer with emojis." User asks "Who are you?" and first response uses emojis. But by the second user turn ("How to go from Paris to NY?"), the model responds with a full text paragraph ignoring the emoji instruction.
- Right panel: Same system message. With GAtt, all responses across multiple turns (4 user turns shown) consistently use emojis only, demonstrating maintained instruction following.

[p. 16] To address these limitations, Ghost Attention (GAtt) is proposed, a very simple method inspired by Context Distillation (Bai et al., 2022b) that hacks the fine-tuning data to help the attention focus in a multi-stage process. GAtt enables dialogue control over multiple turns, as illustrated in Figure 9 (right).

**GAtt Method.** [p. 16] Assume access to a multi-turn dialogue dataset between two persons (e.g., a user and an assistant), with a list of messages [u_1, a_1, ..., u_n, a_n], where u_n and a_n correspond to the user and assistant messages for turn n, respectively. An instruction, *inst*, is defined that should be respected throughout the dialogue. For example, *inst* could be "act as." This instruction is synthetically concatenated to all the user messages of the conversation.

[p. 16] Next, synthetic data is sampled from this using the latest RLHF model. This produces a context-dialogue and the sample with which to fine-tune a model, in a process analogous to Rejection Sampling. Instead of augmenting all context-dialogue turns with the instruction, it can be dropped in all but the first turn, but this would lead to a mismatch at training time between the system message, i.e., all the intermediate assistant messages that come before the last turn, and the sample. To fix this issue, which could hurt the training, the loss is simply set to 0 for all the tokens from the previous turns, including assistant messages.

[p. 16] For the training instructions, a few synthetic constraints are created to sample from: Hobbies ("You enjoy e.g. Tennis"), Language ("Speak in e.g. French"), or Public Figure ("Act as e.g. Napoleon"). To obtain the lists of hobbies and public figures, Llama 2-Chat is asked to generate it, avoiding a mismatch between the instruction and model knowledge (e.g., asking the model to act as someone it had not encountered during training). To make the instructions more complex and diverse, the final instruction is constructed by randomly combining the above constraints.

---
[p. 17 continued]

[p. 17] When constructing the final system message for the training data, the original instruction is also modified half of the time to be less verbose, e.g., "Always act as Napoleon from now" -> "Figure: Napoleon." These steps produce an SFT dataset, on which Llama 2-Chat can be fine-tuned.

**GAtt Evaluation.** [p. 17] GAtt was applied after RLHF V3. A quantitative analysis indicates that GAtt is consistent up to 20+ turns, until the maximum context length is reached (see Appendix A.3.5). The authors tried to set constraints not present in the training of GAtt at inference time, for instance "Always answer with Haiku," for which the model remained consistent as illustrated in Appendix Figure 28.

**Figure 10** (p. 17): "Attention visualization for a dialogue with and without GAtt. We considered the maximum activations across the network and we bin neighboring tokens together."
- Two triangular heatmaps showing attention activations for a dialogue with the system message "Act as Oscar Wilde."
- Left panel ("Baseline before GAtt"): Attention to the system message (left side of the triangle) fades quickly as the dialogue progresses through multiple turns. The system message tokens receive diminishing attention in later turns.
- Right panel ("Baseline after GAtt"): The GAtt-equipped model maintains large attention activations with respect to the system message for a larger portion of the dialogue. The system message tokens retain high attention weights even in later turns.
- Demonstrates that GAtt reshapes attention during fine-tuning so that the model sustains focus on the system message across turns.

[p. 17] Despite its utility, the current implementation of GAtt is described as vanilla, and more development and iteration on this technique could likely further benefit the model. For instance, the model could be taught to change the system message during the conversation by integrating such data during fine-tuning.

## 3.4 RLHF Results [p. 17-19]

### 3.4.1 Model-Based Evaluation [p. 17-18]

[p. 17] Evaluating LLMs is a challenging open-research problem. Human evaluation, while a gold standard, can be complicated by various HCI considerations (Clark et al., 2021; Gehrmann et al., 2023), and is not always scalable. Thus, to select the best-performing models among several ablations at each iteration from RLHF-V1 to V5, the improvement of the rewards from the latest reward models was first observed, to save costs and increase iteration speed. Major model versions were later validated with human evaluations.

**How Far Can Model-Based Evaluation Go?** [p. 17] To measure the robustness of the reward model, a test set of prompts for both helpfulness and safety was collected, and three annotators were asked to judge the quality of the answers based on a 7-point Likert scale (the higher the better). The reward models overall are well calibrated with human preference annotations, as illustrated in Figure 29 in the appendix. This confirms the relevance of using the reward as a point-wise metric, despite being trained with a Pairwise Ranking Loss.

[p. 17-18] Still, as Goodhart's Law states, when a measure becomes a target, it ceases to be a good measure. To ensure the reward measure does not diverge from human preferences, a more general reward was additionally used, trained on diverse open-source Reward Modeling datasets. No such divergence has been observed yet, and the authors hypothesize that iterative model updates may be helping to prevent this.

[p. 18] As a last verification step to ensure no regression between the new model and the previous one, both are used to sample during the next annotation iteration. This enables a model comparison "for free" on new prompts and can help to increase diversity when sampling.

**Progression of Models.** [p. 18] Figure 11 reports the progress of the different SFT and then RLHF versions for both Safety and Helpfulness axes, measured by the in-house Safety and Helpfulness reward models. On this set of evaluations, Llama 2-Chat outperforms ChatGPT on both axes after RLHF-V3 (harmlessness and helpfulness >50%). Despite the aforementioned relevance of using the reward as a point-wise metric, it can arguably be biased in favor of Llama 2-Chat. Therefore, for a fair comparison, the final results are additionally computed using GPT-4 to assess which generation is preferred. The order in which ChatGPT and Llama 2-Chat outputs appeared in the GPT-4 prompt are randomly swapped to avoid any bias. As expected, the win-rate in favor of Llama 2-Chat is less pronounced, although obtaining more than a 60% win-rate for the latest Llama 2-Chat.

**Figure 11** (p. 18): "Evolution of Llama 2-Chat. We show the evolution after multiple iterations fine-tuning for the win-rate % of Llama 2-Chat compared to ChatGPT. Left: the judge is our reward model, which may favor our model, and right, the judge is GPT-4, which should be more neutral."
- Left panel ("Helpfulness — Judge: Meta Reward Models"): X-axis: Helpfulness (10%-90%). Y-axis: Harmlessness (10%-80%). Scatter of labeled points: SFT-v1 (~18% helpfulness, ~20% harmlessness), SFT-v2 (~38%, ~48%), RLHF-v1 (~42%, ~50%), RLHF-v2 (~42%, ~52%), RLHF-v3 (~52%, ~58%), RLHF-v4 (~57%, ~63%), RLHF-v5 (no PPO) (~63%, ~72%), RLHF-v5 (with PPO) (~68%, ~78%).
- Right panel ("Helpfulness — Judge: GPT-4"): Same axes and label set. SFT-v1 (~8%, ~10%), SFT-v2 (~28%, ~30%), RLHF-v1 (~38%, ~45%), RLHF-v2 (~32%, ~35%), RLHF-v3 (~42%, ~40%), RLHF-v4 (~50%, ~48%), RLHF-v5 (no PPO) (~55%, ~58%), RLHF-v5 (with PPO) (~62%, ~65%).
- Both panels show a clear upward trajectory from SFT-v1 through RLHF-v5 (with PPO), with the Meta Reward Models judge showing higher win-rates overall compared to GPT-4.

[p. 18] The prompts used for this evaluation correspond to a validation set of 1,586 and 584 prompts for safety and helpfulness, respectively.

### 3.4.2 Human Evaluation [p. 18-19]

[p. 18] Human evaluation is often considered the gold standard for judging models for natural language generation, including dialogue models. To evaluate the quality of major model versions, human evaluators were asked to rate the Llama 2-Chat models compared to open-source models (Falcon, MPT MosaicML NLP Team et al. (2023), Vicuna Chiang et al. (2023)), as well as closed-source models (ChatGPT (OpenAI, 2023) and PaLM Anil et al. (2023)) on over 4,000 single and multi-turn prompts. For ChatGPT, the gpt-3.5-turbo-0301 model was used in all generations. For PaLM, the chat-bison-001 model was used in all generations. The final prompt count for human evaluations for each model is shown in Table 32. More methodology details are in Appendix, Section A.3.7. The section reports helpfulness results; safety results are presented in Section 4.4.

**Results.** [p. 18-19] As shown in Figure 12, Llama 2-Chat models outperform open-source models by a significant margin on both single turn and multi-turn prompts. Particularly, Llama 2-Chat 7B model outperforms MPT-7B-chat on 60% of the prompts. Llama 2-Chat 34B has an overall win rate of more than 75% against equivalently sized Vicuna-33B and Falcon 40B models.

[p. 19] The largest Llama 2-Chat model is competitive with ChatGPT. Llama 2-Chat 70B model has a win rate of 36% and a tie rate of 31.5% relative to ChatGPT. Llama 2-Chat 70B model outperforms PaLM-bison chat model by a large percentage on the prompt set. More results and analysis is available in Section A.3.7.

**Figure 12** (p. 19): "Human evaluation results for Llama 2-Chat models compared to open- and closed-source models across ~4,000 helpfulness prompts with three raters per prompt."
- A grouped bar chart with 6 comparison groups on the x-axis, each with "Single Turn" and "Multi-Turn" sub-bars:
  1. Llama-2-7b-chat vs. MPT-7b-chat
  2. Llama-2-13b-chat vs. Vicuna-13b-v1.1
  3. Llama-2-34b-chat vs. Vicuna-33b-v1.3
  4. Llama-2-34b-chat vs. Falcon-40b-instruct
  5. Llama-2-70b-chat vs. PaLM-Bison
  6. Llama-2-70b-chat vs. ChatGPT-0301
- Y-axis: Win Rate % (0-100). Bars colored: Win (dark blue), Tie (medium blue), Loss (light blue).
- Key observations: Llama 2-Chat consistently wins against open-source models (groups 1-4) with win rates of ~50-80%. Against PaLM-Bison (group 5), Llama 2-Chat 70B shows a clear win (~60% single turn). Against ChatGPT (group 6), Llama 2-Chat 70B shows a competitive but lower win rate (~36%), with substantial ties (~31.5%).

**Inter-Rater Reliability (IRR).** [p. 19] In the human evaluations, three different annotators provided independent assessments for each model generation comparison. High IRR scores (closer to 1.0) are typically seen as better from a data quality perspective, however, context is important. Highly subjective tasks like evaluating the overall helpfulness of LLM generations will usually have lower IRR scores than more objective labelling tasks.

[p. 19] Gwet's AC1/2 statistic (Gwet, 2008, 2014) was used to measure inter-rater reliability (IRR), as it was found to be the most stable metric across different measurement scenarios. On the 7-point Likert scale helpfulness task used in the analysis, Gwet's AC2 score varies between 0.37 and 0.55 depending on the specific model comparison. Scores on the lower end of that range come from model comparisons with similar win rates to each other (like the Llama 2-Chat-70B-chat vs. ChatGPT comparison). Scores on the higher end come from model comparisons with a more clear winner (like the Llama 2-Chat-34b-chat vs. Falcon-40b-instruct).

**Limitations of human evaluations.** [p. 19] While the results indicate that Llama 2-Chat is on par with ChatGPT on human evaluations, several limitations are noted:

- By academic and research standards, the prompt set of 4k prompts is large. However, it does not cover real-world usage of these models, which will likely cover a significantly larger number of use cases.
- Diversity of the prompts could be another factor in the results. For example, the prompt set does not include any coding- or reasoning-related prompts.
- Only the final generation of a multi-turn conversation is evaluated. A more interesting evaluation could be to ask the models to complete a task and rate the overall experience with the model over multiple turns.
- Human evaluation for generative models is inherently subjective and noisy. As a result, evaluation on a different set of prompts or with different instructions could result in different results.
