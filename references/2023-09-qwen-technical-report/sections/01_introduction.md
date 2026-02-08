# Introduction [p. 3-4]

[p. 3] LLMs (Radford et al., 2018; Devlin et al., 2018; Raffel et al., 2020; Brown et al., 2020; OpenAI, 2023; Chowdhery et al., 2022; Anil et al., 2023; Thoppilan et al., 2022; Touvron et al., 2023a,b) have revolutionized AI by providing a powerful foundation for complex reasoning and problem-solving tasks. These models compress vast knowledge into neural networks, making them versatile agents. With a chat interface, LLMs can perform tasks previously thought exclusive to humans, especially those involving creativity and expertise (OpenAI, 2022; Ouyang et al., 2022; Anil et al., 2023; Google, 2023; Anthropic, 2023a,b). They can engage in natural language conversations, answer questions, provide information, and generate creative content. This has led to a wide range of applications from chatbots and virtual assistants to language translation and summarization tools.

LLMs are not limited to language tasks; they can also function as generalist agents (Reed et al., 2022; Bai et al., 2022a; Wang et al., 2023a; AutoGPT, 2023; Hong et al., 2023), collaborating with external systems, tools, and models to achieve objectives. LLMs can understand multimodal instructions (OpenAI, 2023; Bai et al., 2023; Liu et al., 2023a; Ye et al., 2023; Dai et al., 2023; Peng et al., 2023b), execute code (Chen et al., 2021; Zheng et al., 2023; Li et al., 2023d), use tools (Schick et al., 2023; LangChain, Inc., 2023; AutoGPT, 2023), and more.

**Figure 1** (p. 3): "Model Lineage of the Qwen Series." A flowchart showing the relationship between QWEN models. QWEN (the base pretrained model) branches into: QWEN-PMP (which leads to QWEN-RM), QWEN-CHAT (which leads to QWEN-CHAT-RLHF), CODE-QWEN (which leads to CODE-QWEN-CHAT), MATH-QWEN-CHAT, and QWEN-VL (which leads to QWEN-VL-CHAT). Models are color-coded: grey for Pretrain Models, green dashed for RM Models, blue for SFT Models, yellow for RLHF Models. The multimodal LLM QWEN-VL and QWEN-VL-CHAT (Bai et al., 2023) are also based on QWEN base models.

[p. 3-4] Despite impressive capabilities, LLMs are often criticized for lack of reproducibility, steerability, and accessibility. The authors present the initial version of the QWEN series. QWEN is a moniker deriving from the Chinese Qianwen, meaning "thousands of prompts." QWEN is a comprehensive language model series with distinct models at varying parameter counts, including base pretrained language models, chat models finetuned with SFT and RLHF, and specialized models in coding and math.

## Key contributions

[p. 4] The contributions are outlined as five points:

1. The base language models, QWEN, have undergone extensive training using up to 3 trillion tokens of diverse texts and codes. They consistently demonstrate superior performance across a multitude of downstream tasks, even compared to significantly larger counterparts.

2. QWEN-CHAT models have been carefully finetuned on a curated dataset for task performing, chat, tool use, agent, safety, etc. Benchmark evaluation shows SFT models achieve superior performance. Reward models were trained to mimic human preference and applied in RLHF. Through human evaluation, QWEN-CHAT models trained with RLHF are highly competitive, still falling behind GPT-4 on their benchmark.

3. Specialized models CODE-QWEN (CODE-QWEN-7B and CODE-QWEN-14B) and their chat variants (CODE-QWEN-14B-CHAT and CODE-QWEN-7B-CHAT). CODE-QWEN has been pre-trained on extensive datasets of code and further fine-tuned for code generation, debugging, and interpretation. Results on HumanEval (Chen et al., 2021), MBPP (Austin et al., 2021), and HumanEvalPack (Muennighoff et al., 2023) demonstrate high proficiency.

4. MATH-QWEN-CHAT specifically designed for mathematical problems. Both MATH-QWEN-7B-CHAT and MATH-QWEN-14B-CHAT outperform open-sourced models in the same sizes with large margins and are approaching GPT-3.5 on GSM8K (Cobbe et al., 2021) and MATH (Hendrycks et al., 2021).

5. Open-sourced QWEN-VL and QWEN-VL-CHAT for visual and language instructions, outperforming current open-source vision-language models across various benchmarks, supporting text recognition and visual grounding in both Chinese and English (Bai et al., 2023).

[p. 4] The 14B-parameter and 7B-parameter base pretrained models QWEN and aligned chat models QWEN-CHAT are officially open-sourced. GitHub: https://github.com/QwenLM/Qwen.

## Report structure

[p. 4] Section 2 describes pretraining approach and results. Section 3 covers alignment methodology and reports automatic and human evaluation results, including tool use, code interpreter, and agent. Sections 4 and 5 cover specialized coding and math models. Section 6 provides related work overview. Section 7 concludes.
