# 4 Related Work [p. 8-9]

## Context in count-based and discriminative LMs

[p. 8] The earliest learned LMs were *count-based* (e.g., Kneser and Ney, 1995): they estimated p(x_n | x_{0:n}) based on a (smoothed) empirical n-gram frequency #(x_{0:n}) / #(x_{0:n-1}) (where #(x) is the number of times the sequence x appears in training data). As the number of distinct n-gram counts grows exponentially in n, it was typically set to a small value. Count-based models have a clear dependence on context: any token within the last n words that also appears in a training n-gram is relevant, anything further back is not.

Subsequent models improved on these by allowing the use of skip-grams, caches, and feature-based models (Goodman, 2001; Bengio et al., 2003). Some of these in principle allowed the use of unlimited-length contexts, but only by imposing strong restrictions on the ways in which context features could interact.

## Context in RNN LMs

[p. 8] Recurrent neural network language models (Mikolov et al., 2010; Elman, 1990) provide a more expressive mechanism for the use of long-range context: models write to a recurrent "state vector" which can be carried arbitrarily far into the future. Computational issues limit the effective context size such models can be practically trained on, but this size is still significantly greater the models mentioned above: as previously noted, Khandelwal et al. (2018) revealed influence from up to 200 tokens of context. Similar effects are reported by Sankar et al. (2019) for neural dialogue models, and Li et al. (2016) describe an alternative procedure for ablating contexts.

## Context in Transformer LMs

[p. 8-9] Transformers introduce yet another mechanism for extracting information from long-range context: attention. Attention is also used with RNNs, but typically with just a single head -- the hidden state still carries most of the information. In transformers, context enters into predictions primarily via unbounded random access. These models appear to benefit from significantly longer contexts than previous models.

Some recent work investigates the behavior of individual transformer attention heads (Clark et al., 2019; Voita et al., 2019). This work finds that certain attention heads are sensitive to things like word frequency, positional information, and certain syntactic phenomena. While extremely informative about the computational structures implemented by fixed models, these approaches do not necessarily reveal anything about usable information:

> "indeed, patterns of attention do not necessarily correlate with model predictions" (Jain and Wallace, 2019). [p. 9]

## Other related work

[p. 9] The finding that fine-grained ordering information contributes little usable information is consistent with Rae et al. (2019)'s finding that long-range contexts could be informatively summarized in fixed-sized vectors; the finding that most usable information is carried by nouns is consistent with earlier findings about both specialized neural architectures (Henaff et al., 2016) and discourse representations in feature-based models (Barzilay and Lapata, 2008). The approach also shares similar motivations to information-theoretic work on *probing* (Voita and Titov, 2020; Pimentel et al., 2020), which uses related tools to interpret linguistic structure in LM representations rather than characterizing their effect on LM predictions.

Several recent papers have explored the effect of training-time and test-time ablations in models for other data analysis tasks: Pham et al. (2020) find that shuffling experiments have a limited effect on the accuracy of models for natural language inference, while Perez et al. (2021) describe several experiments aimed at *introducing* usable information for several question answering and sentence understanding tasks.
