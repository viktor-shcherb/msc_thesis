# G. Details of Task Phrasing and Specifications [p. 50–61]

[p. 50] The following figures illustrate the formatting and phrasing of all the tasks included in the paper. All data comes from the ground truth datasets in this section, and no samples from GPT-3 are included here.

## Figure G.1

**Figure G.1** (p. 50): "Formatted dataset example for RACE-h. When predicting, we normalize by the unconditional probability of each answer as described in 2."

The figure shows a formatted example for the RACE-h (high school level) reading comprehension task:
- **Context:** An article about informal conversation as an important part of business relationships, covering cultural norms across Latin America, France, the United States, Japan, China, Korea, and the Middle East regarding suitable discussion topics. The article discusses topics like family, hobbies, politics, religion, and salary.
- **Questions and answers presented in sequence:**
  - Q: What shouldn't you do when talking about sports with colleagues from another country? A: Criticizing the sports of your colleagues' country.
  - Q: Which is typically a friendly topic in most places according to the author? A: Sports.
  - Q: Why are people from Asia more private in their conversation with others? A: They don't want to have their good relationship with others harmed by informal conversation.
  - Q: The author considers politics and religion _. A: [blank for model to complete]
- **Answer choices for the final question:**
  - Correct Answer: taboo
  - Incorrect Answer: cheerful topics
  - Incorrect Answer: rude topics
  - Incorrect Answer: topics that can never be talked about

## Figure G.2

**Figure G.2** (p. 51): "Formatted dataset example for ANLI R2"

The figure shows a formatted example for ANLI Round 2 (Adversarial NLI):
- **Context:** "anli 2: anli 2: The Gold Coast Hotel & Casino is a hotel and casino located in Paradise, Nevada. This locals' casino is owned and operated by Boyd Gaming. The Gold Coast is located one mile (~1.6km) west of the Las Vegas Strip on West Flamingo Road. It is located across the street from the Palms Casino Resort and the Rio All Suite Hotel and Casino. Question: The Gold Coast is a budget-friendly casino. True, False, or Neither?"
- **Answer choices:**
  - Correct Answer: Neither
  - Incorrect Answer: True
  - Incorrect Answer: False

## Figure G.3

**Figure G.3** (p. 51): "Formatted dataset example for RACE-m. When predicting, we normalize by the unconditional probability of each answer as described in 2."

The figure shows a formatted example for the RACE-m (middle school level) reading comprehension task:
- **Context:** An article about Mrs. Smith, an unusual teacher who told each student to bring a few potatoes in a plastic bag. On each potato the students had to write the name of a person they hated. The children carried the bags everywhere for two weeks, experiencing the smell and weight. Mrs. Smith used this to teach a lesson about carrying hatred in one's heart.
- **Questions and answers presented in sequence:**
  - Q: Which of the following is True according to the passage? A: If a kid hated four people, he or she had to carry four potatoes.
  - Q: We can learn from the passage that we should _. A: throw away the hatred inside
  - Q: The children complained about _ besides the weight trouble. A: the smell
  - Q: Mrs. Smith asked her students to write _ on the potatoes. A: [blank for model to complete]
- **Answer choices for the final question:**
  - Correct Answer: names
  - Incorrect Answer: numbers
  - Incorrect Answer: time
  - Incorrect Answer: places

---
[p. 52–56 continued]

## Figure G.4

**Figure G.4** (p. 52): "Formatted dataset example for PIQA"

The figure shows a formatted example for PIQA (Physical Intuition QA):
- **Context:** "How to apply sealant to wood."
- **Answer choices:**
  - Correct Answer: "Using a brush, brush on sealant onto wood until it is fully saturated with the sealant."
  - Incorrect Answer: "Using a brush, drip on sealant onto wood until it is fully saturated with the sealant."

## Figure G.5

**Figure G.5** (p. 52): "Formatted dataset example for COPA"

The figure shows a formatted example for COPA (Choice of Plausible Alternatives):
- **Context:** "My body cast a shadow over the grass because"
- **Answer choices:**
  - Correct Answer: "the sun was rising."
  - Incorrect Answer: "the grass was cut."

## Figure G.6

**Figure G.6** (p. 52): "Formatted dataset example for ReCoRD. We consider the context above to be a single 'problem' because this is how the task is presented in the ReCoRD dataset and scored in the ReCoRD evaluation script."

