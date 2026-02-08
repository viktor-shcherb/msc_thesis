# 2 Related Work [p. 2-3]

## Language modeling advances

In recent years, significant advances in language modeling include: [p. 2]
- Novel architectures to better encode context (Bengio et al., 2003; Mikolov et al., 2010; Merity et al., 2016; Al-Rfou et al., 2018)
- Improving regularization and optimization algorithms (Gal and Ghahramani, 2016)
- Speeding up the Softmax computation (Grave et al., 2016a)
- Enriching the output distribution family (Yang et al., 2017)

## Long-range context

A line of work directly feeds a representation of the wider context into the network as an additional input. Existing works range from manually defined context representations (Mikolov and Zweig, 2012; Ji et al., 2015; Wang and Cho, 2015) to others that rely on document-level topics learned from data (Dieng et al., 2016; Wang et al., 2017). [p. 2-3]

## Long-term dependency in generic sequence modeling

A long-standing research problem. Since the ubiquitous adoption of LSTM, many efforts have been spent on: [p. 3]
- Relieving the vanishing gradient problem, including better initialization (Le et al., 2015), additional loss signal (Trinh et al., 2018), augmented memory structure (Ke et al., 2018)
- Modifying the internal architecture of RNNs to ease optimization (Wu et al., 2016; Li et al., 2018)

The authors note their work is different: it is based on the Transformer architecture and shows that language modeling as a real-world task benefits from the ability to learn longer-term dependency. [p. 3]
