# 7.6 Image Recognition Results [p. 61]

[p. 61] The performance of the image understanding capabilities of Llama 3 is evaluated on a range of tasks spanning natural image understanding, text understanding, charts understanding and multimodal reasoning:

- **MMMU** (Yue et al., 2024a) is a challenging dataset for multimodal reasoning where the model is expected to understand images and solve college-level problems spanning 30 different disciplines. This includes both multiple-choice and open ended questions. The model is evaluated on the validation set with 900 images, in line with other works. [p. 61]

- **VQAv2** (Antol et al., 2015) tests the ability of a model to combine image understanding, language understanding and commonsense knowledge to answer generic questions about natural images. [p. 61]

- **AI2 Diagram** (Kembhavi et al., 2016) evaluates models capability to parse scientific diagrams and answer questions about the same. The same evaluation protocol as Gemini and x.ai is used, and scores using a transparent bounding box are reported. [p. 61]

- **ChartQA** (Masry et al., 2022) is a challenging benchmark for charts understanding. This requires the model to visually understand different kinds of charts and answer logical questions about the charts. [p. 61]

- **TextVQA** (Singh et al., 2019) is a popular benchmark dataset that requires models to read and reason about text in images to answer questions about them. This tests the OCR understanding ability of the model on natural images. [p. 61]

- **DocVQA** (Mathew et al., 2020) is a benchmark dataset focused on document analysis and recognition. It contains images of a wide range of documents which evaluates a model's ability to perform OCR understanding and reason about the contents of a document to answer questions about them. [p. 61]

**Table 29** (p. 61): "Image understanding performance of our vision module attached to Llama 3. We compare model performance to GPT-4V, GPT-4o, Gemini 1.5 Pro, and Claude 3.5 Sonnet. ^{triangle} Results obtained using external OCR tools."

|                        | Llama 3-V 8B | Llama 3-V 70B | Llama 3-V 405B | GPT-4V | GPT-4o | Gemini 1.5 Pro | Claude 3.5 |
|------------------------|-------------|--------------|----------------|--------|--------|----------------|------------|
| MMMU (val, CoT)        | 49.6        | 60.6         | 64.5           | 56.4   | **69.1** | 62.2           | 68.3       |
| VQAv2 (test-dev)       | 78.0        | 79.1         | **80.2**       | 77.2   | --     | **80.2**       | --         |
| AI2 Diagram (test)     | 84.4        | 93.0         | 94.1           | 78.2   | 94.2   | 94.4           | **94.7**   |
| ChartQA (test, CoT)    | 78.7        | 83.2         | 85.8           | 78.4   | 85.7   | 87.2           | **90.8**   |
| TextVQA (val)          | 78.2        | 83.4         | **84.8**       | 78.0   | --     | 78.7           | --         |
| DocVQA (test)          | 84.4        | 92.2         | 92.6           | 88.4   | 92.8   | 93.1^{triangle} | **95.2**   |

[p. 61] The results in Table 29 show that the vision module attached to Llama 3 performs competitively across a wide range of image-recognition benchmarks at varying model capacities. Using the resulting Llama 3-V 405B model, GPT-4V is outperformed on all benchmarks, while being slightly behind Gemini 1.5 Pro and Claude 3.5 Sonnet. Llama 3 405B appears particularly competitive on document understanding tasks. [p. 61]
