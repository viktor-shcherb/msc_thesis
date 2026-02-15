# Appendix A: Models [p. 17]

## Model Selection and Evaluation Criteria

[p. 17] The authors select in total 37 models for evaluation and analysis. The main text results only include aligned models (GPT-4, Gemini-1.5, and 15 open-source models). Besides the aligned models, the authors also evaluate 7 open-source base models using RULER. The authors use the performance of Llama2-7b (base) and Llama2-7b (chat) at context length of 4K as the threshold for determining effective context length. In the analysis section, they evaluate in total 11 models, including model series Yi and LWM, as well as models of novel architectures including Mamba and RWKV.

**Table 4: Information of evaluated and analyzed models in RULER** [p. 17]

| Model | Aligned | Size | Context Length | Huggingface (Wolf et al., 2019) / API |
|-------|---------|------|----------------|---------------------------------------|
| GPT-4 (OpenAI: Josh Achiam et al., 2023) | ✓ | - | 128K | gpt-4-1106-preview |
| Gemini-1.5 (Reid et al., 2024) | ✓ | - | 1M | gemini-1.5-pro |
| Llama3.1 (Meta AI, 2024b) | ✓ | 70B | 128K | meta-llama/Meta-Llama-3.1-70B-Instruct |
| Llama3.1 (Meta AI, 2024b) | ✓ | 8B | 128K | meta-llama/Meta-Llama-3.1-8B-Instruct |
| Command-R-plus (Cohere, 2024) | ✓ | 104B | 128K | CohereForAI/c4ai-command-r-plus |
| Qwen2 (Yang et al., 2024) | ✓ | 72B | 128K | Qwen/Qwen2-72B-Instruct |
| Yi (Young et al., 2024) | ✓ | 34B | 200K | 01-ai/Yi-34B-200K |
| Mixtral-8x22B (Jiang et al., 2024) | ✓ | 39B/141B | 32K | mistralai/Mixtral-8x22B-Instruct-v0.1 |
| Mistral-v0.2 (Mistral AI, 2024a) | ✓ | 7B | 32K | mistralai/Mistral-7B-Instruct-v0.2 |
| GLM4 (GLM et al., 2024) | ✓ | 9B | 1M | THUDM/glm-4-9b-chat-1m |
| GradientAI/Llama3 (Meta AI, 2024a) | ✓ | 70B | 1M | gradientai/Llama-3-70B-Instruct-Gradient-1048k |
| Phi3-medium (Abdin et al., 2024) | ✓ | 14B | 128K | microsoft/Phi-3-medium-128k-instruct |
| LWM (Liu et al., 2024a) | ✓ | 7B | 1M | LargeWorldModel/LWM-Text-Chat-1M |
| DBRX (Databricks, 2024) | ✓ | 36B/132B | 1M | databricks/dbrx-instruct |
| Together (Together AI, 2023b) | ✓ | 7B | 32K | togethercomputer/Llama-2-7B-32K-Instruct |
| LongChat (Li et al., 2023a) | ✓ | 7B | 32K | lmsys/longchat-7b-v1.5-32k |
| LongAlpaca (Chen et al., 2024) | ✓ | 13B | 32K | Yukang/LongAlpaca-13B |
| Mixtral-base (Jiang et al., 2024) | ✗ | 8x7B | 32K | mistralai/Mixtral-8x7B-v0.1 |
| Mistral-base (Mistral AI, 2023) | ✗ | 7B | 32K | alpindale/Mistral-7B-v0.2-hf |
| LWM-base (Liu et al., 2024a) | ✗ | 7B | 1M | LargeWorldModel/LWM-Text-1M |
| LongLoRA-base (Chen et al., 2024) | ✗ | 7B | 100K | Yukang/Llama-2-7b-longlora-100k-ft |
| Yarn-base (Peng et al., 2024) | ✗ | 7B | 128K | NousResearch/Yarn-Llama-2-7b-128k |
| Together-base (Together AI, 2023a) | ✗ | 7B | 32K | togethercomputer/Llama-2-7B-32K |
| Jamba-base (AI21, 2024) | ✗ | 52B | 256K | ai21labs/Jamba-v0.1 |
| Llama2 (chat) (Touvron et al., 2023) | ✓ | 7B | 4K | meta-llama/Llama-2-7b-chat-hf |
| Llama2 (base) (Touvron et al., 2023) | ✗ | 7B | 4K | meta-llama/Llama-2-7b-hf |
| Yi series (Young et al., 2024) | ✓ | 6B,9B | 200K | 01-ai/Yi-(6B,9B)-200K |
| LWM series (Liu et al., 2024a) | ✓ | 7B | 128K,256K,512K | LargeWorldModel/LWM-Text-Chat-(128K,256K,512K) |
| LWM-base series (Liu et al., 2024a) | ✗ | 7B | 32K,128K,256K,512K | LargeWorldModel/LWM-Text-(32K,128K,256K,512K) |
| Mamba (Gu & Dao, 2023) | ✗ | 2.8B | 2K | state-spaces/mamba-2.8b-slimpj |
| RWKV (Peng et al., 2023) | ✗ | 7B | 4K | RWKV/v5-Eagle-7B-HF |

Note: The "Aligned" column uses checkmarks (✓) for aligned/instruction-tuned models and crosses (✗) for base models. Size is given in billions of parameters (B) or as mixture-of-experts notation (e.g., 39B/141B). Context Length shows the maximum context window supported by each model.
