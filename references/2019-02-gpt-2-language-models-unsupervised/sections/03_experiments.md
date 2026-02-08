# 3. Experiments [p. 4-6]

[p. 4] Four LMs trained and benchmarked with approximately log-uniformly spaced sizes. Architectures summarized in Table 2. The smallest model is equivalent to the original GPT, and the second smallest equivalent to the largest model from BERT (Devlin et al., 2018). The largest model, GPT-2, has over an order of magnitude more parameters than GPT. The learning rate of each model was manually tuned for the best perplexity on a 5% held-out sample of WebText. All models still underfit WebText and held-out perplexity has as of yet improved given more training time. [p. 4]

## 3.1. Language Modeling [p. 4-5]

[p. 4-5] Evaluates zero-shot domain transfer on the primary task -- language modeling. Since the model operates on a byte level and does not require lossy pre-processing or tokenization, it can be evaluated on any language model benchmark. Results on language modeling datasets are commonly reported as perplexity (scaled or exponentiated version of the average negative log probability per canonical prediction unit -- usually a character, a byte, or a word). The authors compute the log-probability of a dataset according to a WebText LM and divide by the number of canonical units. [p. 4-5]

For many of these datasets, WebText LMs would be tested significantly out-of-distribution, having to predict aggressively standardized text, tokenization artifacts such as disconnected punctuation and contractions, shuffled sentences, and even the string `<UNK>` which is extremely rare in WebText -- occurring only 26 times in 40 billion bytes. [p. 5]

Main results reported in Table 3 using invertible de-tokenizers which remove as many tokenization/pre-processing artifacts as possible. These de-tokenizers are invertible so log probability can still be calculated; they can be thought of as a simple form of domain adaptation. Gains of 2.5 to 5 perplexity observed for GPT-2 with these de-tokenizers. [p. 5]

WebText LMs transfer well across domains and datasets, improving the state of the art on 7 out of the 8 datasets in a zero-shot setting. Large improvements noticed on small datasets such as Penn Treebank and WikiText-2 (only 1 to 2 million training tokens). Large improvements also noticed on datasets measuring long-term dependencies like LAMBADA (Paperno et al., 2016) and the Children's Book Test (Hill et al., 2015). The model is still significantly worse than prior work on the One Billion Word Benchmark (Chelba et al., 2013), likely due to it being both the largest dataset and having the most destructive pre-processing (1BW's sentence level shuffling removes all long-range structure). [p. 5]

**Table 3** (p. 5): "Zero-shot results on many datasets. No training or fine-tuning was performed for any of these results. PTB and WikiText-2 results are from (Gong et al., 2018). CBT results are from (Bajgar et al., 2016). LAMBADA accuracy result is from (Hoang et al., 2018) and LAMBADA perplexity result is from (Grave et al., 2016). Other results are from (Dai et al., 2019)."

|         | LAMBADA (PPL) | LAMBADA (ACC) | CBT-CN (ACC) | CBT-NE (ACC) | WikiText2 (PPL) | PTB (PPL) | enwik8 (BPB) | text8 (BPC) | WikiText103 (PPL) | 1BW (PPL) |
|---------|---------------|---------------|--------------|--------------|-----------------|-----------|--------------|-------------|-------------------|-----------|
| SOTA    | 99.8          | 59.23         | 85.7         | 82.3         | 39.14           | 46.54     | 0.99         | 1.08        | 18.3              | **21.8**  |
| 117M    | 35.13         | 45.99         | 87.65        | 83.4         | 29.41           | 65.85     | 1.16         | 1.17        | 37.50             | 75.20     |
| 345M    | **15.60**     | 55.48         | **92.35**    | 87.1         | **22.76**       | 47.33     | 1.01         | **1.06**    | 26.37             | 55.72     |
| 762M    | **10.87**     | 60.12         | **93.45**    | 88.0         | **19.93**       | **40.31** | **0.97**     | 1.02        | 22.05             | 44.575    |
| 1542M   | **8.63**      | **63.24**     | **93.30**    | **89.05**    | **18.34**       | **35.76** | **0.93**     | **0.98**    | **17.48**         | 42.16     |

Bold values indicate results that improve over SOTA.

## 3.2. Children's Book Test [p. 5]

