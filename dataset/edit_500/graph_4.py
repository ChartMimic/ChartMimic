import matplotlib.pyplot as plt
import networkx as nx

# ===================
# Part 2: Data Preparation
# ===================
# Create a new graph representing a smart home network
G = nx.Graph()
# Add nodes representing different smart devices
devices = {
    0: "Smart Hub",
    1: "Thermostat",
    2: "Light Sensor",
    3: "Security Camera",
    4: "Smart Lock"
}
G.add_nodes_from(devices.keys())
# Add edges representing connections between devices
G.add_edges_from([(0, 1), (0, 2), (0, 3), (0, 4)])

# explicitly set positions for visual appeal
pos = {0: (0, 0), 1: (1, 0), 2: (0, 1), 3: (1, 1), 4: (0.5, 2.0)}

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
plt.figure(figsize=(10, 8))

# Draw nodes with specific colors and sizes
nx.draw_networkx_nodes(G, pos, node_size=2000, nodelist=[4], node_color="teal")
nx.draw_networkx_nodes(G, pos, node_size=3000, nodelist=[0, 1, 2, 3], node_color="orchid")

# Draw edges with specific style
nx.draw_networkx_edges(G, pos, alpha=0.5, width=6)

# Adding text annotations for devices
nx.draw_networkx_labels(G, pos, labels=devices, font_size=16)
plt.axis("off")

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig('graph_4.pdf', bbox_inches='tight')
