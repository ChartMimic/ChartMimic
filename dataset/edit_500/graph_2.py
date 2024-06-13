import matplotlib.pyplot as plt
import networkx as nx
import numpy as np; np.random.seed(0); np.random.seed(0)

# ===================
# Part 2: Data Preparation
# ===================
# Create a random transportation network graph
transport_network = nx.random_geometric_graph(10, 0.3)

# Position the nodes based on their connections using a different layout algorithm
pos = nx.kamada_kawai_layout(
    transport_network
)  # This layout algorithm may produce a more spread-out layout

# Randomly select some routes to color blue
routes = list(transport_network.edges())
highlighted_routes = np.random.choice(
    len(routes), size=int(len(routes) * 0.3), replace=False
)  # 30% of the routes
highlighted_routes = [routes[i] for i in highlighted_routes]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
fig = plt.subplots(figsize=(8, 8))

# Draw the locations
nx.draw_networkx_nodes(transport_network, pos, node_size=200, node_color="pink")

# Draw the routes
nx.draw_networkx_edges(transport_network, pos, alpha=0.3)

# Draw the selected routes in blue
nx.draw_networkx_edges(transport_network, pos, edgelist=highlighted_routes, edge_color="#d0e2e8")

# Remove axis
plt.axis("off")

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig('graph_2.pdf', bbox_inches='tight')
