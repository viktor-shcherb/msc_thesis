---
title: "LoCoBench: A Comprehensive Long-Context Code Benchmark for LLMs"
authors: "Qiu, Liu, Liu, Murthy, Zhang, Chen, Wang, Zhu, Yang, Tan, Cen, Qian, Heinecke, Yao, Savarese, Xiong, Wang"
year: 2025
venue: "arXiv 2025"
paper_type: preprint
categories: ["benchmarking", "long-context-evaluation"]
scope: ["software engineering tasks", "code understanding", "10K-1M token contexts", "10 programming languages"]
benchmarks_used: ["locobench", "humaneval", "swe-verified"]
models_introduced: []
models_evaluated: ["gpt-5", "gemini-2.5-pro", "claude-4.5-sonnet", "gemini-2.5-flash"]
key_claims:
  - id: C1
    claim: "LoCoBench provides 8,000 evaluation scenarios spanning 10 programming languages with context lengths from 10K to 1M tokens across 8 task categories"
    evidence: "Section 3, benchmark statistics"
    status: supported
    magnitude: "8,000 scenarios, 1,000 projects, 50,000+ files, 15M total LOC"
  - id: C2
    claim: "Existing code benchmarks operate with short contexts (typically under 10K tokens) and focus on isolated tasks, failing to evaluate complex long-context software engineering capabilities"
    evidence: "Section 2, comparison table with HumanEval (164 instances, Python-only), SWE-Bench (2,294 instances, Python), Multi-SWE-Bench (1,632, 7 languages)"
    status: supported
  - id: C3
    claim: "Gemini-2.5-Pro emerges as the overall leader in comprehensive evaluation, with particular strength in cross-file refactoring and long-context utilization"
    evidence: "Section 5, performance visualizations"
    status: unvalidated
    scope: "Based on visualizations only; no numerical results tables provided"
  - id: C4
    claim: "LoCoBench introduces 6 novel evaluation metrics: Architectural Coherence Score (ACS), Dependency Traversal Accuracy (DTA), Cross-File Reasoning Depth (CFRD), Incremental Development Capability (IDC), Information Coverage Utilization (ICU), and Multi-Session Memory Retention (MMR)"
    evidence: "Section 3, metric definitions"
    status: supported
  - id: C5
    claim: "Model performance degrades as context length increases from 10K to 1M tokens, with Expert-level scenarios (500K-1M) remaining a significant challenge for all evaluated models"
    evidence: "Section 5, difficulty calibration results"
    status: unvalidated
    scope: "Claimed but no numerical degradation figures provided"
cross_references: []
open_questions:
  - question: "How well do synthetically generated benchmark projects reflect the complexity and architectural patterns of real-world open-source codebases?"
    addressed_by: null
  - question: "Do the 6 novel metrics (ACS, DTA, CFRD, ICU, MMR, IDC) correlate with human expert judgments of software engineering quality?"
    addressed_by: null
  - question: "How do open-weight models compare to proprietary models on long-context code tasks at the 500K-1M scale?"
    addressed_by: null
  - question: "What is the practical ceiling for current LLMs on Expert-level (500K-1M token) software engineering tasks?"
    addressed_by: null
---

# LoCoBench: A Comprehensive Long-Context Code Benchmark for LLMs

**Authors:** Jielin Qiu, Zuxin Liu, Zhiwei Liu, Rithesh Murthy, Jianguo Zhang, Haolin Chen, Shiyu Wang, Ming Zhu, Liangwei Yang, Juntao Tan, Zhepeng Cen, Cheng Qian, Shelby Heinecke, Weiran Yao, Silvio Savarese, Caiming Xiong, Huan Wang (Salesforce AI Research)
**Date:** September 2025, arXiv:2509.09614

---

## Core Research Problem

Long-context language models now support context windows extending to millions of tokens, but evaluation benchmarks for code understanding have not kept pace. Existing benchmarks suffer from three critical limitations:

1. **Scale limitations.** Most code benchmarks contain fewer than 3,000 evaluation instances. HumanEval provides only 164 Python-only problems. SWE-Bench offers 2,294 instances restricted to Python bug fixes. Multi-SWE-Bench extends to 1,632 instances across 7 languages but remains limited in scope (Section 2).

2. **Context limitations.** Traditional code benchmarks operate with short contexts, typically under 10K tokens. They evaluate single-file or single-function tasks that do not require understanding the broader codebase architecture, cross-file dependencies, or system-level design patterns (Section 2).

3. **Task scope limitations.** Existing benchmarks focus on isolated code generation, completion, or bug fixing. They do not evaluate capabilities essential for real-world software engineering: architectural understanding, cross-file refactoring, multi-session development continuity, integration testing, or security analysis across large codebases (Section 1, Section 2).

