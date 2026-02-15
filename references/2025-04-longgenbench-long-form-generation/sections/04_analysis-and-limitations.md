# 4 Analysis and Limitations [p. 9–10]

## Richness of Content [p. 9]

Despite efforts to design sub-scenarios that enhance task diversity and richness, the model's outputs tend to converge as output volume increases. This results in a homogenization of recorded events, even when differences in time and location should introduce variety. Such convergence not only degrades overall quality but also diminishes the diversity of the generated content, leading to repetitive and predictable outputs. In our experiments, approximately 45% of long outputs exhibited significant repetition or nearly identical text that was then repeated with only varied time or location prompts. Adjusting parameters like repetition_penalty during inference has shown limited success in mitigating this issue, highlighting the need for more advanced techniques to maintain content richness over long sequences [p. 9].

## Rationality of Content [p. 9]

While our current research focuses primarily on evaluating instruction-following capabilities, a more comprehensive analysis of content rationality and coherence is needed. For example, when tasked with generating a diary for a software engineer, the model should ensure that all recorded activities align with the specified careers. However, in many instances, this logical consistency is lacking. Additionally, temperature records in virtual diaries should reflect realistic temporal changes. For instance, in a San Francisco diary task, we would expect temperatures to vary from cooler (0-10 degrees Celsius) at the beginning of the year to warmer (20-30 degrees Celsius) by mid-year. Yet, the model consistently generates warmer temperatures throughout, even into December. These issues may arise due to the model's limited exposure to temporally varied datasets, particularly in diary or climate-related contexts. Future work could address this by incorporating more domain-specific and temporally annotated data during fine-tuning [p. 9].

## Instruction Data [p. 9–10]

A significant performance discrepancy between models' abilities to handle long-range inputs (such as Ruler (Hsieh et al., 2024)) and their long-form output generation can likely be attributed to the length distribution of instruction-tuning data. Most instruction-tuning datasets are brief, typically under 200 tokens, and lack the extended instructional content necessary for generating longer outputs. This gap suggests that organizing or synthesizing instruction-tuning data with longer, more comprehensive examples could be a valuable direction for future research. Potential solutions

---

[p. 10 continued]

include applying transfer learning techniques from models trained on long-form datasets or using data augmentation methods to synthesize longer instructional content from existing short-form data [p. 10].

## Generalizability [p. 10]

LongGenBench effectively evaluates instruction-following in creative and technical tasks but may not fully capture the creativity and specialized knowledge required for abstract reasoning or unconstrained storytelling. Future versions could include open-ended tasks like creative fiction writing and legal document drafting, which demand intricate narratives and precision. Expanding in this direction would enhance the benchmark's versatility while providing deeper insights into LLMs' capabilities. However, LongGenBench's current focus on instruction adherence offers a strong foundation for evaluating practical, instruction-driven long-form text generation [p. 10].
