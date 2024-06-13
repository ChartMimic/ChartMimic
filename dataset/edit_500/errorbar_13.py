import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Data
categories = [
    "Transformer \n(k=1)",
    "Transformer \nblue\n(k=2)",
    "Transformer \n(k=1)",
    "Transformer blue\n (k=1)",
][::-1]
subcategories = ["[s]", "[ΔT]", "[${ΔT^{-1}}$]", "[none]"][::-1]
values = [
    [0.75, 0.74, 0.73, 0.69],
    [0.75, 0.74, 0.735, 0.69],
    [0.73, 0.72, 0.71, 0.67],
    [0.72, 0.71, 0.7, 0.66],
]
errors = [
    [0.03, 0.02, 0.02, 0.015],
    [0.03, 0.02, 0.03, 0.015],
    [0.02, 0.05, 0.04, 0.02],
    [0.02, 0.02, 0.02, 0.018],
]
percentages = [
    "+9.0%",
    "+7.8%",
    "+7.5%",
    " ",
    "+7.5%",
    "+5.5%",
    "+5.0%",
    " ",
    "+10.0%",
    "+8.0%",
    "+7.5%",
    " ",
    "+9.0%",
    "+7.5%",
    "+7.0%",
    " ",
][::-1]
xlim = [0.60, 0.8]

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
plt.savefig('errorbar_13.pdf', bbox_inches='tight')
