# 4.5 Priority Sort [p. 19–22]

[p. 19] This task tests whether the NTM can sort data -- an important elementary algorithm. A sequence of random binary vectors is input to the network along with a scalar priority rating for each vector. The priority is drawn uniformly from the range [-1, 1]. The target sequence contains the binary vectors sorted according to their priorities, as depicted in Figure 16.

Each input sequence contained 20 binary vectors with corresponding priorities, and each target sequence was the 16 highest-priority vectors in the input.^5

> ^5 "We limited the sort to size 16 because we were interested to see if NTM would solve the task using a binary heap sort of depth 4." [p. 19]

**Figure 16** (p. 21): "Example Input and Target Sequence for the Priority Sort Task. The input sequence contains random binary vectors and random scalar priorities. The target sequence is a subset of the input vectors sorted by the priorities."
The figure shows an input block of binary vectors with priority values (labelled 5, 7, 4, 6, 3, 2, 1 in descending priority) connected by an arrow to a target block of binary vectors labelled 1, 2, 3, 4, 5, 6, 7... in sorted order. The input has random binary patterns; the target shows the same patterns reordered by priority.

## Memory use analysis [p. 21]

[p. 21] Inspection of NTM's memory use led the authors to hypothesise that it uses the priorities to determine the relative location of each write. To test this hypothesis they fitted a linear function of the priority to the observed write locations. Figure 17 shows that the locations returned by the linear function closely match the observed write locations. It also shows that the network reads from the memory locations in increasing order, thereby traversing the sorted sequence.

**Figure 17** (p. 21): "NTM Memory Use During the Priority Sort Task. Left: Write locations returned by fitting a linear function of the priorities to the observed write locations. Middle: Observed write locations. Right: Read locations."
Three panels, each with Location on the y-axis and Time on the x-axis. Left panel (Hypothesised Locations): a scatter of dots arranged approximately linearly, showing the predicted write locations from the linear fit. Middle panel (Write Weightings): actual write weightings show a similar scatter pattern matching the hypothesised locations closely. Right panel (Read Weightings): a clean diagonal line from bottom-left to top-right, showing the network reads memory locations in sequential (increasing) order during the output phase.

## Learning curves [p. 21–22]

[p. 21] The learning curves in Figure 18 demonstrate that NTM with both feedforward and LSTM controllers substantially outperform LSTM on this task. Note that eight parallel read and write heads were needed for best performance with a feedforward controller on this task; this may reflect the difficulty of sorting vectors using only unary vector operations (see Section 3.4).

**Figure 18** (p. 22): "Priority Sort Learning Curves."
The figure plots cost per sequence (bits) on the y-axis (range 0–140) against sequence number (thousands) on the x-axis (range 0–1000). Three curves are shown: LSTM (blue, cross markers), NTM with LSTM Controller (green, square markers), NTM with Feedforward Controller (red, triangle markers). LSTM starts around 80–90 bits and converges slowly to approximately 50 bits after 1M sequences. Both NTM variants drop rapidly, converging to near 0 bits (approximately 10–20 bits) within the first 200–400k sequences. NTM with both controller types substantially outperforms LSTM.
