# Appendix E: More experiments in LM after pre-training [p. 31]

## Training stability in supervised fine-tuning [p. 31]

To investigate the long-term impacts of attention sink on model behaviors after pre-training, we conduct supervised fine-tuning (SFT) on our pre-trained 1B LMs with softmax attention and sigmoid attention without normalization. Specifically, we utilize the platform¹ to conduct our experiments. The experimental configurations include: the UltraChat dataset (about 200k training samples)² (Ding et al., 2023), learning rate of 2e-5 with cosine scheduling, batch size of 64, each of which contains 2048 tokens, one training epoch. As shown in Figure 30, we monitor the training loss and gradient norm during two LMs during SFT. These two models behave similarly in terms of the above two metrics. Additionally, despite no attention sink, LMs with sigmoid attention without normalization have no issues of training stability during SFT. Though not from the attention sink perspective, a concurrent work by Ramapuram et al. (2024) discussed the theory and practices for Transformer models with sigmoid attention in detail. We refer the readers to Ramapuram et al. (2024) for more analyses.

**Figure 30** (p. 31): The training loss and gradient norm in our 1B LMs with softmax attention and sigmoid attention without normalization in supervised fine-tuning.

Description: Two line plots showing training metrics during fine-tuning over steps (x-axis: 0-2.0k steps).
- Left panel (Train Loss): Shows two overlapping curves for sigmoid (blue) and softmax (orange) attention. Both start around 2.6 and decrease smoothly to ~1.8-2.0, with very similar trajectories. Y-axis: Train Loss (1.6-2.8).
- Right panel (Gradient Norm): Shows two overlapping curves for sigmoid (blue) and softmax (orange) attention. Both start around 1.2-1.4 and decrease to near 0, stabilizing around 0.2-0.4. Y-axis: Gradient Norm (0.0-1.4).
- Key elements: Time series plots with steps (k) on x-axis, training metrics on y-axis
- Notable patterns: Both attention mechanisms show nearly identical training dynamics with smooth convergence and stable gradient norms
- Supports claim: LMs with sigmoid attention without normalization have no training stability issues during supervised fine-tuning despite lacking attention sink

---

¹https://github.com/huggingface/alignment-handbook
²https://huggingface.co/datasets/HuggingFaceH4/ultrachat_200k
