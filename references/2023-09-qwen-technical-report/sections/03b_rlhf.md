# 3.2 Reinforcement Learning from Human Feedback [p. 10–11]

[p. 10] While SFT has proven to be effective, its generalization and creativity capabilities may be limited, and it is prone to overfitting. To address this issue, Reinforcement Learning from Human Feedback (RLHF) is implemented to further align SFT models with human preferences, following the approaches of Ouyang et al. (2022); Christiano et al. (2017). This process involves training a reward model and using Proximal Policy Optimization (PPO) (Schulman et al., 2017) to conduct policy training.

## 3.2.1 Reward Model [p. 10–11]

[p. 10] To create a successful reward model, like building a large language model (LLM), it is crucial to first undergo pretraining and then finetuning. This pretraining process, also known as preference model pretraining (PMP) (Bai et al., 2022b), necessitates a vast dataset of comparison data. This dataset consists of sample pairs, each containing two distinct responses for a single query and their corresponding preferences. Similarly, finetuning is also conducted on this type of comparison data, but with a higher quality due to the presence of quality annotations.

### Prompt diversity for reward model finetuning

[p. 10] During the fine-tuning phase, a variety of prompts are gathered and the reward model is adjusted based on human feedback for responses from the QWEN models. To ensure the diversity and complexity of user prompts are properly taken into account, a classification system with around 6600 detailed tags is created and a balanced sampling algorithm is implemented that considers both diversity and complexity when selecting prompts for annotation by the reward model (Lu et al., 2023).

### Response generation for annotation

[p. 10] To generate a wide range of responses, QWEN models of different sizes and sampling strategies are utilized, as diverse responses can help reduce annotation difficulties and enhance the performance of the reward model. These responses are then evaluated by annotators following a standard annotation guideline, and comparison pairs are formed based on their scores.

### Reward model architecture

[p. 10–11] The same-sized pre-trained language model QWEN is used to initiate the process. A pooling layer is incorporated into the original QWEN model to extract the reward for a sentence based on a specific end token.

### Reward model training details

[p. 11] - Learning rate: constant value of 3 x 10^{-6}
- Batch size: 64
- Sequence length: 2048
- Training duration: a single epoch

### Reward model evaluation

[p. 11] The accuracy on the test dataset is adopted as an important but not exclusive evaluation metric for the reward model.

**Table 4: Test Accuracy of QWEN preference model pretraining (PMP) and reward model (RM) on diverse human preference benchmark datasets.**

| Dataset | QWEN Helpful-base | QWEN Helpful-online | Anthropic Helpful-base | Anthropic Helpful-online | OpenAI Summ. | Stanford SHP | OpenAI PRM800K |
|---------|-------------------|---------------------|------------------------|--------------------------|--------------|--------------|----------------|
| PMP     | 62.68             | 61.62               | 76.52                  | 65.43                    | 69.60        | 60.05        | 70.59          |
| RM      | 74.78             | 69.71               | 73.98                  | 64.57                    | 69.99        | 60.10        | 70.52          |

[p. 11] The test pairwise accuracy of PMP and reward models is reported on diverse human preference benchmark datasets (Bai et al., 2022b; Stiennon et al., 2020; Ethayarajh et al., 2022; Lightman et al., 2023). Specifically, QWEN Helpful-base and QWEN Helpful-online are proprietary datasets. The responses in QWEN Helpful-base are generated from QWEN without RLHF, whereas QWEN Helpful-online includes responses from QWEN with RLHF. The results show that the PMP model demonstrates high generalization capabilities on out-of-distribution data, and the reward model demonstrates significant improvement on the QWEN reward datasets.

## 3.2.2 Reinforcement Learning [p. 11]

[p. 11] The Proximal Policy Optimization (PPO) process involves four models: the policy model, value model, reference model, and reward model. Before starting the PPO procedure, the policy model's updates are paused and the focus is solely on updating the value model for 50 steps. This approach ensures that the value model can adapt to different reward models effectively.

### PPO training details

- During the PPO operation, two responses are sampled for each query simultaneously. This strategy has proven to be more effective based on internal benchmarking evaluations.
- KL divergence coefficient: 0.04
- Reward normalization: based on the running mean
- Policy and value model learning rates: 1 x 10^{-6} and 5 x 10^{-6}, respectively
- Value loss clipping with a clip value of 0.15
- Inference policy top-p: 0.9

### Findings on entropy and reward

[p. 11] When top-p is set to 1.0, there is a faster increase in reward, although the entropy is slightly lower than when top-p is set to 0.9. This ultimately results in consistently higher evaluation rewards under similar conditions.

### Pretrained gradient for alignment tax

[p. 11] A pretrained gradient is implemented to mitigate the alignment tax. Empirical findings indicate that, with the specific reward model used, the KL penalty is adequately robust to counteract the alignment tax in benchmarks that are not strictly code or math in nature, such as those that test common sense knowledge and reading comprehension. It is imperative to utilize a significantly larger volume of the pretrained data in comparison to the PPO data to ensure the effectiveness of the pretrained gradient. An overly large value for the pretrained gradient coefficient can considerably impede the alignment to the reward model, eventually compromising the ultimate alignment, while an overly small value would only have a marginal effect on alignment tax reduction.
