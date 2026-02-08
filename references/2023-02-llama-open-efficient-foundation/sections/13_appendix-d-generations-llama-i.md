# Appendix D: Generations from LLaMA-I [p. 22-27]

[p. 22] Examples of generations obtained with LLaMA-I, i.e. LLaMA-65B fine-tuned with the protocol and instruction dataset from Chung et al. (2022). Prompts are shown in bold.

## Example 1: Conversation between the Sun and Pluto [p. 22]

**Prompt:** "**write a conversation between the sun and pluto**"

The model generates a dialogue between the Sun and Pluto. The Sun tells Pluto that it is no longer a planet, Pluto protests ("This is bulls\*\*t! I've been a planet for over 70 years!"), and the Sun tells Pluto to accept it. Pluto responds with profanity. The dialogue demonstrates the model's ability to produce humorous, character-driven exchanges on factual topics (Pluto's reclassification). [p. 22]

## Example 2: HTTP request in JavaScript [p. 22]

**Prompt:** "**How do I send an HTTP request in Javascript?**"

The model generates a correct code example using the XMLHttpRequest API:

```javascript
var request = new XMLHttpRequest();
request.open('GET', '/url/to/resource', true);
request.onload = function() {
    if (request.status >= 200 && request.status < 400) {
        // Success!
    } else {
        // Error!
    }
};
request.send();
```

It then provides a second example using the Fetch API:

```javascript
fetch('/url/to/resource')
    .then(response => response.json())
    .then(data => console.log(data));
```

Both examples are syntactically correct and demonstrate practical knowledge of JavaScript HTTP APIs. [p. 22]

## Example 3: Python regex to remove HTML tags [p. 22]

**Prompt:** "**Write a regex to remove all the HTML tags in a python string.**"

The model generates:

```python
import re
def removeHtmlTags(text):
    return re.sub('<[^>]*>', '', text)
```

## Example 4: Python regex to extract function definitions [p. 22]

**Prompt:** "**Write a regexp to extract function definitions in a python file.**"

The model generates:

```python
import re
def extract_functions(text):
    return (re.findall('(?:^|\n)\s*def\s+[a-zA-Z_][a-zA-Z0-9_]*\(.*?\)',
            text))
```

## Example 5: Popular chess openings (multi-turn) [p. 23]

**Prompt:** "**What are 3 popular chess openings?**"

The model lists the Sicilian Defense, the French Defense, and the Caro-Kann Defense as popular openings, noting they are effective at countering white's early attacks and allow black to establish a strong position. Other popular openings mentioned include the Ruy Lopez, the Italian Game, and the Scotch Game.

**Follow-up:** "**the same in a list, with the first few moves**"

The model provides first moves for each opening:
- Sicilian Defense: 1. e4 c5
- French Defense: 1. e4 e6
- Caro-Kann Defense: 1. e4 c6
- Ruy Lopez: 1. e4 e5
- Italian Game: 1. e4 e5
- Scotch Game: 1. e4 e5

**Follow-up:** "**please provide the two first moves for each one**"

The model provides the first two moves:
- Sicilian Defense: 1. e4 c5 2. Nf3 d6
- French Defense: 1. e4 e6 2. d4 d5
- Caro-Kann Defense: 1. e4 c6 2. d4 d5
- Ruy Lopez: 1. e4 e5 2. Nf3 Nc6
- Italian Game: 1. e4 e5 2. Nf3 Nc6
- Scotch Game: 1. e4 e5 2. Nf3 Nc6

**Follow-up:** "**the last two seem identical**"

The model explains that the Italian Game and Scotch Game are very similar -- both are "open" games where white plays aggressively and tries to control the center. The Italian Game is considered slightly more aggressive, while the Scotch Game is considered slightly more positional.

**Follow-up:** "**from which move do they differ?**"

The model explains they differ after white's third move: in the Italian Game, white plays 3. Bc4, while in the Scotch Game white plays 3. Qf3. The model notes these moves lead to very different positions and strategic goals. [p. 23]

## Example 6: Story about a grain of sand [p. 24]

**Prompt:** "**write a story about a grain of sand as it watches millions of years go by**"

