# Appendix B: Task Configurations [p. 18]

## Configurability of RULER

RULER is designed to be configurable to allow for diverse sequence lengths and task complexities [p. 18]. For each task, there arises combinatorially large number of configurations one can adopt [p. 18]. In the main text, the authors evaluate 6 models with 13 representative tasks spanning the four categories of RULER [p. 18]. The task selection process is described in the next appendix section [p. 18].

## Task Configuration Details

### Retrieval (NIAH Variants)

**S-NIAH (Single NIAH):** The authors include the passkey retrieval (Mohtashami & Jaggi 2023) and the vanilla NIAH (Kamradt 2023), both use word-number as key-value and differ only in their background haystack [p. 18]. Additionally, the authors change the value type to UUID, for the purpose of testing model skills in retrieving long strings from context [p. 18]. For MK-NIAH, the authors add three distractor needles into the haystack [p. 18]. The authors also include existing setups from previous works: line retrieval (Liu et al. 2024a) and key-value retrieval (Liu et al. 2024d) with the haystack filled entirely with distractor needles [p. 18]. For MV-NIAH and MQ-NIAH, the authors test 4 values and 4 queries respectively [p. 18].

**Multi-hop tracing:** For VT, the authors insert 1 chain with 4 name-binding hops, totally 5 variable names need to be returned [p. 18].

**Aggregation:** For CWE, in total 10 common words need to be returned, each appears 30 times whereas the uncommon words appear 3 times each [p. 18]. For FWE, the authors set α to 2.0 in Zeta distribution for sampling synthetic words [p. 18].

**QA:** For QA, the authors augment SQuAD (Rajpurkar et al. 2018) and HotpotQA (Yang et al. 2018) to simulate long-context scenario [p. 18]. They are representative of single-hop and multi-hop question answering tasks respectively [p. 18].

**Table 5: Our total 13 task configurations in RULER** [p. 18]

| Task | Configurations |
|------|----------------|
| **Single NIAH** | **Subtask-1:** type_key = word, type_value = number, type_haystack = repeat, ∼passkey retrieval<br>**Subtask-2:** type_key = word, type_value = number, type_haystack = essay, ∼vanilla NIAH<br>**Subtask-3:** type_key = word, type_value = uuid, type_haystack = essay |
| **MK-NIAH** | **Subtask-1:** num_keys = 4, type_key = word, type_value = number, type_haystack = essay<br>**Subtask-2:** num_keys = full haystack, type_key = word, type_value = number, ∼line retrieval<br>**Subtask-3:** num_keys = full haystack, type_key = uuid, type_value = uuid, ∼KV retrieval |
| **MV-NIAH** | num_values = 4, type_key = word, type_value = number, type_haystack = essay |
| **MQ-NIAH** | num_queries = 4, type_key = word, type_value = number, type_haystack = essay |
| **VT** | num_chains = 1, num_hops = 4 |
| **CWE** | freq_cw = 30, freq_ucw = 3, num_cw = 10 |
| **FWE** | α = 2.0 |
| **QA** | dataset = SQuAD<br>dataset = HotpotQA |

Notes on notation:
- S-NIAH = Single Needle-in-a-Haystack
- MK-NIAH = Multi-Key NIAH
- MV-NIAH = Multi-Value NIAH
- MQ-NIAH = Multi-Query NIAH
- VT = Variable Tracking
- CWE = Common Words Extraction
- FWE = Frequent Words Extraction
- QA = Question Answering
- freq_cw = frequency of common words
- freq_ucw = frequency of uncommon words
- num_cw = number of common words
