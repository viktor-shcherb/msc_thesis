# F Appendix: Input/Output Examples [p. 32–34]

[p. 32] This appendix presents examples of correct and incorrect chains of thought produced by LaMDA 137B across several tasks, as well as examples from PaLM 540B on SayCan robot planning tasks.

## Table 13: Letter Concatenation [p. 32]

**Table 13** (p. 32): Examples of correct and incorrect chains of thought produced by LaMDA 137B on the letter concatenation task.

| Question | Model Answer | Correct? |
|---|---|---|
| Take the last letters of the words in "Waldo Schmidt" and concatenate them. | The last letter of "Waldo" is "o". The last letter of "Schmidt" is "t". Concatenating them is "ot". So the answer is ot. | CORRECT |
| Take the last letters of the words in "Daniel Friedman" and concatenate them. | The last letter of "Daniel" is "l". The last letter of "Friedman" is "m". Concatenating them is "lm". So the answer is lm. | INCORRECT |

[p. 32] In the incorrect example, the model states the last letter of "Friedman" is "m", but the last letter of "Friedman" is actually "n" (highlighted in green in the PDF as the error). The correct concatenation should be "ln", not "lm".

## Table 14: Coin Flip [p. 32]

**Table 14** (p. 32): Examples of correct and incorrect chains of thought produced by LaMDA 137B on the coinflip task.

| Question | Model Answer | Correct? |
|---|---|---|
| A coin is heads up. Andree flips the coin. Audrie does not flip the coin. Is the coin still heads up? | The coin was flipped by Andree. So the coin was flipped 1 time, which is an odd number. The coin started heads up, so after an odd number of flips, it will be tails up. So the answer is no. | CORRECT |
| A coin is heads up. Kristian does not flip the coin. Dallas does not flip the coin. Is the coin still heads up? | The coin was flipped by Kristian. So the coin was flipped 1 time, which is an odd number. The coin started heads up, so after an odd number of flips, it will be tails up. So the answer is no. | INCORRECT |

[p. 32] In the incorrect example, the model hallucinates that "The coin was flipped by Kristian" (highlighted in green as the error), when in fact the question states Kristian does not flip the coin. The correct answer should be "yes" since neither person flips the coin.

## Table 15: CSQA [p. 32]

**Table 15** (p. 32): Examples of correct and incorrect chains of thought produced by LaMDA 137B on CSQA.

| Question | Answer Choices | Model Answer | Correct? |
|---|---|---|---|
| When a person is beginning work, what are they building? | (a) time (b) accomplishing (c) working (d) momentum (e) tiredness | The answer must be something that is built. Of the above choices, only momentum is built. So the answer is (d). | CORRECT |
| Where are you likely to find a hamburger? | (a) fast food restaurant (b) pizza (c) ground up dead cows (d) mouth (e) cow carcus | The answer must be a place where hamburgers are found. Of the above choices, only fast food restaurants serve hamburgers. So the answer is (a). | CORRECT |
| Aside from water and nourishment what does your dog need? | (a) bone (b) charm (c) petted (d) lots of attention (e) walked | The answer must be something that a dog needs. Of the above choices, only bone is something that a dog needs. So the answer is (a). | INCORRECT (Ground truth is (d).) |
| What are you waiting alongside with when you're in a reception area? | (a) motel (b) chair (c) hospital (d) people (e) hotels | The answer must be something that is waiting with you in a reception area. Of the above choices, only people are waiting with you in a reception area. So the answer is (e). | INCORRECT (Ground truth is (d).) |

[p. 32] In the third example, the model incorrectly narrows down to "bone" as the only thing a dog needs, overlooking "lots of attention" which is the ground truth. In the fourth example, the model correctly identifies "people" as what waits with you but selects (e) instead of (d), which is the correct letter for "people." The error is highlighted as "answer is (e)" -- the ground truth is (d).

## Table 16: StrategyQA [p. 33]

**Table 16** (p. 33): Examples of correct and incorrect chains of thought produced by LaMDA 137B on StrategyQA.

| Question | Model Answer | Correct? |
|---|---|---|
| Will The Exorcist stimulate limbic system? | The Exorcist is a horror movie. Horror movies are scary. The limbic system is involved in fear. Thus, The Exorcist will stimulate the limbic system. So the answer is yes. | CORRECT |
| Was Jackson Pollock trained by Leonardo da Vinci? | Leonardo da Vinci lived in the 15th century. Jackson Pollock lived in the 20th century. Thus, Jackson Pollock could not have been trained by Leonardo da Vinci. So the answer is no. | CORRECT |
| Can Harry Potter book a flight on Asiana Airlines? | Harry Potter is a fictional character. Thus, Harry Potter can do anything. So the answer is yes. | INCORRECT (Ground truth is "no".) |
| Would a sophist use an épée? | A sophist is a person who is skilled in the art of persuasion. An épée is a type of sword. Thus, a sophist could use an épée. So the answer is yes. | INCORRECT (Ground truth is "no".) |

