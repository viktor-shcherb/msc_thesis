# What Makes Long Context More than Retrieval? [p. 3]

We require a taxonomy to capture task difficulty variations beyond mere "number of tokens". We focus on the information that is canonically required to solve the task as the conditioning variable. Our classification can be summarized via the following two questions, when asked about a task:

(I) How difficult is it to find and extract the required information?

(II) How much information is needed to be found?

Assuming that some highlighted portion of the relevant information is needed to solve the task (see Figure 1), the latter question asks how much text is highlighted, while the former addresses the challenge of locating the relevant text for highlighting.

For instance, consider the task of summarizing a book, in comparison to a NIAH style of identifying a numerical detail in a long financial report (e.g., "how much did the company earn in 2015?"). Although both tasks involve long texts, the information required and its accessibility vary significantly. The NIAH task focuses on localized, identifiable information. The book summarization task is more difficult on both axes (I) and (II).

## (I) Dispersion

Although the question above intuitively defines "difficulty of information finding", we offer a more concrete description. Between two similar tasks, we consider the information harder to find in one task compared to another if: (1) it is more obscured (e.g., linguistically, semantically, contextually, etc); (2) it is more sparse, such that it is interspersed with non-required information; (3) its indicators are less redundant, such that there are fewer places in the document where the same information is available.

## (II) Scope

The property of scope is simpler, and refers to the minimal quantity of information needed to solve the task. Importantly, we are not concerned with precise metric for "quantity of information" at this stage – it can refer to quantity of tokens, sentences, relations, cells in a table, etc. Any metric that reliably captures difficulty for an established solver is sufficient for our purposes.

### Illustrative example

To illustrate, consider the Wikipedia entry for New York City and a simple question: "What is the estimated population of the city?" Since the task requires a small snippet of information, we say that the task has small scope. And since it is easily accessible, we say that it has low dispersion. Contrast instead, the question "how many syllables are in this document?" – since this question requires the entire document to answer, we say that it has large scope, but if we consider counting syllables as straightforward, then we say its dispersion is still low. Finally, with the question "Was the city's mayor elected before or after the city was affected by Hurricane Sandy?" – since it requires snippets from at least two different areas of the text, we can say that when compared to the question about the city's population, the dispersion is higher, but not as high as for the question "What makes the city a prominent place on the world stage?" which poses a challenge on both axes.
