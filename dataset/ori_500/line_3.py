# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Data for ogbl-collab
collab_x = np.array(
    ["All", "MLP", "GCN", "NCN", "NCNC", "NeoGNN-BUDDY", "SEAL", "Node2Vec"]
)
collab_y = np.array([75, 73, 72, 70, 69, 71, 73, 74])
collab_err = np.array([5, 4, 4, 3, 3, 4, 4, 5])

# Data for ogbl-ppa
ppa_x = np.array(
    ["All", "MLP", "GCN", "NCN", "NCNC", "NeoGNN-BUDDY", "SEAL", "Node2Vec"]
)
ppa_y = np.array([65, 63, 62, 60, 59, 61, 63, 64])
ppa_err = np.array([5, 4, 4, 3, 3, 4, 4, 5])
# Labels
label_ogbl_collab = "ogbl-collab"
label_ogbl_ppa = "ogbl-ppa"

# Axes Limits and Labels
ylabel_value = "Hits@50"
yticks_values = np.arange(40, 81, 10)
ylim_values = [40, 85]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Plotting the data
plt.figure(
    figsize=(10, 5)
)  # Adjusting figure size to match the original image's dimensions
plt.errorbar(
    collab_x,
    collab_y,
    yerr=collab_err,
    fmt="o-",
    label= label_ogbl_collab,
    color="#3d89be",
    capsize=5,
)
plt.errorbar(
    ppa_x,
    ppa_y,
    yerr=ppa_err,
    fmt="--",
    label=label_ogbl_ppa,
    color="#ff7f0e",
    marker="s",
    capsize=5,
)

# Set x,y-axis to only display specific ticks and extend y-axis to leave space at top
plt.yticks(yticks_values, fontsize=16)
plt.ylim(ylim_values)  # Adjusted y-axis limit

# set x-axis label to be rotated
plt.xticks(rotation=45, fontsize=12)

# Adding labels and title
plt.ylabel(ylabel_value, fontsize=16)
plt.legend(loc="upper center", bbox_to_anchor=(0.72, 1), ncol=2, fontsize=16)

# Adjusting figure size to match the original image's dimensions of 360 (height) by 720 (width)
plt.gcf().set_size_inches(10, 5)

# ===================
# Part 4: Saving Output
# ===================
# Adjusting layout to reduce white space
plt.tight_layout()
plt.savefig('line_3.pdf', bbox_inches='tight')
