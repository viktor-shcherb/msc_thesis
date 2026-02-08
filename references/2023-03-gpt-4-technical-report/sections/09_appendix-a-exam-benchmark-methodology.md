# Appendix A: Exam Benchmark Methodology [p. 24-26]

## A.1 Sourcing [p. 24]

[p. 24] Exams were sourced from either the most recent publicly-available official past exams, or practice exams in published third-party 2022-2023 study material which were purchased. These materials were cross-checked against the model's training data to determine the extent to which the training data was not contaminated with any exam questions, which is also reported in the paper.

The Uniform Bar Exam was run by collaborators at CaseText and Stanford CodeX. [p. 24]

## A.2 Prompting: multiple-choice [p. 24]

[p. 24] For each multiple-choice section, a few-shot prompt with gold standard explanations and answers for a similar exam format was used. For each question, an explanation was sampled (at temperature 0.3) to extract a multiple-choice answer letter(s).

Each multiple-choice section was sourced as a pair of exams: one holdout and one nonholdout. The methodology was iterated on using the nonholdout exam, and then each holdout exam was run once for a final score. No nonholdout exam was sourced for the USABO and for the MKSAP questions; instead these were run once using the best-guess methodology as determined by iterating on the AP Biology exam. [p. 24]

For the AMC 10 and AMC 12 held-out test exams, a bug was discovered that limited response length. The bug was fixed and the exams were rerun to ensure accurate results. For most exam runs, the model's letter choice was extracted directly from the explanation. For the GPT-4 USABO and SAT reading/writing runs (with and without vision), the GPT-3.5 runs, and the GPT-4 runs of SAT Math, GRE, USNCO, AP Biology, AP Chemistry, and AP Environmental Science without vision, a letter choice was instead sampled at temperature 0 using the already-sampled explanation. These methodological differences resulted from code mismatches detected post-evaluation, and the authors believe their impact on the results to be minimal. [p. 24]

## A.3 Prompting: free-response [p. 24]

[p. 24] For each free-response section, the model was given the free-response question's prompt as a simple instruction-following-style request, and a response was sampled using temperature 0.6. For AP exams, the most recent 2022 prompts were used, which are all publicly-available; for the SAT, three prompts were used -- Sample Essay Prompt 1 and Sample Essay Prompt 2 from *Test Specifications for the Redesigned SAT* (CollegeBoard, 2015) plus the official SAT Practice Essay #1 (CollegeBoard, 2016) -- and the average score was taken; for the GRE, the issue essay and argument essay prompts from a commercially-available prep book were used.

Due to the longer iteration time of human expert grading, no methodology iteration on temperature or prompt was done; instead the free response questions were each run only a single time at the best-guess temperature (0.6) and prompt (a simple instruction-following prompt displayed in section A.8). [p. 24]

All free-response questions consisting of formal essays which required evaluation of writing quality (AP English Language and Composition, AP English Literature and Composition, AP World History, AP US History, AP US Government and Politics, AP Art History, the GRE, and the SAT) were graded by 1-2 qualified third-party contractors with relevant work experience grading those essays. The responses were sampled using a few-shot prompt containing one high-quality sample GRE essay response (also shown in section A.8) in order to encourage the model to produce appropriately sophisticated text, rather than an unnaturally terse reply. All other free-response questions were graded on their technical content, according to the guidelines from the publicly-available official rubrics. [p. 24]

## A.4 Images [p. 25]

[p. 25] Oftentimes, an exam question may include an image. Models like GPT-3.5, which consume text (but not images) as input might not have access to all the information needed to correctly solve a problem. When evaluating text models on multiple-choice questions, a text tag stating IMAGE was included with a non-meaningful filename wherever an image would be missing. This allows lower-bounding the text-based models' performance on multiple-choice exams.

When evaluating multimodal models on multiple-choice questions, the images were embedded into the prompt. The SAT Reading and Writing, MKSAP, Sommelier, AP Psychology, AP English Language, and AP English Literature exams' multiple-choice sections did not contain any images. For all free-response questions, plus the USABO 2020 Semifinal, any images and diagrams were instead transcribed as objectively as possible. This reduced the manual grading load required to evaluate free-response answers, because after this transcription process the free-response prompts include no images, so the scores for GPT-4 could be run once and used for both the vision and no-vision conditions. [p. 25]

Note: Footnote 12 states: "For example, on the AP Statistics exam, a common failure response was 'Since there is no graph provided, we cannot determine the correct answer for this problem.'" [p. 25]

## A.5 Scoring [p. 25]

[p. 25] Multiple-choice section scores and free-response section scores were synthesized into overall scores using the best available approximations of the real methodologies:
- **SAT:** Multiple-choice scores were converted into scaled scores using the score calculation chart from an official sample SAT as republished on an SAT prep site [74].
- **GRE:** Multiple-choice scores were converted to the 130-170 scale using the official formula of multiplying accuracy by 40 and adding 130.
- **AP exams:** Score calculators found on a public study site were used, which are based on the point values from the official AP scoring guidelines from 2019-2020 [75].

Percentiles are based on the most recently available score distributions for test-takers of each exam type. [p. 25]

