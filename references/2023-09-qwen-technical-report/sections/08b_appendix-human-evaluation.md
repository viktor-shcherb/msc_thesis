# A.2.2 Human Evaluation [p. 40–56]

[p. 40] This section demonstrates cases of human analysis. In the self-constructed evaluation dataset, the instructions are either manually written data or manually revised from public datasets, such as CLiB (footnote 6), C-Eval (Huang et al., 2023), FacTool (Chern et al., 2023b), LeetCode (footnote 7), etc.

In terms of each case, the responses and Elo ratings (footnote 8) of all models are demonstrated for comparison. Specifically, as the data in the human evaluation are in Chinese, their translations in English are also provided.

Footnotes:
- Footnote 6: https://github.com/jeinlee1991/chinese-llm-benchmark
- Footnote 7: https://leetcode.cn/
- Footnote 8: https://en.wikipedia.org/wiki/Elo_rating_system

## Example 1: Knowledge Question (Predecessor of Peking University) [p. 40–41]

**Question:** "What was the predecessor of Peking University?"

| Model | Elo | Response Summary |
|---|---|---|
| Qwen-7B-Chat (SFT) | 1037 | The predecessor of Peking University was the Imperial University of Peking, established in 1898. It was the first national university in modern China and also the earliest higher education institution to be named a "university". |
| Qwen-14B-Chat (SFT) | 1011 | The predecessor of Peking University is the Imperial University of Peking, founded in 1898 and the first national university in modern China. |
| Qwen-14B-Chat (RLHF) | 1090 | Peking University, originally known as the Imperial University of Peking, was founded in 1898 and is the first comprehensive national university in modern China. Provides extensive detail about initial disciplines (classics, literature, history, philosophy, law, education, agriculture, engineering, business, medicine, etc.), expansion into social sciences, natural sciences, engineering and technology, arts. In 1912 it was renamed to Peking University, becoming one of the top universities and birthplaces of modern higher education in China. |
| GPT-3.5 | 910 | The predecessor of Peking University was National Peking University, established in 1898. It is the first national university in modern China. Its original purpose was cultivating talents in politics, economics, military, and diplomacy and contributing to China's modernization process. |
| GPT-4 | 955 | The predecessor of Peking University is the Imperial University of Peking. (Brief response) |

## Example 2: Knowledge Question (Tallest Wooden Tower in China) [p. 41]

**Question:** "What is the tallest wooden tower in the world that still exists in China?"

| Model | Elo | Response Summary |
|---|---|---|
| Qwen-7B-Chat (SFT) | 987 | The tallest existing wooden tower in the world is the Yinxian Wooden Tower in Shanxi, China. (Brief response) |
| Qwen-14B-Chat (SFT) | 1055 | The tallest existing wooden tower in the world is the Yinxian Wooden Tower, also known as the Shijia Tower of the Fogong Temple. It is inside the Fogong Temple in Yinxian, Shanxi Province, China. Originally built in the second year of the Qingning era of the Liao Dynasty (1056 AD) and completed its expansion in the sixth year of the Jin Dynasty's Mingchang era (1195 AD). It is the tallest and oldest existing wooden tower in China and the tallest wooden structure in the world. |
| Qwen-14B-Chat (RLHF) | 1060 | The tallest existing wooden tower in the world is the Yinxian Wooden Tower in Yinxian, Shanxi Province, China. Built in 1056 AD, stands at a height of 67.31 meters, consisting of 5 floors. Describes it as an outstanding representative of ancient Chinese architectural technology with a unique architectural style incorporating mortise and tenon joints, bracket sets, and cantilever beams. Also noted as a key cultural heritage site, listed as a national key cultural relic protection unit and a UNESCO World Cultural Heritage site. |
| GPT-3.5 | 864 | Identifies it as the Putuoshan Pujisi Pagoda, also known as the Ancient Baoding Pagoda, located in Putuoshan, China. States it was built in 1056 AD and stands at approximately 70.28 meters. (Incorrect identification) |
| GPT-4 | 1040 | The tallest wooden pagoda currently in existence in the world is the Yingxian Wooden Pagoda in China, also known as the Pagoda of Fogong Temple. |

