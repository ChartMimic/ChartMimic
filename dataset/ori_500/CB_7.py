# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Data
x = [0, 8, 16, 24, 32, 40, 48, 56, 64, 96, 128]
y = [0, 8, 16, 24, 32, 40, 48, 56, 64, 96, 128]
percentages = [
    "99.6%",
    "99.9%",
    "96.0%",
    "92.3%",
    "90.9%",
    "99.5%",
    "90.9%",
    "91.3%",
    "92.5%",
    "93.3%",
    "98.7%",
]

# Axes Limits and Labels
xlabel_value = "HC$_{first}$ (before aging)"
ylabel_value = "HC$_{first}$ (after aging)"
xticklabels = [f"{num}K" for num in x]
yticklabels = [f"{num}K" for num in y]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create figure and axis
fig, ax = plt.subplots(figsize=(8, 6))

# Plot data with different marker style
ax.plot(x, y, color="black", linewidth=2)
ax.scatter(x, y, marker="o", color="#3b76af", s=100)

# Annotate percentages with different font style
for i, txt in enumerate(percentages):
    ax.annotate(
        txt,
        (x[i], y[i]),
        textcoords="offset points",
        xytext=(0, 10),
        ha="center",
        fontsize=9,
    )

# Set labels with different font style
ax.set_xlabel(xlabel_value, fontsize=12)
ax.set_ylabel(ylabel_value, fontsize=12)

# Set ticks
ax.set_xticks(x)
ax.set_yticks(y)

# Set tick labels with different font style
ax.set_xticklabels(xticklabels, fontsize=9)
ax.set_yticklabels(yticklabels, fontsize=9)

# Set grid with lighter lines
ax.grid(True, linestyle="--", linewidth=0.5, color="gray")

# ===================
# Part 4: Saving Output
# ===================
# Show plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig("CB_7.pdf", bbox_inches="tight")
