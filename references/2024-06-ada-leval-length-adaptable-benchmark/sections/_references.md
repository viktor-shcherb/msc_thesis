# References

## Cited references

### An et al., 2023
Chenxin An, Shansan Gong, Ming Zhong, Mukai Li, Jun Zhang, Lingpeng Kong, and Xipeng Qiu. 2023. L-eval: Instituting standardized evaluation for long context language models. *arXiv preprint arXiv:2307.11088*.
- Cited in 01_introduction.md and 02_related-work.md as a recent long-context benchmark with limitations in length adaptability.

### Bai et al., 2023
Yushi Bai, Xin Lv, Jiajie Zhang, Hongchang Lyu, Jiankai Tang, Zhidian Huang, Zhengxiao Du, Xiao Liu, Aohan Zeng, Lei Hou, et al. 2023. Longbench: A bilingual, multitask benchmark for long context understanding. *arXiv preprint arXiv:2308.14508*.
- Cited in 01_introduction.md and 02_related-work.md as a bilingual long-context benchmark with limitations (fixed lengths, open-ended tasks with F1/ROUGE metrics).

### Cai et al., 2024
Zheng Cai, Maosong Cao, Haojiong Chen, Kai Chen, Keyu Chen, Xin Chen, Xun Chen, Zehui Chen, Zhi Chen, Pei Chu, et al. 2024. Internlm2 technical report.
- Cited in 04_evaluation-results.md as the source for the InternLM2-7b model evaluated in experiments.

### Chen et al., 2023a
Howard Chen, Ramakanth Pasunuru, Jason Weston, and Asli Celikyilmaz. 2023a. Walking down the memory maze: Beyond context limit through interactive reading. *arXiv preprint arXiv:2310.05029*.
- Cited in 02_related-work.md as a divide-and-conquer method that constructs a memory tree with document segment summaries.

### Chen et al., 2023b
Shouyuan Chen, Sherman Wong, Liangjian Chen, and Yuandong Tian. 2023b. Extending context window of large language models via positional interpolation. *arXiv preprint arXiv:2306.15595*.
- Cited in 02_related-work.md as a position interpolation method that linearly scales down input position indices.

### Cobbe et al., 2021
Karl Cobbe, Vineet Kosaraju, Mohammad Bavarian, Mark Chen, Heewoo Jun, Lukasz Kaiser, Matthias Plappert, Jerry Tworek, Jacob Hilton, Reiichiro Nakano, et al. 2021. Training verifiers to solve math word problems. *arXiv preprint arXiv:2110.14168*.
- Cited in 01_introduction.md as an example of existing benchmarks using short questions/instructions.

### Contributors, 2023
OpenCompass Contributors. 2023. Opencompass: A universal evaluation platform for foundation models. https://github.com/open-compass/opencompass.
- Cited in 04_evaluation-results.md as the evaluation platform used for all experiments.

### Dao et al., 2022a
Tri Dao, Dan Fu, Stefano Ermon, Atri Rudra, and Christopher Re. 2022a. Flashattention: Fast and memory-efficient exact attention with io-awareness. *Advances in Neural Information Processing Systems*, 35:16344-16359.
- Cited in 01_introduction.md and 02_related-work.md as Flash Attention, a key efficient attention mechanism.

### Dao et al., 2022b
Tri Dao, Daniel Y Fu, Khaled K Saab, Armin W Thomas, Atri Rudra, and Christopher Re. 2022b. Hungry hungry hippos: Towards language modeling with state space models. *arXiv preprint arXiv:2212.14052*.
- Cited in 02_related-work.md as one of several efficient attention advancements in Transformers.

### Dasigi et al., 2021
Pradeep Dasigi, Kyle Lo, Iz Beltagy, Arman Cohan, Noah A Smith, and Matt Gardner. 2021. A dataset of information-seeking questions and answers anchored in research papers. *arXiv preprint arXiv:2105.03011*.
- Cited in 01_introduction.md as a benchmark focusing on specific long-context abilities.

### Dettmers et al., 2022
Tim Dettmers, Mike Lewis, Younes Belkada, and Luke Zettlemoyer. 2022. Llm.int8(): 8-bit matrix multiplication for transformers at scale. *arXiv preprint arXiv:2208.07339*.
- Cited in 01_introduction.md as a quantization technique for extending context capabilities.

### Ding et al., 2023
Jiayu Ding, Shuming Ma, Li Dong, Xingxing Zhang, Shaohan Huang, Wenhui Wang, and Furu Wei. 2023. Longnet: Scaling transformers to 1,000,000,000 tokens. *arXiv preprint arXiv:2307.02486*.
- Cited in 01_introduction.md and 02_related-work.md as introducing Dilated Attention in LongNet, reducing attention complexity to nearly linear and scaling to 1 billion tokens.

