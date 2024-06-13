# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Approximated data points based on the image
decomposition_IO_norm = [0, 20, 40, 60, 80]
coco_10k = [0.60, 0.70, 0.72, 0.73, 0.74]
laion_10k = [0.58, 0.67, 0.70, 0.71, 0.73]
coco_5k = [0.56, 0.66, 0.67, 0.68, None]
laion_5k = [0.55, 0.61, 0.64, 0.65, None]
clip_y = [0.75, 0.75]
clip_x = [-10, 90]

# Axes Limits and Labels
xlabel_value = "Decomposition IO Norm"
xlim_values = [-10, 90]

ylabel_value = "Accuracy"
ylim_values = [0.53, 0.76]
yticks_values = [0.55, 0.60, 0.65, 0.70, 0.75]

# Labels
label_1="coco (10k)"
label_2="laion (10k)"
label_3 = "coco (5k)"
label_4="laion (5k)"
label_5="CLIP"

# Titles
title_1 = "Effect of Vocab on Zero Shot Accuracy"
title_2 = "Dictionary"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create the plot
plt.figure(figsize=(6, 6))  # Adjust figure size to match original image dimensions
plt.plot(decomposition_IO_norm, coco_10k, label=label_1, color="red", marker="o")
plt.plot(
    decomposition_IO_norm, laion_10k, label=label_2, color="green", marker="o"
)
plt.plot(decomposition_IO_norm, coco_5k, label=label_3, color="blue", marker="o")
plt.plot(
    decomposition_IO_norm, laion_5k, label=label_4, color="orange", marker="o"
)
plt.plot(clip_x, clip_y, label=label_5, color="black", linestyle="--")

# Add title and labels
plt.title(title_1)
plt.xlabel(xlabel_value)
plt.ylabel(ylabel_value)
plt.xticks(decomposition_IO_norm)
plt.xlim(xlim_values)
plt.yticks(yticks_values)
plt.ylim(ylim_values)
# Add legend with additional entry
plt.legend(title=title_2,loc="lower right")

# Adding the white grid manually
plt.grid(color="white", linestyle="-", linewidth=0.5)

# ===================
# Part 4: Saving Output
# ===================
# Show the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig('line_11.pdf', bbox_inches='tight')
