# D GPT-4 Performance [p. 15]

The authors evaluate GPT-4 (8K) on a subset of 500 random multi-document QA examples with 20 total documents in each input context (Figure 15). GPT-4 achieves higher absolute performance than any other language model, but still shows a U-shaped performance curve -- its performance is highest when relevant information occurs at the very start or end of the context, and performance degrades when it must use information in the middle of its input context. [p. 15]

**Figure 15** (p. 15): "Although GPT-4 has higher absolute performance than other models, its performance still degrades when relevant information occurs in the middle of the input context."

The figure shows accuracy (y-axis, approximately 50-90%) vs. position of document with the answer (x-axis, 1st to 20th) for 20 total retrieved documents (~4K tokens, 500 question sample). Seven models are shown: claude-1.3, claude-1.3-100k, gpt-3.5-turbo-0613, gpt-3.5-turbo-16k-0613, mpt-30b-instruct, longchat-13b-16k, and gpt-4-0613. GPT-4-0613 (pink line) achieves the highest accuracy overall, starting at approximately 82% at position 1, dipping to approximately 60% around positions 10-15, and rising back to approximately 72% at position 20. Other models show their typical U-shaped curves at lower absolute performance levels (approximately 50-75%).
