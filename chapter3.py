#!/usr/bin/env python
# coding: utf-8

# In[1]:


import networkx as nx


# In[2]:


max([13434,34,443,33,434])


# In[4]:


max(['ahmed', 'mohsan', 'tarak'])


# In[5]:


max(['ahmed', 'mohsan', 'tarak'],key =len)


# In[9]:


G=nx.Graph()
G.add_nodes_from(['a','b','c','d','e','f','j'])
G.add_edges_from([('a','b'),('b','c'),('a','c'),('a','d'),('d','e'),('e','f'),('f','d'),('f','j')])
nx.draw(G,with_labels=True,node_color='red',node_size=1800,font_color='white',font_size=25)


# In[10]:


highest_degree_node = max(G.nodes, key=G.degree)
highest_degree_node


# In[11]:


G.degree(highest_degree_node)


# In[12]:


betweenness = nx.centrality.betweenness_centrality(G)
highest_betweenness_node = max(G.nodes, key=betweenness.get)
highest_betweenness_node


# In[13]:


betweenness[highest_betweenness_node]


# In[20]:


import statistics

print('Mean degree:', statistics.mean(degree_sequence))
print('Median degree:', statistics.median(degree_sequence))


# In[21]:


betweenness = nx.centrality.betweenness_centrality(G)
betweenness_sequence = list(betweenness.values())

print('Mean betweenness:', statistics.mean(betweenness_sequence))
print('Median betweenness:', statistics.median(betweenness_sequence))


# In[25]:


min_degree, max_degree = min(degree_counts.keys()), max(degree_counts.keys())

plot_x = list(range(min_degree, max_degree + 1))


# In[19]:


degree_sequence = [G.degree(n) for n in G.nodes]


# In[23]:




from collections import Counter

degree_counts = Counter(degree_sequence)
degree_counts


# In[26]:


plot_y = [degree_counts.get(x, 0) for x in plot_x]


# In[27]:


import matplotlib.pyplot as plt

plt.bar(plot_x, plot_y)


# In[28]:


counts, bins, patches = plt.hist(betweenness_sequence, bins=10)


# In[29]:


bins


# In[30]:


nx.connected_components(G)


# In[31]:


core = next(nx.connected_components(G))
core


# In[32]:


len(core)


# In[33]:


components = list(nx.connected_components(G))


# In[34]:


len(components)


# In[35]:


C = G.copy()


# In[36]:


import random

nodes_to_remove = random.sample(list(C.nodes), 2)
C.remove_nodes_from(nodes_to_remove)


# In[39]:


number_of_steps = 5
M = G.number_of_nodes() // number_of_steps
M


# In[40]:


num_nodes_removed = range(0, G.number_of_nodes(), M)


# In[41]:


N = G.number_of_nodes()
C = G.copy()
random_attack_core_proportions = []
for nodes_removed in num_nodes_removed:
    # Measure the relative size of the network core
    core = next(nx.connected_components(C))
    core_proportion = len(core) / N
    random_attack_core_proportions.append(core_proportion)
    
    # If there are more than M nodes, select M nodes at random and remove them
    if C.number_of_nodes() > M:
        nodes_to_remove = random.sample(list(C.nodes), M)
        C.remove_nodes_from(nodes_to_remove)


# In[42]:


plt.title('Random failure')
plt.xlabel('Number of nodes removed')
plt.ylabel('Proportion of nodes in core')
plt.plot(num_nodes_removed, random_attack_core_proportions, marker='o')


# In[43]:


nodes_sorted_by_degree = sorted(G.nodes, key=G.degree, reverse=True)
top_degree_nodes = nodes_sorted_by_degree[:M]
top_degree_nodes


# In[ ]:




