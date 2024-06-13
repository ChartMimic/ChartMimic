# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Sample data (replace with actual values)
users = [20, 40, 60, 80, 100]
cnn = [0.5, 0.65, 0.7, 0.72, 0.75]
cnn_hmm = [0.55, 0.6, 0.65, 0.68, 0.7]
rf = [0.45, 0.55, 0.6, 0.62, 0.65]
rf_hmm = [0.48, 0.58, 0.63, 0.65, 0.68]

# Axes Limits and Labels
xlabel_value = "No. of Users in Development Set"
xlim_values = [5, 105]
xticks_values = np.arange(20, 101, 20)

ylabel_value = "F1"
ylim_values = [0.44, 0.76]
yticks_values = np.arange(0.45, 0.76, 0.05)

# Labels
label_1 = "CNN"
label_2 = "CNN+HMM"
label_3 = "RF"
label_4 = "RF+HMM"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create the plot
plt.figure(figsize=(6, 4))  # Adjusted to match the original image's dimensions
plt.plot(users, cnn, marker="v", color="#ffa500", label=label_1)
plt.plot(users, cnn_hmm, marker="^", color="#ff4500", label=label_2)
plt.plot(users, rf, marker="s", color="#4169e1", label=label_3)
plt.plot(users, rf_hmm, marker="o", color="#00008b", label=label_4)

# Set x,y-axis to only display specific ticks and extend y-axis to leave space at top
plt.xticks(xticks_values, fontsize=10)
plt.xlim(xlim_values)  # Adjusted y-axis limit
plt.yticks(yticks_values, fontsize=10)
plt.ylim(ylim_values)  # Adjusted x-axis limit

# Add vertical dotted line
plt.axvline(x=20, color="blue", linestyle=":", linewidth=1.2)

# Add legend
plt.legend(loc="lower right", fontsize=12)

# Add labels and title
plt.xlabel(xlabel_value, fontsize=12)
plt.ylabel(ylabel_value , fontsize=12)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and save plot
plt.tight_layout()
plt.savefig('line_33.pdf', bbox_inches='tight')
