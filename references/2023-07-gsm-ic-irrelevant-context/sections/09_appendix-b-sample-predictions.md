# B. Sample Predictions on GSM-IC [p. 14–16]

[p. 14] In addition to the example outputs shown in Figure 3, the paper includes more example problems and the predictions by different techniques (Tables 11 and 12).

**Table 11** (p. 15): Output example #1 for different prompting techniques, on a GSM8K problem and a corresponding GSM-IC problem. While all techniques give correct answers to the original problem, they output different results for the modified GSM-IC problem.

Original GSM8K Problem: "Jessica is six years older than Claire. In two years, Claire will be 20 years old. How old is Jessica now?"

Modified Problem (w/ Irrelevant Sentence): "Jessica is six years older than Claire. In two years, Claire will be 20 years old. Twenty years ago, the age of Claire's father is 3 times of Jessica's age. How old is Jessica now?"

| Method | Original GSM8K Problem | Modified Problem (w/ Irrelevant Sentence) |
|---|---|---|
| CoT | In two years, Claire will be 20 years old. So, Claire is 18 years old now. Jessica is six years older than Claire, so Jessica is 18 + 6 = 24 years old now. The answer is 24. | Jessica is six years older than Claire, so Jessica is 20 - 6 = 14 years old. Twenty years ago, the age of Claire's father is 3 times of Jessica's age, so 20 years ago, the age of Claire's father is 3 * 14 = 42 years old. The answer is 14. |
| LtM | Let's break down this problem: 1. How old is Claire now? 2. How old is Jessica now? 1. In two years, Claire will be 20 years old. So Claire is 20 - 2 = 18 years old now. 2. Jessica is six years older than Claire. So Jessica is 18 + 6 = 24 years old now. The answer is 24. | A: Let's break down this problem: 1. How old is Claire now? 2. How old is Jessica now? 1. In two years, Claire will be 20 years old. So Claire is 18 years old now. 2. Twenty years ago, the age of Claire's father is 3 times of Jessica's age. So 20 years ago, Claire's father is 3 * Jessica's age. So Claire's father is 3 * Jessica's age now. So Claire's father is 3 * Jessica's age - 20 years old now. So Claire's father is 3 * Jessica's age - 20 + 18 = 3 * Jessica's age - 2 years old now. So Claire's father is 3 * Jessica's age - 2 + 6 = 3 * Jessica's age + 4 years old now. So Claire's father is 3 * Jessica's age + 4 - 18 = 3 * Jessica's age - 14 years old now. So Claire's father is 3 * Jessica's age - 14 + 20 = 3 * Jessica's age + 6 years old now. So 3 * Jessica's age + 6 = 3 * Jessica's age - 2 + 6 = 3 * Jessica's age + 4. So 3 * Jessica's age + 6 = 3 * Jessica's age + 4. So 6 = 4. So Jessica's age = 2. So Jessica is 2 years old now. The answer is 2. |
| PROGRAM | Claire_age = 20 - 2 / Jessica_age = Claire_age + 6 / print(Jessica_age) | Claire_age = 20 - 2 / Jessica_age = Claire_age - 6 / Claire_father_age = 3 * Jessica_age / print(Jessica_age) |

**Table 12** (p. 16): Output example #2 for different prompting techniques, on a GSM8K problem and a corresponding GSM-IC problem. While all techniques give correct answers to the original problem, they output the same incorrect result for the modified GSM-IC problem.

Original GSM8K Problem: "Lucy has $65 in the bank. She made a $15 deposit and then followed by a $4 withdrawal. What is Lucy's bank balance?"

Modified Problem (w/ Irrelevant Sentence): "Lucy has $65 in the bank. She made a $15 deposit and then followed by a $4 withdrawal. Lucy's mother's monthly rent is $10. What is Lucy's bank balance?"

| Method | Original GSM8K Problem | Modified Problem (w/ Irrelevant Sentence) |
|---|---|---|
| CoT | Lucy has $65 in the bank. She made a $15 deposit, so she has $65 + $15 = $80. She then made a $4 withdrawal, so she has $80 - $4 = $76. The answer is $76. | Lucy has $65 in the bank. She made a $15 deposit and then followed by a $4 withdrawal. Lucy's mother's monthly rent is $10. Lucy's bank balance is $65 + $15 - $4 - $10 = $66. The answer is $66. |
| LtM | Let's break down this problem: 1. How much money did Lucy deposit? 2. How much money did Lucy withdraw? 3. How much money does Lucy have in the bank? 1. Lucy deposited $15. 2. Lucy withdrew $4. 3. Lucy has $65 + $15 - $4 = $76 in the bank. The answer is $76. | Let's break down this problem: 1. How much money did Lucy deposit? 2. How much money did Lucy withdraw? 3. How much money does Lucy have in the bank? 1. Lucy deposited $15. 2. Lucy withdrew $4. 3. Lucy has $65 + $15 - $4 - $10 = $66 in the bank. The answer is $66. |
| PROGRAM | Lucy_balance = 65 / Lucy_balance = Lucy_balance + 15 / Lucy_balance = Lucy_balance - 4 / print(Lucy_balance) | Lucy_bank = 65 / Lucy_bank = Lucy_bank + 15 / Lucy_bank = Lucy_bank - 4 / Lucy_bank = Lucy_bank - 10 / print(Lucy_bank) |

[p. 15-16] In Table 11, all techniques give correct answers to the original problem (24), but produce different incorrect results for the modified problem. CoT produces 14, LtM produces 2, and PROGRAM produces an incorrect result by changing `+ 6` to `- 6`. In Table 12, all techniques give the correct answer ($76) to the original problem but all produce the same incorrect answer ($66) for the modified problem, incorporating the irrelevant $10 monthly rent into the calculation.
