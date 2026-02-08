# Evaluation [p. 5-6]

Gemma is evaluated across a broad range of domains, using both automated benchmarks and human evaluation. [p. 5]

## Human Preference Evaluations

In addition to running standard academic benchmarks on the finetuned models, final release candidates are sent to human evaluation studies to be compared against the Mistral v0.2 7B Instruct model (Jiang et al., 2023). [p. 5]

On a held-out collection of around 1000 prompts oriented toward asking models to follow instructions across creative writing tasks, coding, and following instructions, Gemma 7B IT has a 61.2% positive win rate and Gemma 2B IT has a 45% win rate over Mistral v0.2 7B Instruct. On a held-out collection of around 400 prompts oriented towards testing basic safety protocols, Gemma 7B IT has a 63.5% win rate, while Gemma 2B IT has a 60.1% win rate. The corresponding numbers are reported in Table 5. [p. 5]

**Table 5** (p. 5): Win rate of Gemma 1.1 IT models versus Mistral 7B v0.2 Instruct with 95% confidence intervals. Breakdowns of wins, ties, and losses are reported, and ties are broken evenly when reporting the final win rate. Gemma 1.0 results can be found in the appendix.

| Model                | Safety          | Instr. Following |
|----------------------|-----------------|------------------|
| **Gemma 1.1 IT 7B** | **63.5%**       | **61.2%**        |
| *95% Conf. Interval* | [60.7%, 66.1%] | [59.3%, 63%]     |
| *Win / Tie / Loss*   | 51.5% / 23.9% / 24.6% | 52.2% / 18.1% / 29.8% |
| **Gemma 1.1 IT 2B** | **60.1%**       | **45%**          |
| *95% Conf. Interval* | [57.3%, 62.8%] | [43.1%, 46.9%]   |
| *Win / Tie / Loss*   | 48.5% / 23.2% / 28.3% | 37.1% / 15.8% / 47.1% |

## Automated Benchmarks

Gemma models' performance is measured on domains including physical reasoning (Bisk et al., 2019), social reasoning (Sap et al., 2019), question answering (Clark et al., 2019; Kwiatkowski et al., 2019), coding (Austin et al., 2021; Chen et al., 2021), mathematics (Cobbe et al., 2021), commonsense reasoning (Sakaguchi et al., 2019), language modeling (Paperno et al., 2016), reading comprehension (Joshi et al., 2017), and more. [p. 5]

For most automated benchmarks the same evaluation methodology as in Gemini is used. Specifically for those where performance is compared with Mistral, the methodology from the Mistral technical report is replicated as closely as possible. These specific benchmarks are: ARC (Clark et al., 2018), CommonsenseQA (Talmor et al., 2019), Big Bench Hard (Suzgun et al., 2022), and AGI Eval (English-only) (Zhong et al., 2023). Due to restrictive licensing, no evaluations on LLaMA-2 could be run and only those metrics previously reported (Touvron et al., 2023b) are cited. [p. 5]

Gemma 2B and 7B models are compared to several external open-source (OSS) LLMs across a series of academic benchmarks, reported in Table 6 and Table 7. [p. 5]

On MMLU (Hendrycks et al., 2020), Gemma 7B outperforms all OSS alternatives at the same or smaller scale; it also outperforms several larger models, including LLaMA2 13B. However, human expert performance is gauged at 89.8% by the benchmark authors; as Gemini Ultra is the first model to exceed this threshold, there is significant room for continued improvements to achieve Gemini and human-level performance. [p. 5]

Gemma models demonstrate particularly strong performance on mathematics and coding benchmarks. On mathematics tasks, which are often used to benchmark the general analytical capabilities of models, Gemma models outperform other models by at least 10 points on GSM8K (Cobbe et al., 2021) and the more difficult MATH (Hendrycks et al., 2021) benchmark. Similarly, they outperform alternate open models by at least 6 points on HumanEval (Chen et al., 2021). They even surpass the performance of the code-fine-tuned CodeLLaMA-7B models on MBPP (CodeLLaMA achieves a score of 41.4% where Gemma 7B achieves 44.4%). [p. 6]

**Table 6** (p. 6): Academic benchmark results, compared to similarly sized, openly-available models trained on general English text data. Footnote: Mistral reports 50.2 on a different split for MBPP and on their split the Gemma 7B model achieves 54.5. Asterisks (*) denote evaluations run by the authors. Note that due to restrictive licensing, no evaluations on LLaMA-2 could be run; all values above were previously reported in Touvron et al. (2023b).

