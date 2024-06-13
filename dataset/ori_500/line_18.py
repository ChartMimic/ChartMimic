# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Sample data
iterations = np.array([0, 250, 500, 750, 1000, 1250, 1500, 1750, 2000])
gpt4_7b = np.array([0.1, 0.4, 0.7, 0.85, 0.9, 0.92, 0.93, 0.94, 0.95])
gpt4_7b_ft = np.array([0.05, 0.2, 0.35, 0.5, 0.6, 0.65, 0.7, 0.72, 0.73])
llama_7b = np.array([0.1, 0.45, 0.75, 0.88, 0.9, 0.91, 0.92, 0.93, 0.94])
llama_7b_ft = np.array([0.05, 0.25, 0.4, 0.55, 0.65, 0.7, 0.75, 0.77, 0.78])

# Axes Limits and Labels
xlabel_value = "Iterations"
ylabel_value = "Attack Success Rate"

# Labels
label_1 = "7B"
label_2 = "7B (Fine-tuned)"

# Titles
title_1 = "GPT-4 Evaluation"
title_2 = "Llama Guard Evaluation"


# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Set the figure size to match the original image's dimensions
plt.figure(figsize=(9, 4))

# First subplot
plt.subplot(1, 2, 1)
plt.plot(
    iterations,
    gpt4_7b,
    marker="o",
    color="#0a6ae1",
    label=label_1,
    markerfacecolor="#0a6ae1",
    linewidth=2,
    markersize=5,
)
plt.plot(
    iterations,
    gpt4_7b_ft,
    marker="o",
    color="#d75faa",
    label=label_2,
    markerfacecolor="#d75faa",
    linewidth=2,
    markersize=5,
)
plt.fill_between(iterations, gpt4_7b - 0.05, gpt4_7b + 0.05, color="#0a6ae1", alpha=0.2)
plt.fill_between(
    iterations, gpt4_7b_ft - 0.03, gpt4_7b_ft + 0.03, color="#d75faa", alpha=0.2
)
plt.title(title_1, fontsize=14)
plt.xlabel(xlabel_value, fontsize=12)
plt.ylabel(ylabel_value, fontsize=12)

# Second subplot
plt.subplot(1, 2, 2)
plt.plot(
    iterations,
    llama_7b,
    marker="o",
    color="#0a6ae1",
    label=label_1,
    markerfacecolor="#0a6ae1",
    linewidth=2,
    markersize=5,
)
plt.plot(
    iterations,
    llama_7b_ft,
    marker="o",
    color="#d75faa",
    label=label_2,
    markerfacecolor="#d75faa",
    linewidth=2,
    markersize=5,
)
plt.fill_between(
    iterations, llama_7b - 0.05, llama_7b + 0.05, color="#0a6ae1", alpha=0.2
)
plt.fill_between(
    iterations, llama_7b_ft - 0.03, llama_7b_ft + 0.03, color="#d75faa", alpha=0.2
)
plt.title(title_2, fontsize=14)
plt.xlabel(xlabel_value, fontsize=12)
plt.ylabel(ylabel_value, fontsize=12)
plt.legend(loc="lower right", frameon=True, bbox_to_anchor=(1, 0.1))

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and save plot
plt.tight_layout()
plt.savefig('line_18.pdf', bbox_inches='tight')