The figure shows a formatted example for ReCoRD (Reading Comprehension with Commonsense Reasoning Dataset):
- **Context:** A CNN article about Yuval Rabin, whose father Yitzhak Rabin was assassinated while serving as Prime Minister of Israel, criticizing Donald Trump for appealing to "Second Amendment people" and warning that politicians' words can incite violence and undermine democracy. Rabin wrote in USAToday about parallels between Israel of the 1990s and the U.S. today. Additional bullet points note that the son of a former Israeli Prime Minister who was assassinated wrote an op ed about violent political rhetoric and warns of "parallels" between Israel of the 1990s and the U.S. today.
- **Answer choices:**
  - Correct Answer: "- Referencing his father, who was shot and killed by an extremist amid political tension in Israel in 1995, Rabin condemned Donald Trump's aggressive rhetoric."
  - Correct Answer: "- Referencing his father, who was shot and killed by an extremist amid political tension in Israel in 1995, Rabin condemned Trump's aggressive rhetoric."
  - Incorrect Answer: "- Referencing his father, who was shot and killed by an extremist amid political tension in Israel in 1995, Rabin condemned Hillary Clinton's aggressive rhetoric."
  - Incorrect Answer: "- Referencing his father, who was shot and killed by an extremist amid political tension in Israel in 1995, Rabin condemned U.S.'s aggressive rhetoric."
  - Incorrect Answer: "- Referencing his father, who was shot and killed by an extremist amid political tension in Israel in 1995, Rabin condemned Yitzhak Rabin's aggressive rhetoric."

## Figure G.7

**Figure G.7** (p. 52): "Formatted dataset example for ANLI R1"

The figure shows a formatted example for ANLI Round 1 (Adversarial NLI):
- **Context:** "anli 1: anli 1: Fulton James MacGregor MSP is a Scottish politician who is a Scottish National Party (SNP) Member of Scottish Parliament for the constituency of Coatbridge and Chryston. MacGregor is currently Parliamentary Liaison Officer to Shona Robison, Cabinet Secretary for Health & Sport. He also serves on the Justice and Education & Skills committees in the Scottish Parliament. Question: Fulton James MacGregor is a Scottish politician who is a Liaison officer to Shona Robison who he swears is his best friend. True, False, or Neither?"
- **Answer choices:**
  - Correct Answer: Neither
  - Incorrect Answer: True
  - Incorrect Answer: False

## Figure G.8

**Figure G.8** (p. 53): "Formatted dataset example for OpenBookQA. When predicting, we normalize by the unconditional probability of each answer as described in 2."

The figure shows a formatted example for OpenBookQA:
- **Context:** "Organisms require energy in order to do what?"
- **Answer choices:**
  - Correct Answer: "mature and develop."
  - Incorrect Answer: "rest soundly."
  - Incorrect Answer: "absorb light."
  - Incorrect Answer: "take in nutrients."

## Figure G.9

**Figure G.9** (p. 53): "Formatted dataset example for HellaSwag"

The figure shows a formatted example for HellaSwag:
- **Context:** "Making a cake: Several cake pops are shown on a display. A woman and girl are shown making the cake pops in a kitchen. They"
- **Answer choices:**
  - Correct Answer: "bake them, then frost and decorate."
  - Incorrect Answer: "taste them as they place them on plates."
  - Incorrect Answer: "put the frosting on the cake as they pan it."
  - Incorrect Answer: "come out and begin decorating the cake as well."

## Figure G.10

**Figure G.10** (p. 53): "Formatted dataset example for ANLI R3"

The figure shows a formatted example for ANLI Round 3 (Adversarial NLI):
- **Context:** "anli 3: anli 3: We shut the loophole which has American workers actually subsidizing the loss of their own job. They just passed an expansion of that loophole in the last few days: $43 billion of giveaways, including favors to the oil and gas industry and the people importing ceiling fans from China. Question: The loophole is now gone True, False, or Neither?"
- **Answer choices:**
  - Correct Answer: False
  - Incorrect Answer: True
  - Incorrect Answer: Neither

## Figure G.11

**Figure G.11** (p. 53): "Formatted dataset example for ARC (Challenge). When predicting, we normalize by the unconditional probability of each answer as described in 2."

