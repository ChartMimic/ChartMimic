# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Data for plotting
models = [
    "gpt-4",
    "text-davinci-003",
    "text-davinci-002",
    "claude-1",
    "claude-2",
    "text-bison@002",
    "hf_falcon-40b",
    "llama-2-70",
    "llama-2-70-chat",
]
values = {
    "Model-Basedness": [2, 1.5, 1.8, 1.2, 1.6, 1.4, 1.9, 1.1, 1.3],
    "Meta-Cognition": [0.8, 0.6, 0.7, 0.5, 0.9, 0.4, 1.0, 0.3, 0.2],
    "Exploration": [0.3, 0.5, 0.4, 0.6, 0.2, 0.7, 0.1, 0.8, 0.9],
    "Risk Taking": [0.9, 0.7, 0.8, 0.6, 1.0, 0.5, 0.4, 0.2, 0.3],
    "Bayesian Reasoning": [0.2, 0.4, 0.3, 0.5, 0.1, 0.6, 0.7, 0.9, 0.8],
    "Simple Bandits": [0.5, 0.3, 0.4, 0.2, 0.6, 0.1, 0.7, 0.8, 0.9],
}
colors = ["blue", "orange", "green", "red", "purple", "brown"]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create subplots
fig, axes = plt.subplots(1, 6, figsize=(12, 4), sharey=True)

# Plot each category
for ax, (category, color) in zip(axes, zip(values.keys(), colors)):
    ax.scatter(values[category], models, color=color)
    ax.set_title(category)
    ax.set_xlim(0, 2)
    ax.axvline(x=1, color="black", linestyle="--", linewidth=1)

# Set common labels
fig.text(0.5, 0.04, "Value", ha="center", va="center")

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and show plot
plt.tight_layout(rect=[0.03, 0.05, 1, 0.95])
plt.savefig('scatters_1.pdf', bbox_inches='tight')
