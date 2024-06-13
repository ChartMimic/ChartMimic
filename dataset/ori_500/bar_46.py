# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Data
models = ["Lavila", "Video-LLaMA", "BLIP1", "BLIP2", "LLaVA", "OSCaR", "GPT4V"]
percentages = [0.0, 0.71, 4.64, 4.64, 31.79, 73.93, 82.5]
title = "Human Study"
xlabel = "Model"
ylabel = "Percentage (%)"
ylim = [0, 90]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create figure and bar chart
plt.figure(figsize=(10, 6))
bars = plt.bar(models, percentages, color="skyblue")

# Add percentage labels on top of each bar
for bar in bars:
    yval = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2, yval, f"{yval}%", ha="center", va="bottom"
    )

# Set chart title and labels
plt.title(title)
plt.xlabel(xlabel)
plt.ylabel(ylabel)

# Set y-axis range and gridlines
plt.ylim(0, 90)
plt.grid(axis="both", linestyle="--", alpha=0.7)

plt.gca().spines["top"].set_visible(False)
plt.gca().spines["right"].set_visible(False)

# ===================
# Part 4: Saving Output
# ===================
# Displaying the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig("bar_46.pdf", bbox_inches="tight")