The figure shows a formatted example for ARC (Challenge):
- **Context:** "Question: George wants to warm his hands quickly by rubbing them. Which skin surface will produce the most heat? Answer:"
- **Answer choices:**
  - Correct Answer: "dry palms"
  - Incorrect Answer: "wet palms"
  - Incorrect Answer: "palms covered with oil"
  - Incorrect Answer: "palms covered with lotion"

## Figure G.12

**Figure G.12** (p. 53): "Formatted dataset example for SAT Analogies"

The figure shows a formatted example for SAT Analogies:
- **Context:** "lull is to trust as"
- **Answer choices:**
  - Correct Answer: "cajole is to compliance"
  - Incorrect Answer: "balk is to fortitude"
  - Incorrect Answer: "betray is to loyalty"
  - Incorrect Answer: "hinder is to destination"
  - Incorrect Answer: "soothe is to passion"

## Figure G.13

**Figure G.13** (p. 53): "Formatted dataset example for Winograd. The 'partial' evaluation method we use compares the probability of the completion given a correct and incorrect context."

The figure shows a formatted example for Winograd:
- **Correct Context:** "Grace was happy to trade me her sweater for my jacket. She thinks the sweater"
- **Incorrect Context:** "Grace was happy to trade me her sweater for my jacket. She thinks the jacket"
- **Target Completion:** "looks dowdy on her."

## Figure G.14

**Figure G.14** (p. 54): "Formatted dataset example for Winogrande. The 'partial' evaluation method we use compares the probability of the completion given a correct and incorrect context."

The figure shows a formatted example for Winogrande:
- **Correct Context:** "Johnny likes fruits more than vegetables in his new keto diet because the fruits"
- **Incorrect Context:** "Johnny likes fruits more than vegetables in his new keto diet because the vegetables"
- **Target Completion:** "are saccharine."

## Figure G.15

**Figure G.15** (p. 54): "Formatted dataset example for MultiRC. There are three levels within MultiRC: (1) the passage, (2) the questions, and (3) the answers. During evaluation, accuracy is determined at the per-question level, with a question being considered correct if and only if all the answers within the question are labeled correctly. For this reason, we use K to refer to the number of **questions** shown within the context."

The figure shows a formatted example for MultiRC:
- **Context:** A long reading comprehension passage (titled "READING COMPREHENSION ANSWER KEY") about U.S. diplomacy with Pakistan and the Taliban, covering events from early 2000 including Karl Inderfurth and Michael Sheehan meeting with General Musharraf in Islamabad, President Clinton's one-day stopover in Pakistan on March 25, 2000 (the first time a U.S. president had been there since 1969), and discussions about tensions between Pakistan and India, nuclear proliferation, and Bin Laden. The passage ends with the question: "Who did The State Department feel should visit both India and Pakistan?"
- **Answer choices:**
  - Correct Answer: "- [False] Bin Laden"
  - Incorrect Answer: "- [True] Bin Laden"

## Figure G.16

**Figure G.16** (p. 54): "Formatted dataset example for ARC (Easy). When predicting, we normalize by the unconditional probability of each answer as described in 2."

The figure shows a formatted example for ARC (Easy):
- **Context:** "Question: Which factor will most likely cause a person to develop a fever? Answer:"
- **Answer choices:**
  - Correct Answer: "a bacterial population in the bloodstream"
  - Incorrect Answer: "a leg muscle relaxing after exercise"
  - Incorrect Answer: "several viral particles on the skin"
  - Incorrect Answer: "carbohydrates being digested in the stomach"

## Figure G.17

**Figure G.17** (p. 55): "Formatted dataset example for StoryCloze"

The figure shows a formatted example for StoryCloze:
- **Context:** "Bob went to the gas station to fill up his car. His tank was completely empty and so was his wallet. The cashier offered to pay for his gas if he came back later to pay. Bob felt grateful as he drove home."
- **Answer choices:**
  - Correct Answer: "Bob believed that there were good people in the world."
  - Incorrect Answer: "Bob contemplated how unfriendly the world was."

## Figure G.18

**Figure G.18** (p. 55): "Formatted dataset example for CoQA"

