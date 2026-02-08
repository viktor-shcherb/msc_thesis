# X Thread — Claude 2.1-200K Needle In A Haystack Results [https://x.com/GregKamradt/status/1727018183608193393]

**Type:** twitter-thread
**Fetched:** 2026-02-08
**Priority:** primary

Note: X/Twitter threads cannot be directly fetched via automated tools (require JavaScript rendering). Content below was extracted via ThreadReaderApp mirror ([thread](https://threadreaderapp.com/thread/1727018183608193393.html)).

---

## Context

This thread, posted November 21, 2023, presented the second NIAH test, this time on Anthropic's Claude 2.1 with its 200K token context window — the largest commercially available at the time.

## Test Configuration

- **Model:** Claude 2.1 (Anthropic, 200K token context window)
- **Needle:** "The best thing to do in San Francisco is eat a sandwich and sit in Dolores Park on a sunny day."
- **Retrieval question:** "What is the best thing to do in San Francisco?"
- **Haystack corpus:** Paul Graham essays (concatenated to reach up to 200K tokens, ~470 pages)
- **Test grid:** 35 document depths x 35 context lengths (1K–200K tokens)
- **Evaluator:** GPT-4 via LangChain evaluation framework

## Key Findings

1. **Recall at extreme positions.** At 200K tokens (nearly 470 pages), Claude 2.1 was able to recall facts at some document depths. Top and bottom document positions showed approximately 100% accuracy.

2. **Top vs. bottom placement.** Top placement (beginning of document) performed worse than bottom placement (end of document). This finding was noted by the ThreadReaderApp summary as similar to GPT-4's behavior, though the GPT-4 thread itself emphasized a "beginning-of-document advantage." The discrepancy may reflect different patterns at different context scales, or limitations of the summarized thread content.

3. **Degradation starting around 90K tokens.** Performance degraded significantly starting around 90K tokens, particularly for facts placed at the document's end positions.

4. **Mid-document recall unreliable.** Retrieval from mid-document positions proved unreliable, consistent with the "lost in the middle" phenomenon observed with GPT-4.

5. **Low context lengths not guaranteed.** Performance at low context lengths was not guaranteed to be perfect either, indicating that retrieval failures are not solely a function of context length.

## Cost

- Total test cost: approximately $1,016 in API calls
- Claude 2.1 pricing: $8 per million tokens

## Practical Recommendations (per Kamradt)

- Prompt engineering matters — different prompting approaches can affect retrieval
- Facts are not guaranteed to be retrieved reliably in production applications
- Reducing context when possible improves accuracy
- Strategic positioning of information matters (beginning and second half preferred)

## Comparison with GPT-4-128K

- Both models showed "lost in the middle" degradation patterns
- Both showed positional bias (beginning and end better than middle)
- Claude 2.1 was tested at a larger scale (200K vs 128K tokens) with a finer grid (35x35 vs 15x15)
- The broader test revealed that context window size alone does not guarantee reliable information retrieval

Source: [ThreadReaderApp mirror of X thread](https://threadreaderapp.com/thread/1727018183608193393.html), [Original X thread](https://x.com/GregKamradt/status/1727018183608193393)
