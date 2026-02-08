# Related Work [p. 2-4]

## Long-Context Techniques [p. 2-3]

[p. 2] Methodologies primarily focus on three key areas: more efficient attention mechanisms, divide-and-conquer paradigms, and scalable position embedding techniques.

**Efficient Attention Mechanisms.** Notable advancements in attention within Transformers achieved by several studies (Zaheer et al., 2020; Guo et al., 2021; Dao et al., 2022b; Ding et al., 2023). A key development is Flash Attention (Dao et al., 2022a), which streamlines the attention process by circumventing the need to read and write the attention matrix across different memory tiers, resulting in faster processing and reduced memory usage compared to traditional attention methods. In LongNet, Ding et al. (2023) introduces Dilated Attention, which reduces the computation complexity of attention to nearly linear and scales to 1 billion tokens. However, Liu et al. (2023a) identified a limitation where these mechanisms tend to falter with the middle portions of long texts.

[p. 3] **Divide-and-Conquer.** WebGPT (Nakano et al., 2021) addresses long-form QA by interacting with a text-based web-browsing environment. PEARL (Sun et al., 2023) introduces a framework that prompts LLMs to generate and execute plans for tackling complex long-text reasoning tasks. Chen et al. (2023a) constructs a memory tree with the summarization of document segments and navigates on the memory tree to answer the original question.

**Scalable Position Embeddings.** Scalable position embeddings have been instrumental in extending the context window of LLMs. RoPE (Su et al., 2021) utilizes a rotation matrix to enhance positional information, integrating explicit relative position dependencies into the self-attention mechanism. ALiBi (Press et al., 2021) does not add position embeddings to word embeddings, instead applying a linearly decreasing penalty to attention scores based on key-query distances. Position Interpolation (Chen et al., 2023b) adopts a different strategy by linearly scaling down input position indices to align with preset context window sizes, requiring few fine-tuning steps. NTK-aware Scaled RoPE and ReRoPE (Su, 2023) further combine the benefits of position interpolation and length extrapolation methods without any fine-tuning steps.

## Long-Context Language Models [p. 3]

Building on advancements in long-context techniques, several long-context LLMs are developed and released:
- Llama 2 (Touvron et al., 2023) integrates RoPE to expand its context window to 4,000 tokens.
- Vicuna-v1.5 (Zheng et al., 2023) further extends this capability by fine-tuning Llama 2 on high-quality, extensive conversations, increasing the context window to 16,000 tokens.
- Longchat (Li* et al., 2023) models condense RoPE to utilize model weights learned in the pretraining stage.
- ChatGLM2-32k (Zeng et al., 2022) is trained on a 32,000-token context length using position interpolation.

Proprietary language models have seen even more significant advancements. GPT-4-Turbo (OpenAI, 2023) extends its context window to 128,000 tokens. Claude-2 and Claude-2.1 have achieved context lengths of 100,000 and 200,000 tokens respectively. Kimi Chat, developed by Moonshot.ai, claims to handle up to 200,000 Chinese characters. However, no existing dataset can evaluate the capability in tackling such long texts.

## Long-Context Benchmarks [p. 3-4]

[p. 3] Efforts to evaluate the long-context capabilities of language models have been intensifying, with a focus primarily on traditional QA and summarization tasks. NarrativeQA (Kočiskỳ et al., 2018) offers a QA dataset built on entire books from Project Gutenberg and movie transcripts. GovReport (Huang et al., 2021) provides a dataset comprising national policy issues, each accompanied by an expert-written summary. SCROLLS (Shaham et al., 2022) introduces a suite of datasets that requires models to process and reason over long contexts.

[p. 4] Concurrently, L-Eval (An et al., 2023) and LongBench (Bai et al., 2023) are designed for comprehensive evaluation of long-context capabilities of LLMs. L-Eval offers a collection of long documents across different domains and provides both close-ended and open-ended tasks. LongBench is a bilingual long context benchmark covering six task categories. Most tasks in these benchmarks are traditional QA and summarization with fixed document, questions and answers. They are inflexible on text length (up to ~32,000 tokens), which fall short of adapting to ultra-long context evaluation. Additionally, LongBench uses mostly open-ended tasks with traditional F1 and ROUGE metric that may not align well with human judgments. In contrast, the authors' benchmarks support length-adaptable evaluation, provide sufficient cases and evaluate models using accuracy metrics, avoiding inconsistencies with human evaluation.