For percentile results on the AMC 10 and 12, since 2022 score distributions are as yet unpublished, two official published score distributions from November 2021 for exams A and B were used, and the minimum lower percentile of the two and the maximum upper percentile of the two were taken to report an estimated percentile range [76]. Other percentiles were based on official score distributions [77] [78] [79] [80] [81]. [p. 25]

## A.6 Codeforces rating [p. 25]

[p. 25] To determine the Codeforces rating (ELO), each model was evaluated on 10 recent contests. Each contest had roughly 6 problems, and the model was given 10 attempts per problem. After each contest, ELO adjustments were repeatedly performed based on the model's performance until the ELO rating converges to an equilibrium rating (this simulates repeatedly attempting the contest with the same model performance). Each of the 10 contests was simulated 100 times, and the average equilibrium ELO rating across all contests is reported.

Roughly 50% of simulations have 0 problems solved, which results in an equilibrium ELO rating of 0. As a result the final average ELOs are quite low. The maximum equilibrium ELO achieved on a single contest was around 1000 for GPT-3.5 and 1300 for GPT-4. [p. 25]

## A.7 Model snapshot details [p. 25]

[p. 25] GPT-4 multiple-choice questions were run using a model snapshot from March 1, 2023, whereas the free-response questions were run and scored using a non-final model snapshot from February 23, 2023. GPT-3.5's multiple-choice questions and free-response questions were all run using a standard ChatGPT snapshot. The USABO semifinal exam was run using an earlier GPT-4 snapshot from December 16, 2022.

The evaluations suggest RLHF does not significantly affect the base GPT-4 model's capability -- see Appendix B for more discussion. [p. 25]

## A.8 Example few-shot prompts [p. 26]

[p. 26] An example few-shot prompt is shown for a multiple choice exam (AP Art History [82]).

The prompt format begins with "ANSWER KEY" followed by "Here are the answers for the problems in the exam." Each problem is presented with the question text, answer choices labeled [A] through [D], an explanation paragraph, and a final line stating "The answer is therefore [X]".

Five example problems are shown from AP Art History, followed by a template for the sixth problem (the actual test question):

**Problem 1:** "Choose the most likely completion of the following sentence. Honore Daumier's Nadar Raising Photography to the Height of Art was done immediately after __." Choices: [A] the first photographic exhibition in history, [B] the first use of color photography, [C] a court decision that determined that photographs could be considered works of art, [D] the invention of the zoopraxiscope. Answer: [C]. The explanation notes this relates to Nadar, a famous French photographer, and the recognition of photography as a legitimate art form via a court decision.

**Problem 2:** "Artists working in New Spain were most influenced by contemporary art in Europe during which of the following periods?" Choices: [A] Romanticism, [B] Renaissance, [C] Mannerism, [D] Baroque. Answer: [D]. The explanation discusses how the Baroque period's ornate and elaborate styles influenced by the Catholic Church were well-suited to art produced in New Spain.

**Problem 3:** "Choose the most likely completion of the following sentence. Works like the Sistine Chapel frescoes directly influenced the form and scale of works by __." Choices: [A] Gianlorenzo Bernini, [B] Giovanni Battista Gaulli, [C] Peter Paul Rubens, [D] Rachel Ruysch. Answer: [B]. The explanation notes Giovanni Battista Gaulli (Baciccio) was heavily influenced by the Sistine Chapel frescoes in his use of large-scale, dramatic compositions and religious themes.

---
[p. 27 continued]

**Problem 4:** "Choose the most likely completion of the following sentence. The work En la barberia no se llora (No Crying Allowed in the Barbershop) explores themes of __." Choices: [A] sexual stereotyping, [B] women's liberation, [C] conflict and peace, [D] racial discrimination. Answer: [A]. The explanation discusses how the barbershop as a masculine space where crying is not allowed reinforces traditional gender roles and stereotypes.

**Problem 5:** "Which of the following artists explored themes related to the human body and its relationship to the environment?" Choices: [A] Ai Weiwei, [B] Doris Salcedo, [C] Kiki Smith, [D] El Anatsui. Answer: [C]. The explanation notes Kiki Smith is known for exploring the human body and its relationship to the environment through fragmented or incomplete figures.

**Problem 6 (template):** The prompt shows the template format used after the few-shot examples. Problem 6 uses a placeholder `<PROBLEM TEXT AND ANSWER CHOICES GO HERE>`. The explanation is generated by the model with parameters `t=0.3, n=1, max_tokens=512, stop='\nThe answer is therefore'`. The final answer choice is then sampled separately with parameters `t=0.0, n=1, stop=']'`. [p. 27]

**Example prompt for a free-response question** [p. 27]: The prompt uses delimiter tokens. The task prompt would be replaced by a prompt like an official sample GRE essay task, and the essay response with an example of a high-scoring essay [83]. The format is:

- `<|endofreply|>Analytical Writing: Issue Essay`
- `<TEXT OF SAMPLE ISSUE TASK PROMPT>`
- `Response:<|endofprompt|><TEXT OF SAMPLE ISSUE TASK ESSAY RESPONSE - SCORE 6><|endofreply|>`
- `<FREE-RESPONSE PROMPT TEXT GOES HERE>`
- `Response:<|endofprompt|>`
- The answer is sampled with parameters `t=0.6, n=1, stop='<|endofreply|>'`. [p. 27-28]
