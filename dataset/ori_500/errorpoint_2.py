# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Data for plotting
categories = ["Pulwama-Balakot", "CAA", "Kashmir", "Religion", "Politics"]
means = [0.24, 0.22, 0.20, 0.19, 0.18]
errors = [0.04, 0.03, 0.02, 0.02, 0.02]
dataset_mean = [0.162]
xlabel = "Incivility (Fraction of Videos)"
label = "Dataset mean"

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
plt.savefig("errorpoint_2.pdf", bbox_inches="tight")
