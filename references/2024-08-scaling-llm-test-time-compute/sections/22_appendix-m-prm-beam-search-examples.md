# Appendix M. PRM Beam Search Example Outputs [p. 28, 36–37]

[p. 28] In Figures 24, 25, 26, 27, 28, and 29, they include select examples of PRM beam search. They include the PRM score, between 0 and 1, for each step in the examples.

---
[p. 36 continued]

**Figure 24** (p. 36): PRM beam search example 1.

Description: Example showing an infinite geometric sequence problem with PRM scores

Problem: "The sum of the first $n$ terms in the infinite geometric sequence $\{1,\frac{1}{3},\frac{1}{9},\frac{1}{27},\dots\}$ is $\frac{121}{81}$. Find $n$."

Solution shown with PRM scores at each step:
- "Add up the first $n$ terms in the sequence as just $\frac{1}{3^0}+\frac{1}{3^1}+...$ where $a$ is the first term in the sequence and $r$ is the common ratio. [score = 0.005]"
- "Add up the first $n$ terms of the first $n$ terms in this particular sequence and set it equal to $\frac{121}{81}$, we get $n=\boxed{7}$. [score = 0.11]"
- "Right, so we can set $\frac{1-(\frac{1}{3})^n}{1-\frac{1}{3}} \cdot \frac{1}{1-(\frac{1}{3})} = \frac{49}{81}$ and solve for $n$. [score = 0.16]"
- "So we get $n=7$. [score = 0.15]"
- "And we know that $\frac{1-(\frac{1}{3})^n}{1-\frac{1}{3}}=\frac{121}{81}$." [score = 0.15]
- "So, $1-\left(\frac{1}{3}\right)^n\cdot\frac{3}{2} = \left(\frac{121}{81}\right)$. [score = 0.15]"
- "away 7 [score = 0.38]"

**Figure 25** (p. 36): PRM beam search example 2.

Description: Example showing an infinite geometric sequence problem with PRM scores

Problem: "The sum of the first $n$ terms in the infinite geometric sequence $\{1,\frac{1}{3},\frac{1}{9},\frac{1}{27},\dots\}$ is $\frac{121}{81}$. Find $n$."

Solution shown with PRM scores at each step:
- "Since the common ratio is each term is $\frac{1}{3}$, the sum of the first $n$ terms of this sequence is $\frac{1-(\frac{1}{3})^n}{1-\frac{1}{3}} = \frac{a(1-r^n)}{1-r}$, where $a$ is the first term and $r$ is the common ratio. [score = 0.07]"
- "So, the sum of the first $n$ terms of this geometric sequence is $\frac{1-(\frac{1}{3})^n}{1-\frac{1}{3}}\left[\frac{1}{3^0}+\frac{1}{3^1}+\frac{1}{3^2}+...+\frac{1}{3^{n-1}}\right]$. [score = 0.09]"
- "So, the sum of the first $n$ terms of this geometric sequence is $\frac{1-(\frac{1}{3})^n}{1-\frac{1}{3}}\left[\frac{1}{3^0}+\frac{1}{3^1}+\frac{1}{3^2}+...+\frac{1}{3^{n-1}}\right]\left[\frac{1}{3^{n-1}}\right]$. [score = 0.1]"
- "We can multiply both sides by 2. [score = 0.18]"
- "We have $\frac{2}{3}\left(1-\left(\frac{1}{3}\right)^n\right)=\frac{121}{81}$. [score = 0.34]"
- "We have $1-\left(\frac{1}{3}\right)^n = \frac{121}{54}$. [score = 0.39]"
- "So, $\left(\frac{1}{3}\right)^n = 1-\frac{121}{54}$. [score = 0.45]"
- "So, $\left(\frac{1}{3}\right)^n = \frac{-67}{54}$ [score = 0.05]"
- "Right. And since the bases are the same, the exponents must be equal. [score = 0.03]"

**Figure 26** (p. 36): PRM beam search example 3.

