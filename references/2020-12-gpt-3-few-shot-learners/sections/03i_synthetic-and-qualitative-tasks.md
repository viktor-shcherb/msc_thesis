# 3.9 Synthetic and Qualitative Tasks [p. 21]

[p. 21] One way to probe GPT-3's range of abilities in the few-shot (or zero- and one-shot) setting is to give it tasks which require it to perform simple on-the-fly computational reasoning, recognize a novel pattern that is unlikely to have occurred in training, or adapt quickly to an unusual task. Several tasks are devised to test this class of abilities:

1. First, GPT-3's ability to perform arithmetic is tested.
2. Second, several tasks that involve rearranging or unscrambling the letters in a word are created, tasks which are unlikely to have been exactly seen during training.
3. Third, GPT-3's ability to solve SAT-style analogy problems few-shot is tested.
4. Finally, GPT-3 is tested on several qualitative tasks, including using new words in a sentence, correcting English grammar, and news article generation.

The synthetic datasets will be released with the hope of stimulating further study of test-time behavior of language models.

## 3.9.1 Arithmetic [p. 21]

[p. 21] To test GPT-3's ability to perform simple arithmetic operations without task-specific training, a small battery of 10 tests is developed that involve asking GPT-3 a simple arithmetic problem in natural language:

- **2 digit addition (2D+)** -- The model is asked to add two integers sampled uniformly from [0, 100), phrased in the form of a question, e.g. "Q: What is 48 plus 76? A: 124."
- **2 digit subtraction (2D-)** -- The model is asked to subtract two integers sampled uniformly from [0, 100); the answer may be negative. Example: "Q: What is 34 minus 53? A: -19".
- **3 digit addition (3D+)** -- Same as 2 digit addition, except numbers are uniformly sampled from [0, 1000).
- **3 digit subtraction (3D-)** -- Same as 2 digit subtraction, except numbers are uniformly sampled from [0, 1000).
- **4 digit addition (4D+)** -- Same as 3 digit addition, except uniformly sampled from [0, 10000).
- **4 digit subtraction (4D-)** -- Same as 3 digit subtraction, except uniformly sampled from [0, 10000).
- **5 digit addition (5D+)** -- Same as 3 digit addition, except uniformly sampled from [0, 100000).
- **5 digit subtraction (5D-)** -- Same as 3 digit subtraction, except uniformly sampled from [0, 100000).
- **2 digit multiplication (2Dx)** -- The model is asked to multiply two integers sampled uniformly from [0, 100), e.g. "Q: What is 24 times 42? A: 1008".
- **One-digit composite (1DC)** -- The model is asked to perform a composite operation on three 1 digit numbers, with parentheses around the last two. For example, "Q: What is 6+(4*8)? A: 38". The three 1 digit numbers are selected uniformly on [0, 10) and the operations are selected uniformly from {+, -, *}.

[p. 22] In all 10 tasks the model must generate the correct answer exactly. For each task a dataset of 2,000 random instances is generated and all models are evaluated on those instances.

### Few-shot arithmetic results

[p. 22] GPT-3 is first evaluated in the few-shot setting, for which results are shown in Figure 3.10. On addition and subtraction, GPT-3 displays strong proficiency when the number of digits is small, achieving 100% accuracy on 2 digit addition, 98.9% at 2 digit subtraction, 80.2% at 3 digit addition, and 94.2% at 3-digit subtraction. Performance decreases as the number of digits increases, but GPT-3 still achieves 25-26% accuracy on four digit operations and 9-10% accuracy on five digit operations, suggesting at least some capacity to generalize to larger numbers of digits. GPT-3 also achieves 29.2% accuracy at 2 digit multiplication, an especially computationally intensive operation. Finally, GPT-3 achieves 21.3% accuracy at single digit combined operations (for example, 9*(7+5)), suggesting that it has some robustness beyond just single operations.

