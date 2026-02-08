# G Appendix: Full Prompts [p. 35–41]

[p. 35–41] This appendix provides the few-shot exemplars used for the full chain of thought prompts across different tasks. Tables 20–28 cover math word problems, AQuA algebraic word problems, last letter concatenation, coin flip, CSQA, StrategyQA, date understanding, sports understanding, and SayCan robot planning respectively.

## Table 20: Math Word Problems Prompt [p. 35]

**Table 20** (p. 35): Few-shot exemplars for full chain of thought prompt for math word problems. This set of exemplars was used for all math word problem datasets except AQuA.

**PROMPT FOR MATH WORD PROBLEMS**

**Q:** There are 15 trees in the grove. Grove workers will plant trees in the grove today. After they are done, there will be 21 trees. How many trees did the grove workers plant today?
**A:** There are 15 trees originally. Then there were 21 trees after some more were planted. So there must have been 21 - 15 = 6. The answer is 6.

**Q:** If there are 3 cars in the parking lot and 2 more cars arrive, how many cars are in the parking lot?
**A:** There are originally 3 cars. 2 more cars arrive. 3 + 2 = 5. The answer is 5.

**Q:** Leah had 32 chocolates and her sister had 42. If they ate 35, how many pieces do they have left in total?
**A:** Originally, Leah had 32 chocolates. Her sister had 42. So in total they had 32 + 42 = 74. After eating 35, they had 74 - 35 = 39. The answer is 39.

**Q:** Jason had 20 lollipops. He gave Denny some lollipops. Now Jason has 12 lollipops. How many lollipops did Jason give to Denny?
**A:** Jason started with 20 lollipops. Then he had 12 after giving some to Denny. So he gave Denny 20 - 12 = 8. The answer is 8.

**Q:** Shawn has five toys. For Christmas, he got two toys each from his mom and dad. How many toys does he have now?
**A:** Shawn started with 5 toys. If he got 2 toys each from his mom and dad, then that is 4 more toys. 5 + 4 = 9. The answer is 9.

**Q:** There were nine computers in the server room. Five more computers were installed each day, from monday to thursday. How many computers are now in the server room?
**A:** There were originally 9 computers. For each of 4 days, 5 more computers were added. So 5 * 4 = 20 computers were added. 9 + 20 is 29. The answer is 29.

**Q:** Michael had 58 golf balls. On tuesday, he lost 23 golf balls. On wednesday, he lost 2 more. How many golf balls did he have at the end of wednesday?
**A:** Michael started with 58 golf balls. After losing 23 on tuesday, he had 58 - 23 = 35. After losing 2 more, he had 35 - 2 = 33 golf balls. The answer is 33.

**Q:** Olivia has $23. She bought five bagels for $3 each. How much money does she have left?
**A:** Olivia had 23 dollars. 5 bagels for 3 dollars each will be 5 x 3 = 15 dollars. So she has 23 - 15 dollars left. 23 - 15 is 8. The answer is 8.

## Table 21: AQuA Prompt [p. 36]

**Table 21** (p. 36): Few-shot exemplars for full chain of thought prompt for AQuA.

**PROMPT FOR AQUA ALGEBRAIC WORD PROBLEMS**

**Q:** John found that the average of 15 numbers is 40. If 10 is added to each number then the mean of the numbers is?
Answer Choices: (a) 50 (b) 45 (c) 65 (d) 78 (e) 64
**A:** If 10 is added to each number, then the mean of the numbers also increases by 10. So the new mean would be 50. The answer is (a).

**Q:** If a / b = 3/4 and 8a + 5b = 22, then find the value of a.
Answer Choices: (a) 1/2 (b) 3/2 (c) 5/2 (d) 4/2 (e) 7/2
**A:** If a / b = 3/4, then b = 4a / 3. So 8a + 5(4a / 3) = 22. This simplifies to 8a + 20a / 3 = 22, which means 44a / 3 = 22. So a is equal to 3/2. The answer is (b).

**Q:** A person is traveling at 20 km/hr and reached his destiny in 2.5 hr then find the distance?
Answer Choices: (a) 53 km (b) 55 km (c) 52 km (d) 60 km (e) 50 km
**A:** The distance that the person traveled would have been 20 km/hr * 2.5 hrs = 50 km. The answer is (e).

**Q:** How many keystrokes are needed to type the numbers from 1 to 500?
Answer Choices: (a) 1156 (b) 1392 (c) 1480 (d) 1562 (e) 1788
**A:** There are 9 one-digit numbers from 1 to 9. There are 90 two-digit numbers from 10 to 99. There are 401 three-digit numbers from 100 to 500. 9 + 90(2) + 401(3) = 1392. The answer is (b).

