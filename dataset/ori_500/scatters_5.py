# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Data points for each group
siren = [(0.05, 950), (0.10, 800)]
wire = [(0.07, 850), (0.12, 700)]
ffn = [(0.06, 450), (0.11, 400)]
sz3 = [(0.08, 600), (0.13, 550)]
nncomp = [(0.09, 250), (0.14, 200)]
ours = [(0.15, 300), (0.20, 100)]
labels = ["SIREN", "WIRE", "FFN", "SZ3", "NNComp", "Ours"]
xlabel = "Bit per pixel (BPP)"
ylabel = "WRMSE"
title = "Scatter Plot of WRMSE vs BPP"
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create a scatter plot
fig, ax = plt.subplots(figsize=(6, 6))

# Plot each group with different color and marker
ax.scatter(*zip(*siren), color="blue", label=labels[0])
ax.scatter(*zip(*wire), color="cyan", label=labels[1])
ax.scatter(*zip(*ffn), color="red", label=labels[2])
ax.scatter(*zip(*sz3), color="green", label=labels[3])
ax.scatter(*zip(*nncomp), color="magenta", label=labels[4], marker="x")
ax.scatter(*zip(*ours), color="orange", label=labels[5])

# Add legend
ax.legend(loc="upper right")

# Add labels and title
ax.set_xlabel(xlabel)
ax.set_ylabel(ylabel)
ax.set_title(title)

# ===================
# Part 4: Saving Output
# ===================
# Displaying the plot with tight layout to minimize white space
fig.tight_layout()
plt.savefig('scatters_5.pdf', bbox_inches='tight')
