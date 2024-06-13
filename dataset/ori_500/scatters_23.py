# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Data for plotting
models = [
    "GPT4",
    "Mixtal-8x7B",
    "MPT-7B",
    "Llama2-70B",
    "Falcom-40B",
    "Davinci-003",
    "Davinci-002",
    "Claude-2",
    "Claude-1",
]
values = {
    "Model-Basedness": [1.8, 1.5, 1.8, 1.2, 1.6, 1.4, 1.9, 1.1, 1.3],
    "Meta-Cognition": [0.8, 0.6, 0.7, 0.5, 0.9, 0.4, 1.0, 0.3, 0.2],
    "Exploration": [0.3, 0.5, 0.4, 0.6, 0.2, 0.7, 0.1, 0.8, 0.9],
    "Risk Taking": [0.9, 0.7, 0.8, 0.6, 1.0, 0.5, 0.4, 0.2, 0.3],
    "Bayesian Reasoning": [0.2, 0.4, 0.3, 0.5, 0.1, 0.6, 0.7, 0.9, 0.8],
    "Simple Bandits": [0.5, 0.3, 0.4, 0.2, 0.6, 0.1, 0.7, 0.8, 0.9],
}
colors = ["blue", "orange", "green", "red", "purple", "brown"]
xlabel = "Models"
ylabel = "Score"
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create subplots 2x2
fig, axs = plt.subplots(2, 2, figsize=(8, 8), sharey=True)
axes = axs.flatten()

# Plot each category
for ax, (category, color) in zip(axes, zip(values.keys(), colors)):
    ax.scatter(
        models,
        values[category],
        color=color,
        label=category,
        s=100,
        edgecolor="black",
        alpha=0.6,
        marker="o",
    )
    ax.set_title(category)
    ax.set_xticks(models)
    ax.set_xticklabels(models, rotation=45, ha="right")
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.legend()

# Enhance style
for ax in axes:
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.grid(True, linestyle="--", alpha=0.5)
    ax.set_ylim(0, 2)  # Ensure all plots have the same y-axis limits

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and save plot
plt.tight_layout()
plt.savefig('scatters_23.pdf', bbox_inches='tight')