### Frantar et al., 2022
Elias Frantar, Saleh Ashkboos, Torsten Hoefler, and Dan Alistarh. 2022. Gptq: Accurate post-training quantization for generative pre-trained transformers. *arXiv preprint arXiv:2210.17323*.
- Cited in 01_introduction.md as a quantization technique.

### Guo et al., 2021
Mandy Guo, Joshua Ainslie, David Uthus, Santiago Ontanon, Jianmo Ni, Yun-Hsuan Sung, and Yinfei Yang. 2021. Longt5: Efficient text-to-text transformer for long sequences. *arXiv preprint arXiv:2112.07916*.
- Cited in 02_related-work.md as an efficient attention advancement for Transformers.

### Hendrycks et al., 2020
Dan Hendrycks, Collin Burns, Steven Basart, Andy Zou, Mantas Mazeika, Dawn Song, and Jacob Steinhardt. 2020. Measuring massive multitask language understanding. *arXiv preprint arXiv:2009.03300*.
- Cited in 01_introduction.md as an example of existing benchmarks using short questions.

### Huang et al., 2021
Luyang Huang, Shuyang Cao, Nikolaus Parulian, Heng Ji, and Lu Wang. 2021. Efficient attentions for long document summarization. *arXiv preprint arXiv:2104.02112*.
- Cited in 01_introduction.md and 02_related-work.md as providing GovReport, a long-document summarization dataset.

### Huang et al., 2023
Yuzhen Huang, Yuzhuo Bai, Zhihao Zhu, Junlei Zhang, Jinghan Zhang, Tangjun Su, Junteng Liu, Chuancheng Lv, Yikai Zhang, Jiayi Lei, et al. 2023. C-eval: A multi-level multi-discipline chinese evaluation suite of foundation models. *arXiv preprint arXiv:2305.08322*.
- Cited in 01_introduction.md as an example of existing capability benchmarks using short questions.

### Kočiskỳ et al., 2018
Tomas Kočiskỳ, Jonathan Schwarz, Phil Blunsom, Chris Dyer, Karl Moritz Hermann, Gabor Melis, and Edward Grefenstette. 2018. The narrativeqa reading comprehension challenge. *Transactions of the Association for Computational Linguistics*, 6:317-328.
- Cited in 02_related-work.md as providing the NarrativeQA long-context QA dataset.

### Kryściński et al., 2021
Wojciech Kryściński, Nazneen Rajani, Divyansh Agarwal, Caiming Xiong, and Dragomir Radev. 2021. Booksum: A collection of datasets for long-form narrative summarization. *arXiv preprint arXiv:2105.08209*.
- Cited in 03_ada-leval.md as the source data for TSort (derived from Project Gutenberg).

### Li* et al., 2023
Dacheng Li*, Rulin Shao*, Anze Xie, Ying Sheng, Lianmin Zheng, Joseph E. Gonzalez, Ion Stoica, Xuezhe Ma, and Hao Zhang. 2023. How long can open-source llms truly promise on context length?
- Cited in 01_introduction.md and 02_related-work.md as describing LongChat-32k models that condense RoPE.

### Liu et al., 2023a
Nelson F Liu, Kevin Lin, John Hewitt, Ashwin Paranjape, Michele Bevilacqua, Fabio Petroni, and Percy Liang. 2023a. Lost in the middle: How language models use long contexts. *arXiv preprint arXiv:2307.03172*.
- Cited in 02_related-work.md as identifying a limitation where efficient attention mechanisms falter with middle portions of long texts.

### Liu et al., 2023b
Tianyang Liu, Canwen Xu, and Julian McAuley. 2023b. Repobench: Benchmarking repository-level code auto-completion systems. *arXiv preprint arXiv:2306.03091*.
- Cited in 01_introduction.md as a benchmark focusing on specific long-context abilities.

### Nakano et al., 2021
Reiichiro Nakano, Jacob Hilton, Suchir Balaji, Jeff Wu, Long Ouyang, Christina Kim, Christopher Hesse, Shantanu Jain, Vineet Kosaraju, William Saunders, et al. 2021. Webgpt: Browser-assisted question-answering with human feedback. *arXiv preprint arXiv:2112.09332*.
- Cited in 02_related-work.md as WebGPT, a divide-and-conquer approach for long-form QA.

### OpenAI, 2023
OpenAI. 2023. Gpt-4 technical report.
- Cited in 01_introduction.md and 02_related-work.md as the GPT-4 model with 128k context window.

