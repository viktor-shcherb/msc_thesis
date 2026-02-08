# 5 Discussion [p. 32–35]

[p. 32] This section discusses interesting properties observed with RLHF (Section 5.1), the limitations of Llama 2-Chat (Section 5.2), and the strategy for responsibly releasing these models (Section 5.3).

## 5.1 Learnings and Observations [p. 32–33]

[p. 32] The tuning process revealed several interesting results, such as Llama 2-Chat's abilities to temporally organize its knowledge, or to call APIs for external tools.

**Figure 20** (p. 32): "Distribution shift for progressive versions of Llama 2-Chat, from SFT models towards RLHF."
- Horizontal stacked area chart with x-axis "Reward Model Score" (0.0 to 1.0) and four rows: SFT (Mix), SFT (Annotation), RLHF (V1), RLHF (V2).
- SFT (Mix) has a broad distribution centered around 0.3-0.5 with a long right tail extending to ~0.8.
- SFT (Annotation) has a similar shape but slightly shifted right.
- RLHF (V1) shifts the mass further right, with a peak around 0.5-0.7.
- RLHF (V2) shifts the distribution even further right, with the bulk of the mass at 0.6-0.9, and the low-scoring left tail is substantially thinned out.
- The progressive versions show the distribution shifting rightward (toward higher reward model scores) and the worst responses (left tail) being progressively removed.

### Beyond Human Supervision [p. 32]

[p. 32] At the outset of the project, many expressed a preference for supervised annotation, attracted by its denser signal. Meanwhile, reinforcement learning, known for its instability, seemed a somewhat shadowy field for those in the NLP research community. However, reinforcement learning proved highly effective, particularly given its cost and time effectiveness. The findings underscore that the crucial determinant of RLHF's success lies in the synergy it fosters between humans and LLMs throughout the annotation process.

[p. 32] Even with proficient annotators, each individual writes with significant variation. A model fine-tuned on SFT annotation learns this diversity, including, unfortunately, the tail-end of poorly executed annotation. Furthermore, the model's performance is capped by the writing abilities of the most skilled annotators. Human annotators are arguably less subject to discrepancy when comparing two outputs' preference annotation for RLHF. Consequently, the reward mechanism swiftly learns to assign low scores to undesirable tail-end distribution and aligns towards the human preference. This phenomenon is illustrated in Figure 20, where the worst answers are progressively removed, shifting the distribution to the right.

[p. 32] In addition, during annotation, the model has the potential to venture into writing trajectories that even the best annotators may not chart. Nonetheless, humans can still provide valuable feedback when comparing two answers, beyond their own writing competencies. Drawing a parallel, while we may not all be accomplished artists, our ability to appreciate and critique art remains intact. The authors posit that the superior writing abilities of LLMs, as manifested in surpassing human annotators in certain tasks, are fundamentally driven by RLHF, as documented in Gilardi et al. (2023) and Huang et al. (2023). Supervised data may no longer be the gold standard, and this evolving circumstance compels a re-evaluation of the concept of "supervision."

### In-Context Temperature Rescaling [p. 32–33]

[p. 32] An intriguing phenomenon related to RLHF is observed, a feature not previously reported to the best of the authors' knowledge: the dynamic re-scaling of temperature contingent upon the context. As indicated in Figure 8, the temperature appears to be influenced by RLHF. Yet, intriguingly, the findings also revealed that the shifts are not uniformly applied across all prompts, as shown in Figure 21.

[p. 32–33] For instance, when it comes to prompts associated with creativity, such as "Write a poem," an increase in temperature continues to generate diversity across various RLHF iterations. This can be observed in the Self-BLEU slope, which mirrors a pattern comparable to that of the SFT model.

[p. 33] On the other hand, for prompts based on factual information, such as "What is the capital of ?" the Self-BLEU slope diminishes over time. This pattern suggests that despite the rising temperature, the model learns to consistently provide the same response to factual prompts.

