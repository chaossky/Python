import networkx as nx
import matplotlib.pyplot as plt

G=nx.random_geometric_graph(50,0.3)
plt.figure(figsize=(6,6))
nx.draw(G,node_size=40,alpha=0.7)
plt.title("Brain Connectivity Network")
plt.show()