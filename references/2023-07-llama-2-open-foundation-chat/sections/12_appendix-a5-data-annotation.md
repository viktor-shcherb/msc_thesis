# A.5 Data Annotation [p. 72–75]

[p. 72] Human annotators were relied upon to collect annotations for the supervised fine-tuning stage and human preferences to train the reward models. This section provides details about the data annotation process.

## A.5.1 SFT Annotation Instructions [p. 72]

[p. 72] Single-turn and multi-turn dialogue annotations were collected from a pool of annotators. Annotators were asked to write responses that are informative, truthful, relevant, clear and harmless. They were also asked to prioritize harmlessness over informativeness and helpfulness in cases of prompts that could lead the responses to be problematic. The kind of responses that could lead to negative user experiences were categorized and shared with the annotators. A summary of these categories can be seen in Section A.5.2.

## A.5.2 Negative User Experience Categories [p. 74]

[p. 74] There are different kinds of responses that could cause a negative user experience when interacting with the models. Annotators were instructed to avoid writing responses that violate safety guidelines, for example, they were asked that prompts they write *do not*:

1. Promote or enable criminal activities.
2. Promote or enable dangerous behaviors to the user or other people.
3. Contain, promote or enable offensive and abusive behavior towards the user or other people.
4. Contain, promote or enable sexually explicit content.

## A.5.3 Quality Assurance Process [p. 74]

[p. 74] A quality assurance process was implemented to ensure only high quality annotations were used for training the model. A team of highly skilled content managers manually reviewed the annotations and approved the ones that would be used.

During the quality assurance step, reviewers were asked to only approve those annotations that matched the guidelines: (a) they are consistent with the dialogue history, (b) follow instructions in the prompt, (c) are free of grammatical, spelling and other writing errors, and (d) do not fall into any of the categories described in Section A.5.2. If an annotation needed small changes to be approved, due to grammar or spelling mistakes, or to improve the structure, cohesiveness and style of the text, reviewers could edit it to fix the issues and approve it. If the answer could not be approved without major changes, the reviewers were asked to reject it and write the feedback necessary to improve it.

## A.5.4 Annotator Selection [p. 74–75]

[p. 74] To select the annotators who could work on different data collection tasks, a multi-step assessment process was conducted where understanding of the guidelines, alignment with quality assessment criteria, alignment with sensitive topics guidelines, and reading and writing skills were tested.

The process included 4 tests:

- The first test consists of 3 sections of testing to evaluate grammar, reading comprehension and writing style. Each section is timed and the test should take a total of 50 minutes to complete. A candidate must score 90% on part I to continue on to parts II and III, and an average score of 4 on part II and III to pass the test. [p. 74]

- The second test consisted of 42 questions split into sensitive topics alignment, answer ranking and two examples of answer writing, which were manually reviewed. To pass the test, annotators needed to agree with the criteria on 80% of the answers, and pass the written examples with a score of 4 out of 5. [p. 74]

- [p. 75] The third test consisted in measuring the alignment with quality assessment criteria. The test consisted of 31 different questions asking the annotators to grade different prompt-answer pairs, as well as ranking different answers to the same prompt. To measure alignment, responses from different team members were first collected, and the annotators who agreed with the preferences in more than 26 of the questions passed the test.

- Finally, the last test consisted of a prompt response assessment where annotators choose a minimum of 6 out of 18 prompts to write responses for. Each response was manually assessed to evaluate production readiness. Annotators that have scored an average of >4 have passed the training.
