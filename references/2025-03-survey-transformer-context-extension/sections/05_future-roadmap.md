# 5 Future Roadmap and Open Problems [p. 8]

Despite the rapid development of long context techniques, numerous challenges remain unresolved. Looking to future roadmap, we list vital open problems and present our perspectives on the developments. They are also divided into two parts: approaches and evaluation [p. 8].

## 5.1 Approaches [p. 8]

**Method Integration** would combine methods' strengths to address the challenges of extrapolating long context from multiple perspectives [p. 8].

**Long Text Generation** remains under-researched, which concentrate on effective long-text generation techniques and the evaluation of generation quality [p. 8].

**Sparse Attention Mechanisms** may lead to a decrease in models' original language ability, thereby limiting their potential for processing long context [p. 8].

**"Lost-in-the-Middle" Issue** has not yet been completely resolved, there is a lack of targeted solutions and appropriate verification methods [p. 8].

**Scalability of Methods** requires to explore how existing methods can be adapted to models of different scales or even different architectural frameworks, enhancing their generality and applicability [p. 8].

**Methods Enabling "Train Short, Test Long"** haven't emerged, which train on short texts while excelling in long-context. These methods can reduce resource needs and improve generalization [p. 8].

**Trade-off between Information Filtering and Generation Effects** means existing methods can be optimized by integrating RAG to enhance efficiency and quality without too long input [p. 8].

## 5.2 Evaluation [p. 8]

**Knowledge Leakage Issue** is ever-present. As LLMs gain the ability to gather information from the Internet and their training data scope expands, existing solutions become increasingly ineffective and some operations may limit innovation [p. 8].

**Novel Benchmark Design** needed to be proposed. We need to construct benchmarks with coherent content and long-distance dependencies to more effectively test the model's ability to process long context. For example, asking models to process inputs from multiple books [p. 8].

**Updated LLM-based Metrics** are a development direction. Though LLM-based metrics show higher consistency with human judgments than other metrics, they are costly, have random outputs, and even lack human emotions. We need to combine LLM with other techniques to better evaluate [p. 8].
