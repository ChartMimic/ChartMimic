# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Define subplot titles
titles = [
    "MOLHIV",
    "Graph-SST2",
    "MNIST-75SP",
    "SPMotif-0.5",
    "SPMotif-0.7",
    "SPMotif-0.9",
]

# Loop through each subplot
for i in range(4):
    # Sample data (replace with actual data)
    ratios = np.linspace(0.1, 1.0, 5)
    performance_pna_ours = np.random.uniform(0.76, 0.82, len(ratios))
    performance_gin_ours = np.random.uniform(0.74, 0.78, len(ratios))
    performance_pna_gsat = np.mean(performance_pna_ours) * np.ones(len(ratios))
    performance_gin_gsat = np.mean(performance_gin_ours) * np.ones(len(ratios))

    # Error for sample data (replace with actual error values)
    error = np.random.uniform(0.01, 0.02, len(ratios))

# Axes Limits and Labels
xlabel_value = "Ratio r"
ylabel_value = "Performance"

# Labels
label_1 = "PNA + ours"
label_2 = "GIN + ours"
label_3 = "PNA + GSAT"
label_4 = "GIN + GSAT"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Set figure size to match the original image's dimensions
plt.figure(figsize=(16, 8))

# Loop through each subplot
for i in range(4):
    plt.subplot(2, 2, i + 1)
    plt.plot(ratios, performance_pna_ours, "-s", label=label_1, color="purple")
    plt.fill_between(
        ratios,
        performance_pna_ours - error,
        performance_pna_ours + error,
        color="purple",
        alpha=0.2,
    )
    plt.plot(ratios, performance_gin_ours, "-s", label=label_2, color="orange")
    plt.fill_between(
        ratios,
        performance_gin_ours - error,
        performance_gin_ours + error,
        color="orange",
        alpha=0.2,
    )
    plt.plot(ratios, performance_pna_gsat, "--", label=label_3, color="purple")
    plt.plot(ratios, performance_gin_gsat, "--", label=label_4, color="orange")
    plt.title(titles[i])
    plt.xlabel(xlabel_value)
    plt.ylabel(ylabel_value)
    plt.legend(loc="upper right")
    plt.grid(True)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout
plt.tight_layout()

# Show the plot
plt.savefig('line_20.pdf', bbox_inches='tight')
