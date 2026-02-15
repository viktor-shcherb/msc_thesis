# Appendix E: Gemini Evaluation [p. 20]

We evaluated the Gemini 1.5 Pro 002 model on the QA1 task of BABILong. We were requesting model responses via API, some of the requests were denied due to built-in content safety filtering, even with BLOCK_NONE set. In Fig. 6, we only report results for requests where the model did not refused to response. We present the results for both that as the context size increases, the model can refuse to respond up to 14% of the time. We used 1000 samples for lengths up to 32K, for larger lengths we used 100 samples per length. [p. 20]

**Figure 6** (p. 20): "Results of Gemini 1.5 Pro 002 evaluations. Built-in content safety filtering causes up to 14% of requests to be denied with increased context size. Without rejected means that we removed from evaluation all cases where the model refused to answer. Few-shot means that we used instructions with in-context examples."

Description: Two side-by-side heatmaps showing accuracy percentages
- Left panel: "Few shot (without rejected)" - shows Gemini-1.5-pro-002 performance
- Right panel: "Few shot" - shows performance including rejected requests
- Key elements: Both heatmaps show context size (x-axis: 0k to 2M) vs. qa1 tasks (y-axis: qa-1 to qa-5), with color coding from red (low accuracy ~0%) to green (high accuracy ~100%)
- Notable patterns: Left panel shows generally higher accuracy (60-100% range in green/yellow) across most context sizes; right panel shows more degradation (more red/orange) especially at longer context lengths due to rejected requests; accuracy decreases as context size increases in both panels
- Supports claim: Content safety filtering impacts evaluation, and performance degrades with context length even when accounting for rejections [p. 20]

Retreival-augmented Llama-3 has a strong advantage of being able to perform on any context length up to 10M tokens. On QA4 and QA5 this approach allows it to match and even surpass weaker competitors on longer context sizes. However, on QA2 and QA3 this approach fails dramatically. The reason for this performance drop lies in inability to retrieve to maintain the critical found sentences, complicating the task for the underlying Llama. Additionally, relevant sentences in these tasks are not always semantically similar to the question, preventing the model from retrieving all necessary facts for correct reasoning. [p. 20]

It is important to note, that all BABILong tasks are in practice solvable even with smaller models. Finetuned RMT, ARMT, and Mamba achieve outstanding scores across most sequence lengths, significantly outperforming LLMs despite having up to 100 times ewer parameters. Mamba has an advantage on medium-length sequences, but recurrent memory models (RMT and ARMT) excel in processing much larger sequences up to 10M tokens. [p. 20]
