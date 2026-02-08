# X Thread — Visualization Code and Design Decisions [https://x.com/GregKamradt/status/1729573848893579488]

**Type:** twitter-thread
**Fetched:** 2026-02-08
**Priority:** supplementary

[not accessible: The X/Twitter thread requires JavaScript rendering and the ThreadReaderApp mirror for this thread (November 28, 2023) was behind authentication at the time of fetching. Direct X.com access and ThreadReaderApp both failed to return thread content.]

## Known Information (from README and repository cross-references)

The thread is referenced in the GitHub README in the "Results Visualization" section:

> `LLMNeedleInHaystackVisualization.ipynb` holds the code to make the pivot table visualization. The pivot table was then transferred to Google Slides for custom annotations and formatting. See the [google slides version](https://docs.google.com/presentation/d/15JEdEBjm32qBbqeYM6DK6G-3mUJd7FAJu-qEzj8IYLQ/edit?usp=sharing). See an overview of how this viz was created [here](https://twitter.com/GregKamradt/status/1729573848893579488).

From the repository:
- The visualization is generated using `LLMNeedleInHaystackVisualization.ipynb`
- It creates a pivot table mapping context length against document depth with color-coded accuracy scores
- The raw pivot table output from the Jupyter notebook was transferred to Google Slides for annotation
- This heatmap format (context length x document depth, color = score) became the widely adopted standard for presenting NIAH results

The thread (November 28, 2023) reportedly covered:
- Code overview for generating the NIAH heatmap visualizations
- Design decisions behind the pressure-test visualization format
- Why this format was chosen for communicating long-context retrieval performance

Source: [GitHub README reference](https://github.com/gkamradt/LLMTest_NeedleInAHaystack/blob/main/README.md)
