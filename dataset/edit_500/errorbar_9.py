import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Categories and values (estimated from the image)
categories = [
    "Cloud Computing",
    "Edge Computing",
    "Quantum Computing",
    "AI and Machine Learning",
    "Blockchain Technology",
    "Cybersecurity",
    "Internet of Things (IoT)",
][::-1]
values = [-72, -68, -65, -63, -60, -58, -55][::-1]
error = [3, 2.5, 2, 1.5, 1, 0.75, 0.5]
xlabel = "Average Temperature (°F)"
ylabel = "Cities"
title = "Average Winter Temperatures of Major Cities"
xlim = [-75,-50]
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create horizontal bar chart
fig, ax = plt.subplots(figsize=(8, 8))  # Adjust figure size
bars = ax.barh(
    categories,
    values,
    color="#c5b3d6",
    edgecolor="white",
    height=0.5,
    xerr=error,
    capsize=0,
)

# Set labels and title (if any)
ax.set_xlabel(xlabel)
ax.set_ylabel(ylabel)
ax.set_title(title)

# Invert y-axis to match the image
ax.invert_yaxis()

# Set x-axis range to match the reference image
ax.set_xlim(xlim)

# Remove grid lines
ax.xaxis.grid(False)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# Set background color to white
ax.set_facecolor("white")

# ===================
# Part 4: Saving Output
# ===================
# Displaying the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig('errorbar_9.pdf', bbox_inches='tight')
