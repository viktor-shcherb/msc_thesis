# Appendix D: Training Dataset Details [p. 33–34]

[p. 33] Most of the component data sources for the RWKV World v2 dataset are used intact, with no upor down-sampling done so all tokens are given equal weighting. Recent works have demonstrated the impact that automated data mixing can have on pretraining (Albalak et al., 2023; Xie et al., 2024), but we leave this as an exploration for future work. Some sub-sampling is done for overrepresented languages within a few data sources. All tokens are given equal weighting unless otherwise noted in Table 9.

## Table 9: Dataset Components [p. 34]

| Dataset | Domain | Dataset | Domain |
|---------|--------|---------|--------|
| Wikipedia^a | Encyclopedia | marianna13/vault_text | Books |
| SlimPajama | Web | marianna13/random_quora | Forums |
| peSzo | Academia | marianna13/zlib | Books |
| BigPatent | Patents | minipile | Various |
| Pile of Law | Legal, Administrative | tatoeba | Multilingual Translations |
| StarCoder^b | Code | poetry-foundation | Poetry |
| OSCAR23.01^c | Multilingual Web | proof-pile | Academia: Math |
| TED2020 | Transcripts: TED, TEDx | reddit-math | Forums: Math |
| PhilPapers | Academia: Philosophy | soda | Dialogue |
|  |  | song_lyrics | Lyrics |
|  |  | TinyStories | Stories |
| NIH-ExPORTER | Grants: NIH | walkthroughs2020 | Game Walkthroughs |
| EuroParl | Multilingual Legal |  |  |
| Enron-Emails | Emails | wikihow-qa-16k | How-To |
| Ubuntu IRC | Chat | Alpaca | Various |
| HackerNews | Forums | camel-ai/math | Math |
| OpenWebText2 | Web | camel-ai/code | Code |
| Gutenberg PG-19 | Books | camel-ai/physics | Physics |
| Books3 | Books | camel-ai/chemistry | Chemistry |
| OpenSubtitles | Subtitles | camel-ai/ai_society | Job Roles |
| YTSubtitles | Subtitles | camel-ai/biology | Biology |
| ao3_skylion | Stories | Dolly | Various |
| honeyfeed-3600 | Stories | Evol-Instruct | Various |
| scribble-17k | Stories | gpt4all | Code |
| syosetu711k | Stories (Japanese) | Guanaco | Various Multilingual |
| marianna13/fanfics | Stories |  |  |
| marianna13/gamedev | Forums | LaMini | Various |
| marianna13/ta-books | Books | oasst1 | Multilingual Conversations |
| marianna13/libgen | Textbooks, Books |  |  |
| marianna13/research_gate | Academia | ShareGPT | Conversations |
| marianna13/superuser | Forums | UltraChat | Conversations |
| marianna13/the-eye | Books | BELLE 10M Chinese | Various Chinese |

Caption: Components of the RWKV World v2 dataset, their source links, and their domains.
^a For Wikipedia, we include all languages from date 04/01/2023, with certain overrepresented languages randomly subsampled (see wiki.txt in the supplementary material for exact amounts)
^b For StarCoder, we included only those datasets with at least 10 stars
^c For OSCAR23.01, we include non-English languages only, with certain languages randomly subsampled (see oscar.txt in the supplementary material for exact amounts)

### Table 10: RWKV World v2 dataset component citations [p. 34]

| Component | Citation |
|-----------|----------|
| SlimPajama | Soboleva et al. (2023) |
| StarCoder | Li et al. (2023b) |
| OSCAR23.01 | Suárez et al. (2019) |
| TED2020 | Reimers & Gurevych (2020) |
| the Pile | Gao et al. (2020) |
| Evol-Instruct | Xu et al. (2023) |
