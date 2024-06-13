# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Generate sample data with distinct performance trends for each subplot
ratios = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])

# Different patterns of performance for each subplot
performances = {
    "SPMotif-0.5": {
        "pna": np.linspace(0.6, 0.85, 10),
        "gin": np.linspace(0.5, 0.7, 10),
    },
    "SPMotif-0.7": {
        "pna": 0.75 + 0.05 * np.cos(2 * np.pi * ratios),
        "gin": 0.55 + 0.05 * np.sin(2 * np.pi * ratios),
    },
    "SPMotif-0.9": {"pna": 0.7 + 0.15 * ratios, "gin": 0.6 + 0.1 * ratios**2},
}

std_dev = {"pna": np.array([0.05] * 10), "gin": np.array([0.08] * 10)}
# Axes Limits and Labels
xlabel_value = "Ratio r"
xlim_values = [0.05, 1.05]
xticks_values = np.arange(0.1, 1.1, 0.1)

ylabel_value = "Performance"
ylim_values = [0.4, 0.9]
yticks_values = np.arange(0.4, 0.9, 0.1)

# Labels
labels = ["PNA", "GIN"]

# Titles
titles = ["SPMotif-0.5", "SPMotif-0.7", "SPMotif-0.9"]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Plot settings
fig, axs = plt.subplots(3, 1, figsize=(6, 12))
colors = ["#1f77b4", "#2ca02c"]
markers = ["o", "^"]

for i, ax in enumerate(axs):
    # Get specific data for this subplot
    pna_data = performances[titles[i]]["pna"]
    gin_data = performances[titles[i]]["gin"]

    # PNA Performance
    ax.plot(
        ratios,
        pna_data,
        label=labels[0],
        color=colors[0],
        marker=markers[0],
        linestyle="--",
    )
    ax.fill_between(
        ratios,
        pna_data - std_dev["pna"],
        pna_data + std_dev["pna"],
        color=colors[0],
        alpha=0.2,
    )

    # GIN Performance
    ax.plot(
        ratios,
        gin_data,
        label=labels[1],
        color=colors[1],
        marker=markers[1],
        linestyle="-.",
    )
    ax.fill_between(
        ratios,
        gin_data - std_dev["gin"],
        gin_data + std_dev["gin"],
        color=colors[1],
        alpha=0.2,
    )

    ax.set_xticks(xticks_values)
    ax.set_xlim(xlim_values)
    ax.set_title(titles[i])
    ax.set_xlabel(xlabel_value)
    ax.grid(True, which="both", linestyle=":", linewidth="0.5")
    ax.legend(loc="lower right" if i == 1 else "upper left")

    ax.set_yticks(yticks_values)
    ax.set_ylim(ylim_values)
    ax.set_ylabel(ylabel_value)

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig('line_71.pdf', bbox_inches='tight')
