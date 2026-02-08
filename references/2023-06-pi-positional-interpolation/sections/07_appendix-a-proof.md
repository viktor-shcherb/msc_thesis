# Appendix A: Proof [p. 15]

## Theorem 2.1 (Interpolation bound)

[p. 15] For attention score $a(s) = \mathrm{Re}\left[\sum_{j=0}^{d/2-1} h_j e^{\mathrm{i}s\theta_j}\right]$, where $\theta_j = c^{-2j/d}$, its interpolation value $a(s)$ for $s \in [s_1, s_2]$ is bounded as follows:

$$|a(s) - a_{\text{linear}}(s)| \leq d \left(\max_j |h_j|\right) \frac{(s - s_1)(s_2 - s)}{8 \ln c} \tag{5}$$

where $a_{\text{linear}}(s)$ is the linear interpolation of two grid point $a(s_1)$ and $a(s_2)$ that are known to behave well, enforced by LLM pre-training:

$$a_{\text{linear}}(s) := (1 - \lambda(s))a(s_1) + \lambda(s)a(s_2), \qquad \lambda(s) := \frac{s - s_1}{s_2 - s_1} \tag{6}$$

## Proof

[p. 15] Using Taylor expansion, we have:

$$a(s_1) = a(s) + a'(s)(s_1 - s) + \frac{1}{2}a''(\xi_1)(s - s_1)^2 \tag{9}$$

$$a(s_2) = a(s) + a'(s)(s - s_2) + \frac{1}{2}a''(\xi_2)(s - s_2)^2 \tag{10}$$

where $\xi_1 \in [s_1, s]$ and $\xi_2 \in [s, s_2]$. Multiplying Eqn. 9 with $s - s_2$ and Eqn. 10 with $s - s_1$ and subtract, we get:

$$a(s) - a_{\text{linear}}(s) = R(s) := -\frac{(s - s_1)(s - s_2)}{2(s_1 - s_2)} \left[a''(\xi_1)(s - s_1) - a''(\xi_2)(s - s_2)\right] \tag{11}$$

Now we bound the second order derivative $a''(s)$. Note that for any complex number $x$, $|\mathrm{Re}(x)| \leq |x|$ so we have:

$$|a''(s)| \leq \sum_{j=0}^{d/2-1} |h_j||\phi_j''(s)| \leq \sum_{j=0}^{d/2-1} |h_j|\theta_j^2 \tag{12}$$

$$\leq \left(\max_j |h_j|\right) \sum_{j=0}^{d/2-1} c^{-4j/d} = \left(\max_j |h_j|\right) \frac{1}{1 - c^{-4/d}} \tag{13}$$

Note that when $x < 0$ and $c > 1$, $c^x \leq 1 + x \ln c$, therefore $c^{-4/d} \leq 1 - 4/d \ln c$ and we have:

$$\frac{1}{1 - c^{-4/d}} \leq \frac{1}{4/d \ln c} = \frac{d}{4 \ln c} \tag{14}$$

So

$$|a''(s)| \leq \left(\max_j |h_j|\right) \frac{d}{4 \ln c} =: M \tag{15}$$

Let the above bound to be $M$, we have:

$$|R(s)| \leq \frac{(s - s_1)(s_2 - s)}{2(s_2 - s_1)} \left[M(s - s_1) + M(s_2 - s)\right] = \frac{M}{2}(s - s_1)(s_2 - s) \tag{16}$$

As a result:

$$|a(s) - a_{\text{linear}}(s)| = |R(s)| \leq d \left(\max_j |h_j|\right) \frac{(s - s_1)(s_2 - s)}{8 \ln c} \tag{17}$$

$\square$
