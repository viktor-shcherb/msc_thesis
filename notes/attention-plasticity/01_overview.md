# Attention Plasticity: Overview

## Definition

**Attention plasticity** measures whether an attention head can flexibly select relevant information from the context depending on the future query. It quantifies the head's capacity for **query-dependent key selection**:

- **High plasticity**: Which keys receive attention depends on the query—different queries retrieve different information from the same context
- **Low plasticity**: Certain keys are always prioritized regardless of query—the head has a fixed preference that ignores query content

## Core Insight

The fundamental purpose of attention is **random access**: given a context, the model should be able to retrieve whichever information is relevant to the current query. A head with low plasticity undermines this—it always prioritizes the same keys (e.g., recent tokens, specific positions) regardless of what the query actually needs.

In transformer attention, a query $q$ compares against keys $k_1, k_2, \ldots$ via dot products. For keys $k_1$ and $k_2$, the outcome of $q^\top k_1 > q^\top k_2$ determines which key "wins."

Attention plasticity asks: **does this outcome depend on the query, or is it predetermined?**

## Intuition

Consider two attention heads processing the same context:

**Head A (Low Plasticity)**: Always attends strongly to the most recent tokens, regardless of query. If asked "What color is the car?" or "Who is the president?", it retrieves the same information—whatever is positionally recent.

**Head B (High Plasticity)**: Attends to different tokens depending on the query. For "What color is the car?" it finds the color description; for "Who is the president?" it finds the name. The query determines what gets retrieved.

Head A has essentially hardcoded a retrieval heuristic (recency). Head B implements true query-dependent retrieval—the essence of attention.

## Measurement Approach

1. **Model queries** as having a positional component plus semantic variability
2. **For key pairs**, compute the probability distribution over "which key wins"
3. **Plasticity = Bernoulli variance** of this probability: $4p(1-p)$
   - Maximum (1.0) when $p = 0.5$: outcome is maximally query-dependent
   - Minimum (0.0) when $p \approx 0$ or $p \approx 1$: outcome is predetermined, query doesn't matter

## Significance for Transformer Analysis

Attention plasticity reveals whether heads implement genuine query-key matching or fall back to fixed heuristics:

- **Low plasticity heads**: Act like fixed retrieval rules (e.g., "always attend to position -1"). Useful for structural patterns but limited in flexibility.
- **High plasticity heads**: Implement true content-based retrieval. Can adapt to retrieve different information based on query needs.

A model with predominantly low-plasticity heads may struggle with tasks requiring flexible information retrieval from context, as it cannot effectively use queries to select relevant keys.
