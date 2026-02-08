# 2.2 Tokenization [p. 6]

[p. 6] The design of vocabulary significantly impacts training efficiency and downstream task performance. QWEN uses byte pair encoding (BPE) as the tokenization method, following GPT-3.5 and GPT-4. The starting point is the open-source fast BPE tokenizer, tiktoken (Jain, 2022), with the cl100k base vocabulary.

## Vocabulary augmentation

- The vocabulary is augmented with commonly used Chinese characters and words, as well as those in other languages, to enhance multilingual downstream task performance (particularly Chinese).
- Following Touvron et al. (2023a,b), numbers are split into single digits.
- The final vocabulary size is approximately 152K.

## Compression efficiency

The QWEN tokenizer is evaluated against several other tokenizers: XLM-R (Conneau et al., 2019), LLaMA (Touvron et al., 2023a), Baichuan (Inc., 2023a), and InternLM (InternLM Team, 2023). The findings reveal that QWEN achieves higher compression efficiency than its competitors in most languages, implying that the cost of serving can be significantly reduced since a smaller number of tokens from QWEN can convey more information.

Preliminary experiments confirmed that scaling the vocabulary size of QWEN does not negatively impact downstream performance of the pretrained model. Despite the increase in vocabulary size, experiments show that QWEN maintains its performance levels in downstream evaluation.

**Figure 3** (p. 6): "Encoding compression rates of different models." A bar chart comparing encoding compression rates across approximately 20+ languages (including en, zh, ar, ko, vi, ja, tr, id, pl, ru, nl, pt, it, de, es, fr, etc., and code) for six models: XLM-R, LLaMA-7B, Baichuan-7B, ChatGLM-6B, InternLM-7B, and Qwen. The y-axis shows "Compression Rate" ranging from 0.0 to 3.5, with XLM-R (supporting 100 languages) as the base value 1 (not shown in the figure). QWEN achieves high compression rates for many languages beyond Chinese, English, and code, equipping the model with strong scalability and high training and inference efficiency. 1 million document corpora per language were randomly selected for testing.
