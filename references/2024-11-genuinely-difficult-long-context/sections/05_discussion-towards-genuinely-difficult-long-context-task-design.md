# Discussion: Towards Genuinely Difficult Long-Context Task Design [p. 4–5]

## Challenges

Designing meaningful long-context tasks amidst rapid model progress is profoundly challenging, making the deficiency in tasks representing difficulty on both the dispersion and scope axes unsurprising. One source of this challenge is the lack of diverse, coherent long texts, as models' context windows can now be comparable to the length of the New Testament¹ and the Odyssey.² The methodologies discussed in §2 for creating long context tasks – lengthening short context tasks and synthetically creating length-adjustable tasks – are preferred for their straightforward definition and the incremental adjustments they require on existing data. They rely on the common understanding of machine comprehension as formulated with short context in mind (Dunietz et al., 2020), and therefore they are intuitive and easy to comprehend for NLP researchers without domain expertise (e.g., in law or biomedical fields that have long contexts).

## Future work

The goals laid forward in this work are clear: For more durable and robust measurements of long-context capabilities, we must design tasks that explicitly target both the dispersion and scope capabilities of models. How can this be achieved? As mentioned, one possible avenue is to rely more on tasks that require domain expertise, such as legal documents (Bruno and Roth, 2022), financial reports (Reddy et al., 2024), biomedical publications (Stylianou et al., 2021), and so on. In specialized domains, it is common that dispersion will be naturally higher (Zhao et al., 2023). Tasks that involve implicit aggregations over structured data, such as table manipulation (Caciularu et al., 2024), are possible avenues for increasing both scope and dispersion synthetically by leveraging the data structure. In this work, we argue that an explicit vocabulary for such properties of difficulty is what can enable more informed long-context task design in the future.

## Retrieval is still interesting

Although we argue that small scope and low dispersion tasks are the least indicative of the model's ability to long-context capabilities, tasks that are well-served by implicit retrieval or by traditional retrieval-based pipelines are certainly relevant and useful in a variety of common use-cases (Stylianou et al., 2021; Bruno and Roth, 2022; Gao et al., 2023).

## Other uses for a long-context window

This paper only talks about long context inputs that serve as inputs to a task. The long context of course can have other purposes as well, like containing many in-context examples (Bertsch et al., 2024) or containing other modalities and structures (Jiang et al., 2023).

## Acknowledgments

The authors would like to thank Gabriel Stanovsky for the fruitful discussions. This work has been funded by the Israel Science Foundation, grant number 23/670, for which we are grateful.

---

¹www.readinglength.com/book/isbn-0198980805
²www.readinglength.com/book/isbn-0140268863