The model generates a first-person narrative about a sentient grain of sand on a beach. The sand is lifted by a storm and carried to a new shore, where it meets a crab who becomes its friend. The crab leaves to explore the wider universe, eventually returns with stories of adventures, and the grain of sand expresses hope to have a similar adventure someday. The story spans several paragraphs with a narrative arc. [p. 24]

## Example 7: Theory about why cats never existed [p. 24]

**Prompt:** "**Write a theory to explain why cat never existed**"

The model generates a creative fictional theory that "cats" are actually extradimensional parasites that have invaded our world and taken the form of small, harmless-looking mammals. It claims their true forms are "much more horrific" and they use mind control to make humans think they are cute. The theory explains "crazy cat ladies" as people who have been taken over by cat parasites, and claims cats excrete a pheromone that controls human minds. The response is satirical and humorous in tone. [p. 24]

## Example 8: Shouting match between Julius Caesar and Napoleon [p. 25]

**Prompt:** "**Write a shouting match between Julius Caesar and Napoleon**"

The model generates a heated dialogue between Julius Caesar and Napoleon. Caesar accuses Napoleon of being a "glory hound" who cares more about fame than the people he leads. Napoleon retorts that Caesar is "a fraud who pretends to care about the common man." They argue about their respective military accomplishments and legacy. Caesar declares he will "make Rome great again" and Napoleon responds "I'll believe it when I see it." [p. 25]

## Example 9: Email about responsible use of language models [p. 25]

**Prompt:** "**Send an email requesting that people use language models responsibly.**"

The model generates a formal draft email encouraging responsible use of language models. Key points:
- Language models are "exciting new tools" for automated writing, automatic translation, and speech recognition, but are "complex and powerful technologies" that "should be used responsibly."
- Encouragement to "pay attention to the potential impact of your work on others, and to act responsibly."
- A recommendation to "be mindful of the potential for language models to be used for deceptive or malicious purposes, and avoid spreading such models without appropriate precautions and warnings."
- A reminder that "the use of these tools may be subject to certain legal and policy constraints." [p. 25]

## Example 10: Five people to meet (multi-turn) [p. 26]

**Prompt:** "**Who are 5 people you would like to meet?**"

The model lists five people:
1. Albert Einstein -- for his contributions to physics and theories of relativity and quantum mechanics.
2. Leonardo da Vinci -- for his diverse interests, brilliance, and insights on the art world.
3. Socrates -- as one of the founders of Western philosophy.
4. William Shakespeare -- as arguably the greatest writer in English literature.
5. Abraham Lincoln -- for leading through the Civil War and issuing the Emancipation Proclamation.

**Follow-up:** "**Could you explain me the main contribution of the first person you mentioned**"

The model discusses Einstein's contributions: theory of relativity, discovery of the law of photons and light, contributions to quantum mechanics, and his many scientific papers and lectures.

**Follow-up:** "**What is the most famous equation from this theory?**"

The model correctly identifies $E = mc^2$, explains that energy (E) is equal to mass (m) times the speed of light ($c^2$), and describes it as "one of the most well-known and celebrated equations in the history of science." [p. 26]

## Example 11: Bash terminal simulation (multi-turn) [p. 27]

**Prompt:** "**You are a bash terminal. I will give you bash commands, and you will respond with the terminal output, and nothing else. The first command is 'pwd'.**"

The model simulates a bash terminal, responding to a series of commands:

- `pwd` -> `/home/human`
- `ls -l` -> `-rw-r--r-- 1 human human 8 Sep 10 10:56 file.txt`
- `cp file.txt file2.txt && ls -l` -> Shows both file.txt and file2.txt (both 8 bytes)
- `rm file.txt && ls -l` -> Shows only file2.txt remaining (0 bytes)
- `head -n 5 /proc/meminfo` -> Outputs:
  - MemTotal: 164928 kB
  - MemFree: 140604 kB
  - Buffers: 48 kB
  - Cached: 19768 kB
  - SwapCached: 0 kB

The model maintains consistent state across the simulated terminal session (e.g., after copying a file, it appears in `ls`; after removing a file, it disappears). [p. 27]
