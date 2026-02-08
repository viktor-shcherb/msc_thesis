# 3 FLenQA [p. 3-5]

[p. 3] FLenQA (Flexible LENgth Question Answering) follows the requirements set in Section 2.

FLenQA is composed of three reasoning tasks: Monotone Relations (a new task), People In Rooms (a new task) and a simplified version of Ruletaker (Clark et al., 2021). Each task consists of 100 base instances, from which variations of different lengths, different background texts, and different dispersion of facts within the background texts are created.

Each task is completely balanced in its label distribution ("True" and "False"), and they ensure that most base-instances within it will be solved correctly by the LLMs when presented in their un-expanded forms.

The dataset and the code to generate it from scratch are released to support future studies of reasoning and long input performance. Generating the dataset from scratch can be used to prevent data contamination in future evaluation. Details and statistics of the tasks appear in Appendix A.

## 3.1 Base instances [p. 3]

Each base-instance consists of (1) an *optional prefix* (for example introducing the task or supporting facts); (2) *two key paragraphs*, each of which is thematically coherent and starts with a *key sentence* needed for solving the task; and (3) an *optional suffix* (for example, asking a question about the preceding context). Footnote 3: The optionality is at the task level, either all instances in the task have a prefix/suffix, or they don't.

For each instance, the different parts are joined by newlines and fed to the LLM.

Throughout the text, key paragraphs are typeset in red, the supporting sentences within them in darker red, and the optional prefixes and suffixes in black. The full prompts used for each dataset are in Appendix B.

**Deriving the key paragraphs:** Each task relies on two facts, expressed as simple sentences. Each of these sentences is then expanded to a thematically-coherent paragraph, in order to ensure the naturality requirement. This expansion is performed using GPT-4, which they prompt to extend the sentences without adding new information, followed by a manual verification of the results by the authors.

## 3.2 The tasks [p. 3-4]

**Monotone relations (MonoRel):** Each key sentence is comparing two person names on a monotone scale, e.g. "X is larger than Y", "Y is larger than Z". The suffix is a True/False question that asks about a relation between two entities that appear in different sentences (they are not explicitly compared in the text). The relations are transitive and monotone in nature.

> MonoRel Example:
> **Julie Baker is younger than Julian Barton.** This is a fact that remains constant, unchanging like the northern star. It's a truth that is as clear as day that she ...
> **Samantha Arnold is younger than Julie Baker.** It means that Samantha Arnold has experienced fewer birthdays than Julie Baker. ...
> Is Samantha Arnold younger than Julian Barton?

This data is inspired by different monotonic relations describing kinship, introduced by Sinha et al. 2018. They define a new set of relation types in this work. Following the requirements in Section 2, answering the question requires reasoning over both key sentences. The data is created programmatically by randomly drawing names from the Faker python library (Faraglia and Contributors, 2012) and a relation from a list of hand-crafted relations.

[p. 4] **People In Rooms (PIR):** In each sample, in one key sentence a person is said to be located in a named room ("*X is in the old library*"), and the other key sentence describes the room to have a certain property ("the old library has wooden floors"). The task is then to infer whether the given person is located in a room with the given property.

> PIR Example:
> **John's living room is marble-floored**, a reality that is as intrinsic to the building as its very foundations. The moment ...
> **Ethan Washington is in John's living room**, a fact that has become as much a part of the place as the walls and the ceiling. The truth that Ethan Washington is in John's living ...
> Is Ethan Washington in a marble-floored room?

This dataset is inspired by the bAbI set of tasks (Weston et al., 2016), where reasoning is conducted on paths taken by one or more agents. PIR is a simplification of the task, involving just one agent. The names of people in the task are drawn randomly (Faraglia and Contributors, 2012). Rooms and properties were hand selected to be mutually exclusive (for example, a room is either blue-walled or red-walled), so no ambiguous examples are created.

**Simplified Ruletaker:** They employ the task formulation from Ruletaker (Clark et al., 2021), a benchmark designed for theorem proving within texts that present explicit logical theories in natural language. Each instance consists of a logical rule, two sentences each introducing a fact, and a question over the rule and facts. Footnote 4: Initial experiments revealed that most LLMs still struggle with instances involving multiple rules or more than two facts. Their Simplified Ruletaker task consists of generated samples that fit these criteria.

> Simplified Ruletaker Example:
> Facts:
> **Erin is furry.** Erin is known for his furriness. He has a lot of fur and ...
> **Erin is good.** Erin was always known for how good he is. His goodness appears on all matters of life ...
> Rule: If X is big and X is good then X is tall.
> Question: can the statement "Erin is tall" be derived from the rule and the facts?

