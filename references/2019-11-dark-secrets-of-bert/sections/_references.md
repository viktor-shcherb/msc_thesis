# References

Only references cited in the section notes are included below.

## Cited references

**Vaswani et al. (2017)**
- Full: Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz Kaiser, Illia Polosukhin. "Attention Is All You Need." NeurIPS 2017.
- Cited in 01_introduction.md as the foundational Transformer architecture.

**Radford et al. (2018)**
- Full: Alec Radford, Karthik Narasimhan, Tim Salimans, Ilya Sutskever. "Improving Language Understanding by Generative Pre-Training." 2018.
- Cited in 01_introduction.md as achieving state-of-the-art NLP performance with Transformers.

**Devlin et al. (2018)**
- Full: Jacob Devlin, Ming-Wei Chang, Kenton Lee, Kristina Toutanova. "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding." NAACL 2019.
- Cited in 01_introduction.md as the BERT paper; cited in 03_methodology.md for fine-tuning hyperparameters.

**Rajpurkar et al. (2016)**
- Full: Pranav Rajpurkar, Jian Zhang, Konstantin Lopyrev, Percy Liang. "SQuAD: 100,000+ Questions for Machine Comprehension of Text." EMNLP 2016.
- Cited in 01_introduction.md (SQuAD leaderboard) and 03_methodology.md (QNLI dataset).

**Wang et al. (2018)**
- Full: Alex Wang, Amanpreet Singh, Julian Michael, Felix Hill, Omer Levy, Samuel R. Bowman. "GLUE: A Multi-Task Benchmark and Analysis Platform for Natural Language Understanding." ICLR 2019.
- Cited in 01_introduction.md (GLUE benchmark) and 03_methodology.md (GLUE tasks used).

**Goldberg (2019)**
- Full: Yoav Goldberg. "Assessing BERT's Syntactic Abilities." arXiv:1901.05287, 2019.
- Cited in 02_related-work.md for subject-verb agreement and for observation that smaller BERT performs better on syntax tests.

**Jawahar et al. (2019)**
- Full: Ganesh Jawahar, Benoit Sagot, Djame Seddah. "What Does BERT Learn about the Structure of Language?" ACL 2019.
- Cited in 02_related-work.md for extending probing to multiple layers/tasks.

**Tran et al. (2018)**
- Full: Ke Tran, Arianna Bisazza, Christof Monz. "The Importance of Being Recurrent for Modeling Hierarchical Structure." EMNLP 2018.
- Cited in 02_related-work.md for LSTMs generalizing better to longer sequences than Transformers.

**Liu et al. (2019)**
- Full: Nelson F. Liu, Matt Gardner, Yonatan Belinkov, Matthew E. Peters, Noah A. Smith. "Linguistic Knowledge and Transferability of Contextual Representations." NAACL 2019.
- Cited in 02_related-work.md for transferability findings about middle vs. higher layers.

**Tang et al. (2018)**
- Full: Gongbo Tang, Mathias Muller, Annette Rios, Rico Sennrich. "Why Self-Attention? A Targeted Evaluation of Neural Machine Translation Architectures." EMNLP 2018.
- Cited in 02_related-work.md for self-attention outperforming CNN/RNN on word sense disambiguation.

**Voita et al. (2019)**
- Full: Elena Voita, David Talbot, Fedor Moiseev, Rico Sennrich, Ivan Titov. "Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned." ACL 2019.
- Cited in 02_related-work.md for finding that only a small subset of heads is important.

**Frankle and Carbin (2018)**
- Full: Jonathan Frankle, Michael Carbin. "The Lottery Ticket Hypothesis: Finding Sparse, Trainable Neural Networks." ICLR 2019.
- Cited in 02_related-work.md for showing overparameterization in complex architectures.

**Adhikari et al. (2019)**
- Full: Ashutosh Adhikari, Achyudh Ram, Raphael Tang, Jimmy Lin. "DocBERT: BERT for Document Classification." arXiv:1904.08398, 2019.
- Cited in 02_related-work.md for showing a simple BiLSTM can match complex architectures on document classification.

**Wu et al. (2019)**
- Full: Felix Wu, Angela Fan, Alexei Baevski, Yann N. Dauphin, Michael Auli. "Pay Less Attention with Lightweight and Dynamic Convolutions." ICLR 2019.
- Cited in 02_related-work.md for showing unnecessary complexity of self-attention and proposing lightweight dynamic convolution.

**Michel et al. (2019)**
- Full: Paul Michel, Omer Levy, Graham Neubig. "Are Sixteen Heads Really Better than One?" NeurIPS 2019.
- Cited in 02_related-work.md for showing Transformer layers can be reduced to a single head.

**Dolan and Brockett (2005)**
- Full: William B. Dolan, Chris Brockett. "Automatically Constructing a Corpus of Sentential Paraphrases." IWP 2005.
- Cited in 03_methodology.md as the MRPC dataset reference.

**Cer et al. (2017)**
- Full: Daniel Cer, Mona Diab, Eneko Agirre, Inigo Lopez-Gazpio, Lucia Specia. "SemEval-2017 Task 1: Semantic Textual Similarity Multilingual and Crosslingual Focused Evaluation." SemEval 2017.
- Cited in 03_methodology.md as the STS-B dataset reference.

**Socher et al. (2013)**
- Full: Richard Socher, Alex Perelygin, Jean Y. Wu, Jason Chuang, Christopher D. Manning, Andrew Y. Ng, Christopher Potts. "Recursive Deep Models for Semantic Compositionality Over a Sentiment Treebank." EMNLP 2013.
- Cited in 03_methodology.md as the SST-2 dataset reference.

**Williams et al. (2018)**
- Full: Adina Williams, Nikita Nangia, Samuel R. Bowman. "A Broad-Coverage Challenge Corpus for Sentence Understanding through Inference." NAACL 2018.
- Cited in 03_methodology.md as the MNLI dataset reference.

**Schutze (1996)**
- Full: Carson T. Schutze. "The Empirical Base of Linguistics: Grammaticality Judgments and Linguistic Methodology." University of Chicago Press, 1996.
- Cited in 03_methodology.md for explaining problems with CoLa's underlying methodology.

**Wang et al. (2019)**
- Full: Alex Wang, Yada Pruksachatkun, Nikita Nangia, Amanpreet Singh, Julian Michael, Felix Hill, Omer Levy, Samuel R. Bowman. "SuperGLUE: A Stickier Benchmark for General-Purpose Language Understanding Systems." NeurIPS 2019.
- Cited in 03_methodology.md noting that CoLa is not included in the upcoming version of GLUE.

**Baker et al. (1998)**
- Full: Collin F. Baker, Charles J. Fillmore, John B. Lowe. "The Berkeley FrameNet Project." COLING-ACL 1998.
- Cited in 04b_relation-specific-heads.md as the FrameNet reference for frame semantics data.

**Yosinski et al. (2014)**
- Full: Jason Yosinski, Jeff Clune, Yoshua Bengio, Hod Lipson. "How transferable are features in deep neural networks?" NeurIPS 2014.
- Cited in 04c_attention-change-fine-tuning.md for results on fine-tuning a CNN pre-trained on ImageNet.

**Romanov and Shivade (2018)**
- Full: Alexey Romanov, Chaitanya Shivade. "Lessons from Natural Language Inference in the Clinical Domain." EMNLP 2018.
- Cited in 04c_attention-change-fine-tuning.md for results on transfer learning for medical NLI.