|             |                 | LLaMA-2 |       | Mistral | Gemma |       |
|-------------|-----------------|---------|-------|---------|-------|-------|
| Benchmark   | metric          | 7B      | 13B   | 7B      | 2B    | 7B    |
| MMLU        | 5-shot, top-1   | 45.3    | 54.8  | 62.5    | 42.3  | **64.3** |
| HellaSwag   | 0-shot          | 77.2    | 80.7  | 81.0    | 71.4  | **81.2** |
| PIQA        | 0-shot          | 78.8    | 80.5  | **82.2**| 77.3  | 81.2  |
| SIQA        | 0-shot          | 48.3    | 50.3  | 47.0*   | 49.7  | **51.8** |
| BoolQ       | 0-shot          | 77.4    | 81.7  | 83.2*   | 69.4  | **83.2** |
| Winogrande  | partial scoring | 69.2    | 72.8  | **74.2**| 65.4  | 72.3  |
| CQA         | 7-shot          | 57.8    | 67.3  | 66.3*   | 65.3  | **71.3** |
| OBQA        |                 | **58.6**| 57.0  | 52.2    | 47.8  | 52.8  |
| ARC-e       |                 | 75.2    | 77.3  | 80.5    | 73.2  | **81.5** |
| ARC-c       |                 | 45.9    | 49.4  | **54.9**| 42.1  | 53.2  |
| TriviaQA    | 5-shot          | 72.1    | **79.6**| 62.5  | 53.2  | 63.4  |
| NQ          | 5-shot          | 25.7    | **31.2**| 23.2  | 12.5  | 23.0  |
| HumanEval   | pass@1          | 12.8    | 18.3  | 26.2    | 22.0  | **32.3** |
| MBPP&dagger; | 3-shot         | 20.8    | 30.6  | 40.2*   | 29.2  | **44.4** |
| GSM8K       | maj@1           | 14.6    | 28.7  | 35.4*   | 17.7  | **46.4** |
| MATH        | 4-shot          | 2.5     | 3.9   | 12.7    | 11.8  | **24.3** |
| AGIEval     |                 | 29.3    | 39.1  | 41.2*   | 24.2  | **41.7** |
| BBH         |                 | 32.6    | 39.4  | **56.1***| 35.2 | 55.1  |
| **Average** |                 | 46.9    | 52.4  | 54.5    | 45.0  | **56.9** |

## Memorization Evaluations

Recent work has shown that aligned models may be vulnerable to new adversarial attacks that can bypass alignment (Nasr et al., 2023). These attacks can cause models to diverge, and sometimes regurgitate memorized training data in the process. The focus is on discoverable memorization, which serves as a reasonable upper-bound on the memorization of a model (Nasr et al., 2023) and has been the common definition used in several studies (Anil et al., 2023; Carlini et al., 2022; Kudugunta et al., 2023). [p. 6]

Memorization is tested on the Gemma pretrained models with the same methodology performed in Anil et al. (2023). 10,000 documents from each corpus are sampled and the first 50 tokens are used as a prompt for the model. The focus is mainly on exact memorization, where texts are classified as memorized if the subsequent 50 tokens generated by the model exactly match the ground truth continuation in the text. To better capture potential paraphrased memorizations, approximate memorization is also included (Ippolito et al., 2022) using a 10% edit distance threshold. [p. 6]

Note: The authors' use of "memorization" relies on the definition of that term found at www.genlaw.org/glossary.html. [p. 6, footnote 1]

---
[p. 7 continued]

**Table 7** (p. 7): HuggingFace H6 benchmark. The performance of small models is sensitive to small modifications in prompts and the authors further validate the quality of their models on an independent implementation of multiple known benchmarks. All evaluations were run by HuggingFace.

| Benchmark  | Mistral 7B | Gemma 7B |
|------------|-----------|----------|
| ARC-c      | 60.0      | **61.9** |
| HellaSwag  | **83.3**  | 82.2     |
| MMLU       | 64.2      | **64.6** |
| TruthfulQA | 42.2      | **44.8** |
| Winogrande | 78.4      | **79.0** |
| GSM8K      | 37.8      | **50.9** |
| Average    | 61.0      | **63.8** |

**Figure 2** (p. 7): "Comparing average memorization rates across model families. We compare the Gemma pretrained models to PaLM and PaLM 2 models of comparable size and find similarly low rates of memorization."