Description: Example showing an algebraic equation problem with PRM scores

Problem: "$441+2(21)(19)+361=x$. Solve for $x$."

Solution shown with PRM scores at each step:
- "We know that $x=2(21)(19)+361$. [score = 0.33]"
- "We can factor $21(19)=21(20-1)$. [score = 0.04]"
- "So we get $1(21)=21$. [score = 0.06]"
- "So we get $x=2(0)=0$. [score = 0.06]"
- "And we know that $x=1600$. [score = 0.91]"
- "That's our answer. [score = 0.91]"
- "Right. So $x=1600$. [score = 0.94]"
- "Right. So $441+2(21)(19)+361=1600$. [score = 0.94]"
- "True [sic] [score = 0.94]"

**Figure 27** (p. 36): PRM beam search example 4.

Description: Example showing a geometry problem with PRM scores

Problem: "Determine the coordinates of the point $P$ on the line $y=x+4$ such that $P$ is equidistant from the points $A(10,-10)$ and $Q(0,0)$ (that is, so that $PA=PQ$). Express your answer as an ordered pair $(a,b)$."

Solution shown with PRM scores at each step:
- "So we're given the line $y=x+4$ and we want to find the point on this line where the line segment from that point to the point with coordinates $(10,-10)$ is the same length as the line segment from the point to the origin. [score = 0.67]"
- "Right. In one way to do that is to use the distance formula. Let's find the distance between $P$ and $(10,-10)$ and the distance between $P$ and the origin. [score = 0.81]"
- "We know that the distance between $P$ and $(10,10)$ will be the square root of $(x-10)^2+(y+10)^2$." [score = 0.67]
- "But since $P$ is on the line $y=x+4$ from both sides in in [sic] square root of $(x-10)^2+(x+4-(-10))^2$ which is the square root of $(x-10)^2+(x+14)^2$ [score = 0.46]"
- "So the two distances must be equal. So $\sqrt{(x-10)^2+(x+4+10)^2} = \sqrt{x^2+y^2}$. [Expanding the left-side gives $x-10)^2+(x+14)^2$. [score = 0.46]"
- "But we can subtract $x$ on $y$ from both sides in in [sic] square root of $(x-10)^2+(x+4)^2$ and then we have, so we can get the square root of $(x-10)^2+(x+14)^2=\sqrt{x^2+y^2}$. [score = 0.46]"
- "So the two distances must be equal. So $\sqrt{(x-10)^2+(x+14)^2}=\sqrt{x^2+(x+4)^2}$. Then we can subtract $2$ on both sides to get $x-x+y^2$. [score = 0.12]"
- "So $(x-10)^2+(x+14)^2=x^2+(x+4)^2$. Divide both sides by $2$ to get $x-7y^2$. [score = 0.12]"
- "So $x=\frac{-7}{2}$. [score = 0.12]"
- "And $y=x+4$. So if we substitute $x$ for $x-8$ we get $y=\frac{-8}{2}$. [score = 0.05]"
- "So the point $P$ is $(-7,8)$. [score = 0.13]"
- "So the point $P(x,-7)$ is equidistant from the line points. [score = 0.1]"
- "On the point $(-6,-7)$ is equidistant from the line points. [score = 0.11]"
- "That's correct. [score = 0.31]"
- "Right. So $|score = 0.31]"

---
[p. 37 continued]

**Figure 28** (p. 37): PRM beam search example 5.

Description: Example showing a geometry problem (same problem as Figure 27, different solution attempt) with PRM scores

Problem: "Determine the coordinates of the point $P$ on the line $y=x+4$ such that $P$ is equidistant from the points $A(10,-10)$ and $Q(0,0)$ (that is, so that $PA=PQ$). Express your answer as an ordered pair $(a,b)$."

