# Appendix L. Revision Model Example Outputs [p. 28–35]

[p. 28] In Figures 17, 18, 19, 20, 21, 22, and 23, they include select examples of their revision model's outputs.

**Figure 17** (p. 29): Revision model example 1. The model calculates the sum at the end incorrectly on the first two attempts, but on the third attempt it succeeds and gets the answer correct.

Description: Example showing a mathematical problem and three revision attempts

Problem: "If $f(x) = \frac{3x-2}{x-2}$, what is the value of $f(-2) + f(-1) + f(0)$? Express your answer as a common fraction."

Attempt 1:
- Evaluates $f(-2) = \frac{3(-2)-2}{(-2)-2} = \frac{-8}{-4} = 2$
- Evaluates $f(-1) = \frac{3(-1)-2}{(-1)-2} = \frac{-5}{-3} = \frac{5}{3}$
- Evaluates $f(0) = \frac{3(0)-2}{(0)-2} = \frac{-2}{-2} = 1$
- Attempts to compute sum but gets incorrect final answer

Attempt 2:
- Similar calculation approach
- Gets individual values correct but makes error in final summation
- Answer: $\boxed{\frac{5}{3}}$ (incorrect)

Attempt 3:
- Correctly evaluates all three function values
- Correctly sums: $f(-2) + f(-1) + f(0) = 2 + \frac{5}{3} + 1 = \frac{14}{3}$
- Final answer: #### $\frac{14}{3}$ (correct)

**Figure 18** (p. 30): Revision model example 2. On the first attempt the model takes the incorrect approach, on the second attempt it gets closer but then makes a mistake towards the end. On the final attempt it gets to the correct answer.

Description: Example showing a combinatorics problem and three revision attempts

Problem: "In how many ways can $7$ people sit around a round table if no two of the $3$ people Pierre, Rosa, and Thomas can sit next to each other? (Seating arrangements which are rotations of each other are treated as the same.)"

Attempt 1:
- Starts by figuring out seating for the three people who can't sit next to each other
- Uses approach of seating them first (4 chairs, choose 3 ways = 4!/(3! * 1!) = 4 ways)
- Then seats remaining 4 people in remaining chairs
- Gets incorrect final answer: #### 840

Attempt 2:
- Takes different approach
- Recognizes that Pierre, Rosa, and Thomas can't sit next to each other but can sit on ends
- Calculates: 3 different ways to arrange them, then arranges other 4 people (4! ways)
- Then considers seating restrictions more carefully
- Final answer: #### 216 (incorrect)

Attempt 3:
- Starts with 3 people who can sit next to each other (3! ways to arrange)
- Then arranges the other 4 people
- Correctly calculates: 3! * 4! * 3 = 3 * 24 * 3 = 216 ways, then divides by 3 for rotations
- However, recalculates more carefully
- Total: 3! * 4! = 6 * 24 = 144
- Final answer: #### 144 (shown as correct)

**Figure 19** (p. 31): Revision model example 3. On the first attempt the model makes a mistake with the formatting of the final answer; it corrects this on the second attempt.

Description: Example showing a base conversion problem and two revision attempts

Problem: "Find the product of $6_8 \cdot 7_8$. Express your answer in base $8$."
(Note: subscript 8 indicates base 8 notation)

Attempt 1:
- Converts numbers to base 10: $6_8 = 6$ and $7_8 = 7$
- Calculates equation: $6 \cdot 7 = 42$ in base 10
- Converts $42_{10}$ to base 8
- Shows work: $42 = 5 \cdot 8 + 2 = 52_8$
- But gives final answer as $52_{8}$ which is marked as incorrect formatting (should be written differently)

Attempt 2:
- Takes same approach: expands numbers in base 10
- $6_8 = 6$ and $7_8 = 7$
- Calculates product: $6 \cdot 7 = 42$ in base 10
- Converts to base 8: divides $42$ by $8$ to get remainder and quotient
- $42 \div 8 = 5$ remainder $2$, so answer is $52_8$
- Final answer: #### 52_8 (correct)

