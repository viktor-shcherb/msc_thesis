# Appendix Tables: NIAH and Case Studies [p. 19-21]

[p. 19]

## Table 4: Needle-in-a-Haystack Performance Across Document Depths [p. 19]

Table 4: Performance of GPT-4 and 13 community models on the Needle-in-a-Haystack task at various document depths. The document is split into three equal segments: 0-33% depth, 33-66% depth, and 66-100% depth. Peak Failure Depth indicates the document depth at which the most test cases failed for each model. Results are reported at the training length for each model.

| Model | $L_{train}$ | HF PATH | Peak Failure Depth | Acc |
|-------|-------------|---------|-------------------|-----|
| GPT-4-128K | – | – | 0-33.3% | 100.0 |
| **Trained on open-source data** | | | | |
| TinyLlama-1.3B-1T(ours) | 2k | – | 0-33.3% | 56.6 |
| TinyLlama-1.1B-1T | 2k | TinyLlama/TinyLlama-1.1B-intermediate-step-480k-1T | 0-33.3% | 48.0 |
| TinyLlama-1.1B-3T | 2k | TinyLlama/TinyLlama-1.1B-intermediate-step-1431k-3T | 0-33.3% | 80.3 |
| Pythia-1.4b | 2k | EleutherAI/pythia-1.4b | 0-33.3% | 22.5 |
| OpenLlama-3B | 2k | openlm-research/open_llama_3b | 0-33.3% | 85.0 |
| Llama2-7B | 4k | meta-llama/Llama-2-7b | 0-33.3% | 98.0 |
| Llama3-8B | 8k | meta-llama/Llama-3-7b | 0-33.3% | 99.8 |
| Together-base | 32k | togethercomputer/Llama-2-7B-32K | 0-33.3% | 63.0 |
| LWM-base | 32k | LargeWorldModel/LWM-Text-32K | 0-33.3% | 31.8 |
| Mistral-base | 32k | mistralai/Mistral-7B-v0.1 | 0-33.3% | 54.8 |
| Llama3.1-8B | 128k | meta-llama/Meta-Llama-3.1-8B | 0-33.3% | 66.0 |
| Yarn-base | 128k | NousResearch/Yarn-Llama-2-7b-128k | 0-33.3% | 32.4 |
| Yi-6b-200k | 200k | 01-ai/Yi-6B-200K | 0-33.3% | 20.8 |
| Gradient-Llama3-8B | 262k | gradientai/Llama-3-70B-Instruct-Gradient-256k | 0-33.3% | 46.0 |

Key observations:
- GPT-4-128K achieves perfect 100.0% accuracy with peak failure in the 0-33.3% depth range
- Among open-source models, Llama3-8B (8k training) achieves the highest accuracy at 99.8%
- Models with longer training context (128k, 200k, 262k) do not necessarily perform better than shorter context models
- Most models exhibit peak failure in the 0-33.3% document depth range, indicating difficulty with early-context information
- TinyLlama models show varying performance (22.5% to 80.3%) despite similar 2k training lengths

---
[p. 20]

## Table 5: Needle-in-a-Haystack Input Format [p. 20]

Table 5: The input format of the Needle-in-a-Haystack (4-Needle) test where the needles are 6-digit numbers and the haystack is Paul Graham Essays (gkamradt, 2023). The needles we use in this work are numbers to exclude the influence by inner-knowledge following previous work (Zhang et al., 2024c; Mohtashami & Jaggi, 2023; Hsieh et al., 2024; Zhang et al., 2024d)

| Haystack Needles Query | Text |
|------------------------|------|
| | There is an important info hidden inside a lot of irrelevant text. Find it and memorize them. I will quiz you about the important information there.\n\n July 2006I've discovered a handy test for figuring out what you're addicted to. Imagine you were going to spend the weekend at a friend's house on a little island off the coast of Maine. There are no shops on the island and you won't be able to leave while you're there. Also, you've never been to this house before, so you can't assume it will have more than any house might. What, besides clothes and toiletries, do you make a point of packing? That's what you're addicted to... One of the magic numbers is 144231, they're going to issue a public report tracking how this specific tranche of money is spent. NFTs are a new territory, and this way of using them is especially new, but I'm excited about its potential. And I'm excited to see what happens with this particular project, because unlike an NFT project that has already happened, this NFT gets better as the price gets higher. The reserve price was about \$2.5 million, because that's what it takes for the name to be accurate: that's what it costs to... One of the magic numbers is 543171, you can't expect an idea to be novel to everyone. Any insight that you have will probably have already been had by at least one of the world's 7 billion people. But it's sufficient if an idea is novel to a lot of readers. Ditto for correctness, importance, and strength. In effect the four components One of the magic numbers is 264468 And we were always far ahead of them in features. Sometimes, in desperation, competitors would try to introduce features that we didn't have. But with Lisp our development cycle was so fast that we could sometimes duplicate a new feature within a day or two of a competitor announcing it in a press release. By the time journalists covering the press release got round to One of the magic numbers is 423103. If there is a founder community just as there's a VC community. They all know one another, and techniques spread rapidly between them. If one tries a new programming language or a new hosting provider and gets good results, 6 months later half of...\n\n What are the magic numbers mentioned in the provided text?\n The numbers are ✓ |
| **Answer** | [144231, 543171, 264468, 423103] |

