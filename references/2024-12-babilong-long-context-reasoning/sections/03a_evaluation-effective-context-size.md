# 3.1 Evaluation of Effective Context Size [p. 5-6]

## Research question [p. 5]

One of the most important questions regarding performance of long-context models is how effectively they utilize the input context. Ideally, a model should maintain uniformly high performance regardless of the input size. For instance, if an LLM can process 128K tokens, it is expected to use all of this context in addressing the user's task. [p. 5]

## Experimental setup [p. 5]

We evaluated the performance of models on question-answering tasks with varying numbers of supporting facts (QA1-QA3) to study how LLMs utilize the available context. Here, we distinguish between a QA task, which requires using facts to answer, and an information retrieval task, which should generate a list of relevant facts or references to information sources. We consider performance satisfactory if the accuracy of an answer exceeds 85% and a completion rate below 30%⁴. [p. 5]

⁴https://huggingface.co/togethercomputer/Llama-2-7B-32K-Instruct
⁵This definition of satisfactory performance is not universal and should be adapted to the specific task at hand.

## Main findings on context utilization [p. 5]

Our benchmarking results show that current LLMs do not efficiently use their full context (Fig. 2). Only 23 out of 34 tested LLMs were able to correctly answer 85% or more of the questions for any of QA1-QA3 tasks in a baseline setting without background distractor text. Even for the simplest task involving a single supporting fact (QA1), the majority of models are only able to efficiently use up to 4K tokens, except for LLama-3.1 and LLama-3.1-8B instruct that can use up to 16K, as well as Qwen-2.5-70b and Gemini Pro 1.5 up to 64K. The range of full context utilization on QA1 varies from 5% to maximum 50%. When facts are embedded within texts, all tested LLMs fail below 85% performance (Fig. 2, QA2). The task with three supporting facts proves to be extremely challenging to current LLMs, with the best scores falling below 80% (Fig. 2, QA3). [p. 5]

**Figure 2** (p. 5): "LLMs struggle to answer questions about facts in texts larger than 10,000 tokens. The plots demonstrate how the performance of selected leading models deteriorates with increasing context size. For single supporting fact questions (QA1), the majority of models perform well up to 4,000 tokens. However, when a correct response requires two (QA2) or three (QA3) facts, LLMs fail to achieve satisfactory accuracy."

Description: Three side-by-side line graphs showing accuracy (%) vs context size (tokens, log scale from 100 to 100000) for QA1 (single supporting fact), QA2 (two supporting facts), and QA3 (three supporting facts). Each graph shows multiple model trajectories:
- QA1: Most models maintain >90% accuracy up to ~4K tokens, then decline. GPT-4, Gemini 1.5 Pro 002, Qwen2.5-72b-instruct, Meta-Llama-3.1-70B-instruct, and Meta-Llama-3.1-8B-instruct show best performance.
- QA2: More rapid decline, with most models dropping below 60% by 10K tokens. Horizontal dashed line at ~30% marks lower performance threshold.
- QA3: Steepest decline, with all models performing poorly beyond a few thousand tokens, mostly below 40% accuracy at 10K+ tokens.

Supports claim: Current LLMs do not efficiently use their full context, with performance declining sharply as length and task complexity increase [p. 5].

## Performance of specific models [p. 5-6]

Going deeper in performance of specific models presented in the Table 2 we found the following. Yarn fails to extend to longer contexts despite showing stable results in long-context language modeling (Peng et al., 2023b). LongChat, Mistral, and both LLama2-7B-32K-instruct models, even when fine-tuned on 32K lengths, failed to perform well on 32K tokens. Activation Beacon performed better than Yarn context extension method for Mistral 7B, but still achieved low results (< 40%) on 32K tokens. In contrast, Mistral-v0.2 and Mistral-v0.1, trained on lengths up to 32K, performed well on these lengths. Yi-9B-200k, trained on sequences up to 200K, shows less than 30% on 64K tokens and more. Yi-34B-200k shows very promising and stable [p. 5]

results on lengths up to 64K, but unfortunately we were not able to run it on 128K tokens. Phi-3-mini drops significantly from 64K to 128K, reaching only 10%, while Phi-3-medium maintains 30% at 128K. Jamba-v1 and Phi-3-mini show close results, but Jamba-v1 does not have drop at 128K and shows 34% on this length. Command-R and Phi-3-medium are the most robust to longer contexts, but start to lose performance more sharply at 128K and 256K. Command-R show results very close to GPT-4 at 32K+ contexts. [p. 6]

We added results for models released since June 2024, including LLama 3.1, Phi 3.5, Qwen 2.5, and GPT-4o-mini. All claim to support 128K context length. Phi-3.5-mini shows improvements mainly for contexts up to 16K. The new Phi-3.5-MoE performs similarly to Phi-3-medium, but with only 6.6B active parameters compared to 14B of Phi-3-medium. LLama-3.1 models show significant improvement: LLama-3.1-8B matches GPT-4o-mini, while LLama-3.1-70B outperforms GPT-4 on longer contexts. Qwen-2.5 models outperform LLama-3.1 of similar size and achieved the best results of all evaluated open LLMs on BABILong. [p. 6]

## Context extension through multistage pre-training [p. 6]

Most of the new models use multistage pre-training with progressively increasing sequence lengths. For example, LLama-3.1 (Dubey et al., 2024) is pre-trained in six stages from 8K to 128K, and only proceeds to larger lengths if it maintains high short context scores and successfully solves the needle-in-a-haystack task. During supervised fine-tuning, LLama-3.1 models mix short context data with synthetic long context data, including question-answering, summarization, and code tasks. [p. 6]