The figure shows a formatted example for CoQA (Conversational Question Answering):
- **Context:** A passage about Helsinki, the capital and largest city of Finland, located in the region of Uusimaa in southern Finland. The passage covers Helsinki's population (metropolitan population of over 1.4 million), its location relative to Tallinn, Stockholm, and St. Petersburg, and the Helsinki metropolitan area including Helsinki, Espoo, Vantaa, Kauniainen, and surrounding commuter towns. It notes Helsinki is the world's northernmost metro area of over one million people and the northernmost capital of an EU member state. Approximately 75% of foreign companies operating in Finland have settled in the Helsinki region.
- **Questions and answers presented as a multi-turn conversation:**
  - Q: what is the most populous municipality in Finland? A: Helsinki
  - Q: how many people live there? A: 1.4 million in the metropolitan area
  - Q: what percent of the foreign companies that operate in Finland are in Helsinki? A: 75%
  - Q: what towns are a part of the metropolitan area? A: [blank for model to complete]
- **Target Completion:** "Helsinki, Espoo, Vantaa, Kauniainen, and surrounding commuter towns"

## Figure G.19

**Figure G.19** (p. 55): "Formatted dataset example for Cycled Letters"

The figure shows a formatted example for Cycled Letters (word unscrambling):
- **Context:** "Please unscramble the letters into a word, and write that word: asinoc ="
- **Target Completion:** "casino"

## Figure G.20

**Figure G.20** (p. 56): "Formatted dataset example for DROP"

The figure shows a formatted example for DROP (Discrete Reasoning Over Paragraphs):
- **Context:** A passage about Saint Jean de Brébeuf, a French Jesuit missionary who travelled to New France in 1625, worked primarily with the Huron, spent time in France from 1629 to 1633, learned the Huron language and culture, and was captured and ritually tortured and killed on March 16, 1649 during an Iroquois raid. Brébeuf was beatified in 1925 and canonized as a saint in 1930. The question asks: "How many years did Saint Jean de Brébeuf stay in New France before he went back to France for a few years? Answer:"
- **Target Completion:** "4"

## Figure G.21

**Figure G.21** (p. 56): "Formatted dataset example for LAMBADA"

The figure shows a formatted example for LAMBADA:
- **Context:** A fill-in-the-blank passage: "She held the torch in front of her. She caught her breath. 'Chris? There's a step.' 'What?' 'A step. Cut in the rock. About fifty feet ahead.' She moved faster. They both moved faster. 'In fact,' she said, raising the torch higher, 'there's more than a ____. ->"
- **Target Completion:** "step"

## Figure G.22

**Figure G.22** (p. 56): "Formatted dataset example for Anagrams 1 (A1)"

The figure shows a formatted example for Anagrams 1 (word unscrambling):
- **Context:** "Please unscramble the letters into a word, and write that word: skicts ="
- **Target Completion:** "sticks"

## Figure G.23

**Figure G.23** (p. 56): "Formatted dataset example for Anagrams 2"

The figure shows a formatted example for Anagrams 2 (word unscrambling):
- **Context:** "Please unscramble the letters into a word, and write that word: volwskagen ="
- **Target Completion:** "volkswagen"

## Figure G.24

**Figure G.24** (p. 56): "Formatted dataset example for Natural Questions"

The figure shows a formatted example for Natural Questions:
- **Context:** "Q: Who played tess on touched by an angel? A:"
- **Target Completion:** "Delloreese Patricia Early (July 6, 1931 { November 19, 2017), known professionally as Della Reese"

---
[p. 57–61 continued]

## Figure G.25

**Figure G.25** (p. 57): "Formatted dataset example for QuAC"