Two panels are shown, both with log-scale y-axis (% Exact Memorized):
- Left panel ("Memorization of English Web Content"): Compares Gemma 2B, Gemma 7B, and PaLM 2 Small. All models show memorization rates below ~1%.
- Right panel ("Memorization of All Content"): Same three models. Gemma memorizes training data at a comparable rate to PaLM when measuring total memorization across all content.

In Figure 2, the results of the evaluation are compared with the closest sized PaLM (Chowdhery et al., 2022) and PaLM 2 models (Anil et al., 2023). [p. 7]

### Verbatim Memorization

PaLM 2 compared with PaLM by evaluating on a shared subset of their training corpora. However, there is even less overlap between the Gemma pretraining data with the PaLM models, and so using this same methodology, much lower memorization rates are observed (Figure 2 left). Instead, estimating the "total memorization" across the entire pretraining dataset gives a more reliable estimate (Figure 2 right) where Gemma memorizes training data at a comparable rate to PaLM. [p. 7]

### Personal Data

Perhaps of higher importance is the possibility that personal data might be memorized. As part of making Gemma pre-trained models safe and reliable, automated techniques were used to filter out certain personal information and other sensitive data from training sets. [p. 7]

To identify possible occurrences of personal data, Google Cloud Sensitive Data Protection is used (available at https://cloud.google.com/sensitive-data-protection). This tool outputs three severity levels based on many categories of personal data (e.g., names, emails, etc.). The highest severity is classified as "sensitive" and the remaining two as simply "personal". Then, how many memorized outputs contain any sensitive or personal data is measured. [p. 7]

**Figure 3** (p. 7): "Measuring personal and sensitive data memorization rates. No sensitive data was memorized, hence it is omitted from the figure."

Two panels are shown:
- Left panel ("2B Model"): Bar chart with x-axis showing data sources (Code, Wiki, Science, Web, Multilingual) and y-axis showing % Exact Memorized (log scale). Each bar is split into "Personal Data: Yes" (green) and "Personal Data: No" (gray). No sensitive data bars are present.
- Right panel ("7B Model"): Same layout. The model memorizes some data classified as potentially "personal" but at a much lower rate. No sensitive data is memorized.

The authors note that the personal data detection tools are known to have many false positives (they only match patterns and do not consider context), meaning results likely overestimate the amount of personal data identified. [p. 7]

---
[p. 8 continued]

### Approximate Memorization

**Figure 4** (p. 8): "Comparing exact and approximate memorization."

Two panels are shown:
- Left panel ("2B Model"): Bar chart comparing exact memorization (dark teal) vs. approximate memorization (light green) across data sources (Code, Wiki, Science, Web, Multilingual). Y-axis is % Memorized on log scale (0.1 to 10).
- Right panel ("7B Model"): Same layout. Approximate memorization is roughly 50% more data than exact memorization, and this is nearly consistent across each of the different subcategories over the dataset.

Roughly 50% more data is approximately memorized (note the log scale) and this is nearly consistent across each of the different subcategories over the dataset. [p. 8]

## Safety Evaluations

**Table 8** (p. 8): Safety academic benchmark results of Gemma 1.1 IT models, compared to similarly sized, openly-available models. Evaluations run by the authors. Note that due to restrictive licensing, no evaluations on LLaMA-2 could be run; previously-published numbers for LLaMA-2 on TruthfulQA are not reported, as different non-comparable evaluation set-ups are used: MC2 for Gemma vs. GPT-Judge for LLaMA-2. Results for Gemma 1.0 IT models can be found in the appendix.

| Benchmark     | metric      | Mistral v0.2 7B* | Gemma 1.1 IT 2B | Gemma 1.1 IT 7B |
|---------------|-------------|-------------------|------------------|------------------|
| RealToxicity  | avg         | 8.44              | **7.03**         | 8.04             |
| BOLD          |             | 46.0              | **47.76**        | 45.2             |
| CrowS-Pairs   | top-1       | 32.76             | 45.89            | **49.67**        |
| BBQ Ambig     | 1-shot, top-1 | **97.53**       | 58.97            | 86.06            |
| BBQ Disambig  | top-1       | 84.45             | 53.9             | **85.08**        |
| Winogender    | top-1       | **64.3**          | 50.14            | 57.64            |
| TruthfulQA    |             | **48.54**         | 44.24            | 45.34            |
| Winobias 1_2  |             | **65.72**         | 55.93            | 59.22            |
| Winobias 2_2  |             | 84.53             | **89.46**        | 89.2             |
| Toxigen       |             | 61.77             | **29.64**        | 38.75            |
