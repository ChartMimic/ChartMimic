# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Data for plotting
x = [40, 50, 60, 70, 80, 90, 100]
y = [7.5, 6.5, 6.0, 5.75, 5.6, 5.5, 5.5]
bits = [
    "2.91 bit",
    "3.11 bit",
    "3.32 bit",
    "3.53 bit",
    "3.63 bit",
    "3.74 bit",
    "3.94 bit",
]  # Removed the extra '4.15 bit'

# Axes Limits and Labels
xlabel_value = "Ratio of 4-bit Utilization (%)"
xlim_values = [35, 105]
xticks_values = np.arange(40, 101, 10)

ylabel_value = "Perplexity (PPL)"
ylim_values = [5.0, 8.0]
yticks_values = np.arange(5.0, 7.6, 0.5)

# Labels
label_1 = "APTQ"
label_2 = "LLaMa-7B (FP16): 5.22"
label_3 = "OWQ-4bit: 5.56"
label_4 = "GPTQ-4bit: 5.62"
label_5 = "LLM-QAT-4bit: 7.4"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create the plot
fig, ax = plt.subplots(figsize=(5, 4))

# Plot the line
ax.plot(x, y, marker="o", color="blue", label=label_1)

# Set x,y-axis to only display specific ticks and extend y-axis to leave space at top
plt.yticks(yticks_values, fontsize=10)
plt.xticks(xticks_values, fontsize=10)
plt.xlim(xlim_values)  # Adjusted y-axis limit

# Annotate the points with bit values
for i, txt in enumerate(bits):
    ax.annotate(
        txt, (x[i], y[i]), textcoords="offset points", xytext=(0, 10), ha="center"
    )

# Horizontal lines for comparison
ax.axhline(y=5.22, color="magenta", linestyle="--", label=label_2)
ax.axhline(y=5.56, color="orange", linestyle="--", label=label_3)
ax.axhline(y=5.62, color="green", linestyle="--", label=label_4)
ax.axhline(y=7.4, color="red", linestyle="--", label=label_5)

# Set labels and title
ax.set_xlabel(xlabel_value, fontsize=12)
ax.set_ylim(ylim_values)  # Adjusted y-axis limit
ax.set_xlim(xlim_values)  # Adjusted x-axis limit
ax.set_ylabel(ylabel_value, fontsize=12)

# Set the legend
ax.legend(loc="center right", fontsize=10)

# Set grid
ax.grid(True)

# ===================
# Part 4: Saving Output
# ===================
# Adjusting layout to add more space on the right
plt.tight_layout()
plt.savefig('line_22.pdf', bbox_inches='tight')
