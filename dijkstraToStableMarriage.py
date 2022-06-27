'''
Peter Yu
6/26/2022
'''

import networkx as nx
import matplotlib.pyplot as plt

# Intitalization of graph
G = nx.Graph()

edges = [('A', 'b'), ('b', 'a'), ('b', 'c'), ('c', 'a'), ('B', 'c'), ('C', 'a')]

G.add_edges_from(edges)
pos = nx.spring_layout(G)
plt.figure()

nx.draw(
    G, pos, edge_color='black', width=1, linewidths=1,
    node_size=500, node_color='pink', alpha=0.9,
    labels={node: node for node in G.nodes()}
)

nx.draw_networkx_edge_labels(
    G, pos,
    edge_labels={('A', 'b'): 2, 
                 ('b', 'a'): 3, 
                 ('b', 'c'): 5,
                 ('c', 'a'): 7,
                 ('B', 'c'): 1,
                 ('C', 'a'): 1},
    font_color='red'
)

# Used for visualization purposes
plt.axis('off')
plt.show()

# ------------------------------------- This Part is to get the preference matricies and connect it with the stable marriage problem ---------------------------------------------------------
men = ['A', 'B', 'C']
women = ['a', 'b', 'c']

# Lengths of each edge
lengths = {
    ('A', 'b'): 2, 
    ('b', 'a'): 3, 
    ('b', 'c'): 5,
    ('c', 'a'): 7,
    ('B', 'c'): 1,
    ('C', 'a'): 1,
}

# Adding reverse tuples to lengths
for i in range(len(lengths)):
    lengths.update({(list(lengths.keys())[i])[::-1]: list(lengths.values())[i]})
lengths

pref = {
    'A': {},
    'B': {},
    'C': {}
}

for i in range(len(men)):
    for j in range(len(women)):
        current_path = nx.shortest_path(G, source=men[i], target=women[j])
        
        l = 0
        
        for k in range(len(current_path) - 1):
            l = (l + lengths[(current_path[k], current_path[k + 1])])
        
        pref[men[i]].update({current_path[-1]: l})
        
# Sorting preferences by length
pref_final = {}
for i in range(len(pref)):
    sorted_preferences = dict(sorted(pref[men[i]].items(), key=lambda item: item[1]))
    pref_final.update({men[i]: sorted_preferences})
    
  
pref_final
# The dataset in this file results in the preferences:
# {'A': {'b': 2, 'a': 5, 'c': 7},
#  'B': {'c': 1, 'b': 6, 'a': 8},
#  'C': {'a': 1, 'b': 4, 'c': 8}}

# You can use NetworkX to compute shortest path in a graph and find the length
# https://networkx.org/documentation/stable/reference/algorithms/shortest_paths.html
