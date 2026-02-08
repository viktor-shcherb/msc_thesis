# Appendix B: Data Opt-Out by Applying AI-Crawler Blocks Retroactively [p. 80–81]

[p. 80] To ensure that pretraining data contains only permissive content, the FineWeb and FineWeb-2 datasets are further refined by excluding material from websites that have opted out of being crawled by popular AI crawlers. Specifically, if a website has blocked at least one of the AI crawlers listed below, its content is removed from the datasets.

## List of blocked bots (crawlers)

```
"AI2Bot",           # AI2
"Applebot-Extended", # Apple
"Bytespider",       # Bytedance
"CCBot",            # Common Crawl
"CCBot/2.0",        # Common Crawl
"CCBot/1.0",        # Common Crawl
"ClaudeBot",        # Anthropic
"cohere-training-data-crawler", # Cohere
"Diffbot",          # Diffbot
"Meta-ExternalAgent", # Meta
"Google-Extended",  # Google
"GPTBot",           # OpenAI
"PanguBot",         # Huawei
"*"
```

These removals are applied retroactively to all earlier crawl dumps since 2013 for each corresponding website in the datasets.

## Impact of robots.txt Compliance on Token Counts

**Table B.1** (p. 80): The amount of tokens filtered due to `robots.txt` compliance.

| Dataset | Before filtering | After filtering |
|---|---|---|
| FineWeb-Edu (English) | 4.9T | 4.5T |
| FineWeb-2 (Multilingual) | 47T | 45T |

[p. 80] Tables B.2 and B.3 summarize the number of documents whose owners withheld consent for all AI-user bots. Across both the English and multilingual corpora, GPTBot encountered the highest rate of crawling restrictions. The impact of `robots.txt` compliance on token counts is reported in Table B.1, where a larger token loss is observed in English data. Within the multilingual corpus, token losses are concentrated primarily in high-resource European languages.

## Table B.2: Removed Content from FineWeb (English Corpus)

**Table B.2** (p. 81): Amounts of removed content from FineWeb (English corpus), due to detecting AI crawler blocks and removing content retroactively in all historic crawl parts.

| User Agent | # Documents | String Length |
|---|---|---|
| Any | 2,166,674 | 6,651,679,136 |
| GPTBot | 1,772,197 | 5,507,756,064 |
| CCBot/2.0 | 1,393,545 | 4,327,394,627 |
| CCBot/1.0 | 1,393,481 | 4,325,955,822 |
| CCBot | 1,393,308 | 4,325,579,851 |
| Google-Extended | 1,136,219 | 3,546,644,538 |
| ClaudeBot | 944,635 | 2,788,745,217 |
| Bytespider | 805,820 | 2,374,417,800 |
| Applebot-Extended | 719,728 | 2,043,420,047 |
| Diffbot | 604,731 | 1,796,156,863 |
| Meta-ExternalAgent | 396,052 | 1,126,438,127 |
| AI2Bot | 134,445 | 379,861,906 |
| cohere-training-data-crawler | 57,226 | 154,069,541 |
| PanguBot | 52,381 | 144,140,774 |

## Table B.3: Removed Content from FineWeb-2 (Multilingual Corpus)

**Table B.3** (p. 81): Amounts of removed content from FineWeb-2 (multilingual corpus), due to detecting AI crawler blocks and removing content retroactively in all historic crawl parts.

| User Agent | # Documents | String Length |
|---|---|---|
| Any | 477,587 | 1,362,219,484 |
| GPTBot | 357,519 | 917,798,306 |
| CCBot/2.0 | 236,948 | 702,838,337 |
| CCBot/1.0 | 236,727 | 702,364,875 |
| CCBot | 236,601 | 701,794,846 |
| Bytespider | 162,312 | 552,309,871 |
| ClaudeBot | 158,727 | 456,243,083 |
| Google-Extended | 183,289 | 449,718,843 |
| Diffbot | 65,086 | 227,280,041 |
| Applebot-Extended | 90,969 | 206,990,083 |
| Meta-ExternalAgent | 42,473 | 130,161,736 |
| cohere-training-data-crawler | 25,460 | 86,120,947 |
| AI2Bot | 22,021 | 74,044,873 |
| PanguBot | 20,908 | 73,436,339 |