[p. 22] As Figure 3.10 makes clear, small models do poorly on all of these tasks -- even the 13 billion parameter model (the second largest after the 175 billion full GPT-3) can solve 2 digit addition and subtraction only half the time, and all other operations less than 10% of the time.

### Zero-shot and one-shot arithmetic results

[p. 22-23] One-shot and zero-shot performance are somewhat degraded relative to few-shot performance, suggesting that adaptation to the task (or at the very least recognition of the task) is important to performing these computations correctly. Nevertheless, one-shot performance is still quite strong, and even zero-shot performance of the full GPT-3 significantly outperforms few-shot learning for all smaller models. All three settings for the full GPT-3 are shown in Table 3.9, and model capacity scaling for all three settings is shown in Appendix H.

### Table 3.9: Results on basic arithmetic tasks for GPT-3 175B. {2,3,4,5}D{+,-} is 2, 3, 4, and 5 digit addition or subtraction, 2Dx is 2 digit multiplication. 1DC is 1 digit composite operations. Results become progressively stronger moving from the zero-shot to one-shot to few-shot setting, but even the zero-shot shows significant arithmetic abilities. [p. 23]

| Setting | 2D+ | 2D- | 3D+ | 3D- | 4D+ | 4D- | 5D+ | 5D- | 2Dx | 1DC |
|---|---|---|---|---|---|---|---|---|---|---|
| GPT-3 Zero-shot | 76.9 | 58.0 | 34.2 | 48.3 | 4.0 | 7.5 | 0.7 | 0.8 | 19.8 | 9.8 |
| GPT-3 One-shot | 99.6 | 86.4 | 65.5 | 78.7 | 14.0 | 14.0 | 3.5 | 3.8 | 27.4 | 14.3 |
| GPT-3 Few-shot | 100.0 | 98.9 | 80.4 | 94.2 | 25.5 | 26.8 | 9.3 | 9.9 | 29.2 | 21.3 |

### Memorization spot-check

[p. 23] To spot-check whether the model is simply memorizing specific arithmetic problems, the authors took the 3-digit arithmetic problems in the test set and searched for them in the training data in both the forms "<NUM1> + <NUM2> =" and "<NUM1> plus <NUM2>". Out of 2,000 addition problems they found only 17 matches (0.8%) and out of 2,000 subtraction problems they found only 2 matches (0.1%), suggesting that only a trivial fraction of the correct answers could have been memorized. In addition, inspection of incorrect answers reveals that the model often makes mistakes such as not carrying a "1", suggesting it is actually attempting to perform the relevant computation rather than memorizing a table.

### Overall arithmetic assessment

[p. 23] Overall, GPT-3 displays reasonable proficiency at moderately complex arithmetic in few-shot, one-shot, and even zero-shot settings.

### Figures

**Figure 3.10** (p. 22): "Results on all 10 arithmetic tasks in the few-shot settings for models of different sizes."
- Caption: "There is a significant jump from the second largest model (GPT-3 13B) to the largest model (GPT-3 175), with the latter being able to reliably accurate 2 digit arithmetic, usually accurate 3 digit arithmetic, and correct answers a significant fraction of the time on 4-5 digit arithmetic, 2 digit multiplication, and compound operations. Results for one-shot and zero-shot are shown in the appendix."
- X-axis: Parameters in LM (Billions), from 0.1B to 175B. Y-axis: Accuracy, from 0 to 100.
- 10 lines for different tasks: Two Digit Addition (blue, reaches ~100 at 175B), Two Digit Subtraction (orange, reaches ~98.9), Three Digit Addition (green, reaches ~80), Three Digit Subtraction (red, reaches ~94), Four Digit Addition (purple, reaches ~25), Four Digit Subtraction (brown, reaches ~27), Five Digit Addition (pink, reaches ~9), Five Digit Subtraction (gray, reaches ~10), Two Digit Multiplication (yellow, reaches ~29), Single Digit Three Ops (cyan, reaches ~21).
- All tasks show near-zero performance for models from 0.1B through 6.7B, with a notable jump at 13B for simple tasks and a dramatic jump at 175B across all tasks.
- The largest jump in performance occurs between 13B and 175B for all tasks.