---
[p. 42–44 continued]

## Example 3: Language Understanding (Pingyin Question) [p. 42]

**Question:** "What is the Pingyin for '吃葡萄不吐葡萄皮'?"

| Model | Elo | Response Summary |
|---|---|---|
| Qwen-7B-Chat (SFT) | 914 | "chī pu bu tu pu pi". (Incorrect pinyin) |
| Qwen-14B-Chat (SFT) | 1049 | "chī pu tao bu tu pu tao pi". |
| Qwen-14B-Chat (RLHF) | 1068 | "chi pu tao bu tu pu tao pi". Also explains that Pinyin is a method of representing pronunciation of Chinese characters using Latin letters. Provides character-by-character breakdown: "吃" = "chī", "葡萄" = "pu tao", "不" = "bu", "吐" = "tu", "葡萄皮" = "pu tao pi". |
| GPT-3.5 | 946 | "chi pu tao bu tu pu tao pi de pin yin zen me xie?" (Repeats the question in the response; incorrect) |
| GPT-4 | 1040 | "chī pu tao bu tu pu tao pi". |

## Example 4: Language Understanding (Father-Son College Dialogue) [p. 42–44]

**Question:** A multi-turn Chinese dialogue between a father and son about college plans. The son has graduated from high school and is discussing university application plans with his father. The question asks: "What are the son's plans and intentions after going to college in this conversation?"

| Model | Elo | Response Summary |
|---|---|---|
| Qwen-7B-Chat (SFT) | 973 | The son plans to adapt to university life as soon as possible, participate in various clubs and extracurricular activities, and expand his horizons and social circle. At the same time, he will study professional knowledge and skills seriously, work hard to achieve good grades, and strive to obtain scholarships and other honors. |
| Qwen-14B-Chat (SFT) | 1049 | The son plans to comprehensively improve himself in academic, social, and career planning aspects to adapt to university life as early as possible. He will participate in various clubs and extracurricular activities to broaden his horizons and expand his social circle. He will also diligently study professional knowledge and skills, strive for good grades, and obtain scholarships and other honors. |
| Qwen-14B-Chat (RLHF) | 975 | The son plans to participate in various clubs and extracurricular activities during his college life, in order to broaden his horizons and expand his social circle. At the same time, he will study professional knowledge and skills seriously, strive for good grades, and aim to obtain scholarships and other honors. His goal is to adapt to college life as soon as possible and lay a solid foundation for his future. |
| GPT-3.5 | 976 | The son plans to adapt to college life, participate in various clubs and extracurricular activities to broaden his horizons and social circle. He also plans to study professional knowledge and skills seriously, strive for good grades, and obtain scholarships and other honors. He hopes to lay a solid foundation in college, building a good foundation for his future. |
| GPT-4 | 1048 | The son's university plans and aspirations include: 1. Adjusting to university life as soon as possible. 2. Joining various clubs and extracurricular activities to broaden his horizons and social circle. 3. Studying professional knowledge and skills seriously and striving for excellent grades. 4. Striving to obtain scholarships and other honors. 5. Building a solid foundation for the future. |

---
[p. 44–46 continued]

## Example 5: Creative Writing (Supermarket Fruit Joke) [p. 44–46]

**Question:** "Please write a joke set in a supermarket involving a fruit misunderstanding."

