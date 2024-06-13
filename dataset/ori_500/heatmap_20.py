# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import pandas as pd

# ===================
# Part 2: Data Preparation
# ===================
# Define the emotion labels
emotions = [
    "angry",
    "sad",
    "disgust",
    "contempt",
    "fear",
    "neutral",
    "surprise",
    "happy",
]

# Define the data for the original and adjusted values
original_values = [0.10, 0.00, 0.30, 0.00, 0.00, 0.50, 0.00, 0.10]
adjusted_values = [0.12, 0.00, 0.44, 0.00, 0.00, 0.44, 0.00, 0.00]
titles = ["Original", "Adjusted"]
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create a figure with two subplots (one for original and one for adjusted values)
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

# Define the color palette
cmap = plt.get_cmap("coolwarm")

# Plot heatmap for original values
im1 = ax1.imshow(pd.DataFrame([original_values], columns=emotions), cmap=cmap)
ax1.set_title(titles[0])
ax1.set_xticks(range(len(emotions)))
ax1.set_xticklabels(emotions, rotation=45, ha="center")
ax1.set_yticks(range(1))
ax1.set_yticklabels([""], rotation=0)

# Add annotations for original values
for i in range(1):
    for j in range(len(emotions)):
        ax1.text(
            j, i, f"{original_values[j]:.2f}", ha="center", va="center", color="black"
        )

# Plot heatmap for adjusted values
im2 = ax2.imshow(pd.DataFrame([adjusted_values], columns=emotions), cmap=cmap)
ax2.set_title(titles[1])
ax2.set_xticks(range(len(emotions)))
ax2.set_xticklabels(emotions, rotation=45, ha="center")
ax2.set_yticks(range(1))
ax2.set_yticklabels([""], rotation=0)

# Add annotations for adjusted values
for i in range(1):
    for j in range(len(emotions)):
        ax2.text(
            j, i, f"{adjusted_values[j]:.2f}", ha="center", va="center", color="black"
        )

# Display the figure
plt.subplots_adjust(hspace=-0.5)

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig("heatmap_20.pdf", bbox_inches="tight")