[p. 5] The Children's Book Test (CBT) (Hill et al., 2015) examines LM performance on different categories of words: named entities, nouns, verbs, and prepositions. Rather than perplexity, CBT reports accuracy on an automatically constructed cloze test (predict which of 10 possible choices for an omitted word is correct). Following the LM approach introduced in the original paper, the authors compute the probability of each choice and the rest of the sentence conditioned on this choice according to the LM, and predict the one with the highest probability. [p. 5]

Performance steadily improves as model size increases and closes the majority of the gap to human performance (as shown in Figure 2). Data overlap analysis: one of the CBT test set books, The Jungle Book by Rudyard Kipling, is in WebText, so results reported on the validation set which has no significant overlap. [p. 5]

GPT-2 achieves new state of the art results of 93.30% on common nouns and 89.05% on named entities. A de-tokenizer was applied to remove PTB style tokenization artifacts from CBT. [p. 5]

**Figure 2** (p. 5): "Performance on the Children's Book Test as a function of model capacity. Human performance are from Bajgar et al. (2016), instead of the much lower estimates from the original paper."

Two panels (Common Nouns, Named Entities). X-axis: # of parameters in LM (117M, 345M, 762M, 1542M). Y-axis: Accuracy. Both panels show accuracy increasing with model size, approaching human performance (dashed line). Bajgar et al. (2016) baseline shown as a dotted line below human level.

## 3.3. LAMBADA [p. 5-6]

[p. 5] The LAMBADA dataset (Paperno et al., 2016) tests the ability of systems to model long-range dependencies in text. The task is to predict the final word of sentences which require at least 50 tokens of context for a human to successfully predict.

GPT-2 improves the state of the art from 99.8 (Grave et al., 2016) to 8.6 perplexity and increases LM accuracy from 19% (Dehghani et al., 2018) to 52.66%. Investigation of GPT-2's errors showed most predictions are valid continuations of the sentence, but are not valid final words. This suggests the LM is not using the additional useful constraint that the word must be the final of the sentence. Adding a stop-word filter as an approximation further increases accuracy to 63.24%, improving the overall state of the art on this task by 4%. [p. 5-6]

The previous state of the art (Hoang et al., 2018) used a different restricted prediction setting where model outputs were constrained to only words that appeared in the context. For GPT-2, this restriction is harmful rather than helpful since 19% of answers are not in context. The authors use a version of the dataset without preprocessing. [p. 6]

## 3.4. Winograd Schema Challenge [p. 6]

[p. 6] The Winograd Schema challenge (Levesque et al., 2012) measures the capability of a system to perform commonsense reasoning by measuring its ability to resolve ambiguities in text. Trinh & Le (2018) demonstrated significant progress using LMs by predicting the resolution of the ambiguity with higher probability. The authors follow their problem formulation and visualize performance with both full and partial scoring techniques in Figure 3.

GPT-2 improves state of the art accuracy by 7%, achieving 70.70%. The dataset is quite small with only 273 examples; the authors recommend reading Trichelair et al. (2018) to help contextualize this result. [p. 6]

**Figure 3** (p. 6): "Performance on the Winograd Schema Challenge as a function of model capacity."

X-axis: # of parameters in LM (117M, 345M, 762M, 1542M). Y-axis: Accuracy (50-75%). Three lines plotted: SOTA (dashed horizontal ~63%), Partial Scoring (orange, increasing from ~58% to ~70%), Full Scoring (blue, increasing from ~56% to ~70%). Both scoring methods show clear improvement with scale, surpassing SOTA at 762M parameters.

## 3.5. Reading Comprehension [p. 6]

[p. 6] The Conversation Question Answering dataset (CoQA) (Reddy et al., 2018) consists of documents from 7 different domains paired with natural language dialogues between a question asker and a question answerer about the document. CoQA tests reading comprehension capabilities and the ability of models to answer questions that depend on conversation history (such as "Why?").

Greedy decoding from GPT-2 when conditioned on a document, the history of the associated conversation, and a final token `A:` achieves 55 F1 on the development set. This matches or exceeds the performance of 3 out of 4 baseline systems without using the 127,000+ manually collected question answer pairs those baselines were trained on. The supervised SOTA, a BERT based system (Devlin et al., 2018), is nearing the 89 F1 performance of humans. [p. 6]

While GPT-2's performance is exciting for a system without any supervised training, some inspection of its answers and errors suggests GPT-2 often uses simple retrieval based heuristics such as *answer with a name from the document in response to a who question*. [p. 6]

