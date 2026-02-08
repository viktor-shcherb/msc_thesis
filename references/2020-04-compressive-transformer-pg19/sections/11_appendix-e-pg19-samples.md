# Appendix E: PG-19 Samples [p. 16–19]

[p. 16] The authors show a few different samples from the Compressive Transformer trained on PG-19. They use Nucleus Sampling with p = 0.98 (Holtzman et al., 2019). They choose extracts of books from the test set as prefixes. The model is able to continue in the style of the text, creating artificial dialogue or descriptive text, and remembering the names of characters over hundreds of words.

As the Compressive Transformer is trained without state resetting, it is actually slightly out of sample when provided with the (relatively) short contexts. This is because its memory and compressed memory may be still empty (whereas they are always full during training). However there is a trend of the samples usually improving towards the end.

### Sample 1: Baby Mine by Maragaret Mayo [p. 17]

**Context:** Chapter I of "Baby Mine" by Maragaret Mayo, beginning with "Even in college Alfred Hardy was a young man of fixed ideas and high ideals and proud of it." The context introduces Alfred Hardy and his friend Jimmy Jinks and their contrasting temperaments.

**Compressive Transformer continuation:** The model generates an extended narrative continuing in the style of the novel, producing dialogue between Alfred and Jimmy about their friend "Jimmy Jinks" living a single life. The generated text maintains character names, dialogue style, and narrative voice consistent with the original context over many paragraphs.

### Sample 2: The Diary of Samuel Pepys [p. 18]

**Context:** An entry from "The Diary of Samuel Pepys" dated June 1st, written in first-person diary style. The context describes Pepys travelling by water to Woolwich, then to Deptford, dining at a tavern, visiting Redriffe, attending a celebration with cakes, conducting business at the office, and managing financial matters (Lord's imprest of L1000 and Mr. Creed's of L10,000).

**Compressive Transformer continuation:** The model generates text in first-person diary style consistent with Pepys's voice, describing daily activities such as business at the office, dinner, going to Deptford, taking oaths of allegiance, and reflecting on one's situation. The continuation maintains the diarist's characteristic tone and period-appropriate language.

### Sample 3: The Patrol of the Sun Dance Trail by Ralph Connor [p. 19]

**Context:** Opening passage of "The Patrol of the Sun Dance Trail" by Ralph Connor, describing a scene at the headquarters of Superintendent Strong of the North West Mounted Police near the Kicking Horse Pass. A man arrives running along a tote-road and enters a wooden shack.

**Compressive Transformer continuation:** The model generates a lengthy third-person narrative describing members of the Superintendent's Force observing a stranger approaching, with detailed descriptions of the man's appearance and bearing. The text continues with an extended descriptive passage about horses, chariots, and a journey through "the Hollow of the Mountains." The generated text maintains the descriptive, adventure-novel style of the original context.