---

## 3.9.2 Word Scrambling and Manipulation Tasks [p. 23]

[p. 23] To test GPT-3's ability to learn novel symbolic manipulations from a few examples, a small battery of 5 "character manipulation" tasks is designed. Each task involves giving the model a word distorted by some combination of scrambling, addition, or deletion of characters, and asking it to recover the original word. The 5 tasks are:

- **Cycle letters in word (CL)** -- The model is given a word with its letters cycled, then the "=" symbol, and is expected to generate the original word. For example, it might be given "lyinevitab" and should output "inevitably".
- **Anagrams of all but first and last characters (A1)** -- The model is given a word where every letter except the first and last have been scrambled randomly, and must output the original word. Example: criroptuon = corruption.
- **Anagrams of all but first and last 2 characters (A2)** -- The model is given a word where every letter except the first 2 and last 2 have been scrambled randomly, and must recover the original word. Example: opoepnnt -> opponent.
- **Random insertion in word (RI)** -- A random punctuation or space character is inserted between each letter of a word, and the model must output the original word. Example: s.u" c/c!e.s" s i/o/n = succession.
- **Reversed words (RW)** -- The model is given a word spelled backwards, and must output the original word. Example: stcejbo -> objects.

[p. 23] For each task 10,000 examples are generated, chosen to be the top 10,000 most frequent words as measured by [Nor09] of length more than 4 characters and less than 15 characters. The few-shot results are shown in Figure 3.11.

[p. 24] Task performance tends to grow smoothly with model size, with the full GPT-3 model achieving 66.9% on removing random insertions, 38.6% on cycling letters, 40.2% on the easier anagram task, and 15.1% on the more difficult anagram task. None of the models can reverse the letters in a word.

[p. 24] In the one-shot setting, performance is significantly weaker (dropping by half or more), and in the zero-shot setting the model can rarely perform any of the tasks (Table 3.10). This suggests that the model really does appear to learn these tasks at test time, as the model cannot perform them zero-shot and their artificial nature makes them unlikely to appear in the pre-training data (although this cannot be confirmed with certainty).

[p. 24] "In-context learning curves" can further quantify performance by plotting task performance as a function of the number of in-context examples. In-context learning curves for the Symbol Insertion task are shown in Figure 1.2. Larger models are able to make increasingly effective use of in-context information, including both task examples and natural language task descriptions.

[p. 24] Finally, it is worth adding that solving these tasks requires character-level manipulations, whereas the BPE encoding operates on significant fractions of a word (on average ~0.7 words per token), so from the LM's perspective succeeding at these tasks involves not just manipulating BPE tokens but understanding and pulling apart their substructure. Also, CL, A1, and A2 are not bijective (that is, the unscrambled word is not a deterministic function of the scrambled word), requiring the model to perform some search to find the correct unscrambling. Thus, the skills involved appear to require non-trivial pattern-matching and computation.

### Table 3.10: GPT-3 175B performance on various word unscrambling and word manipulation tasks, in zero-, one-, and few-shot settings. CL is "cycle letters in word", A1 is anagrams of but the first and last letters, A2 is anagrams of all but the first and last two letters, RI is "Random insertion in word", RW is "reversed words". [p. 23]

| Setting | CL | A1 | A2 | RI | RW |
|---|---|---|---|---|---|
| GPT-3 Zero-shot | 3.66 | 2.28 | 8.91 | 8.26 | 0.09 |
| GPT-3 One-shot | 21.7 | 8.62 | 25.9 | 45.4 | 0.48 |
| GPT-3 Few-shot | 37.9 | 15.1 | 39.7 | 67.2 | 0.44 |

### Figures

