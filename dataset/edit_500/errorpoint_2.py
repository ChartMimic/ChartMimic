import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Data for plotting
categories = ["Data Privacy", "AI Ethics", "Cybersecurity", "Tech Regulation", "Innovation"]
means = [0.28, 0.25, 0.23, 0.21, 0.20]
errors = [0.03, 0.02, 0.02, 0.03, 0.02]
dataset_mean = [0.23]
xlabel = "Importance (Fraction of Reports)"
label = "Dataset Mean"
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Plotting the data
plt.figure(figsize=(8, 6))  # Adjusting figure size to match original image's dimensions
plt.errorbar(
    means,
    categories,
    xerr=errors,
    fmt="o",
    color="#bc4949",
    ecolor="#bc4949",
    capsize=0,
    label="Mean",
)
plt.axvline(dataset_mean, linestyle="--", label=label)

# Customizing the plot
plt.xlabel(xlabel)
plt.legend()

# ===================
# Part 4: Saving Output
# ===================
# Adjusting the layout and saving the figure
plt.tight_layout()
plt.savefig('errorpoint_2.pdf', bbox_inches='tight')
