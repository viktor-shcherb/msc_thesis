# Introduction [p. 2]

[p. 2] LLMs hold the promise of fundamentally improving human interaction with the digital world. A crucial feature supporting this evolution is the ability to effectively process long-context inputs.

Until now, LLMs with robust long-context capabilities have been primarily provided through proprietary LLM APIs (Anthropic, 2023; OpenAI, 2023), with no open recipe for building long-context models with on-par downstream performance. Existing open-sourced long-context models (Tworkowski et al., 2023b; Chen et al., 2023; Mohtashami and Jaggi, 2023; MosaicML, 2023b) often fall short on evaluations and primarily measure long-context capabilities with language modeling loss and synthetic tasks, which do not comprehensively demonstrate effectiveness in diverse, real-world scenarios. Additionally, these models often overlook the necessity of maintaining strong performance on standard short-context tasks, either bypassing the evaluations or reporting degenerated performance (Peng et al., 2023; Chen et al., 2023).

## Contributions

[p. 2] The authors describe their approach to build long-context LLMs with superior performance over all existing open-sourced models:

- Models built by continually pretraining from LLAMA 2 checkpoints with additional 400 billion tokens formed as long training sequences
- Smaller 7B/13B variants trained with 32,768-token sequences; 34B/70B variants with 16,384-token sequences
- Extensive evaluation using language modeling, synthetic tasks, and a wide range of real-world benchmarks covering both long and short context tasks
- Language modeling demonstrates a clear power-law scaling behavior with respect to context lengths (Figure 1)
- Compared to LLAMA 2 on research benchmarks: significant improvements on long-context tasks and modest improvements on standard short-context tasks, especially on coding, math, and knowledge benchmarks
- A simple and cost-effective instruction finetuning procedure without human-annotated data produces a chat model that achieves stronger overall performance than gpt-3.5-turbo-16k on long-context benchmarks covering question answering, summarization, and multi-document aggregation tasks

## Paper Outline

[p. 2] The remaining paper presents the continual long-context pretraining approach and a lightweight instruction tuning procedure, followed by detailed results on short and long context tasks. An analysis section discusses positional encodings, length distribution of the dataset, and training curriculum. Finally, responsible safety evaluations are reported, validating that the models largely maintain the safety performance of the original LLAMA 2 series.
