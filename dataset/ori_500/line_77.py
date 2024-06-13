# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Sample data generation
models = ["Llama", "Falcon", "Qwen"]
configurations = ["Config A", "Config B", "Config C"]
iterations = np.arange(1, 11)

data = {
    "Llama": {
        "Config A": np.random.rand(10) * 10 + 80,
        "Config B": np.random.rand(10) * 10 + 75,
        "Config C": np.random.rand(10) * 10 + 85,
    },
    "Falcon": {
        "Config A": np.random.rand(10) * 10 + 60,
        "Config B": np.random.rand(10) * 10 + 65,
        "Config C": np.random.rand(10) * 10 + 55,
    },
    "Qwen": {
        "Config A": np.random.rand(10) * 10 + 70,
        "Config B": np.random.rand(10) * 10 + 75,
        "Config C": np.random.rand(10) * 10 + 65,
    },
}
# Axes Limits and Labels
xlabel_value = "Iteration"
ylabel_value = "Score"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Plotting setup
fig, axs = plt.subplots(3, 1, figsize=(8, 12), sharex=True)

# Styling choices
colors = ["#ff69b4", "#00fa9a", "#1e90ff"]  # Brighter, more vivid colors
markers = ["p", "*", "h"]  # More complex marker styles
line_styles = [":", "-.", "--"]  # More distinct line styles

# Custom background styling
fig.set_facecolor("#f0f0f0")
for ax in axs:
    ax.set_facecolor("#f7f7f7")

# Plotting
for idx, model in enumerate(models):
    ax = axs[idx]
    ax.grid(color="gray", linestyle=":", linewidth=0.5)  # Lighter grid
    for config, color, marker, line_style in zip(
        configurations, colors, markers, line_styles
    ):
        scores = data[model][config]
        ax.plot(
            iterations,
            scores,
            marker=marker,
            color=color,
            label=f"{config} - {model}",
            linestyle=line_style,
            markersize=10,
        )
        ax.set_title(f"Performance of {model}", fontsize=14)
        ax.set_xlabel(xlabel_value, fontsize=12)
        ax.set_ylabel(ylabel_value, fontsize=12)
        ax.legend(
            loc="upper left", fancybox=True, framealpha=1, shadow=True, borderpad=1
        )
        # Enhanced visibility
        for spine in ax.spines.values():
            spine.set_visible(True)
            spine.set_color("#dddddd")

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig('line_77.pdf', bbox_inches='tight')
