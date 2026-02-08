# 8 Final Discussions [p. 18]

[p. 18] The report discusses the full-stack development of the Yi language model family. Yi-34B achieves GPT-3.5 matching performance and is deployable (thanks to the 4/8-bit quantization) on consumer-grade devices, making it an ideal model for local deployment. [p. 18]

## Key Takeaways from Pretraining

[p. 18] The key takeaways from the Yi pretraining procedure are about data quantity and quality:

1. Training the model on a larger amount of data than the Chinchilla optimal delivers clear and consistent performance gain, which the authors highly recommend for all pretraining teams. The model is trained on 3.1T tokens, yet the authors believe with larger amount of data, they can continue to improve the model performance (i.e., the model has not saturated at 3.1T). [p. 18]

2. When it comes to the pretraining data quality, the authors believe the most critical two factors are the source of the data (e.g., whether the text is produced for professional usage or for casual social media posting) and the details of the data cleaning (e.g., the strength of filtering and deduplication). Since data cleaning is a very complicated pipeline and it is extremely difficult to conduct extensive grid-search styled optimizations, the current solution may still have room for improvements. [p. 18]

## Key Takeaways from Finetuning

[p. 18] The key takeaways from the Yi finetuning procedure is to heavily iterate on a small amount of data (≤ 10K), case by case, over multiple iterations, directly by the machine learning engineer, and improved from real user feedback. This approach clearly deviates from the instruction-scaling approach, initially introduced by the FLAN series [9] then followed by the UltraChat series [19]. [p. 18]

## Outlook

[p. 18] As demonstrated by the current results, the reasoning capability, which the authors view as the core capability for real-world deployment of language models, is strongly correlated with model scale when the amount of pretraining data is fixed. The authors believe that given the current results, continuing to scale up model parameters using thoroughly optimized data will lead to even stronger frontier models in upcoming next versions. [p. 18]