### Press et al., 2021
Ofir Press, Noah A Smith, and Mike Lewis. 2021. Train short, test long: Attention with linear biases enables input length extrapolation. *arXiv preprint arXiv:2108.12409*.
- Cited in 02_related-work.md as introducing ALiBi, which applies linearly decreasing penalties to attention scores.

### Shaham et al., 2022
Uri Shaham, Elad Segal, Maor Ivgi, Avia Efrat, Ori Yoran, Adi Haviv, Ankit Gupta, Wenhan Xiong, Mor Geva, Jonathan Berant, et al. 2022. Scrolls: Standardized comparison over long language sequences. *arXiv preprint arXiv:2201.03533*.
- Cited in 01_introduction.md and 02_related-work.md as SCROLLS, a suite of long-document evaluation datasets.

### Su, 2023
Jianlin Su. 2023. Rectified rotary position embeddings. https://github.com/bojone/rerope.
- Cited in 02_related-work.md and 05_ablation-study.md as ReRoPE/Leaky ReRoPE, combining position interpolation and length extrapolation without fine-tuning.

### Su et al., 2021
Jianlin Su, Yu Lu, Shengfeng Pan, Ahmed Murtadha, Bo Wen, and Yunfeng Liu. 2021. Roformer: Enhanced transformer with rotary position embedding. *arXiv preprint arXiv:2104.09864*.
- Cited in 01_introduction.md and 02_related-work.md as RoPE, integrating rotation matrices for positional information in self-attention.

### Sun et al., 2022
Yutao Sun, Li Dong, Barun Patra, Shuming Ma, Shaohan Huang, Alon Benhaim, Vishrav Chaudhary, Xia Song, and Furu Wei. 2022. A length-extrapolatable transformer. *arXiv preprint arXiv:2212.10554*.
- Cited in 01_introduction.md as a scalable position embedding technique.

### Sun et al., 2023
Simeng Sun, Yang Liu, Shuohang Wang, Chenguang Zhu, and Mohit Iyyer. 2023. Pearl: Prompting large language models to plan and execute actions over long documents. *arXiv preprint arXiv:2305.14564*.
- Cited in 02_related-work.md as PEARL, a divide-and-conquer framework for long-text reasoning.

### Suzgun et al., 2022
Mirac Suzgun, Nathan Scales, Nathanael Scharli, Sebastian Gehrmann, Yi Tay, Hyung Won Chung, Aakanksha Chowdhery, Quoc V Le, Ed H Chi, Denny Zhou, et al. 2022. Challenging big-bench tasks and whether chain-of-thought can solve them. *arXiv preprint arXiv:2210.09261*.
- Cited in 01_introduction.md as an example of existing benchmarks using short questions.

### Touvron et al., 2023
Hugo Touvron, Louis Martin, Kevin Stone, Peter Albert, Amjad Almahairi, Yasmine Babaei, Nikolay Bashlykov, Soumya Batra, Prajjwal Bhargava, Shruti Bhosale, et al. 2023. Llama 2: Open foundation and fine-tuned chat models. *arXiv preprint arXiv:2307.09288*.
- Cited in 01_introduction.md and 02_related-work.md as Llama 2, integrating RoPE to expand context to 4k tokens.

### Zaheer et al., 2020
Manzil Zaheer, Guru Guruganesh, Kumar Avinava Dubey, Joshua Ainslie, Chris Alberti, Santiago Ontanon, Philip Pham, Anirudh Ravula, Qifan Wang, Li Yang, et al. 2020. Big bird: Transformers for longer sequences. *Advances in neural information processing systems*, 33:17283-17297.
- Cited in 01_introduction.md and 02_related-work.md as an efficient attention mechanism for long sequences.

### Zeng et al., 2022
Aohan Zeng, Xiao Liu, Zhengxiao Du, Zihan Wang, Hanyu Lai, Ming Ding, Zhuoyi Yang, Yifan Xu, Wendi Zheng, Xiao Xia, et al. 2022. Glm-130b: An open bilingual pre-trained model. *arXiv preprint arXiv:2210.02414*.
- Cited in 01_introduction.md, 02_related-work.md, and 04_evaluation-results.md as the source for ChatGLM2-6B-32k and ChatGLM3-6B-32k models.

### Zheng et al., 2023
Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan Zhuang, Zhanghao Wu, Yonghao Zhuang, Zi Lin, Zhuohan Li, Dacheng Li, Eric Xing, et al. 2023. Judging llm-as-a-judge with mt-bench and chatbot arena. *arXiv preprint arXiv:2306.05685*.
- Cited in 01_introduction.md, 02_related-work.md, 04_evaluation-results.md, and 05_ablation-study.md as the source for Vicuna-v1.5 models (fine-tuned Llama 2 with extended context windows).
