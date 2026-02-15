# 1 Introduction [p. 1–2]

## Transformer Success and Long Context Challenge

The Transformer architecture (Vaswani, 2017) has made significant progress in many NLP tasks (Devlin, 2018; Radford, 2018; Lewis, 2019; Raffel et al., 2020; Brown, 2020; Chen et al., 2021a; Cobbe et al., 2021), and has become the foundational model of many applications [p. 1].

Large language models can handle tasks involving short texts, within the pre-trained context length. However, current scenarios always involve longer texts, such as:
- Book- or repo-level tasks (Sharma et al., 2019; Liu et al., 2023a; Zhang et al., 2023a; Liu et al., 2023b)
- Dialogue systems with long contexts (Dey et al., 2022; Li et al., 2024a)
- Content-rich in-context learning (Li et al., 2024c) [p. 1]

## Performance Degradation Factors

The performance of pre-trained LLMs degrades and the models often fail to utilize the complete knowledge contained within the long context inputs. This may be caused by three inherent challenges [p. 1]:
1. Out-of-distribution (OOD) problem (Han et al., 2024)
2. "Lost in the Middle" phenomenon (Liu et al., 2024a)
3. Quadratic complexity of attention (Zhou et al., 2024)

Recently, a lot of work has been proposed to improve and evaluate models' ability to handle long contexts in the community [p. 1].

## Survey Scope and Contributions

This survey focuses on approaches and evaluation in the long context domain [p. 1]. The authors systematically review existing related work and, as illustrated in Figure 1, propose a novel taxonomy for approaches, categorizing them into four main groups:
1. Positional encoding
2. Context compression
3. Retrieval augmented
4. Attention pattern [p. 1]

Additionally, the survey focuses on the evaluation aspect and organizes work on data, tasks, and metrics based on existing long context benchmarks [p. 1].

The paper summarizes unresolved issues in the long context domain and puts forward views on future developments [p. 1].

## Distinction from Prior Surveys

There are also some surveys that focus on the long context domain. They each have their own emphasis, but there is no systematic and comprehensive survey of approaches and evaluation in the field of long context, which can provide researchers with a quick and efficient guide [p. 1].

Some surveys only include one part of the methods, lacking a comprehensive overview of the approaches related to long context:
- Zhao et al. (2023) focus on work addressing length extrapolation from the perspective of positional encoding
- Some surveys from the perspective of KV Cache (Li et al., 2025; Shi et al., 2024) [p. 1]

Besides, though some surveys have categorized existing work, their taxonomies are not clear, and there are overlaps between categories. For example:
- Huang et al. (2023) divide the methods for enhancing Transformer architecture models into five categories, but some existing methods can belong to multiple categories
- Pawar et al. (2024) also has this problem, classifying existing techniques into two categories: interpolation and extrapolation
- Some surveys even involve some common methods that are not specifically designed for long contexts [p. 2]

Dong et al. (2023b) provide an overview of the text-processing methods, architectures, special characteristics and application for long context, but they cover some general topics. What's more, these surveys pay little or even no attention to the evaluation aspect [p. 2].

## Focus on Transformer-Based Models

To fill the above gap, this survey proposes a novel and comprehensive taxonomy on both approaches and evaluation aspects. It is worth noting that the focus is on work that applies Transformer-based models to long text tasks, but not improving Transformers nor other architectures at a universal scenario. That is to say, this survey does not cover fields like:
- Long chain-of-thought reasoning (Chen et al., 2025)
- Multimodal long context (Song et al., 2024; Qiu et al., 2024)
- Efficient Transformer (Zhou et al., 2024)
- State Space Model (SSM) (Wang et al., 2024c) [p. 2]

In addition, the long context the authors focus on is the long input content, rather than the introduction of external knowledge in the Retrieval-Augmented Generation (RAG) scenario (Yu et al., 2024; Zhao et al., 2024; Fan et al., 2024) [p. 2].
