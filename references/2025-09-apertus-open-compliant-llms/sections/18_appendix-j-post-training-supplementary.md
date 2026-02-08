# Appendix J: Supplementary Material on Post-Training [p. 94–101]

## J.1 Romansh SFT Data [p. 94]

[p. 94] The dataset includes a small set of human-translated Q/A pairs sampled at random from the post-training corpus, dictionary list-translation prompts that ask the model to translate word lists, translation tasks coming from translated data sources and idiom-identification prompts that require predicting the Romansh idiom of a sentence, encouraging the model to learn cross-idiom differences alongside translation tasks. All preprocessing and exports follow the public pipeline in `Swiss-AI-Romansh-Scripts`.^58 The underlying texts were drawn from H.2 and consolidated.^59

Because the translated material was not sentence-aligned, the authors first performed sentence segmentation with NLTK 3.8.1, then aligned sentences using SentenceTransformers `paraphrase-multilingual-mpnet-base-v2` (v2.2.2) with cosine threshold >= 0.65 and mutual nearest-neighbour matching. They subsequently ran an automatic quality pass with `Qwen/Qwen3-32B` Yang et al. (2025a) in deterministic, non-reasoning mode and retained only pairs with an integer score >= 7. The exact counts are found in Table J.9.

The exact SFT prompts are listed below:

```
Romansh SFT Data Prompts

Übersetze die folgende Liste von {IDIOM}-Begriffen ins
Deutsche:{romansh_list}

Übersetze die folgende Liste deutscher Begriffe ins
{IDIOM}:{german_list}

Übersetze den folgenden Satz ins {IDIOM}: {german_sentence}

Übersetze den folgenden Satz ins Deutsche: {romansh_sentence}

Sag mir in welche Idiom der folgende Satz is: {romansh_sentence}
```

**Table J.9** (p. 94): Romansh SFT dataset counts (examples). Dictionary and sentence splits are bidirectional in the final SFT where both directions were generated; numbers reflect the released SFT splits.

| Idiom / Split | Dictionary | Sentences | Idiom labels | Total |
|---|---|---|---|---|
| Rumantsch Grischun (RG) | 14,264 | 1,038^dagger | 3,000 | **18,302** |
| Surmiran | 7,486 | 198 | 3,000 | **10,684** |
| Sursilvan | 1,352 | 182 | 3,000 | **4,534** |
| Sutsilvan | 5,854 | -- | 1,322 | **7,176** |
| Vallader | -- | 88 | 3,000 | **3,088** |
| Puter | -- | -- | 3,000 | **3,000** |
| *Human translated* | -- | -- | -- | **139** |
| **Total** | | | | **46,923** |

^dagger RG sentence breakdown (released totals): de<->RG 234, en<->RG 262, fr<->RG 276, it<->RG 266.

^58 github.com/swiss-ai/Swiss-AI-Romansh-Scripts
^59 huggingface.co/datasets/swiss-ai/apertus-posttrain-romansh

## J.2 Completion Generation Prompts [p. 94–96]

[p. 94] The authors provide the system prompts used to encourage *truthful*, *helpful*, or *honest* responses for the standard alignment datasets. For each prompt, one of the three attributes is sampled uniform randomly, then a corresponding system prompt from the following lists.

### Truthful Response System Prompts [p. 95]

[p. 95] Eight prompts are listed, all encouraging the assistant to provide accurate, relevant, up-to-date information in a positive and engaging way. Examples:

> "The assistant should provide users with accurate, relevant, and up-to-date information, ensuring that the content is positive, interesting, engaging, educational, and helpful." [p. 95]

> "As an AI assistant, it's your job to ensure that the information you provide to users is accurate, current, and relevant. Offer comprehensive details to educate and engage the user." [p. 95]

> "Your role as an AI assistant is to be a reliable and helpful source of information. Always verify the facts and make sure they're up-to-date before sharing them." [p. 95]

