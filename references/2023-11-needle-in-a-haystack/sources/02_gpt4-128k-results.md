# X Thread — GPT-4-128K Needle In A Haystack Results [https://x.com/GregKamradt/status/1722386725635580292]

**Type:** twitter-thread
**Fetched:** 2026-02-08
**Priority:** primary

Note: X/Twitter threads cannot be directly fetched via automated tools (require JavaScript rendering). Content below was extracted via ThreadReaderApp mirror ([thread](https://threadreaderapp.com/thread/1722386725635580292.html)).

---

## Context

This thread, posted November 8, 2023, presented the first public Needle In A Haystack results. Greg Kamradt tested GPT-4-128K's ability to retrieve a planted fact from varying context lengths and document depths.

## Test Configuration

- **Model:** GPT-4-128K (OpenAI)
- **Needle:** "The best thing to do in San Francisco is eat a sandwich and sit in Dolores Park on a sunny day."
- **Retrieval question:** "What is the best thing to do in San Francisco?"
- **Haystack corpus:** Paul Graham essays (49 essays in the repository, concatenated and repeated to reach up to 128K tokens)
- **Test grid:** 15 document depths (0%–100%) x 15 context lengths (1K–128K tokens)
- **Evaluator:** GPT-4 via LangChain evaluation framework

## Key Findings

1. **Performance degradation above 73K tokens.** GPT-4-128K's recall performance started to degrade when context exceeded approximately 73K tokens. Below this threshold, retrieval was generally reliable.

2. **Poor recall at 7%–50% document depth.** Facts placed between 7% and 50% of the document depth showed the lowest recall accuracy. This suggests a "lost in the middle" effect where the model attends more strongly to the beginning and end of the context.

3. **Beginning-of-document advantage.** Information positioned at the very beginning of the document (near 0% depth) showed consistent, reliable recall regardless of context length.

4. **Heatmap visualization.** The results were presented as a 2D heatmap with context length on one axis and document depth on the other, color-coded by retrieval accuracy score (1–10 scale). This visualization format became widely adopted for long-context evaluation.

## Cost

- Total test cost: approximately $200 in API calls
- Individual 128K-token input calls: $1.28 each

## Practical Takeaways (per Kamradt)

- Facts are not guaranteed to be retrieved from large context windows
- Reducing context size improves retrieval accuracy
- Document positioning significantly influences model performance

## Suggested Future Work

Kamradt suggested:
- Sigmoid distribution testing (testing more points in the middle of the depth range where failures concentrate)
- Key-value retrieval validation for additional methodological rigor

Source: [ThreadReaderApp mirror of X thread](https://threadreaderapp.com/thread/1722386725635580292.html), [Original X thread](https://x.com/GregKamradt/status/1722386725635580292)
