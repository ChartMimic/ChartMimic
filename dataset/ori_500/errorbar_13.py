# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Data
categories = [
    "DNN x \n(k=1)",
    "DNN x \nred\n(k=2)",
    "DNN x \n(k=1)",
    "DNN x red\n (k=1)",
][::-1]
subcategories = ["[m]", "[ΔR]", "[${ΔR^{-1}}$]", "[none]"][::-1]
values = [
    [0.84, 0.83, 0.82, 0.76],
    [0.84, 0.83, 0.825, 0.76],
    [0.82, 0.81, 0.8, 0.74],
    [0.81, 0.8, 0.79, 0.73],
]
errors = [
    [0.02, 0.01, 0.01, 0.01],
    [0.02, 0.01, 0.02, 0.01],
    [0.01, 0.04, 0.03, 0.015],
    [0.01, 0.01, 0.01, 0.012],
]
percentages = [
    "+9.5%",
    "+8.3%",
    "+8.0%",
    " ",
    "+8.0%",
    "+6.6%",
    "+6.2%",
    " ",
    "+10.6%",
    "+8.9%",
    "+8.0%",
    " ",
    "+9.6%",
    "+8.6%",
    "+7.8%",
    " ",
][::-1]
xlim = [0.5, 0.9]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Plotting
fig, axes = plt.subplots(4, 1, figsize=(8, 8), sharex=True)

for i, ax in enumerate(axes):
    ax.barh(subcategories, values[i][::-1], xerr=errors[i], color="gray", capsize=5)
    ax.set_yticklabels(subcategories)
    ax.set_xlim(xlim)
    ax.set_ylabel(categories[i])
    for j, v in enumerate(values[i][::-1]):
        ax.text(
            v + errors[i][j] + 0.01,
            j,
            percentages[i * 4 + j],
            color="black",
            va="center",
        )

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and save
plt.tight_layout()
plt.savefig("errorbar_13.pdf", bbox_inches="tight")
