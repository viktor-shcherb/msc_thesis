# Figures

**Figure 1** (p. 2): "Framework of survey. We first list three inherent challenges in Section 2. And then we systematically review related approaches and propose a novel taxonomy with four major categories in Section 3. Next, in Section 4, we organize the evaluation aspect from three perspectives: data, tasks, and metrics based on existing benchmarks. At last, we show our views on future roadmap and open problems in Section 5."

Description: Complex framework diagram showing the structure of the survey paper
- Key elements: The figure is divided into 5 main sections arranged horizontally:
  - Section 2 "Challenges" (top left): Shows "Out-of-distribution (OOD) problems", "Lost in the Middle" Phenomenon, and "Quadratic Complexity"
  - Section 3 "Approaches" (center, largest section): Shows four main categories:
    - 3.1 Positional Encoding: includes variants of rotary position embedding, variants of position attention bias
    - 3.2 Context Compression: shows soft compression (with summary tokens and compression) and hard compression (with selection and summarization components)
    - 3.3 Retrieval Augmented: displays process flow of Retrieve → Concatenation → Attention, with multiple retrieval strategies (sliding window, parallel context, sparse attention)
    - 3.4 Attention Pattern: shows three attention pattern variations (sliding window, parallel context, sparse attention)
  - Section 4 "Evaluation" (top right): Organized into three subsections:
    - 4.1 Data: Length Level, #Examples, Domain
    - 4.2 Tasks: Shows icons for QA, Needle-in-a-Haystack, Statistical tasks, Code, In-Context Learning, Text Generation
    - 4.3 Metrics: Shows symbols for Algorithms, Model-based, LLM-based
  - Section 5 "Future Roadmap and Open Problems" (bottom): Two subsections:
    - 5.1 Approaches: Lists "Method Integration", "Long Text Generation", "Serve System Design", "Length-no-Matter" Issue", "Scalability of Methods"
    - 5.2 Evaluation: Lists "Methods Enabling" ["from Short, Test Long"]", "Trade-off between Information Filtering and Generation Effects", "Knowledge Leakage Issue", "Novel Benchmark Design", "Upgraded LLM-based Metrics"
- Notable patterns: The diagram flows from challenges (top/left) through approaches (center) to evaluation (right) and future directions (bottom), showing a comprehensive taxonomy of the long context domain
- Supports claim: This figure provides the overall structure of the survey and illustrates how the authors categorize approaches into four distinct categories, which is the core contribution mentioned in the introduction

**Figure 2** (p. 20): "Distribution of averaged input #words of datasets in each task. Consistent colors indicate identical categories. The color of each bar refers to the category of the task, with bars of the same color belonging to the same category."

Description: Box plot showing word count distributions across different tasks
- Key elements: Y-axis shows word counts on a logarithmic scale (10², 10³, 10⁴, 10⁵, 10⁶), X-axis lists 18 different tasks grouped by category
- Tasks shown (left to right): QA SinHop, QA MulHop, Re. NIAH, Stat. ArCal, Stat. NumInfo, Stat. SenAgg, Stat. PassCount, Code Compl, Code Run, Code Debug, I.C.L. Few-shot, I.C.L. L.M, TextGen. SinSum, TextGen. MulSum, Others. Reorder, Others. ConCons, Others. SumSource, Others. CharID
- Notable patterns:
  - Most tasks fall in the 10³ to 10⁵ word range
  - I.C.L. Few-shot task shows notably larger context (reaching toward 10⁶)
  - Question Answering tasks (left side) generally have lower word counts (10³ to 10⁴)
  - The color coding groups related task types: consistent colors indicate identical categories, with bars of the same color belonging to the same category
  - Box plots show median, quartiles, and outliers for each task's input length distribution
- Supports claim: This figure provides empirical evidence for the statement in B.2 [p. 19] that "We also count the distribution of input length in each task in Figure 2 to give readers a deeper understanding of different tasks"
