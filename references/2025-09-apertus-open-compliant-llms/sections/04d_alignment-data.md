# 4.1.4 Alignment Data [p. 30–31]

[p. 30] The alignment data consists of prompt-completion pairs that are then assigned rewards (Section 4.3). The data is divided into two subsets corresponding to the two alignment stages: one set of *standard* prompts and completions that are scored by a pretrained reward model (Section 4.3.1), and another set of *controversial* prompts that are assessed for adherence to constitutional values with an LLM-as-judge (Section 4.3.2).

## Prompts [p. 30]

[p. 30] Prompts are taken from the OLMo 2 preference mix,^38 excluding both items that forbid crawling (Appendix B) and those which have a non-permissive license, namely the Flan v2 and No Robots subsets.

In the remaining set, Qwen3-32B is used as a classifier model to label prompts as ideologically controversial. Non-controversial prompts tend to contain technical, factual, or mathematical questions with a single correct answer regardless of ideology; controversial prompts have answers shaped by one's ideological commitments and often have no neutral answer (see Appendix J.3 for details). As a validation step, several prompts and models are tested against 800 human labels collected from volunteers, achieving a final accuracy of [p. 30]

---
[p. 31 continued]

73%. Human validators reached unanimous agreement on 52% of items, had 66% pairwise agreement, and an average majority agreement of 83%.^39 [p. 31]

To the prompts classified as controversial, the Wildchat subset of PolyglotToxicityPrompts (Jain et al., 2024) is added, and then prompts from PRISM (Kirk et al., 2025) falling under the *values-guided* or *controversy-guided* conversation types. [p. 31]

The resulting collection includes 380,537 non-controversial prompts and 72,698 controversial prompts. [p. 31]

## Completions [p. 31]

[p. 31] Five LLMs generate completions for the prompts: Llama 3.1 8B, Llama 3.3 70B, Qwen 2.5 72B, Qwen 3 14B, and Qwen 3 32B.

For the non-controversial prompts, two completions are sampled from each model: one with the default system prompt, and one with a system prompt that encourages the response to be one of the following (each with equal probability): *truthful*, *helpful*, or *honest*^40 (similarly to the pipelines from UltraFeedback; Cui et al. 2024; and Tulu 3; Lambert et al. 2025). A completion with Qwen 2.5 72B is also added, which used a persona based on the Swiss AI Charter, as described in Section 4.3.2 below. In all cases, a temperature of 1 is used to encourage diversity in the completions. 10 responses from the Apertus-SFT model are also sampled to serve as off-policy examples (also with temperature set to 1).^41 After annotating all the aforementioned completions for rewards, two completions are sampled for each prompt in the following manner: one from the completions set whose rewards are higher than all the on-policy completions, and the other from all the completions worse than the 20th percentile of the on-policy completions. This heuristic is adopted because preliminary experiments showed that downstream performance is only weakly dependent on completion quality within a reasonable range, with a slight advantage for selecting completions at the extremes, *i.e.*, those that are nearly the best or nearly the worst. This approach also ensures that both offline completions (typically higher quality, from strong models) and off-policy completions (typically lower quality) are well represented in the training data. [p. 31]

The resulting pairs for each prompt are then used for training both QRPO and, for ablation studies, DPO. For DPO, these pairs naturally serve as "chosen" and "rejected" samples, while for QRPO the samples are used independently, since QRPO is trained on absolute reward signals rather than relative preferences. [p. 31]

For the controversial prompts, completions are generated from the same models, but rather than using principles like "helpfulness," system prompts incorporate samples from the `persona` subset of PersonaHub (Ge et al., 2025) and a persona based on the Swiss AI Charter. As above, 10 responses from the Apertus-SFT model are also included. [p. 31]

---

**Footnotes:**
- ^38: https://huggingface.co/datasets/allenai/olmo-2-0325-32b-preference-mix
- ^39: Annotators are internal to ETH Zurich and EPFL. Items are scored on a scale from 0 (Objective) to 3 (High), then converted into 0 (Objective) and 1 (High) during the ablation stage.
- ^40: We provide the system prompts, taken from Ultrafeedback Cui et al. 2024, in Appendix J.2
- ^41: Technically, the responses are on-policy until training begins.
