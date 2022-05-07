#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random

get_ipython().run_line_magic('matplotlib', 'inline')
import networkx as nx


# In[3]:


G = nx.Graph()
nx.add_cycle(G,[0, 1, 2, 3])
nx.add_cycle(G,[4, 5, 6, 7])
G.add_edge(0, 7)

nx.draw(G, with_labels=True)


# In[4]:


partition = [
    {1, 2, 3},
    {4, 5, 6},
    {0, 7},
]


# In[5]:


nx.community.is_partition(G, partition)


# In[6]:


partition_map = {}
for idx, cluster_nodes in enumerate(partition):
    for node in cluster_nodes:
        partition_map[node] = idx

partition_map


# In[7]:


partition_map[0] == partition_map[7]


# In[8]:


node_colors = [partition_map[n] for n in G.nodes]
        
nx.draw(G, node_color=node_colors, with_labels=True)


# In[9]:


def modularity(G, partition):
    W = sum(G.edges[v, w].get('weight', 1) for v, w in G.edges)
    summation = 0
    for cluster_nodes in partition:
        s_c = sum(G.degree(n, weight='weight') for n in cluster_nodes)
        # Use subgraph to count only internal links
        C = G.subgraph(cluster_nodes)
        W_c = sum(C.edges[v, w].get('weight', 1) for v, w in C.edges)
        summation += W_c - s_c ** 2 / (4 * W)
    
    return summation / W


# In[10]:


modularity(G, partition)


# In[11]:


partition_2 = [
    {0, 1, 2, 3},
    {4, 5, 6, 7},
]
modularity(G, partition_2)


# In[12]:


nx.community.quality.modularity(G, partition_2)


# In[13]:


K = nx.karate_club_graph()
nx.draw(K, with_labels=True)


# In[14]:


K.nodes[0]


# In[16]:


K.nodes[9]


# In[22]:


K = nx.karate_club_graph()
club_color = {
    'Mr. Hi': 'orange',
    'Officer': 'lightblue',
}
node_colors = [club_color[K.nodes[n]['club']] for n in K.nodes]
nx.draw(K, node_color=node_colors, with_labels=True)


# In[24]:


groups = {
    'Mr. Hi': set(),
    'Officer': set(),
}

for n in K.nodes:
    club = K.nodes[n]['club']
    groups[club].add(n)
    
groups


# In[25]:


empirical_partition = list(groups.values())
empirical_partition


# In[26]:


nx.community.is_partition(K, empirical_partition)


# In[27]:


nx.community.quality.modularity(K, empirical_partition)


# In[28]:


random_nodes = random.sample(K.nodes, 17)
random_partition = [set(random_nodes),
                    set(K.nodes) - set(random_nodes)]
random_partition


# In[29]:


random_node_colors = ['orange' if n in random_nodes else 'lightblue' for n in K.nodes]
nx.draw(K, node_color=random_node_colors)


# In[30]:


nx.community.quality.modularity(K, random_partition)


# In[31]:


G = nx.karate_club_graph()
nx.draw(G)


# In[32]:


nx.edge_betweenness_centrality(G)


# In[33]:


my_edge_betweenness = nx.edge_betweenness_centrality(G)
my_edge_betweenness[0, 1]


# In[34]:


my_edge_betweenness.get((0, 1))


# In[35]:


max(my_edge_betweenness, key=my_edge_betweenness.get)


# In[36]:


max(G.edges(), key=my_edge_betweenness.get)


# In[37]:


my_edge_betweenness = nx.edge_betweenness_centrality(G)
most_valuable_edge = max(G.edges(), key=my_edge_betweenness.get)
G.remove_edge(*most_valuable_edge)


# In[38]:


nx.connected_components(G)


# In[39]:


list(nx.connected_components(G))


# In[40]:


G = nx.karate_club_graph()
partition_sequence = []
for _ in range(G.number_of_edges()):
    my_edge_betweenness = nx.edge_betweenness_centrality(G)
    most_valuable_edge = max(G.edges(), key=my_edge_betweenness.get)
    G.remove_edge(*most_valuable_edge)
    my_partition = list(nx.connected_components(G))
    partition_sequence.append(my_partition)


# In[41]:


len(partition_sequence), nx.karate_club_graph().number_of_edges()


# In[42]:


len(partition_sequence[0])


# In[43]:


len(partition_sequence[-1]), nx.karate_club_graph().number_of_nodes()


# In[44]:


G = nx.karate_club_graph()
modularity_sequence = [modularity(G, p) for p in partition_sequence]
modularity_sequence


# In[45]:


import matplotlib.pyplot as plt
plt.plot(modularity_sequence)
plt.ylabel('Modularity')
plt.xlabel('Algorithm step')


# In[46]:


def my_modularity(partition):
    return nx.community.quality.modularity(G, partition)
best_partition = max(partition_sequence, key=my_modularity)


# In[47]:


best_partition


# In[48]:


def create_partition_map(partition):
    partition_map = {}
    for idx, cluster_nodes in enumerate(partition):
        for node in cluster_nodes:
            partition_map[node] = idx
    return partition_map


# In[49]:


best_partition_map = create_partition_map(best_partition)

node_colors = [best_partition_map[n] for n in G.nodes()]
nx.draw(G, with_labels=True, node_color=node_colors)


# In[50]:


nx.community.quality.modularity(G, best_partition)


# In[51]:


for partition in partition_sequence:
    if len(partition) == 2:
        two_cluster_partition = partition
        break

two_cluster_partition


# In[52]:


two_cluster_partition_map = create_partition_map(two_cluster_partition)

node_colors = [two_cluster_partition_map[n] for n in G.nodes()]
nx.draw(G, with_labels=True, node_color=node_colors)


# In[53]:


nx.community.quality.modularity(G, two_cluster_partition)


# In[54]:


import matplotlib.pyplot as plt

pos = nx.layout.spring_layout(G)
fig = plt.figure(figsize=(15, 6))

plt.subplot(1, 2, 1)
two_cluster_partition_map = create_partition_map(two_cluster_partition)
node_colors = [two_cluster_partition_map[n] for n in G.nodes()]
nx.draw(G, with_labels=True, node_color=node_colors, pos=pos)
plt.title('Predicted communities')

plt.subplot(1, 2, 2)
node_colors = [G.nodes[n]['club'] == 'Officer' for n in G.nodes()]
nx.draw(G, with_labels=True, node_color=node_colors, pos=pos)
plt.title('Actual communities')


# In[55]:


G.nodes[8]


# In[56]:


list(nx.community.girvan_newman(G))[:5]