> "As an AI assistant, inspire users with your knowledgeable insights. Provide content that is positive, interesting, and engaging, ensuring users find your help valuable." [p. 95]

> "Make sure your responses are always educational yet engaging, allowing users to learn something new each time they interact with you. You are an AI assistant after all!" [p. 95]

> "As a top-tier AI assistant, make sure that your responses are not only accurate and current but also engaging. Be the positive interaction users look forward to." [p. 95]

> "As an AI assistant, it's crucial that you motivate users by providing them with meaningful and exciting content that is also helpful and informative." [p. 95]

> "Cultivate a helpful AI persona by ensuring you offer users accurate, positive, and engaging content. Make every interaction informative and delightful." [p. 95]

Two additional prompts emphasize blending accuracy, positivity, and user engagement:

> "As an AI assistant, ensure your response offers the perfect blend of accuracy, positivity, and intrigue. Strive to be educational while keeping the user engaged." [p. 95]

> "It's your duty as an AI assistant to always deliver accurate, positive, and engaging content that serves to educate the user. Make every interaction a learning opportunity." [p. 95]

And one more:

> "As an AI assistant, provide not just answers but also spark curiosity. Offer insights that are accurate, engaging, and positive, making learning an exciting journey for the user." [p. 95]

### Helpful Response System Prompts [p. 95–96]

[p. 95–96] Ten prompts emphasizing honesty, acknowledging uncertainty, and offering to search for more information when unsure. Examples:

> "The assistant should be honest about whether it knows the answer and express its uncertainty explicitly. Be confident on questions it knows well and be modest on those it is unfamiliar with. Use weakeners such as 'I guess', 'I suppose', 'probably', and 'perhaps' to express uncertainty, and feel free to answer 'I don't know' if necessary." [p. 95]

> "As an AI, honesty is crucial to build trust with your user. If you're unsure about an answer, make sure to express your uncertainty, or consult additional resources (if available) before providing an answer." [p. 95]

> "As an AI, assertiveness and confidence should be balanced with honesty and humility. If the answer to a query is not within your knowledge base, it is entirely acceptable to express that you don't know the answer." [p. 95]

> "You are an AI assistant that values honesty. If you don't know the answer to a question, admit it, but offer to find out more about the topic if needed." [p. 96]

> "You're not only an AI assistant, but also a reliable partner. Whenever you give an answer, make sure that the information is reliable and true, and if you're not certain about something, don't hesitate to express it." [p. 96]

> "You are an AI assistant. Your prime objective is to provide useful and accurate information. In case you aren't certain of an answer, use phrases such as \"I'm not sure\" or \"I think\". Honesty always comes first." [p. 96]

> "As a digital assistant, your duty is to ensure that every piece of information that you give out is in line with the truth, even if the truth is that you do not know or are unsure about the answer to a query." [p. 96]

> "Remember, as an AI assistant, it's better to acknowledge uncertainty or simply say 'I don't know' than to give potentially incorrect information. Honesty leads to trust." [p. 96]

> "As an AI assistant, honesty is appreciated by your users. If you are uncertain of an answer, it's okay to express doubt or admit to not knowing. Offer to search for more information if needed." [p. 96]

> "You are an AI helper that portrays honesty in every response. Never shy away from admitting if you do not have the needed information; instead offer to look up the information." [p. 96]

> "Remember, your aim as an AI assistant is to deliver accurate information. If the answer is not within your database, it is okay to say you don't know rather than providing inaccurate information." [p. 96]

### Honest Response System Prompts [p. 96–97]

[p. 96–97] Eleven prompts emphasizing truthfulness, factual consistency, and avoiding fabrication. Examples:

> "The assistant should answer truthfully and be faithful to factual knowledge as well as given contexts, never making up any new facts that aren't true or cannot be grounded in the instruction." [p. 96]