**Figure 3.11** (p. 24): "Few-shot performance on the five word scrambling tasks for different sizes of model."
- Caption: "There is generally smooth improvement with model size although the random insertion task shows an upward slope of improvement with the 175B model solving the task the majority of the time. Scaling of one-shot and zero-shot performance is shown in the appendix. All tasks are done with K = 100."
- X-axis: Parameters in LM (Billions), from 0.1B to 175B. Y-axis: Accuracy, from 0 to 70.
- 5 lines: cycle letters (blue, reaches ~38.6 at 175B), mid word 1 anagrams (orange, reaches ~15 at 175B), mid word 2 anagrams (green, reaches ~40 at 175B), random insertion (red, reaches ~67 at 175B), reversed words (purple, stays near 0 across all sizes).
- Random insertion shows the steepest upward slope at the largest model sizes. Cycle letters and mid word 2 anagrams show generally smooth improvement. Mid word 1 anagrams shows modest improvement. Reversed words remains near zero for all model sizes.

---

## 3.9.3 SAT Analogies [p. 24]

[p. 24] To test GPT-3 on another task that is somewhat unusual relative to the typical distribution of text, a set of 374 "SAT analogy" problems [TLBS03] is collected. Analogies are a style of multiple choice question that constituted a section of the SAT college entrance exam before 2005. A typical example is "audacious is to boldness as (a) sanctimonious is to hypocrisy, (b) anonymous is to identity, (c) remorseful is to misdeed, (d) deleterious is to result, (e) impressionable is to temptation". The student is expected to choose which of the five word pairs has the same relationship as the original word pair; in this example the answer is "sanctimonious is to hypocrisy".

[p. 24] On this task GPT-3 achieves 65.2% in the few-shot setting, 59.1% in the one-shot setting, and 53.7% in the zero-shot setting, whereas the average score among college applicants was 57% [TL05] (random guessing yields 20%). As shown in Figure 3.12, the results improve with scale, with the full 175 billion model improving by over 10% compared to the 13 billion parameter model.

### Figures

**Figure 3.12** (p. 25): "Zero-, one-, and few-shot performance on SAT analogy tasks, for different sizes of model."
- Caption: "The largest model achieves 65% accuracy in the few-shot setting, and also demonstrates significant gains to in-context learning which are not present in smaller models."
- X-axis: Parameters in LM (Billions), from 0.1B to 175B. Y-axis: Accuracy, from 20 to ~70.
- Three lines: Zero-Shot (blue), One-Shot (green), Few-Shot K=20 (orange).
- Horizontal dashed line: "Random Guessing" at 20.
- At small model sizes (0.1B-0.4B), all three settings cluster around 28-35%. Zero-Shot rises to ~40 at 2.6B, then ~49 at 13B, then ~54 at 175B. One-Shot is similar at small sizes, rises to ~55 at 13B, then ~59 at 175B. Few-Shot is also similar at small sizes but diverges more at larger scales, reaching ~40 at 2.6B, ~55 at 13B, then ~65 at 175B.
- The gap between few-shot and zero-shot widens substantially at larger model sizes, demonstrating significant gains to in-context learning.

---

## 3.9.4 News Article Generation [p. 25]

[p. 25] Previous work on generative language models qualitatively tested their ability to generate synthetic "news articles" by conditional sampling from the model given a human-written prompt consisting of a plausible first sentence for a news story [RWC+19]. Relative to [RWC+19], the dataset used to train GPT-3 is much less weighted towards news articles, so trying to generate news articles via raw unconditional samples is less effective -- for example GPT-3 often interprets the proposed first sentence of a "news article" as a tweet and then posts synthetic responses or follow-up tweets. To solve this problem the authors employed GPT-3's few-shot learning abilities by providing three previous news articles in the model's context to condition it. With the title and subtitle of a proposed next article, the model is able to reliably generate short articles in the "news" genre.

### Human evaluation methodology

[p. 25] To gauge the quality of news article generation from GPT-3 (which the authors believe is likely to be correlated with conditional sample generation quality in general), they decided to measure human ability to distinguish GPT-3-generated articles from real ones. Similar work has been carried out by Kreps et al. [KMB20] and Zellers et al. [ZHR+19]. Generative language models are trained to match the distribution of content generated by humans, so the (in)ability of humans to distinguish the two is a potentially important measure of quality.^3