Key features of the test:
- Uses 6-digit numbers as needles to avoid inner-knowledge bias
- Needles are embedded in Paul Graham essay text as haystack
- Four needles total in the example shown
- Format includes explicit instruction to find and memorize important information
- Question asks for all magic numbers mentioned
- Answer format is a list of the four 6-digit numbers

---
[p. 21]

## Table 6: Case Study - QA on Llama3 Report [p. 21]

Table 6: QA on the Llama3 report (Llama Team, 2024) using Llama3 STRING and Llama3 RoPE. The input consists of 95,179 tokens after tokenization, with questions primarily from Section 3 of the paper.

| Llama 3 report | Read the following paper about Llama 3. Answer the question based on the paper. \n\n The Llama 3 Herd of Models\n Llama Team, AI @ Meta\n\n A detailed contributor list can be found in the appendix of this paper.\n\n Modern artificial intelligence (AI) systems are powered by foundation models. This paper presents a new set of foundation models, called Llama 3. It is a herd of language models that natively support multilinguality... |
|----------------|---------|
| **Question** | How many long-context training stages does Llama3 have? Please describe them (The answer is in Section 3.4.2 of Llama Team (2024)) |
| Llama 3 RoPE | Llama3 is a large language model developed by Meta AI, and it has several training stages to achieve its impressive performance. The training stages are as follows: 1 Initial Pre-Training: In this stage, Llama3 is pre-trained using AdamW with a peak learning rate of 8X10-5, a linear warm-up of 8,000 steps, and a cosine learning rate schedule decaying to 8x10-7 over 1,200,000 steps. The model is trained on long sequences to support context windows of up to 128K tokens. The model is gradually adapted to the increased context length requirements, starting from the original 8K context window and ending in the final 128K✗(cannot follow instruction) |
| Llama 3 STRING | Llama3 has six stages of long-context training, starting from an 8K context window and ending in a 128K context window. This long-context pre-training stage was performed using approximately 800B training tokens, drawn from the same data repository as Section 3.2 Answer explanation: The question requires the reader to identify the number of long-context training stages for Llama3 and describe them.✓ |
| **Question** | Describe the differences in model architecture between Llama3 and Llama2 (The answer is in Section 3.2 of Llama Team (2024)) |
| Llama 3 RoPE | The paper describes Llama3 as a dense Transformer model with 405B parameters, while Llama 2 is not specified to have a specific model architecture. However, based on the context, it can be inferred that Llama2 is likely a dense Transformer model as well, but with fewer parameters than Llama3. The paper highlights that Llama3 makes minimal architectural modifications to Llama2, suggesting that the main differences between the two models lie in the scale and hyperparameters rather than the architecture itself. ✗(not addressing the question) |
| Llama 3 STRING | The main differences between Llama-3 and Llama-2 are: 1. Llama-3 uses grouped query attention (GQA) with 8 key-value heads to improve inference speed and reduce the size of key-value caches during decoding. 2. Llama-3 uses an attention mask that prevents self-attention between different documents within the same sequence. 3. Llama-3 has a larger vocabulary with 128K tokens, which includes all characters from the tiktoken tokenizer and 28K additional tokens to better support non-English languages. 4. Llama-3 increases the RoPE base frequency hyperparameter to 500,000, which enables better support for longer contexts.✓ |
| **Question** | How does Llama3 perform context parallelism in training (The answer is in Section 3.3.2 of Llama Team (2024)) |
| Llama 3 RoPE | A. By using a combination of tensor parallelism, pipeline parallelism, and data parallelism. B. By using a combination of pipeline parallelism and data parallelism. C. By using a combination of tensor parallelism, pipeline parallelism, and data parallelism. D. By using a combination of context parallelism, pipeline parallelism, and data parallelism.E. By using only data parallelism. Answer: D✗(deviated from the question) |
| Llama 3 STRING | The context parallelism in Llama-3 training is implemented using an all-gather based method, where the key (K) and value (V) tensors are first all-gathered and then the attention output is computed for the local query (Q) tensor chunk. This approach is used to support different types of attention masks, including the document mask, and to balance the communication and computation in the critical path. ✓ |
| **Question** | What are the two criteria used to assess successful adaptation in long-context training (The answer is in Section 3.4.2 of Llama Team (2024)) |
| Llama 3 RoPE | Model performance on short-context evaluations and needle-in-a-haystack tasks. ✓correct but incomplete |
| Llama 3 STRING | The two criteria used to assess successful adaptation in long-context training are: 1. Model performance on short-context evaluations has recovered completely. 2. The model perfectly solves "needle in a haystack" tasks up to that length. These criteria are mentioned in Section 3.4.2 of the paper. ✓ |

