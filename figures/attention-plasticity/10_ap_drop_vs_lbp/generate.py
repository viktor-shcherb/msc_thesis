"""ap_drop vs LongBench Pro score scatter (7 matched models, family-colored)."""
import matplotlib.pyplot as plt
import numpy as np

# --- Data (from 05_benchmark_connection.md Table 1) ---
models = [
    ("Ministral3-14B", 40.14, 0.068, "Ministral"),
    ("Ministral3-8B",  37.80, 0.082, "Ministral"),
    ("Qwen3-14B",      37.11, 0.161, "Qwen"),
    ("Qwen3-8B",       33.41, 0.178, "Qwen"),
    ("Qwen3-4B",       31.26, 0.186, "Qwen"),
    ("Ministral3-3B",  30.18, 0.072, "Ministral"),
    ("Llama-3.2-3B",   15.71, 0.230, "Llama"),
]

family_colors = {
    "Ministral": "#2166ac",
    "Qwen":      "#b2182b",
    "Llama":     "#4dac26",
}
family_markers = {
    "Ministral": "o",
    "Qwen":      "s",
    "Llama":     "D",
}

fig, ax = plt.subplots(figsize=(5.5, 4.5))

# Plot by family for legend grouping
for family in ["Ministral", "Qwen", "Llama"]:
    subset = [(n, lbp, apd) for n, lbp, apd, f in models if f == family]
    names = [s[0] for s in subset]
    lbps  = [s[1] for s in subset]
    drops = [s[2] for s in subset]
    ax.scatter(drops, lbps, c=family_colors[family], marker=family_markers[family],
               s=80, zorder=5, label=family, edgecolors="white", linewidth=0.5)
    for name, apd, lbp in zip(names, drops, lbps):
        # Offset labels to avoid overlap
        ha, va, dx, dy = "left", "bottom", 0.004, 0.6
        if name == "Ministral3-3B":
            ha, va, dx, dy = "left", "top", 0.004, -0.6
        elif name == "Ministral3-8B":
            ha, va, dx, dy = "right", "bottom", -0.004, 0.6
        elif name == "Qwen3-14B":
            ha, va, dx, dy = "right", "bottom", -0.004, 0.6
        ax.annotate(name, (apd, lbp), xytext=(apd + dx, lbp + dy),
                    fontsize=7.5, ha=ha, va=va, color=family_colors[family])

# Trend line (all 7 points)
all_drops = [m[2] for m in models]
all_lbps  = [m[1] for m in models]
z = np.polyfit(all_drops, all_lbps, 1)
x_fit = np.linspace(0.05, 0.25, 100)
ax.plot(x_fit, np.polyval(z, x_fit), "--", color="gray", alpha=0.5, linewidth=1)

# Correlation
r = np.corrcoef(all_drops, all_lbps)[0, 1]
ax.text(0.97, 0.97, f"$r = {r:.2f}$", transform=ax.transAxes,
        ha="right", va="top", fontsize=10, color="gray",
        bbox=dict(boxstyle="round,pad=0.3", facecolor="white", edgecolor="gray", alpha=0.8))

ax.set_xlabel("$\\mathrm{AP}_{\\mathrm{drop}}$ (first 20% $-$ last 20%)", fontsize=11)
ax.set_ylabel("LongBench Pro Overall", fontsize=11)
ax.set_xlim(0.04, 0.26)
ax.set_ylim(12, 44)
ax.legend(fontsize=9, loc="upper right", bbox_to_anchor=(0.88, 0.98))
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig("/Users/Viktor/PycharmProjects/msc_thesis/figures/attention-plasticity/10_ap_drop_vs_lbp/figure.png",
            dpi=200, bbox_inches="tight")
plt.savefig("/Users/Viktor/PycharmProjects/msc_thesis/figures/attention-plasticity/10_ap_drop_vs_lbp/figure.pdf",
            bbox_inches="tight")
print(f"Done: 10_ap_drop_vs_lbp (r = {r:.3f})")
