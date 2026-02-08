# References

## Cited works

- **Liu et al. (2023)** — *Lost in the Middle: How Language Models Use Long Contexts.* The NIAH test results empirically confirm the "lost in the middle" phenomenon described in this paper, where models attend more strongly to the beginning and end of context windows while losing information in the middle. Kamradt's GPT-4 and Claude 2.1 results both show this degradation pattern at mid-document depths.

- **OpenAI (2023)** — *GPT-4 Technical Report / GPT-4 Turbo announcement.* GPT-4-128K (GPT-4 Turbo) was the first model tested with NIAH. OpenAI announced the 128K context window at DevDay (November 2023), and Kamradt's test was one of the first independent evaluations of its long-context capabilities.

- **Anthropic (2023)** — *Claude 2.1 release.* Claude 2.1 with its 200K token context window was the second model tested. Anthropic advertised the 200K context window as the largest commercially available at the time, and the NIAH test showed significant retrieval limitations despite the large window.

- **Paul Graham** — *Essays (paulgraham.com).* 49 Paul Graham essays are used as the haystack corpus — the background text into which the needle is inserted. These essays were chosen as generic, unrelated content to test retrieval of a specific planted fact.
