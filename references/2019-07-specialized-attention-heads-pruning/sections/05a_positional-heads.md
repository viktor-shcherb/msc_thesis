# 5 Characterizing Heads [p. 4]

The authors investigate whether heads play consistent and interpretable roles within the model. By examining attention matrices of heads ranked highly by LRP, three functions are identified: [p. 4]

1. **Positional:** the head points to an adjacent token
2. **Syntactic:** the head points to tokens in a specific syntactic relation
3. **Rare words:** the head points to the least frequent tokens in a sentence

## 5.1 Positional Heads [p. 4-5]

> "We refer to a head as 'positional' if at least 90% of the time its maximum attention weight is assigned to a specific relative position (in practice either -1 or +1, i.e. attention to adjacent tokens)." [p. 4]

Such heads are shown in purple in Figures 1c for English-Russian, 2b for English-German, 2d for English-French and marked with the relative position. [p. 4-5]

The positional heads correspond to a large extent to the most confident heads and the most important heads as ranked by LRP. In fact, the average maximum attention weight exceeds 0.8 for every positional head for all language pairs considered. [p. 5]
