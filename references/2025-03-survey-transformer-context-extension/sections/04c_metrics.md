# 4.3 Metrics [p. 7]

In addition to data and tasks, metrics can directly reflect the model's ability to handle long contexts. With demand for long context task designs gradually changing from classic NLP tasks to more practical tasks, the requirements for metrics are constantly increasing [p. 7].

We categorize metrics for testing models' capabilities on long context according to the three stages of metrics development: Algorithmic Metrics, Model-based Metrics, and LLM-based Metrics. From these three metrics stages, it can be seen that the metrics development trend becomes more and more complex and flexible [p. 7].

## 4.3.1 Algorithmic Metrics [p. 7]

Algorithmic metrics are calculated based on the model output or logits through defined formulas. Their implementation is very simple and can reflect the effect of language modeling and some downstream tasks to a certain extent [p. 7].

Perplexity (PPL) is one of the most common algorithmic metrics for evaluating long context benchmarks (Beltagy et al., 2020; Roy et al., 2021; Press et al., 2021) [p. 7]. Meanwhile, some benchmarks employ other algorithmic metrics such as accuracy, f1, and N-gram-based metrics (ROUGE, Lin, 2004 and BLEU, Papineni et al., 2002, etc.) to evaluate LLMs on downstream tasks (Shaham et al., 2023; Bai et al., 2023; Kasai et al., 2021) [p. 7].

However, these algorithmic metrics have several limitations, such as content quality, syntactic accuracy, and human correlation issues (Reiter and Belz, 2009; Stent et al., 2005; Sun et al., 2021; An et al., 2023; Improving; Tan et al., 2024) [p. 7]. This causes algorithmic metrics to be limited in reflecting the model's ability to process long context. A number of approaches have been developed to improve algorithmic metrics. Such as enhancing scoring techniques, restructuring task formats and so on (Yuan et al., 2024; Dong et al., 2023a; Li et al., 2024b) [p. 7-8].

## 4.3.2 Model-based Metrics [p. 8]

To improve the consistency with human judgments, pre-trained language models are being employed to evaluate (Zhang et al., 2020; Yuan et al., 2021) [p. 8]. Specifically, pre-trained models (such as BERTScore, Devlin, 2018, BART, Lewis, 2019, etc.) are used to calculate the similarity score between the model output and reference text to evaluate the performance of downstream tasks [p. 8].

However, these model-based metrics entirely rely on representations learned from pre-trained language models and require reference texts. They may not be accurate enough for evaluating some novel and creative text generation tasks [p. 8].

## 4.3.3 LLM-based Metrics [p. 8]

Combining the above two metrics issues, LLM-based metrics are proposed, utilizing sufficient knowledge within LLMs for evaluation [p. 8]. For example, LLM-based metrics enable LLMs to offer human-like multi-dimensional assessment (Wang et al., 2023a; Li et al., 2023a; Shen et al., 2023; Chiang et al., 2023; Zhang et al., 2024; Liu et al., 2024; Zheng et al., 2024; Liu et al., 2023c; Tan et al., 2024; Mu et al., 2024a) and interpretable reasoning (Wang et al., 2023b; Luo et al., 2023; Wu et al., 2023) [p. 8].

LLM-based metrics fundamentally distinguish from the other two metrics, which behave much more mechanically. In addition, they demonstrate enhanced agreement with human evaluations (Wang et al., 2023a; Li et al., 2023a) [p. 8]. Due to this high consistency and wider applicability of LLM-based metrics for evaluation, LLM-based metrics are gaining increasing attention in long-context evaluation [p. 8].