## 3.3 Length Variations [p. 4-5]

[p. 4] Each base instance is expanded to input lengths of roughly 250, 500, 1000, 2000, and 3000 tokens. Footnote 5: They consider a sample to be of length N if its token count as measured by the GPT4 tokenizer is in (N - 70, N + 70).

To extend the inputs to those targets, they add background text that is irrelevant to the question ("padding", per Section 2). For each basic-instance and length pair, they create different versions that differ in their source of background text: either *duplicate*, *similar* or *different* than the key paragraphs of the instance. For each of these, they also vary the dispersion of the key-paragraph within the background text.

### 3.3.1 Background Texts [p. 4-5]

**Duplicate:** To evaluate the extreme case where the length changes but the information remains the same, they perform an experiment where the each length text consists of multiple copies of the key paragraph. They duplicate each key paragraphs without any modification to achieve the target length of the input. The two duplicated paragraphs appear in alternating order until the desired sample length is achieved. In this case, of the two sub-tasks of QA reasoning - identifying the key information and reasoning over it, the first sub-task is trivial.

**Similar: resampling from the same task.** To get background text that is similar to the key paragraphs, they pad using paragraphs sampled from other base instances of the same task. To avoid creating contradictions, they exclude paragraphs that contain entities appearing in the key paragraphs. This padding therefore does not produce adversarial or ambiguous versions of the samples. This type of padding creates an input that resembles the RAG setup, where the input is composed of independent texts from a similar source (Mao et al., 2020).

[p. 5] **Different: Book Corpus.** To get background text that differs from the key paragraphs, they use text from the Books Corpus (Zhu et al., 2015). They sample a random (continuous) text from the Book Corpus, and inject each of the key paragraphs within it, while respecting sentence boundaries.

### 3.3.2 Location of key paragraphs in the text [p. 5]

Four distinct ways in which the key paragraphs are dispersed within the background text are considered. In the first three cases the key paragraphs appear adjacent to each other, while in the fourth the key paragraphs are separated by intervening text of various lengths.

(1) *Key paragraphs first*: The key paragraphs appear at the beginning of the text followed by padding;

(2) *Key paragraphs middle*: Half of the padding is affixed before and half after the key paragraphs, but not between them (the key paragraphs are exactly in the middle);

(3) *Key paragraphs last*: The key paragraphs appear at the end of the text, with padding prepended before them as a prefix;

(4) *Random placement*: padding is added before, between and after the paragraphs, with random intervals.

A visual representation is provided in Figure 2.

**Figure 2** (p. 5): "Inputs construction. Key sentences (dark red), are expanded to key paragraphs (light red) which are dispersed in controlled locations among padding text (grey) which is irrelevant to the task."
- Shows four input construction layouts: Key Paragraphs First, Key Paragraphs Middle, Key Paragraphs Last, and Random Placement. Each layout is illustrated as a block of text with red (key) paragraphs placed at the described position among grey (padding) text.

## 3.4 Base instances are answerable [p. 5]

The baseline accuracy is estimated by evaluating the LLMs on the minimal text of each sample in the dataset that includes only the question and the key paragraphs relevant to it. The results of the base instances are brought in Table 1. They found that even when using non-CoT prompting, four out of the five models achieve high accuracy (>0.89). The lowest performing model (GPT3.5) achieves high enough accuracy for degradation to be observable (0.77).

**Table 1: Minimal length accuracy.** The evaluated models have high accuracy on the tasks in our dataset when evaluated on the minimal text (250 tokens). CoT improves performance across almost all tasks and models.

| Model          | Prompt | MonoRel | PIR  | Ruletaker* |
|----------------|--------|---------|------|------------|
| GPT3.5         | Direct | 0.77    | 0.81 | 0.74       |
|                | CoT    | 0.86    | 0.88 | 0.88       |
| GPT4           | Direct | 1.00    | 1.00 | 0.98       |
|                | CoT    | 1.00    | 1.00 | 0.97       |
| Gemini Pro     | Direct | 0.84    | 1.00 | 0.92       |
|                | CoT    | 0.88    | 0.96 | 0.97       |
| Mistral Medium | Direct | 0.99    | 1.00 | 0.73       |
|                | CoT    | 1.00    | 1.00 | 0.89       |
| Mixtral 8x7B   | Direct | 0.92    | 0.97 | 0.80       |
|                | CoT    | 0.86    | 0.97 | 0.93       |
