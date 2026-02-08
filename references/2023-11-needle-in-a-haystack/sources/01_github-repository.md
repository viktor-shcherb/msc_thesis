# LLMTest_NeedleInAHaystack GitHub Repository [https://github.com/gkamradt/LLMTest_NeedleInAHaystack]

**Type:** github-repo
**Fetched:** 2026-02-08
**Priority:** primary

Repository metrics (as of fetch date): 2.2k stars, 233 forks, 8 contributors, MIT License. Languages: Jupyter Notebook (89.4%), Python (10.6%).

---

## Methodology

The README describes the test as:

> A simple 'needle in a haystack' analysis to test in-context retrieval ability of long context LLMs.

The test follows three steps:

1. Place a random fact or statement (the "needle") in the middle of a long context window (the "haystack")
2. Ask the model to retrieve this statement
3. Iterate over various document depths (where the needle is placed) and context lengths to measure performance

Source: [README.md](https://github.com/gkamradt/LLMTest_NeedleInAHaystack/blob/main/README.md)

## Default Needle and Retrieval Question

From `run.py`, the default test parameters are:

- **Needle:** `"\nThe best thing to do in San Francisco is eat a sandwich and sit in Dolores Park on a sunny day.\n"`
- **Retrieval question:** `"What is the best thing to do in San Francisco?"`

Source: [needlehaystack/run.py](https://github.com/gkamradt/LLMTest_NeedleInAHaystack/blob/main/needlehaystack/run.py)

## Haystack Corpus

The haystack consists of 49 Paul Graham essays (`.txt` files) stored in `needlehaystack/PaulGrahamEssays/`. The essays are concatenated and repeated as needed to fill the desired context length. The `read_context_files()` method reads all `.txt` files and keeps appending them until the total token count reaches the maximum context length being tested.

Source: [needlehaystack/llm_needle_haystack_tester.py](https://github.com/gkamradt/LLMTest_NeedleInAHaystack/blob/main/needlehaystack/llm_needle_haystack_tester.py)

## Test Parameters (`LLMNeedleHaystackTester`)

All configurable parameters from the class constructor:

| Parameter | Default | Description |
|-----------|---------|-------------|
| `needle` | (required) | The statement/fact to embed in the haystack |
| `haystack_dir` | `"PaulGrahamEssays"` | Directory of text files for background context |
| `retrieval_question` | (required) | The question to prompt retrieval |
| `results_version` | `1` | Version number for re-running same combinations |
| `num_concurrent_requests` | `1` | Parallel API requests |
| `save_results` | `True` | Save results to JSON files |
| `save_contexts` | `True` | Save full context strings to files |
| `final_context_length_buffer` | `200` | Tokens reserved for system messages and output |
| `context_lengths_min` | `1000` | Minimum context length (tokens) |
| `context_lengths_max` | `16000` | Maximum context length (tokens) |
| `context_lengths_num_intervals` | `35` | Number of intervals between min/max |
| `context_lengths` | `None` | Custom list overrides min/max/intervals |
| `document_depth_percent_min` | `0` | Minimum depth % (should be >0) |
| `document_depth_percent_max` | `100` | Maximum depth % (should be <100) |
| `document_depth_percent_intervals` | `35` | Number of depth intervals |
| `document_depth_percents` | `None` | Custom list overrides min/max/intervals |
| `document_depth_percent_interval_type` | `"linear"` | `"linear"` or `"sigmoid"` distribution |
| `seconds_to_sleep_between_completions` | `None` | Throttle between API calls |
| `print_ongoing_status` | `True` | Print status during execution |

When `context_lengths` is `None`, lengths are generated via `np.linspace(min, max, num=intervals, endpoint=True)` rounded to integers.

When `document_depth_percent_interval_type` is `"sigmoid"`, depths are computed using a logistic function: `L * sigmoid(-k * (x - x0))` with `L=100`, `x0=50`, `k=0.1`.

Source: [needlehaystack/llm_needle_haystack_tester.py](https://github.com/gkamradt/LLMTest_NeedleInAHaystack/blob/main/needlehaystack/llm_needle_haystack_tester.py)

## Needle Insertion Algorithm

The `insert_needle()` method works as follows:

1. Encode both needle and context to tokens
2. Reduce context length by `final_context_length_buffer` (default 200 tokens)
3. If context + needle exceeds target length, truncate context tokens
4. If `depth_percent == 100`, append needle at end
5. Otherwise, calculate `insertion_point = int(len(tokens_context) * (depth_percent / 100))`
6. Walk backwards from insertion point to find the nearest sentence boundary (period token)
7. Insert needle tokens at the sentence boundary
8. Decode back to string

This ensures the needle is always placed at a sentence break, not mid-sentence.

Source: [needlehaystack/llm_needle_haystack_tester.py](https://github.com/gkamradt/LLMTest_NeedleInAHaystack/blob/main/needlehaystack/llm_needle_haystack_tester.py)

## Supported Model Providers

Three providers are supported:

1. **OpenAI** — Uses `AsyncOpenAI` client, `tiktoken` tokenizer, `max_tokens=300`, `temperature=0`
2. **Anthropic** — Uses `AsyncAnthropic` client (completions API, not messages), `max_tokens_to_sample=300`, `temperature=0`
3. **Cohere** — Uses Cohere SDK

Source: [needlehaystack/providers/](https://github.com/gkamradt/LLMTest_NeedleInAHaystack/tree/main/needlehaystack/providers)

## Prompt Templates

**OpenAI prompt** (chat messages format):
```
System: "You are a helpful AI bot that answers questions for a user. Keep your response short and direct"
User: {context}
User: "{retrieval_question} Don't give information outside the document or repeat your findings"
```

**Anthropic prompt** (completion format):
```
You are a helpful AI bot that answers questions for a user. Keep your response short and direct

H: <context>
{context}
</context>

{retrieval_question} Don't give information outside the document or repeat your findings

A: Here is the most relevant sentence in the context:
```

Source: [needlehaystack/providers/openai.py](https://github.com/gkamradt/LLMTest_NeedleInAHaystack/blob/main/needlehaystack/providers/openai.py), [needlehaystack/providers/Anthropic_prompt.txt](https://github.com/gkamradt/LLMTest_NeedleInAHaystack/blob/main/needlehaystack/providers/Anthropic_prompt.txt)

## Evaluation Scoring Rubric

The OpenAI evaluator uses the following accuracy criteria with `temperature=0`:

```
Score 1: The answer is completely unrelated to the reference.
Score 3: The answer has minor relevance but does not align with the reference.
Score 5: The answer has moderate relevance but contains inaccuracies.
Score 7: The answer aligns with the reference but has minor omissions.
Score 10: The answer is completely accurate and aligns perfectly with the reference.
Only respond with a numberical score
```

The evaluator uses LangChain's `labeled_score_string` evaluator, comparing the model's response (`prediction`) against the true needle text (`reference`) for the asked question (`input`). The default evaluator model is `gpt-3.5-turbo-0125`.

Source: [needlehaystack/evaluators/openai.py](https://github.com/gkamradt/LLMTest_NeedleInAHaystack/blob/main/needlehaystack/evaluators/openai.py)

## Multi-Needle Extension (`LLMMultiNeedleHaystackTester`)

The multi-needle variant distributes multiple facts throughout the context:

- First needle placed at the specified `depth_percent`
- Spacing calculated as: `depth_percent_interval = (100 - depth_percent) / len(self.needles)`
- Each subsequent needle placed at `depth_percent + N * depth_percent_interval`

Example from README (10 needles, initial depth 40%):
```
depth_percent_interval = (100 - 40) / 10 = 6
Needle 1: 40%, Needle 2: 46%, Needle 3: 52%, ..., Needle 10: 94%
```

Default multi-needle test facts:
- `" Figs are one of the secret ingredients needed to build the perfect pizza. "`
- `" Prosciutto is one of the secret ingredients needed to build the perfect pizza. "`
- `" Goat cheese is one of the secret ingredients needed to build the perfect pizza. "`

Source: [needlehaystack/llm_multi_needle_haystack_tester.py](https://github.com/gkamradt/LLMTest_NeedleInAHaystack/blob/main/needlehaystack/llm_multi_needle_haystack_tester.py), [needlehaystack/run.py](https://github.com/gkamradt/LLMTest_NeedleInAHaystack/blob/main/needlehaystack/run.py)

## Results Visualization

The repository includes `LLMNeedleInHaystackVisualization.ipynb` for generating pivot table visualizations from the JSON results. The pivot tables map context length (x-axis) against document depth (y-axis) with color-coded accuracy scores, producing the characteristic NIAH heatmap. The raw pivot table was transferred to Google Slides for custom annotations and formatting.

Google Slides version: https://docs.google.com/presentation/d/15JEdEBjm32qBbqeYM6DK6G-3mUJd7FAJu-qEzj8IYLQ/edit?usp=sharing

Source: [README.md](https://github.com/gkamradt/LLMTest_NeedleInAHaystack/blob/main/README.md)

## Installation and Usage

Install via PyPI: `pip install needlehaystack`

Environment variables required:
- `NIAH_MODEL_API_KEY` — API key for the model under test
- `NIAH_EVALUATOR_API_KEY` — API key for the OpenAI evaluator (when using OpenAI evaluation strategy)

Example commands:
```zsh
# OpenAI
needlehaystack.run_test --provider openai --model_name "gpt-3.5-turbo-0125" \
  --document_depth_percents "[50]" --context_lengths "[2000]"

# Anthropic
needlehaystack.run_test --provider anthropic --model_name "claude-2.1" \
  --document_depth_percents "[50]" --context_lengths "[2000]"

# Cohere
needlehaystack.run_test --provider cohere --model_name "command-r" \
  --document_depth_percents "[50]" --context_lengths "[2000]"
```

Source: [README.md](https://github.com/gkamradt/LLMTest_NeedleInAHaystack/blob/main/README.md)

## LangSmith Integration

The framework supports LangSmith for evaluation orchestration and result storage. Users can create custom evaluation datasets and run comparative tests through the LangSmith API. Multi-needle evaluation with LangSmith uses custom datasets (e.g., `multi-needle-eval-pizza`).

Example LangSmith multi-needle command:
```
needlehaystack.run_test --evaluator langsmith --context_lengths_num_intervals 3 \
  --document_depth_percent_intervals 3 --provider openai \
  --model_name "gpt-4-0125-preview" --multi_needle True \
  --eval_set multi-needle-eval-pizza \
  --needles '["Figs are one of the secret ingredients needed to build the perfect pizza.", \
  "Prosciutto is one of the secret ingredients needed to build the perfect pizza.", \
  "Goat cheese is one of the secret ingredients needed to build the perfect pizza."]'
```

Source: [README.md](https://github.com/gkamradt/LLMTest_NeedleInAHaystack/blob/main/README.md)

## Original Test Configurations

The README links to two original test runs:
- **GPT-4-128K** — Run November 8, 2023 ([X thread](https://twitter.com/GregKamradt/status/1722386725635580292))
- **Claude 2.1** — Run November 21, 2023 ([X thread](https://twitter.com/GregKamradt/status/1727018183608193393))

Original results are stored in `/original_results`. The README notes that the script has been significantly upgraded since those tests, so data formats may not match current script output.

Source: [README.md](https://github.com/gkamradt/LLMTest_NeedleInAHaystack/blob/main/README.md)
