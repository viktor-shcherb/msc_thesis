# Introduction [p. 1-2]

[p. 1] GPT-4 is presented as a large multimodal model capable of processing image and text inputs and producing text outputs. Such models are positioned as important for dialogue systems, text summarization, and machine translation, with substantial interest and progress in recent years [1-34].

A main goal is to improve the ability to understand and generate natural language text in complex and nuanced scenarios. GPT-4 was evaluated on a variety of exams originally designed for humans. It performs quite well and often outscores the vast majority of human test takers. On a simulated bar exam, GPT-4 achieves a score in the top 10% of test takers; GPT-3.5 scores in the bottom 10%. [p. 1]

On traditional NLP benchmarks, GPT-4 outperforms both previous large language models and most state-of-the-art systems (which often have benchmark-specific training or hand-engineering). On the MMLU benchmark [35, 36], an English-language suite of multiple-choice questions covering 57 subjects, GPT-4 outperforms existing models by a considerable margin in English and also demonstrates strong performance in other languages. On translated variants of MMLU, GPT-4 surpasses the English-language state-of-the-art in 24 of 26 languages considered. [p. 1]

[p. 1-2] A key challenge discussed is developing deep learning infrastructure and optimization methods that behave predictably across a wide range of scales. This allowed predictions about GPT-4's expected performance based on small runs trained in similar ways, tested against the final run to increase confidence in training.

[p. 2] Despite its capabilities, GPT-4 has similar limitations to earlier GPT models [1, 37, 38]: it is not fully reliable (e.g., can suffer from "hallucinations"), has a limited context window, and does not learn from experience. Care should be taken when using the outputs of GPT-4, particularly in contexts where reliability is important.

GPT-4's capabilities and limitations create significant and novel safety challenges. The report includes an extensive system card (after the Appendix) describing risks around bias, disinformation, over-reliance, privacy, cybersecurity, proliferation, and more. Interventions to mitigate potential harms include adversarial testing with domain experts and a model-assisted safety pipeline. [p. 2]