**The core gap is the absence of a comprehensive benchmark that evaluates long-context LLM capabilities across the full spectrum of software engineering tasks, from 10K to 1M token contexts, across multiple programming languages and architectural patterns.**

---

## Problem Solutions

LoCoBench addresses these gaps through a large-scale, multi-dimensional benchmark design:

1. **Scale.** 8,000 evaluation scenarios derived from 1,000 synthetically generated projects across 10 programming languages, with over 50,000 files and 15 million total lines of code.
2. **Context range.** Systematic scaling from 10K to 1M tokens across four calibrated difficulty levels.
3. **Task diversity.** 8 task categories covering architectural understanding, cross-file refactoring, feature implementation, bug investigation, multi-session development, code comprehension, integration testing, and security analysis.
4. **Multi-dimensional evaluation.** 17 metrics across 4 dimensions, including 6 newly proposed metrics, combined into a single LoCoBench Score (LCBS).

---

## Approach Details

### Benchmark Construction Pipeline

The benchmark is constructed via a 5-phase synthetic pipeline:

**Phase 1: Specification generation.** 1,000 diverse project specifications are generated across 10 programming languages (100 per language), spanning 36 domain categories grouped into 10 main domains. Each specification defines architectural patterns and complexity requirements.

**Phase 2: Codebase generation.** Complete codebases are generated from specifications, producing 10--100 files per project. Mean project size is 14,559 lines of code and 48.7 files.

**Phase 3: Scenario creation.** Each of the 1,000 projects is transformed into 8 evaluation scenarios (one per task category), yielding 8,000 total scenarios. Context is selected intelligently from the codebase to match target difficulty levels.

**Phase 4: Validation.** Automated quality assurance including compilation checks (language-specific compilers: gcc, javac, Python), cyclomatic complexity analysis, dependency depth measurement, architectural coherence scoring, information coverage ratio calculation (target >0.7), and bias detection filtering.

**Phase 5: Evaluation.** LLM evaluation using the 17-metric framework.

### Programming Languages

Python, C++, Java, C, C#, JavaScript, TypeScript, Go, Rust, PHP -- each representing 10% of scenarios with equal distribution.

### Task Categories

| Category | Focus |
|---|---|
| Architectural Understanding | Design patterns, dependencies, system design comprehension |
| Cross-File Refactoring | Multi-file restructuring while maintaining functionality |
| Feature Implementation | Complex feature development within existing systems |
| Bug Investigation | Systematic debugging across codebases |
| Multi-Session Development | Context persistence across development sessions |
| Code Comprehension | Large codebase understanding and analysis |
| Integration Testing | Component interaction and end-to-end validation |
| Security Analysis | Vulnerability assessment and threat identification |

### Difficulty Calibration

Scenarios are distributed across four difficulty levels (25% each):

| Level | Context Range |
|---|---|
| Easy | 10K--100K tokens |
| Medium | 100K--200K tokens |
| Hard | 200K--500K tokens |
| Expert | 500K--1M tokens |

### Evaluation Framework: 17 Metrics Across 4 Dimensions

**Software Engineering Excellence (8 metrics, weight 0.4):**
- Architectural Coherence Score (ACS) -- *newly proposed*
- Dependency Traversal Accuracy (DTA) -- *newly proposed*
- Cross-File Reasoning Depth (CFRD) -- *newly proposed*
- System Thinking Score (STS)
- Robustness Score (RS)
- Comprehensiveness Score (CS)
- Innovation Score (IS)
- Solution Elegance Score (SES)

**Functional Correctness (4 metrics, weight 0.3):**
- Code Compilation Success (CCS)
- Unit Test Performance (UTP)
- Integration Test Performance (ITP)
- Incremental Development Capability (IDC) -- *newly proposed*

**Code Quality Assessment (3 metrics, weight 0.2):**
- Security Analysis Score (SAS)
- Average Issues Found (AIF)
- Code Style Adherence (CSA)

**Long-Context Utilization (2 metrics, weight 0.1):**
- Information Coverage Utilization (ICU) -- *newly proposed*
- Multi-Session Memory Retention (MMR) -- *newly proposed*

### LoCoBench Score (LCBS)

Metrics are first normalized and averaged within each dimension:

> SE = (1/8) * sum of normalized SE metrics
> FC = (1/4) * sum of normalized FC metrics
> CQ = (1/3) * sum of normalized CQ metrics
> LCU = (1/2) * sum of normalized LCU metrics

The final score uses a weighted combination scaled to [0, 5]:

> LCBS = 5 * (0.4 * SE + 0.3 * FC + 0.2 * CQ + 0.1 * LCU)

