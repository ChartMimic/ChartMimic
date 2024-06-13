# ===================
# Part 1: Importing Libraries
# ===================
import networkx as nx
import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Create a graph and add a self-loop to node 0
G = nx.complete_graph(3, create_using=nx.DiGraph)
# G.add_edge(0, 0)
pos = nx.circular_layout(G)

# Add self-loops to the remaining nodes
edgelist = [(1, 1), (2, 2), (0, 0)]
G.add_edges_from(edgelist)

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
plt.figure(figsize=(10, 8))

# As of version 2.6, self-loops are drawn by default with the same styling as
# other edges
nx.draw(G, pos, with_labels=True, node_color="coral")

# Draw the newly added self-loops with different formatting
nx.draw_networkx_edges(G, pos, edgelist=edgelist, arrowstyle="<|-", style="dashed")

# ===================
# Part 4: Saving Output
# ===================
# Displaying the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig("graph_5.pdf", bbox_inches="tight")
