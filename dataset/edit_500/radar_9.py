import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Data
categories = ["Urban Transport", "Tech Growth", "Financial Stability", "Healthcare Quality", "Educational Attainment", "Environmental Sustainability"]
values1 = [58.4, 72.1, 63.5, 71.2, 69.0, 66.3]
values2 = [66.5, 67.2, 57.1, 53.8, 50.4, 60.7]
labels = ["Predictive Model 2023", "Predictive Model 2024"]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Number of variables
num_vars = len(categories)

# Compute angle for each category
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# The plot is circular, so we need to "complete the loop" and append the start to the end.
values1 += values1[:1]
values2 += values2[:1]
angles += angles[:1]
# Plot
fig, ax = plt.subplots(figsize=(8, 7), subplot_kw=dict(polar=True))
ax.fill(angles, values1, color="#d1553e", alpha=0.25)
ax.fill(angles, values2, color="#4d88b9", alpha=0.25)
ax.plot(angles, values1, color="#d1553e", linewidth=2, label=labels[0])
ax.plot(angles, values2, color="#4d88b9", linewidth=2, label=labels[1])

# Labels and annotations for each point
for angle, value1, value2 in zip(angles[:-1], values1[:-1], values2[:-1]):
    ax.annotate(
        f"{value1}", xy=(angle, value1), xytext=(5, 5), textcoords="offset points"
    )
    ax.annotate(
        f"{value2}", xy=(angle, value2), xytext=(5, -10), textcoords="offset points"
    )

# Labels for each point
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories)

# remove ylabels
ax.set_yticklabels([])

# Legend
ax.legend(
    loc="lower center",
    bbox_to_anchor=(0.5, -0.1),
    ncol=2,
    frameon=True,
    facecolor="#f2f2f2",
    edgecolor="#f2f2f2",
)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout for better fit and save the plot
plt.tight_layout()
plt.savefig('radar_9.pdf', bbox_inches='tight')
