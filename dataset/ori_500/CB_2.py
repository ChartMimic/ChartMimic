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
models = ["GPT-2", "Llama 2 7B", "Llama 2 70B", "Mixtral 8x7B", "GPT-3.5", "GPT-4"]
simple = [0, 6, 8, 12, 12, 56]
complex = [0, 16, 4, 18, 10, 4]
code = [0, 12, 20, 26, 20, 22]
simple_trend = [0, 6, 8, 12, 12, 56]
labels = ["Simple", "Complex", "Code", "Simple Trend"]
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Plotting
fig, ax = plt.subplots(
    figsize=(8, 5)
)  # Adjusting figure size to match the original image's dimensions

bar_width = 0.25
index = np.arange(len(models))

bar1 = ax.bar(
    index, simple, bar_width, label=labels[0], color="#db7a6e", edgecolor="grey"
)
bar2 = ax.bar(
    index + bar_width,
    complex,
    bar_width,
    label=labels[1],
    color="#e5a893",
    edgecolor="grey",
)
bar3 = ax.bar(
    index + 2 * bar_width,
    code,
    bar_width,
    label=labels[2],
    color="#f9ebe7",
    edgecolor="grey",
)

# Trend line for 'Simple Trend'
ax.plot(
    index,
    simple_trend,
    color="#cb56ae",
    marker="o",
    linestyle="dashed",
    label=labels[3],
)

# Adding percentages on top of the bars
for i, rect in enumerate(bar1 + bar2 + bar3):
    height = rect.get_height()
    ax.text(
        rect.get_x() + rect.get_width() / 2.0,
        height,
        f"{height}%",
        ha="center",
        va="bottom",
    )

# Labels, title and custom x-axis tick labels
ax.set_xlabel("Model")
ax.set_ylabel("Success Rate (%)")
ax.set_yticks(np.arange(0, 61, 10))
ax.set_title("Encoding/Decoding Schelling Points by Model")
ax.set_xticks(index + bar_width)
ax.set_xticklabels(models, rotation=30)
ax.legend()

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig("CB_2.pdf", bbox_inches="tight")
