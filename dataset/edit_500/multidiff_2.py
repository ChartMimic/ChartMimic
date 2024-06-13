import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Data for the histogram: scores from two types of assessments
test_scores_public = np.random.normal(loc=60, scale=10, size=1000)  # e.g., scores from public training facilities
test_scores_private = np.random.normal(loc=100, scale=10, size=1000)  # e.g., scores from private training facilities

# Data for the pie chart: resource allocation
labels = ["Equipment", "Training", "Facilities", "Nutrition", "Coaching"]
budget = [25, 20, 30, 15, 10]
colors = plt.cm.tab20c(np.linspace(0, 1, len(budget)))
explode = (0.1, 0, 0, 0, 0)  # highlight the largest segment
titles= ["Athlete Performance in Training", "Resource Allocation in Sports Facilities"]
xlabel = "Performance Score"
ylabel = "Number of Athletes"
histlabels = ["Public Training", "Private Training"]


# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Set up the figure and grid
fig = plt.figure(figsize=(10, 5))
gs = gridspec.GridSpec(1, 2, figure=fig)

# Histogram plot
axes1 = fig.add_subplot(gs[0, 0])
axes1.hist(
    [test_scores_public, test_scores_private],
    bins=50,
    stacked=True,
    color=["#6495ED", "#FFA07A"],
    label=histlabels,
)
axes1.set_title(titles[0])
axes1.set_xlabel(xlabel)
axes1.set_ylabel(ylabel)
axes1.legend(loc="upper left")

# Pie chart plot
axes2 = fig.add_subplot(gs[0, 1])
axes2.pie(
    budget,
    explode=explode,
    labels=labels,
    colors=colors,
    autopct="%1.1f%%",
    shadow=True,
    startangle=90,
)
axes2.set_title(titles[1])

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and save the figure
plt.tight_layout()
plt.savefig('multidiff_2.pdf', bbox_inches='tight')