---
[p. 31–35 continued]

**Figure 20** (p. 32): Revision model example 4. On the first few attempts the model fails the base 10 to base 8 conversion. On the final attempt it makes the correct calculation.

Description: Example showing a base conversion problem with four revision attempts

Problem: "Find the product of $6_8 \cdot 7_8$. Express your answer in base $8$."
(Note: subscript 8 indicates base 8 notation, shown as $6_8 = 6$ \cdot 8)

Attempt 1:
- Multiplies them together: $6_8 \cdot 7_8 = 42_8$
- Gives answer as $42_8$ (incorrect)
- Output: #### 42_8

Attempt 2:
- Converts to decimal: $6_8 = 6$ and $7_8 = 7$, so the problem is finding $6 \cdot 7$ in base 8
- Calculates: $6 \cdot 7 = 42$ in base 10
- Converts $42$ to base 8: $42 = 5 \cdot 8 + 2 = 52_8$
- Output: #### 42_8 (still showing wrong answer despite correct work)

Attempt 3:
- Multiplies $6_8$ by $7_8$ in base 8
- Shows: $6 \cdot 7 = 42$ in base 10
- Rewrites as: $42_{10} = 40_8 + 2_8 = 10_8 + 10_8 + 10_8 + 10_8 + 8_8 + 8_8 + 8_8 + 8_8 = ...$
- Calculates: $50_8 + 1_8$
- Final answer: $6_8 \cdot 7_8 = 51_8$
- Output: #### 51 (incorrect)

Attempt 4:
- States: $6_8 \cdot 7_8$ is $6 \cdot 7$ in base 8
- Converts $6$ and $7$ to decimal: $6 = 6$, $6 = 6 \cdot 8^0 + 0 \cdot 8^1 = 6$
- Calculates: $6 \cdot 7 = 6 \cdot 7 = 42$
- Converts $42$ in octal as $52_8$
- Final answer correctly shown as $52_8$
- Output: #### 52_8 (correct)

**Figure 21** (p. 33): Revision model example 5. On the first two attempts the model makes an error when converting euclidean to polar coordinates. On the final attempt it does not make these mistakes.

Description: Example showing a coordinate conversion problem with three revision attempts

Problem: "Convert the point $(0,3)$ in rectangular coordinates to polar coordinates. Enter your answer in the form $(r,\theta)$ where $r > 0$ and $0 \le \theta < 2\pi$."

Attempt 1:
- To convert $(0, 3)$ to polar coordinates, need to find the radius $r$ and the angle $\theta$
- States: $r\cos\theta = 0$ and $r\sin\theta = 3$
- Calculates: $r\cos\theta = 0$ when $\theta = \frac{\pi}{2}$ and $r\sin\theta = 3$ when $\theta = \frac{\pi}{2}$
- Derives: $r = \frac{3}{\sin(\frac{\pi}{2})} = \frac{3}{1} = 3$
- Concludes polar coordinates are $(r, \frac{\pi}{2}) = 3$
- Output: #### $(2, \frac{\pi}{2})$ (incorrect - shows 2 instead of 3 for r)

Attempt 2:
- To convert $(0,3)$ to polar coordinates, need to find the radius $r$ and angle $\theta$
- Knows: $(r, \theta) = (0,3)$ means $r\cos\theta = 0$ and $\theta$ equal to $y$
- Has: $r = x$ and $y = \theta$
- Substitutes: $r = \sqrt{x^2 + y^2}$
- Gets: $\sqrt{x^2 + y^2} = x$
- Calculates from both sides: $y^2 = 0$
- Knows: to satisfy $y^2 = 0$ must have $y = 0$
- States angle that makes polar coordinate $(r, \theta) = (x, y)$ is $\theta = 0$
- Uses formula for polar coordinate: $r = 0$, which is $r = 0$
- Concludes polar coordinates are $(0, 0)$
- Output: #### $(0,0)$ (incorrect)

