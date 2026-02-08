# 3.9.6 Correcting English Grammar [p. 29]

[p. 29] Another task well suited for few-shot learning is correcting English grammar. GPT-3 is tested in the few-shot setting by giving prompts of the form "Poor English Input: <sentence>\n Good English Output: <sentence>". GPT-3 is given one human-generated correction and then asked to correct 5 more (again without any omissions or repeats). Results are shown in Figure 3.17.

## Figures

**Figure 3.17** (p. 30): "Representative GPT-3 completions for the few-shot task of correcting English grammar. Boldface is GPT-3's completions, plain text is human prompts. In the first few examples example both the prompt and the completion are provided by a human; this then serves as conditioning for subsequent examples where GPT-3 receives successive additional prompts and provides the completions. Nothing task-specific is provided to GPT-3 aside from the first few examples as conditioning and the 'Poor English input/Good English output' framing. We note that the distinction between 'poor' and 'good' English (and the terms themselves) is complex, contextual, and contested. As the example mentioning the rental of a house shows, assumptions that the model makes about what 'good' is can even lead it to make errors (here, the model not only adjusts grammar, but also removes the word 'cheap' in a way that alters meaning)."
- Shows multiple pairs of "Poor English input" / "Good English output":
  - Human-provided conditioning examples:
    - "I eated the purple berries." -> "I ate the purple berries."
    - "Thank you for picking me as your designer. I'd appreciate it." -> "Thank you for choosing me as your designer. I appreciate it."
    - "The mentioned changes have done. or I did the alteration that you requested. or I changed things you wanted and did the modifications." -> "The requested changes have been made. or I made the alteration that you requested. or I changed things you wanted and made the modifications."
    - "I'd be more than happy to work with you in another project." -> **"I'd be more than happy to work with you on another project."**
  - GPT-3 generated corrections:
    - "Please provide me with a short brief of the design you're looking for and that'd be nice if you could share some examples or project you did before." -> **"Please provide me with a brief description of the design you're looking for and that would be nice if you could share some examples or projects you have done before."**
    - "The patient was died." -> **"The patient died."**
    - "We think that Leslie likes ourselves." -> **"We think that Leslie likes us."**
    - "Janet broke Bill on the finger." -> **"Janet broke Bill's finger."**
    - "Mary arranged for, in St. Louis, John to rent a house cheap." -> **"Mary arranged for John to rent a house in St. Louis."** (Note: removes "cheap", altering meaning)
    - "Today I have went to the store to to buys some many bottle of water." -> **"Today I went to the store to buy some bottles of water."**
    - "I have tried to hit ball with bat, but my swing is has miss." -> **"I tried to hit the ball with the bat, but my swing missed."**
- The figure demonstrates GPT-3's ability to correct grammatical errors in a few-shot setting, but also reveals that the model sometimes makes semantic changes beyond pure grammar correction (e.g., removing "cheap" from the house rental example).