The figure shows a formatted example for QuAC (Question Answering in Context):
- **Context:** "TITLE: William Perry (American football) -- Professional career PARAGRAPH: In 1985, he was selected in the first round of the 1985 NFL Draft by the Chicago Bears; he had been hand-picked by coach Mike Ditka. However, defensive coordinator Buddy Ryan, who had a highly acrimonious relationship with Ditka, called Perry a 'wasted draft-pick'. Perry soon became a pawn in the political power struggle between Ditka and Ryan. Perry's 'Refrigerator' nickname followed him into the NFL and he quickly became a favorite of the Chicago Bears fans. Teammates called him 'Biscuit,' as in 'one biscuit shy of 350 pounds.' While Ryan refused to play Perry, Ditka decided to use Perry as a fullback when the team was near the opponents' goal line or in fourth and short situations, either as a ball carrier or a lead blocker for star running back Walter Payton. Ditka stated the inspiration for using Perry as a fullback came to him during five-yard sprint exercises. During his rookie season, Perry rushed for two touchdowns and caught a pass for one. Perry even had the opportunity to run the ball during Super Bowl XX, as a nod to his popularity and contributions to the team's success. The first time he got the ball, he was tackled for a one-yard loss while attempting to throw his first NFL pass on a halfback option play. The second time he got the ball, he scored a touchdown (running over Patriots linebacker Larry McGrew in the process). About halfway through his rookie season, Ryan finally began to play Perry, who soon proved that he was a capable defensive lineman. His Super Bowl ring size is the largest of any professional football player in the history of the event. His ring size is 25, while the ring size for the average adult male is between 10 and 12. Perry went on to play for ten years in the NFL, retiring after the 1994 season. In his ten years as a pro, he regularly struggled with his weight, which hampered his performance at times. He played in 138 games, recording 29.5 sacks and five fumble recoveries, which he returned for a total of 71 yards. In his offensive career he ran five yards for two touchdowns, and had one reception for another touchdown. Perry later attempted a comeback, playing an unremarkable 1996 season with the London Monarchs of the World League of American Football (later NFL Europa). Q: what team did he play for? A:"
- **Target Completion:** "the Chicago Bears"

## Figure G.26

**Figure G.26** (p. 57): "Formatted dataset example for Symbol Insertion"

The figure shows a formatted example for Symbol Insertion (word unscrambling with inserted symbols):
- **Context:** "Please unscramble the letters into a word, and write that word: r e!c.i p r o.c a/l ="
- **Target Completion:** "reciprocal"

## Figure G.27

**Figure G.27** (p. 57): "Formatted dataset example for Reversed Words"

The figure shows a formatted example for Reversed Words:
- **Context:** "Please unscramble the letters into a word, and write that word: taefed ="
- **Target Completion:** "defeat"

## Figure G.28

**Figure G.28** (p. 58): "Formatted dataset example for SQuADv2"

The figure shows a formatted example for SQuADv2 (Stanford Question Answering Dataset v2):
- **Context:** "Title: The Blitz Background: From the German point of view, March 1941 saw an improvement. The Luftwaffe flew 4,000 sorties that month, including 12 major and three heavy attacks. The electronic war intensified but the Luftwaffe flew major inland missions only on moonlit nights. Ports were easier to find and made better targets. To confuse the British, radio silence was observed until the bombs fell. X- and Y-Gerät beams were placed over false targets and switched only at the last minute. Rapid frequency changes were introduced for X-Gerät, whose wider band of frequencies and greater tactical flexibility ensured it remained effective at a time when British selective jamming was degrading the effectiveness of Y-Gerät."
- **Multi-turn Q&A:**
  - Q: How many sorties were flown in March 1941? A: 4,000
  - Q: When did the Luftwaffe fly inland missions? A: [blank for model to complete]
- **Target Completion:** "only on moonlit nights"

## Figure G.29

**Figure G.29** (p. 58): "Formatted dataset example for BoolQ"

The figure shows a formatted example for BoolQ (Boolean Questions):
- **Context:** "Normal force -- In a simple case such as an object resting upon a table, the normal force on the object is equal but in opposite direction to the gravitational force applied on the object (or the weight of the object), that is, N = m g (\displaystyle N=mg), where m is mass, and g is the gravitational field strength (about 9.81 m/s on Earth). The normal force here represents the force applied by the table against the object that prevents it from sinking through the table and requires that the table is sturdy enough to deliver this normal force without breaking. However, it is easy to assume that the normal force and weight are action-reaction force pairs (a common mistake). In this case, the normal force and weight need to be equal in magnitude to explain why there is no upward acceleration of the object. For example, a ball that bounces upwards accelerates upwards because the normal force acting on the ball is larger in magnitude than the weight of the ball. question: is the normal force equal to the force of gravity? answer:"
- **Target Completion:** "yes"

## Figure G.30

**Figure G.30** (p. 58): "Formatted dataset example for CB"

The figure shows a formatted example for CB (CommitmentBank):
- **Context:** "The trend toward lower rents may seem surprising given that some communities in New York are bemoaning the loss of favorite local businesses to high rents. But, despite the recent softening, for many of these retailers there's still been too big a jump from the rental rates of the late 1970s, when their leases were signed. Certainly, the recent drop in prices doesn't mean Manhattan comes cheap. question: Manhattan comes cheap. true, false, or neither? answer:"
- **Target Completion:** "false"

