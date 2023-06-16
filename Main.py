import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_excel("./KPNetwork.xlsx")
G = nx.Graph()
for index, row in df.iterrows():
    node1 = row[0]  # Première colonne
    node2 = row[1]  # Deuxième colonne
    G.add_edge(node1, node2)

nx.draw(G, with_labels=True)
plt.savefig("net.png")
plt.show()

# Graph with 0 nodes and 0 edges