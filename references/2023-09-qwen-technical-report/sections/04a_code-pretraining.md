# 4 CODE-QWEN: Specialized Model for Coding [p. 16]

[p. 16] Training on domain-specific data has been shown to be highly effective, particularly in the case of code pretraining and finetuning. A language model that has been reinforced with training on code data can serve as a valuable tool for coding, debugging, and interpretation, among other tasks. In this work, a series of generalist models have been developed using pretraining and alignment techniques. Building on this foundation, domain-specific models for coding have been created by leveraging the base language models of QWEN, including continued pretrained model, CODE-QWEN, and supervised finetuned model, CODE-QWEN-CHAT. Both models have 14 billion and 7 billion parameters versions.

## 4.1 Code Pretraining [p. 16]

[p. 16] The authors believe that relying solely on code data for pretraining can result in a significant loss of the ability to function as a versatile assistant. Unlike previous approaches that focused solely on pretraining on code data (Li et al., 2022, 2023d), a different approach is taken (Roziere et al., 2023) by starting with the base models QWEN trained on a combination of text and code data, and then continuing to pretrain on code-specific data.

---
[p. 17 continued]

[p. 17] The models are continued pretrained on a total of around 90 billion tokens of code data. During the pre-training phase, the model is initialized using the base language models QWEN. Many applications that rely on specialized models for coding may encounter lengthy contextual scenarios, such as tool usage and code interpretation, as mentioned in Section 3.4. To address this issue, the models are trained with context lengths of up to 8192. Similar to base model training in Section 2.4, Flash Attention (Dao et al., 2022) is employed in the attention modules, and the standard optimizer AdamW (Kingma & Ba, 2014; Loshchilov & Hutter, 2017) is adopted, setting beta_1 = 0.9, beta_2 = 0.95, and epsilon = 10^{-8}. The learning rate is set as 6.0 x 10^{-5} for CODE-QWEN-14B and 3.0 x 10^{-5} for CODE-QWEN-7B, with 3% warm up iterations and no learning rate decays.
