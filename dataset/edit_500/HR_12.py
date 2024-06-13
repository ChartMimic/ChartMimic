import matplotlib.pyplot as plt
from matplotlib import patches
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Given data
features = [
    "accuracy",
    "clarity",
    "conciseness",
    "coherence",
    "relevance",
    "depth of information",
    "engagement",
    "originality",
    "organization",
    "technical correctness",
    "creativity",
]
impact_values = [0.01, 0.03, 0.02, -0.01, 0.02, 0.03, -0.02, 0.05, -0.04, 0.1, 0.15]
# Starting x-axis value
start_x = 0.60
cumulative_values = [start_x]

axvhline = 0.85
ylim = [-0.5, 11]
xlim = [0.5, 0.9]
xticks = [0.55, 0.60, 0.65, 0.70, 0.75, 0.80, 0.85]
textposition = [[0.85, 10.5], [0.60, -2]]
textlabels = ["f(x) = 0.85", "f(x) = 0.60"]
ylim = [-0.5, 11]
xlim = [0.5, 1]
xticks = [0.55, 0.60, 0.65, 0.70, 0.75, 0.80, 0.85,0.90,0.95,1.0]
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Calculate the start point for each bar
for impact in impact_values:
    next_value = cumulative_values[-1] + impact
    cumulative_values.append(next_value)

# Define colors for positive and negative impact
colors = ["#ea3356" if impact > 0 else "#3d89f3" for impact in impact_values]

fig, ax = plt.subplots(figsize=(8, 6))
# Add dashed lines to connect bars
for i in range(len(impact_values) - 1):
    plt.plot(
        [cumulative_values[i + 1], cumulative_values[i + 1]],
        [features[i], features[i + 1]],
        "k--",
        linewidth=0.5,
        color="gray",
    )
# Customize bars with arrows

# Drawing pencil-shaped bars with two right corners cut off
for idx, (feature, impact) in enumerate(zip(features, impact_values)):
    left = cumulative_values[idx]
    bar_width = 0.6  # Set the bar width

    if impact > 0:
        color = "#ea3356"
        width = impact
        text_x = left + width
        # Draw the main bar body
        ax.add_patch(
            patches.Rectangle(
                (left, idx - bar_width / 2),
                width - 0.005,
                bar_width,
                facecolor=color,
            )
        )
        # Draw the tip
        ax.add_patch(
            patches.Polygon(
                [
                    (left + width - 0.005, idx - bar_width / 2),
                    (left + width, idx),
                    (left + width - 0.005, idx + bar_width / 2),
                ],
                closed=True,
                facecolor=color,
            )
        )
        ax.text(text_x, idx, f"+{impact}", va="center", ha="left", color="#ea3356")
    else:
        color = "#3d89f3"
        width = -impact  # Width is positive for drawing
        text_x = left - width
        if impact == 0:
            ax.add_patch(
                patches.Rectangle(
                    (left - width, idx - bar_width / 2),
                    width,
                    bar_width,
                    facecolor=color,
                    edgecolor=color,
                )
            )
        else:
            # Draw the main bar body
            ax.add_patch(
                patches.Rectangle(
                    (left - width + 0.005, idx - bar_width / 2),
                    width - 0.005,
                    bar_width,
                    facecolor=color,
                )
            )
            # Draw the tip
            ax.add_patch(
                patches.Polygon(
                    [
                        (left - width + 0.005, idx - bar_width / 2),
                        (left - width, idx),
                        (left - width + 0.005, idx + bar_width / 2),
                    ],
                    closed=True,
                    facecolor=color,
                )
            )

        ax.text(
            text_x, idx, f"-{np.abs(impact)}", va="center", ha="right", color="#3d89f3"
        )

ax.axvline(axvhline, linestyle="--", color="gray", alpha=0.3)
# Set labels and title
ax.yaxis.grid(True, linestyle="dotted", color="gray", alpha=0.3)
ax.set_axisbelow(True)
ax.tick_params(axis="both", length=0)
# Remove spines
ax.spines["right"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.set_ylim(ylim)
ax.set_xlim(xlim)
ax.set_xticks(xticks)
# Adjust layout to make room for labels and display the plot
# Add text annotation for f(x)
ax.text(textposition[0][0], textposition[0][1], textlabels[0], va="bottom", ha="center", color="grey")
ax.text(textposition[1][0], textposition[1][1], textlabels[1], va="bottom", ha="center", color="grey")

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig('HR_12.pdf', bbox_inches='tight')
