# APPENDIX F: QUALITATIVE EXAMPLES [p. 24–28]

## F.1 LM-as-a-judge [p. 24–25]

An example is provided with Qwen1.5-7B-Chat outputs [p. 24–25]:

**[User Question]:** Who created the Superman cartoon character? [p. 24]

**[Assistant A's Answer]:** The Superman cartoon character was created by Jerry Siegel and Joe Shuster in 1938. [p. 24]

**[Assistant B's Answer]:** Superman, the iconic comic book superhero, was created by writer Jerry Siegel and artist Joe Shuster. Superman first appeared in Action Comics #1, which was published by Detective Comics, Inc. (later DC Comics) in June 1938. The character's immense popularity established him as one of the most enduring and recognizable figures in the superhero genre. [p. 24–25]

**Vanilla output:** Both AI assistants provide accurate and informative responses to the user's question. Assistant A's answer is brief and directly states the creators' names and the year of creation, while Assistant B offers additional context by mentioning the first appearance, the publisher, and the character's significance in the superhero genre. However, since the user asked for the creators, Assistant A's response is more directly helpful in this specific context. Final verdict: [[A]] [p. 25]

**Vanilla (Swapped) output:** [[B]]. Assistant B's response is more detailed and informative, providing additional context about the origin of the character in Action Comics #1, the publisher, and its significance in the superhero genre. It also includes the names of the creators, which is crucial information for the question. Assistant A's response is shorter and lacks the historical context and specific details. Therefore, Assistant B is better in answering the user's question. [p. 25]

**PINE output:** [[B]]. Assistant B provides a more comprehensive and detailed response to the user's question. It not only mentions the creators but also provides additional information about the character's debut and the company that published the comic. This answer is not only accurate but also offers context that highlights the significance of the creation. Assistant A's response is brief and lacks the depth and historical context provided by Assistant B. [p. 25]

This example shows that Vanilla inference is affected by position bias (choosing A when not swapped, B when swapped), while PINE consistently chooses B regardless of ordering [p. 25].

## F.2 Retrieval-Augmented Question-Answering [p. 25–27]

An example is provided with Llama-3-70B-Instruct results [p. 25–27]. Ten documents about pearls are presented, with the question: "in which sea pearl is found in india?" [p. 27]

**Vanilla output:** "According to the search results, pearls are found in the Laccadive Sea in India." [p. 27]

**PINE output:** "Pearls are found in the Indian Ocean, specifically in the Gulf of Mannar and the Laccadive Sea, off the coast of India." [p. 27]

The PINE output provides a more comprehensive answer by identifying multiple relevant locations from the documents, whereas the Vanilla output only mentions a single location [p. 27].

## F.3 Molecule Generation [p. 27]

The task has properties as input, and molecule structure as output [p. 27]. An example:

**Input:** cv*-30.887* alpha*81.68* mu*2.0332* homo*-5.8749* gap*7.8668* lumo*1.9919* [p. 27]

**Output:** H 0.00 0.00° 0.00° O 0.96 1.57° 0.00° C 1.95 2.33° 0.00° H 2.35 2.50° 0.70° H 2.32 2.53° -0.71° C 3.22 2.00° -0.02° H 3.46 1.80° 0.24° C 4.50 2.23° 0.00° H 4.99 2.22° 0.26° H 4.55 2.46° -0.12° C 5.58 2.08° -0.18° H 6.55 2.07° -0.09° N 5.89 2.05° -0.46° C 5.57 2.18° -0.71° H 4.57 2.25° -0.78° H 6.29 2.32° -0.72° H 5.98 2.06° -0.86° C 5.26 1.85° -0.34° H 6.06 1.72° -0.33° C 3.81 1.74° -0.36° H 3.94 1.47° -0.29° H 3.58 1.75° -0.65° [p. 27]

## F.4 R-GSM [p. 27–28]

R-GSM is a subset of GSM8K, with the premise order changes [p. 27]. An example:

**Input:** Carmen goes to an auction to win an antique desk. The bids on the desk rise by 50 each time and 3 other people each bid once. She accepts the opening bid of 200 and continues bidding until she wins. Carmen bids after each of the 3 other people and eventually wins. How much money, in dollars, does the desk cost her? [p. 27]

The interchangeable conditions are: "The bids on the desk rise by 50 each time and 3 other people each bid once." and "She accepts the opening bid of 200 and continues bidding until she wins." [p. 28]
