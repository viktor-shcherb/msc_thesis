# C. Full Prompts in Experiments [p. 17–18]

[p. 17–18] The prompts for all experiments are listed in Tables 13 and 14.

## Table 13: Prompts without instruction

**Table 13** (p. 17): Prompts used for all investigated techniques, without instruction. The placeholder [Problem of Interest] is substituted for each problem at the test time.

| Method | Example w/ IrrCtx? | Prompt |
|---|---|---|
| CoT | No | Q: Elsa has 5 apples. Anna has 2 more apples than Elsa. How many apples do they have together? A: Anna has 2 more apples than Elsa, so Anna has 2 + 5 = 7 apples. Elsa and Anna have 5 + 7 = 12 apples together. The answer is 12. Q: [Problem of Interest] A: |
| CoT | Yes | Q: Elsa has 5 apples. Anna has 2 more apples than Elsa. Liz has 4 peaches. How many apples do they have together? A: Anna has 2 more apples than Elsa, so Anna has 2 + 5 = 7 apples. Elsa and Anna have 5 + 7 = 12 apples together. The answer is 12. Q: [Problem of Interest] A: |
| LtM | No | Q: Elsa has 5 apples. Anna has 2 more apples than Elsa. How many apples do they have together? A: Let's break down this problem: 1. How many apples does Anna have? 2. How many apples do Elsa and Anna have together? 1. Anna has 2 more apples than Elsa. So Anna has 2 + 5 = 7 apples. 2. Elsa and Anna have 5 + 7 = 12 apples together. Q: [Problem of Interest] A: Let's break down this problem: |
| LtM | Yes | Q: Elsa has 5 apples. Anna has 2 more apples than Elsa. Liz has 4 peaches. How many apples do they have together? A: Let's break down this problem: 1. How many apples does Anna have? 2. How many apples do Elsa and Anna have together? 1. Anna has 2 more apples than Elsa. So Anna has 2 + 5 = 7 apples. 2. Elsa and Anna have 5 + 7 = 12 apples together. Q: [Problem of Interest] A: Let's break down this problem: |
| 0-CoT | N/A | Q: [Problem of Interest] A: Let's think step by step: |
| PROGRAM | No | Q: Elsa has 5 apples. Anna has 2 more apples than Elsa. How many apples do they have together? A: Let's solve the problem by a Python program: Elsa_apples = 5 / Anna_apples = 2 + Elsa_apples / Elsa_Anna_apples = Elsa_apples + Anna_apples / print(Elsa_Anna_apples) Q: [Problem of Interest] A: Let's solve the problem by a Python program: |
| PROGRAM | Yes | Q: Elsa has 5 apples. Anna has 2 more apples than Elsa. Liz has 4 peaches. How many apples do they have together? A: Let's solve the problem by a Python program: Elsa_apples = 5 / Anna_apples = 2 + Elsa_apples / Elsa_Anna_apples = Elsa_apples + Anna_apples / print(Elsa_Anna_apples) Q: [Problem of Interest] A: Let's solve the problem by a Python program: |

## Table 14: Prompts with instructions

**Table 14** (p. 18): All prompts with instructions. The placeholder [Problem of Interest] is substituted for each problem at the test time.

| Method | Example w/ IrrCtx? | Prompt |
|---|---|---|
| CoT | No | Solve grade school math problems. Feel free to ignore irrelevant information given in the questions. Q: Elsa has 5 apples. Anna has 2 more apples than Elsa. How many apples do they have together? A: Anna has 2 more apples than Elsa, so Anna has 2 + 5 = 7 apples. Elsa and Anna have 5 + 7 = 12 apples together. The answer is 12. Q: [Problem of Interest] A: |
| CoT | Yes | Solve grade school math problems. Feel free to ignore irrelevant information given in the questions. Q: Elsa has 5 apples. Anna has 2 more apples than Elsa. Liz has 4 peaches. How many apples do they have together? A: Anna has 2 more apples than Elsa, so Anna has 2 + 5 = 7 apples. Elsa and Anna have 5 + 7 = 12 apples together. The answer is 12. Q: [Problem of Interest] A: |
| LtM | No | Solve grade school math problems. Feel free to ignore irrelevant information given in the questions. Q: Elsa has 5 apples. Anna has 2 more apples than Elsa. How many apples do they have together? A: Let's break down this problem: 1. How many apples does Anna have? 2. How many apples do Elsa and Anna have together? 1. Anna has 2 more apples than Elsa. So Anna has 2 + 5 = 7 apples. 2. Elsa and Anna have 5 + 7 = 12 apples together. Q: [Problem of Interest] A: Let's break down this problem: |
| LtM | Yes | Solve grade school math problems. Feel free to ignore irrelevant information given in the questions. Q: Elsa has 5 apples. Anna has 2 more apples than Elsa. Liz has 4 peaches. How many apples do they have together? A: Let's break down this problem: 1. How many apples does Anna have? 2. How many apples do Elsa and Anna have together? 1. Anna has 2 more apples than Elsa. So Anna has 2 + 5 = 7 apples. 2. Elsa and Anna have 5 + 7 = 12 apples together. Q: [Problem of Interest] A: Let's break down this problem: |
| 0-CoT | N/A | Solve grade school math problems. Feel free to ignore irrelevant information given in the questions. Q: [Problem of Interest] A: Let's think step by step: |
| PROGRAM | No | Solve grade school math problems. Feel free to ignore irrelevant information given in the questions. Q: Elsa has 5 apples. Anna has 2 more apples than Elsa. How many apples do they have together? A: Let's solve the problem by a Python program: Elsa_apples = 5 / Anna_apples = 2 + Elsa_apples / Elsa_Anna_apples = Elsa_apples + Anna_apples / print(Elsa_Anna_apples) Q: [Problem of Interest] A: Let's solve the problem by a Python program: |
| PROGRAM | Yes | Solve grade school math problems. Feel free to ignore irrelevant information given in the questions. Q: Elsa has 5 apples. Anna has 2 more apples than Elsa. Liz has 4 peaches. How many apples do they have together? A: Let's solve the problem by a Python program: Elsa_apples = 5 / Anna_apples = 2 + Elsa_apples / Elsa_Anna_apples = Elsa_apples + Anna_apples / print(Elsa_Anna_apples) Q: [Problem of Interest] A: Let's solve the problem by a Python program: |
