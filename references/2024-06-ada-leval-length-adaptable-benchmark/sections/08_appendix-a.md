# Appendix A: Test Case Building Statistics [p. 11]

[p. 11] For each case length on the TSort task, a length upper limit is set for each text segment and the neighboring paragraphs before and after these contiguous chapters. A stride is also set between beginning paragraphs. Table 11 demonstrates the detail statistics on the length upper limit and the stride.

**Table 11** (p. 11): The length upper limit of text segments and stride between beginning paragraphs on TSort.

| Setting | Before | Segments | After | Stride |
|---|---|---|---|---|
| 2k | 200 | 350 | 200 | 64 |
| 4k | 300 | 800 | 300 | 64 |
| 8k | 400 | 1750 | 400 | 64 |
| 16k | 500 | 3700 | 500 | 64 |
| 32k | 500 | 7700 | 500 | 128 |
| 64k | 500 | 15700 | 500 | 128 |
| 128k | 500 | 31700 | 500 | 128 |

On BestAnswer task, two questions are regarded as similar questions when they have 40% of tags in common. Under ultra-long-context settings, both questions should contain at least 1 tag in common. [p. 11]
