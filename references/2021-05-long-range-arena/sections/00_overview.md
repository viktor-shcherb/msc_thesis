# Overview [p. 1]

**Title:** Long Range Arena: A Benchmark for Efficient Transformers

**Authors:** Yi Tay^1*, Mostafa Dehghani^1*, Samira Abnar^1, Yikang Shen^1, Dara Bahri^1, Philip Pham^1, Jinfeng Rao^1, Liu Yang^1, Sebastian Ruder^2, Donald Metzler^1
(*First two authors contributed equally.)

**Affiliations:**
1. Google Research
2. Google DeepMind

**Contact:** {yitay, dehghani}@google.com

**Venue:** Preprint (arXiv:2011.04006v1)

**Date:** 8 Nov 2020

**Code:** https://github.com/google-research/long-range-arena

## Abstract

> "Transformers do not scale very well to long sequence lengths largely because of quadratic self-attention complexity. In the recent months, a wide spectrum of efficient, fast Transformers have been proposed to tackle this problem, more often than not claiming superior or comparable model quality to vanilla Transformer models. To this date, there is no well-established consensus on how to evaluate this class of models. Moreover, inconsistent benchmarking on a wide spectrum of tasks and datasets makes it difficult to assess relative model quality amongst many models. This paper proposes a systematic and unified benchmark, Long-Range Arena, specifically focused on evaluating model quality under long-context scenarios. Our benchmark is a suite of tasks consisting of sequences ranging from 1K to 16K tokens, encompassing a wide range of data types and modalities such as text, natural, synthetic images, and mathematical expressions requiring similarity, structural, and visual-spatial reasoning. We systematically evaluate ten well-established long-range Transformer models (Reformers, Linformers, Linear Transformers, Sinkhorn Transformers, Performers, Synthesizers, Sparse Transformers, and Longformers) on our newly proposed benchmark suite. Long-Range Arena paves the way towards better understanding this class of efficient Transformer models, facilitates more research in this direction, and presents new challenging tasks to tackle. Our benchmark code will be released at https://github.com/google-research/long-range-arena." [p. 1]

## Section Headings

1. Introduction [p. 1]
2. Long-Range Arena (LRA) [p. 2]
   - 2.1 Desiderata [p. 2]
   - 2.2 Tasks [p. 3]
     - 2.2.1 Long ListOps [p. 3]
     - 2.2.2 Byte-level Text Classification [p. 3]
     - 2.2.3 Byte-level Document Retrieval [p. 3]
     - 2.2.4 Image Classification on Sequences of Pixels [p. 4]
     - 2.2.5 Pathfinder (Long-Range Spatial Dependency) [p. 4]
     - 2.2.6 Pathfinder-X (Long-Range Spatial Dependencies with Extreme Lengths) [p. 4]
   - 2.3 Required Attention Span of LRA Tasks [p. 5]
3. Experimental Results [p. 5]
   - 3.1 Models [p. 5]
   - 3.2 Philosophy Behind the Benchmark [p. 5]
   - 3.3 Quantitative Results [p. 6-7]
   - 3.4 Efficiency Benchmarks [p. 7]
   - 3.5 Overall Results: No One-Size-Fits-All [p. 8]
4. Related Work [p. 8-9]
   - 4.1 Efficient Transformers [p. 8]
   - 4.2 Existing Benchmarks [p. 8-9]
5. Conclusion [p. 9]
6. Acknowledgements [p. 9]
References [p. 9-12]
A. Appendix [p. 13-15]
   - A.1 LRA Tasks [p. 13]
     - A.1.1 ListOps [p. 13]
     - A.1.2 Byte-level Document Classification [p. 13]
     - A.1.3 Byte-level Document Matching [p. 13]
   - A.2 Image Classification [p. 13]
     - A.2.1 Generalization Gap [p. 13-14]
     - A.2.2 Visualizations of Learned Embedding by a Vanilla Transformer [p. 14-15]
   - A.3 Pathfinder [p. 15]
     - A.3.1 Visualization of the Attention Maps from a Vanilla Transformer [p. 15]
B. Models and Implementation [p. 16]
   - B.1 A Brief Overview of Model Implementations [p. 16]
   - B.2 Special Cases of our Implementation [p. 16]
C. Recommendations for Fair Comparison [p. 16]
