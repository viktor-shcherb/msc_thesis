# Argument 4: Despite being defined narrowly as copying random sequences, induction heads can implement surprisingly abstract types of in-context learning [p. 19-21]

## Strength of argument for sub-claims [p. 19]

|                      | Small Attention-Only | Small with MLPs | Large Models |
|----------------------|----------------------|-----------------|--------------|
| Contributes Some     |                      |                 | Plausibility |
| Contributes Majority |                      |                 | Plausibility |

Note: The Small Attention-Only and Small with MLPs columns are left blank (grayed out in the original). This argument applies specifically to large models. [p. 19]

## Motivation [p. 19]

All of the previous evidence (in Arguments 1-3) focused on observing or perturbing the connection between induction head formation and macroscopic in-context learning. A totally different angle is to find examples of induction heads implementing seemingly-difficult in-context learning behaviors; this would make it plausible that induction heads account for the majority of in-context learning. This evidence applies even to the very largest models (and the authors study up to 12B parameter models), but since it shows only a small number of tasks, it is only suggestive regarding in-context learning in general. [p. 19]

Recall that induction heads are defined as heads that empirically copy arbitrary token sequences using a "prefix matching" attention pattern. The goal is to find heads that meet this definition but *also* perform more interesting and sophisticated behaviors, essentially showing that induction heads in large models can be "generalizable". [p. 19]

---
[p. 20 continued]

## Approach [p. 20]

In this argument, anecdotal examples of induction heads from larger transformers are shown (the 40-layer model with 13 billion parameters) that exhibit exactly such behaviors -- namely literal copying, translation, and a specific type of abstract pattern matching. The behaviors are all of the form `[A*][B*]...[A][B]`, aka the "fuzzy nearest neighbor match" or "find something similar early in the sequence and complete the sequence in analogy". The authors verify that these heads score highly on their "copying" and "prefix matching" evaluations (that is, they increase the probability of the token they attend to, and attend to tokens where the prefix matches the present token on random text), and are thus "induction heads" by their strict empirical definition, at the same time as they *also* perform these more sophisticated tasks. [p. 20]

## Example heads summary table [p. 20]

| Head                  | Layer Depth | Copying score (?) | Prefix matching score (?) |
|-----------------------|-------------|--------------------|---------------------------|
| Literal copying head  | 21 / 40     | 0.89               | 0.75                      |
| Translation head      | 7 / 40      | 0.20               | 0.85                      |
| Pattern-matching head | 26 / 40     | 0.69               | 0.94                      |

Note: The "(?)" markers next to "Copying score" and "Prefix matching score" appear in the original table headers, likely indicating links to definitions in the HTML article. [p. 20]

## Behavior 1: Literal sequence copying [p. 20-21]

The simplest case is a head that literally copies repeated text, to get familiar with the visualization interface and the basic dynamics of these heads. An induction head is selected which seems to perform very basic copying behavior, and its behavior is examined on the first paragraph of Harry Potter. The first few sentences are repeated afterwards to show the head's behavior on longer segments of repeated text. **For the following interactive visualizations, the authors recommend visiting the HTML article.** [p. 20]

The visualization shows two different things:
- In red, "Attention" lets you see where the head is attending to predict the *next* token.
- In blue, "Logit attr" shows the earlier tokens that contributed to the prediction of the *current* token, using "direct-path" logit attribution.^21 [p. 20]

---
[p. 21 continued]

The visualization is explored by visiting the HTML article and hovering the cursor over the second paragraph. [p. 21]

**Figure 12** (p. 21): "Literal sequence copying visualization." Shows the first paragraph of Harry Potter text displayed with attention and logit attribution highlighting. The text begins with `<EOT>Mr and Mrs Dursley, of number four, Privet Drive, were proud to say that they were perfectly normal, thank you very much.` The full paragraph continues through multiple sentences. Below the first paragraph, the same text is repeated (starting with `Mr and Mrs Dursley, of number four, Privet Drive...`). The visualization has two toggle buttons: "Attention" (red) and "Logit attr" (blue). "Selected is **source**" mode is shown.

Key observations from the visualization:
- Tokens in red highlight show attention patterns, where the head attends back to previous instances of the same text.
- The head predicts repeating the names "Dursley" and "Potters"; the phrase "a small son"; and then the entire repeated sentences at the end.
- In all cases, these successful predictions are made by attending back to a previous instance where this phrase was present in the text. [p. 21]

## Behavior 2: Translation [p. 21-22]

It is a well-known result that language models can translate between languages. Intriguingly, the authors have encountered many examples of induction heads that can do translation. A head found in layer 7 of the 40-layer model is explored, showcasing translation between English, French, and German. (As with the others in this section, this head is *also* an "induction head" by the same definition the authors have been using all along, because when shown repeated *random* tokens, it uses a "prefix matching" attention pattern to copy the sequence verbatim.) [p. 21]

