# 7. Memorization and Privacy [p. 9]

Large language models may, under particular circumstances, be vulnerable to attacks causing the model to produce memorized training data (Nasr et al., 2023). To study susceptibility to such attacks and quantify memorization, the models are evaluated for verbatim and approximate memorization as was done in several prior studies (Anil et al., 2023; Carlini et al., 2022; Gemini Team, 2024; Kudugunta et al., 2023). [p. 9]

The evaluation setting of Gemma Team (2024) is followed, which tests for (50 token) memorizations of training data given a prompt of 50 tokens. Overall memorization rates are compared across a uniform sample of the entire dataset, using both an exact match criteria and approximate match criteria (Ippolito et al., 2022) using an edit distance of 10%. [p. 9]

> "This work uses a very restricted definition of 'memorization': whether a model can be induced to generate near-copies of some training examples when prompted with appropriate instructions." [p. 9, footnote 1]

## Verbatim Memorization [p. 9]

Results are in Figure 1. Gemma 2 memorizes significantly less than prior models at a similar size, with memorization rates below 0.1% (note the log y-axis). The memorization breakdown by data source shows that, similar to Gemma 1, Gemma 2 memorizes more from code, wiki, and science sources, and also that it memorizes significantly less across the board (again, note the log y-axis). [p. 9]

## Approximate Memorization [p. 9]

Figure 1 also presents approximate memorization by data source. While approximate memorization is higher than exact, the rate of memorization is still low. The approximate memorization of Gemma 2 is much lower than even the exact memorization of Gemma 1. The increase in approximate memorization is much lower than prior models; in some cases no lift at all was observed (c.f. Gemma Team, 2024, Figure 4) (note that no bar indicates no increase, i.e., the rate of approximate memorization equals that of exact memorization). [p. 9]

**Figure 1** (p. 9): "Comparing memorization rates. **We find significantly lower memorization rates across-the-board.** (Left) Overall memorization across model families. (Right) Exact and approximate memorization per data source."

The left panel is a bar chart with log y-axis showing "% Exact Memorized" for several models (Gemma 1 2B, Gemma 1 9B [unclear: exact model names on x-axis partially obscured], Gemma 2 variants). Gemma 2 models show memorization rates below 0.1%, substantially lower than Gemma 1 and other models. The right panel shows a grouped bar chart with log y-axis showing "% Memorized" broken down by data source (Code, Multilingual, Science, Wiki). For each source, bars represent Exact 2B, Exact 9B, Exact 27B, Approx 2B, Approx 9B, Approx 27B. Code and wiki sources show highest memorization rates; all rates are very low (below 0.1 on the log scale). [p. 9]

## Personal Data [p. 9]

The same prevention methods at training time and the same evaluations as Gemma Team (2024) are used. Google Cloud Sensitive Data Protection Tool is used to find potential instances of personal data. The many categories of personal data (e.g., phone numbers, account numbers) are classified into three severity levels. Memorized outputs are analyzed using these severity levels. [p. 9]

No instances of high-severity data being emitted were found, and a very low rate of 0.00026% of memorized data was found to contain lower-severity personal information. These automated tools are known to incur false positives because they do not account for context, meaning the results are likely overestimates. [p. 9]
