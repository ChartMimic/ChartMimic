# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0); np.random.seed(0)

# ===================
# Part 2: Data Preparation
# ===================
# Data
road_conditions = ["Urban", "Suburban", "Highway", "Rural"]
accident_rate_speed30 = [15, 10, 5, 8]
avg_speed_speed30 = [30, 28, 35, 33]
accident_rate_speed50 = [20, 15, 10, 12]
avg_speed_speed50 = [50, 48, 55, 53]
colors = ["#736aa6", "#983530", "#f2bf42", "#5384ed"]
labels = ["Accident Rate", "Average Speed"]

# X-axis positions
x = np.arange(len(road_conditions))
indexs = [2, 4]

# Plot labels
speed30_title = "(a) Speed Limit 30 mph"
speed50_title = "(b) Speed Limit 50 mph"
ylabel_speed30 = "Average Speed (mph)"
ylabel_speed50 = "Accident Rate (%)"
yticks_speed30 = [0, 10, 20, 30, 40]
yticks_speed50 = [10, 25, 40, 55, 70]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(5, 6))

barwidth = 0.3
# Movielens subplot
for i in range(len(x)):
    ax1.bar(
        (i - 2) * 0.3 + indexs[0],
        accident_rate_speed30[i],
        width=0.3,
        label="Accuracy",
        color=colors[i],
    )
    ax1.bar(
        (i - 2) * 0.3 + indexs[1],
        avg_speed_speed30[i],
        width=0.3,
        label="Unfairness",
        color=colors[i],
    )
ax1.set_title(speed30_title)
ax1.set_xticks([index - 0.15 for index in indexs])
ax1.set_xticklabels(labels)
ax1.set_ylabel(ylabel_speed30)
ax1.set_yticks(yticks_speed30)
ax1.tick_params(axis="both", which="both", length=0)

# Tenrec subplot
for i in range(len(x)):
    ax2.bar(
        (i - 2) * 0.3 + indexs[0],
        accident_rate_speed50[i],
        width=0.3,
        label="Accuracy",
        color=colors[i],
    )
    ax2.bar(
        (i - 2) * 0.3 + indexs[1],
        avg_speed_speed50[i],
        width=0.3,
        label="Unfairness",
        color=colors[i],
    )
ax2.set_title(speed50_title)
ax2.set_xticks([index - 0.15 for index in indexs])
ax2.set_xticklabels(labels)
ax2.set_ylabel(ylabel_speed50)
ax2.set_yticks(yticks_speed50)

ax2.tick_params(axis="both", which="both", length=0)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and save the figure
plt.tight_layout()
plt.savefig('bar_48.pdf', bbox_inches='tight')
