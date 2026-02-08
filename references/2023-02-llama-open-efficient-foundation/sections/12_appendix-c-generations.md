# Appendix C: Generations from LLaMA-65B [p. 19-21]

[p. 19] Examples of generations obtained with LLaMA-65B (without instruction finetuning) are shown. Prompts are in bold.

## Example 1: Fibonacci sequence continuation [p. 19]

**Prompt:** "**1 1 2 3 5 8**"

The model continues the Fibonacci sequence (13 21 34 55 89 144 233 377 610 987) and then generates an expository passage about the Fibonacci sequence, explaining it was discovered by Leonardo of Pisa around 1200, that it is an infinite sequence which grows rapidly, and that it is named after Fibonacci. The model references his famous Liber abaci of 1202 and the study of rabbit population growth.

## Example 2: Recommendation letter [p. 19]

**Prompt:** "**Here is the recommendation letter that I wrote for an application to a dragon feeder position at the Magic Unicorn Corporation:**"

The model generates a full recommendation letter in a formal style, addressed to "Dear recruiter," written by "Honorable Knight Sir George." The letter recommends an unnamed person for the dragon feeder position, citing their ability to remember and process large amounts of information and their deep understanding of dragons (as an accomplished knight). The letter is well-structured with proper formal letter conventions.

## Example 3: Python code generation [p. 19]

**Prompt:** (implied code prompt)

The model generates a Python function `solve(a: float, b: float, c: float)` that finds the real roots of ax^2+bx+c using the quadratic formula. The code correctly computes the discriminant `d = b**2-4*a*c`, handles three cases (d > 0: two roots, d == 0: one root, else: returns False), and uses `math.sqrt(d)` for computation. The code is 10 lines long and syntactically correct.

## Example 4: Yann LeCun rap album review [p. 20]

**Prompt:** "**Did you know that Yann LeCun dropped a rap album last year? We listened to it and here's what we thought:**"

The model generates a creative fictional review of a rap album by "Dr. LeCun, the founder of deep learning." The album is titled "Deep Learning" and described as a mix of rock, punk and rap. The review praises LeCun's flow and lyrical ability, and includes fictional lyrics about AI and deep learning: "We gotta think about the future, it's gonna be here soon / Maybe we can even put some AI in the moon / Think about the children, think about the next generation / Let's make sure we put the right systems in their foundation." A chorus is included: "It's all about the learning / it's all about the network / It's all about the training / it's all about the perception."

## Example 5: Seinfeld-style AI watch scene [p. 20]

**Prompt:** "**(An hilarious scene between Jerry and George where George presents his new AI watch)**"

The model generates a dialogue in the style of the TV show Seinfeld, where George presents an "AI watch" to Jerry. George describes it as a minicomputer with features including a world time clock, alarm, calculator, database, language translator, word processor, spellchecker, PDA, and modem that "even makes cappuccino." The scene includes characteristic Seinfeld-style humor with the punchline: Jerry asks "I don't see anything on your wrist" and George replies "That's because it's a microprocessor."

## Example 6: Historical dialogue between Gauss and Curie [p. 21]

**Prompt:** "**The sun goes down, and finally Gauss and Curie find time to relax and discuss after an exhausting day of work.**"

The model generates a dialogue between the historical figures Gauss and Curie discussing whether Gauss was "the first geek." Gauss argues his case based on inventing the commercial telegraph in 1833 and sending the first message on the first commercial telegraph line between Hamburg and Cuxhaven in Germany. The message he sent was the Latin phrase "numquam retrorsum" meaning "Never backwards." Curie challenges his claim by noting the word "geek" did not exist then, but Gauss argues the telegraph was an early form of social media. The dialogue includes a humorous exchange about Twitter's 140-character limit versus Gauss's 11-character Latin phrase, with Gauss claiming he "managed to do more with less."
