# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Data points
gpu_hours = [500, 1000, 1500, 2000, 2500, 3500]
accuracy = [77, 81, 79, 82, 83, 84.7]
labels = [None, "iBOT", None, "MoCo v3", "D2V2", "D2V2-Refined"]
dashed_lines = [(500, 77, 1000, 81), (2500, 83, 3500, 84.7)]

title = "ImageNet-1K Linear Probing"
xlabel = "Pre-training GPU Hours"
ylabel = "Accuracy [%]"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Plotting the data points
plt.figure(figsize=(8, 5))
plt.scatter(gpu_hours, accuracy, color="black", s=100)  # Adjusted marker size

# Annotating the data points
for i, label in enumerate(labels):
    plt.annotate(
        label,
        (gpu_hours[i], accuracy[i]),
        textcoords="offset points",
        xytext=(0, 10),
        ha="center",
    )

# Plotting the dashed lines with correct colors and annotations
plt.plot([500, 1000], [77, 81], linestyle="--", color="green")
plt.annotate("+5.3%", (750, 79), color="green")
plt.plot([500, 1500], [77, 79], linestyle="--", color="black")
plt.annotate("MAE", (1000, 77.5), color="black")
plt.plot([2500, 3500], [83, 84.7], linestyle="--", color="orange")
plt.annotate(
    "D2V2-Refined",
    (2900, 84),
    color="orange",
    textcoords="offset points",
    xytext=(0, 10),
    ha="center",
)

# Annotating the dashed lines correctly
plt.annotate("+5.3%", (750, 79), color="green")

# Setting the title and labels
plt.title(title)
plt.xlabel(xlabel)
plt.ylabel(ylabel)

# Adjusting y-axis scale
plt.ylim(76, 86)
plt.yticks([77, 79, 81, 83, 85])
plt.xlim(-100, 4100)
plt.xticks([0, 1000, 2000, 3000, 4000])
plt.grid(True)

# removing the top, left, and right spines
plt.gca().spines["top"].set_visible(False)
plt.gca().spines["left"].set_visible(False)
plt.gca().spines["right"].set_visible(False)

# ===================
# Part 4: Saving Output
# ===================
# Show the plot with tight layout
plt.tight_layout()
plt.savefig('scatters_10.pdf', bbox_inches='tight')
