import matplotlib.pyplot as plt
import networkx as nx

# ===================
# Part 2: Data Preparation
# ===================
# Create a directed graph
G = nx.DiGraph()

# Add nodes with their respective colors
nodes = {
    0: "teal",
    1: "coral",
    2: "gold",
    3: "indigo",
    4: "skyblue",
    5: "salmon",
    6: "orchid",
}
for node, color in nodes.items():
    G.add_node(node, color=color)

# Add edges with labels representing network connections
edges = [(0, 2, "2"), (1, 5, "44"), (2, 5, "91"), 
         (3, 1, "57"), (4, 2, "59"), (5, 6, "97")]
for u, v, label in edges:
    G.add_edge(u, v, label=label)

# Define node positions in a circular layout
pos = nx.circular_layout(G)

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
fig = plt.subplots(figsize=(8, 8))

# Draw nodes with color attribute
node_colors = [G.nodes[node]["color"] for node in G.nodes]
nx.draw_networkx_nodes(G, pos, node_color=node_colors)

# Draw edges with labels
nx.draw_networkx_edges(G, pos, arrows=True)
edge_labels = {(u, v): G[u][v]["label"] for u, v in G.edges}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# Remove axis
plt.axis("off")

# ===================
# Part 4: Saving Output
# ===================
# Displaying the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig('graph_1.pdf', bbox_inches='tight')
