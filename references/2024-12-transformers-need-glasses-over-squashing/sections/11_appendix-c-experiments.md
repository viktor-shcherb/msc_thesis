# Appendix C: Experiments [p. 20-21]

The prompting done on Gemini 1.5 in our work does not require custom resources as we use hosted Gemini instances. We run a local version of Gemma 7B on modest hardware to analyse the internal representations.

## C.1 Experimental Details [p. 20]

We detail the way in which we execute the prompting for the various experiments.

### Counting experiments [p. 20]

For the sum experiment we prompt as:

> "Please perform the following sum: seq. Please give the answer on the final line exactly as 'The final answer to your maths question is: xxxx', where 'xxxx' is your answer."

For the ones and zero sequences, we similarly prompt as:

> "Please count the number of ones in the following sequence: seq. Please give the answer on the final line exactly as 'The final answer to your maths question is: xxxx', where 'xxxx is your answer."

For the word counting experiment, we prompt as:

> "Please count the number of times 'car' appears in the following sentence: 'seq'. Please give the answer on the final line exactly as 'The final answer to your maths question is: xxxx', where 'xxxx' is your answer."

For the CoT experiments, we supply examples of the form:

> "Let's think step by step, showing me your reasoning. Here are a few examples:
> 
> Please perform the following sum: 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1
> We divide the sum into groups of 5. (1 + 1 + 1 + 1 + 1) + (1 + 1 + 1 + 1 + 1) + 1 + 1
> The answer is then 2 * 5 + 2 = 12
> The final answer to your maths question is: 12
> 
> Please perform the following sum: 1 + 1 + 1 + 1 + 1 + 1
> We divide the sum into groups of 5.
> (1 + 1 + 1 + 1 + 1) + 1
> The answer is then 1 * 5 + 1 = 6
> The final answer to your maths question is: 6"

With similar strategies for the 4 experiments.

### Copying experiments [p. 20]

For the copying experiments, we use the following prompt:

> "Consider the following sequence: seq. What is the last digit in this sequence? Please answer exactly as 'The answer to your question is: <ANSWER>'"

and change appropriately the sequence as described.

[p. 21] We commit to releasing the code we have used to generate the prompts in the near future.

## C.2 Counting with Gemma [p. 21]

We report similar results for the counting experiments using Gemma [27] in Figure 6 and 7. Compared to Gemini 1.5, Gemma seems to answer less accurately on the counting prompts.

**Figure 6** (p. 21): "Gemma 7B LLMs being prompted to (i) sum 1+···+ 1(left), (ii) Count the number of ones in a sequence of 1s (center), and (iii) Count the number of ones in a sequence of ones and zeroes (the sequence is a Bernoulli sequence with probability of sampling a one being 0.7) (right)."

Description: Three-panel plot showing Gemma 7B counting performance
- Left panel: Shows performance on summing sequences of 1s, with accuracy degrading as sequence length increases
- Center panel: Shows accuracy of counting ones in a sequence of all 1s, similar degradation pattern with length
- Right panel: Shows counting ones in mixed 0/1 sequences (Bernoulli p=0.7), showing similar performance degradation
- All three panels suggest decreased accuracy as the counting task difficulty (sequence length) increases

**Figure 7** (p. 21): "Frequency of different outputs for Gemma 7B"

Description: Histogram or distribution plot
- Shows the distribution of different answer outputs produced by Gemma 7B on counting tasks
- Illustrates the variety of incorrect answers the model produces when it fails at counting
- Supports claim: Demonstrates the types of errors Gemma makes on counting tasks

## C.3 Synthetic Experiments on Representational Collapse [p. 21]

To provide further experimental evidence of representational collapse with other positional encodings, we experiment using the original sinusoidal embeddings from [30]. We sample key, query, and values from a Gaussian distribution with variance σ² = 1/d, with d the dimension of the embeddings. We set d = 64 and otherwise follow the exact structure of the decoder-only Transformer presented in the original Transformer paper. We experiment with a single attention layer and check the convergence of the representations of the final token between a sequence of length n and a sequence of length n+1 in which we simply copy the final token. We present the results in Figure 8. We see how also for sinusoidal PEs with key, queries, and values randomly sampled, the convergence still occurs.

**Figure 8** (p. 22): "Convergence behaviour with a synthetic Transformer experiment. We sample the key, query, and values from a Gaussian distribution and apply the traditional sinusoidal PEs from [30]. We apply a logarithmic scale on the y-axis."

Description: Convergence plot for synthetic Transformer experiment (y-axis in log-scale)
- Shows convergence of final token representations as sequence length n increases
- Compares sequences of length n vs n+1 (where n+1 has final token copied)
- Demonstrates that even with sinusoidal positional encodings (from original Transformer), representational collapse still occurs
- Uses d=64 dimensional embeddings, single attention layer, Gaussian-sampled parameters
- Supports claim: Representational collapse is not limited to specific positional encoding schemes

The authors test the decay of the total variation of the softmax distributions of two growing sequences, to experimentally verify Lemma B.2. They sample a sequence x of length n with values uniformly distributed in the range [0,1]. They then create x* by adding to the first k=200 elements of x noise which is uniformly sampled between [0, 0.1]. In Figure 9, they show how the total variation between their respective softmax distributions decays with the sequence length [p. 22].

**Figure 9** (p. 22): "Total variation decay of softmax distributions with growing sequence length. We sample n elements uniformly from [0,1] and then create a related sequence by taking its first k=200 and adding to these elements noise sampled uniformly from [0, 0.1]. We measure the total variation between their softmax distributions. It is clear how the total variation decays with length, in accordance with Lemma B.2. Error bars show minimum and maximum over 5 seeds."