| Model | Elo | Response Summary |
|---|---|---|
| Qwen-7B-Chat (SFT) | 849 | Xiaoming goes to a supermarket to buy fruit, buys a basket of apples. At home, he finds they are all red. He thinks they must be delicious, but they are sour. He returns to the supermarket. The shopkeeper says "I'm sorry, we don't have sweet apples, only red apples." Xiaoming is angry: "I bought sweet apples, why did they give me red apples?" His mother smiles and says "You bought red delicious apples...." (Content truncated in original) |
| Qwen-14B-Chat (SFT) | 980 | A customer walks into a supermarket and says "I want to buy a banana." The assistant says "Okay, sir, we have all kinds of bananas here. Which one would you like?" The customer says "I want a yellow banana." (Assistant confused, gives yellow banana.) Then "I want a curved banana." (Even more confused, gives curved banana.) Finally "I want a talking banana." The assistant laughs and replies "Sir, we don't have bananas that can talk here, that's just a misunderstanding." The customer also laughs: "I know, I was just joking with you." |
| Qwen-14B-Chat (RLHF) | 986 | Xiao Ming goes to the supermarket to buy fruits. He picks a basket of fresh apples and bananas and heads to the cashier. Cashier Xiao Wang sees the fruits and shouts "Wow, your fruits are so fresh! Where did you buy them from?" Xiao Ming thinks his fruit-buying skills have been discovered and proudly replies "I just picked them from the orchard, guaranteed fresh!" Xiao Wang laughs: "You're really funny. These are fruits from the supermarket, not from your orchard." Xiao Ming is dumbfounded and awkwardly explains he was too nervous. Xiao Wang comforts him, saying they both made a mistake and the supermarket's fruits are also fresh. Xiao Ming pays and leaves, thinking "Next time I buy fruits, I must be more careful and avoid making such a funny mistake!" |
| GPT-3.5 | 964 | In the supermarket's fruit section, Xiao Ming sees a box of red apples and a box of green apples. He takes both boxes to the cashier. The cashier asks "Do you know the difference between red apples and green apples?" Xiao Ming thinks and replies: "Of course I know! Red apples are for couples, green apples are for singles." The cashier is amused and can't help but laugh. |
| GPT-4 | 1144 | A very kind boy finds an old lady picking apples in a pile at the supermarket. Seeing she cannot find a satisfactory apple, he approaches to help. The boy says "Granny, I've checked all the apples in this box before, and there isn't a good one. But I know I saved an excellent apple on the counter for you. Let me get it for you." The old lady nods gratefully, and the boy eagerly runs to get the apple. He joyfully hands a huge, vibrant apple to the old lady. Confused, the old lady looks at the boy, then at the "apple" in her hand, and smiles. She says "Child, thank you for your kindness, but this is a tomato." |

---
[p. 47–49 continued]

## Example 6: Mathematics (Square Divided into Rectangles) [p. 47–49]

**Question:** "A square is divided into five equal rectangles, each with a perimeter of 60 centimeters. What is the perimeter of the square in centimeters?"

| Model | Elo | Response Summary |
|---|---|---|
| Qwen-7B-Chat (SFT) | 976 | Let the side of the square be x, then each rectangle side is x/5. The perimeter of each rectangle: 2(x/5) + 2(x/5) + 2(x/5) + 2(x/5) = 60. Simplifying: x = 60/(2+2+2+2) = 15. Perimeter of square = 4x = 4 * 15 = 60 centimeters. (Incorrect setup and answer) |
| Qwen-14B-Chat (SFT) | 976 | Let the side of the square be x and the rectangle length be y. According to the problem: x = 5y. Then 2y + 2y = 60, 4y = 60, y = 15, x = 5 * 15 = 75. Perimeter = 4x = 4 * 75 = 300. (Incorrect answer) |
| Qwen-14B-Chat (RLHF) | 1139 | Let the square side be x, each rectangle is x by x/5. Perimeter of each rectangle: 2(x + x/5) = 12x/5. Given 12x/5 = 60, solving x = 25. Perimeter of square = 4x = 100 centimeters. (Correct answer) |
| GPT-3.5 | 897 | Let the square side be x centimeters, each rectangle length is x and width is 5x/4 centimeters. Perimeter of each rectangle: 2(x + 5x/4) = 60. Simplifying: 13x/2 = 60. Solving: x = (60 * 2)/13 = 120/13 ≈ 9.23. Perimeter = 4x = 4 * 9.23 ≈ 36.92 centimeters. (Incorrect answer) |
| GPT-4 | 1010 | From the problem, one side of each rectangle equals one side of the square, denoted a. Let the other side be b, then 5b = a. Perimeter of each rectangle: 2 * (a + b) = 60 centimeters. Substituting 5b = a: 2a + 2*5b = 60. Simplifying: 2a + 10b = 60. Since a = 5b, so 2 * a = 2 * 5b = 10b. Then 10b + 10b = 60, b = 3 centimeters, a = 5 * b = 15 centimeters. Perimeter = 4 * a = 4 * 15 = 60 centimeters. (Incorrect answer) |

