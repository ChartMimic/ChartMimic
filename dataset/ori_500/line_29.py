# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Data for plotting
xllm_steps = range(1, 21)
xLLM_fidelity = [
    0.1,
    0.125,
    0.15,
    0.1625,
    0.175,
    0.1875,
    0.2,
    0.2125,
    0.225,
    0.2375,
    0.25,
    0.25625,
    0.2625,
    0.26875,
    0.275,
    0.275,
    0.275,
    0.275,
    0.275,
    0.275,
]
single_steps = [0, 21]
single_pass_fidelity = [0.1] * len(single_steps)

# Axes Limits and Labels
xlabel_value = "# of Steps"
xlim_values = [0, 21]
xticks_values = [0, 5, 10, 15, 20]

ylabel_value = "Avg. Fidelity"
ylim_values = [0, 100]

# Labels
label_1 = "xLLM"
label_2 = "Single-Pass LLM"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Plotting the lines
plt.figure(figsize=(4, 3))
plt.plot(xllm_steps, xLLM_fidelity, "o-.", label=label_1, color="#8280cd")
plt.plot(single_steps, single_pass_fidelity, "-", label=label_2, color="red")

# Adding legend
plt.legend()

# Labeling axes
plt.xlabel(xlabel_value)
plt.ylabel(ylabel_value)
plt.xlim(xlim_values)
plt.xticks(xticks_values)

# ===================
# Part 4: Saving Output
# ===================
# Display the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig('line_29.pdf', bbox_inches='tight')
