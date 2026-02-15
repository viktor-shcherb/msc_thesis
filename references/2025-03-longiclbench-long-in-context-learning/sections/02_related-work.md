# Related Work [p. 4]

## Long In-context Learning on LLMs

As pre-trained language models continue to grow in size, in-context learning (ICL) has emerged as a favored approach for addressing a wide array of tasks without the need for extensive fine-tuning (Dong et al., 2023). A body of research has established that increasing the number of examples demonstrations can enhance ICL performance (Liu et al., 2022; Wu et al., 2023). Nonetheless, there are studies indicating that longer input prompts can actually diminish performance (Liu et al., 2023), with the effectiveness of prior large language models (LLMs) being constrained by the maximum sequence length encountered during their training [p. 4].

It is also claimed in previous works that LLM+ICL falls short on specification-heavy tasks due to inadequate long-text understanding ability (Peng et al., 2023c). To counter this issue, various works have introduced memory augmentation and extrapolation techniques to support ICL with an extensive set of demonstrations (Li et al., 2023c; Wang et al., 2023).

## Long Context Techniques over LLMs

The effectiveness of Transformer-based models is hindered by the quadratic increase in computational complexity relative to sequence length, particularly in handling long context inputs. Recent efforts have explored various strategies to address this challenge [p. 4].

Some studies have pursued continued fine-tuning of the LLM with longer context (Rozière et al., 2024; Tworkowski et al., 2023). Others have leveraged position extrapolation or interpolation, building upon relative rotary positional embedding (Su et al., 2021), to extend input length beyond the training phase (Press et al., 2022; Chen et al., 2023a).

Additionally, these works aim to mitigate computational issues, including sliding memory window and chunk segmentation (Hao et al., 2022; Ratner et al., 2023; Zhu et al., 2024). Furthermore, alternative architectures beyond attention explore to handle long inputs more naturally, such as selective-state-spaces models (Peng et al., 2023a; Gu & Dao, 2023). These diverse approaches claim that they can enhance the capabilities of LLMs in processing long context inputs more efficiently.

## Long Context Evaluation

Due to the imperious demands for the support of long-range LLMs, there is a series of benchmarks focusing on long context evaluation [p. 4].

Long-Range Arena (Tay et al., 2021) includes tasks specifically crafted for evaluating sequences ranging from 1K to 16K tokens to evaluate variations of fast Transformers.

LongBench (Bai et al., 2023b) comprises 21 bilingual datasets with an average length of around 6k words, which have been processed in a unified format to enable effortless benchmarking.

L-Eval Benchmark (An et al., 2023) supports 20 sub-tasks with input lengths of 3K to 200K tokens.

LooGLE (Li et al., 2023b) focuses on summarization and long dependency QA tasks with test instances exceeding 100k words.

Most recently, ∞Bench (Zhang et al., 2024) encompasses 12 tasks with an average length of 200K tokens. Another recent work explores the impact of extending input lengths, especially on reasoning tasks (Levy et al., 2024).

## Extreme-label Classification

Extreme-label Classification involves categorizing data into one of an extremely large number of labels, which has been applied in a variety of real-world domains such as emotion classification, named entity recognition, and biological function prediction, each requiring precise differentiation among vast label spaces (Zhang et al., 2017; Sileo et al., 2019; Demszky et al., 2020; Ding et al., 2021) [p. 4].

Previous methods to tackle Extreme-label Classification tasks range from embedding-based approaches to att-tuned retrievals (Bhatia et al., 2015; Vulić et al., 2021). However, integrating this task with long-context large language models presents unique challenges.

The large scale of the label space complicates the in-context learning process, where LLMs are expected to discern fine-grained differences among labels based on extensive context (Milos et al., 2023). These challenges make the proposed LongICLBench with a range of difficulty levels a good testing scenario to evaluate the capability of long-context large language models.
