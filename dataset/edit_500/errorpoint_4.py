import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Data (example values, replace with actual data)
categories = [
    "Climate Change",
    "Technology",
    "Health",
    "Economy",
    "Social Issues",
    "International Relations",
]
unique_speaker_mean = [20, 18, 25, 22, 24, 26]
unique_shouter_mean = [10, 9, 11, 10, 12, 11]
unique_speaker_error = [2, 1.5, 2.5, 2, 2.5, 2]
unique_shouter_error = [1, 0.75, 1.25, 1, 1.5, 1.25]
labels = ["Unique speaker count mean", "Unique shouter count mean"]
ylabel = "Number of speakers"
axlabel = "Dataset unique shouter count mean"
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Plotting
fig, ax = plt.subplots(
    figsize=(10, 6)
)  # Adjust the size to match the original image's dimensions
ax.errorbar(
    categories,
    unique_speaker_mean,
    yerr=unique_speaker_error,
    fmt="o",
    color="blue",
    label=labels[0],
)
ax.errorbar(
    categories,
    unique_shouter_mean,
    yerr=unique_shouter_error,
    fmt="o",
    color="red",
    label=labels[1],
)

# Customization
ax.set_ylabel(ylabel)
ax.set_xticklabels(categories, rotation=45, ha="right")
ax.axhline(
    y=sum(unique_shouter_mean) / len(unique_shouter_mean),
    color="grey",
    linestyle="--",
    label=axlabel,
)
ax.legend()

# ===================
# Part 4: Saving Output
# ===================
# Show plot
plt.tight_layout()
plt.savefig('errorpoint_4.pdf', bbox_inches='tight')