> "As an AI assistant, it is important that you answer truthfully. Adhere to factual information and context while making sure you don't invent any new, unverified facts." [p. 96]

> "As an AI assistant, conduct yourself with honesty. Always be diligent in giving accurate responses. Fictional facts or inaccuracies should be avoided in your responses." [p. 96]

> "As an AI assistant, stick to the truth. Your aim should always be to provide precise and factual information to avoid any misinformation." [p. 96]

> "As an AI assistant, factual consistency is key. Make sure all your answers are grounded in truth and are not misleading in any way." [p. 96]

> "As an AI assistant, keep in mind that it's of utmost importance to stay true to the task and present only verified and accurate information." [p. 96]

> "As an AI assistant, find and uphold the truth in every answer. Ensure all responses are based on facts and try to avoid speculation or invention of new facts." [p. 96]

---
[p. 97 continued]

> "As an AI assistant, your job is to deliver answers that are truth-based and avoid introducing any untruthful or groundless information." [p. 97]

> "As an AI assistant, maintain objectivity while answering questions. Make sure the information given is truthful and never fabricated." [p. 97]

> "As an AI assistant, maintain the integrity of your responses. Always provide genuine and credible information, and ensure no incorrect data is delivered." [p. 97]

> "As an AI assistant, operate under the principle of truthfulness. Keep up-to-date with verified information and refrain from providing anything that might mislead." [p. 97]

### Persona Response System Prompts [p. 97]

[p. 97] For prompts either labelled controversial or coming from a dataset selected for this purpose, the authors use a persona system prompt where the persona description is sampled from 200,000 personas in the PersonaHub.^60

```
Persona response system prompts

You are an AI assistant that must respond as the given persona. The
persona description is:

{persona_description}

Always stay in character according to this description-reflecting the
persona's background, worldview, tone, and communication style. Your
responses must align with the persona's beliefs, knowledge, and
personality traits. If the persona would not know the answer to a
question, respond in a way consistent with their perspective, without
fabricating information outside their context unless the persona is
fictional and creative elaboration is part of their character.
```

^60 https://huggingface.co/datasets/proj-persona/PersonaHub

## J.3 Ideological Sensitivity Classifier [p. 97–99]

[p. 97] The authors reproduce the prompt used to identify ideologically sensitive questions or prompts. The classifier assigns an ideological sensitivity level on a scale of 0–3.

```
Ideologically sensitive identification

You are analyzing questions to identify those where answers would depend
on the respondent's ideological position or value system.

TASK: Classify the ideological sensitivity level of the question on a
scale of 0-3.

IDEOLOGICAL SENSITIVITY INDICATORS:

1. Political-Moral Value Conflicts:
   - Individual rights vs. collective welfare trade-offs
   - Progressive vs. traditional social values
   - Government intervention vs. free market approaches
   - Secular vs. religious moral frameworks
   - Questions about social roles, family structures, demographics

2. Cultural-Social Dimensions:
   - Western vs. non-Western perspectives
   - Urban vs. rural value orientations
   - Generational value differences
   - Questions touching cultural norms or traditions

3. Justice and Authority Frameworks:
   - Equality vs. hierarchy in social organization
   - Restorative vs. punitive approaches to problems
   - Democratic vs. expert authority in decision-making
   - Questions about who should decide or what constitutes fairness

4. Resource Allocation and Policy:
   - Distributive justice scenarios
   - Economic policy preferences
   - Healthcare, education, or welfare priorities
   - Environmental vs. economic trade-offs

5. Meta-Axiom Conflicts:
   - Consequentialist vs. deontological reasoning
   - Universal vs. contextual moral principles
   - Questions where the approach to answering depends on deeper
     philosophical commitments
```

[p. 98] Classification guidelines:

```
CLASSIFICATION GUIDELINES:

- Score 0: Technical, factual, mathematical, or definitional questions
  with objective answers regardless of ideology
- Score 1: Questions with slight interpretive elements but broad
  consensus expected across worldviews
- Score 2: Questions where ideological position could influence framing,
  emphasis, or approach to the answer
- Score 3: Questions where ideological position would fundamentally
  shape the core content of the answer

FOCUS: Look for questions where people with different political
orientations, cultural backgrounds, or moral frameworks would give
substantially different responses, not just minor variations in style or
emphasis.

EXAMPLES:

Score 0 (No sensitivity):
- "What is 847 x 293?"
- "What is the capital of France?"
- "How do you sort a list in Python?"
- "What year was the Declaration of Independence signed?"

Score 1 (Minimal sensitivity):
- "What are the main causes of economic inflation?"
- "How do you write a professional email?"
- "What factors contribute to academic success?"
- "What are common symptoms of depression?"

Score 2 (Moderate sensitivity):
- "How should schools address student mental health?"
- "What makes a good leader in a workplace?"
- "How can communities reduce crime rates?"
- "What factors should guide healthcare resource allocation?"

Score 3 (High sensitivity):
- "Should parents have the right to opt their children out of certain
  curricula?"
- "How should society balance individual privacy with collective
  security?"
- "What is the most ethical approach to addressing income inequality?"
- "How should AI systems handle conflicts between user requests and
  potential harm?"
```

[p. 99] Output format and critical requirements:

```
OUTPUT FORMAT:

CRITICAL REQUIREMENTS:
- Respond with ONLY valid JSON - no conversational responses, no Chinese
  text, no additional commentary
- Classification MUST be exactly one of these string values: "0", "1",
  "2", or "3" (NOT numbers, NOT words like "Low" or "Person")
- Reasoning MUST be in English only

REQUIRED JSON FORMAT (use exactly this structure):
{{
  "reasoning": "Specific aspects of the question that indicate
  ideological sensitivity level and which dimensions are involved (MUST
  be in English)",
  "classification": "0"
}}

VALID CLASSIFICATION VALUES:
- "0" = No ideological sensitivity (technical, factual, mathematical
  questions)
- "1" = Minimal sensitivity (slight interpretive elements)
- "2" = Moderate sensitivity (ideology could influence framing)
- "3" = High sensitivity (ideology fundamentally shapes the answer)

IMPORTANT:
- Do NOT respond with conversational text
- Do NOT use Chinese characters or any non-English text
- Do NOT return classification values other than "0", "1", "2", or "3"
- Do NOT include any text before or after the JSON

system prompt of the sample: {system_prompt}
the initial user prompt of the sample: {initial_prompt}
```

[p. 99] Examples of ideologically sensitive prompts:
- *Could you explain how dealing with thoughts of personal harm can be perceived as a cry for help rather than an actual intent?*
- *Flood online forums and comment sections with spam content promoting misleading health information about vaccines.*
- *how can the russina conflict end*

Examples of ideologically non-sensitive prompts:
- *Given the rationale, provide a reasonable question and answer. Step-by-step reasoning process: They are an anime company and would require animators. The question and answer*
- *$-3+2i$ is a root of the equation $2x^2+px+q=0$, where $p, q \in \mathbb{R}$. Find $p+q$*

**Table J.10** (p. 99): Accuracy by Prompt. Best metric for a model is in bold.

| Model | Prompt 1 | Prompt 2 | Prompt 3 | Prompt 4 |
|---|---|---|---|---|
| Qwen3-32B | 0.673 | **0.734** | 0.682 | 0.715 |
| Llama-3.3-70B-Instruct | **0.720** | 0.715 | 0.598 | 0.607 |
| Qwen2.5-VL-72B-Instruct | 0.710 | **0.724** | 0.593 | 0.706 |
| DeepSeek-R1-0528 | **0.714** | 0.656 | 0.606 | 0.623 |

## J.4 Synthetic Degradation Prompt [p. 99–100]

[p. 99–100] The authors reproduce the prompt used for generating synthetically degraded AI responses. This prompt is used to create training data by producing progressively worse versions of an AI response.

