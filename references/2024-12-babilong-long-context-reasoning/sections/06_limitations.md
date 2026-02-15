# Limitations [p. 10]

## Background text sources [p. 10]

The BABILong benchmark uses background texts to hide facts in them. In our experiments, we only tried PG19 and Wiki as background text sources. Other background texts may have a different effect on the results. PG19 and Wiki were chosen as they contain natural narratives and facts about people, in a way similar to bAbI tasks. Interference between similar facts in the background text can make the benchmark even more difficult. [p. 10]

## RAG optimization [p. 10]

In GPT-4 and LLama-3 with RAG experiments, we do not optimize the retrieval component. We tried several prompts experiments with LLMs, but the ones that we selected could be suboptimal. We provide them in Appendix J and in our GitHub repository. [p. 10]

## Limited vocabulary in fact generation [p. 10]

The current version of the dataset reuses parameters for fact generation from the bAbI (Weston et al., 2016). As the initial work used vocabularies of limited size, this results in a low variety of names and objects within the facts. This limitation makes the BABILong tasks easier for fine-tuned models, as they can quickly learn specific tokens that differentiate facts from background text. This issue is partially mitigated by generating distractor facts using the same vocabularies. Enhancing the dataset's vocabulary in future versions could easily address this limitation. [p. 10]

## Alternative fact sources [p. 10]

We could also use other sources of facts and questions (e.g., reasoning datasets such as Rule-taker (Clark et al., 2020), ProofWriter (Tafjord et al., 2021), FOLIO (Han et al., 2022), PrOn-toQA (Saparov & He, 2023), LogicNLI (Tian et al., 2021), and DELTA (Pouflis et al., 2024)), mixing samples of question-answering datasets with background text from the same domain, or using LLMs to generate questions about statements that belong to the original documents. Keeping the same framework as in BABILong, this will lead to more complex and real-world scenarios. [p. 10]

## Sequential nature of RMT [p. 10]

Although recurrent approaches, like RMT, are hindered by their sequential nature, resulting in reduced parallelizability, they compensate by constant memory requirements, but it is also their limitation as storage capacity of the model is finite. However, BABILong is solvable by this type of models. [p. 10]
