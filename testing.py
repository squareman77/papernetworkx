
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
from networkx import Graph
from networkx import algorithms



for i in range(100):
    a = 1000 + 50*i
    b=(np.log(a))/a
    c=0

    graph = nx.gn_graph(a, kernel=lambda x: 1)
    graph= graph.to_undirected()
    graph2 = nx.erdos_renyi_graph(a,b)
    graph = nx.compose(graph, graph2)

    dictionary = algorithms.edge_betweenness_centrality(graph, k=None, normalized=False, weight=None, seed=None)

    for key, value in dictionary.items():
        if(value >= dictionary[(0,1)]):
            c+= 1
    print(c)




# print(graph.edges())

# nx.draw(graph)
# plt.show()