# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Data for plotting
x = [10, 20, 30, 50, 155]
y = [1.30, 1.21, 1.27, 1.28, 1.29]
x2 = [50]
y2 = [1.19]

# Labels and Plot Types
label_Llama_2_7B = "Llama 2 7B"
label_Llama_2_13B = "Llama 2 13B"
ax1_txt = [
    "1.30\nLlaSMol Lite",
    "1.21\nLlaSMol Attn",
    "1.27\nLlaSMol FFN",
    "1.28\nLlaSMol",
    "1.29\nLlaSMol Plus",
]
ax2_txt = "1.19\nLlaSMol Large"

# Axes Limits and Labels
xlabel_value = "Trainable Parameter Size (M)"
ylabel_value = "RMSE"
xticklabels1 = [str(num) for num in x]
ylim_values = [1.15, 1.35]
yticks_values = [
    1.15,
    1.20,
    1.25,
    1.30,
]
xlim_values = [-10, 170]
xticks_values = [0, 50, 100, 150]
xticklabels2 = ["0", "50", "100", "150"]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create the figure and axis
fig, ax = plt.subplots(
    figsize=(6, 8)
)  # Adjust the size to match the original image's dimensions

# Plot the data
ax.plot(x, y, "ro-", label=label_Llama_2_7B, linewidth=2)
ax.plot(x2, y2, "b*", markersize=10, label=label_Llama_2_13B)

# Annotate the points
for i, txt in enumerate(ax1_txt):
    ax.annotate(
        txt,
        (x[i], y[i]),
        textcoords="offset points",
        xytext=(0, 5),
        ha="center",
        fontsize=10,
    )
ax.annotate(
    ax2_txt,
    (x2[0], y2[0]),
    textcoords="offset points",
    xytext=(0, 5),
    ha="center",
    color="black",
    fontsize=10,
)

# Set labels and title
ax.set_xlabel(xlabel_value, fontsize=10)
ax.set_ylabel(ylabel_value, fontsize=10)

# Set the legend
legend = ax.legend(fontsize=10)

# Adjust x-axis labels
ax.set_xticks(x)
ax.set_xticklabels(xticklabels1, ha="center")
ax.set_ylim(ylim_values)
ax.set_yticks(yticks_values)
ax.set_xlim(xlim_values)
ax.set_xticks(xticks_values)
ax.set_xticklabels(xticklabels2, ha="center")

# ===================
# Part 4: Saving Output
# ===================
# Show the plot with tight layout
plt.tight_layout()
plt.savefig("CB_23.pdf", bbox_inches="tight")
