# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Data
devices = ["Lighting", "Thermostat", "Security", "Speakers", "Appliances", "Camera", "Locks", "Sensors"]
very_dissatisfied = [50, 30, 0, 0, 0, 15, 0, 0]
dissatisfied = [0, 0, 40, 20, 0, 0, 0, 0]
neutral = [0, 0, 0, 0, 60, 0, 0, 0]
satisfied = [0, 0, 0, 0, 0, 0, 80, 67]
# very_satisfied = [150, 100, 60, 70, 90, 80, 75, 60]
labels = ["Very Dissatisfied", "Dissatisfied", "Neutral", "Satisfied", ]
xlabel = "Smart Home Devices"
ylabel = "Number of Users"
ylim = [0, 100]


# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Set figure size to match the original image's dimensions
plt.figure(figsize=(6, 4))

# Plotting
bar_width = 0.8
index = np.arange(len(devices))

plt.bar(index, very_dissatisfied, bar_width, color="red", label=labels[0])
plt.bar(index, dissatisfied, bar_width, color="green", label=labels[1], bottom=very_dissatisfied)
plt.bar(
    index,
    neutral,
    bar_width,
    color="grey",
    label=labels[2],
    bottom=[i + j for i, j in zip(very_dissatisfied, dissatisfied)],
)
plt.bar(
    index,
    satisfied,
    bar_width,
    color="orange",
    label=labels[3],
    bottom=[i + j + k for i, j, k in zip(very_dissatisfied, dissatisfied, neutral)],
)

# Labels and Title
plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.ylim(ylim)
# plt.title('Emotion Frequencies by Sentiment')
plt.xticks(index, devices, rotation=45, ha="center")
plt.legend(loc="upper left")

# ===================
# Part 4: Saving Output
# ===================
# Show plot
plt.tight_layout()
plt.savefig('bar_26.pdf', bbox_inches='tight')