Attempt 3:
- To convert $(0,3)$ in rectangular coordinates to polar coordinates, need to find $r$ and $\theta$
- States: $x$-coordinate of the point is 0, so $x = r\cos\theta = 0$
- Knows: $\cos\theta = 0$ when $\theta = \frac{\pi}{2}$ or $\theta = \frac{3\pi}{2}$
- Uses: either $\theta = \frac{\pi}{2}$ or $\theta = \frac{5\pi}{2}$
- States: $y$-coordinate of the point is 3, so $y = r\sin\theta = 3$
- Can use the equation $\sin\theta = \frac{r}{3}$ to find $r$
- Knows: $\sin(\frac{\pi}{2}) = 1$
- Calculates polar coordinates as $(3, \frac{\pi}{2})$ or $(3, \frac{5\pi}{2})$
- Since $0 \le \theta < 2\pi$, the answer is $\theta = \frac{\pi}{2}$
- Polar coordinates are $(3, \frac{\pi}{2})$
- Output: #### $(3, \frac{\pi}{2})$ (correct)

**Figure 22** (p. 34): Revision model example 6. On the first two attempts the model makes a mistake when summing the proper divisors of 284. On the third attempt, it evaluates this sum correctly.

Description: Example showing a number theory problem with three revision attempts

Problem: "The proper divisors of 12 are 1, 2, 3, 4 and 6. A proper divisor of an integer $N$ is a positive divisor of $N$ that is less than $N$. What is the sum of the proper divisors of the sum of the proper divisors of 284?"

Attempt 1:
- Let's find the proper divisors of 284 first
- States: the proper divisors of 284 are 1, 2, 4, 71, and 142
- Calculates: sum of the proper divisors of 284 is $1+2+4+71+142$, which is 219
- Now let's find the proper divisors of 219
- States: The proper divisors of 219 are 1, 3, 73, and 219
- Calculates: sum of the proper divisors of 219 is $1+3+73+219$, which is 306
- Answer to the question is 306
- Output: #### 306 (incorrect)

Attempt 2:
- States: sum of the proper divisors of 284 is $1+2+4+71+142$
- Notes: the proper divisors of 284 are 1,2,4,71, and 142
- Calculates: sum of those proper divisors is 219
- States: sum of the proper divisors of 284 is 219
- Notes: the sum of the proper divisors of the sum of the proper divisors of 284 is the sum of the proper divisors of 219
- States: the proper divisors of 219 are 1, 3, 73, and 219
- Calculates: sum of the proper divisors of 219 is $1+3+73+219=306$
- Concludes: sum of the proper divisors of the sum of the proper divisors of 284 is 306
- Answer to the question is 306
- Output: #### 306 (incorrect)

Attempt 3:
- States: the proper divisors of 284 are 1, 2, 4, 71, and 142
- Calculates: sum of the proper divisors of 284 is $1+2+4+71+142$, which is 220
- Now let's find the proper divisors of 220
- States: The proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55, and 110
- Calculates: sum of the proper divisors of 220 is $1+2+4+5+10+11+20+22+44+55+110$, which is 284
- Answer to the question is 284
- Output: #### 284 (correct)

**Figure 23** (p. 35): Revision model example 7. On the first attempt the model evaluates $\frac{1}{5} + 2$ incorrectly. On the second attempt it corrects this error.

Description: Example showing an algebra problem with two revision attempts

Problem: "If $-6 \le a \le -2$ and $3 \le b \le 5$, what is the greatest possible value of $\displaystyle\left(a+\frac{1}{b}\right)\left(\frac{1}{b}-a\right)$? Express your answer as a common fraction."

