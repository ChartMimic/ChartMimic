# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# New field: Sports Activities
activities = [
    "Running",
    "Swimming",
    "Cycling",
    "Weightlifting",
    "Yoga",
    "Basketball",
    "Tennis",
    "Soccer",
    "Hiking",
    "Dancing",
]

# Approximate participation rates in percentage
participation_rates = [15.0, 12.5, 10.5, 9.0, 8.0, 7.5, 6.5, 6.0, 5.5, 4.5]
xlabel = "Participation Rate (%)"
ylabel = "Activity"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create horizontal bar chart
plt.figure(figsize=(8, 8))  # Adjust figure size
plt.barh(activities, participation_rates, color="lightcoral", edgecolor="gray")

# Adding data labels
for index, value in enumerate(participation_rates):
    plt.text(value, index, f" {value}%", va="center")
# Set labels and title
plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.gca().spines["top"].set_visible(False)
plt.gca().spines["right"].set_visible(False)
plt.gca().spines["bottom"].set_visible(False)
plt.gca().spines["left"].set_visible(False)

# ===================
# Part 4: Saving Output
# ===================
# Show the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig('bar_55.pdf', bbox_inches='tight')
