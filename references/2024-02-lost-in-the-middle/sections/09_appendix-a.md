# A Ambiguity in Multi-Document QA Distractor Documents [p. 14]

Following past work on NaturalQuestions-Open (Izacard et al., 2021; Izacard and Grave, 2021, *inter alia*), the authors use a Wikipedia dump from late 2018 as their retrieval corpus. However, this standard Wikipedia dump has a small amount of temporal mismatch with the NaturalQuestions annotations. [p. 14]

For example, consider the question "what nfl team does robert griffin iii play for". The NaturalQuestions annotated answer is "currently a free agent". However, the Wikipedia retrieval corpus contains the information that he plays for the "Baltimore Ravens", since he was released from the team between the Wikipedia dump's timestamp and the NaturalQuestions annotation process. [p. 14]

The authors use the ambiguity annotations of Min et al. (2020) to create a subset of unambiguous questions. Experiments on this unambiguous subset of the data show similar results and conclusions as the experiments on the full questions collection (Figure 12). [p. 14]

**Figure 12** (p. 14): "Language model performance on a unambiguous subset of questions."

The figure shows accuracy (y-axis, approximately 58-76%) vs. position of document with the answer (x-axis, 1st to 20th) for 20 total retrieved documents (~4K tokens, unambiguous questions). Six models are shown: claude-1.3, claude-1.3-100k, gpt-3.5-turbo-0613, gpt-3.5-turbo-16k-0613, mpt-30b-instruct, and longchat-13b-16k. The same U-shaped performance curve is observed as in the full question set. Performance is highest at the 1st position (approximately 65-76% depending on model) and at the 20th position, with a dip in the middle positions around the 10th document.