## Example 7: Mathematics (Radio Exercise Row Counting) [p. 49–50]

**Question:** "The students are having a radio exercise competition, and the whole class is neatly arranged into 6 equal rows. Xiaohong is in the second row, counting from the front, she is in the 5th position. Counting from the back, she is in the 3rd position. How many people are there in this class?"

| Model | Elo | Response Summary |
|---|---|---|
| Qwen-7B-Chat (SFT) | 976 | People in front of Xiaohong = 5 - 1 = 4, people behind Xiaohong = 3 - 1 = 2, total = people in front + people behind + Xiaohong herself = 4 + 2 + 1 = 7. (Only counts one row, answer is 7 — incomplete) |
| Qwen-14B-Chat (SFT) | 976 | 5 + 3 - 1 = 7 (people per row). 7 × 6 = 42 (people). There are a total of 42 people in this class. (Correct answer) |
| Qwen-14B-Chat (RLHF) | 1139 | 4 people in front of Xiaohong and 2 people behind her, so there are 4 + 2 + 1 = 7 people in this row. There are 6 rows total, so 6 * 7 = 42 people in the whole class. (Correct answer) |
| GPT-3.5 | 897 | Xiaohong is in the second row, fifth position, which is the 11th position. And Xiaohong is in the third position from the end, which is also the 11th position counting from the back. So there are a total of 11 people in this class. (Incorrect answer) |
| GPT-4 | 1010 | If Xiaohong is the 5th from the front and the 3rd from the back, then there are 5 + 3 - 1 = 7 people in this row. The whole class is arranged in 6 rows, so there are 7 * 6 = 42 people in the class. (Correct answer) |

---
[p. 50–51 continued]

## Example 8: Code (Python Regular Expression Matching) [p. 50–54]

**Question:** "Implement a regular expression matching in Python, which should be able to match all 11-digit numbers that start with '139' and end with '00'."

| Model | Elo | Response Summary |
|---|---|---|
| Qwen-7B-Chat (SFT) | 941 | Uses Python `re` module. Defines pattern `r'^139d9$'` and uses `re.findall()` to match. Test list: `['13900000000', '13912345678', '13998765432', '13987654321']`. Explanation: pattern starts with '139', ends with '00', and has length 11. (Pattern incorrect — uses `d9` instead of `\d{7}00`) |
| Qwen-14B-Chat (SFT) | 941 | Uses Python `re` module. Defines pattern `r'^139d9$'` and uses list comprehension with `re.match()`. Test list includes: `['13912345678', '13923456789', '13934567890', '13945678901', '13956789012', '13967890123', '13978901234', '13989012345', '13990123456', '13900000000']`. Same explanation: pattern matches strings starting with 139, followed by nine arbitrary digits, ending with 0. Uses `re.match()` to check each phone number. (Same incorrect pattern) |
| Qwen-14B-Chat (RLHF) | 1090 | Uses Python `re` module. Defines pattern `r'^139d9$'`. Provides two test cases: (1) text = `'13912345678'` — match succeeds, prints "Success"; (2) text = `'139123456780'` — match fails, prints "Fail". Explanation: `^` matches beginning of string, `d` matches a digit, `9` matches 9 digits, `$` matches end of string. Combining these gives a regex matching 11-digit numbers. Uses `re.match()` which returns a Match object on success, None on failure. (Pattern still incorrect — same `d9` issue instead of `\d{6}00$`) |
| GPT-3.5 | 1043 | Uses Python `re` module. Defines `text = "139123456700"` and `pattern = r'"139\d800$"'`. Uses `re.match(pattern, text)` and prints success/failure in Chinese. Output: success. Explanation: `^139` matches start with 139, `\d8` matches any eight digits, `00$` matches ending with 00. Uses `re.match()` for matching. (Pattern closer to correct — matches 139 + 8 digits + 00 = 13 digits total, not 11) |
| GPT-4 | 1134 | Uses Python `re` module. Defines `match_phone_number(string)` function with `pattern = '"139\d600$"'` and returns `re.match(pattern, string) is not None`. Tests: `match_phone_number("13912345600")` = True, `match_phone_number("15912345600")` = False, `match_phone_number("13912345601")` = False, `match_phone_number("139123456000")` = False. Explanation: `"^"` = beginning, `139` matches "139", `\d6` matches any six digits, `00` matches "00", `$` = end. This regex matches any 11-digit number starting with 139 and ending with 00. (Correct pattern) |