[p. 25] In order to see how well humans can detect model generated text, 25 article titles and subtitles were arbitrarily selected from the website newser.com (mean length: 215 words). Completions of these titles and subtitles were then generated from four language models ranging in size from 125M to 175B (GPT-3) parameters (mean length: ~200 words). For each model, around 80 US-based participants were presented with a quiz consisting of these real titles and subtitles followed by either the human written article or the article generated by the model.^4 Participants were asked to select whether the article was "very likely written by a human", "more likely written by a human", "I don't know", "more likely written by a machine", or "very likely written by a machine".

[p. 25] The articles selected were not in the models' training data and the model outputs were formatted and selected programmatically to prevent human cherry-picking. All models used the same context to condition outputs on and were pre-trained with the same context size and the same article titles and subtitles were used as prompts for each model. However, a control experiment was also run for participant effort and attention that followed the same format but involved intentionally bad model generated articles. This was done by generating articles from a "control model": a 160M parameter model with no context and increased output randomness.

### Table 3.11: Human accuracy in identifying whether short (~200 word) news articles are model generated. Human accuracy (measured by the ratio of correct assignments to non-neutral assignments) ranges from 86% on the control model to 52% on GPT-3 175B. This table compares mean accuracy between five different models, and shows the results of a two-sample T-Test for the difference in mean accuracy between each model and the control model (an unconditional GPT-3 Small model with increased output randomness). [p. 26]

| Model | Mean accuracy | 95% Confidence Interval (low, hi) | t compared to control (p-value) | "I don't know" assignments |
|---|---|---|---|---|
| Control (deliberately bad model) | 86% | 83%-90% | - | 3.6% |
| GPT-3 Small | 76% | 72%-80% | 3.9 (2e-4) | 4.9% |
| GPT-3 Medium | 61% | 58%-65% | 10.3 (7e-21) | 6.0% |
| GPT-3 Large | 68% | 64%-72% | 7.3 (3e-11) | 8.7% |
| GPT-3 XL | 62% | 59%-65% | 10.7 (1e-19) | 7.5% |
| GPT-3 2.7B | 62% | 58%-65% | 10.4 (5e-19) | 7.1% |
| GPT-3 6.7B | 60% | 56%-63% | 11.2 (3e-21) | 6.2% |
| GPT-3 13B | 55% | 52%-58% | 15.3 (1e-32) | 7.1% |
| GPT-3 175B | 52% | 49%-54% | 16.9 (1e-34) | 7.8% |

### Human detection results

[p. 26] Mean human accuracy (the ratio of correct assignments to non-neutral assignments per participant) at detecting that the intentionally bad articles were model generated was ~86% where 50% is chance level performance. By contrast, mean human accuracy at detecting articles that were produced by the 175B parameter model was barely above chance at ~52% (see Table 3.11).^5 Human abilities to detect model generated text appear to decrease as model size increases: there appears to be a trend towards chance accuracy with model size, and human detection of GPT-3 is close to chance.^6 This is true despite the fact that participants spend more time on each output as model size increases (see Appendix E).

[p. 26] Examples of synthetic articles from GPT-3 are given in Figures 3.14 and 3.15.^7 Much of the text is -- as indicated by the evaluations -- difficult for humans to distinguish from authentic human content. Factual inaccuracies can be an indicator that an article is model generated since, unlike human authors, the models have no access to the specific facts that the article titles refer to or when the article was written. Other indicators include repetition, non sequiturs, and unusual phrasings, though these are often subtle enough that they are not noticed.

[p. 26] Related work on language model detection by Ippolito et al. [IDCBE19] indicates that automatic discriminators like GROVER [ZHR+19] and GLTR [GSR19] may have greater success at detecting model generated text than human evaluators. Automatic detection of these models may be a promising area of future research.

