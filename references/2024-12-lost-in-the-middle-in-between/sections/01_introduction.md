# 1 Introduction [p. 1-2]

Recent advancements in attention mechanisms, such as Flash Attention (Dao et al., 2023) and Attention with Linear Biases (Press et al., 2022), have ushered in a new generation of language models capable of handling significantly larger context sizes. These developments enable question-answering tasks to be performed over a substantial number of retrieved documents within a single input prompt (as shown in Figure 1).

**Figure 1** (p. 1): "Question Answering setups with documents containing relevant information (green) and distractor documents at different ordinal positions, with both Single-hop (1a) and Multi-hop (1b) questions."

Description: Two diagram panels comparing question answering configurations
- Panel (a): Shows "Previous work" with a single-hop setup containing one gold document with final answer, requiring minimal reasoning
- Panel (b): Shows "We explore models' performance" with multi-hop setup requiring reasoning across multiple evidence documents at different distances (Distance = 0 and Distance = 1 shown)
- Key elements: Documents labeled with position numbers (D-1, D-2, etc.), green highlighting for relevant documents, Query and Question boxes
- Notable patterns: Demonstrates how documents are positioned relative to each other in single vs multi-hop scenarios
- Supports claim: Illustrates the difference between prior work focusing on single pieces of information vs. the paper's focus on multiple distributed pieces

However, despite this remarkable progress, recent studies reveal a critical limitation: long-context models fail to utilize information within their inputs equitably, exhibiting a pronounced bias toward information located at the edges of the context—a problem known as the "lost in the middle" (Liu et al., 2024).

This limitation poses significant challenges for retrieval-augmented generation (RAG) systems, particularly in open-book question-answering scenarios. As the volume of input information increases, so does the likelihood that critical pieces of information necessary for answering a question may be overlooked (Shaier et al., 2024d). This stands in contrast to earlier RAG systems, where documents were processed independently without explicit ordering, resulting in performance that typically improved with the inclusion of more retrieved documents (Izacard and Grave, 2020).

Current efforts to address the "Lost in the Middle" problem primarily focus on approaches like document re-ranking (Peysakhovich and Lerer, 2023; Tang et al., 2023), document length reduction via summarization (Kim et al., 2024), or extending training to include long-context tasks (An et al., 2024). However, these strategies face significant limitations in multi-hop QA settings, where reasoning involves multiple steps across disconnected documents, the number of possible document order permutations grows combinatorially with the number of reasoning steps. This makes re-ranking and extended training approaches increasingly impractical as they would need to account for an overwhelming number of positional combinations. Similarly, the likelihood of omitting essential information during summarization grows with the number of reasoning steps, jeopardizing the integrity of reasoning chains.

In this work, we investigate the "Lost in the Middle" problem within the context of multi-hop QA. We argue that addressing this issue is critical for advancing the field, given the unique challenges it presents to current mitigation strategies. Specifically, we experiment with chain-of-thought (CoT) prompting (Zhou et al., 2023) and document reduction methods to tackle this problem, utilizing recent long-context models such as GPT-3.5-Turbo, MPT-7b-instruct, and Llama-2-7b-longlora. Our key findings include:

1. Performance degradation is not only influenced by the absolute position of information within the context but also by the relative distance between multiple relevant documents.

2. Chain-of-Thought prompting aids in identifying relevant documents but fails to resolve the performance disparity caused by evidence document positions.

3. Existing context reduction methods often produce reasoning chains that are too fragile for effective application in multi-hop QA.

By highlighting these challenges and evaluating potential solutions, this study contributes to research in overcoming the "Lost in the Middle" problem and improving long-context model performance in complex multi-hop reasoning tasks.