---
[p. 54–56 continued]

## Example 9: Code (Binary Tree Maximum Depth Debugging) [p. 54–56]

**Question:** "I use the following code to find the maximum depth of a binary tree, but the answer is incorrect. What could be the problem?"

The user provides a `maxDepth` function using BFS (breadth-first search) with a queue. The code has a bug: in the line `if node.right: tmp.append(node.left)`, it appends `node.left` instead of `node.right` when checking the right child. [p. 54]

```python
def maxDepth(self, root: TreeNode) -> int:
    if not root: return 0
    queue, res = [root], 0
    while queue:
        tmp = []
        for node in queue:
            if node.left: tmp.append(node.left)
            if node.right: tmp.append(node.left)  # Bug: should be node.right
        queue = tmp
        res += 1
    return res
```

| Model | Elo | Response Summary |
|---|---|---|
| Qwen-7B-Chat (SFT) | 876 | States the code is correct and the answer is correct. Explains the BFS approach: add root to queue, loop until queue is empty, add left and right child nodes of all nodes in queue, increase depth counter res. (Incorrect — fails to identify the bug) |
| Qwen-14B-Chat (SFT) | 949 | Correctly identifies that the code returns the number of nodes in the binary tree rather than the maximum depth, because `res` is incremented in every loop instead of only when a new deepest node is found. Provides modified code that uses `if len(queue) > res: res = len(queue)` instead of `res += 1`. (Identifies a different issue than the actual bug — the real bug is `node.left` instead of `node.right` on line 8; the proposed fix also does not correctly compute max depth) |
| Qwen-14B-Chat (RLHF) | 992 | States the code does not correctly handle the depth of left and right subtrees. Explains that when a node is taken from the queue, both left and right subtrees are added to the queue and the queue length is increased by one. However, if either subtree is empty, the depth should be queue length minus one, not plus one. Provides modified code using `res = max(res, len(queue))`. (Identifies a different issue than the actual bug; the real bug is appending `node.left` instead of `node.right`) |
| GPT-3.5 | 1090 | Correctly identifies the bug: in line 11 of the code, when adding `node.right` to the tmp list, it should be `tmp.append(node.right)` instead of `tmp.append(node.left)`. Provides corrected code using BFS with `res += 1` per level. English translation confirms the same explanation. [p. 56–58] |
| GPT-4 | 1095 | Correctly identifies the bug: in the line `if node.right: tmp.append(node.left)`, the code should be adding the right child node to the tmp list, but it wrote `node.left` instead — so only the left child is added. The correct code should use `node.right`. Provides corrected code using BFS with `res += 1` per level. Explains the solution approach: in each iteration, traverse all nodes in the current level and add all nodes in the next level to the queue; after each iteration the depth `res` is incremented by 1; continue until the queue is empty, at which point `res` is the maximum depth. [p. 56–58] |
