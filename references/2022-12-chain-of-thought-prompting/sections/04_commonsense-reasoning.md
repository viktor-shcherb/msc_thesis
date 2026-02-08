# 4 Commonsense Reasoning [p. 7--8]

[p. 7] Although chain of thought is particularly suitable for math word problems, the language-based nature of chain of thought actually makes it applicable to a broad class of commonsense reasoning problems, which involve reasoning about physical and human interactions under the presumption of general background knowledge. Commonsense reasoning is key for interacting with the world and is still beyond the reach of current natural language understanding systems (Talmor et al., 2021).

## Benchmarks [p. 7]

Five datasets covering a diverse range of commonsense reasoning types are considered:

1. **CSQA** (Talmor et al., 2019) -- asks commonsense questions about the world involving complex semantics that often require prior knowledge.
2. **StrategyQA** (Geva et al., 2021) -- requires models to infer a multi-hop strategy to answer questions.
3. **Date Understanding** -- a specialized evaluation set from the BIG-bench effort (BIG-bench collaboration, 2021): involves inferring a date from a given context.
4. **Sports Understanding** -- a specialized evaluation set from BIG-bench (BIG-bench collaboration, 2021): involves determining whether a sentence relating to sports is plausible or implausible.
5. **SayCan** (Ahn et al., 2022) -- involves mapping a natural language instruction to a sequence of robot actions from a discrete set. Figure 3 shows examples with chain of thought annotations for all datasets.

## Prompts [p. 7]

The same experimental setup as in the prior section is followed. For CSQA and StrategyQA, the authors randomly selected examples from the training set and manually composed chains of thought for them to use as few-shot exemplars. The two BIG-bench tasks do not have training sets, so the first ten examples were selected as exemplars in the evaluation set as few-shot exemplars and numbers are reported on the rest of the evaluation set. For SayCan, six examples from the training set used in Ahn et al. (2022) are used and chains of thought are also manually composed.

## Results [p. 7--8]

[p. 7] Figure 7 highlights these results for PaLM (full results for LaMDA, GPT-3, and different model scales are shown in Table 4). For all tasks, scaling up model size improved the performance of standard prompting; chain-of-thought prompting led to further gains, with improvements appearing to be largest for PaLM 540B. With chain-of-thought prompting, PaLM 540B achieved strong performance relative to baselines:

- **StrategyQA:** outperforming the prior state of the art (75.6% vs 69.4%)
- **Sports Understanding:** outperforming an unaided sports enthusiast on sports understanding (95.4% vs 84%)

These results demonstrate that chain-of-thought prompting can also improve performance on tasks requiring a range of commonsense reasoning abilities (though note that gain was minimal on CSQA).

## Figure 7 [p. 7]

**Figure 7** (p. 7): "Chain-of-thought prompting also improves the commonsense reasoning abilities of language models. The language model shown here is PaLM. Prior best numbers are from the leaderboards of CSQA (Talmor et al., 2019) and StrategyQA (Geva et al., 2021) (single-model only, as of May 5, 2022). Additional results using various sizes of LaMDA, GPT-3, and PaLM are shown in Table 4."

The figure shows five line plots arranged horizontally for CSQA, StrategyQA, Date, Sports, and SayCan. Each plot has solve rate (%) on the y-axis and model scale (# parameters in billions: 8, 62, 540) on the x-axis. Four lines/markers are shown:
- Standard prompting (solid line, filled circles)
- Chain of thought (dashed line, open circles)
- Prior supervised best (dashed horizontal line)
- Human (dashed horizontal line, where applicable)

Key observations from the plots:
- **CSQA:** Solve rates ~70--80% range; chain-of-thought prompting shows modest improvement over standard prompting at all scales. Prior supervised best and human performance are in the ~80--90% range.
- **StrategyQA:** Chain-of-thought prompting at PaLM 540B reaches ~75--80%, surpassing prior supervised best (~69%).
- **Date Understanding:** Chain-of-thought prompting at PaLM 540B reaches ~65--70%, well above standard prompting (~40%).
- **Sports Understanding:** Chain-of-thought prompting at PaLM 540B reaches ~95%, above human performance (~84%).
- **SayCan:** Chain-of-thought prompting at PaLM 540B reaches ~85%, substantially above standard prompting (~60%).

