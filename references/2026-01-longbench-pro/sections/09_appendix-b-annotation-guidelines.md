# Appendix B. Annotation Guidelines [p. 21-26]

[p. 21-23] Appendix B describes the end-to-end annotation protocol used to construct benchmark samples.

## B.1 Sample-Generation Prompt [p. 21-22]

The generation prompt instructs annotators/models to:
- identify source language and keep all outputs language-consistent,
- generate 3 questions per input that satisfy secondary-task constraints,
- provide answer, design rationale, and step-by-step solution for each question,
- enforce unique/verifiable identifiers (natural preferred; constructed if needed),
- include plausible distractors for MCQ tasks,
- provide three reference summaries for summarization tasks.

Required quality checks before acceptance include task compliance, answer verifiability, ambiguity avoidance, difficulty adequacy, and domain-linguistic correctness.

## B.2 Sample Verification Criteria [p. 22-23]

Human-model collaborative verification uses three checks:
- **Task A:** question compliance with task/context requirement.
- **Task B:** answer correctness grounded in document and reasoning trace.
- **Task C:** challenge level (must fail on at least one of five frontier models).

Candidate outcomes:
- pass and keep,
- edit then keep,
- reject and regenerate.

Explicit prohibitions include fabricated facts, hallucinated justification, subjective/unverifiable questions, and overly trivial prompts.

## B.3 Sample Rewriting Criteria [p. 23-24]

Appendix B standardizes prompt rewriting into two fixed templates:
- **Non-Thinking Prompt:** direct answer with `[Answer]` then required elements.
- **Thinking Prompt:** explicit reasoning first, then `[Answer]` output block.

Mandatory structure has 3 parts:
1. task description + output requirement,
2. optional supplementary context,
3. output example (format-only, not true answer).

## B.4 Answer Review Criteria [p. 25]

Answer review combines:
- human precision (component correctness),
- model-supported recall (missing answer components).

Two annotators independently review; expert adjudication resolves disagreements and decides whether reconstruction is required.

## B.5 Sample Quality Evaluation Criteria [p. 25-26]

Five scoring dimensions (each scored at {0, 0.5, 1}):
1. Task Alignment
2. Context Requirement Alignment
3. Difficulty
4. Authenticity
5. Answer Correctness

Scoring protocol:
- 3 experts score independently.
- Final score per dimension is mean across experts.
- Scoring requires written rationale and consistency across ambiguous cases.