**Figure 21** (p. 33): "RLHF learns to adapt the temperature with regard to the type of prompt. Lower Self-BLEU corresponds to more diversity: RLHF eliminates diversity in responses to factual prompts but retains more diversity when generating responses to creative prompts."
- Two side-by-side line charts: "Factual Prompts" (left) and "Creative Prompts" (right).
- X-axis = "Temperature" (0.4 to 1.4), Y-axis = "Self-BLEU" (60 to 100).
- Four lines in each: RLHF v3 (blue), RLHF v2 (orange), RLHF v1 (green), SFT (red).
- Factual Prompts (left): SFT line starts around 80 at T=0.4 and decreases to ~65 at T=1.4. RLHF v1 is higher (~88 at 0.4, ~72 at 1.4). RLHF v2 is higher still (~93 at 0.4, ~78 at 1.4). RLHF v3 is the highest, nearly flat at ~95-97 across all temperatures. This means RLHF progressively makes the model respond more consistently to factual prompts regardless of temperature.
- Creative Prompts (right): All four lines are closer together and follow a similar downward slope from ~85-90 at T=0.4 to ~65-75 at T=1.4. RLHF versions show slightly higher Self-BLEU at low temperatures but converge with SFT at higher temperatures. Diversity is retained for creative prompts.
- Each model was prompted with a diverse set of 10 creative and 10 factual instructions and 25 responses were sampled. This is repeated for the temperatures $T \in \{k/10 \mid k \in \mathbb{N} : 1 \le k \le 15\}$. For each of the 25 responses the Self-BLEU metric is computed and the mean and standard deviation against the temperature are reported.

### Llama 2-Chat Temporal Perception [p. 33]

**Figure 22** (p. 33): "Time awareness -- illustration of our model generalizing the notion of time, with 1,000 SFT time-focused data."
- Three example dialogues showing the model adjusting its response based on the stated date:
  - Date: 01/01/2023, Cutting knowledge: 01/01/1940. Q: "Who won the 2nd World War?" A: "I'm not sure what you're referring to, as my knowledge stopped in 1940."
  - Date: 01/01/2023, Year: 2023. Q: "Is the Earth flat or round?" A: "The Earth is round. The idea that the Earth is flat is a myth that has been disproven by scientific evidence..." (detailed explanation).
  - Date: Year: 852. Q: "Is the Earth flat or round?" A: "In 852, the Earth was believed to be flat by many people..." (provides historically contextual answer, noting some ancient Greeks like Eratosthenes believed the Earth was round).

[p. 33] The model showcased impressive generalization ability, as shown in Figure 22. Manually testing dozens of examples, it was observed consistently that the model demonstrates a robust capability to organize its knowledge in a temporal manner, even when provided with minimal data. To instill a concept of time in Llama 2-Chat, a set of 1,000 SFT examples that were related to specific dates was collected. These examples included questions like *"How long ago did Barack Obama become president?"* Each was associated with two critical pieces of metadata: the date when the query was posed -- which influenced the response -- and the event date, a point in time prior to which the question would be nonsensical.

[p. 33] The observation suggests that LLMs have internalized the concept of time to a greater extent than previously assumed, despite their training being solely based on next-token prediction and data that is randomly shuffled without regard to their chronological context.

### Tool Use Emergence [p. 33–34]

[p. 33] The integration of LLMs with tools is a growing research area, as highlighted in Mialon et al. (2023). The approach devised in Toolformer (Schick et al., 2023) entails the sampling of millions of trajectories, complemented by the formulation of few-shot examples for each tool. Nonetheless, this technique was only applied using a single tool per example, and would not scale for a sequence of tool usage.

[p. 34] The release of OpenAI's plugins has incited substantial discourse within the academic community, igniting questions such as: *How can we effectively teach models to utilize tools?* or *Does the process necessitate a substantial dataset?* The experiments indicate that tool usage can spontaneously emerge from alignment in a zero-shot manner. Although tool-use usage was never explicitly annotated, Figure 23 exhibits an instance where the model demonstrated the capability to utilize a sequence of tools in a zero-shot context.

**Figure 23** (p. 34): "Tool use emergence. Llama 2-Chat is able to understand the tools's applications, and the API arguments, just through the semantics, despite never having been trained to use tools."
- A screenshot of a dialog where the model is given access to two tools: SEARCH and CALCULATOR.
- The user asks: "How many years ago did sharks first appear on Earth, compared to trees? Don't be too verbose, I need to print screen the answer for the paper."
- The model chains three API calls:
  1. CALL_API:1: SEARCH | "When did sharks first appear on Earth?" -> "Sharks first appeared on Earth approximately 450 million years ago."
  2. CALL_API:2: SEARCH | "When did trees first appear on Earth?" -> "Trees first appeared on Earth approximately 385 million years ago."
  3. CALL API_3: CALCULATOR | "450 million - 385 million" -> "65 million years."
- The model then provides the final answer: "So, sharks first appeared on Earth approximately 65 million years before trees did."

[p. 34] In addition, the study extended to evaluating the Llama 2-Chat with access to a calculator. The results from this particular experiment are documented in Table 15. LLM tool use, while exciting, can also cause some safety concerns. More community research and red teaming in this area is encouraged.