[p. 26] Ippolito et al. [IDCBE19] also note that human accuracy at detecting model generated text increases as humans observe more tokens. To do a preliminary investigation of how good humans are at detecting longer news articles generated by GPT-3 175B, 12 world news articles from Reuters with an average length of 569 words were selected and completions of these articles from GPT-3 with an average length of 498 words (298 words longer than the initial experiments) were generated. Following the methodology above, two experiments were run, each on around 80 US-based participants, to compare human abilities to detect the articles generated by GPT-3 and a control model.

[p. 26] Mean human accuracy at detecting the intentionally bad longer articles from the control model was ~88%, while mean human accuracy at detecting the longer articles that were produced by GPT-3 175B was still barely above chance at ~52% (see Table 3.12). This indicates that, for news articles that are around 500 words long, GPT-3 continues to produce articles that humans find difficult to distinguish from human written news articles.

### Footnotes

^3 This task is also relevant to the potential misuse of language models discussed in Section 6.1.

^4 The authors wanted to identify how good an average person on the internet is at detecting language model outputs, so they focused on participants drawn from the general US population. See Appendix E for details.

^5 A two-sample Student's T-Test is used to test for significant difference between the means of the participant accuracies of each model and the control model and report the normalized difference in the means (as the t-statistic) and the p-value.

^6 If a model consistently produces texts that are more impressive than human articles, it is possible that human performance on this task would drop below 50%. Indeed, many individual participants scored below 50% on this task.

^7 Additional non-news samples can be found in Appendix F.

---

### Table 3.12: People's ability to identify whether ~500 word articles are model generated (as measured by the ratio of correct assignments to non-neutral assignments) was 88% on the control model and 52% on GPT-3 175B. This table shows the results of a two-sample T-Test for the difference in mean accuracy between GPT-3 175B and the control model (an unconditional GPT-3 Small model with increased output randomness). [p. 27]

| Model | Mean accuracy | 95% Confidence Interval (low, hi) | t compared to control (p-value) | "I don't know" assignments |
|---|---|---|---|---|
| Control | 88% | 84%-91% | - | 2.7% |
| GPT-3 175B | 52% | 48%-57% | 12.7 (3.2e-23) | 10.6% |

### Figures (continued)

**Figure 3.13** (p. 27): "People's ability to identify whether news articles are model-generated (measured by the ratio of correct assignments to non-neutral assignments) decreases as model size increases. Accuracy on the outputs on the deliberately-bad control model (an unconditioned GPT-3 Small model with higher output randomness) is indicated with the dashed line at the top, and the random chance (50%) is indicated with the dashed line at the bottom. Line of best fit is a power law with 95% confidence intervals."
- X-axis: Number of parameters (log scale), from 1e8 to 1e11. Y-axis: Accuracy (%), from ~50 to ~86.
- Dashed horizontal lines: control at ~86% (top), random chance at 50% (bottom).
- Data points (with 95% confidence interval error bars): GPT-3 Small (~125M) at ~76%, GPT-3 Medium (~350M) at ~61%, GPT-3 Large (~760M) at ~68%, GPT-3 XL (~1.3B) at ~62%, GPT-3 2.7B at ~62%, GPT-3 6.7B at ~60%, GPT-3 13B at ~55%, GPT-3 175B at ~52%.
- A power law best-fit line (solid black) descends from upper-left to lower-right, with a gray shaded 95% confidence band. The trend shows a smooth decrease in human detection accuracy as model size increases.
- Supports the claim that human detection of GPT-3-generated text approaches random chance with the largest models.

**Figure 3.14** (p. 28): "The GPT-3 generated news article that humans had the greatest difficulty distinguishing from a human written article (accuracy: 12%)."
- Shows a GPT-3 generated article with:
  - Title: "United Methodists Agree to Historic Split"
  - Subtitle: "Those who oppose gay marriage will form their own denomination"
  - Article body discusses the United Methodist Church agreeing to a historic split, the creation of a new denomination called the Christian Methodist denomination, mentions 12.5 million members, the history of the denomination, and the schism over the role of LGBTQ people in the church.
