# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import networkx as nx

# ===================
# Part 2: Data Preparation
# ===================
# Create a cycle graph with 12 nodes
G = nx.cycle_graph(12)
weights = {edge: i + 1 for i, edge in enumerate(G.edges())}
nx.set_edge_attributes(G, weights, "weight")

pos = nx.spring_layout(G, iterations=200)

labels = {i: str(i) for i in range(12)}

# Draw edge labels
edge_labels = nx.get_edge_attributes(G, "weight")

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
plt.figure(figsize=(10, 8))
nx.draw(G, pos, node_size=800, node_color="gold")
nx.draw_networkx_labels(G, pos, labels=labels)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# ===================
# Part 4: Saving Output
# ===================
# Show the plot
plt.tight_layout()
plt.savefig("graph_3.pdf", bbox_inches="tight")