The weight distribution prioritizes Software Engineering Excellence (40%) and Functional Correctness (30%), with Code Quality (20%) and Long-Context Utilization (10%) receiving lower weights.

### Architecture Patterns

10 architectural patterns are represented: Monolithic, Microservices, Serverless, Event-Driven, Layered, Clean, Hexagonal, MVC, MVVM, and Component-Based.

### Key Results

The paper evaluates GPT-5, Gemini-2.5-Pro, Claude Sonnet 4, and Gemini-2.5-Flash. Results are presented primarily through visualizations (Figures 5--11) without numerical tables.

The paper claims that **Gemini-2.5-Pro emerges as the overall leader**, with particular strengths in cross-file refactoring and long-context utilization. However, no LCBS scores or per-metric numerical breakdowns are provided in the main text.

### Comparison with Prior Benchmarks

| Benchmark | Instances | Languages | Max Context | Task Types |
|---|---|---|---|---|
| HumanEval | 164 | 1 (Python) | Short | Code generation |
| SWE-Bench | 2,294 | 1 (Python) | Short | Bug fixing |
| Multi-SWE-Bench | 1,632 | 7 | Short | Bug fixing |
| LongCodeBench | 600+ | Limited | Medium | Code completion |
| LongCodeArena | 1,500+ | Limited | Medium | Code completion |
| DevBench | 200+ | Limited | Mixed | Mixed |
| RULER | 4,000+ | N/A | Long | NLP-focused |
| **LoCoBench** | **8,000** | **10** | **1M tokens** | **8 SE categories** |

---

## Limitations and Failure Modes

1. **Synthetic benchmark.** All 1,000 projects are synthetically generated rather than sourced from real open-source repositories. While automated validation (compilation, complexity analysis, bias detection) is applied, synthetic code may not capture the idiosyncratic complexity, legacy patterns, technical debt, and documentation quality of real-world codebases. The paper does not validate the representativeness of synthetic projects against real repositories.

2. **No numerical results tables.** The paper presents model comparisons through visualizations (Figures 5--11) but does not provide tabulated LCBS scores, per-metric breakdowns, or statistical significance tests. This makes it impossible to precisely assess model performance differences or reproduce comparative analyses.

3. **LLM-as-judge evaluation.** Many of the 17 metrics -- particularly the subjective ones (Innovation Score, Solution Elegance Score, System Thinking Score) -- rely on LLM-based evaluation rather than execution-based ground truth. The paper does not report inter-annotator agreement or correlation with human expert judgments for these metrics.

4. **Novel metrics unvalidated externally.** The 6 newly proposed metrics (ACS, DTA, CFRD, IDC, ICU, MMR) are introduced without external validation. Whether they meaningfully capture the software engineering qualities they claim to measure is not established through correlation studies with human experts or alternative measurement approaches.

5. **Limited model coverage.** Only 4 proprietary models are evaluated (GPT-5, Gemini-2.5-Pro, Claude Sonnet 4, Gemini-2.5-Flash). No open-weight models are evaluated, limiting the benchmark's utility for the open-source research community.

6. **Equal language distribution.** Allocating 10% of scenarios to each of 10 languages assumes equal importance, which may not reflect real-world software engineering distributions where Python, JavaScript, and Java dominate.

7. **Weight justification absent.** The LCBS weight vector [0.4, 0.3, 0.2, 0.1] assigns only 10% weight to Long-Context Utilization despite this being the benchmark's distinguishing feature. The rationale for these weights is not empirically justified.

---

## Conclusions

### Contributions

1. **Large-scale long-context code benchmark.** LoCoBench provides 8,000 evaluation scenarios across 10 programming languages with context lengths systematically scaled from 10K to 1M tokens, substantially exceeding prior benchmarks in both scale and context range (Section 3).

2. **Comprehensive task taxonomy for software engineering.** The 8 task categories -- architectural understanding, cross-file refactoring, feature implementation, bug investigation, multi-session development, code comprehension, integration testing, and security analysis -- provide broader coverage of real-world SE activities than prior benchmarks focused on generation or bug fixing (Section 3).

3. **Novel evaluation metrics.** Six new metrics targeting previously unmeasured capabilities: Architectural Coherence Score, Dependency Traversal Accuracy, Cross-File Reasoning Depth, Incremental Development Capability, Information Coverage Utilization, and Multi-Session Memory Retention (Section 3).

4. **Multi-dimensional scoring framework.** The 4-dimension, 17-metric framework aggregated into LCBS provides a structured approach to evaluating LLMs as software engineering assistants (Section 3).

### Implications

1. **Expert-level long-context code tasks remain unsolved.** (Inference) The finding that model performance degrades at 500K-1M token contexts suggests that current architecture improvements in context handling have not yet translated to reliable performance on complex SE tasks at extreme context lengths.