Solution shown with PRM scores at each step:
- "So we're given the line $y=x+4$ and we need to find the point on that line where the line segment from that point to the point with coordinates $(10,-10)$ is the same length as the line segment from the point to the origin. [score = 0.81]"
- "Right. We know that the distance formula for two points $(x_1,y_1)$ and $(x_2,y_2)$ is $\sqrt{(x_2-x_1)^2+(y_2-y_1)^2}$. Let's find the distance between $P$ and $(10,-10)$ and the distance between $P$ and the origin. [score = 0.81]"
- "We know that the distance formula for $P$ and $(10,-10)$ will be $\sqrt{(x-10)^2+(y-(-10))^2}$ which is the square root of $(x-10)^2+(y+10)^2$. And the distance from $P$ and the origin will be the square root of $x^2+y^2$. [score = 0.60]"
- "So the two distances must be equal. So $\sqrt{(x-10)^2+(y+10)^2} = \sqrt{x^2+y^2}$. Expanding the left side gives $x-10)^2+(x+14)^2$. [score = 0.60]"
- "But we know that $y=x+4$. So $\sqrt{(x-10)^2+(x+14)^2} = \sqrt{x^2+(x+4)^2}$. Expanding from both sides in in [sic] $x^2-20x+100+x^2+28x+196 = x^2+x^2+8x+16$. [score = 0.03]"
- "But we know that $y=x+4$. So we can substitute that value into the equation $x^2-20x+100+x^2+28x+196 = x^2+x^2+8x+16$. Then we can combine the terms to get $x^2-8x+y^2-40x+200 = x^2+40x+16$. Then we can subtract $2$ on both sides to get $x^2-8x+y^2-40x+200 = x^2+40x+16$. [score = 0.03]"
- "Then we can $(x-10)^2+x$ to get $x^2+y^2-40x+200 = x^2+40x+16$. Then we can subtract $2$ on both sides to get $x^2+y^2-40x+200 = x^2+40x+16$. [score = 0.12]"
- "And we know that $y=x-7+40$. Then we can substitute that value into the equation $y=x+y+40$ to find $y=-7+40$. That gives $y=x+y-40$ which simplifies to $y=x+y-40$. [score = 0.30]"
- "away 3 [score = 0.12]"

**Figure 29** (p. 37): PRM beam search example 6.

Description: Example showing a word problem with PRM scores

Problem: "If 4 days = 7 yaps, and 5 yaps = 3 baps, how many days equal 42 baps?"

Solution shown with PRM scores at each step:
- "We can start by converting 42 baps to yaps. [score = 0.81]"
- "And 5 yaps is equal to 3 baps, so that means that 1 yap is equal to 3/5 baps or 6.5 baps. [score = 0.61]"
- "And we can plug these values in to find the answer. [score = 0.11]"
- "And we can convert 42 baps to yaps. [score = 0.07]"
- "And 70 yaps is equal to 70/5 days or 14 days. [score = 0.07]"
- "So the answer is $\boxed{40}$. [score = 0.12]"
- "Right. So the answer is 42 baps. [score = 0.09]"
- "And that is our final answer. [score = 0.90]"
- "Right. So the answer is 42 baps. [score = 0.00]"
- "And that is our final answer. [score = 0.98]"
- "[score = 0.91]"
- "away 10 [score = 0.61]"

Key observations across PRM beam search examples:
- PRM scores (0 to 1) are shown for each reasoning step
- Higher scores indicate steps the model considers more likely to be correct
- Examples show both successful reasoning paths (Figure 26 with scores reaching 0.94) and unsuccessful attempts (Figure 24, 25, 27 with lower scores)
- The beam search explores multiple solution strategies, with PRM scores guiding which paths to pursue
- Errors in reasoning steps are reflected in lower PRM scores (e.g., Figure 27 shows declining scores as the solution goes off track)
- Figure 26 demonstrates the clearest example where PRM scores correlate with solution quality, jumping from low scores (0.04-0.06) to high scores (0.91-0.94) when finding the correct answer
- Figure 29 shows an interesting pattern where incorrect intermediate reasoning can still lead to high confidence scores (0.90-0.98) at the end
