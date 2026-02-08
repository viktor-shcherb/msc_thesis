# Limitations [p. 8-9]

[p. 8-9] Two main limitations of SCROLLS are identified:

1. **Evaluation of long output texts, specifically in summarization.** Since ROUGE only accounts for *n*gram overlaps, it might downvalue paraphrases of the reference summary that contain the same semantic content. Establishing unbiased, automated metrics for long generations that correlate well with human judgments is an emerging field of research, and the authors note they may decide to replace or complement ROUGE with model-based evaluation in the future.

2. **Monolingual benchmark.** SCROLLS is limited to English. Model evaluation over languages other than English has major significance, affecting the usage of language processing technology in applications worldwide. SCROLLS takes an initial step in standardizing evaluation over long text in general. A natural future direction is establishing benchmarks focusing on other languages as well.
