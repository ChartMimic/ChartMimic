# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Create a random graph
G = nx.random_geometric_graph(30, 0.3)

# Position the nodes based on their connections using a different layout algorithm
pos = nx.kamada_kawai_layout(
    G
)  # This layout algorithm may produce a more spread-out layout

# Randomly select some edges to color blue
edges = list(G.edges())
blue_edges = np.random.choice(
    len(edges), size=int(len(edges) * 0.3), replace=False
)  # 30% of the edges
blue_edges = [edges[i] for i in blue_edges]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
fig = plt.subplots(figsize=(8, 8))

# Draw the nodes
nx.draw_networkx_nodes(G, pos, node_size=200, node_color="pink")

# Draw the edges
nx.draw_networkx_edges(G, pos, alpha=0.3)

# Draw the selected edges in blue
nx.draw_networkx_edges(G, pos, edgelist=blue_edges, edge_color="#d0e2e8")

# Remove axis
plt.axis("off")

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig("graph_2.pdf", bbox_inches="tight")
