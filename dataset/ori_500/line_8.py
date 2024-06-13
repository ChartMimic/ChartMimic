# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Data
driving_styles = ["Passive", "Rail", "Replay", "Sportive"]
relaxation_dry = [1.4, 0.9, 0.8, 0.5]
relaxation_rain = [1.3, 1.1, 1.0, 0.3]
error = [0.05, 0.05, 0.05, 0.05]

# Axes Limits and Labels
xlabel_value = "Driving Style"

ylabel_value = "Relaxation Level"
ylim_values = [0, 1.5]

# Labels
label_Dry =" Dry"
label_Rain = "Rain"

# Titles
title = "Weather"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Plot
fig, ax = plt.subplots(figsize=(6, 6))
ax.errorbar(
    driving_styles,
    relaxation_dry,
    yerr=error,
    fmt="o-",
    color="black",
    ecolor="black",
    elinewidth=2,
    capsize=5,
    capthick=2,
    label=label_Dry,
)
ax.errorbar(
    driving_styles,
    relaxation_rain,
    yerr=error,
    fmt="s-",
    color="red",
    ecolor="red",
    elinewidth=2,
    capsize=5,
    capthick=2,
    label=label_Rain,
)

# Customization
ax.set_xlabel(xlabel_value)
ax.set_ylabel(ylabel_value)

ax.tick_params(
    axis="both", which="major", length=5, direction="in", top=True, right=True
)
ax.legend(title=title, loc="lower left", frameon=False)
ax.set_ylim(ylim_values)

# ===================
# Part 4: Saving Output
# ===================
# Show plot
plt.tight_layout()
plt.savefig('line_8.pdf', bbox_inches='tight')
