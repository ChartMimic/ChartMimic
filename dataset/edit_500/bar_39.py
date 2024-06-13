# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Data
categories = ["Apple", "Google", "Microsoft", "Amazon", "Tesla"][::-1]
q1_revenue = [230, 275, 310, 150, 400][::-1]
q2_revenue = [260, 290, 330, 170, 420][::-1]
q3_revenue = [290, 310, 360, 200, 450][::-1]

labels = ["Q1 Revenue", "Q2 Revenue", "Q3 Revenue"]
bar_width = 0.5
y_pos = range(len(categories))


# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Stacked Bar Chart
fig, ax = plt.subplots(figsize=(8, 5))

ax.barh(y_pos, q1_revenue, bar_width, color="#e4754f", label=labels[0])
ax.barh(y_pos, q2_revenue, bar_width, left=q1_revenue, color="#feffc7", label=labels[1])
ax.barh(
    y_pos,
    q3_revenue,
    bar_width,
    left=[i + j for i, j in zip(q1_revenue, q2_revenue)],
    color="#81acce",
    label=labels[2],
)

# Adding the numerical values within each segment
for i in range(len(categories)):
    ax.text(
        q1_revenue[i] / 2,
        i,
        str(q1_revenue[i]),
        ha="center",
        va="center",
        color="white",
    )
    ax.text(
        q1_revenue[i] + q2_revenue[i] / 2,
        i,
        str(q2_revenue[i]),
        ha="center",
        va="center",
        color="black",
    )
    ax.text(
        q1_revenue[i] + q2_revenue[i] + q3_revenue[i] / 2,
        i,
        str(q3_revenue[i]),
        ha="center",
        va="center",
        color="white",
    )

# Labels and Legend
ax.set_xticks([])
ax.set_yticks(y_pos)
ax.set_yticklabels(categories)
ax.legend(loc="upper right")

# ===================
# Part 4: Saving Output
# ===================
# Displaying the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig("bar_39.pdf", bbox_inches="tight")