## Figure G.31

**Figure G.31** (p. 59): "Formatted dataset example for RTE"

The figure shows a formatted example for RTE (Recognizing Textual Entailment):
- **Context:** "The bet, which won him dinner for four, was regarding the existence and mass of the top quark, an elementary particle discovered in 1995. question: The Top Quark is the last of six flavors of quarks predicted by the standard model theory of particle physics. True or False? answer:"
- **Target Completion:** "False"

## Figure G.32

**Figure G.32** (p. 59): "Formatted dataset example for WiC"

The figure shows a formatted example for WiC (Word-in-Context):
- **Context:** "An outfitter provided everything needed for the safari. Before his first walking holiday, he went to a specialist outfitter to buy some boots. question: Is the word 'outfitter' used in the same way in the two sentences above? answer:"
- **Target Completion:** "no"

## Figure G.33

**Figure G.33** (p. 59): "Formatted dataset example for WSC"

The figure shows a formatted example for WSC (Winograd Schema Challenge):
- **Context:** "Final Exam with Answer Key Instructions: Please carefully read the following passages. For each passage, you must identify which noun the pronoun marked in *bold* refers to. ===== Passage: Mr. Moncrieff visited Chester's luxurious New York apartment, thinking that it belonged to his son Edward. The result was that Mr. Moncrieff has decided to cancel Edward's allowance on the ground that he no longer requires *his* financial support. Question: In the passage above, what does the pronoun '*his*' refer to? Answer:"
- **Target Completion:** "mr. moncrieff"

## Figure G.34

**Figure G.34** (p. 59): "Formatted dataset example for TriviaQA. TriviaQA allows for multiple valid completions."

The figure shows a formatted example for TriviaQA:
- **Context:** "Q: 'Nude Descending A Staircase' is perhaps the most famous painting by which 20th century artist? A:"
- **Target Completions** (multiple valid answers):
  - MARCEL DUCHAMP
  - r mutt
  - duchamp
  - marcel duchamp
  - R.Mutt
  - Marcel duChamp
  - Henri-Robert-Marcel Duchamp
  - Marcel du Champ
  - henri robert marcel duchamp
  - Duchampian
  - Duchamp
  - duchampian
  - marcel du champ
  - Marcel Duchamp
  - MARCEL DUCHAMP

## Figure G.35

**Figure G.35** (p. 60): "Formatted dataset example for WebQA"

The figure shows a formatted example for WebQA:
- **Context:** "Q: What school did burne hogarth establish? A:"
- **Target Completion:** "School of Visual Arts"

## Figure G.36

**Figure G.36** (p. 60): "Formatted dataset example for De->En. This is the format for one- and few-shot learning, for this and other language tasks, the format for zero-shot learning is 'Q: What is the {language} translation of {sentence} A: {translation}.'"

The figure shows a formatted example for German-to-English translation:
- **Context:** "Keinesfalls dürfen diese für den kommerziellen Gebrauch verwendet werden. ="
- **Target Completion:** "In no case may they be used for commercial purposes."

## Figure G.37

**Figure G.37** (p. 60): "Formatted dataset example for En->De"

The figure shows a formatted example for English-to-German translation:
- **Context:** "In no case may they be used for commercial purposes. ="
- **Target Completion:** "Keinesfalls dürfen diese für den kommerziellen Gebrauch verwendet werden."

## Figure G.38

**Figure G.38** (p. 60): "Formatted dataset example for En->Fr"

The figure shows a formatted example for English-to-French translation:
- **Context:** "Analysis of instar distributions of larval I. verticalis collected from a series of ponds also indicated that males were in more advanced instars than females. ="
- **Target Completion:** "L'analyse de la distribution de fréquence des stades larvaires d'I. verticalis dans une série d'étangs a également démontré que les larves mâles étaient à des stades plus avancés que les larves femelles."

## Figure G.39

**Figure G.39** (p. 60): "Formatted dataset example for Fr->En"