- The article is presented in monospace font and reads as a plausible news article, demonstrating GPT-3's ability to generate coherent, topical news content that humans found very difficult to identify as machine-generated.

**Figure 3.15** (p. 28): "The GPT-3 generated news article that humans found the easiest to distinguish from a human written article (accuracy: 61%)."
- Shows a GPT-3 generated article with:
  - Title: "Star's Tux Promise Draws Megyn Kelly's Sarcasm"
  - Subtitle: "Joaquin Phoenix pledged to not change for each awards event"
  - Article body discusses Joaquin Phoenix wearing a tuxedo at the Golden Globes with a paper bag over his head, his pledge not to change, and a dialogue with Megyn Kelly on The Tonight Show questioning his commitment.
- The article contains somewhat unusual phrasing and dialogue that made it easier for humans to identify as machine-generated compared to Figure 3.14.

---

## 3.9.5 Learning and Using Novel Words [p. 26]

[p. 26] A task studied in developmental linguistics [CB78] is the ability to learn and utilize new words, for example using a word in a sentence after seeing it defined only once, or conversely inferring a word's meaning from only one usage. Here GPT-3's ability to do the former is qualitatively tested. Specifically, GPT-3 is given the definition of a nonexistent word, such as "Gigamuru", and then asked to use it in a sentence. One to five previous examples of a (separate) nonexistent word being defined and used in a sentence are provided, so the task is few-shot in terms of previous examples of the broad task and one-shot in terms of the specific word.

[p. 29] Table 3.16 shows the 6 examples generated; all definitions were human-generated, and the first answer was human-generated as conditioning while the subsequent answers were generated by GPT-3. These examples were generated continuously in one sitting and the authors did not omit or repeatedly try any prompts. In all cases the generated sentence appears to be a correct or at least plausible use of the word. In the final sentence the model generates a plausible conjugation for the word "screeg" (namely "screeged"), although the use of the word is slightly awkward ("screeged at each other") despite being plausible in the sense that it could describe a toy sword fight. Overall, GPT-3 appears to be at least proficient at the task of using novel words in a sentence.

**Figure 3.16** (p. 29): "Representative GPT-3 completions for the few-shot task of using a new word in a sentence. Boldface is GPT-3's completions, plain text is human prompts. In the first example both the prompt and the completion are provided by a human; this then serves as conditioning for subsequent examples where GPT-3 receives successive additional prompts and provides the completions. Nothing task-specific is provided to GPT-3 other than the conditioning shown here."
- Shows 6 word-definition-sentence examples:
  1. **"whatpu"** -- "A 'whatpu' is a small, furry animal native to Tanzania." Sentence: "We were traveling in Africa and we saw these very cute whatpus." (human-generated conditioning)
  2. **"farduddle"** -- "To do a 'farduddle' means to jump up and down really fast." Sentence (GPT-3): **"One day when I was playing tag with my little sister, she got really excited and she started doing these crazy farduddles."**
  3. **"yalubalu"** -- "A 'yalubalu' is a type of vegetable that looks like a big pumpkin." Sentence (GPT-3): **"I was on a trip to Africa and I tried this yalubalu vegetable that was grown in a garden there. It was delicious."**
  4. **"Burringo"** -- "A 'Burringo' is a car with very fast acceleration." Sentence (GPT-3): **"In our garage we have a Burringo that my father drives to work every day."**
  5. **"Gigamuru"** -- "A 'Gigamuru' is a type of Japanese musical instrument." Sentence (GPT-3): **"I have a Gigamuru that my uncle gave me as a gift. I love to play it at home."**
  6. **"screeg"** -- "To 'screeg' something is to swing a sword at it." Sentence (GPT-3): **"We screeged at each other for several minutes and then we went outside and ate ice cream."**
- Demonstrates GPT-3's ability to correctly use novel words (including generating plausible conjugations) after seeing only a definition and one prior example of the task format.
