# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Data
categories = ["Female Player", "Male Player", "LLM Player", "Person Player"]
models = [
    "gpt-3.5-turbo-0613",
    "gpt-3.5-turbo-instruct",
    "gpt-4",
    "llama-2-13b",
    "llama-2-70b",
]
values = np.random.rand(4, 5) * 5 + 3  # Random values for demonstration
colors = ["mistyrose", "cornflowerblue", "lightgreen", "lightcoral", "lightblue"]
referlines = [3.4, 4.2, 6, 7, 7.5]
ylabel = "Average Amount Sent ($)"
ylim = [3, 8]
arrowstart = (0.05, 0.07)
arrowend = (0.48, 0.07)
arrowstart2 = (0.55, 0.07)
arrowend2 = (0.9, 0.07)
xlim = [-0.5, 3.5]
textposition = [[0.5, 2], [2.5, 2]]
textlabel = "Trustee Scenario"
spanposition = [[-0.5, 1.5], [1.5, 3.5]]


# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Plotting
fig, ax = plt.subplots(figsize=(10, 5))
width = 0.1
x = np.arange(len(categories))
ax.axvspan(
    spanposition[0][0],
    spanposition[0][1],
    color="#f5fff1",
)
ax.axvspan(
    spanposition[1][0],
    spanposition[1][1],
    color="#f5f5fd",
)

for i, subcategory in enumerate(categories):
    for j, (model, color, referline) in enumerate(zip(models, colors, referlines)):
        ax.bar(
            i + (j - 2) * width,
            values[i, j] - referline,
            width,
            bottom=referline,
            label=model if i == 0 else "",
            color=color,
        )

# Annotations
for k, model in enumerate(models):
    for i, category in enumerate(categories):
        ax.text(
            i + (k - 2) * width, values[i, k] + 0.1, f"{values[i, k]:.1f}", ha="center"
        )

for line, color in zip(referlines, colors):
    ax.axhline(line, color=color, linestyle="--")
    ax.text(3.4, line + 0.1, f"{line:.1f}", ha="center", color=color)

# Customizations
ax.set_ylabel(ylabel)
ax.set_xticks(x)
ax.set_xticklabels(categories)
ax.set_ylim(ylim)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
plt.annotate(
    "",
    xy=arrowstart,
    xytext=arrowend,
    xycoords="figure fraction",
    arrowprops=dict(arrowstyle="<->", color="green", lw=1),
)
plt.annotate(
    "",
    xy=arrowstart2,
    xytext=arrowend2,
    xycoords="figure fraction",
    arrowprops=dict(arrowstyle="<->", color="purple", lw=1),
)
current_ticks = ax.get_xticks()
new_ticks = current_ticks + 0.5
ax.set_xlim(xlim)
# Set the new ticks without labels
ax.set_xticks(new_ticks, minor=True)  # Add as minor ticks
ax.xaxis.set_minor_formatter(plt.NullFormatter())  # Hide labels for minor ticks

# Enable grid for minor ticks, adjust grid appearance as needed
ax.grid(which="minor", color="black", linestyle="--", alpha=0.5)
ax.text(
    textposition[0][0],
    textposition[0][1],
    textlabel,
    ha="center",
    va="top",
    fontsize=12,
    color="green",
)
ax.text(
    textposition[1][0],
    textposition[1][1],
    textlabel,
    ha="center",
    va="top",
    fontsize=12,
    color="purple",
)
ax.legend(ncol=5, loc="upper center", bbox_to_anchor=(0.5, 1.2))

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig("HR_20.pdf", bbox_inches="tight")
