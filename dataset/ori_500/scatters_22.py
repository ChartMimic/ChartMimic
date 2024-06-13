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
categorys1 = ["Model-Basedness", "Meta-Cognition"]
colors1 = ["blue", "orange"]
categorys2 = ["Exploration", "Risk Taking"]
colors2 = ["green", "red"]  
titles = ["Performance Comparison", "Strategic Traits"]
xlabel = "Value"
ylabel = "Models"
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6), sharey=True)

# Plotting for ax1 - first two categories
for category, color in zip(categorys1, colors1):
    ax1.scatter(values[category], models, color=color, label=category)
ax1.set_title(titles[0])
ax1.set_xlabel(xlabel)
ax1.set_ylabel(ylabel)
ax1.legend()

# Plotting for ax2 - next two categories
for category, color in zip(categorys2, colors2):
    ax2.scatter(values[category], models, color=color, label=category)
ax2.set_title(titles[1])
ax2.set_xlabel(xlabel)
ax2.legend()

# Common settings
for ax in [ax1, ax2]:
    ax.set_yticks(range(len(models)))
    ax.set_yticklabels(models)
    ax.grid(True, linestyle="--", alpha=0.6)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and show plot
plt.tight_layout()
plt.savefig('scatters_22.pdf', bbox_inches='tight')
