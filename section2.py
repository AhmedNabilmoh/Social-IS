import networkx as nx
G = nx.Graph()
nodes_to_add = ['a','b', 'c', 'd','e','f','g']
G.add_nodes_from(nodes_to_add)
edges_to_add = [('a', 'c'), ('b', 'c'), ('c', 'd'),('d','e'),('g','b'),('a','f')]
G.add_edges_from(edges_to_add)

nx.draw(G,with_labels=True,
        node_color='red',
        node_size=1600,
        font_color='white',
        font_size=30,)
print(G.nodes())
print(G.edges())

for node in G.nodes:
    print(node)
for edge in G.edges:
    print(edge)
    
    
print(G.number_of_nodes())
print(G.number_of_edges())

for neighbor in G.neighbors('f'):
    print(neighbor)
    
print(list(G.neighbors('f')))
print(nx.is_tree(G))
print(nx.is_connected(G))

print(G.has_node('a'))
print(G.has_edge('a', 'c'))


print(G.has_node('a'))
print(G.has_edge('a', 'd'))

print(G.degree('a'))
len(list(G.neighbors('a')))

print(G.nodes())
print([G.degree(n) for n in G.nodes()])

items = ['spider', 'y', 'banana']
[item.upper() for item in items]
print(G.nodes())
print([G.degree(n) for n in G.nodes()])
g = (len(item) for item in items)
list(g)

G = nx.Graph()

G.add_nodes_from(['cat','dog','virus',13])

G.add_edge('cat','dog')

nx.draw(G, with_labels=True, font_color='white', node_size=1000)

D = nx.DiGraph()

D.add_edges_from([('a','b'),('b','c'),('b','a'),('c','b'),('d','e'),('e','d'),('a','e'),('e','a'),('d','c'),('c','d')])

nx.draw(D, with_labels=True)

print(D.has_edge('a','b'))
print('Successors of 2:', list(D.successors('a')))
print('Predecessors of 2:', list(D.predecessors('b')))
print(D.in_degree('a'))
print(D.out_degree('e'))

D.degree('a')
print('Successors of 2:', list(D.successors('c')))
print('"Neighbors" of 2:', list(D.neighbors('d')))