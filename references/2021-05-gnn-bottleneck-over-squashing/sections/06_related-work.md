# 6 Related Work [p. 9]

## Under-reaching

[p. 9] Barcelo et al. (2020) found that the expressiveness of GNNs captures only a small fragment of first-order logic. The main limitation arises from the inability of a node to be aware of nodes that are farther away than the number of layers $K$, while the existence of such nodes *can* be easily described using logic. This limitation is denoted as *under-reaching*. Nevertheless, even when information is reachable within $K$ edges, that information might be over-squashed along the way. Thus, the *over-squashing* limitation described in this paper is *tighter* than *under-reaching*.

## Over-smoothing

[p. 9] As observed before, node representations become indistinguishable and prediction performance severely degrades as the number of layers increases. The accepted explanation to this phenomenon is *over-smoothing* (Li et al., 2018; Wu et al., 2020; Oono and Suzuki, 2020). This might explain the empirical optimality of few layers in short-range tasks (e.g., only $K=2$ layers in Kipf and Welling (2017)). Nonetheless, some problems depend on longer-range information propagation and thus *require* more layers, to avoid *under-reaching*. The authors hypothesize that in long-range problems, the explanation for the degraded performance is *over-squashing* rather than *over-smoothing*. For further discussion of over-smoothing vs. over-squashing, see Appendix E.

## Avoiding over-squashing

[p. 9] Some previous work avoids over-squashing by various profitable means: Gilmer et al. (2017) add "virtual edges" to shorten long distances; Scarselli et al. (2008) add "supersource nodes"; and Allamanis et al. (2018) designed program analyses that serve as 16 "shortcut" edge types. However, none of these explicitly explained these solutions using over-squashing, and did not identify the bottleneck and its negative cross-domain implications.
