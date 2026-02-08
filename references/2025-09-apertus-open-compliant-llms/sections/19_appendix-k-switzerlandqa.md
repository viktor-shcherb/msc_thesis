# Appendix K: SwitzerlandQA [p. 102]

[p. 102] To evaluate whether Apertus can serve as a knowledgeable foundation for Sovereign AI initiatives, the authors test the model on its understanding of Switzerland's environment by developing a novel benchmark **SwitzerlandQA** specifically tailored to Switzerland's context.

## Benchmark Design

The benchmark spans five domains that reflect the themes emphasized in Swiss naturalisation exams, civic education materials, and integration resources:

- **Geography** -- covers Switzerland's location, terrain, hiking regions, population, general economy, and climate
- **History** -- addresses significant events, notable figures, and key developments across time
- **Social Life** -- includes food, traditions, and festivals that shape everyday culture
- **Political Life** -- focuses on Switzerland's political organization and institutional structure
- **Insurance** -- a particularly relevant civic topic, covers national insurance rules as well as canton-specific systems for subsidies and related regulations

## Dataset Statistics

[p. 102] The benchmark represents 26 cantons, with each canton having at least 200 questions, yielding **9,167 unique items per language** across domains and levels of granularity. To support multilingual evaluation, the dataset was translated into German, French, Italian, Romansh, and English. Automatic translations were subsequently sampled and checked to ensure semantic fidelity and terminological consistency. Each item follows a four-option multiple-choice format with a single correct answer.

## Granularity Levels

Questions are organized at three levels of granularity:

- **National level:** broad knowledge relevant to Switzerland as a whole (e.g., "What is the highest mountain in Switzerland?")
- **Cantonal level:** knowledge specific to an individual canton (e.g., "What event led to Appenzell's excommunication in the early 15th century?")
- **Commune level:** fine-grained local knowledge at the municipal level (e.g., "What was the population of the commune of St. Sulpice in 2023?")

Although all three levels are represented, the cantonal level was prioritized, as it provides a balance between the generality of national questions and specificity of commune ones.

## Data Collection

[p. 102] For data collection, the authors relied primarily on official sources. Where possible, they included questions from naturalisation exams, which represent a standardized and widely recognized measure of civic knowledge. To expand coverage, they contacted cantonal cultural departments and requested resources containing authoritative information in the target domains. Where insufficient questions were available, new items were generated in English using GPT-4o, guided by official materials to preserve factual accuracy and regional relevance. In total, they compiled information from **107 unique official data sources**, ranging from canton-level handbooks and civic guides to municipal archives.

## Limitations

[p. 102] The dataset also has limitations:

1. While translations into German, French, Italian, and English were generally reliable, the Romansh subset carries a higher risk of translation inaccuracies due to the limited linguistic resources.
2. Coverage across cantons is uneven: some cantons provide extensive official documentation on their history, culture, and institutions, while others offer much less. As a result, the depth of representation varies across cantons, which may introduce regional evaluation imbalances.
