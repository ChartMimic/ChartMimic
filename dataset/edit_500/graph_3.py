import matplotlib.pyplot as plt
import networkx as nx

# ===================
# Part 2: Data Preparation
# ===================
# Create a cycle graph with 12 nodes representing tech companies
tech_graph = nx.cycle_graph(12)
connection_strengths = {edge: (i + 1) * 10 for i, edge in enumerate(tech_graph.edges())}
nx.set_edge_attributes(tech_graph, connection_strengths, "connection_strength")

layout_pos = nx.spring_layout(tech_graph, iterations=200)

company_labels = {i: f"Company {i}" for i in range(12)}

# Draw edge labels
edge_labels = nx.get_edge_attributes(tech_graph, "connection_strength")

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
plt.figure(figsize=(10, 8))
nx.draw(tech_graph, layout_pos, node_size=800, node_color="gold")
nx.draw_networkx_labels(tech_graph, layout_pos, labels=company_labels)
nx.draw_networkx_edge_labels(tech_graph, layout_pos, edge_labels=edge_labels)

# ===================
# Part 4: Saving Output
# ===================
# Show the plot
plt.tight_layout()
plt.savefig('graph_3.pdf', bbox_inches='tight')