## 3.6. Summarization [p. 6]

[p. 6] Tests GPT-2's ability to perform summarization on the CNN and Daily Mail dataset (Nallapati et al., 2016). To induce summarization behavior, the text `TL;DR:` is added after the article and 100 tokens are generated with Top-k random sampling (Fan et al., 2018) with $k = 2$ (which reduces repetition and encourages more abstractive summaries than greedy decoding). The first 3 generated sentences in these 100 tokens are used as the summary. [p. 6]

While qualitatively the generations resemble summaries (as shown in Table 14), they often focus on recent content from the article or confuse specific details. On the commonly reported ROUGE 1,2,L metrics the generated summaries only begin to approach the performance of classic neural baselines and just barely outperform selecting 3 random sentences from the article. GPT-2's performance drops by 6.4 points on the aggregate metric when the task hint is removed, which demonstrates the ability to invoke task specific behavior in a language model with natural language. [p. 6]

**Table 4** (p. 6): "Summarization performance as measured by ROUGE F1 metrics on the CNN and Daily Mail dataset. Bottom-Up Sum is the SOTA model from (Gehrmann et al., 2018)"

|                  | R-1   | R-2   | R-L   | R-AVG |
|------------------|-------|-------|-------|-------|
| Bottom-Up Sum    | **41.22** | **18.68** | **38.34** | **32.75** |
| Lede-3           | 40.38 | 17.66 | 36.62 | 31.55 |
| Seq2Seq + Attn   | 31.33 | 11.81 | 28.83 | 23.99 |
| GPT-2 TL;DR:     | 29.34 | 8.27  | 26.58 | 21.40 |
| Random-3         | 28.78 | 8.63  | 25.52 | 20.98 |
| GPT-2 no hint    | 21.58 | 4.03  | 19.47 | 15.03 |

## 3.7. Translation [p. 6]

[p. 6] Tests whether GPT-2 has learned to translate from one language to another. To help infer the desired task, the language model is conditioned on a context of example pairs of the format `english sentence = french sentence` and then after a final prompt of `english sentence =` the model samples with greedy decoding, using the first generated sentence as the translation.

On the WMT-14 English-French test set, GPT-2 gets 5 BLEU, which is slightly worse than a word-by-word substitution with a bilingual lexicon inferred in previous work on unsupervised word translation (Conneau et al., 2017b). [p. 6]

---
[p. 7 continued]

On the WMT-14 French-English test set, GPT-2 is able to leverage its very strong English language model to perform significantly better, achieving 11.5 BLEU. This outperforms several unsupervised machine translation baselines from (Artetxe et al., 2017) and (Lample et al., 2017) but is still much worse than the 33.5 BLEU of the current best unsupervised machine translation approach (Artetxe et al., 2019). [p. 7]

Performance on this task was surprising since the authors deliberately removed non-English webpages from WebText as a filtering step. To confirm this, they ran a byte-level language detector (cld2) on WebText which detected only 10MB of data in the French language, approximately 500x smaller than the monolingual French corpus common in prior unsupervised machine translation research. [p. 7]

## 3.8. Question Answering [p. 7-8]

[p. 7] A potential way to test what information is contained within a language model is to evaluate how often it generates the correct answer to factoid-style questions. Previous showcasing of this behavior in neural systems where all information is stored in parameters such as *A Neural Conversational Model* (Vinyals & Le, 2015) reported qualitative results due to the lack of high-quality evaluation datasets. The recently introduced Natural Questions dataset (Kwiatkowski et al., 2019) is a promising resource to test this more quantitatively. [p. 7]

Similar to translation, the context of the language model is seeded with example question answer pairs which helps the model infer the short answer style of the dataset. GPT-2 answers 4.1% of questions correctly when evaluated by the exact match metric commonly used on reading comprehension datasets like SQuAD. As a comparison point, the smallest model does not exceed the 1.0% accuracy of an incredibly simple baseline which returns the most common answer for each question type (who, what, where, etc...). GPT-2 answers 5.3 times more questions correctly, suggesting that model capacity has been a major factor in the poor performance of neural systems on this kind of task as of yet. [p. 7-8]

The probability GPT-2 assigns to its generated answers is well calibrated and GPT-2 has an accuracy of 63.1% on the 1% of questions it is most confident in. The 30 most confident answers generated by GPT-2 on development set questions are shown in Table 5. [p. 7-8]

