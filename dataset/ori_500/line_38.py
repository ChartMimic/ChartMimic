# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Data
epochs = ["3", "10", "30", "100"]  # Treat epochs as strings to make them categorical
gpt_neo = [0.8, 0.8, 0.8, 0.8]
model_3 = [0.7, 0.65, 0.6, 0.75]
model_5 = [0.65, 0.75, 0.35, 0.5]
model_7 = [0.6, 0.65, 0.5, 0.65]
model_10 = [0.45, 0.5, 0.45, 0.4]
model_30 = [0.3, 0.45, 0.75, 0.35]

# Axes Limits and Labels
xlabel_value = "# Epochs"

ylabel_value = "MA"
ylim_values = [0.0, 0.83]
yticks_values = np.arange(0.0, 0.81, 0.2)

# Labels
label_GPT_Neo="GPT-Neo"
label_3 = "3"
label_5 = "5"
label_7 = "7"
label_10 = "10"
label_30 = "30"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Plot
plt.figure(figsize=(6, 3))
plt.axhline(y=0.8, color="black", linestyle="--", linewidth=1, label=label_GPT_Neo)
plt.plot(epochs, model_3, "r-", marker="s", label=label_3)
plt.plot(epochs, model_5, "y-", marker="s", label=label_5)
plt.plot(epochs, model_7, "k-", marker="s", label=label_7)
plt.plot(epochs, model_10, "b-", marker="s", label=label_10)
plt.plot(epochs, model_30, "g-", marker="s", label=label_30)

plt.yticks(yticks_values, fontsize=14)
plt.ylim(ylim_values)

# Set x-axis labels equidistantly
ax = plt.gca()
ax.set_xticks(np.arange(len(epochs)))  # Positional indexing for equidistant spacing
ax.set_xticklabels(epochs, fontsize=14)  # Labeling x-ticks as per epochs

plt.xlabel(xlabel_value, fontsize=16)
plt.ylabel(ylabel_value, fontsize=16)

plt.legend(
    loc="lower left", ncol=3, fontsize=12, columnspacing=5
)  # Adjusted legend settings

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and show plot
plt.tight_layout()
plt.savefig('line_38.pdf', bbox_inches='tight')
