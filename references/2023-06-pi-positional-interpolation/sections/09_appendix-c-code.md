# Appendix C: Code [p. 17–18]

## C.1 Code for Fig. 2 [p. 17]

[p. 17] Python code using PyTorch to generate Figure 2 (extrapolation vs. interpolation visualization). The code:

1. Builds basis functions with $d = 4096 // 32 = 128$, $\theta = 10000$, and frequencies $\theta_j = 1/(\theta^{2j/d})$.
2. Constructs a basis function matrix for positions $[0, L)$ where $L = 2048$.
3. Fits random data points $y$ via linear regression with regularization $\epsilon = 0.0$ (least squares).
4. Evaluates the fitted function over $[0, 2L)$ to show extrapolation behavior (panel 2).
5. Evaluates the fitted function over a fine-grained grid $[25, 75)$ with step 0.125 to show interpolation behavior (panel 3).
6. Plots three subplots: (1) attention score within $[0, L]$, (2) effect of extrapolation showing the function shooting up beyond $L$, (3) effect of interpolation showing smooth behavior between integer positions.

```python
# build basis function
d = 4096 // 32
theta = 10000
# Frequency computation,
freqs = 1.0 / (theta ** (torch.arange(0, d, 2)[: (d // 2)].float() / d))

# construct basis function
L = 2048

x = torch.zeros(L)
x[:L] = torch.arange(0, L)

# basis functions
xfreq = torch.outer(x, freqs)

y = torch.randn(x.shape[0])

# do linear regression
X = torch.cat([xfreq.sin(), xfreq.cos()], dim=1)

eps = 0.000
coeffs = torch.linalg.solve(X.t() @ X + torch.eye(X.shape[1]) * eps, X.t() @ y)

x2 = torch.arange(0, 2*L)
xfreq2 = torch.outer(x2, freqs)
X2 = torch.cat([xfreq2.sin(), xfreq2.cos()], dim=1)

y2 = X2 @ coeffs

x3 = torch.arange(25, 75, 0.125)
xfreq3 = torch.outer(x3, freqs)
X3 = torch.cat([xfreq3.sin(), xfreq3.cos()], dim=1)

y3 = X3 @ coeffs

plt.figure(figsize=(16,5))

plt.subplot(1, 3, 1)
plt.plot(x2[:L], y2[:L], "r")
plt.scatter(x, y)
plt.ylabel("attention score $a(s)$")
plt.xlabel("Positional difference $s$")

plt.subplot(1, 3, 2)

plt.plot(x2, y2, "r")
plt.scatter(x, y)
plt.axvline(L, color="k", linestyle="--", linewidth=0.5)

plt.title("Effect of Extrapolation")
plt.xlabel("Positional difference $s$")


plt.subplot(1, 3, 3)
plt.plot(x3, y3, "r")
for i in range(25,75):
    plt.axvline(i, color="k", linestyle="--", linewidth=0.5)
plt.title("Effect of Interpolation")
plt.xlabel("Positional difference $s$")
plt.show()
```

## C.2 Code for Fig. 5 [p. 18]

[p. 18] Python code using PyTorch to generate Figure 5 (visualization of the extrapolation bound quantity $B(s)/d$). The code:

1. Uses $L = 2048$, positions $[0, 2L)$, $d = 4096 // 32 = 128$, $\theta = 10000$.
2. Computes $|A_k(s)|$ via cumulative sums of sine and cosine components, then takes the magnitude.
3. Sums these magnitudes to get $B(s)$ and divides by $d$.
4. Plots $B(s)/d$ versus positional difference $s$ with a horizontal dashed line at 1.0.

```python
L = 2048
x = torch.arange(0, 2*L)
d = 4096 // 32
theta = 10000
freqs = 1.0 / (theta ** (torch.arange(0, d, 2)[: (d // 2)].float() / d))

xfreq = torch.outer(x, freqs)

mags = (xfreq.sin().cumsum(dim=1).pow(2) + xfreq.cos().cumsum(dim=1).pow(2)).sqrt()

plt.plot(mags.sum(dim=1)/d)
plt.axhline(1.0, color='k', linestyle='--')
plt.xlabel("Positional difference $s$")
plt.ylabel("$B(s)/d$")
plt.show()
```
