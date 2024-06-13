import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Sample data for reproduction
bits = np.arange(16)
recall_sum_transport = np.array(
    [300, 280, 270, 450] + sorted(list(np.random.randint(250, 450, 12)))
)
recall_sum_technology = np.array(
    [310, 290, 265, 450] + sorted(list(np.random.randint(250, 450, 12)))
)
ot_recall = [sorted(np.random.randint(50, 250, 12), reverse=True) for i in range(2)]

# Creating an array of bits to adjust spacing for the bars
adjusted_bits = np.array(bits, dtype=float)
# Adjust spacing for purple and the three bars before it
adjusted_bits[3] += 0.5
# Adjust spacing between the red/blue bars and the others
adjusted_bits[4:] += 4

title = "Public Transport"
xlabel = "Number of Sensors"
ylabel = "Signal Strength"
ylim = [0, 480]
axhline = 450

title2 = "Technology Devices"
xlabel2 = "Number of Sensors"
ylabel2 = "Signal Strength"
ylim2 = [0, 480]
axhline2 = 450
xticks = adjusted_bits[4:]
xtickslabel = np.arange(0, 12)

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Set figure size to match original image dimensions

blue_colors = [plt.cm.Blues(i) for i in np.linspace(0.8, 0.5, 10)]
red_colors = [plt.cm.Reds(i) for i in np.linspace(0.3, 0.7, 10)]
plt.figure(figsize=(10, 4))

# Subplot 1: Flickr30k
plt.subplot(1, 2, 1)
plt.bar(
    adjusted_bits[:4],
    recall_sum_transport[:4],
    color=["#4a895c", "#c3884c", "#75140c", "purple"],
)
plt.bar(adjusted_bits[4:], recall_sum_transport[4:], color=blue_colors)
plt.bar(adjusted_bits[4:], ot_recall[0], width=0.5, color=red_colors)
plt.title(title, y=-0.3)
plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.ylim(ylim)
plt.xticks(xticks,xtickslabel)
plt.axhline(axhline, linestyle="dotted", color="black")

# Subplot 2: MS-COCO
plt.subplot(1, 2, 2)
plt.bar(
    adjusted_bits[:4],
    recall_sum_technology[:4],
    color=["#4a895c", "#c3884c", "#75140c", "purple"],
)
plt.bar(adjusted_bits[4:], recall_sum_technology[4:], color=blue_colors)
plt.bar(adjusted_bits[4:], ot_recall[1], width=0.5, color=red_colors)
plt.title(title2, y=-0.3)
plt.xlabel(xlabel2)
plt.ylabel(ylabel2)
plt.ylim(ylim2)
plt.xticks(xticks,xtickslabel)
plt.axhline(axhline2, linestyle="dotted", color="black")

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and display the plot
plt.tight_layout()
plt.savefig('HR_3.pdf', bbox_inches='tight')
