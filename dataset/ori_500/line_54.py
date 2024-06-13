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
relaxation_snow = [0.7, 0.6, 0.5, 0.2]  # Additional data for snow condition
relaxation_fog = [1.0, 0.8, 0.7, 0.4]  # Additional data for fog condition
error = [0.05, 0.05, 0.05, 0.05]

# Axes Limits and Labels
xlabel_value = "Driving Style"

ylabel_value = "Relaxation Level"
ylim_values = [0, 1.5]

# Titles
titles = ["Dry vs Rain", "Snow vs Fog", "Rain vs Snow"]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create a 1x3 subplot layout
fig, axs = plt.subplots(1, 3, figsize=(12, 4))

# Titles and setup for subplots
data_pairs = [
    (relaxation_dry, relaxation_rain),
    (relaxation_snow, relaxation_fog),
    (relaxation_rain, relaxation_snow),
]
colors_pairs = [("black", "red"), ("blue", "green"), ("red", "blue")]

# Plot each condition in a separate subplot
for ax, title, (data1, data2), (color1, color2) in zip(
    axs, titles, data_pairs, colors_pairs
):
    ax.errorbar(
        driving_styles,
        data1,
        yerr=error,
        fmt="o-",
        color=color1,
        ecolor=color1,
        elinewidth=2,
        capsize=5,
        capthick=2,
        label=f'{title.split(" vs ")[0]}',
    )
    ax.errorbar(
        driving_styles,
        data2,
        yerr=error,
        fmt="s-",
        color=color2,
        ecolor=color2,
        elinewidth=2,
        capsize=5,
        capthick=2,
        label=f'{title.split(" vs ")[1]}',
    )
    ax.set_xlabel(xlabel_value)
    ax.set_ylabel(ylabel_value)
    ax.tick_params(
        axis="both", which="major", length=5, direction="in", top=True, right=True
    )
    ax.legend(loc="upper right", frameon=True)
    ax.set_ylim(ylim_values)
    ax.grid(True, which="major", linestyle="--", linewidth=0.5, alpha=0.5)
    ax.set_title(title)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and save the figure
plt.tight_layout()
plt.savefig('line_54.pdf', bbox_inches='tight')
