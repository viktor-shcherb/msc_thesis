# Challenging Long Context Is Under-Explored [p. 4]

Revisiting the works surveyed in §2, they clearly differ with respect to both scope and dispersion.

## With respect to dispersion

The information needed for tasks ranges from easily accessible to highly dispersed and difficult to detect. On low dispersion we have NIAH (Kamradt, 2023; Mohtashami and Jaggi, 2023) and a myriad of factual single-hop QA datasets (Tseng et al., 2016; Kočiský et al., 2017; Kwiatkowski et al., 2019; Dasigi et al., 2021, inter alia) in which the answer is relatively accessible. Adding more snippets of information separated by distractors, either in the form of several needles (Arora et al., 2023; Hsieh et al., 2024) or of hops in a multi-hop question (Trivedi et al., 2022; Zhao et al., 2023), complicates the information detection due to the need to find at least two snippets (Levy et al., 2024), thereby increasing dispersion. Dispersion can also be increased by making the detection of the information less straightforward (e.g., Pang et al., 2022) or requiring aggregation (Shaham et al., 2023). Lastly, summarization tasks are of a very high dispersion (Huang et al., 2021a; Wang et al., 2022), as they require the non-trivial detection of salient facts that are interwoven with the irrelevant text.

## With respect to scope

Tasks overwhelmingly target relatively small scope. In addition to the aforementioned NIAH tasks and their variants, many QA datasets apply as well (Li et al., 2023b; Zhao et al., 2023; Reddy et al., 2024, inter alia). A somewhat higher scope is achieved by datasets for query-based summarization (Zhong et al., 2021; Wang et al., 2022), and QA datasets with more obfuscated answers that require parsing the text surrounding the answer for its verification (An et al., 2023; He et al., 2023). Although much higher on the scope ladder, book summarization is still limited in its scope: datasets include texts that are only of up to 20k tokens (Huang et al., 2021a; Chen et al., 2022a; Shaham et al., 2023). Currently, tasks with the highest scope, requiring information across the entire input length, are artificial and of low dispersion, like common words extraction (Hsieh et al., 2024).

## Conclusion

Figure 2 summarizes the above classification of tasks and datasets. Note that without a concrete definition of dispersion and scope, the plot is only an illustration that involves a good deal of subjective judgements. However, we conclude (1) the majority of tasks designed to challenge LLMs in a long-context setting target either scope or dispersion, such that (2) tasks that push current models' capabilities on both axes are under-represented in the current landscape.

## Figure 2

**Figure 2** (p. 4): This figure illustrates our subjective judgment on the distribution of long-context benchmarks for each task, categorized by their scope and dispersion characteristics, with the four quadrants indicated by the dashed lines. Difficulty is expressed by shade, where red is more difficult and green in easier. Notably, some tasks, like Question-answering (QA), appear in multiple quadrants, as different benchmarks demand varying levels of scope and dispersion (e.g., a single fact versus multiple facts spread across a document). For a detailed breakdown of benchmarks and their task associations, refer to Appendix A.

The figure shows a 2D plot with:
- Horizontal axis: Scope
- Vertical axis: Dispersion
- Four quadrants with color-coded difficulty (green/yellow/orange/red)
- Tasks plotted include: NIAH, QA, NLI, Retrieval, Summarization, Reasoning, Classification, Aggregation, Text Scoring, and others
- Various specific benchmarks are labeled at their positions on the plot
