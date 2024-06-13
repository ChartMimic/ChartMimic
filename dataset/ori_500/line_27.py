# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Data for plotting
compression_rate = [1, 12, 18, 30]
cnn_error_rate = [26.0, 30.2, 34.4, 55.0]
cif_error_rate = [17.9, 24.7, 28.6, 36.8]
star_error_rate = [15.8, 18.0, 19.8, 22.6]

# Axes Limits and Labels
xlabel_value = "Compression Rate"
xlim_values = [-2, 32]
xticks_values = [1, 12, 18, 30]
xticklabels = ["$1$", "$12$", "$18$", "$30$"]

ylabel_value = "Word Error Rate (%)"

# Labels
label_CNN = "CNN"
label_CIF="CIF"
label_STAR="STAR"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Plotting the data
plt.figure(figsize=(6, 6))  # Adjusting figure size to match original image dimensions
plt.plot(
    compression_rate, cnn_error_rate, "o-", label=label_CNN, color="#e8d2cc", markersize=4
)
plt.plot(
    compression_rate, cif_error_rate, "x-", label=label_CIF, color="#9f6a8d", markersize=4
)
plt.plot(
    compression_rate, star_error_rate, "s-", label=label_STAR, color="#5c5048", markersize=4
)

# Set y-axis to only display specific ticks and extend y-axis to leave space at top
plt.xticks(xticks_values, xticklabels)
plt.xlim(xlim_values)  # Extend y-axis to leave some space above 10^-1

# Adding data labels
for i, txt in enumerate(cnn_error_rate):
    plt.annotate(
        txt,
        (compression_rate[i], cnn_error_rate[i]),
        textcoords="offset points",
        xytext=(0, 5),
        ha="center",
        fontsize=12,
    )
for i, txt in enumerate(cif_error_rate):
    plt.annotate(
        txt,
        (compression_rate[i], cif_error_rate[i]),
        textcoords="offset points",
        xytext=(0, 5),
        ha="center",
        fontsize=12,
    )
for i, txt in enumerate(star_error_rate):
    plt.annotate(
        txt,
        (compression_rate[i], star_error_rate[i]),
        textcoords="offset points",
        xytext=(0, 5),
        ha="center",
        fontsize=12,
    )

# Setting the axis labels
plt.xlabel(xlabel_value, fontsize=16)
plt.ylabel(ylabel_value, fontsize=16)

# Change the axis colors
ax = plt.gca()
ax.spines["bottom"].set_color("#cccccc")
ax.spines["bottom"].set_linewidth(1.4)
ax.spines["left"].set_color("#cccccc")
ax.spines["left"].set_linewidth(1.4)
ax.spines["top"].set_color("#ffffff")
ax.spines["right"].set_color("#ffffff")

# Adjust tick parameters to ensure ticks do not extend outside
ax.tick_params(axis="both", which="both", length=0)  # Hide tick marks

# Adding the legend
plt.legend(loc="upper left")

# Adding grid
plt.grid(True, which="both", linestyle="--", linewidth=1, color="#808080")

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and save plot
plt.tight_layout()
plt.savefig('line_27.pdf', bbox_inches='tight')