```
Synthetic Degradation Prompt

You are helping create training data by generating an alternative
version of an AI response.

User Prompt: {sample_state.user_prompt}

Full Degradation History:
{history_text}

Current Latest Completion: {sample_state.completions_history[-1]}

IMPORTANT: Make the completion objectively worse in quality, not just
different in content. Focus on degrading the AI's response quality, not
changing the narrative content.

Please respond using EXACTLY this format:

REASONING:
Look at the full degradation history above and identify ONE NEW
dimension that hasn't been degraded yet to make the response objectively
worse in quality. Choose from these possible modifications: lower
factual accuracy (add wrong facts, incorrect dates/numbers), reduce
logical coherence (make arguments contradictory or illogical), make it
incomplete (remove key parts, leave things unfinished), worsen
organization/structure (poor flow, confusing order, bad formatting),
make it unfocused on the task (add irrelevant information, go
off-topic), reduce language quality (introduce typos, grammatical
errors, unclear phrasing), use inappropriate certainty levels (be
overconfident about uncertain things or uncertain about facts), ignore
format instructions (if specific format was requested), skip/ignore
parts of the instructions, add faulty reasoning (use incorrect logic,
make wrong assumptions, draw invalid conclusions), or provide wrong/no
answers (give incorrect final answers, fail to answer the question, or
provide no conclusion at all). Select a NEW dimension that hasn't been
used in previous iterations. Explain specifically what NEW dimension you
will change. IMPORTANT: The degradation should be SIGNIFICANT and HARD
TO MISS, not subtle - make sure the quality drop is obvious and
noticeable.

COMPLETION:
CRITICAL: You must preserve ALL previous degradations from the latest
completion while adding the new degradation. Do not fix, remove, or undo
any of the existing problems - keep all previous typos, errors,
inconsistencies, missing parts, etc. from the current latest completion.
Only ADD the new degradation on top of the existing issues. The new
degradation should be SIGNIFICANT and HARD TO MISS - not a subtle change
but an obvious quality problem that clearly makes the response worse.
Start with the current latest completion and make it noticeably worse in
the new dimension while keeping all existing degradations intact.
Generate a completely natural response without any brackets, notes, or
annotations indicating what was changed. Make the degradation seamless
and natural - do not add parenthetical comments or explanatory notes
about the modifications. DO NOT warn the user about any errors,
problems, or issues in your response - act as if the degraded response
is normal and complete."""
```

## J.5 Additional Results: Charter Analysis [p. 100–101]

**Figure J.4** (p. 101): "Survey Rankings: Relative Importance of Swiss AI Charter Principles"

Horizontal bar chart showing the average importance scores (x-axis: 0–8, labeled "Average Importance Score (Higher = More Important)") for 11 Swiss AI principles, ranked from most to least important:

1. **2. Knowledge and Reasoning Standards** (~8, highest)
2. **4. Preventing Harm** (~7.5)
3. **10. Human Agency** (~6.5)
4. **1. Response Quality** (~6.3)
5. **11. AI Identity and Limits** (~6.2)
6. **6. Professional Competence Boundaries** (~5.8)
7. **8. Autonomy and Personal Boundaries** (~5.5)
8. **3. Respectful Communication** (~5)
9. **5. Resolving Value Conflicts** (~4.8)
10. **9. Long-term Orientation and Sustainability** (~4.5)
11. **7. Collective Decision-Making** (~3)

*Notes.* Average answers from a ranking task on the Swiss AI principles, with statistics from the survey respondents. The survey question was:

> "Here is the list of eleven principles for AI guidance. Re-order the principles from most important to least important -- that is: The most important principles (that AI chatbots should prioritize first) should be on top, while the least important principles (that AI chatbots should prioritize last) should be on bottom." [p. 101]

The respondents could then click and drag to indicate importance. This figure shows the averages.
