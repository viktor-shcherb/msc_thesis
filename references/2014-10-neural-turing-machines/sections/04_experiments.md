# 4 Experiments [p. 10-13]

[p. 10] This section presents preliminary experiments on a set of simple algorithmic tasks such as copying and sorting data sequences. The goal was not only to establish that NTM is able to solve the problems, but also that it is able to do so by learning compact internal programs. The hallmark of such solutions is that they generalise well beyond the range of the training data. For example, the authors were curious to see if a network trained to copy sequences of length up to 20 could copy a sequence of length 100 with no further training.

For all the experiments, three architectures were compared:
1. NTM with a feedforward controller
2. NTM with an LSTM controller
3. A standard LSTM network

Because all the tasks were episodic, the dynamic state of the networks was reset at the start of each input sequence. For the LSTM networks, this meant setting the previous hidden state equal to a learned bias vector. For NTM, the previous state of the controller, the value of the previous read vectors, and the contents of the memory were all reset to bias values.

All the tasks were supervised learning problems with binary targets; all networks had logistic sigmoid output layers and were trained with the cross-entropy objective function. Sequence prediction errors are reported in bits-per-sequence. For more details about the experimental parameters see Section 4.6.

## 4.1 Copy [p. 10-13]

[p. 10] The copy task tests whether NTM can store and recall a long sequence of arbitrary information. The network is presented with an input sequence of random binary vectors followed by a delimiter flag. Storage and access of information over long time periods has always been problematic for RNNs and other dynamic architectures. The authors were particularly interested to see if an NTM is able to bridge longer time delays than LSTM.

The networks were trained to copy sequences of eight bit random vectors, where the sequence lengths were randomised between 1 and 20. The target sequence was simply a copy of the input sequence (without the delimiter flag). No inputs were presented to the network while it receives the targets, to ensure that it recalls the entire sequence with no intermediate assistance.

[p. 11] As can be seen from Figure 3, NTM (with either a feedforward or LSTM controller) learned much faster than LSTM alone, and converged to a lower cost. The disparity between the NTM and LSTM learning curves is dramatic enough to suggest a qualitative, rather than quantitative, difference in the way the two models solve the problem.

**Figure 3** (p. 11): "Copy Learning Curves."
The figure shows learning curves plotting cost per sequence (bits) on the y-axis (range 0-10) against sequence number (thousands) on the x-axis (range 0-1000). Three curves are shown: LSTM (blue, with cross markers), NTM with LSTM Controller (green, with square markers), and NTM with Feedforward Controller (red, with triangle markers). LSTM starts around 8-10 bits and slowly decreases, remaining above ~2 bits even after 1000k sequences. Both NTM variants drop rapidly to near 0 within the first ~200k sequences, with the feedforward NTM converging slightly faster.

The authors also studied the ability of the networks to generalise to longer sequences than seen during training (that they can generalise to novel vectors is clear from the training error). Figures 4 and 5 demonstrate that the behaviour of LSTM and NTM in this regime is radically different. NTM continues to copy as the length increases (footnote 2: the limiting factor was the size of the memory, 128 locations, after which the cyclical shifts wrapped around and previous writes were overwritten), while LSTM rapidly degrades beyond length 20.

The preceding analysis suggests that NTM, unlike LSTM, has learned some form of copy algorithm. To determine what this algorithm is, the authors examined the interaction between the controller and the memory (Figure 6). The authors believe that the sequence of operations performed by the network can be summarised by the following pseudocode:

```
initialise: move head to start location
while input delimiter not seen do
    receive input vector
    write input to head location
    increment head location by 1
end while
return head to start location
while true do
    read output vector from head location
    emit output
    increment head location by 1
end while
```

This is essentially how a human programmer would perform the same task in a low-level programming language.

**Figure 4** (p. 12): "NTM Generalisation on the Copy Task. The four pairs of plots in the top row depict network outputs and corresponding copy targets for test sequences of length 10, 20, 30, and 50, respectively. The plots in the bottom row are for a length 120 sequence. The network was only trained on sequences of up to length 20. The first four sequences are reproduced with high confidence and very few mistakes. The longest one has a few more local errors and one global error: at the point indicated by the red arrow at the bottom, a single vector is duplicated, pushing all subsequent vectors one step back. Despite being subjectively close to a correct copy, this leads to a high loss."
The figure shows two rows of heatmaps. Top row: four pairs of Targets/Outputs for lengths 10, 20, 30, and 50 — the NTM reproduces all four faithfully. Bottom row: one pair of Targets/Outputs for length 120 — mostly correct but with one global duplication error partway through. The network was trained only up to length 20, demonstrating strong generalisation.

**Figure 5** (p. 13): "LSTM Generalisation on the Copy Task. The plots show inputs and outputs for the same sequence lengths as Figure 4. Like NTM, LSTM learns to reproduce sequences of up to length 20 almost perfectly. However it clearly fails to generalise to longer sequences. Also note that the length of the accurate prefix decreases as the sequence length increases, suggesting that the network has trouble retaining information for long periods."
The figure shows the same layout as Figure 4 but for LSTM. Top row: four pairs for lengths 10, 20, 30, 50 — LSTM handles length 10 and 20 but deteriorates for 30 and 50. Bottom row: length 120 — LSTM output diverges rapidly from the target after an initial correct prefix.

**Figure 6** (p. 13): "NTM Memory Use During the Copy Task. The plots in the left column depict the inputs to the network (top), the vectors added to memory (middle) and the corresponding write weightings (bottom) during a single test sequence for the copy task. The plots on the right show the outputs from the network (top), the vectors read from memory (middle) and the read weightings (bottom). Only a subset of memory locations are shown. Notice the sharp focus of all the weightings on a single location in memory (black is weight zero, white is weight one). Also note the translation of the focal point over time, reflects the network's use of iterative shifts for location-based addressing, as described in Section 3.3.2. Lastly, observe that the read locations exactly match the write locations, and the read vectors match the add vectors. This suggests that the network writes each input vector in turn to a specific memory location during the input phase, then reads from the same location sequence during the output phase."
The figure has two columns (Write Weightings, Read Weightings) each with three rows: Inputs/Outputs (top), Adds/Reads (middle), Location weightings (bottom). The write weightings show a sharp diagonal line moving through memory locations as vectors are stored. The read weightings show the same diagonal pattern during the output phase. Add vectors match input vectors; read vectors match add vectors.

[p. 12] In terms of data structures, the authors state that NTM has learned how to create and iterate through arrays. The algorithm combines both content-based addressing (to jump to start of the sequence) and location-based addressing (to move along the sequence). The iteration would not generalise to long sequences without the ability to use relative shifts from the *previous* read and write weightings (Equation 7), and without the focus-sharpening mechanism (Equation 9) the weightings would probably lose precision over time.
