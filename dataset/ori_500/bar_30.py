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
models = ["Mixtral-8x7b-Instruct", "GPT-3.5", "GPT-4"]
zero_shot = [6.11, 44.44, 42.78]
one_shot = [28.33, 56.11, 60.56]
ds_agent = [31.11, 85.00, 99.44]

# X-axis positions
x = np.arange(len(models))

# Bar width
bar_width = 0.2
gap_width = 0.02

labels = ["Zero-shot", "One-shot", "DS-Agent"]
ylabel = "One pass rate (%)"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Plotting bars
fig, ax = plt.subplots(figsize=(6, 4))  # Adjusting figure size to match 468x360 pixels
rects1 = ax.bar(
    x - bar_width - gap_width, zero_shot, bar_width, label=labels[0], color="#f2a49e"
)
rects2 = ax.bar(x, one_shot, bar_width, label=labels[1], color="#a9c8f0")
rects3 = ax.bar(
    x + bar_width + gap_width, ds_agent, bar_width, label=labels[2], color="#cdbcfa"
)

# Adding text for labels, title, and custom x-axis tick labels
ax.set_ylabel(ylabel)
ax.set_xticks(x)
ax.set_xticklabels(models)
ax.legend(loc="lower center", bbox_to_anchor=(0.5, -0.2), ncol=3)


# Adding data labels inside the bars
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate(
            "{}".format(height),
            xy=(rect.get_x() + rect.get_width() / 2, height + 2),
            xytext=(0, 0),  # No offset
            textcoords="offset points",
            ha="center",
            va="center",
            color="black",
            fontsize=8,
        )


autolabel(rects1)
autolabel(rects2)
autolabel(rects3)

# Adjusting the layout and font sizes
ax.tick_params(axis="x", labelsize=8)
ax.tick_params(axis="y", labelsize=8)
ax.yaxis.label.set_size(8)

# Adding grid
ax.grid(axis="y", linestyle="--", alpha=0.6)
ax.grid(axis="x", linestyle="--", alpha=0.6)
ax.set_axisbelow(True)

plt.subplots_adjust(bottom=0.2, top=0.95)

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig("bar_30.pdf", bbox_inches="tight")