**Figure 13** (p. 22): "Translation head visualization." Shows the attention pattern and logit attribution for a head in layer 7 of the 40-layer model. The input text contains three parallel sentences:
- `EN: This is the largest temple that I've ever seen.`
- `FR: C'est le plus grand temple que j'ai jamais vu.`
- `DR: Das ist der größte Tempel, den ich je gesehen habe.`

The attention pattern (in red, top left) is more or less an "off-diagonal" pattern, but it meanders a little bit away from a sharp diagonal. The meandering is because different languages have different word order and token lengths. As this head attends sequentially to past tokens that will semantically come next, the attended token position in the earlier sentences jumps around. [p. 22]

The logit attribution patterns for this head are not perfectly sharp; that is, even in cases where the attention head is attending to the matching word in an earlier language, it does not always *directly* increase the logit of the corresponding prediction. The authors guess that this is because this head's output needs to be further processed by later layers. However, taken overall, the direct logit attributions show clear evidence of contributing on net to the correct translation. [p. 22]

## Behavior 3: Pattern matching [p. 22-23]

In this final example, an attention head (found at layer 26 of the 40-layer model) is shown which does more complex pattern matching. One might even think of it as learning a simple function in context. (Again, this head *also* scores highly on the authors' measurements of "basic" induction behavior when shown repeated random sequences, so it is an induction head by that definition.) [p. 22]

To explore this behavior, some synthetic text is generated which follows a simple pattern. Each line follows one of four templates, followed by a label for which template it is drawn from. The template is random selected, as are the words which fill in the template: [p. 22]

- (month) (animal): 0
- (month) (fruit): 1
- (color) (animal): 2
- (color) (fruit): 3

Below, the attention head's behavior on this synthetic example is shown. To make the diagram easier to read, the attention pattern is masked to only show the ":" tokens as the destination, and the logit attribution to only show where the output is the integer tokens. [p. 22]

**Figure 14** (p. 23): "Pattern matching head visualization." Shows the attention pattern and logit attribution for a head at layer 26 of the 40-layer model, applied to the synthetic template text. The input text displays many lines such as:
- `<EOT>June grape: 1`
- `blue pear: 3`
- `July bird: 0`
- `gray strawberry: 3`
- `January kiwi: 1`
- `purple pineapple: 3`
- `September strawberry: 1`
- `March snake: 0`
- `April frog: 0`
- `purple frog: 2`
- `June lion: 0`
- `September lion: 0`
- `March fish: 0`
- `purple snake: 2`
- `October monkey: 0`
- `blue cherry: 3`
- `July lion: 0`
- `purple strawberry: 3`
- `yellow snake: 2`
- `gray pineapple: 3`
- `March fish: 0`
- `April lion: 0`
- `green lizard: 2`
- `blue lizard: 2`
- `June monkey: 0`
- `yellow kiwi: 3`
- `October cherry: 1`
- `yellow lion: 2`

The attention pattern shows the head attending back to previous instances of the correct category more often than not. It often knows to skip over lines where one of the words is identical but the pattern is wrong (such as "January bird" primarily attending to "April fish" and not "grey bird"). This head is not perfect at this, but empirically it allocates about 65% of its attention from the colons to the correct positions, when tested on a range of similar problems. [p. 23]

## What's going on with more abstract heads that are also induction heads? [p. 24]

The authors emphasize that the attention heads described above simultaneously implement *both* the abstract behaviors described, and these *very same* attention heads (as in, the exact same head in the same layer) *also* satisfy the formal definition of induction head (literal copying of random sequences using prefix matching). The comparison is not a metaphor or a blurring of the definition: induction heads which are *defined* by their ability to copy literal sequences *turn out to also* sometimes match more abstract patterns. This is what the table at the beginning of the section shows empirically. [p. 24]

But this still leaves the question: *why* do the same heads that inductively copy random text also exhibit these other behaviors? One hint is that these behaviors can be seen as "spiritually similar" to copying. Recall that where an induction head is defined as implementing a rule like `[A][B] ... [A] -> [B]`, the empirically observed heads also do something like `[A*][B*] ... [A] -> [B]` where `A*` and `B*` are similar to `A` and `B` in some higher-level representation. There are several ways these similar behaviors could be connected. For example, note that the first behavior is a special case of the second, so perhaps induction heads are implementing a more general algorithm that reverts to the special case of copying when given a repeated sequence.^22 Another possibility is that induction heads implement literal copying when they take a path through the residual stream that includes only them, but implement more abstract behaviors when they process the outputs of earlier layers that create more abstract representations (such as representations where the same word in English and French are embedded in the same place). [p. 24]

In Argument 5 the authors strengthen this argument by giving a mechanistic account of how induction heads (when doing simple copying with prefix-matching) attend back to the token that comes next in the pattern, and observe that the actual mechanism they use could naturally generalize to more abstract pattern matching. The point in this section is just that it is actually quite natural for these more abstract induction heads to also exhibit the basic copying behaviors underlying their definition. [p. 24]
