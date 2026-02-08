# Appendix E: Qualitative Analysis [p. 13-15]

[p. 13] The authors manually analyze examples from each of the datasets in the benchmark demonstrating cases that require contextualizing and synthesizing information over long ranges of text. Figures 5, 6, 7, 8 and 9 showcase gold references, relevant parts from input documents required to generate those references, and queries when they exist, from GovReport, QMSum, Qasper, NarrativeQA and ContractNLI. Together with the SummScreenFD example in Figure 2 and the QuALITY example in Figure 3 they illustrate cases where important information is spread across multiple sections of the inputs.

**Figure 5** (p. 14): "An example from GovReport, a dataset of government reports and their expert-written summaries. This example shows the spread of the relevant information in the document, exemplified by the first and last sentences of the summary."
- Shows a document excerpt about internet layers and the Deep Web, with word count markers ("...[486 words]...", "...[346 words]...", "...[3,791 words]...", "...[979 words]...") showing how relevant information for the first and last summary sentences is spread across the document. The document discusses topics including the Deep Web, the FBI's development of malware to identify Tor users, and law enforcement techniques for deanonymizing dark web activity.

**Figure 6** (p. 14): "An example from QMSum, a query-based summarization dataset over meeting transcripts. Information relevant for generating the last two sentences in the answer is spread in different locations in the transcript."
- Query: "What did the group discuss about budget balancing?"
- Shows an answer followed by a meeting transcript excerpt with word count markers ("...[1,813 words]...", "...[656 words]...", "...[4,651 words]...") illustrating how the relevant information is scattered across the transcript. The discussion involves LCD screens, advanced chip costs, budget limits, and transmitter/receiver/speaker hardware decisions.

**Figure 7** (p. 14): "An example from the Qasper dataset, which includes question answering over scientific papers. The evidence for the first part of the reference answer appears in the introduction, while the indication that neural models were also experimented with exists further in the document, in a description of the results table."
- Question: "What approaches without reinforcement learning have been tried?"
- Answer: "classification, regression, neural methods"
- Shows an article excerpt with word count markers ("...[142 words]...", "...[1,006 words]...", "...[1,398 words]...") demonstrating that the answer components come from different sections of the paper: the contributions statement mentions classification and regression approaches, while the results table description mentions neural regressor (NNR) and neural classifier (NNC).

**Figure 8** (p. 15): "An example from NarrativeQA, where the task is to answer questions about books and movie scripts. In this question about The Hound of the Baskervilles, the answer is first discussed in several places without certainty, where even the final reveal is preceded by an explicit distractor."
- Question: "Whose initials are on the bottom of the burnt letter to Sir Charles?"
- Answer: "Laura Lyons"
- Shows a story excerpt with word count markers ("...[35,871 words]...", "...[861 words]...", "...[1,983 words]...", "...[97 words]...", "...[19,996 words]..."). The relevant information appears in multiple places: a letter from Coombe Tracey addressed in a woman's hand, a burned letter with initials "L. L." found in the grate, identification of Laura Lyons as having initials L. L., and eventually Mrs. Lyons' confession "Yes, I did write it."

**Figure 9** (p. 15): "An example from ContractNLI, a natural language inference dataset over non-disclosure agreements (NDAs). Here, the challenge of finding the evidence, residing in the middle of a long document, is further amplified by the hypothesis being only implicitly contradicted."
- Hypothesis: "All Confidential Information shall be expressly identified by the Disclosing Party."
- Label: Contradiction
- Shows a contract excerpt with word count markers ("...[427 words]...", "...[1,661 words]...", "...[4,178 words]..."). The contract defines "Confidential Information" broadly (section 3.1.4) to include "technical, scientific, commercial, financial and market information, trade partners, potential clients, trade leads and trade secrets, and all other information in whatever form," and states that if the Recipient is uncertain whether information is Confidential, it should treat it as confidential until the contrary is agreed in writing. This implicitly contradicts the hypothesis that all confidential information must be expressly identified.
