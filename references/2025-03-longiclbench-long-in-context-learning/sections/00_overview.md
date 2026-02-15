# Overview

## Paper Metadata

**Title:** Long-context LLMs Struggle with Long In-context Learning

**Authors:** Tianle Li, Ge Zhang, Quy Duc Do, Xiang Yue, Wenhu Chen

**Affiliations:**
- University of Waterloo (Tianle Li, Wenhu Chen)
- Carnegie Mellon University (Xiang Yue)
- Vector Institute, Toronto (Ge Zhang, Quy Duc Do)

**Contact:** {t29li,wenhuchen}@uwaterloo.ca

**URLs:**
- GitHub: https://github.com/TIGER-AI-Lab/LongICLBench
- OpenReview: https://openreview.net/forum?id=Cy2xlg0e46

**Published:** Transactions on Machine Learning Research (03/2025)

## Abstract

> "Large Language Models (LLMs) have made significant strides in handling long sequences. Some models like Gemini could even be capable of dealing with millions of tokens. However, their performance evaluation has largely been confined to metrics like perplexity and synthetic tasks, which may not fully capture their true abilities in more challenging, real-world scenarios. We introduce a benchmark (LongICLBench) for long in-context learning in extreme-label classification using six datasets with 28 to 174 classes and input lengths from 2K to 50K tokens. Our benchmark requires LLMs to comprehend the entire input to recognize the massive label spaces to make correct predictions. We evaluate on 15 long-context LLMs and find that they perform well on less challenging classification tasks with smaller label space and shorter demonstrations, they struggle in more challenging task like Discovery with 174 labels, suggesting a gap in their ability to process long, context-rich sequences. Further analysis reveals a bias towards labels presented later in the sequence and a need for improved reasoning over multiple pieces of information. Our study reveals that long context understanding and reasoning is still a challenging task for the existing LLMs. We believe LongICLBench could serve as a more realistic evaluation for the future long-context LLMs."

## Section Headings

1. Introduction
2. Related Work
   - Long In-context Learning on LLMs
   - Long Context Techniques over LLMs
   - Long Context Evaluation
   - Extreme-label Classification
3. Long In-context Evaluation
   - 3.1 Long In-context Benchmark
   - 3.2 Model and Experimental Setup
   - 3.3 Experiment Result
4. Exploratory Experiment
   - 4.1 Scattered Distribution
   - 4.2 Grouped Distribution
5. Conclusion
   - Broader Impact Statement
6. References
A. Appendix
   - A.1 Additional Datasets
   - A.2 Prompting Template
   - A.3 Additional Distribution Analysis
   - A.4 Data Accessibility