[p. 33] In the Harry Potter example, the model incorrectly reasons that a fictional character "can do anything." In the sophist/épée example, the model reasons that because a sophist could physically use an épée, the answer is yes, but the ground truth is "no" -- the question is about whether sophists characteristically use épées, not whether they physically could.

## Table 17: Date Understanding [p. 33]

**Table 17** (p. 33): Examples of correct and incorrect chains of thought produced by LaMDA 137B on Date Understanding.

| Question | Model Answer | Correct? |
|---|---|---|
| May 6, 1992 is like yesterday to Jane, but that is actually ten years ago. What is the date a month ago in MM/DD/YYYY? | May 6, 1992 is ten years ago, so today is May 6, 2002. So a month ago will be April 6, 2002. So the answer is 04/06/2002. | CORRECT |
| This is the last day of 1899. What is the date 24 hours later in MM/DD/YYYY? | Today is 12/31/1899. 24 hours later will be 01/01/1900. So the answer is 01/01/1900. | CORRECT |
| Jane scheduled 3 apointments with 5 poeple for tomorrow (Tue, 7/9/1972). What is the date one week ago from today in MM/DD/YYYY? | Tomorrow is 7/9/1972. One week ago from today is 7/2/1972. So the answer is 7/2/1972. | INCORRECT (Ground truth is 07/01/1972.) |
| Today is the palindrome day of 2020, because the MMDDYYYY format of the date is the same backwards as forwards. What is the date tomorrow in MM/DD/YYYY? | Today is 02/29/2020. Tomorrow will be 03/01/2020. So the answer is 03/01/2020. | INCORRECT (Ground truth is "02/03/2020".) |

[p. 33] In the third example, the model incorrectly computes "one week ago from today" -- if tomorrow is 7/9/1972 (Tuesday), today is 7/8/1972 (Monday), and one week ago from today is 7/1/1972, not 7/2/1972. The error is highlighted on "One week ago from today is 7/2/1972." In the fourth example, the model incorrectly identifies the palindrome day of 2020 as 02/29/2020 when it should be 02/02/2020 (since 02022020 is a palindrome), making tomorrow 02/03/2020. The error is highlighted on "Today is 02/29/2020."

## Table 18: Sports Understanding [p. 33]

**Table 18** (p. 33): Examples of correct and incorrect chains of thought produced by LaMDA 137B on Sports Understanding.

| Question | Model Answer | Correct? |
|---|---|---|
| Is the following sentence plausible? "Joao Moutinho was out at third." | Joao Moutinho is a soccer player. Being out at third is part of baseball, not soccer. So the answer is no. | CORRECT |
| Is the following sentence plausible? "Malcolm Brogdon eurostepped to the basket in the NBA Championship." | Malcolm Brogdon is a basketball player. Eurostepping to the basket is part of basketball. So the answer is yes. | CORRECT |
| Is the following sentence plausible? "Derrick White backhanded a shot." | Derrick White is a basketball player. Backhanding a shot is part of basketball. So the answer is yes. | INCORRECT (Ground truth is "no", backhanding a shot is part of hockey.) |
| Is the following sentence plausible? "Nazem Kadri was out at home." | Nazem Kadri is a hockey player. Being out at home is part of hockey. So the answer is yes. | INCORRECT (Ground truth is "no", being out at home is part of baseball.) |

[p. 33] In the Derrick White example, the model incorrectly associates "backhanding a shot" with basketball when it is actually part of hockey. In the Nazem Kadri example, the model incorrectly associates "being out at home" with hockey when it is actually part of baseball.

## Table 19: SayCan Robot Planning [p. 34]

**Table 19** (p. 34): Examples of correct and incorrect chains of thought produced by PaLM 540B on SayCan robot planning tasks.

| Question | Model Answer | Correct? |
|---|---|---|
| I spilled my coke on the table, could you throw it away and then bring me something to help clean? | Explanation: The user has spilled their coke on the table. I will throw away the coke and then bring the user a sponge. Plan: find(coke), pick(coke), find(trash), put(coke), find(sponge), pick(sponge), find(table), put(sponge). | CORRECT |
| Could you compost that apple for me? | Explanation: The user would like me to compost the apple. I will move the apple to the compost. Plan: find(apple), pick(apple), find(trash), put(apple). | CORRECT |
| Can you bring me a drink that is not coke? | Explanation: The user asked me to bring a drink that is not coke, I will bring a sprite. Plan: find(sprite), pick(sprite), find(user), put(sprite). | INCORRECT (Feasible answers including finding lime soda, pepsi, grapefruit soda or water, because there is no sprite in the scene as defined in Table 28.) |
| Can you bring me something salty? | Explanation: The user would like something salty. There are several options in the objects list, so I will bring the user a lime soda. Plan: find(lime soda), pick(lime soda), find(user), put(lime soda). | INCORRECT (Feasible answers including finding chips. The model misidentify lime soda as salty.) |