## Table 22: Last Letter Concatenation Prompt [p. 36]

**Table 22** (p. 36): Few-shot exemplars for full chain of thought prompt for the last letter concatenation task.

**PROMPT FOR LAST LETTER CONCATENATION**

**Q:** Take the last letters of the words in "Elon Musk" and concatenate them.
**A:** The last letter of "Elon" is "n". The last letter of "Musk" is "k". Concatenating them is "nk". The answer is nk.

**Q:** Take the last letters of the words in "Larry Page" and concatenate them.
**A:** The last letter of "Larry" is "y". The last letter of "Page" is "e". Concatenating them is "ye". The answer is ye.

**Q:** Take the last letters of the words in "Sergey Brin" and concatenate them.
**A:** The last letter of "Sergey" is "y". The last letter of "Brin" is "n". Concatenating them is "yn". The answer is yn.

**Q:** Take the last letters of the words in "Bill Gates" and concatenate them.
**A:** The last letter of "Bill" is "l". The last letter of "Gates" is "s". Concatenating them is "ls". The answer is ls.

---
[p. 37–41 continued]

## Table 23: Coin Flip Prompt [p. 37]

**Table 23** (p. 37): Few-shot exemplars for full chain of thought prompt for the coinflip task.

**PROMPT FOR COIN FLIP**

**Q:** Q: A coin is heads up. Ka flips the coin. Sherrie flips the coin. Is the coin still heads up?
**A:** The coin was flipped by Ka and Sherrie. So the coin was flipped 2 times, which is an even number. The coin started heads up, so after an even number of flips, it will still be heads up. So the answer is yes.

**Q:** A coin is heads up. Jamey flips the coin. Teressa flips the coin. Is the coin still heads up?
**A:** The coin was flipped by Jamey and Teressa. So the coin was flipped 2 times, which is an even number. The coin started heads up, so after an even number of flips, it will be heads up. So the answer is yes.

**Q:** A coin is heads up. Maybelle flips the coin. Shalonda does not flip the coin. Is the coin still heads up?
**A:** The coin was flipped by Maybelle. So the coin was flipped 1 time, which is an odd number. The coin started heads up, so after an odd number of flips, it will be tails up. So the answer is no.

**Q:** A coin is heads up. Millicent does not flip the coin. Conception flips the coin. Is the coin still heads up?
**A:** The coin was flipped by Conception. So the coin was flipped 1 time, which is an odd number. The coin started heads up, so after an odd number of flips, it will be tails up. So the answer is no.

**Q:** A coin is heads up. Sal flips the coin. Raymond does not flip the coin. Is the coin still heads up?
**A:** The coin was flipped by Sal. So the coin was flipped 1 time, which is an odd number. The coin started heads up, so after an odd number of flips, it will be tails up. So the answer is no.

**Q:** A coin is heads up. Conception flips the coin. Kristian does not flip the coin. Is the coin still heads up?
**A:** The coin was flipped by Conception. So the coin was flipped 1 time, which is an odd number. The coin started heads up, so after an odd number of flips, it will be tails up. So the answer is no.

**Q:** A coin is heads up. Inga does not flip the coin. Elanor does not flip the coin. Is the coin still heads up?
**A:** The coin was flipped by no one. So the coin was flipped 0 times. The coin started heads up, and it was not flipped, so it is still heads up. So the answer is yes.

**Q:** A coin is heads up. Ryan flips the coin. Shaunda flips the coin. Is the coin still heads up?
**A:** The coin was flipped by Ryan and Shaunda. So the coin was flipped 2 times, which is an even number. The coin started heads up, so after an even number of flips, it will still be heads up. So the answer is yes.

## Table 24: CSQA Prompt [p. 38]

**Table 24** (p. 38): Few-shot exemplars for full chain of thought prompt for CSQA. There are newlines between the answer choices that are omitted in the table for space reasons.

**PROMPT FOR CSQA**

**Q:** What do people use to absorb extra ink from a fountain pen? Answer Choices: (a) shirt pocket (b) calligrapher's hand (c) inkwell (d) desk drawer (e) blotter
**A:** The answer must be an item that can absorb ink. Of the above choices, only blotters are used to absorb ink. So the answer is (e).

**Q:** What home entertainment equipment requires cable?
Answer Choices: (a) radio shack (b) substation (c) television (d) cabinet
**A:** The answer must require cable. Of the above choices, only television requires cable. So the answer is (c).

**Q:** The fox walked from the city into the forest, what was it looking for? Answer Choices: (a) pretty flowers (b) hen house (c) natural habitat (d) storybook
**A:** The answer must be something in the forest. Of the above choices, only natural habitat is in the forest. So the answer is (b).

