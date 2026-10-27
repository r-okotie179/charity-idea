import networkx as nx

'''
Wanted to more efficiently run the update of the graph, and thus to use this approach
'''

G = nx.path_graph(3)
G.nodes[0].update({'color': 'red', 'score': 10})
G.nodes[1].update({'color': 'blue', 'score': 20})
G.nodes[2].update({'score': 30}) # 'color' is intentionally missing here

attribute_to_remove = 'color'

for node, attr_dict in G.nodes(data=True):
    # Removes 'color', does nothing if 'color' doesn't exist (e.g., node 2)
    attr_dict.pop(attribute_to_remove, None) 

print(G.nodes(data=True))
# Output: [(0, {'score': 10}), (1, {'score': 20}), (2, {'score': 30})]