The performance of GPT-2 is still much, much, worse than the 30 to 50% range of open domain question answering systems which hybridize information retrieval with extractive document question answering (Alberti et al., 2019). [p. 8]

**Table 5** (p. 7): "The 30 most confident answers generated by GPT-2 on the development set of Natural Questions sorted by their probability according to GPT-2. None of these questions appear in WebText according to the procedure described in Section 4."

| Question | Generated Answer | Correct | Probability |
|----------|-----------------|---------|-------------|
| Who wrote the book the origin of species? | Charles Darwin | yes | 83.4% |
| Who is the founder of the ubuntu project? | Mark Shuttleworth | yes | 82.0% |
| Who is the quarterback for the green bay packers? | Aaron Rodgers | yes | 81.1% |
| Panda is a national animal of which country? | China | yes | 76.8% |
| Who came up with the theory of relativity? | Albert Einstein | yes | 76.4% |
| When was the first star wars film released? | 1977 | yes | 71.4% |
| What is the most common blood type in sweden? | A | no | 70.6% |
| Who is regarded as the founder of psychoanalysis? | Sigmund Freud | yes | 69.3% |
| Who took the first steps on the moon in 1969? | Neil Armstrong | yes | 66.8% |
| Who is the largest supermarket chain in the uk? | Tesco | yes | 65.3% |
| What is the meaning of shalom in english? | peace | yes | 64.0% |
| Who was the author of the art of war? | Sun Tzu | yes | 59.6% |
| Largest state in the us by land mass? | California | no | 59.2% |
| Green algae is an example of which type of reproduction? | parthenogenesis | no | 56.5% |
| Vikram samvat calender is official in which country? | India | yes | 55.6% |
| Who is mostly responsible for writing the declaration of independence? | Thomas Jefferson | yes | 53.3% |
| What us state forms the western boundary of montana? | Montana | no | 52.3% |
| Who plays ser davos in game of thrones? | Peter Dinklage | no | 52.1% |
| Who appoints the chair of the federal reserve system? | Janet Yellen | no | 51.5% |
| State the process that divides one nucleus into two genetically identical nuclei? | mitosis | yes | 50.7% |
| Who won the most mvp awards in the nba? | Michael Jordan | no | 50.2% |
| What river is associated with the city of rome? | the Tiber | yes | 48.6% |
| Who is the first president to be impeached? | Andrew Johnson | yes | 48.3% |
| Who is the head of the department of homeland security 2017? | John Kelly | yes | 47.0% |
| What is the name given to the common currency to the european union? | Euro | yes | 46.8% |
| What was the emperor name in star wars? | Palpatine | yes | 46.5% |
| Do you have to have a gun permit to shoot at a range? | No | yes | 46.4% |
| Who proposed evolution in 1859 as the basis of biological development? | Charles Darwin | yes | 45.7% |
| Nuclear power plant that blew up in russia? | Chernobyl | yes | 45.7% |
| Who played john connor in the original terminator? | Arnold Schwarzenegger | no | 45.2% |

**Figure 1** (p. 2): "Zero-shot task performance of WebText LMs as a function of model size on many NLP tasks. Reading Comprehension results are on CoQA (Reddy et al., 2018), translation on WMT-14 Fr-En (Artetxe et al., 2017), summarization on CNN and Daily Mail (See et al., 2017), and Question Answering on Natural Questions (Kwiatkowski et al., 2019). Section 3 contains detailed descriptions of each result."

Four panels:
1. **Reading Comprehension**: Y-axis F1, X-axis # of parameters. Shows models from Seq2seq (~30 F1) up to Human (~90 F1). GPT-2 (1542M) reaches ~55 F1, exceeding DrQA and PGNet baselines.
2. **Translation**: Y-axis BLEU, X-axis # of parameters. Shows performance improving from ~5 to ~11 BLEU with model size. Reference lines for Denoising, Denoising+Backtranslate, Embed Nearest Neighbor, and Unsupervised Statistical MT.
3. **Summarization**: Y-axis Average of ROUGE 1,2,L. Performance scales from ~18 to ~22 with model size. Reference lines: Lead-3, PGNet, Seq2seq+Attn, Random-3.
4. **Question Answering**: Y-axis Accuracy, X-axis # of parameters. Performance scales from ~2 to ~4.5 with model size. Reference line for "most freq Q-type answer" at ~1 and "Open Domain QA Systems" at ~8.