Description: Line plot showing total variation decay
- X-axis: sequence length n
- Y-axis: total variation between softmax distributions
- Shows decay of total variation as sequence length increases
- Experimental verification of Lemma B.2
- Error bars indicate min/max over 5 random seeds
- Base sequence: n elements sampled uniformly from [0,1]
- Perturbed sequence: first k=200 elements have added noise uniform in [0, 0.1]
- Supports claim: Total variation between softmax distributions decays with growing sequence length

## C.4 Effect of Positional Encodings [p. 22-23]

The authors include a synthetic experiment where they verify the occurrence of the representational collapse phenomenon with different Positional Encodings, namely: Alibi [24], the original Absolute Positional Encodings (APE) [30], and No Positional Encodings (NoPE) [15]. In their synthetic experiment, they sample n queries and keys independently directly from a standard Gaussian. They then construct a related sequence of length n+1 by repeating its last element. They report the L1 distance between the two sequences after a single decoder-Transformer layer, as done for the other representational collapse experiments. They consider a Transformer with a hidden dimension of 64, a single attention head, and they apply normalisations to simulate layer norm. The Transformer is not trained, but only used to simulate the propagation of information of queries and keys sampled from a Gaussian distribution. The results are shown in Figure 10 [p. 22-23]. Representational collapse seems to occur with all 4 positional encodings, with the convergence of the representations happening at a similar sequence lengths [p. 23].

The authors highlight that their condition on the decay of RoPE necessary to fulfill the requirement of Theorem 4.2 is inspired by claims of the decay of RoPE coming from the original work by Su et al. [26]. However, recent work has shown that such claims may not be strictly always upheld [4], as the original claims relied on very specific conditions on the queries and keys. The authors are of the opinion; however, that the range of synthetic and real-world experiments in this work support their representational collapse claims in practice with RoPE. A more precise mathematical treatment of RoPE specifically is therefore left as future work [p. 23].

**Figure 10** (p. 23): "We sample n queries, keys, and values independently from a standard Gaussian, applying different positional encodings. We then construct sequences of length n+1, by repeating the n-th token. We report the L1 distance between the last tokens of the sequences of length n and n+1 after one decoder-only Transformer layer. We set the hidden dimension to 64, use a single attention head, and normalise appropriately to simulate the effects of LayerNorm. The y-axis is shown in log-scale."

Description: Multi-line plot comparing positional encodings
- Four positional encoding types compared: RoPE, Alibi [24], APE (Absolute Positional Encodings) [30], NoPE (No Positional Encodings) [15]
- X-axis: sequence length n
- Y-axis: L1 distance between final token representations (log-scale)
- Setup: hidden dimension d=64, single attention head, LayerNorm simulation
- All four encodings show representational collapse at similar sequence lengths
- Supports claim: Representational collapse is not specific to RoPE, occurs across different positional encoding schemes

## C.5 Ablation on Prompt Structure [p. 23]

The authors ablate the prompt structure specifically for the copying task. In particular, they consider the prompts: (Type 1) "What is the last digit of the following sequence? Please answer exactly as 'The answer to your question is: <ANSWER>' ". Here is the sequence: {seq} and (Type 2) "Please answer exactly as 'The answer to your question is: <ANSWER>'. What is the last digit of the following sequence? {seq}" [p. 23].

The results are presented in Figure 11. The authors find that the prompt indeed does affect the performance on the task, as the prompt affects the distribution of the attention over the layer. However, for both types of prompts, the model ends up failing, in accordance with their theory [p. 23].

They also show for completeness, in Figure 12, that representational collapse occurs in Gemma 7B also for the 'Type 1' prompt [p. 23].

**Figure 11** (p. 24): "Performance of a Gemini model on the following prompts: (Type 1) 'What is the last digit of the following sequence? Please answer exactly as 'The answer to your question is: <ANSWER>' '. Here is the sequence: {seq} and (Type 2) 'Please answer exactly as 'The answer to your question is: <ANSWER>'. What is the last digit of the following sequence? {seq}'"

Description: Comparison plot of prompt structure effects
- Compares two prompt types for the copying task on Gemini model
- Type 1: Question first, then instruction format
- Type 2: Instruction format first, then question
- Shows that prompt structure affects performance (different attention distributions)
- Both prompt types ultimately fail at longer sequences, consistent with theory
- Supports claim: While prompt engineering can shift performance, it cannot overcome representational collapse

**Figure 12** (p. 24): "Representational collapse in Gemma for the prompt: 'What is the last digit of the following sequence? Please answer exactly as 'The answer to your question is: <ANSWER>' '. Here is the sequence: {seq} and (Type 2) "

Description: Representational collapse visualization for Gemma 7B
- Shows representational collapse occurring in Gemma 7B model
- Uses Type 1 prompt structure
- Demonstrates that representational collapse is observable across different models (Gemini and Gemma) and prompt formats
- Supports claim: Representational collapse is a fundamental phenomenon, not artifact of specific prompt structure

## C.6 Local sliding window attention [p. 23-24]

A fundamental limitation of an attention mechanism that leverages the softmax function is that it cannot remain sharp, especially as the sequence length grows [31]. This is in fact a key intuition that the authors exploit to show their result on representational collapse [p. 23].

A good way to address representational collapse and the related phenomenon of over-squashing is then that of limiting the spread of the softmax function, by directly limiting the amount of tokens the attention mechanism pays attention to. This mechanism is often referred to as a local sliding window and is a major architectural change present in Gemma 2 [28]. The authors believe that such an architectural change elegantly addresses representational collapse and over-squashing at the source as it avoids the issues that come with growing token sequences – something which their theory often exploits [p. 23-24].
