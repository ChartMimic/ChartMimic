import networkx as nx
import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Create a directed graph representing a small transportation network
G = nx.DiGraph()

# Add nodes representing cities
cities = ['Beijing', 'Chengdu', 'Shanghai']
G.add_nodes_from(cities)

# Define edges representing direct transportation routes between cities
edges = [('Beijing', 'Chengdu'), ('Chengdu', 'Shanghai'), ('Shanghai', 'Beijing')]
G.add_edges_from(edges)

# Add self-loops representing intra-city transportation routes
self_loops = [('Beijing', 'Beijing'), ('Chengdu', 'Chengdu'), ('Shanghai', 'Shanghai')]
G.add_edges_from(self_loops)

# Get positions for the nodes in a circular layout
pos = nx.circular_layout(G)

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
plt.figure(figsize=(10, 8))

# Draw the transportation network with nodes and edges
nx.draw(G, pos, with_labels=True, node_color="coral")

# Draw the self-loops with different formatting
nx.draw_networkx_edges(G, pos, edgelist=self_loops, arrowstyle="<|-", style="dashed")

# ===================
# Part 4: Saving Output
# ===================
# Displaying the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig('graph_5.pdf', bbox_inches='tight')