2. **Benchmark may drive long-context code optimization.** (Inference) By providing calibrated difficulty levels and multi-dimensional metrics, LoCoBench could serve as an optimization target for model developers specifically targeting code-related long-context capabilities.

3. **Synthetic benchmarks as scalable alternative.** (Inference) The 5-phase synthetic generation pipeline demonstrates a methodology for creating large-scale code benchmarks without the licensing, curation, and contamination challenges of sourcing from real repositories, though at the cost of potential distribution mismatch.

---

## Key Claims

1. **C1: LoCoBench provides 8,000 scenarios across 10 languages at 10K-1M tokens.** The benchmark covers Python, C++, Java, C, C#, JavaScript, TypeScript, Go, Rust, and PHP, with 1,000 projects generating 8 scenarios each across 4 difficulty levels. Evidence: Section 3, benchmark statistics. Status: **supported**.

2. **C2: Existing code benchmarks are insufficient for long-context SE evaluation.** HumanEval has 164 Python-only instances; SWE-Bench has 2,294 Python-only bug fixes; even Multi-SWE-Bench (1,632 instances, 7 languages) operates at short context lengths. Evidence: Section 2, comparison table. Status: **supported**.

3. **C3: Gemini-2.5-Pro leads overall performance.** Claimed to excel particularly in cross-file refactoring and long-context utilization. Evidence: Section 5, visualizations only -- no numerical tables provided. Status: **unvalidated** (cannot verify from paper's presentation).

4. **C4: Six novel metrics are introduced.** ACS, DTA, CFRD, IDC, ICU, and MMR are defined and applied within the evaluation framework. Evidence: Section 3, metric definitions. Status: **supported** (metrics are defined, though not externally validated).

5. **C5: Performance degrades at extreme context lengths.** Expert-level scenarios (500K-1M tokens) are claimed to be a significant challenge. Evidence: Section 5, difficulty calibration results. Status: **unvalidated** (no numerical degradation data provided).

---

## Open Questions

1. **How well do synthetically generated projects reflect real-world codebase complexity?** The 5-phase pipeline includes compilation validation and complexity analysis, but distributional similarity to open-source repositories is not measured. **Unresolved.**

2. **Do the novel metrics correlate with human expert judgments?** The 6 new metrics (ACS, DTA, CFRD, IDC, ICU, MMR) are proposed without human correlation studies. Whether they capture meaningful SE quality dimensions requires external validation. **Unresolved.**

3. **How do open-weight models perform on LoCoBench?** Only proprietary models (GPT-5, Gemini-2.5-Pro, Claude Sonnet 4, Gemini-2.5-Flash) are evaluated. Performance of open models (Llama, Qwen, DeepSeek) at long-context code tasks is unknown. **Unresolved.**

4. **What is the practical ceiling for current LLMs at Expert difficulty (500K-1M tokens)?** The paper claims performance degradation but does not quantify it. Understanding the failure modes at extreme context lengths could inform architectural improvements. **Unresolved.**

---

## Core References and Why They Are Referenced

### Code Evaluation Benchmarks

- **Chen et al. (2021)** -- *HumanEval.* 164 hand-crafted Python programming problems with test cases. Primary comparison point: LoCoBench argues HumanEval is too small (164 instances), Python-only, and short-context for evaluating modern long-context LLMs.

- **Jimenez et al. (2024)** -- *SWE-Bench.* 2,294 real-world Python bug-fixing tasks from GitHub repositories. LoCoBench extends beyond SWE-Bench's Python-only, bug-fixing scope to 10 languages and 8 task categories including architectural understanding and security analysis.

- **Zan et al. (2025)** -- *Multi-SWE-Bench.* Extends SWE-Bench to 1,632 instances across 7 languages. Still limited to bug fixing and short contexts. LoCoBench provides broader task coverage and systematic context scaling.

### Long-Context Benchmarks

- **Hsieh et al. (2024)** -- *RULER.* Multi-task synthetic long-context benchmark for NLP tasks. Referenced as the closest prior work in long-context evaluation, but RULER focuses on NLP tasks (retrieval, QA) rather than software engineering.

- **Guo et al. (2024)** -- *LongCodeBench.* 600+ code completion instances at medium context lengths. LoCoBench scales to 8,000 instances with contexts up to 1M tokens across 8 task categories.

- **Bogomolov et al. (2024)** -- *LongCodeArena.* 1,500+ completion-focused instances. Similar limitations to LongCodeBench in task diversity and maximum context length.

### Software Development Evaluation

- **Li et al. (2024)** -- *DevBench.* ~200 mixed software development tasks. LoCoBench extends the scope with 40x more instances and systematic context scaling.
