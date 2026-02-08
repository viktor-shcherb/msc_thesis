# 1 Introduction [p. 1-2]

[p. 1] In the rapidly evolving domain of NLP, the race towards higher model performance often necessitates an escalation in model size, which tends to increase computational costs and inference latency, raising barriers to deployment in practical, real-world scenarios.

**Core contribution:** Mistral 7B demonstrates that a carefully designed language model can deliver high performance while maintaining efficient inference. [p. 1]

**Performance claims:**
- Mistral 7B outperforms the previous best 13B model (Llama 2 [26]) across all tested benchmarks
- Surpasses the best 34B model (LLaMa 34B [25]) in mathematics and code generation
- Approaches the coding performance of Code-Llama 7B [20] without sacrificing performance on non-code related benchmarks

**Architectural choices:**
- Grouped-query attention (GQA) [1]: significantly accelerates inference speed and reduces memory requirement during decoding, allowing for higher batch sizes and hence higher throughput -- a crucial factor for real-time applications
- Sliding window attention (SWA) [6, 3]: designed to handle longer sequences more effectively at a reduced computational cost, alleviating a common limitation in LLMs

[p. 2] **Release and deployment:**
- Released under the Apache 2.0 license
- Accompanied by a reference implementation facilitating easy deployment either locally or on cloud platforms such as AWS, GCP, or Azure using the vLLM [17] inference server and SkyPilot
- Integration with Hugging Face is streamlined for easier integration
- Crafted for ease of fine-tuning across a myriad of tasks
- A chat model fine-tuned from Mistral 7B significantly outperforms the Llama 2 13B -- Chat model

> "Through our work, our aim is to help the community create more affordable, efficient, and high-performing language models that can be used in a wide range of real-world applications." [p. 2]