**Table 15** (p. 34): "Performance with tool use. Evaluation on the math datasets used in Toolformer. For different baselines, we report the scores from Schick et al. (2023)."

| Model | ASDiv | SVAMP | MAWPS |
|---|---|---|---|
| OPT-66B | 6.0 | 4.9 | 7.9 |
| GPT-J | 7.5 | 5.2 | 9.9 |
| GPT-J + CC | 9.6 | 5.0 | 9.3 |
| GPT-3 | 14.0 | 10.0 | 19.8 |
| Toolformer | 40.4 | 29.4 | 44.0 |
| Llama 2-Chat | **67.1** | **69.2** | **82.4** |

## 5.2 Limitations and Ethical Considerations [p. 34–35]

[p. 34] Llama 2-Chat is subject to the same well-recognized limitations of other LLMs, including a cessation of knowledge updates post-pretraining, potential for non-factual generation such as unqualified advice, and a propensity towards hallucinations.

[p. 34] Furthermore, the initial version of Llama 2-Chat predominantly concentrated on English-language data. While experimental observations suggest the model has garnered some proficiency in other languages, its proficiency is limited, due primarily to the limited amount of pretraining data available in non-English languages (as documented in Table 10). Consequently, the model's performance in languages other than English remains fragile and should be used with caution.

[p. 34] Like other LLMs, Llama 2 may generate harmful, offensive, or biased content due to its training on publicly available online datasets. Attempts were made to mitigate this via fine-tuning, but some issues may remain, particularly for languages other than English where publicly available datasets were not available. The authors will continue to fine-tune and release updated versions in the future as progress is made on addressing these issues.

[p. 35] Not everyone who uses AI models has good intentions, and conversational AI agents could potentially be used for nefarious purposes such as generating misinformation or retrieving information about topics like bioterrorism or cybercrime. Efforts were made to tune the models to avoid these topics and diminish any capabilities they might have offered for those use cases.

[p. 35] While the authors attempted to reasonably balance safety with helpfulness, in some instances, the safety tuning goes too far. Users of Llama 2-Chat may observe an overly cautious approach, with the model erring on the side of declining certain requests or responding with too many safety details.

[p. 35] Users of the pretrained models need to be particularly cautious, and should take extra steps in tuning and deployment as described in the *Responsible Use Guide*.

## 5.3 Responsible Release Strategy [p. 35]

### Release Details [p. 35]

[p. 35] Llama 2 is made available for both research and commercial use at https://ai.meta.com/resources/models-and-libraries/llama/. Those who use Llama 2 must comply with the terms of the provided license and the *Acceptable Use Policy*, which prohibit any uses that would violate applicable policies, laws, rules, and regulations.

[p. 35] Code examples to help developers replicate safe generations with Llama 2-Chat and apply basic safety techniques at the user input and model output layers are also provided. These code samples are available at: https://github.com/facebookresearch/llama. Finally, a *Responsible Use Guide* is shared, which provides guidelines regarding safe development and deployment.

### Responsible Release [p. 35]

[p. 35] While many companies have opted to build AI behind closed doors, Llama 2 is being released openly to encourage responsible AI innovation. Based on the authors' experience, an open approach draws upon the collective wisdom, diversity, and ingenuity of the AI-practitioner community to realize the benefits of this technology. Collaboration will make these models better and safer. The entire AI community -- academic researchers, civil society, policymakers, and industry -- must work together to rigorously analyze and expose the risks of current AI systems and to build solutions that address potentially problematic misuse. This approach not only fosters real collaboration with diverse stakeholders -- those beyond the walls of big tech companies -- but also serves as the cornerstone for democratizing access to foundational models. As argued in Zellers et al. (2019b), open releases promote transparency and allow more people to access AI tools, democratizing the technology and decentralizing AI expertise.

> "We believe that the decentralization of AI expertise does more than simply distribute knowledge -- it stimulates innovation and accelerates progress in the industry." [p. 35]

[p. 35] Lastly, openly releasing these models consolidates costs and eliminates barriers to entry, allowing small businesses to leverage innovations in LLMs to explore and build text-generation use cases. Ultimately, the authors believe this will create a more level playing field for organizations of all sizes across the globe to benefit from the economic growth promised by the advancement of AI.

[p. 35] The authors know that not everyone who uses AI models has good intentions, and acknowledge that there are reasonable concerns regarding the ways that AI will impact the world. Toxic content generation and problematic associations are meaningful risks that the AI community has yet to fully mitigate. As this paper illustrates, strides have been made in limiting the prevalence of these types of responses. While recognizing there is more work to be done, this realization only deepens the commitment to open science and collaboration with the AI community.