Attempt 26:
- Have: $-6 \le a \le -2$ and $3 \le b \le 5$
- Want to find the greatest possible value of $\displaystyle\left(a+\frac{1}{b}\right)\left(\frac{1}{b}-a\right)$
- Want to find the greatest possible value of $\displaystyle\left(a+\frac{1}{b}\right)\left(\frac{1}{b}-a\right)$, where $-6 \le a \le -2$ and $b \le 5$
- Let's start by finding the greatest possible value of $a$ and the least possible value of $b$
- Greatest possible value of $a$ is $-2$
- Least possible value of $b$ is $3$
- Want to find the greatest possible value of $\displaystyle\left(a+\frac{1}{b}\right)\left(\frac{1}{b}-a\right)$, where $a = -2$ and $b = 3$
- Want to find the greatest possible value of $\displaystyle\left(-2+\frac{1}{3}\right)\left(\frac{1}{3}-(-2)\right)$
- Want to find the greatest possible value of $\displaystyle\left(-2+\frac{1}{3}\right)\left(\frac{1}{3}+2\right)$
- Want to find the greatest possible value of $\displaystyle\left(\frac{-5}{3}\right)\left(\frac{7}{3}\right)$
- Want to find the greatest possible value of $\displaystyle-\frac{35}{3} \cdot \frac{7}{3}$
- Want to find the greatest possible value of $\displaystyle\frac{-5}{3} \cdot \frac{7}{3}$
- Want to find the greatest possible value of $\displaystyle\frac{-35}{9}$
- The greatest possible value of $\displaystyle\left(a+\frac{1}{b}\right)\left(\frac{1}{b}-a\right)$, where $-6 \le a \le -2$ and $3 \le b \le 5$ is $\boxed{-\frac{25}{9}}$
- Output: #### $-\frac{-25}{9}$ (incorrect)

Attempt 27:
- Want to find the greatest possible value of $\displaystyle\left(a+\frac{1}{b}\right)\left(\frac{1}{b}-a\right)$
- Want to find the greatest possible value of $\displaystyle\left(a+\frac{1}{b}\right)\left(\frac{1}{b}-a\right)$, where $-6 \le a \le -2$ and $3 \le b \le 5$
- Let's start by finding the greatest possible value of $a$ and the smallest possible value of $b$
- Greatest possible value of $a$ is $-2$
- Smallest possible value of $b$ is $3$
- Want to find the greatest possible value of $\displaystyle\left(a+\frac{1}{b}\right)\left(\frac{1}{b}-a\right)$, where $a = -2$ and $b = 3$
- Want to find the greatest possible value of $\displaystyle\left(-2+\frac{1}{3}\right)\left(\frac{1}{3}-(-2)\right)$
- Want to find the greatest possible value of $\displaystyle\left(-2+\frac{1}{3}\right)\left(\frac{1}{3}+2\right)$
- Want to find the greatest possible value of $\displaystyle\left(\frac{-5}{3}\right)\left(\frac{7}{3}\right)$
- Want to find the greatest possible value of $\displaystyle-\frac{35}{9} \cdot \frac{7}{3}$
- Want to find the greatest possible value of $\displaystyle-\frac{5}{3}\cdot$
- States: $\displaystyle-\frac{5}{3}\cdot \frac{7}{3} = \frac{-35}{9}$
- The greatest possible value of $\displaystyle\left(a+\frac{1}{b}\right)\left(\frac{1}{b}-a\right)$, where $-6 \le a \le -2$ and $3 \le b \le 5$ is $\boxed{-\frac{-35}{9}}$
- Output: #### $-\frac{35}{9}$ (correct)

Key observations across examples:
- The revision model demonstrates self-correction capabilities across multiple attempts
- Common error types include: arithmetic mistakes in final calculations, incorrect problem-solving approaches, and formatting errors
- The model often gets closer to correct solution with each revision
- Some problems require fundamental strategy changes (Example 18), while others need only computational corrections (Example 17, 19, 20)
- Base conversion problems (Figures 19, 20) show the model struggling with proper notation and conversion logic across multiple attempts
- Coordinate conversion (Figure 21) shows confusion about the fundamental formulas before getting them right
- Number theory problem (Figure 22) shows arithmetic errors in summing divisors that are corrected on retry
- Algebraic manipulation (Figure 23) shows small arithmetic errors ($\frac{1}{3} + 2$ miscalculation) that are corrected
