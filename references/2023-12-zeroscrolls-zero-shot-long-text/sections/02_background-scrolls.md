# 2 Background: SCROLLS [p. 2]

SCROLLS (Shaham et al., 2022) was introduced as a long text understanding benchmark. Its datasets were curated, cleaned, and reformatted to a single input-output format allowing for easy and fast usage, with every example containing a single long document, such as a scientific paper or a book. [p. 2]

Since its launch, SCROLLS has facilitated significant progress, including:
- New pretraining objectives (Tay et al., 2023)
- Adaptations of short-text models to long sequences (Phang et al., 2022; Xiong et al., 2022; Ivgi et al., 2023; Bertsch et al., 2023)
- Dedicated long sequence models pretrained from scratch (Guo et al., 2022; Ainslie et al., 2023)

All the aforementioned methods eventually fine-tune a specialized model for every single task in SCROLLS, a setting that remains important for many applications. However, in the modern era of general purpose, zero-shot reasoning LLMs, a new evaluation setup is required, where this dependence on task-specific fine-tuning is alleviated. [p. 2]