**Q:** Sammy wanted to go to where the people were. Where might he go? Answer Choices: (a) populated areas (b) race track (c) desert (d) apartment (e) roadblock
**A:** The answer must be a place with a lot of people. Of the above choices, only populated areas have a lot of people. So the answer is (a).

**Q:** Where do you put your grapes just before checking out? Answer Choices: (a) mouth (b) grocery cart (c) super market (d) fruit basket (e) fruit market
**A:** The answer should be the place where grocery items are placed before checking out. Of the above choices, grocery cart makes the most sense for holding grocery items. So the answer is (b).

**Q:** Google Maps and other highway and street GPS services have replaced what? Answer Choices: (a) united states (b) mexico (c) countryside (d) atlas
**A:** The answer must be something that used to do what Google Maps and GPS services do, which is to give directions. Of the above choices, only atlases are used to give directions. So the answer is (d).

**Q:** Before getting a divorce, what did the wife feel who was doing all the work? Answer Choices: (a) harder (b) anguish (c) bitterness (d) tears (e) sadness
**A:** The answer should be the feeling of someone getting divorced who was doing all the work. Of the above choices, the closest feeling is bitterness. So the answer is (c).

## Table 25: StrategyQA Prompt [p. 39]

**Table 25** (p. 39): Few-shot exemplars for full chain of thought prompt for StrategyQA.

**PROMPT FOR STRATEGYQA**

**Q:** Do hamsters provide food for any animals?
**A:** Hamsters are prey animals. Prey are food for predators. Thus, hamsters provide food for some animals. So the answer is yes.

**Q:** Could Brooke Shields succeed at University of Pennsylvania?
**A:** Brooke Shields went to Princeton University. Princeton University is about as academically rigorous as the University of Pennsylvania. Thus, Brooke Shields could also succeed at the University of Pennsylvania. So the answer is yes.

**Q:** Yes or no: Hydrogen's atomic number squared exceeds number of Spice Girls?
**A:** Hydrogen has an atomic number of 1. 1 squared is 1. There are 5 Spice Girls. Thus, Hydrogen's atomic number squared is less than 5. So the answer is no.

**Q:** Yes or no: Is it common to see frost during some college commencements?
**A:** College commencement ceremonies can happen in December, May, and June. December is in the winter, so there can be frost. Thus, there could be frost at some commencements. So the answer is yes.

**Q:** Yes or no: Could a llama birth twice during War in Vietnam (1945-46)?
**A:** The War in Vietnam was 6 months. The gestation period for a llama is 11 months, which is more than 6 months. Thus, a llama could not give birth twice during the War in Vietnam. So the answer is no.

**Q:** Yes or no: Would a pear sink in water?
**A:** The density of a pear is about 0.6g/cm^3, which is less than water. Objects less dense than water float. Thus, a pear would float. So the answer is no.

## Table 26: Date Understanding Prompt [p. 39]

**Table 26** (p. 39): Few-shot exemplars for full chain of thought prompt for Date Understanding.

**PROMPT FOR DATE UNDERSTANDING**

**Q:** 2015 is coming in 36 hours. What is the date one week from today in MM/DD/YYYY?
**A:** If 2015 is coming in 36 hours, then it is coming in 2 days. 2 days before 01/01/2015 is 12/30/2014, so today is 12/30/2014. So one week from today will be 01/05/2015. So the answer is 01/05/2015.

**Q:** The first day of 2019 is a Tuesday, and today is the first Monday of 2019. What is the date today in MM/DD/YYYY?
**A:** If the first day of 2019 was Tuesday, then 01/01/2019 was a Tuesday. Today is the first monday, would be six days later. So today is 01/07/2019. So the answer is 01/07/2019.

**Q:** The concert was scheduled to be on 06/01/1943, but was delayed by one day to today. What is the date 10 days ago in MM/DD/YYYY?
**A:** One day after 06/01/1943 is 06/02/1943, so today is 06/02/1943. 10 days before today is 05/23/1943. So the answer is 05/23/1943.

**Q:** It is 4/19/1969 today. What is the date 24 hours later in MM/DD/YYYY?
**A:** Today is 04/19/1969. 24 hours later is one day after today, which would be 04/20/1969. So the answer is 04/20/1969.

**Q:** Jane thought today is 3/11/2002, but today is in fact Mar 12, which is 1 day later. What is the date 24 hours later in MM/DD/YYYY?
**A:** Today is 03/12/2002. So the date 24 hours later will be 03/13/2002. So the answer is 03/13/2002.

