# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import networkx as nx

# ===================
# Part 2: Data Preparation
# ===================
G = nx.house_graph()
# explicitly set positions
pos = {0: (0, 0), 1: (1, 0), 2: (0, 1), 3: (1, 1), 4: (0.5, 2.0)}

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
plt.figure(figsize=(10, 8))

nx.draw_networkx_nodes(G, pos, node_size=2000, nodelist=[4], node_color="teal")
nx.draw_networkx_nodes(
    G, pos, node_size=3000, nodelist=[0, 1, 2, 3], node_color="orchid"
)
nx.draw_networkx_edges(G, pos, alpha=0.5, width=6)
# Adding text annotations
labels = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4"}
nx.draw_networkx_labels(G, pos, labels=labels, font_size=16)
plt.axis("off")

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig("graph_4.pdf", bbox_inches="tight")
