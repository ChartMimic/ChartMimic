# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Data
methods = ["CodeBERT", "ChatGPT-3.5", "ChatGPT-4.0", "CodeAgent"]
recall_scores = [0.6364, 0.8008, 0.8427, 0.9011]
f1_scores = [0.75, 0.8720, 0.9012, 0.9389]

# Axes Limits and Labels
ax1_title = "Average Recall Scores by Method"
ax1_ylim = [0.60, 1.00]
ax1_ylabel = "Scores"
ax2_title = "Average F1 Scores by Method"
ax2_ylim = [0.60, 1.00]
ax2_ylabel = "Scores"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create figure and axes
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

# Bar chart for Average Recall Scores
ax1.bar(methods, recall_scores, color="skyblue")
ax1.plot(methods, recall_scores, marker="o", color="blue")
for i, score in enumerate(recall_scores):
    ax1.text(i, score, f"{score*100:.2f}%", ha="center", va="bottom")
ax1.set_title(ax1_title)
ax1.set_ylim(0.60, 1.00)
ax1.set_ylabel(ax1_ylabel)
# set ax1 background color
ax1.set_facecolor("#f5f5f5")

# Bar chart for Average F1 Scores
ax2.bar(methods, f1_scores, color="skyblue")
ax2.plot(methods, f1_scores, marker="o", color="red")
for i, score in enumerate(f1_scores):
    ax2.text(i, score, f"{score*100:.2f}%", ha="center", va="bottom")
ax2.set_title(ax2_title)
ax2.set_ylim(ax2_ylim)
ax2.set_ylabel(ax2_ylabel)
ax2.set_facecolor("#f5f5f5")

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and save plot
plt.tight_layout()
plt.savefig("CB_17.pdf", bbox_inches="tight")