The figure shows a formatted example for French-to-English translation:
- **Context:** "L'analyse de la distribution de fréquence des stades larvaires d'I. verticalis dans une série d'étangs a également démontré que les larves mâles étaient à des stades plus avancés que les larves femelles. ="
- **Target Completion:** "Analysis of instar distributions of larval I. verticalis collected from a series of ponds also indicated that males were in more advanced instars than females."

## Figure G.40

**Figure G.40** (p. 60): "Formatted dataset example for En->Ro"

The figure shows a formatted example for English-to-Romanian translation:
- **Context:** "The truth is that you want, at any price, and against the wishes of the peoples of Europe, to continue the negotiations for Turkey's accession to the European Union, despite Turkey's continuing refusal to recognise Cyprus and despite the fact that the democratic reforms are at a standstill. ="
- **Target Completion:** "Adevărul este că vă doriți, cu orice preț și împotriva dorinței europenilor, să continuați negocierile de aderare a Turciei la Uniunea Europeană, în ciuda refuzului continuu al Turciei de a recunoaște Ciprul și în ciuda faptului că reformele democratice au ajuns într-un punct mort."

## Figure G.41

**Figure G.41** (p. 61): "Formatted dataset example for Ro->En"

The figure shows a formatted example for Romanian-to-English translation:
- **Context:** "Adevărul este că vă doriți, cu orice preț și împotriva dorinței europenilor, să continuați negocierile de aderare a Turciei la Uniunea Europeană, în ciuda refuzului continuu al Turciei de a recunoaște Ciprul și în ciuda faptului că reformele democratice au ajuns într-un punct mort. ="
- **Target Completion:** "The truth is that you want, at any price, and against the wishes of the peoples of Europe, to continue the negotiations for Turkey's accession to the European Union, despite Turkey's continuing refusal to recognise Cyprus and despite the fact that the democratic reforms are at a standstill."

## Figure G.42

**Figure G.42** (p. 61): "Formatted dataset example for Arithmetic 1DC"

The figure shows a formatted example for single-digit composite arithmetic:
- **Context:** "Q: What is (2 * 4) * 6? A:"
- **Target Completion:** "48"

## Figure G.43

**Figure G.43** (p. 61): "Formatted dataset example for Arithmetic 2D-"

The figure shows a formatted example for two-digit subtraction:
- **Context:** "Q: What is 17 minus 14? A:"
- **Target Completion:** "3"

## Figure G.44

**Figure G.44** (p. 61): "Formatted dataset example for Arithmetic 2D+"

The figure shows a formatted example for two-digit addition:
- **Context:** "Q: What is 98 plus 45? A:"
- **Target Completion:** "143"

## Figure G.45

**Figure G.45** (p. 61): "Formatted dataset example for Arithmetic 2Dx"

The figure shows a formatted example for two-digit multiplication:
- **Context:** "Q: What is 95 times 45? A:"
- **Target Completion:** "4275"

## Figure G.46

**Figure G.46** (p. 61): "Formatted dataset example for Arithmetic 3D-"

The figure shows a formatted example for three-digit subtraction:
- **Context:** "Q: What is 509 minus 488? A:"
- **Target Completion:** "21"

## Figure G.47

**Figure G.47** (p. 61): "Formatted dataset example for Arithmetic 3D+"

The figure shows a formatted example for three-digit addition:
- **Context:** "Q: What is 556 plus 497? A:"
- **Target Completion:** "1053"

## Figure G.48

**Figure G.48** (p. 61): "Formatted dataset example for Arithmetic 4D-"

The figure shows a formatted example for four-digit subtraction:
- **Context:** "Q: What is 6209 minus 3365? A:"
- **Target Completion:** "2844"

---
[p. 62 continued]

## Figure G.49

**Figure G.49** (p. 62): "Formatted dataset example for Arithmetic 4D+"

The figure shows a formatted example for four-digit addition:
- **Context:** "Q: What is 9923 plus 617? A:"
- **Target Completion:** "10540"

## Figure G.50

**Figure G.50** (p. 62): "Formatted dataset example for Arithmetic 5D-"

The figure shows a formatted example for five-digit subtraction:
- **Context:** "Q: What is 40649 minus 78746? A:"
- **Target Completion:** "-38097"

## Figure G.51

**Figure G.51** (p. 62): "Formatted dataset example for Arithmetic 5D+"

The figure shows a formatted example for five-digit addition:
- **Context:** "Q: What is 65360 plus 16204? A:"
- **Target Completion:** "81564"
