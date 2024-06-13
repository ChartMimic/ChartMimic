# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Set a seed for reproducibility

# Define fiscal quarters
quarters = np.array([1, 2, 3, 4, 5])

# Generate synthetic stock market index changes for two different indexes
index_changes_dow_jones = np.random.uniform(
    -5, 5, 5
)  # Example changes in Dow Jones index
index_changes_nasdaq = np.random.uniform(-5, 5, 5)  # Example changes in Nasdaq index

labels = ["Dow Jones Index", "Nasdaq Index"]
axline = 0
xlabel = "Fiscal Quarter"
ylabel = "Index Change (%)"
ylim = [-5, 5]
yticks = np.arange(-5, 5, 5)

# ===================
# Part 3: Plot Configuration and Renderingåå
# ===================
# Create figure and subplots
fig, axs = plt.subplots(figsize=(10, 5))
width = 0.4

# Plotting bars for each index
bars1 = axs.bar(
    quarters - width / 2,
    index_changes_dow_jones,
    width=width,
    color="#78a083",
    label="Dow Jones Index",
)
bars2 = axs.bar(
    quarters + width / 2,
    index_changes_nasdaq,
    width=width,
    color="#d27a41",
    label="Nasdaq Index",
)

# Adding text labels on the bars
for bars in [bars1, bars2]:
    for bar in bars:
        height = bar.get_height()
        axs.text(
            bar.get_x() + bar.get_width() / 2,
            height,
            f"{height:.1f}",
            ha="center",
            va="bottom" if height > 0 else "top",
        )

# Additional plot settings
axs.axhline(axline, color="black")
axs.set_xlabel(xlabel)
axs.set_ylabel(ylabel)
axs.set_ylim(ylim)
axs.set_yticks(yticks)
axs.set_xticks(quarters)
axs.yaxis.grid(True)
axs.set_axisbelow(True)

# Adding legend and adjusting layout
plt.legend(loc="upper center", bbox_to_anchor=(0.5, 1.10), ncol=2)

# ===================
# Part 4: Saving Output
# ===================
# Save the figure as a PDF
plt.tight_layout()
plt.savefig("bar_73.pdf", bbox_inches="tight")
