
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
from networkx import Graph
from networkx import algorithms



for i in range(100):
    #Size of graph
    a = 1000 + 50*i
    #Noise edge probability
    b=(np.log(a))/a
    #Count of number of edges with at least the centrality of edge 0-1 
    c=0

    #Create UA graph with size a
    graph = nx.gn_graph(a, kernel=lambda x: 1)
    #Make undirected
    graph= graph.to_undirected()
    #Erdos renyi noise edges
    graph2 = nx.erdos_renyi_graph(a,b)
    #Compose graphs
    graph = nx.compose(graph, graph2)

    dictionary = algorithms.edge_betweenness_centrality(graph, k=None, normalized=False, weight=None, seed=None)

    for key, value in dictionary.items():
        if(value >= dictionary[(0,1)]):
            c+= 1
    print(c)




# print(graph.edges())

# nx.draw(graph)
# plt.show()
