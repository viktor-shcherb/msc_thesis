# 4 Related Work on Long Context Benchmarks and Datasets [p. 8-9]

## Long Range Arena (LRA) [p. 8]

Long Range Arena (LRA) (Tay et al., 2021) was a one of the pioneering benchmarks for long context modeling. LRA is a set of tasks with lengths from 1 to 16 thousand tokens. However, it mainly consists of very specific tasks such as ListOps (2k tokens), Text Classification (4k tokens) and Byte-Level Text Classification (4k tokens) and Byte-Level Text Retrieval (8k tokens), and others that are less related to NLP. They are not well suited for evaluating of modern LLMs without fine-tuning on these tasks and cannot fully represent the capabilities of LLMs that can handle 100k+ tokens. [p. 8]

## Recent long-context benchmarks [p. 8]

A new set of datasets and benchmarks specifically designed to test the ability of LLMs to handle long contexts has been proposed. The LongBench dataset (Bai et al., 2023) contains 6 types of real and synthetic problems, ranging from summarization and multidoc QA to code completion. The average sample lengths in LongBench are from 5k to 15k tokens with 40k tokens at max respectively, with 40k tokens at max. Scrolls and ZeroSCROLLS (Shaham et al., 2022, 2023) consist of QA, classification, summarization tasks and higher average lengths ranging from 1.7k to 49.3k tokens. L-Eval (An et al., 2023) mostly combines 20 smaller long sequence datasets and adds 4 newly annotated tasks, with query-response pairs encompassing diverse question styles and domains. The average length of examples for L-Eval varies from 3 to 60 thousand tokens. Some of the benchmarks are focusing on evaluation of in-context learning and instruction following, such as LongAlign and LongBench-chat (Bai et al., 2024), ZeroScrolls, LongICLBench (Li et al., 2024). [p. 8]

## Long-context datasets with diverse tasks [p. 8-9]

There are other long-context datasets that primarily consist of QA and summarization tasks over texts from Wiki, arXiv, movie or other sources, e.g., InfinityBench (Zhang et al., 2024b), Loople (Li et al., 2023b), Bamboo (Dong et al., 2023), LVEval (Yuan et al., 2024), NovelQA (Wang et al., 2024b), MarathonQA (Jiang et al., 2024), XL²-Bench (Ni et al., 2024), DocFinQA (Reddy et al., 2024), or ChapterBreak (Sun et al., 2022), Ada-LEval (Wang et al., 2024a) that evaluate operations with text up to 1M tokens or multimodal ones like MMBench (Song et al., 2024a). These datasets vary in length, with maximum sample lengths of 646K tokens in ChapterBreak and average lengths reaching 200K tokens in InfinityBench, NovelQA, LVEval, and some subsets of XL²-Bench. [p. 8-9]

## "Needle-in-a-haystack" inspired benchmarks [p. 9]

Further extending of benchmarks' length with real and human annotated data is very challenging. Therefore, "needle-in-a-haystack" inspired benchmarks were proposed. Following LLMTest¹ with magic numbers as needles in Paul Graham essays as haystack, passkey and key-value retrieval tasks are part of InfinityBench (Zhang et al., 2024b). Counting-Stars (Song et al., 2024b) suggests to insert multiple sentences about little penguins that count stars into the same essays for English or The Story of the Stone for the Chinese language along with a query question about count in these "needle" sentences. RULER (Hsieh et al., 2024) extends "needle-in-a-haystack" with multiple types and amount of "needles". RULER and Counting-Stars tend to produce new task categories such as multi-hop tracing and aggregation to test models beyond searching from context. [p. 9]

## Synthetic benchmarks with predefined lengths [p. 9]

Some benchmarks have pre-defined length bins, such as LongBench (0-4k, 4k-8k, 8k+), Ada-LEval (2k-128k), LVEval (16k, 32k, 64k, 128k), S3Eval (2k, 4k, 8k, 16k) (Lei et al., 2023). A number of benchmarks, including RULER, CountingStars, Ada-LEval, and S3Eval, can be generated at required lengths. All these artificial datasets with generated tasks, some of them covering Chinese language (LongBench, InfinityBench, LongAlign, Counting Stars, CLongEval (Qiu et al., 2024), LV-Eval, XL²-Bench). [p. 9]

## BABILong's focus and unique characteristics [p. 9]

BABILong focuses on natural language reasoning over multiple facts distributed in very large textual corpora. Compared to existing approaches it provides more tasks and more natural and deceptive mixing of information into background documents. BABILong consists of diverse set of 20 tasks that cover different capabilities including multi-hop tracing, aggregation over needles and extending them with basic deduction and induction, compositional size reasoning, and path finding. The benchmark goes with predefined splits up to unprecedented 10M token length. Lengths beyond 10M tokens could be generated and we test models up to 50M tokens. Furthermore, while we evaluate models on English-only tasks from bAbI (Weston et al., 2016) adding new languages is straightforward. [p. 9]

¹https://github.com/gkamradt/LLMTest_NeedleInAHaystack