**Q:** Jane was born on the last day of Feburary in 2001. Today is her 16-year-old birthday. What is the date yesterday in MM/DD/YYYY?
**A:** The last day of February is the 28th, so Jane was born on 02/28/2001. Today is her 16-year old birthday, so today is 02/28/2017. So yesterday was 02/27/2017. So the answer is 02/27/2017.

## Table 27: Sports Understanding Prompt [p. 40]

**Table 27** (p. 40): Few-shot exemplars for full chain of thought prompt for Sports Understanding.

**PROMPT FOR SPORTS UNDERSTANDING**

**Q:** Is the following sentence plausible? "Kyle Palmieri was called for slashing."
**A:** Kyle Palmieri is a hockey player. Being called for slashing is part of hockey. So the answer is yes.

**Q:** Is the following sentence plausible? "Joao Moutinho caught the screen pass in the NFC championship."
**A:** Joao Moutinho is a soccer player. The NFC championship is part of American football, not soccer. So the answer is no.

**Q:** Is the following sentence plausible? "Carson Wentz set the pick and roll."
**A:** Carson Wentz is an American football player. Pick and roll is part of basketball, not football. So the answer is no.

**Q:** Is the following sentence plausible? "Jonas Valanciunas beat the buzzer."
**A:** Jonas Valanciunas is a basketball player. Beating the buzzer is part of basketball. So the answer is yes.

**Q:** Is the following sentence plausible? "Jamel Murray was perfect from the line."
**A:** Jamal Murray is a basketball player. Being perfect from the line is part of basketball. So the answer is yes.

**Q:** Is the following sentence plausible? "Sam Darnold passed the puck."
**A:** Sam Darnold is a American football player. Passing the puck is part of hockey, not American football. So the answer is no.

**Q:** Is the following sentence plausible? "Draymond Green threw a touchdown."
**A:** Draymond Green is an basketball player. Throwing a touchdown is part of football, not basketball. So the answer is no.

**Q:** Is the following sentence plausible? "Malcolm Brogdon banked the shot in."
**A:** Malcolm Brogdon is a basketball player. Banking the shot in is part of basketball. So the answer is yes.

## Table 28: SayCan Robot Planning Prompt [p. 41]

**Table 28** (p. 41): Few-shot exemplars for full chain of thought prompt for SayCan robot planning tasks.

**PROMPT FOR SAYCAN ROBOT PLANNING**

Locations = [counter, table, user, trash, bowl].
Objects = [7up, apple, kettle chips, tea, multigrain chips, coke, lime soda, jalapeno chips, rice chips, orange, grapefruit soda, pepsi, redbull, energy bar, sponge, water].
The robot can pick up items with pick(object) and put down items with put(object) as well as find objects or locations with find(). The robot can only understand the explicit locations and objects listed.

**Human:** I'm hungry, can you bring me some chips.
**Explanation:** The user is hungry and has asked for chips. There are several types of chips available, I will bring the user the kettle chips.
**Plan:** 1. find(kettle chips), 2. pick(kettle chips), 3. find(user), 4. put(kettle chips), 5. done().

**Human:** How would you move the grapefruit drink from the table to the counter?
**Explanation:** The user has asked me to move the grapefruit drink to the counter.
**Plan:** 1. find(grapefruit soda), 2. pick(grapefruit soda), 3. find(counter), 4. put(grapefruit soda), 5. done().

**Human:** How would you bring me some snacks?
**Explanation:** The user has asked for snacks, I will choose two items and bring them. I will bring jalapeno chips and an apple.
**Plan:** 1. find(jalapeno chips), 2. pick(jalapeno chips), 3. find(user), 4. put(jalapeno chips), 5. find(apple), 6. pick(apple), 7. find(user), 8. put(apple), 9. done().

**Human:** How would you bring me something to eat that isn't a fruit?
**Explanation:** The user has asked for a food that isn't a fruit, I will bring an energy bar to them.
**Plan:** 1. find(energy bar), 2. pick(energy bar), 3. find(user), 4. put(energy bar), 5. done().

**Human:** How would you put the rice chips in the bowl and then move the tea to the table?
**Explanation:** The user has asked me to do two tasks, I will do one and then the other.
**Plan:** 1. find(rice chips), 2. pick(rice chips), 3. find(bowl), 4. put(rice chips), 5. find(tea), 6. pick(tea), 7. find(table), 8. put(tea), 9. done().

**Human:** How would you throw away a redbull?
**Explanation:** The user has asked me to throw away the redbull, I will move it to the trash.
**Plan:** 1. find(redbull), 2. pick(redbull), 3. find(trash), 4. put(redbull), 5. done().

**Human:** Bring me a drink.
**Explanation:** The user has asked for a drink and there are many options. I will bring them a water.
**Plan:** 1. find(water), 2. pick(water), 3. find(user), 4. put(water), 5. done().
