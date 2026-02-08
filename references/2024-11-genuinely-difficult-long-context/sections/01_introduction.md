# Introduction [p. 1–2]

The ability to deal with ever-longer contexts has been one of the most notable trends among the emerging capabilities of large language models (LLMs). Starting with a few hundred tokens as the maximal input length of the first attention-based LLMs (Devlin et al., 2019; Raffel et al., 2020), contemporary models are – technically – able to process up to 128k and even 1M tokens (Gemini Team Google, 2024; OpenAI, 2024).

The demand to evaluate LLMs in this setting has led to a line of research on designing long-context tasks and benchmarks, in order to systematically understand models' capabilities and drive their development. However, the field has generally a sole recurring descriptor to define such measurements by – simply, the length of the context. For example, long-context benchmarks group tasks mostly by length in words (e.g., Shaham et al., 2022; Bai et al., 2023; Zhang et al., 2024b). This leads to qualitatively different measurements being conflated together with conclusions about long-context capabilities being extended from one class of tasks to others. The community is, of course, aware that, for example, tasks which require a small part of the input are different from tasks that require a large part of it. But we ask the more general question: What are the properties that differentiate tasks when conditioned on their long context length? What can we accomplish with such a distinction?

In this position paper, we claim that the current landscape of works on long-context will greatly benefit from a more fine-grained characterization of long-context task design. We argue that judging LLMs by their ability to process long sequences, while disregarding the task they process them for, overlooks the characteristics that make certain inputs more difficult, and interesting to research, to begin with (§2).

For example, Needle in a Haystack tasks (NIAH; Ivgi et al., 2024; Mohtashami and Jaggi, 2023) involve queries whose main challenge is finding the relevant information in a long context, without requiring much further processing. Synthetic NIAH datasets are, of course, easier than their natural equivalents (Ivgi et al., 2023), but the "natural vs. artificial" classification is uninformative in our setting, since it applies equally for tasks regardless of context length. What, then, is an informative property? What makes long-context tasks different from each other? For example, multiple-needle variants of NIAH (Hsieh et al., 2024), or those that position the "needles" closer or farther apart (Levy et al., 2024). Evidently, "the number of tokens in the input" is not a sufficient descriptor.

To resolve this roadblock, we present a taxonomy of long-context tasks for the different factors that make them harder when controlling for context length (§3). This taxonomy is derived by surveying the long-context literature and surfacing the most salient points of distinction between various tasks. We focus on (I) how difficult it is to find and extract the required information from the input (its dispersion in the input), and (II) the absolute quantity of required information to solve the task (its scope). See Figure 1 for a summary.

To understand this categorization and its utility, we review the literature on long-context evaluation and position the works with respect to those factors. We find that the most challenging setting, in which a large quantity of required information is present in a dispersed manner that is difficult to extract, is significantly under-explored (§4).

Finally, acknowledging the inherent and legitimate reasons behind the focus on context length as the sole descriptor of difficulty, we discuss possible paths forward for designing more reliable measurements of long-context capabilities when utilizing a more nuanced vocabulary (§5).

## Figure 1
**Figure 1** (p. 1): A taxonomy of long context tasks based on the distribution of the needed information in the text. Tasks with larger scope and higher dispersion are more difficult (indicated by shade) and more indicative of the long context capabilities of large language models.

The figure shows a 2D plot with:
- Horizontal axis: Scope (How much of the information is necessary?) from Low to High
- Vertical axis: Dispersion (How hard is it to find and extract the necessary information?) from Low to High
- Four quadrants showing different task difficulty levels indicated by color (green/yellow/orange/red shading)