Key observations:
- STRING consistently provides more accurate and complete answers compared to RoPE baseline
- RoPE often fails to follow instructions or provides incomplete/deviated answers
- Test uses real long-context document (95,179 tokens) from Llama Team (2024) paper
- Questions target specific technical details from different sections of the paper
- STRING demonstrates better long-range information retrieval and comprehension

---
[p. 22 continued]

## Table 7: Case Study - QA on Llama3 Report (Section 4 Questions) [p. 22]

Table 7: QA on the Llama3 report (Llama Team, 2024) using Llama3 STRING and Llama3 RoPE. The input consists of 95,179 tokens after tokenization, with questions primarily from Section 4 of the paper.

| Llama 3 report | Read the following paper about Llama 3. Answer the question based on the paper. \n\n The Llama 3 Herd of Models\n Llama Team, AI @ Meta\n\n A detailed contributor list can be found in the appendix of this paper.\n\n Modern artificial intelligence (AI) systems are powered by foundation models. This paper presents a new set of foundation models, called Llama 3. It is a herd of language models that natively support multilinguality, coding, reasoning, and tool usage. This paper presents an extensive empirical evaluation of Llama 3. Llama 3 is a dense Transformer model with 405B parameters and a context window of up to 128K tokens. This paper presents an extensive empirical evaluation of Llama 3 Instruct... |
|----------------|---------|
| **Question** | At which stages does the llama3 team average the models (The answer is in Section 4.1.5 of Llama Team (2024)) |
| Llama 3 RoPE | obtained from experiments using various versions of data or hyperparameters at each RM, SFT, or DPO stage? Answer: at each RM, SFT, or DPO stage. The answer is obtained from Section 4.1.6, Iterative Rounds. Rounds✗(not fluent) |
| Llama 3 STRING | The Llama 3 team averages models obtained from experiments using various versions of data or hyperparameters at each RM, SFT, or DPO stage.✓ |
| **Question** | Describe the sources of Llama3's SFT data (The answer is in Section 4.2.2 of Llama Team (2024)) |
| Llama 3 RoPE | Llama3's SFT data is sourced from various places, including human annotations, other NLP tasks, and translated data. Human annotations are collected from linguists and native speakers, and are used to create open-ended prompts that reflect real-world use cases.✗(hallucination! it describes the multilingual SFT data) |
| Llama 3 STRING | In the paper, it is stated that the SFT data is comprised of the following sources: "prompts from our human annotation collection with rejection-sampled responses" and "synthetic data targeting specific capabilities". Additionally, it is mentioned that the SFT data is also comprised of "human-curated data" and "small amounts of human-curated data" for certain capabilities. The Llama3 team used human annotation-based and rule-based techniques to filter out low-quality training samples and improve overall model performance.✓(More details) |
| **Question** | From what is Llama-3's multilingual SFT data derived (The answer is in Section 4.3.2) of Llama Team (2024)) |
| Llama 3 RoPE | Human annotations, data from other NLP tasks, rejection sampled data, and translated reasoning data.✓ |
| Llama 3 STRING | The multilingual SFT data is primarily derived from sources such as human annotations, data from other NLP tasks, rejection sampled data, and translated reasoning data.✓ |
| **Question** | How do the authors verify the long context code reasoning of Llama-3 (The answer is in Section 4.3.4 of Llama Team (2024)) |
| Llama 3 RoPE | They select the most commonly depended-upon files, specifically those referenced by at least five other files, and remove one of these key files from a repository.✗(not addressing the question) |
| Llama 3 STRING | The authors verify the long context code reasoning of Llama-3 by parsing Python files to identify import statements and determine their dependencies. From here, they select the most commonly depended-upon files, specifically those referenced by at least five other files. They remove one of these key files from the repository and instruct the model to identify which files depended on the missing file and to generate the necessary missing code. ✓ |
| **Question** | How does the llama3 team solve the Hallacinations issues (The answer is in Section 4.3.6 of Llama Team (2024)) |
| Llama 3 RoPE | They follow the principle that post-training should align the model to "know what it knows" rather than add knowledge, and generate data that aligns model generations with "facets of factual data present in the pre-training data.✗(not complete) |
| Llama 3 STRING | The llama3 team addresses hallucinations by generating synthetic data with subsets of factual data present in the pre-training data. This data generation process involves extracting a data snippet from the pre-training data, generating factual question about these snippets, sampling responses from the model, scoring the correctness of the generations, scoring the informativeness of the generations, and generating a refusal for responses that are consistently informative and incorrect across the generations. ✓ |

Key observations for Table 7:
- Questions focus on Section 4 (post-training and fine-tuning) details from Llama Team (2024)
- STRING consistently provides more complete and accurate responses than RoPE
- RoPE shows issues with: not following instructions (fluency), hallucination (mixing up different sections), incomplete answers, and not addressing the question directly
- STRING demonstrates superior ability to retrieve specific technical details from different parts of the long document
- Both models tested on same 95,179-token input
