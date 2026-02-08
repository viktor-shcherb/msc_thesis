# 5. Evaluation Results [p. 7–9]

[p. 7] Existing evaluations are increasingly strained by the new and rapidly advancing capabilities of large multimodal models. They typically focus on individual modalities and/or are restricted to tasks with shorter context lengths. The authors highlight a growing need for benchmarks which exemplify the nuanced requirements of real world long mixed-modality use cases. Among these, they highlight the quantitative assessment of reasoning capabilities across long mixed-modality sequences as a key challenge.

The evaluation of Gemini 1.5 series first focuses on understanding and evaluating its novel capabilities, then explores core benchmarks covering capabilities studied in the Gemini 1.0 Technical Report (Gemini-Team et al., 2023). Gemini 1.5 is evaluated in three main categories:^5

1. **Qualitative long-context multimodal evaluations:** manually probe and stress-test the model's long-context abilities, especially for novel capabilities where no quantitative benchmarks exist.
2. **Quantitative long-context multimodal evaluations:** measure the model's long-context abilities on both synthetic and real-world tasks with well-defined metrics.
3. **Quantitative core evaluations:** identify progress and regression in core capabilities (e.g., coding, math, science, multilinguality and instruction following).

> ^5 "We note that all the evaluations are from the same checkpoint of the Gemini 1.5 models that are instruction tuned post pre-training, unless otherwise stated. All sampling evals throughout the report are done with temperature 0 (greedy decoding)." [p. 7]

## 5.1. Qualitative Examples of Multimodal Long-Context Capabilities

[p. 7] The ability to process multiple millions of tokens unlocks practical applications that were not possible before. This section demonstrates surprising interactions observed with Gemini 1.5 Pro across code, text and video.^6

> ^6 "For additional short videos of demonstrations of the long context abilities of Gemini 1.5 Pro across video, text, and code see https://deepmind.google/technologies/gemini/." [p. 7]

**Figure 3** (p. 8): "Given the entire 746,152 token JAX codebase in context, Gemini 1.5 Pro can identify the specific location of a core automatic differentiation method."
- Shows a user prompt asking about the backward pass for autodifferentiation in JAX
- The model correctly identifies the file `jax/_src/interpreters/ad.py` and provides the relevant code for the `backward_pass` function
- Input: JAX Core Codebase, 746,152 tokens, 116 total files

**Figure 4** (p. 8): "Given a reference grammar book and a bilingual wordlist (dictionary), Gemini 1.5 Pro is able to translate from English to Kalamang with similar quality to a human who learned from the same materials."
- Shows the model given a grammar book and dictionary as long context (250K tokens)
- User prompt: translate "I'm getting pandanus, I want to make a mat" from English to Kalamang
- Model output: "An padanual repte, irar paruotkin."

**Figure 5** (p. 8): "With the entire text of Les Miserables in the prompt (1382 pages, 732k tokens), Gemini 1.5 Pro is able to identify and locate a famous scene from a hand-drawn sketch."
- Shows the model given the parsed PDF of Les Miserables (1382 pages, 732,162 tokens)
- User prompt: "Look at the event in this drawing. What page is this on?" with a hand-drawn sketch of candlesticks
- Model correctly identifies this as page 119, quoting the passage about the Bishop giving candlesticks to Jean Valjean

**Figure 6** (p. 9): "When prompted with a 45 minute Buster Keaton movie 'Sherlock Jr.' (1924) (2,674 frames at 1FPS, 684k tokens), Gemini 1.5 Pro retrieves and extracts textual information from a specific frame in and provides the corresponding timestamp. At bottom right, the model identifies a scene in the movie from a hand-drawn sketch."
- Shows the model processing the full movie "Sherlock Jr." (1924), directed by Buster Keaton, 44:33 mins, 684K tokens
- First query asks for key information from a piece of paper removed from a person's pocket and the timecode. Model identifies it as a pawn ticket from I. Goldman + Co. Pawn Brokers at 800 Main St., dated 10/23/1924, for a watch and chain pawned for $4.00 by Will Smith, at timecode 12:01. Output validated against the actual frame.
- Second query asks for the timecode of another event. Model responds "This happens at timecode 15:27." Output validated against the actual frame.
- Additionally, the model identifies a scene from a hand-drawn sketch.

[p. 7–8] Specific capabilities demonstrated:
- Gemini 1.5 Pro is able to ingest entire large codebases such as JAX (746,152 tokens) and answer very specific queries about them (Figure 3)
- In Figure 4, Gemini 1.5 Pro's ability to learn a new language based only on reference materials given in its input is shown (see Section 5.2.2.1 for quantitative metrics for this use case)
- Gemini 1.5 Pro can answer an image query given the entire text of Les Miserables and, being natively multimodal, locate a famous scene from a hand-drawn sketch (Figure 5)
- Gemini 1.5 Pro can answer questions about an entire movie of 45 minutes, retrieving moments and timestamps down to a second (Figure 6)
