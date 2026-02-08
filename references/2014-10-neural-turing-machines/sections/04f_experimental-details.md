# 4.6 Experimental Details [p. 21–23]

[p. 21] For all experiments, the *RMSProp* algorithm was used for training in the form described in (Graves, 2013) with momentum of 0.9. Tables 1 to 3 give details about the network configurations and learning rates used in the experiments. All LSTM networks had three stacked hidden layers. Note that the number of LSTM parameters grows quadratically with the number of hidden units (due to the recurrent connections in the hidden layers). [p. 22] This contrasts with NTM, where the number of parameters does not increase with the number of memory locations. During the training backward pass, all gradient components are clipped elementwise to the range (-10, 10).

## Table 1: NTM with Feedforward Controller Experimental Settings [p. 22]

| Task | #Heads | Controller Size | Memory Size | Learning Rate | #Parameters |
|---|---|---|---|---|---|
| Copy | 1 | 100 | 128 x 20 | 10^-4 | 17,162 |
| Repeat Copy | 1 | 100 | 128 x 20 | 10^-4 | 16,712 |
| Associative | 4 | 256 | 128 x 20 | 10^-4 | 146,845 |
| N-Grams | 1 | 100 | 128 x 20 | 3 x 10^-5 | 14,656 |
| Priority Sort | 8 | 512 | 128 x 20 | 3 x 10^-5 | 508,305 |

## Table 2: NTM with LSTM Controller Experimental Settings [p. 23]

| Task | #Heads | Controller Size | Memory Size | Learning Rate | #Parameters |
|---|---|---|---|---|---|
| Copy | 1 | 100 | 128 x 20 | 10^-4 | 67,561 |
| Repeat Copy | 1 | 100 | 128 x 20 | 10^-4 | 66,111 |
| Associative | 1 | 100 | 128 x 20 | 10^-4 | 70,330 |
| N-Grams | 1 | 100 | 128 x 20 | 3 x 10^-5 | 61,749 |
| Priority Sort | 5 | 2 x 100 | 128 x 20 | 3 x 10^-5 | 269,038 |

## Table 3: LSTM Network Experimental Settings [p. 23]

| Task | Network Size | Learning Rate | #Parameters |
|---|---|---|---|
| Copy | 3 x 256 | 3 x 10^-5 | 1,352,969 |
| Repeat Copy | 3 x 512 | 3 x 10^-5 | 5,312,007 |
| Associative | 3 x 256 | 10^-4 | 1,344,518 |
| N-Grams | 3 x 128 | 10^-4 | 331,905 |
| Priority Sort | 3 x 128 | 3 x 10^-5 | 384,424 |
